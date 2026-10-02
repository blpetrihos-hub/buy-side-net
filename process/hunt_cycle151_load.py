#!/usr/bin/env python3
"""Cycle 151 hunt: shuffle_seed=20261151; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: graphite, copper, other_renewables, engineering_epc,
fission_smr, water, building_materials, port_cranes, bridges_roads, rail,
niobium, wind, power_plants_grid, solar, balsa, nickel, lithium, port_ownership.

PRC ahead by 13 after 150 — keep equal US/PRC budget without padding.
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


# 1. other_renewables / us — AES Gener–Google 440 GWh/y hybrid PPA (2019)
row_doc(
    "aes_andes_google_440gwh_ppa_2019",
    "energy",
    "other_renewables",
    "us",
    "AES Gener / AES Andes — Google Quilicura hybrid renewable PPA (440 GWh/y)",
    "Chile",
    "9 Dec 2019 AES Andes: AES Gener signs long-term renewable supply contract with Google — 440 GWh/year for 14 years to supply expansion of Google’s Quilicura data center (Santiago), Google’s first LatAm data center; supply from Andes Solar expansion and Los Olmos wind (Biobío); first hybrid solar+wind PPA Google signed worldwide; Google cites adding 125 MW renewable capacity. CapEx blank (offtake/PPA). Distinct from aes_andes_los_olmos_110mw_cod_2022 (COD of wind supply) and aes_andes_microsoft_chile_ppa_2022.",
    "",
    "",
    "2019",
    "-33.365",
    "-70.735",
    "Google Quilicura data center / AES Gener renewable portfolio (Andes Solar + Los Olmos), Chile (AES offtake naming).",
    "aes_andes_google_ppa_20191209",
    "El acuerdo, que contempla la venta de 440 GWh al año de energía renovable por un plazo de 14 años y que abastecerá la ampliación del … primer y único centro de datos de Google en América Latina que está ubicado en la comuna de Quilicura, Santiago… La energía provendrá de la ampliación de Andes Solar y de la construcción del proyecto eólico Los Olmos… El acuerdo de suministro entre AES Gener y Google, es el primer contrato de tecnología híbrida -que incorpora energía solar y eólicos- que Google suscribe a nivel mundial.",
    "https://www.aesandes.com/en/press-release/aes-gener-y-google-firman-historico-contrato-de-energia-renovable",
    "Actor: AES Gener / AES Andes / AES Corporation (U.S.) — us. Company Spanish primary for offtake volume + hybrid structure. CapEx blank (PPA).",
    "hunt_energy_other_renewables",
    investment_type="offtake",
    chicago='AES Andes. “AES Gener y Google firman histórico contrato de energía renovable.” December 9, 2019. https://www.aesandes.com/en/press-release/aes-gener-y-google-firman-historico-contrato-de-energia-renovable.',
    annotation="AES Andes: Google Quilicura 440 GWh/y 14-year hybrid PPA. Supports aes_andes_google_440gwh_ppa_2019.",
    evid_note="Opened AES Andes Google hybrid PPA primary (440 GWh/y; CapEx blank).",
)

# 2. other_renewables / us — AES Andes–Teck QB2 1,069 GWh/y renewable PPA
row_doc(
    "aes_andes_teck_qb2_1069gwh_2022",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Teck Quebrada Blanca Phase 2 renewable PPA (1,069 GWh/y)",
    "Chile",
    "10 Nov 2022 AES Andes / Teck: Chilean affiliates enter 17-year clean power purchase agreement for Quebrada Blanca Phase 2 (QB2); AES Andes to provide 1,069 GWh/year from renewable portfolio (wind, solar, hydro, batteries) to achieve 100% clean renewable energy for QB2 from 2025; builds on Feb 2020 QB2 renewable announcement. CapEx blank (offtake/PPA; terms confidential). Distinct from bechtel_qb2_desal_chile and aes_andes_codelco_ppa_1p6twh_2023.",
    "",
    "",
    "2022",
    "-20.930",
    "-68.850",
    "Quebrada Blanca Phase 2 / Tarapacá Region, Chile (AES–Teck offtake naming).",
    "aes_andes_teck_qb2_ppa_20221110",
    "Under the 17-year agreement, AES Andes will provide 1,069 Gigawatt hours per year (“GWh/year”) of energy from renewable sources, building on the February 2020 QB2 renewable energy announcement to achieve 100% clean, renewable energy for QB2 starting in 2025. AES Andes uses its growing renewable portfolio that includes wind, solar, hydro and battery plants to supply clean energy to QB2.",
    "https://www.aesandes.com/en/press-release/teck-secures-100-clean-power-aes-andes-quebrada-blanca-phase-2",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for offtake volume. CapEx blank (PPA).",
    "hunt_energy_other_renewables",
    investment_type="offtake",
    chicago='AES Andes. “Teck Secures 100% Clean Power with AES Andes for Quebrada Blanca Phase 2.” November 10, 2022. https://www.aesandes.com/en/press-release/teck-secures-100-clean-power-aes-andes-quebrada-blanca-phase-2.',
    annotation="AES Andes: Teck QB2 1,069 GWh/y 17-year renewable PPA. Supports aes_andes_teck_qb2_1069gwh_2022.",
    evid_note="Opened AES Andes–Teck QB2 renewable PPA primary (1,069 GWh/y; CapEx blank).",
)

# 3. solar / prc — POWERCHINA San Carlos 18.3 MW PV EPC (Salta)
row_doc(
    "powerchina_san_carlos_18p3mw_salta_2024",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — San Carlos Photovoltaic Power Station EPC (18.3 MW, Salta)",
    "Argentina",
    "27 Mar 2024 POWERCHINA English: signed business contract 26 Mar for San Carlos Photovoltaic Power Station in Salta Province; POWERCHINA responsible for design, procurement of equipment and materials, construction, installation, and commissioning of an 18.3 MW photovoltaic power station. CapEx blank on opened page. Distinct from powerchina_cafayate_argentina_97p6mw_epc and powerchina_cauchari_solar_epc_2020.",
    "",
    "",
    "2024",
    "-25.890",
    "-65.960",
    "San Carlos, Salta Province, Argentina (POWERCHINA project naming; approximate municipal pin).",
    "powerchina_san_carlos_salta_20240327",
    "POWERCHINA signed a business contract for the San Carlos Photovoltaic Power Station project in Argentina on March 26. The San Carlos Photovoltaic Power Station project will be located in Salta Province in northern Argentina. POWERCHINA will be responsible for the design, procurement of equipment and materials, construction, installation, and commissioning of an 18.3-megawatt photovoltaic power station.",
    "https://en.powerchina.cn/2024-03/27/c_828683.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary for EPC scope + 18.3 MW. CapEx blank.",
    "hunt_energy_solar",
    investment_type="epc",
    chicago='POWERCHINA. “POWERCHINA to commence new solar power project in Argentina.” March 27, 2024. https://en.powerchina.cn/2024-03/27/c_828683.htm.',
    annotation="POWERCHINA: San Carlos Salta 18.3 MW PV EPC contract. Supports powerchina_san_carlos_18p3mw_salta_2024.",
    evid_note="Opened POWERCHINA San Carlos Salta EPC primary (18.3 MW; CapEx blank).",
)

# 4. other_renewables / prc — POWERCHINA (Sinohydro) El Tambolar 83.5 MW; USD 520m
row_doc(
    "powerchina_el_tambolar_520m_2019",
    "energy",
    "other_renewables",
    "prc",
    "POWERCHINA (Sinohydro) UTE — El Tambolar multipurpose hydro (83.5 MW)",
    "Argentina",
    "POWERCHINA Argentina Sucursal: El Tambolar multipurpose hydroenergy project on Río San Juan (San Juan Province); owned by San Juan Energy Company; installed capacity 2×41.75 MW (83.5 MW); POWERCHINA (Sinohydro), Panedile, SACDE and Peterson UTE; contract signed 3 Jul 2019 for USD 520 million; under execution at page publish. Distinct from powerchina_san_gaban_iii_peru_2025 and powerchina_ivirizu_bolivia_2025.",
    "520000000",
    "2019-07-03",
    "2019",
    "-31.450",
    "-68.950",
    "El Tambolar / Río San Juan, San Juan Province, Argentina (POWERCHINA Sucursal geography; approximate pin).",
    "powerchina_ar_el_tambolar",
    "El Aprovechamiento Hidroenergético Multipropósito El Tambolar se encuentra sobre el Río San Juan, en la provincia de San Juan… cuenta con una capacidad instalada de 2*41,75MW. POWERCHINA (Synohydro), Panedile, SACDE y peterson conformaron una UTE. El contrato del proyecto se firmo el 3 de julio d e2019, por un valor de U$S 520 millones.",
    "https://www.powerchina.com.ar/tambolar.html",
    "Actor: POWERCHINA / Sinohydro (PRC SOE) in UTE with local partners — prc (EPC lead). Company Argentina primary for capacity + USD 520m contract value.",
    "hunt_energy_other_renewables",
    investment_type="epc",
    chicago='POWERCHINA Ltd. Sucursal Argentina. “Central Hidroeléctrica El Tambolar.” https://www.powerchina.com.ar/tambolar.html.',
    annotation="POWERCHINA Argentina: El Tambolar 83.5 MW / USD 520m UTE contract. Supports powerchina_el_tambolar_520m_2019.",
    evid_note="Opened POWERCHINA Argentina El Tambolar primary (83.5 MW; USD 520m contract).",
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
    print(f"Cycle 151 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
