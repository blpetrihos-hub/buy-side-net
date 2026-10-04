#!/usr/bin/env python3
"""Cycle 203 hunt: shuffle_seed=20261203; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261203).shuffle):
lithium, port_ownership, graphite, niobium, bridges_roads, water, nickel,
balsa, rail, wind, copper, power_plants_grid, fission_smr, solar,
other_renewables, engineering_epc, port_cranes, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES/Freeport/EXIM/DFC/Fluence/Bechtel/
Progress Rail/Wabtec/SSA/USTDA/EnergyX/Albemarle sweeps (catalog dense; 0 new
U.S. rows). PRC equal-budget: CAMC/Zijin/PowerChina/ZPMC/CRIG TAM-TSB already
logged — miss.
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
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
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
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


# 1. port_ownership / other — Hutchison Ports LCT Lázaro Phase III >USD 220m
row_doc(
    "hutchison_lct_lazaro_phase3_220m_2023",
    "infrastructure",
    "port_ownership",
    "other",
    "Hutchison Ports LCT — Lázaro Cárdenas TEC I Phase III expansion",
    "Mexico",
    "25 Oct 2023 Hutchison Ports México: Phase III expansion of specialized container Terminal I at Puerto de Lázaro Cárdenas — investment of more than USD 220 million; +345 m quay (to 1,275 m total) and +28.3 ha yard (to 105 ha); capacity from 1.3m to 2.0m TEU; terminal then planned for 25 RTG + 10 QC. Distinct from apmt_lazaro_phase3_350m_2026 (APM Terminals Phase III at same port) and zpmc_hutchison_lazaro_12artg_2026 (ZPMC ARTG delivery into this Phase III).",
    "220000000",
    "2023-10-25",
    "2023",
    "17.95",
    "-102.17",
    "Hutchison Ports LCT / TEC I, Port of Lázaro Cárdenas, Michoacán (company geography).",
    "hutchison_lct_lazaro_phase3_20231025",
    "Con una inversión de más de 220 millones de dólares, Hutchison Ports LCT conmemora un hito significativo con la ampliación del 50% del área de cesión de la Terminal Especializada de Contenedores I, ubicada en el Puerto de Lázaro Cárdenas, Michoacán. La Fase III se centrará en la construcción de 345 metros de muelle y expandirá el área en 28.3 hectáreas.",
    "https://hutchisonports.com.mx/newsroom/hutchison-ports-lct-ce",
    "Actor: Hutchison Ports (CK Hutchison / Hong Kong) — other (HK coding convention; not PRC). Company Spanish primary. CapEx floor >USD 220m. Shuffle port_ownership.",
    "hunt_cycle203",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="220000000",
    fx_usd="1",
    bib_type="company",
    chicago='Hutchison Ports México. “Hutchison Ports LCT celebra la ampliación del 50% de su terminal en Lázaro Cárdenas.” October 25, 2023. https://hutchisonports.com.mx/newsroom/hutchison-ports-lct-ce.',
    annotation="Hutchison LCT Lázaro Phase III: >USD 220m. Supports hutchison_lct_lazaro_phase3_220m_2023.",
    evid_note="Opened Hutchison Ports México Spanish company primary 2026-10-04; >USD 220m / +345 m quay / +28.3 ha confirmed.",
)

# 2. bridges_roads / allied — OHLA/Ashmore/Ethuss Accesos Norte Fase II financial close
row_doc(
    "ohla_accesos_norte_fase2_1p7tn_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "OHLA / Ashmore / Ethuss — Accesos Norte Fase II 5G (Bogotá)",
    "Colombia",
    "11 Sep 2026 ANI: Proyecto 5G Accesos Norte Fase II reaches financial close — COP $1.2 trillion credit contracts (FDN, JPMorgan, MUFG) enabling construction start; concessionaire Ruta Bogotá Norte S.A. (Ashmore / Grupo Ethuss / OHLA); investment COP $1.7 trillion (CapEx + Opex, Dec 2024); 17.96 km including Autopista Norte Calle 191–245, Carrera Séptima, and Perimetral de Sopó; construction ~66 months; works targeted end-2031. OHLA English twin (17 Sep 2026) cites ~€900m investment and ~€325m financing. CapEx+Opex = COP 1.7tn (ANI primary).",
    "1700000000000",
    "2026-09-11",
    "2026",
    "4.76",
    "-74.05",
    "Autopista Norte / Sabana Centro corridor, Bogotá–Chía–Cajicá–Sopó (ANI geography; approximate north Bogotá pin).",
    "ani_accesos_norte_fase2_20260911",
    "La Agencia Nacional de Infraestructura (ANI) fortalece la confianza inversionista con el cierre financiero del proyecto 5G Accesos Norte Fase II, que aseguró recursos por $1,2 billones mediante la formalización de los contratos de crédito requeridos para respaldar su ejecución. … El proyecto 5G Accesos Norte Fase II cuenta con una inversión de $1,7 billones (Capex y Opex dic. 2024), y una longitud de 17,96 kilómetros.",
    "https://www.ani.gov.co/w/proyecto-5g-accesos-norte-fase-ii-asegura-financiaci%C3%B3n-por-1-2-billones",
    "Actor: OHLA (Spain) with Ashmore (UK) / Grupo Ethuss (Colombia) — allied (Spanish constructor + UK PE). ANI Spanish government primary. Value = COP 1.7tn CapEx+Opex (BRL-style local currency stored without FX). Shuffle bridges_roads.",
    "hunt_cycle203",
    investment_type="concession",
    evidence="documented",
    currency="COP",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Agencia Nacional de Infraestructura (ANI). “Proyecto 5G Accesos Norte Fase II asegura financiación por $1,2 billones.” September 11, 2026. https://www.ani.gov.co/w/proyecto-5g-accesos-norte-fase-ii-asegura-financiaci%C3%B3n-por-1-2-billones.',
    annotation="ANI Accesos Norte Fase II: COP 1.7tn CapEx+Opex / COP 1.2tn FC. Supports ohla_accesos_norte_fase2_1p7tn_2026.",
    evid_note="Opened ANI Spanish government primary 2026-10-04; COP 1.7tn / 17.96 km / Ashmore–Ethuss–OHLA confirmed. OHLA English twin also opened (€900m / €325m).",
)

# 3. port_cranes / allied — Konecranes Transtec World 2× E-ACE electric empty handlers (Santos)
row_doc(
    "konecranes_transtec_eace_santos_2026",
    "infrastructure",
    "port_cranes",
    "allied",
    "Konecranes — 2× E-ACE 7/8 ECC 90 electric empty container handlers (Transtec World / Santos)",
    "Brazil",
    "14 Apr 2026 Konecranes: Transtec World becomes first operator in the Americas to adopt Konecranes electric empty container handlers — two E-ACE 7/8 ECC 90 units for Transtec’s Port of Santos container depot (eight yards; >710,000 containers/year); order placed Q4 2025 with Q2 2026 delivery; high-voltage electric empty handlers with TRUCONNECT remote monitoring; local distributor Equiport. CapEx not disclosed on company primary. Distinct from konecranes_portonave_rtg_2025 / konecranes_cartagena_rtg_2025 / other Konecranes LatAm RTG/MHC rows.",
    "",
    "",
    "2026",
    "-23.95",
    "-46.33",
    "Transtec World container depot, Port of Santos, São Paulo (company geography; approximate Santos pin).",
    "konecranes_transtec_eace_20260414",
    "Two Konecranes E-ACE 7/8 ECC 90 electric empty container handlers will operate across Transtec World’s container depot at the Port of Santos in Brazil, marking the first deployment of Konecranes electric empty container handlers in the Americas. The order was placed In Q4 2025, with delivery planned during Q2 2026.",
    "https://www.konecranes.com/press-releases/transtec-world-becomes-first-operator-in-the-americas-to-adopt-konecranes-electric-empty-container-handlers",
    "Actor: Konecranes (Finland) — allied. Company English primary (Portuguese twin also opened). CapEx blank (OEM award without disclosed USD). Shuffle port_cranes.",
    "hunt_cycle203",
    investment_type="equipment_supply",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Konecranes. “Transtec World becomes first operator in the Americas to adopt Konecranes electric empty container handlers.” April 14, 2026. https://www.konecranes.com/press-releases/transtec-world-becomes-first-operator-in-the-americas-to-adopt-konecranes-electric-empty-container-handlers.',
    annotation="Konecranes Transtec Santos 2× E-ACE: CapEx blank. Supports konecranes_transtec_eace_santos_2026.",
    evid_note="Opened Konecranes English company primary 2026-10-04; 2× E-ACE / Santos / Americas-first confirmed; CapEx undisclosed.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    updated = []

    for row, evid, bib_e in ITEMS:
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
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle203 added {len(added)}: {added}")
    print(f"cycle203 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
