#!/usr/bin/env python3
"""Cycle 215 hunt: shuffle_seed=20261215; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261215).shuffle):
lithium, port_cranes, other_renewables, nickel, solar, port_ownership, niobium,
power_plants_grid, rail, water, engineering_epc, graphite, fission_smr, copper,
building_materials, wind, bridges_roads, balsa.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on EnergyX Black Giant/EXIM Argentina/Freeport El Abra/
Array Lupi/Nextracker Casa/AES Andes Hub/Bechtel QB2 desal blank/Fluor Quellaveco/
Wabtec/GE Vernova/USTDA/Equinix/SSA Marine sweeps (0 new U.S. rows — catalog dense).
PRC equal-budget: Zijin Liex RIGI / Goldwind Sento Sé / CAMCE Bluefields / ZPMC
Tecon Santos / PowerChina Vicuña Batidero already logged; holdovers unsigned.
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


# 1. water / allied — FCC Aqualia PTAR Cajamarca PPP >USD 123m
row_doc(
    "aqualia_ptar_cajamarca_123m_2026",
    "resources",
    "water",
    "allied",
    "FCC Aqualia — PTAR Cajamarca wastewater PPP (ProInversión)",
    "Peru",
    "17 Jul 2026 ProInversión awards FCC Aqualia S.A. the Cajamarca Wastewater Treatment Plant (PTAR) APP: design, finance, build, operate and maintain main wastewater collection system plus treatment plant (~0.6 m³/s / ~592 l/s average flow) ending untreated discharge to Mashcón, San Lucas and Cajamarquino rivers; >365,000 beneficiaries; ~26-year concession after definitive contract. CapEx face = USD 123.3 million project investment (Andina: superior to USD 123m; BNamericas cites CapEx USD 82m + Opex USD 41.3m). Distinct from aqualia_ptar_chincha_96p5m_2025.",
    "123300000",
    "2026-07-17",
    "2026",
    "-7.16",
    "-78.51",
    "Cajamarca city WWTP / Mashcón–Cajamarquino corridor, Cajamarca Region, Peru (project geography; municipal pin).",
    "andina_aqualia_ptar_cajamarca_20260717",
    "La Agencia de Promoción de la Inversión Privada (ProInversión) adjudicó el proyecto de la Planta de Tratamiento de Aguas Residuales (PTAR) de Cajamarca por un monto superior a los 123 millones de dólares. … la buena pro fue otorgada a la empresa FCC Aqualia S.A.",
    "https://andina.pe/agencia/noticia-proinversion-adjudica-proyecto-planta-tratamiento-mas-us-123-millones-1084090.aspx",
    "Actor: FCC Aqualia (Spain / FCC Group) — allied. Andina/ProInversión award primary; Aqualia company 27 Jul 2026 release corroborates award and 26-year scope. CapEx = USD 123.3m project face. Shuffle water.",
    "hunt_cycle215",
    investment_type="ppp_concession",
    evidence="documented",
    currency="USD",
    value_usd="123300000",
    fx_usd="1",
    bib_type="government",
    chicago='Agencia Andina. “ProInversión adjudica proyecto de planta de tratamiento por más de US $123 millones.” July 17, 2026. https://andina.pe/agencia/noticia-proinversion-adjudica-proyecto-planta-tratamiento-mas-us-123-millones-1084090.aspx.',
    annotation="FCC Aqualia PTAR Cajamarca >USD 123m / USD 123.3m. Supports aqualia_ptar_cajamarca_123m_2026.",
    evid_note="Opened Andina/ProInversión primary 2026-10-04; >USD 123m / FCC Aqualia / ~0.6 m³/s / Mashcón–San Lucas–Cajamarquino / >365k beneficiaries confirmed. Value stored as USD 123.3m (BNamericas CapEx+Opex project figure).",
)

# 2. copper / other — Codelco FY2026 authorized Inversión Real USD 3.289bn
row_doc(
    "codelco_fy2026_capex_3289m",
    "resources",
    "copper",
    "other",
    "Codelco — FY2026 authorized real investment (Presupuesto de Caja)",
    "Chile",
    "10 Dec 2025 Ministerio de Hacienda Decreto Exento 389 (totally processed Mar 2026): approves Codelco 2026 cash budget; Artículo 9 caps studies and investment projects under Inversión Real at USD 3,289,286,000 plus VAT (IVA Inversiones USD 615,464,000 → ~USD 3.915bn with VAT). Includes USD 100m Fondo de Aseguramiento de Activos Estratégicos. Copper price assumption 490 USc/lb; production IMF 1,344,002 t. Distinct from codelco_fy2025_capex_5073m.",
    "3289286000",
    "2025-12-10",
    "2026",
    "-33.45",
    "-70.66",
    "Codelco HQ Santiago, Chile (group CapEx authorization; multi-division).",
    "dipres_codelco_presupuesto_caja_2026",
    "Durante el ejercicio presupuestario 2026, los desembolsos en estudios y proyectos de inversión considerados en el ítem \"Inversión Real\" no podrán exceder la suma de USD 3.289.286.000, más IVA. … La inversión señalada precedentemente incluye también recursos por USD 100.000.000 para el Fondo de Aseguramiento de Activos Estratégicos.",
    "https://www.dipres.gob.cl/599/articles-406788_recurso_1.pdf",
    "Actor: Codelco (Chilean state copper SOE) — other. DIPRES/Ministerio de Hacienda decree primary (official PDF). CapEx face = USD 3.289286bn Inversión Real authorization (excl. VAT). Shuffle copper.",
    "hunt_cycle215",
    investment_type="capex",
    evidence="documented",
    currency="USD",
    value_usd="3289286000",
    fx_usd="1",
    bib_type="government",
    chicago='Ministerio de Hacienda / Dirección de Presupuestos (Chile). “Aprueba Presupuesto Anual de Caja de Codelco-Chile para el año 2026.” Decreto Exento 389, December 10, 2025. https://www.dipres.gob.cl/599/articles-406788_recurso_1.pdf.',
    annotation="Codelco FY2026 Inversión Real USD 3.289bn. Supports codelco_fy2026_capex_3289m.",
    evid_note="Opened DIPRES decree PDF 2026-10-04; Inversión Real USD 3,289,286,000 + IVA USD 615,464,000 / USD 100m strategic-asset fund / Dec Exento 389 confirmed.",
)

# 3. copper / other — ENAMI Nueva Paipote smelter modernization USD 1.7bn
row_doc(
    "enami_nueva_paipote_1700m_2025",
    "resources",
    "copper",
    "other",
    "ENAMI — Nueva Paipote / Fundición Hernán Videla Lira modernization",
    "Chile",
    "23 Dec 2025 ENAMI mandates J.P. Morgan and Citi as structuring banks to arrange financing covering estimated USD 1,700 million investment for modernization of Fundición Hernán Videla Lira (Paipote, Atacama) into an integrated metallurgical complex (smelter ~850,000 tpa concentrate + electrolytic refinery ~240,000 tpa cathodes); RCA already granted; works targeted from 1H 2026 (later SEIA pertinence may adjust schedule). Distinct from codelco_enami_qb_10pct_520m_2024 and Codelco–Glencore smelter MoU press.",
    "1700000000",
    "2025-12-23",
    "2025",
    "-27.45",
    "-70.27",
    "Paipote / Fundición Hernán Videla Lira, Atacama Region, Chile (project geography).",
    "portal_minero_enami_paipote_jpm_citi_20251223",
    "El proceso que deberán realizar los bancos seleccionados consiste en promover el megaproyecto y abrir espacios para que diversas entidades financieras puedan ofertar opciones para cubrir los US$1.700 millones de inversión estimados.",
    "https://www.portalminero.com/enami-selecciona-a-j-p-morgan-y-citi-como-bancos-estructuradores-del-financiamiento-de-fundicion-nueva-paipote",
    "Actor: ENAMI (Chilean state mining enterprise) — other. Portal Minero reprint of ENAMI mandate announcement (company quotes). CapEx estimate face = USD 1.7bn. Shuffle copper.",
    "hunt_cycle215",
    investment_type="capex",
    evidence="documented",
    currency="USD",
    value_usd="1700000000",
    fx_usd="1",
    bib_type="press",
    chicago='Portal Minero. “Enami selecciona a J.P. Morgan y Citi como bancos estructuradores del financiamiento de Fundición Nueva Paipote.” December 23, 2025. https://www.portalminero.com/enami-selecciona-a-j-p-morgan-y-citi-como-bancos-estructuradores-del-financiamiento-de-fundicion-nueva-paipote.',
    annotation="ENAMI Nueva Paipote USD 1.7bn financing mandate. Supports enami_nueva_paipote_1700m_2025.",
    evid_note="Opened Portal Minero 2026-10-04; USD 1.7bn estimated investment / J.P. Morgan+Citi structuring / Paipote FHVL / RCA / 850 ktpa smelter + 240 ktpa refinery confirmed from ENAMI quotes.",
)

# 4. port_cranes / allied — CapEx-fill Konecranes Portonave 14 e-RTG to USD 37.8m
row_doc(
    "konecranes_portonave_rtg_2025",
    "infrastructure",
    "port_cranes",
    "allied",
    "Konecranes — 14 electric RTGs for Portonave (Navegantes, Brazil)",
    "Brazil",
    "17 Apr 2025 Konecranes: Portonave orders 14 fully electric battery/busbar RTGs (booked Q4 2024; delivery mid-2026). CapEx-fill: DataPortuaria reports the 14-unit package valued at USD 37.8 million as first seven units enter service (Aug 2026 press). Distinct from zpmc_portonave_sts_2025 and portonave_ertg_210m_brl_2026.",
    "37800000",
    "2026-08-01",
    "2025",
    "-26.90",
    "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina, Brazil (company geography).",
    "dataportuaria_portonave_ertg_37p8m_2026",
    "Portonave incorporated seven new Konecranes electric RTG cranes, 28 meters high and 150 tons, as the first units of a purchase of 14. Valued at USD 37.8 million, they are expected to become operational in mid-August.",
    "https://dataportuaria.com/en/brasil/logistics/portonave-incorporates-seven-electric-rtg-cranes-for-usd-37",
    "Actor: Konecranes (Finland) — allied; buyer Portonave (Brazil). CapEx-fill upgrade from blank using DataPortuaria USD 37.8m for 14 e-RTG package (Konecranes company release had no USD). Shuffle port_cranes.",
    "hunt_cycle215",
    investment_type="equipment_supply",
    evidence="proxy",
    currency="USD",
    value_usd="37800000",
    fx_usd="1",
    bib_type="press",
    chicago='DataPortuaria. “Portonave incorporates seven electric RTG cranes for USD 37.8 million.” 2026. https://dataportuaria.com/en/brasil/logistics/portonave-incorporates-seven-electric-rtg-cranes-for-usd-37.',
    annotation="Konecranes Portonave 14 e-RTG CapEx-fill USD 37.8m. Supports konecranes_portonave_rtg_2025.",
    evid_note="Opened DataPortuaria 2026-10-04; USD 37.8m / 14 Konecranes e-RTGs / first seven incorporated confirmed. UNVERIFIED proxy CapEx-fill vs Konecranes company release (no USD).",
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
    print(f"cycle215 added {len(added)}: {added}")
    print(f"cycle215 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
