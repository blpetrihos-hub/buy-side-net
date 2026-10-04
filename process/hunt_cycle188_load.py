#!/usr/bin/env python3
"""Cycle 188 hunt: shuffle_seed=20261188; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261188)):
building_materials, engineering_epc, graphite, solar, nickel, other_renewables,
fission_smr, copper, water, bridges_roads, port_ownership, port_cranes, wind,
niobium, lithium, rail, power_plants_grid, balsa.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass.
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
≥1/3 U.S. hunt budget spent on DFC/EXIM/USTDA/AES/Atlas/Fluor/Bechtel/Caterpillar/
Progress/Wabtec/NADBank — plus IMPSA Tocoma/Macagua U.S.-controlled row logged.
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


# 1. building_materials / other — Grupo UNACEM 2Q26 CapEx PEN 353.1m
row_doc(
    "unacem_q2_2026_capex_3531m_pen",
    "infrastructure",
    "building_materials",
    "other",
    "Grupo UNACEM — 2Q2026 consolidated CapEx (Atocongo / CALCEM / Condorcocha)",
    "Peru",
    "19 Aug 2026 Grupo UNACEM: allocated PEN 353.1 million consolidated CapEx in 2Q26 — mainly new lime plant (CALCEM), new primary crusher and Mill 1 modifications at Atocongo, SO2 reduction on Kilns 1–2, clinker-yard roofing, and Condorcocha dust-control. CapEx = PEN 353.1m face (PEN stored without FX). Distinct from unacem_calcem_lime_peru_2025 presence/plan row.",
    "353100000",
    "2026-08-19",
    "2026",
    "-12.15",
    "-76.95",
    "Atocongo / Condorcocha / CALCEM plants, Peru (company geography; approximate Lima south Atocongo pin).",
    "unacem_q2_2026_results_20260819",
    "During the period, the Group also allocated PEN 353.1 million in consolidated CAPEX, mainly to the new lime plant (CALCEM), the new primary crusher, and modifications to Mill 1 at the Atocongo plant.",
    "https://grupounacem.com/en/noticias/grupo-unacems-net-income-grew-65-5-in-the-second-quarter-reaching-s-175-4-million/",
    "Actor: Grupo UNACEM (Peru) — other. Company English results release. Shuffle building_materials.",
    "hunt_cycle188",
    investment_type="capex",
    evidence="documented",
    currency="PEN",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Grupo UNACEM. “Grupo UNACEM’s net income grew 65.5% in the second quarter, reaching S/175.4 million.” August 19, 2026. https://grupounacem.com/en/noticias/grupo-unacems-net-income-grew-65-5-in-the-second-quarter-reaching-s-175-4-million/.',
    annotation="UNACEM: 2Q26 CapEx PEN 353.1m. Supports unacem_q2_2026_capex_3531m_pen.",
    evid_note="Opened Grupo UNACEM English results page 2026-10-04.",
)

# 2. building_materials / other — Votorantim Brazil plan progress R$2.7bn invested
row_doc(
    "votorantim_brazil_plan_2p7bn_invested_2025",
    "infrastructure",
    "building_materials",
    "other",
    "Votorantim Cimentos — Brazil 2024–28 CapEx plan progress (R$2.7bn invested)",
    "Brazil",
    "18 Mar 2026 Votorantim Cimentos FY2025 results: of the R$5 billion Brazil investment plan for 2024–2028, R$2.7 billion has already been invested in growth/decarbonization/competitiveness (Edealina, Nobres, Salto de Pirapora grinding; Xambioá kiln modernization; Laranjeiras/Esteio restarts; +3.7 Mtpy capacity targeted from 2026). CapEx progress face = R$2.7bn cumulative invested (BRL stored without FX). Distinct from site-level votorantim_xambioa / nobres / edealina rows.",
    "2700000000",
    "2026-03-18",
    "2025",
    "",
    "",
    "Multi-site Brazil cement CapEx plan — lat/lon blank (portfolio progress).",
    "votorantim_fy2025_results_20260318",
    "Regarding the R$5 billion investment plan for the period 2024-2028 in Brazil, R$2.7 billion is already being invested in a comprehensive program for growth, decarbonization and structural competitiveness.",
    "https://www.votorantimcimentos.com/news/our-2025-financial-results/",
    "Actor: Votorantim Cimentos (Brazil) — other. Company English FY2025 results. Shuffle building_materials overflow.",
    "hunt_cycle188",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Votorantim Cimentos. “Our 2025 financial results.” March 18, 2026. https://www.votorantimcimentos.com/news/our-2025-financial-results/.',
    annotation="Votorantim: Brazil plan R$2.7bn invested of R$5bn. Supports votorantim_brazil_plan_2p7bn_invested_2025.",
    evid_note="Opened Votorantim Cimentos English FY2025 results page 2026-10-04.",
)

# 3. power_plants_grid / us — IMPSA Tocoma/Macagua phase-1 672 MW (Venezuela)
row_doc(
    "impsa_tocoma_macagua_672mw_2026",
    "energy",
    "power_plants_grid",
    "us",
    "IMPSA (IAF / Argentine-American) — Tocoma + Macagua hydro rehab phase 1",
    "Venezuela",
    "12 Aug 2026 IMPSA: signs final agreement with CORPOELEC for rehabilitation/modernization at Tocoma and Macagua — phase 1 recovers 432 MW (Tocoma Units 1–2) + 240 MW (Macagua Units 4–6) = 672 MW within 24 months; first milestone 160 MW (Macagua 5–6) within 90 days of signing. Master plan foresees up to 2,640 MW across both plants. CapEx USD blank (not disclosed on company page). IMPSA acquired Feb 2025 by U.S. fund IAF — side=us. Venezuela under-covered weight.",
    "",
    "",
    "2026",
    "8.00",
    "-62.76",
    "Tocoma and Macagua hydroelectric complexes, Río Caroní, Bolívar state, Venezuela (company geography; approximate Puerto Ordaz corridor pin).",
    "impsa_tocoma_macagua_20260812",
    "The signed contract provides, in its first phase, for the recovery of 432 MW at Tocoma, through the rehabilitation of Units 1 and 2, and 240 MW at Macagua, through Units 4, 5, and 6, bringing the total to 672 MW within a 24-month period.",
    "https://www.impsa.com/en/impsa-restarts-the-tocoma-and-macagua-projects/",
    "Actor: IMPSA (Argentine-American; IAF U.S. fund owner since Feb 2025) — us. Company English press. CapEx blank. Shuffle power_plants_grid / Venezuela priority.",
    "hunt_cycle188",
    investment_type="rehabilitation",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='IMPSA. “IMPSA reactivates the Tocoma and Macagua projects.” August 13, 2026. https://www.impsa.com/en/impsa-restarts-the-tocoma-and-macagua-projects/.',
    annotation="IMPSA: Tocoma/Macagua phase-1 672 MW; CapEx blank. Supports impsa_tocoma_macagua_672mw_2026.",
    evid_note="Opened IMPSA English company press 2026-10-04; ownership via IAF stated on same page.",
)

# 4. rail / allied — ANI Bogotá–Belencito COP 284,436m
row_doc(
    "ani_bogota_belencito_284436m_cop_2026",
    "infrastructure",
    "rail",
    "allied",
    "ANI — Bogotá–Belencito rail corridor obra pública (Consorcio MIA C&E)",
    "Colombia",
    "21 Jul 2026 ANI: awards Bogotá–Belencito freight rail corridor obra pública to Consorcio MIA C&E (Martín Casillas SLU Spain 40% lead + ASCH/Ingecon/Arcom) — 278.4 km incl. La Caro–Zipaquirá and Bogotá–Facatativá ramales; investment COP 284,436 million; 44-month term. CapEx = COP 284,436m face (COP stored without FX). Spanish-led consortium — allied.",
    "284436000000",
    "2026-07-21",
    "2026",
    "5.54",
    "-73.36",
    "Bogotá–Belencito rail corridor via Cundinamarca/Boyacá, Colombia (ANI geography; approximate Tunja mid-corridor pin).",
    "ani_bogota_belencito_20260721",
    "En el corredor férreo Bogotá-Belencito, la licitación se le adjudicó al consorcio MIA C&E … con una inversión de $284.436 millones. … En Audiencia Pública … adjudicó las obras públicas de los corredores férreos Bogotá-Belencito y el Pacífico, con una inversión de $564.958 millones.",
    "https://wwwold.ani.gov.co/ani-adjudico-proyectos-de-obras-publicas-en-los-corredores-ferreos-bogota-belencito-y-pacifico-con",
    "Actor: Consorcio MIA C&E (Spain Martín Casillas lead) via ANI award — allied. Official ANI Spanish press. Shuffle rail.",
    "hunt_cycle188",
    investment_type="concession",
    evidence="documented",
    currency="COP",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Agencia Nacional de Infraestructura (ANI). “ANI adjudicó proyectos de obras públicas en los corredores férreos Bogotá-Belencito y Pacífico con una inversión de $564.958 millones.” July 21, 2026. https://wwwold.ani.gov.co/ani-adjudico-proyectos-de-obras-publicas-en-los-corredores-ferreos-bogota-belencito-y-pacifico-con.',
    annotation="ANI: Bogotá–Belencito COP 284,436m. Supports ani_bogota_belencito_284436m_cop_2026.",
    evid_note="Opened ANI Spanish award press 2026-10-04.",
)

# 5. rail / allied — ANI Pacífico ferro COP 280,522m
row_doc(
    "ani_pacifico_ferro_280522m_cop_2026",
    "infrastructure",
    "rail",
    "allied",
    "ANI — Pacífico rail corridor obra pública (Consorcio Pacífico 2026 / Mota-Engil)",
    "Colombia",
    "21 Jul 2026 ANI: awards Pacífico freight rail corridor (498 km Buenaventura–Yumbo–Zarzal–Cartago–La Felisa + Zarzal–La Tebaida ramal) to Consorcio Pacífico 2026 led by Mota-Engil Latam Col (~50%) — investment COP 280,522 million; includes Palmira–Buga improvement works. CapEx = COP 280,522m face (COP stored without FX). Portuguese Mota-Engil lead — allied. Distinct from Belencito row.",
    "280522000000",
    "2026-07-21",
    "2026",
    "3.88",
    "-77.00",
    "Pacífico rail corridor Buenaventura–La Felisa, Valle del Cauca / Eje Cafetero, Colombia (ANI geography; approximate Buenaventura pin).",
    "ani_pacifico_ferro_20260721",
    "En el caso del corredor férreo del Pacífico, se trata del Consorcio Pacífico 2026 … el cual cuenta con una extensión de 498 kilómetros, una inversión de $280.522 millones y cubre los tramos entre Buenaventura-Yumbo-Zarzal-Cartago-La Felisa y el ramal de Zarzal-La Tebaida.",
    "https://wwwold.ani.gov.co/ani-adjudico-proyectos-de-obras-publicas-en-los-corredores-ferreos-bogota-belencito-y-pacifico-con",
    "Actor: Consorcio Pacífico 2026 (Mota-Engil Portugal group lead) via ANI — allied. Official ANI Spanish press. Shuffle rail.",
    "hunt_cycle188",
    investment_type="concession",
    evidence="documented",
    currency="COP",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Agencia Nacional de Infraestructura (ANI). “ANI adjudicó proyectos de obras públicas en los corredores férreos Bogotá-Belencito y Pacífico con una inversión de $564.958 millones.” July 21, 2026. https://wwwold.ani.gov.co/ani-adjudico-proyectos-de-obras-publicas-en-los-corredores-ferreos-bogota-belencito-y-pacifico-con.',
    annotation="ANI: Pacífico ferro COP 280,522m. Supports ani_pacifico_ferro_280522m_cop_2026.",
    evid_note="Opened ANI Spanish award press 2026-10-04 (same page as Belencito).",
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
    print(f"cycle188 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
