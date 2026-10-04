#!/usr/bin/env python3
"""Cycle 193 hunt: shuffle_seed=20261193; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261193).shuffle):
bridges_roads, copper, other_renewables, graphite, rail, port_cranes, lithium,
nickel, solar, balsa, niobium, fission_smr, wind, water, port_ownership,
power_plants_grid, building_materials, engineering_epc.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Equinix/SEC Freeport/EXIM/DFC/NADBank/AES/Atlas —
    4 new U.S. rows (Equinix MO2/RJ3/ST2/Bogotá CapEx lines).
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


# 1. bridges_roads / allied — Sacyr Segunda Concesión Ruta 68 USD 1.6bn
row_doc(
    "sacyr_ruta68_1600m_2025",
    "infrastructure",
    "bridges_roads",
    "allied",
    "Sacyr Concesiones Chile — Segunda Concesión Ruta 68 (Santiago–Valparaíso)",
    "Chile",
    "1 Jul 2025: Sacyr Concesiones begins operating Segunda Concesión Ruta 68 (~141 km Metropolitana–Valparaíso); planned investment USD 1,600 million (EUR 1,500 million). MOP Diario Oficial decree 9 May 2025 awarded Sacyr (UF 35,970,000 investment envelope; ~USD 1.6bn). New works (tunnels Lo Prado 3 / Zapata 3; lane widenings) targeted start ~2029 / ops ~2033; 30-year max variable term. Distinct from sacyr_ruta57_best_offer_2026 and sacyr_ruta_pie_de_monte_355m_2026.",
    "1600000000",
    "2025-07-01",
    "2025",
    "-33.40",
    "-71.20",
    "Ruta 68 Santiago–Valparaíso corridor, Chile (company/MOP geography; approximate mid-corridor pin).",
    "sacyr_ruta68_ops_20250702",
    "Sacyr Concesiones inició la operación de la segunda concesión de la Ruta 68 … Con una inversión prevista de 1.600 millones de dólares (1.500 millones de euros)",
    "https://sacyr.com/-/inicio-operaciones-ruta-68",
    "Actor: Sacyr Concesiones (Spain) — allied. Company Spanish primary; MOP decree corroborates UF 35.97m / ~USD 1.6bn. CapEx = USD 1.6bn. Shuffle bridges_roads.",
    "hunt_cycle193",
    investment_type="ppp_concession",
    evidence="documented",
    currency="USD",
    value_usd="1600000000",
    fx_usd="1",
    bib_type="company",
    chicago='Sacyr. “Sacyr toma el control de la operación de la concesión de la Ruta 68 en Chile.” July 2, 2025. https://sacyr.com/-/inicio-operaciones-ruta-68.',
    annotation="Sacyr: Ruta 68 Segunda Concesión USD 1.6bn. Supports sacyr_ruta68_1600m_2025.",
    evid_note="Opened Sacyr Spanish press 2026-10-04; MOP Diario Oficial / DGC pages corroborate UF 35.97m award.",
)

# 2. copper / other — Southern Copper board-approved 2026 CapEx USD 1,925.5m
row_doc(
    "southern_copper_capex_1925m_2026",
    "resources",
    "copper",
    "other",
    "Southern Copper (Grupo México) — 2026 capital investment program",
    "Mexico",
    "Southern Copper March 2026 IR presentation CapEx profile: 2026E SCC CapEx USD 1,925.5 million (Mexico USD 764.1m incl. El Pilar/El Arco; Peru USD 1,161.4m incl. Tía María USD 508.3m + current ops). Board-approved annual CapEx program spanning Mexico+Peru copper assets. Distinct from southern_copper_tia_maria_2025 project envelope and El Pilar / Ilo rows. Lat/lon blank (multi-site).",
    "1925500000",
    "2026-03-01",
    "2026",
    "",
    "",
    "Southern Copper Mexico + Peru copper CapEx program (IR presentation; multi-site — lat/lon blank).",
    "scc_ir_capex_mar2026",
    "Capital Expenditures … 2025 $1,325 … 2026E $1,925 … SCC 1,325.7 1,925.5 … Peru 524.6 1,161.4 … Tía María 117.1 508.3",
    "https://southerncoppercorp.com/wp-content/uploads/2026/03/pp260213.pdf",
    "Actor: Southern Copper / Grupo México — other (Mexican-controlled listed miner). Company English IR deck CapEx table. CapEx = USD 1,925.5m. Shuffle copper.",
    "hunt_cycle193",
    investment_type="capex_plan",
    evidence="documented",
    currency="USD",
    value_usd="1925500000",
    fx_usd="1",
    bib_type="company",
    chicago='Southern Copper Corporation. “Company Presentation” (March 2026). https://southerncoppercorp.com/wp-content/uploads/2026/03/pp260213.pdf.',
    annotation="SCC IR: 2026 CapEx USD 1,925.5m. Supports southern_copper_capex_1925m_2026.",
    evid_note="Opened SCC March 2026 IR PDF CapEx/Exhibit 1 table 2026-10-04; PublicNow 10-K excerpt corroborates Board approval of $1,925.5m.",
)

# 3. engineering_epc / us — Equinix MO2 Monterrey USD 81m
row_doc(
    "equinix_mo2_monterrey_81m_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Equinix — MO2 IBX data center phase 1 (Monterrey / Apodaca)",
    "Mexico",
    "30 Oct 2025 Equinix México: official opening of MO2 data center in Monterrey (Apodaca, Nuevo León); phase-1 investment USD 81 million; +720+ cabinets; total build-out expected ~USD 189 million. Distinct from CloudHQ Querétaro / Ascenty SPO rows.",
    "81000000",
    "2025-10-30",
    "2025",
    "25.78",
    "-100.19",
    "Equinix MO2, Apodaca / Monterrey, Nuevo León, Mexico (company geography; approximate Apodaca pin).",
    "equinix_mo2_monterrey_20251030",
    "Equinix … anunció la apertura oficial de su nuevo centro de datos MO2 en Monterrey, Nuevo León. Con una inversión de 81 millones de dólares, en esta primera fase, MO2 agrega más de 720 gabinetes … Se prevé que la nueva instalación tenga una inversión total de aproximadamente US$189 millones una vez construida.",
    "https://newsroom.equinix.com/2025-10-30-Equinix-Mexico-invierte-US-81-millones-en-nuevo-centro-de-datos-en-Monterrey",
    "Actor: Equinix (U.S. Nasdaq:EQIX) — us. Company Spanish newsroom. CapEx = USD 81m phase 1. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle193",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="81000000",
    fx_usd="1",
    bib_type="company",
    chicago='Equinix. “Equinix México invierte US$ 81 millones en nuevo centro de datos en Monterrey.” October 30, 2025. https://newsroom.equinix.com/2025-10-30-Equinix-Mexico-invierte-US-81-millones-en-nuevo-centro-de-datos-en-Monterrey.',
    annotation="Equinix: MO2 Monterrey USD 81m. Supports equinix_mo2_monterrey_81m_2025.",
    evid_note="Opened Equinix México Spanish newsroom 2026-10-04.",
)

# 4. engineering_epc / us — Equinix RJ3 Rio initial USD 45m
row_doc(
    "equinix_rj3_45m_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Equinix — RJ3 IBX data center phase 1 (Rio de Janeiro)",
    "Brazil",
    "26 May 2026 Equinix LatAm Portuguese newsroom summarizing 2025–26 CapEx: RJ3 data center in Rio de Janeiro with initial investment ~USD 45 million; first-phase capacity >550 cabinets. Part of Brazil USD 270m within regional USD 419m envelope (envelope not double-logged). Distinct from Ascenty SPO05/SPO06.",
    "45000000",
    "2025-01-01",
    "2025",
    "-22.91",
    "-43.17",
    "Equinix RJ3, Rio de Janeiro, Brazil (company geography; approximate metro pin).",
    "equinix_latam_419m_20260526",
    "Durante 2025 e 2026, a empresa avançou com novas fases de expansão em São Paulo e no Rio de Janeiro, incluindo a operação do data center RJ3, com um investimento inicial de aproximadamente USD 45 milhões e capacidade para mais de 550 gabinetes em sua primeira fase.",
    "https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix",
    "Actor: Equinix (U.S.) — us. Company Portuguese newsroom. CapEx = USD 45m initial. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle193",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="45000000",
    fx_usd="1",
    bib_type="company",
    chicago='Equinix. “América Latina é a região de maior crescimento e mais dinâmica para a Equinix.” May 26, 2026. https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix.',
    annotation="Equinix: RJ3 initial USD 45m. Supports equinix_rj3_45m_2025.",
    evid_note="Opened Equinix LatAm Portuguese newsroom 2026-10-04.",
)

# 5. engineering_epc / us — Equinix ST2 Santiago phase 2 USD 42m
row_doc(
    "equinix_st2_chile_42m_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Equinix — ST2 IBX phase-2 expansion (Pudahuel, Santiago)",
    "Chile",
    "Equinix LatAm newsroom: ~USD 42 million allocated in 2025 for second-phase expansion of ST2 in Pudahuel, Santiago; +425 cabinets. Distinct from Ascenty SLC04.",
    "42000000",
    "2025-01-01",
    "2025",
    "-33.43",
    "-70.78",
    "Equinix ST2, Pudahuel, Santiago, Chile (company geography).",
    "equinix_latam_419m_20260526",
    "Em 2025, a empresa alocou aproximadamente USD 42 milhões para a segunda fase de expansão de seu data center ST2 em Pudahuel, Santiago, adicionando capacidade para mais de 425 novos gabinetes",
    "https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix",
    "Actor: Equinix (U.S.) — us. Company Portuguese newsroom. CapEx = USD 42m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle193",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="42000000",
    fx_usd="1",
    bib_type="company",
    chicago='Equinix. “América Latina é a região de maior crescimento e mais dinâmica para a Equinix.” May 26, 2026. https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix.',
    annotation="Equinix: ST2 Santiago phase 2 USD 42m. Supports equinix_st2_chile_42m_2025.",
    evid_note="Opened Equinix LatAm Portuguese newsroom 2026-10-04 (same source_id as RJ3/Bogotá lines).",
)

# 6. engineering_epc / us — Equinix Bogotá second DC ~USD 28m
row_doc(
    "equinix_bogota_dc2_28m_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Equinix — second Bogotá IBX data center",
    "Colombia",
    "Equinix LatAm newsroom: ~USD 28 million for development of second Bogotá data center to serve local/regional digital demand. Distinct from ODATA Bogotá BG02/BG03.",
    "28000000",
    "2025-01-01",
    "2025",
    "4.71",
    "-74.07",
    "Equinix second Bogotá IBX, Colombia (company geography; approximate Bogotá pin).",
    "equinix_latam_419m_20260526",
    "Na Colômbia, a Equinix fortaleceu sua presença em Bogotá com o desenvolvimento de seu segundo data center, respaldado por um investimento de cerca de USD 28 milhões",
    "https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix",
    "Actor: Equinix (U.S.) — us. Company Portuguese newsroom. CapEx = USD 28m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle193",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="28000000",
    fx_usd="1",
    bib_type="company",
    chicago='Equinix. “América Latina é a região de maior crescimento e mais dinâmica para a Equinix.” May 26, 2026. https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix.',
    annotation="Equinix: Bogotá DC2 ~USD 28m. Supports equinix_bogota_dc2_28m_2025.",
    evid_note="Opened Equinix LatAm Portuguese newsroom 2026-10-04.",
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
    print(f"cycle193 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
