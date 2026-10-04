#!/usr/bin/env python3
"""Cycle 189 hunt: shuffle_seed=20261189; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md codebook order + Random(20261189)):
power_plants_grid, bridges_roads, water, building_materials, lithium, wind,
balsa, rail, fission_smr, port_ownership, engineering_epc, port_cranes, solar,
copper, other_renewables, niobium, graphite, nickel.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (catalog dense; holdovers unsigned).
≥1/3 U.S. hunt budget spent on USTDA/DFC/EXIM/NADBank/AES/Atlas/Fluor/Bechtel/
Black & Veatch/Chevron/Progress/Wabtec — 2 new U.S. rows logged (BV Andes AET;
Fluor ICA-Mexico JV divestiture).
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


# 1. power_plants_grid / us — Black & Veatch Andes Energy Terminal USTDA FS (Colombia)
row_doc(
    "black_veatch_andes_aet_ustda_2021",
    "energy",
    "power_plants_grid",
    "us",
    "Black & Veatch — Andes Energy Terminal LNG + 400 MW gas power FS (USTDA)",
    "Colombia",
    "3 Jun 2021 Black & Veatch: selected for technical/engineering/commercial feasibility studies of Andes Energy Terminal (AET) on Aguadulce Peninsula, Buenaventura — LNG regasification plus Phase I 270 MW simple-cycle gas turbine upgrading to 400 MW combined-cycle in Phase II; studies funded by USTDA grant. CapEx USD blank (study award; plant CapEx not disclosed on company page). U.S. EPC/consulting presence.",
    "",
    "",
    "2021",
    "3.88",
    "-77.08",
    "Aguadulce Peninsula, Buenaventura Bay, Valle del Cauca, Colombia (company geography; approximate Aguadulce pin).",
    "bv_andes_aet_ustda_20210603",
    "Black & Veatch … has been selected to conduct the technical, engineering and commercial studies of the Andes Energy Terminal (AET) located in the Aguadulce Peninsula in Buenaventura, Colombia. … The feasibility studies, which are funded by a grant from the United States Trade and Development Agency (USTDA)",
    "https://www.bv.com/news/black-and-veatch-to-conduct-feasibility-studies-for-andes-energy-terminal-an",
    "Actor: Black & Veatch (U.S.) — us. Company English press; USTDA-funded FS. CapEx blank. Shuffle power_plants_grid; ≥1/3 U.S. hunt budget.",
    "hunt_cycle189",
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Black & Veatch. “Black & Veatch to Conduct Feasibility Studies for Andes Energy Terminal, an LNG Terminal and Power Plant Project in Buenaventura, Colombia.” June 3, 2021. https://www.bv.com/news/black-and-veatch-to-conduct-feasibility-studies-for-andes-energy-terminal-an.',
    annotation="BV: Andes AET USTDA FS; CapEx blank. Supports black_veatch_andes_aet_ustda_2021.",
    evid_note="Opened Black & Veatch English press 2026-10-04.",
)

# 2. bridges_roads / other — MOPC PY04 Lote 1 Acaray G. 242.296m
row_doc(
    "mopc_py04_acaray_lote1_242296m_pyg_2025",
    "infrastructure",
    "bridges_roads",
    "other",
    "MOPC — PY04 Pilar–Humaitá Lote 1 (Constructora Acaray)",
    "Paraguay",
    "4 Nov 2025 MOPC: signs contracts for second national rigid-pavement route on PY04; Lote 1 Pilar–Boquerón–Humaitá (33.6 km) awarded to Constructora Acaray S.A. for G. 242.296 million; includes fiber-reinforced concrete pavement and bridge reinforcement over arroyos Hondo and Paso Cornelio. CapEx = PYG 242,296,000,000 face (PYG stored without FX). DNCP licitación 461867 total award G. 446,437,609,809 published 15 Nov 2025. Paraguayan contractor — other.",
    "242296000000",
    "2025-11-04",
    "2025",
    "-26.87",
    "-58.30",
    "PY04 Pilar–Boquerón–Humaitá corridor, Ñeembucú, Paraguay (MOPC geography; approximate Pilar pin).",
    "mopc_py04_hormigon_20251104",
    "El Lote 1 fue adjudicado a Constructora Acaray S.A por G. 242.296 millones, mientras que el Lote 2 quedó a cargo del Consorcio Caminos del Sur, integrado por Benito Roggio e Hijos y Heisecke S.A.",
    "https://mopc.gov.py/firman-contratos-y-se-pone-en-marcha-la-construccion-de-la-segunda-ruta-de-hormigon-del-pais/",
    "Actor: Constructora Acaray (Paraguay) via MOPC — other. Official MOPC Spanish press + DNCP total cross-check. Shuffle bridges_roads.",
    "hunt_cycle189",
    investment_type="epc",
    evidence="documented",
    currency="PYG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Ministerio de Obras Públicas y Comunicaciones (MOPC). “Firman contratos y se pone en marcha la construcción de la segunda ruta de hormigón del país.” November 4, 2025. https://mopc.gov.py/firman-contratos-y-se-pone-en-marcha-la-construccion-de-la-segunda-ruta-de-hormigon-del-pais/.',
    annotation="MOPC: PY04 Lote 1 Acaray G. 242.296m. Supports mopc_py04_acaray_lote1_242296m_pyg_2025.",
    evid_note="Opened MOPC Spanish contract-signing press 2026-10-04; DNCP award total cross-checked.",
)

# 3. bridges_roads / allied — MOPC PY04 Lote 2 Caminos del Sur (Benito Roggio AR)
row_doc(
    "mopc_py04_caminos_sur_lote2_204140m_pyg_2025",
    "infrastructure",
    "bridges_roads",
    "allied",
    "MOPC — PY04 Humaitá–Paso de Patria Lote 2 (Consorcio Caminos del Sur / Benito Roggio)",
    "Paraguay",
    "4 Nov 2025 MOPC: Lote 2 Humaitá–Paso de Patria (~25 km) awarded to Consorcio Caminos del Sur (Benito Roggio e Hijos + Heisecke S.A.) for G. 204.140 million; part of ~60 km second national hormigón route on PY04 with bridge reinforcement. CapEx = PYG 204,140,000,000 face (PYG stored without FX). Argentine Benito Roggio lead — allied. Distinct from Acaray Lote 1 row.",
    "204140000000",
    "2025-11-04",
    "2025",
    "-27.07",
    "-58.50",
    "PY04 Humaitá–Paso de Patria corridor, Ñeembucú, Paraguay (MOPC geography; approximate Humaitá pin).",
    "mopc_py04_hormigon_20251104",
    "El Lote 1 fue adjudicado a Constructora Acaray S.A por G. 242.296 millones, mientras que el Lote 2 quedó a cargo del Consorcio Caminos del Sur, integrado por Benito Roggio e Hijos y Heisecke S.A.",
    "https://mopc.gov.py/firman-contratos-y-se-pone-en-marcha-la-construccion-de-la-segunda-ruta-de-hormigon-del-pais/",
    "Actor: Consorcio Caminos del Sur (Benito Roggio Argentina + Heisecke) via MOPC — allied. Official MOPC Spanish press. Shuffle bridges_roads.",
    "hunt_cycle189",
    investment_type="epc",
    evidence="documented",
    currency="PYG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Ministerio de Obras Públicas y Comunicaciones (MOPC). “Firman contratos y se pone en marcha la construcción de la segunda ruta de hormigón del país.” November 4, 2025. https://mopc.gov.py/firman-contratos-y-se-pone-en-marcha-la-construccion-de-la-segunda-ruta-de-hormigon-del-pais/.',
    annotation="MOPC: PY04 Lote 2 Caminos del Sur G. 204.140m. Supports mopc_py04_caminos_sur_lote2_204140m_pyg_2025.",
    evid_note="Opened MOPC Spanish contract-signing press 2026-10-04 (same page as Lote 1).",
)

# 4. building_materials / other — Votorantim Brazil plan progress R$3.1bn invested
row_doc(
    "votorantim_brazil_plan_3p1bn_invested_2026",
    "infrastructure",
    "building_materials",
    "other",
    "Votorantim Cimentos — Brazil 2024–28 CapEx plan progress (R$3.1bn invested)",
    "Brazil",
    "13 Aug 2026 Votorantim Cimentos 2Q26 results: of the R$5 billion Brazil investment plan for 2024–2028, R$3.1 billion has already been invested in previously announced projects; July also announced R$260m Xambioá grinding line (+500 ktpy to 1.5 Mtpy from Jul 2028). CapEx progress face = R$3.1bn cumulative invested (BRL stored without FX). Distinct from votorantim_brazil_plan_2p7bn_invested_2025 and site-level xambioa row.",
    "3100000000",
    "2026-08-13",
    "2026",
    "",
    "",
    "Multi-site Brazil cement CapEx plan — lat/lon blank (portfolio progress).",
    "votorantim_2q2026_results_20260813",
    "Our R$5 billion investment plan for Brazil for the period 2024 to 2028 continues to be implemented, with R$3.1 billion being invested in projects previously announced.",
    "https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/",
    "Actor: Votorantim Cimentos (Brazil) — other. Company English 2Q26 results. Shuffle building_materials.",
    "hunt_cycle189",
    investment_type="other",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Votorantim Cimentos. “Our Financial Results in the Second Quarter of 2026.” August 13, 2026. https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/.',
    annotation="Votorantim: Brazil plan R$3.1bn invested of R$5bn. Supports votorantim_brazil_plan_3p1bn_invested_2026.",
    evid_note="Opened Votorantim Cimentos English 2Q26 results page 2026-10-04.",
)

# 5. building_materials / allied — Holcim ASPI cash price S/1,850.37m (Pacasmayo control)
row_doc(
    "holcim_pacasmayo_aspi_1850370k_pen_2026",
    "infrastructure",
    "building_materials",
    "allied",
    "Holcim — cash purchase of Inversiones ASPI (50.01% Cementos Pacasmayo)",
    "Peru",
    "30 Mar 2026 Holcim Schedule 13D: consummates purchase of 99.99% of Inversiones ASPI S.A. (holder of 50.01% of Cementos Pacasmayo) for aggregate cash S/1,850,370,000 funded from Holcim working capital; SPA dated 15 Dec 2025. CapEx/consideration = PEN 1,850,370,000 face (PEN stored without FX). Distinct from holcim_pacasmayo_peru_2025 ~USD 1.5bn EV agreement row and completion PR without cash figure.",
    "1850370000",
    "2026-03-30",
    "2026",
    "-7.40",
    "-79.55",
    "Cementos Pacasmayo northern Peru cement system (Pacasmayo / Piura / Rioja plants; approximate Pacasmayo pin).",
    "holcim_cpac_schedule13d_20260406",
    "Holcim agreed to acquire from the Sellers 99.99% of the issued and outstanding shares of common stock of Inversiones … in exchange for an aggregate cash purchase price of S/1,850,370,000 (the “Inversiones Acquisition”). The Inversiones Acquisition was consummated on March 30, 2026.",
    "https://www.sec.gov/Archives/edgar/data/1221029/0001104659-26-039944.txt",
    "Actor: Holcim (Swiss) — allied. SEC Schedule 13D text. Shuffle building_materials.",
    "hunt_cycle189",
    investment_type="ownership_equity",
    evidence="documented",
    currency="PEN",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Holcim Ltd. Schedule 13D relating to Cementos Pacasmayo S.A.A. April 6, 2026. https://www.sec.gov/Archives/edgar/data/1221029/0001104659-26-039944.txt.',
    annotation="Holcim: ASPI cash S/1,850.37m for Pacasmayo control. Supports holcim_pacasmayo_aspi_1850370k_pen_2026.",
    evid_note="Opened SEC Schedule 13D complete submission text 2026-10-04.",
)

# 6. engineering_epc / us — Fluor divests ICA-Fluor Daniel Mexico JV USD 175m
row_doc(
    "fluor_ica_mexico_divest_175m_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Fluor — divests equity stake in ICA-Fluor Daniel (Mexico) to ICA",
    "Mexico",
    "16 Jul 2026 Fluor: divests equity stake in ICA-Fluor Daniel JV to partner ICA for USD 175 million; JV founded 1993 supported Mexico oil & gas, power, mining and manufacturing EPC; Fluor retains ability to support ICA project-by-project. Consideration = USD 175m. U.S. EPC presence recalibration in Mexico.",
    "175000000",
    "2026-07-16",
    "2026",
    "",
    "",
    "ICA-Fluor Daniel Mexico JV portfolio — lat/lon blank (nationwide JV exit).",
    "fluor_ica_divest_20260716",
    "Fluor Corporation (NYSE: FLR) announced today that it has divested its equity stake in ICA-Fluor Daniel to its existing JV Partner, ICA for $175 million.",
    "https://newsroom.fluor.com/news-releases/news-details/2026/Fluor-Divests-Equity-Stake-in-Mexico-JV/default.aspx",
    "Actor: Fluor (U.S.) — us. Company newsroom English release. Shuffle engineering_epc; ≥1/3 U.S. hunt budget.",
    "hunt_cycle189",
    investment_type="ownership_equity",
    evidence="documented",
    currency="USD",
    value_usd="175000000",
    fx_usd="1",
    bib_type="company",
    chicago='Fluor Corporation. “Fluor Divests Equity Stake in Mexico JV.” July 16, 2026. https://newsroom.fluor.com/news-releases/news-details/2026/Fluor-Divests-Equity-Stake-in-Mexico-JV/default.aspx.',
    annotation="Fluor: ICA-Fluor Daniel Mexico JV exit USD 175m. Supports fluor_ica_mexico_divest_175m_2026.",
    evid_note="Opened Fluor English newsroom release 2026-10-04.",
)

# 7. wind / other — Terralia El Chorro CFE mixed-scheme award (CapEx blank)
row_doc(
    "terralia_el_chorro_cfe_2026",
    "energy",
    "wind",
    "other",
    "Terralia Energía y Campo — El Chorro wind (CFE esquema mixto award)",
    "Mexico",
    "5 Jun 2026 CFE primera convocatoria esquemas de desarrollo mixto: awards El Chorro wind central to Terralia Energía y Campo (listed on Proyectos México / SENER public award tables for Noreste zone). CapEx USD blank on opened official portal (press ~USD 1bn UNVERIFIED — not used). Mexican developer — other.",
    "",
    "",
    "2026",
    "24.27",
    "-98.80",
    "El Chorro wind project, Tamaulipas / Noreste CFE zone, Mexico (award geography; approximate Tamaulipas wind belt pin).",
    "proyectos_mexico_cfe_mixto_el_chorro_2026",
    "Central | Adjudicatario … El Chorro | Terralia Energía y Campo",
    "https://www.proyectosmexico.gob.mx/proyectos/plan-de-fortalecimiento-y-expansion-del-sistema-electrico-nacional-generacion/",
    "Actor: Terralia Energía y Campo (Mexico) via CFE mixed scheme — other. Official Proyectos México / SENER public table. CapEx blank. Shuffle wind.",
    "hunt_cycle189",
    investment_type="concession",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Proyectos México / Secretaría de Economía. “Plan de Fortalecimiento y Expansión del Sistema Eléctrico Nacional: Generación” (CFE esquema mixto award table listing El Chorro — Terralia Energía y Campo). Accessed October 4, 2026. https://www.proyectosmexico.gob.mx/proyectos/plan-de-fortalecimiento-y-expansion-del-sistema-electrico-nacional-generacion/.',
    annotation="CFE mixto: El Chorro awarded to Terralia; CapEx blank. Supports terralia_el_chorro_cfe_2026.",
    evid_note="Opened Proyectos México public generation/CFE mixto page 2026-10-04.",
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

    for row, evid, bib_e in ITEMS:
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
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle189 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
