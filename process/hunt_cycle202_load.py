#!/usr/bin/env python3
"""Cycle 202 hunt: shuffle_seed=20261202; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261202).shuffle):
port_cranes, other_renewables, niobium, fission_smr, graphite, lithium,
power_plants_grid, building_materials, wind, solar, water, bridges_roads,
copper, rail, balsa, port_ownership, nickel, engineering_epc.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES/Freeport/EXIM/DFC/Progress Rail/Fluence/
Bechtel/Pumpco/MasTec/EnergyX/Albemarle sweeps (catalog dense; Pumpco CapEx
upgrade). PRC: CAMC Bluefields / Zijin Longking / SPIC São Simão / BYD BESS
already logged — equal-budget miss.
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


# 1. water / other — Aguas Pacífico Aconcagua expansion USD 280m (RCA)
row_doc(
    "aguas_pacifico_aconcagua_exp_280m_2026",
    "resources",
    "water",
    "other",
    "Aguas Pacífico SpA / Patria — Aconcagua desal modification (+1,000 l/s)",
    "Chile",
    "28 Apr 2026 Aguas Pacífico (Spanish): Valparaíso CEA approves EIA “Modificación Proyecto Aconcagua” after ~15 months SEA review — adds 1,000 l/s desalinated production (to 2,000 l/s total) via new desal module adjacent to existing Puchuncaví plant, intake/outfall upgrades, and pumping reinforcement using existing 105 km aqueduct; investment USD 280 million; ~3-year build; operations targeted 2030; >500 construction jobs. Distinct from aguas_pacifico_desal_capex_1p2bn_2025 (original plant) and ide_aconcagua_desal_chile_2023 (IDE EPC start).",
    "280000000",
    "2026-04-28",
    "2026",
    "-32.783",
    "-71.533",
    "Puchuncaví / Quintero Bay, Valparaíso Region (company geography; same pin family as IDE Aconcagua).",
    "aguas_pacifico_aconcagua_rca_20260428",
    "Con una inversión de USD $280 millones, esta nueva etapa considera el aumento de la capacidad de producción de agua desalinizada en 1.000 l/s adicionales, la contratación de más de 500 trabadores durante su construcción, que se estima en 3 años, proyectándose su inicio de operaciones para 2030.",
    "https://www.aguaspacifico.cl/noticias/aguas-pacfico-obtiene-permiso-ambiental-rcapara-proyecto-que-aumenta-la-produccinde-agua-desalinizada-a-2000-ls",
    "Actor: Aguas Pacífico SpA (Patria Investments) — other (matches aguas_pacifico_desal_capex_1p2bn_2025 coding). Company Spanish primary. CapEx = USD 280m RCA-approved expansion. Shuffle water.",
    "hunt_cycle202",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="280000000",
    fx_usd="1",
    bib_type="company",
    chicago='Aguas Pacífico. “Aguas Pacífico obtiene permiso ambiental para proyecto que aumenta la producción de agua desalinizada a 2000 l/s.” April 28, 2026. https://www.aguaspacifico.cl/noticias/aguas-pacfico-obtiene-permiso-ambiental-rcapara-proyecto-que-aumenta-la-produccinde-agua-desalinizada-a-2000-ls.',
    annotation="Aguas Pacífico Aconcagua expansion: USD 280m. Supports aguas_pacifico_aconcagua_exp_280m_2026.",
    evid_note="Opened Aguas Pacífico Spanish company primary 2026-10-04; USD 280m / +1,000 l/s / 2030 COD confirmed.",
)

# 2. other_renewables / allied — EDP Punta de Talca BESS USD 44m
row_doc(
    "edp_punta_talca_bess_44m_chile_2026",
    "energy",
    "other_renewables",
    "allied",
    "EDP — Punta de Talca BESS 240 MWh (Ovalle)",
    "Chile",
    "11 Jun 2026 EDP: commercial operations of Punta de Talca BESS in Ovalle municipality — first EDP battery-storage complex in South America; ~USD 44 million invested integrating BESS with the 83 MW Punta de Talca Wind Farm (COD since 2024); installed storage 240 MWh; ~60 GWh average annual storage; potential supply >30,000 households. CapEx = USD 44m. Distinct from wind-farm COD row if any; coded other_renewables for co-located storage CapEx.",
    "44000000",
    "2026-06-11",
    "2026",
    "-30.60",
    "-71.20",
    "Punta de Talca Wind Farm / Ovalle, Coquimbo Region (company geography; approximate municipal pin).",
    "edp_punta_talca_bess_20260611",
    "Approximately US$44 million was invested in integrating the Battery Energy Storage System (BESS) with the Punta de Talca Wind Farm, which has an installed capacity of 83 MW and has been in operation since 2024.",
    "https://edp.com/en/america-do-sul/brasil/imprensa/noticias/edp-inicia-operacoes-de-seu-primeiro-complexo-de-baterias-america-do-sul",
    "Actor: EDP (Portugal) — allied. Company English primary (Portuguese twin also opened). CapEx ≈ USD 44m. Shuffle other_renewables.",
    "hunt_cycle202",
    investment_type="brownfield_storage",
    evidence="documented",
    currency="USD",
    value_usd="44000000",
    fx_usd="1",
    bib_type="company",
    chicago='EDP. “EDP begins operations at its first storage complex in South America.” June 11, 2026. https://edp.com/en/america-do-sul/brasil/imprensa/noticias/edp-inicia-operacoes-de-seu-primeiro-complexo-de-baterias-america-do-sul.',
    annotation="EDP Punta de Talca BESS: USD 44m. Supports edp_punta_talca_bess_44m_chile_2026.",
    evid_note="Opened EDP English company primary 2026-10-04; USD 44m / 240 MWh confirmed.",
)

# 3. power_plants_grid / allied — Hitachi Energy Brazil Service R$50m
row_doc(
    "hitachi_brazil_service_50m_brl_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Hitachi Energy — Brazil Service Center CapEx (Greater São Paulo)",
    "Brazil",
    "20 May 2026 Hitachi Energy: new investment of around R$ 50 million (~USD 11m on page) to expand Service capabilities in Brazil — new Service Center in Greater São Paulo (equipment, production capacity, service ops); operations targeted end-2026; part of ~R$1.4bn / ~USD 280m Brazil investment plan including Guarulhos refurbishment and Pindamonhangaba factory. CapEx = R$50m service tranche. Distinct from hitachi_brazil_transformer_capex_2024 (USD 200m) and hitachi_brazil_addl_70m_2026 (USD 70m add-on).",
    "50000000",
    "2026-05-20",
    "2026",
    "-23.55",
    "-46.63",
    "Greater São Paulo Service Center (company geography; approximate metro pin).",
    "hitachi_brazil_service_20260520",
    "Hitachi Energy, a global leader in electrification, will make a new investment of around R$50 million ($11 million USD) to expand its Service capabilities in Brazil.",
    "https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/05/hitachi-energy-announces-new-r-50-million-11-million-usd-investment-to-accelerate-brazil-s-grid-modernization",
    "Actor: Hitachi Energy (Hitachi Ltd / Japanese–Swiss electrification) — allied. Company English primary. CapEx = R$50m (BRL stored without FX; page also states ~USD 11m). Shuffle power_plants_grid.",
    "hunt_cycle202",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Hitachi Energy. “Hitachi Energy announces new R$50 million ($11 million USD) investment to accelerate Brazil’s grid modernization.” May 20, 2026. https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/05/hitachi-energy-announces-new-r-50-million-11-million-usd-investment-to-accelerate-brazil-s-grid-modernization.',
    annotation="Hitachi Brazil Service: R$50m. Supports hitachi_brazil_service_50m_brl_2026.",
    evid_note="Opened Hitachi Energy English company primary 2026-10-04; R$50m Service Center confirmed.",
)

# 4. power_plants_grid / allied — Enel Brasil R$25.3bn 2025–2027
row_doc(
    "enel_brasil_25p3bn_brl_2025_2027",
    "energy",
    "power_plants_grid",
    "allied",
    "Enel Brasil — distribution CapEx plan 2025–2027 (SP/CE/RJ)",
    "Brazil",
    "Enel Brasil company: invests about R$ 25.3 billion in Brazil operations 2025–2027; of which R$ 24 billion for distribution in São Paulo, Ceará and Rio de Janeiro (+62% vs prior plan); São Paulo tranche ~R$ 10.4 billion for network strengthening/digitalization/expansion amid climate extremes; ~5,000 field hires through 2026. CapEx plan = R$25.3bn. Distinct from Neoenergia distribution rows and csgi_enel_distribucion_peru_3p1bn_2024 (Peru sale).",
    "25300000000",
    "2025-05-08",
    "2025",
    "",
    "",
    "Enel Brasil three-state distribution network (SP/CE/RJ — lat/lon blank).",
    "enel_brasil_25p3bn_2025",
    "Nos próximos três anos, a Enel investirá cerca de R$ 25,3 bilhões em suas operações no Brasil. Desse total, R$ 24 bilhões serão direcionados ao setor de distribuição de energia.",
    "https://www.enel.com.br/pt/midia/news/d2025-1/Enel-anuncia-investimento-de-R$-25bilhoes-no-Brasil.html",
    "Actor: Enel Brasil (Enel SpA Italy) — allied. Company Portuguese primary. CapEx plan = R$25.3bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle202",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Enel Brasil. “Enel anuncia investimento de R$ 25 bilhões no Brasil.” https://www.enel.com.br/pt/midia/news/d2025-1/Enel-anuncia-investimento-de-R$-25bilhoes-no-Brasil.html.',
    annotation="Enel Brasil: R$25.3bn 2025–2027. Supports enel_brasil_25p3bn_brl_2025_2027.",
    evid_note="Opened Enel Brasil Portuguese company primary 2026-10-04; R$25.3bn / R$24bn distribution confirmed.",
)

# 5. power_plants_grid / allied — Enel Américas Brazil grids USD 6.8bn 2026–28
row_doc(
    "enel_americas_brazil_grids_6p8bn_2026_28",
    "energy",
    "power_plants_grid",
    "allied",
    "Enel Américas — Brazil grids CapEx plan 2026–2028",
    "Brazil",
    "Feb 2026 Enel Américas Strategic Plan 2026–28 investor presentation: total group CapEx USD 7.9bn (+5% vs prior plan); investments increase mainly linked to Grids in Brazil; Brazil grids CapEx USD 6.8bn (+8% vs old plan) across Ceará / São Paulo / Rio concessions for quality and resilience. CapEx plan = USD 6.8bn Brazil grids. Complements enel_brasil_25p3bn_brl_2025_2027 (local R$ 2025–27 plan; overlapping but different plan window/currency framing).",
    "6800000000",
    "2026-02-01",
    "2026",
    "",
    "",
    "Enel Américas Brazil grids concessions (SP/CE/RJ — lat/lon blank).",
    "enel_americas_plan_2026_28",
    "Investments vs previous plan increase mainly linked to Grids in Brazil … USD 6.8 bn +8% vs Old Plan",
    "https://www.enelamericas.com/content/dam/enel-americas/investor/strategic-plan/2026/2025-Results-2026-2028-Strategic-Plan-presentation1.pdf",
    "Actor: Enel Américas (Enel SpA Italy) — allied. Official investor-plan PDF. CapEx plan = USD 6.8bn Brazil grids 2026–28. Shuffle power_plants_grid.",
    "hunt_cycle202",
    investment_type="capex_plan",
    evidence="documented",
    currency="USD",
    value_usd="6800000000",
    fx_usd="1",
    bib_type="company",
    chicago='Enel Américas. “2025 Results & 2026–2028 Strategic Plan.” February 2026. https://www.enelamericas.com/content/dam/enel-americas/investor/strategic-plan/2026/2025-Results-2026-2028-Strategic-Plan-presentation1.pdf.',
    annotation="Enel Américas Brazil grids: USD 6.8bn 2026–28. Supports enel_americas_brazil_grids_6p8bn_2026_28.",
    evid_note="Opened Enel Américas Strategic Plan PDF 2026-10-04; USD 6.8bn Brazil grids / USD 7.9bn total confirmed.",
)

# 6. engineering_epc / us — upgrade Pumpco–Bonatti Argentina LNG CapEx to USD 1.2bn (proxy)
row_doc(
    "pumpco_bonatti_argentina_lng_epc_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Pumpco (MasTec) / Bonatti / Contreras — Argentina LNG trunk pipelines EPC",
    "Argentina",
    "30 Jul 2026 Bonatti company: JV with U.S. pipeline contractor Pumpco (MasTec) plus Contreras Hermanos awarded EPC for complete Argentina LNG pipeline system — 48-inch gas line + parallel liquids line, each ~527 km from Meseta Buena Esperanza (Vaca Muerta) to Sierra Grande (Río Negro). UNVERIFIED press (Il Sole 24 Ore / BNamericas) cites total contract ~USD 1.2 billion (Bonatti share ~USD 480m); Bonatti primary confirms award/scope without USD. Upgrades prior USD 1.0bn floor to USD 1.2bn proxy. Subject to project FID.",
    "1200000000",
    "2026-07-30",
    "2026",
    "-38.60",
    "-68.50",
    "Vaca Muerta–Sierra Grande corridor (approximate Neuquén–Río Negro pin).",
    "bonatti_argentina_lng_20260730",
    "Bonatti, in joint venture with Pumpco, has been awarded the Engineering, Procurement and Construction (EPC) contract for the complete pipeline system of the Argentina LNG project",
    "https://www.bonattinternational.com/bonatti-argentina-lng-project",
    "Actor: Pumpco (U.S.; MasTec) lead JV with Bonatti (Italy) / Contreras (Argentina) — us (U.S. pipeline EPC lead). Company English primary for award/scope; CapEx USD 1.2bn from UNVERIFIED press citing contract — evidence=proxy upgrade from prior USD 1.0bn floor. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle202",
    investment_type="epc",
    evidence="proxy",
    currency="USD",
    value_usd="1200000000",
    fx_usd="1",
    bib_type="company",
    chicago='Bonatti. “Bonatti, in joint venture with Pumpco, has been awarded the Engineering, Procurement and Construction (EPC) contract for the complete pipeline system of the Argentina LNG project.” July 30, 2026. https://www.bonattinternational.com/bonatti-argentina-lng-project.',
    annotation="Pumpco–Bonatti Argentina LNG: CapEx upgrade ~USD 1.2bn proxy. Supports pumpco_bonatti_argentina_lng_epc_2026.",
    evid_note="Opened Bonatti English company primary 2026-10-04 (award/scope); CapEx ~USD 1.2bn from Il Sole 24 Ore / BNamericas — evidence=proxy upgrade.",
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
    print(f"cycle202 added {len(added)}: {added}")
    print(f"cycle202 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
