#!/usr/bin/env python3
"""Cycle 214 hunt: shuffle_seed=20261214; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261214).shuffle):
power_plants_grid, balsa, water, niobium, lithium, copper, engineering_epc,
fission_smr, building_materials, solar, wind, other_renewables, bridges_roads,
port_ownership, port_cranes, graphite, nickel, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Argentina Build the Future/
Freeport El Abra/Bechtel QB2 desal blank/Fluor Quellaveco/EnergyX/Nextracker/
Array Lupi/Wabtec/GE Vernova/USTDA Ecuador/Equinix sweeps (0 new U.S. rows —
catalog dense). PRC equal-budget: Goldwind Sento Sé / Envision Casa / Sungrow
BHP Escondida–Spence / PowerChina / CCCC El Barro already logged; holdovers
unsigned.
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


# 1. power_plants_grid / allied — CapEx-fill ENGIE Peru Grupo 1 to USD 339.36m
#    (ProInversión contract signing; Andina state agency primary)
row_doc(
    "engie_peru_grupo1_transmision_230m_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "ENGIE Energía Perú / ENGIE Transmisión Perú — Grupo 1 Plan de Transmisión 2025–2034 APP",
    "Peru",
    "2 Oct 2026: ProInversión and ENGIE Transmisión Perú S.A. sign four Grupo 1 transmission concession contracts (Enlace 500 kV Miguel Grau–Pariñas + SE Pariñas; Enlaces 220 kV Felam–Tierras Nuevas–Salitral; Nueva SE Palián 220/60 kV; Enlace 220 kV Muyurina–Mollepata) in Piura, Lambayeque, Junín and Ayacucho. CapEx-fill: Andina/ProInversión states investment superior to USD 339 million per adjudicatario offer (Gestión cites ProInversión ficha updated 15 Sep 2026 at USD 339.36 million; prior company buena-pro figure was USD 230.8m). COD targeted 2031; 30-year O&M from COD. Distinct from ENGIE Brasil Assú Sol / Asa Branca / ANEEL 01/2026 rows.",
    "339360000",
    "2026-10-02",
    "2026",
    "-5.19",
    "-80.63",
    "Piura / Miguel Grau–Pariñas 500 kV primary link pin (multi-department package; Piura corridor).",
    "andina_engie_grupo1_contratos_20261002",
    "El Grupo 1 representa una inversión superior a 339 millones de dólares, conforme a la oferta del adjudicatario, y es el resultado de un proceso de adjudicación muy competitivo en el que participaron y presentaron ofertas cuatro operadores de prestigio internacional.",
    "https://andina.pe/agencia/noticia-inician-ejecucion-cuatro-proyectos-electricos-beneficio-16-millones-peruanos-1094342.aspx",
    "Actor: ENGIE Energía Perú / ENGIE Transmisión Perú (France) — allied. CapEx-fill upgrade from USD 230.8m company offered amount to USD 339.36m (Andina/ProInversión contract-signing figure; Gestión cites ProInversión ficha USD 339.36m). Shuffle power_plants_grid.",
    "hunt_cycle214",
    investment_type="concession",
    evidence="documented",
    currency="USD",
    value_usd="339360000",
    fx_usd="1",
    bib_type="government",
    chicago='Agencia Andina. “Inician ejecución de cuatro proyectos eléctricos en beneficio de 1.6 millones de peruanos.” October 2, 2026. https://andina.pe/agencia/noticia-inician-ejecucion-cuatro-proyectos-electricos-beneficio-16-millones-peruanos-1094342.aspx.',
    annotation="ENGIE Peru Grupo 1 CapEx-fill >USD 339m / USD 339.36m. Supports engie_peru_grupo1_transmision_230m_2026.",
    evid_note="Opened Andina/ProInversión primary 2026-10-04; >USD 339m per adjudicatario offer / four Grupo 1 contracts signed 2 Oct 2026 / Piura–Lambayeque–Junín–Ayacucho / ENGIE Transmisión Perú confirmed. CapEx-fill uses USD 339.36m (Gestión ProInversión ficha detail).",
)

# 2. power_plants_grid / allied — ISA group FY2025 executed investments COP 6.3 trillion
row_doc(
    "isa_fy2025_invest_6p3tn_cop",
    "energy",
    "power_plants_grid",
    "allied",
    "ISA (Interconexión Eléctrica S.A. E.S.P.) — group FY2025 executed investments",
    "Colombia",
    "2 Mar 2026 ISA English results release: group executed investments of COP 6.3 trillion in 2025 (+31% vs 2024) across LatAm markets where it operates; also secured projects with ~USD 283 million investment and commissioned projects with CapEx USD 664 million (Cuestecitas–Copey–Fundación Colombia energization; Riacho Grande Brazil underground line highlighted). Forward five-year plan COP 25.5 trillion logged separately. CapEx face = COP 6.3tn group executed investments (energy transmission majority; also roads/telecom minority — descriptive group figure).",
    "6300000000000",
    "2026-03-02",
    "2025",
    "6.25",
    "-75.57",
    "ISA HQ Medellín, Colombia (group CapEx; multi-country LatAm footprint).",
    "isa_fy2025_results_20260302",
    "During 2025, ISA executed investments of COP 6.3 trillion, representing a 31% increase compared to 2024, consolidating its leadership in the countries where it operates. Over the next five years, the company plans to invest COP 25.5 trillion.",
    "https://isa.co/en/press/isa-2025-results-investment-growth-shareholder-value/",
    "Actor: ISA / Interconexión Eléctrica (Colombia; Ecopetrol group) — allied coding consistent with prior ISA Energía rows. Company English primary. CapEx = COP 6.3tn FY2025 executed group investments. USD blank (no Fed H.10 COP). Shuffle power_plants_grid.",
    "hunt_cycle214",
    investment_type="capex",
    evidence="documented",
    currency="COP",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ISA. “More investment, greater value: ISA closed 2025 with 31% investment growth and a 48% increase in its share price.” March 2, 2026. https://isa.co/en/press/isa-2025-results-investment-growth-shareholder-value/.',
    annotation="ISA FY2025 executed investments COP 6.3tn. Supports isa_fy2025_invest_6p3tn_cop.",
    evid_note="Opened ISA English primary 2026-10-04; COP 6.3tn executed 2025 / +31% / USD 283m secured / USD 664m commissioned / COP 25.5tn five-year plan confirmed.",
)

# 3. power_plants_grid / allied — ISA 2026–2030 investment plan COP 25.5 trillion
row_doc(
    "isa_capex_plan_25p5tn_2026_2030",
    "energy",
    "power_plants_grid",
    "allied",
    "ISA — LatAm investment plan 2026–2030",
    "Colombia",
    "2 Mar 2026 ISA English results release: over the next five years the company plans to invest COP 25.5 trillion across LatAm markets (Brazil/Colombia/Chile/Peru/Panama footprint). Press coverage attributes ~78% of the plan to electric transmission, with remainder roads/energy solutions/telecom. Distinct from isa_fy2025_invest_6p3tn_cop (executed 2025) and isa_energia_fy2025_capex_5p1bn_brl (Brazil subsidiary).",
    "25500000000000",
    "2026-03-02",
    "2026",
    "6.25",
    "-75.57",
    "ISA HQ Medellín, Colombia (multi-country LatAm plan pin).",
    "isa_fy2025_results_20260302",
    "During 2025, ISA executed investments of COP 6.3 trillion, representing a 31% increase compared to 2024, consolidating its leadership in the countries where it operates. Over the next five years, the company plans to invest COP 25.5 trillion.",
    "https://isa.co/en/press/isa-2025-results-investment-growth-shareholder-value/",
    "Actor: ISA (Colombia) — allied. Company English primary. CapEx plan face = COP 25.5tn 2026–2030. USD blank. Shuffle power_plants_grid.",
    "hunt_cycle214",
    investment_type="capex_plan",
    evidence="documented",
    currency="COP",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ISA. “More investment, greater value: ISA closed 2025 with 31% investment growth and a 48% increase in its share price.” March 2, 2026. https://isa.co/en/press/isa-2025-results-investment-growth-shareholder-value/.',
    annotation="ISA 2026–2030 CapEx plan COP 25.5tn. Supports isa_capex_plan_25p5tn_2026_2030.",
    evid_note="Opened ISA English primary 2026-10-04; COP 25.5tn five-year plan confirmed on same release as FY2025 COP 6.3tn.",
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
    print(f"cycle214 added {len(added)}: {added}")
    print(f"cycle214 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
