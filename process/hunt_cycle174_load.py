#!/usr/bin/env python3
"""Cycle 174 hunt: shuffle_seed=20261174; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261174)): niobium, wind, nickel,
engineering_epc, solar, power_plants_grid, rail, port_ownership, graphite, water,
other_renewables, copper, bridges_roads, port_cranes, balsa, fission_smr, lithium,
building_materials.

Thin top-up (recomputed after shuffle pass): nickel / balsa / fission_smr —
fission filled (U.S.–Colombia civil nuclear MoU); nickel/balsa dry this pass
(catalog dense; AIMA/WITS Ecuador balsa and MMG/Atlantic Nickel already logged).
Niobium filled via St George–Nanum Araxá MoU (allied). Graphite filled via
U.S.–Colombia critical-minerals framework (Colombia×graphite priority cell).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail
past MoU (still prefeasibility/feasibility).
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


# 1. niobium / allied — St George Mining–Nanum MoU on Araxá cerium downstream
row_doc(
    "st_george_nanum_araxa_mou_2026",
    "resources",
    "niobium",
    "allied",
    "St George Mining (ASX:SGQ) + Nanum Nanotecnologia — Araxá Nb-REE cerium MoU",
    "Brazil",
    "12 Mar 2026 (ASX): St George Mining signs MoU with Brazilian Nanum Nanotecnologia for a strategic alliance to assess commercialising the cerium component of rare earths at the 100%-owned Araxá niobium-REE project (Minas Gerais; MRE 70.91 Mt @ 4.06% TREO / 0.62% Nb₂O₅). CapEx blank (non-binding MoU; no offtake CapEx; each party bears own costs).",
    "",
    "",
    "2026",
    "",
    "",
    "Araxá Project, Minas Gerais — lat/lon blank (project-level MoU; no single plant pin).",
    "sgq_asx_nanum_mou_20260312",
    "St George Mining Limited (ASX: SGQ) (“St George” or “the Company”) is pleased to announce that it has signed a Memorandum of Understanding (“MOU”) with Nanum Nanotecnologia (“Nanum”) to create a strategic alliance whereby the parties will collaborate on the commercialisation of the cerium component in the large rare earths resource at the Company’s 100%-owned advanced, high-grade Araxá niobium-REE Project in Minas Gerais, Brazil (“Project”).",
    "https://announcements.asx.com.au/asxpdf/20260312/pdf/06xb95z21863rx.pdf",
    "Actor: St George Mining (Australian ASX) — allied; Nanum (Brazilian) counterpart. Opened ASX release 12 Mar 2026. Thin niobium fill. Distinct from fangda_st_george_araxa_mou_20250115, xinhai_st_george_araxa_epc_mou_2025, st_george_araxa_mre_upgrade_nb_2026.",
    "hunt_cycle174",
    investment_type="other",
    evidence="documented",
    bib_type="company",
    chicago='St George Mining Limited. “Downstream strategy to significantly upgrade the magnet and heavy rare earths from the Araxá Project.” ASX release, March 12, 2026. https://announcements.asx.com.au/asxpdf/20260312/pdf/06xb95z21863rx.pdf.',
    annotation="ASX SGQ: Nanum MoU on Araxá cerium downstream at Nb-REE project. Supports st_george_nanum_araxa_mou_2026.",
    evid_note="Opened ASX PDF release 2026-10-02.",
)

# 2. engineering_epc / allied — Jan De Nul CARP Canal Martín García dredging
row_doc(
    "jan_de_nul_martin_garcia_carp_66m_2026",
    "infrastructure",
    "engineering_epc",
    "allied",
    "Jan De Nul N.V. — CARP Canal Martín García dredging / widening (LPI 1/2026)",
    "Argentina",
    "1–2 Jul 2026: Comisión Administradora del Río de la Plata (CARP) awards Licitación Pública Internacional CARP Nº 1/2026 for maintenance dredging, widening, and eventual improvements of Río de la Plata channels km 39 (Barra del Farallón) to km 0 Río Uruguay (Canal Martín García) to Belgian Jan De Nul N.V.; winning bid USD 65,994,000 before VAT (vs Boskalis USD 149,279,315); initial 5-year term with optional 5-year extension (Res. CARP 17/26).",
    "65994000",
    "2026-07-01",
    "2026",
    "",
    "",
    "Canal Martín García / Río de la Plata (Argentina–Uruguay CARP waters) — lat/lon blank (binational channel corridor).",
    "mrree_uy_carp_martin_garcia_20260702",
    "Resultando la Oferta Nº 1- JAN DE NUL N.V.- de un valor de DOLARES ESTADOUNIDENSES SESENTA Y CINCO MILLONES NOVECIENTOS NOVENTA Y CUATRO MIL (U$S 65.994.000.-) y la Oferta Nº 3 – BOSKALIS INTERNATIONAL URUGUAY S.A. – de un valor de DOLARES ESTADOUNIDENSES CIENTO CUARENTA Y NUEVE MILLONES DOSCIENTOS SETENTA Y NUEVE MIL TRESCIENTOS QUINCE (U$S 149.279.315.-). Como consecuencia del mencionado proceso, la Comisión Administradora del Río de la Plata dictó en el día de la fecha la Resolución CARP Nº 17/26 por la cual se declara a la oferta presentada por JAN DE NUL N.V. como la más conveniente.",
    "https://www.gub.uy/ministerio-relaciones-exteriores/comunicacion/comunicados/carp-adjudica-licitacion-para-canal-martin-garcia",
    "Actor: Jan De Nul N.V. (Belgian) — allied. Opened Uruguay MFA (MRREE) CARP award notice 2 Jul 2026; figures match Boletín Oficial Argentina Res. 17/2026. Distinct from jan_de_nul_via_navegable_troncal_2026 and eiffage_jande_nul_callao_norte_2026.",
    "hunt_cycle174",
    investment_type="epc",
    evidence="documented",
    bib_type="government",
    chicago='Ministerio de Relaciones Exteriores (Uruguay). “CARP adjudica licitación para canal Martín García.” July 2, 2026. https://www.gub.uy/ministerio-relaciones-exteriores/comunicacion/comunicados/carp-adjudica-licitacion-para-canal-martin-garcia.',
    annotation="Uruguay MFA/CARP: Jan De Nul Martín García dredging USD 65.994m. Supports jan_de_nul_martin_garcia_carp_66m_2026.",
    evid_note="Opened Uruguay MFA CARP award communiqué 2026-10-02; cross-checked BO Argentina Res. 17/2026 synthesis.",
)

# 3. solar / allied — Zelestra Babilonia 242 MWdc green financing
row_doc(
    "zelestra_babilonia_176m_2026",
    "energy",
    "solar",
    "allied",
    "Zelestra — Babilonia 242 MWdc solar (Arequipa) USD 176m green financing close",
    "Peru",
    "5 Mar 2026: Spanish Zelestra achieves financial close of 242 MWdc Babilonia solar (La Joya complex, Arequipa) via USD 176 million green project financing from Natixis CIB and BBVA Perú; long-term PPA with Celepsa; internal EPC construction underway; part of ~700 MW La Joya complex with operating San Martín 300 MW.",
    "176000000",
    "2026-03-05",
    "2026",
    "",
    "",
    "Babilonia / La Joya solar complex, Arequipa — lat/lon blank pending verified worksite coords.",
    "zelestra_babilonia_financing_20260305",
    "Zelestra, a global, multi-technology, customer-focused renewable energy company, has successfully achieved Financial Close of the 242 MWdc Babilonia solar project in Perú, through a $176 million project green financing package agreed with Natixis CIB and BBVA Perú.",
    "https://zelestra.energy/en/news/babilonia-financing",
    "Actor: Zelestra (Spanish) — allied. Opened company English press release 5 Mar 2026. Distinct from zelestra_san_martin_peru_cod_179p7m_2025 and sungrow_zelestra_san_martin_peru_273mw_2025.",
    "hunt_cycle174",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='Zelestra. “Zelestra secures $176 million green financing package for the 242 MW Babilonia solar plant in Perú.” March 5, 2026. https://zelestra.energy/en/news/babilonia-financing.',
    annotation="Zelestra: Babilonia 242 MWdc USD 176m green financing. Supports zelestra_babilonia_176m_2026.",
    evid_note="Opened Zelestra company press page 2026-10-02.",
)

# 4. fission_smr / us — U.S.–Colombia civil nuclear MoU (thin top-up)
row_doc(
    "us_colombia_civil_nuclear_mou_202609",
    "energy",
    "fission_smr",
    "us",
    "U.S. + Colombia — civil nuclear cooperation MoU (incl. advanced/SMR exploration)",
    "Colombia",
    "8 Sep 2026 (State Dept): Secretary Rubio and Colombian FM Omar Bula sign a Civil Nuclear Cooperation MoU establishing a bilateral framework for strategic civil nuclear cooperation (NPT/IAEA safeguards) as Colombia considers nuclear power; intent to explore U.S. nuclear technologies including advanced and small modular reactors, fuel, equipment, and services, plus regulatory capacity-building. CapEx blank (MoU framework; no reactor CapEx).",
    "",
    "",
    "2026",
    "",
    "",
    "Colombia (national framework) — lat/lon blank (MoU; no named reactor site).",
    "state_colombia_critical_nuclear_20260908",
    "Establishes a bilateral framework for strategic civil nuclear cooperation between the United States and Colombia, grounded in Non-Proliferation Treaty obligations and International Atomic Energy Agency safeguards, as Colombia considers deploying nuclear power… explore U.S. nuclear technologies (including advanced and small modular reactors), fuel, equipment, and services…",
    "https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation",
    "Actor: U.S. Department of State with Colombia — us. Opened State Department spokesman release 8 Sep 2026. Thin fission_smr top-up; Mexico/Colombia fission priority sweep. Distinct from meitner_acr300_atucha_2026 and peru_first_bilateral_partner_2026.",
    "hunt_cycle174",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='U.S. Department of State, Office of the Spokesman. “Secretary Rubio and Colombian Foreign Minister Bula Sign Arrangements on Critical Minerals and Civil Nuclear Cooperation.” September 8, 2026. https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation.',
    annotation="State Dept: U.S.–Colombia civil nuclear MoU including SMR exploration. Supports us_colombia_civil_nuclear_mou_202609.",
    evid_note="Opened State Department release 2026-10-02.",
)

# 5. graphite / us — U.S.–Colombia critical minerals framework (same release; Colombia×graphite)
row_doc(
    "us_colombia_critical_minerals_framework_202609",
    "resources",
    "graphite",
    "us",
    "U.S. + Colombia — Critical Minerals Framework (supply-chain / finance tools)",
    "Colombia",
    "8 Sep 2026 (State Dept): Secretary Rubio and Colombian FM Omar Bula sign a Critical Minerals Framework to secure resilient critical-minerals and rare-earths supply chains; commit to mobilize guarantees, loans, equity, offtake, insurance, or regulatory facilitation to jointly identify and finance mining and processing projects within six months; also streamlined permitting, price floors, national-security review of asset sales, recycling, and geological mapping. CapEx blank (bilateral framework; no named mine CapEx).",
    "",
    "",
    "2026",
    "",
    "",
    "Colombia (national framework) — lat/lon blank (framework; no named graphite mine).",
    "state_colombia_critical_nuclear_20260908",
    "Establishes a U.S.-Colombia framework to secure resilient, diversified, and fair supply chains for critical minerals and rare earths, committing both governments to mobilize government and private sector support—via guarantees, loans, equity, offtake arrangements, insurance, or regulatory facilitation—to jointly identify and finance mining and processing projects within six months of signing.",
    "https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation",
    "Actor: U.S. Department of State with Colombia — us. Opened same State release 8 Sep 2026. Filed under graphite as Colombia×graphite priority empty cell (framework covers critical minerals/REEs generally; CapEx blank). Distinct from us_colombia_civil_nuclear_mou_202609 (nuclear MoU on same page).",
    "hunt_cycle174",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='U.S. Department of State, Office of the Spokesman. “Secretary Rubio and Colombian Foreign Minister Bula Sign Arrangements on Critical Minerals and Civil Nuclear Cooperation.” September 8, 2026. https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation.',
    annotation="State Dept: U.S.–Colombia Critical Minerals Framework. Supports us_colombia_critical_minerals_framework_202609.",
    evid_note="Opened State Department release 2026-10-02 (shared URL with civil nuclear MoU).",
)

# 6. engineering_epc / us — Caterpillar autonomous haul trucks Vale Northern System
row_doc(
    "caterpillar_vale_northern_autonomous_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Caterpillar + Sotreq — Vale Northern System autonomous haul-truck fleet expansion",
    "Brazil",
    "8 Dec 2025 (Vale): Vale, Caterpillar, and dealer Sotreq sign agreement to expand Cat MineStar Command for hauling autonomous fleet at Serra Norte / Serra Sul (Carajás, Pará) from 14 trucks (up to 320 t) toward ~90 autonomous trucks by 2028 (including up to 400 t); employee digital-training plan accompanies rollout. CapEx blank (fleet-expansion agreement; no disclosed USD CapEx on opened page).",
    "",
    "",
    "2025",
    "",
    "",
    "Serra Norte / Serra Sul, Carajás, Pará — lat/lon blank (multi-site Northern System).",
    "vale_caterpillar_autonomous_20251208",
    "Vale, Caterpillar and Sotreq have signed an agreement to expand the fleet of autonomous haul trucks in iron ore operations in the Northern System, in the Carajás region, in Pará… Currently, the Northern System operation has 14 autonomous haul trucks with a capacity to carry up to 320 tons. This new agreement expands the fleet to approximately 90 autonomous trucks in the region by 2028, operated by Cat® MineStar™ Command for hauling, including trucks with a capacity to carry up to 400-tons.",
    "https://saladeimprensa.vale.com/w/vale-caterpillar-and-sotreq-sign-agreement-to-expand-fleet-of-autonomous-trucks-in-the-northern-system-in-para",
    "Actor: Caterpillar Inc. (U.S.) with Sotreq dealer — us; Vale host. Opened Vale English press room 8 Dec 2025. U.S. side-balance for engineering_epc. Distinct from progress_rail_vli_* and wabtec_* rail equipment rows.",
    "hunt_cycle174",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Vale. “Vale, Caterpillar & Sotreq sign agreement to expand fleet of autonomous trucks in the Northern System, in Pará.” December 8, 2025. https://saladeimprensa.vale.com/w/vale-caterpillar-and-sotreq-sign-agreement-to-expand-fleet-of-autonomous-trucks-in-the-northern-system-in-para.',
    annotation="Vale: Caterpillar autonomous truck expansion to ~90 by 2028. Supports caterpillar_vale_northern_autonomous_2025.",
    evid_note="Opened Vale press room English page 2026-10-02.",
)

# 7. lithium / prc — Ganfeng USD 180m convertible note into Lithium Argentina (PPG)
row_doc(
    "ganfeng_lar_convertible_180m_2026",
    "resources",
    "lithium",
    "prc",
    "Ganfeng Lithium — USD 180m convertible note into Lithium Argentina (PPG support)",
    "Argentina",
    "15 Sep 2026 (GlobeNewswire): Lithium Argentina closes USD 180 million strategic investment from Ganfeng Lithium via six-year unsecured convertible note (4.0% coupon; convert at USD 12.50/share); proceeds with cash to repay USD 259m notes due Jan 2027; PPG JV (67% Ganfeng / 33% LAR consolidating Pozuelos-Pastos Grandes basin, Salta) remains on track to complete by end-Sep 2026.",
    "180000000",
    "2026-09-15",
    "2026",
    "",
    "",
    "PPG / Pozuelos–Pastos Grandes basins, Salta — lat/lon blank (corporate note + basin JV; no single plant pin).",
    "globenewswire_lar_ganfeng_180m_20260915",
    "Lithium Argentina AG (“Lithium Argentina” or the “Company”) (TSX: LAR) (NYSE: LAR) today announced the closing of the $180 million strategic investment from Ganfeng Lithium Group Co., Ltd. (“Ganfeng”) through the issuance of a six-year unsecured convertible note (the “Note” or the “Strategic Investment”)… The Company’s joint venture with Ganfeng in respect of the consolidation of the Pozuelos-Pastos Grandes project (“PPG”) remains on track to be completed by the end of September 2026.",
    "https://www.globenewswire.com/news-release/2026/09/15/3361860/0/en/lithium-argentina-announces-closing-of-180m-strategic-investment-from-ganfeng.html",
    "Actor: Ganfeng Lithium (PRC) — prc; Lithium Argentina host partner. Opened GlobeNewswire company release 15 Sep 2026. Distinct from ganfeng_ppg_jv_framework_2025 and ganfeng_exar_cauchari_rigi_stage2_2026.",
    "hunt_cycle174",
    investment_type="acquisition",
    evidence="documented",
    bib_type="company",
    chicago='Lithium Argentina AG. “Lithium Argentina Announces Closing of $180M Strategic Investment from Ganfeng.” GlobeNewswire, September 15, 2026. https://www.globenewswire.com/news-release/2026/09/15/3361860/0/en/lithium-argentina-announces-closing-of-180m-strategic-investment-from-ganfeng.html.',
    annotation="GlobeNewswire/LAR: Ganfeng USD 180m convertible close supporting PPG. Supports ganfeng_lar_convertible_180m_2026.",
    evid_note="Opened GlobeNewswire LAR release 2026-10-02.",
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
    print(f"Cycle 174 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
