#!/usr/bin/env python3
"""Cycle 212 hunt: shuffle_seed=20261212; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261212).shuffle):
wind, building_materials, engineering_epc, niobium, bridges_roads, fission_smr, water,
solar, port_ownership, other_renewables, lithium, graphite, balsa, rail, port_cranes,
power_plants_grid, nickel, copper.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Black Giant/DFC Serra/
EnergyX/Nextracker/Array/Wabtec MRS/GE Vernova São Simão/Bechtel/Fluor/
Fluence/USTDA/Equinix/Freeport El Abra/SSA Marine sweeps (0 new U.S. rows —
catalog dense; CapEx fills this cycle are allied/other). PRC equal-budget:
PowerChina Chile Decree 4 / Dune Plus / Palmira / State Grid UHV / ZPMC /
CAMCE Bluefields already logged; holdovers unsigned.
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


# 1. wind / allied — Vestas Aquiraz factory CapEx R$130m (V163-4.5 MW localization)
row_doc(
    "vestas_aquiraz_factory_130m_brl_2024",
    "energy",
    "wind",
    "allied",
    "Vestas — Aquiraz hub/nacelle factory investment for V163-4.5 MW (Ceará)",
    "Brazil",
    "9 Aug 2024: Vestas announces R$ 130 million investment to produce the V163-4.5 MW turbine at its hub/nacelle assembly plant in Aquiraz, Ceará; blades also to be manufactured in Ceará near Porto do Pecém (Aeris). Distinct from vestas_dom_inocencio_br_2025 turbine-supply order and vestas_casa_dos_ventos_br_2023.",
    "130000000",
    "2024-08-09",
    "2024",
    "-3.901",
    "-38.391",
    "Vestas Aquiraz factory, Ceará (company/press geography; municipal pin).",
    "terra_vestas_aquiraz_130m_20240809",
    "A dinamarquesa Vestas anunciou nesta sexta-feira que investirá 130 milhões de reais para produzir um novo modelo de turbina eólica em sua fábrica de montagem de hubs e naceles em Aquiraz, no Ceará.",
    "https://www.terra.com.br/economia/vestas-investira-r130-mi-para-fabricar-nova-turbina-eolica-no-ceara,f9d1fbc4a6527698ae571e35682da9c8wlp8f5rc.html",
    "Actor: Vestas (Denmark) — allied. Press reporting Vestas announcement (Terra 9 Aug 2024). CapEx face = R$130m factory localization. USD blank (Fed H.10 unreachable). Shuffle wind.",
    "hunt_cycle212",
    investment_type="manufacturing_capex",
    evidence="proxy",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='Terra / Reuters. “Vestas investirá R$130 mi para fabricar nova turbina eólica no Ceará.” August 9, 2024. https://www.terra.com.br/economia/vestas-investira-r130-mi-para-fabricar-nova-turbina-eolica-no-ceara,f9d1fbc4a6527698ae571e35682da9c8wlp8f5rc.html.',
    annotation="Vestas Aquiraz factory CapEx R$130m. Supports vestas_aquiraz_factory_130m_brl_2024.",
    evid_note="Opened Terra Portuguese press 2026-10-04; R$130m / Aquiraz hubs-nacelles / V163-4.5 MW / Pecém blades confirmed. UNVERIFIED proxy vs company press-room (MME page unreachable).",
)

# 2. other_renewables / other — Codelco first MIGA climate financing USD 532m (2024)
row_doc(
    "codelco_miga_climate_financing_532m_2024",
    "energy",
    "other_renewables",
    "other",
    "Codelco — first MIGA-guaranteed climate financing (Crédit Agricole CIB)",
    "Chile",
    "23 Jul 2024 Codelco: secures first climate financing of USD 532 million from Crédit Agricole CIB, guaranteed by World Bank Group MIGA, to finance transition to a 100% renewable electricity mix by 2030 (PPA renewals with Engie, Colbún, AES Andes and 1.8 TWh/year renewable tender). Distinct from codelco_miga_climate_financing_600m_2025 (second tranche Dec 2025).",
    "532000000",
    "2024-07-23",
    "2024",
    "-33.45",
    "-70.66",
    "Codelco HQ / Chile system-wide renewable PPA program (Santiago pin; no single plant site).",
    "codelco_miga_climate_532m_20240723",
    "Un hito histórico logró Codelco al asegurar un financiamiento climático por US$532 millones otorgado por el banco francés Crédit Agricole CIB y que contó con la garantía de la Agencia Multilateral de Garantía de Inversiones (MIGA por su sigla en inglés), una entidad del Grupo Banco Mundial.",
    "https://www.codelco.com/codelco-emitio-su-primer-financiamiento-climatico-por-us-532-millones",
    "Actor: Codelco (Chilean state copper SOE) borrower — other. Opened Codelco Spanish primary 23 Jul 2024. Financing face = USD 532m. Shuffle other_renewables.",
    "hunt_cycle212",
    investment_type="financing",
    evidence="documented",
    currency="USD",
    value_usd="532000000",
    fx_usd="1",
    bib_type="company",
    chicago='Codelco. “Codelco emitió su primer financiamiento climático por US$532 millones.” July 23, 2024. https://www.codelco.com/codelco-emitio-su-primer-financiamiento-climatico-por-us-532-millones.',
    annotation="Codelco first MIGA climate financing USD 532m. Supports codelco_miga_climate_financing_532m_2024.",
    evid_note="Opened Codelco Spanish primary 2026-10-04; USD 532m Crédit Agricole / MIGA / renewable matrix to 2030 confirmed.",
)

# 3. rail / allied — CapEx-fill Siemens EFE ETCS (2,968,596 UF / ~USD 125.8m)
row_doc(
    "siemens_efe_etcs_chile_2025",
    "infrastructure",
    "rail",
    "allied",
    "Siemens Mobility — ETCS Level 2 / Signaling X for EFE Trenes de Chile (Alameda–Melipilla + Santiago–Batuco)",
    "Chile",
    "EFE awards Siemens Mobility signaling for Tren Alameda–Melipilla + Tren Santiago–Batuco: first ETCS Level 2 and Signaling X in Chile/LatAm across 87 km (61 km Melipilla + 26 km Batuco); 5-year install + 10-year maintenance; onboard systems for 32 trains. CapEx-fill: EFE states signaling award 2.968.596 UF; PortalPortuario cites ~USD 125.8 million equivalent. Distinct from crcc_efe_santiago_batuco_2025 civil works and indra_efe_comms_chile_2025.",
    "2968596",
    "2025-12-10",
    "2025",
    "-33.45",
    "-70.65",
    "Santiago metropolitan EFE corridors (Siemens Mobility / EFE geography).",
    "efe_siemens_indra_adjudicacion_20251210",
    "En total, el sistema de señalización, adjudicado a Siemens Mobility (Alemania), alcanza una inversión de 2.968.596 UF, mientras que el sistema de comunicaciones, adjudicado a Indra Sistemas Chile S.A., filial del grupo español Indra, considera 1.480.508 UF.",
    "https://www.efe.cl/efe-avanza-en-modernizacion-ferroviaria-con-nuevas-adjudicaciones-tecnologicas-a-siemens-e-indra-para-los-proyectos-melipilla-y-batuco/",
    "Actor: Siemens Mobility (Germany) — allied. CapEx-fill upgrade from blank using EFE primary UF award; USD 125.8m from PortalPortuario UF→USD paraphrase. Shuffle rail.",
    "hunt_cycle212",
    investment_type="equipment_supply",
    evidence="documented",
    currency="UF",
    value_usd="125800000",
    fx_usd="",
    bib_type="company",
    chicago='EFE Trenes de Chile. “EFE avanza en modernización ferroviaria con nuevas adjudicaciones tecnológicas a Siemens e Indra para los proyectos Melipilla y Batuco.” December 10, 2025. https://www.efe.cl/efe-avanza-en-modernizacion-ferroviaria-con-nuevas-adjudicaciones-tecnologicas-a-siemens-e-indra-para-los-proyectos-melipilla-y-batuco/.',
    annotation="Siemens EFE ETCS CapEx-fill 2.968.596 UF (~USD 125.8m). Supports siemens_efe_etcs_chile_2025.",
    evid_note="Opened EFE Spanish primary 2026-10-04; 2.968.596 UF Siemens signaling / 87 km ETCS L2 confirmed. USD 125.8m from PortalPortuario secondary conversion entered as value_usd.",
)

# 4. rail / allied — Indra EFE communications package (1,480,508 UF / ~USD 62.7m)
row_doc(
    "indra_efe_comms_chile_2025",
    "infrastructure",
    "rail",
    "allied",
    "Indra Sistemas Chile — communications systems for EFE Melipilla + Batuco",
    "Chile",
    "10 Dec 2025 EFE: awards Indra Sistemas Chile S.A. the communications package for Tren Alameda–Melipilla and Tren Santiago–Batuco (integrated data channels, CCTV, passenger info, voice/intercom, 30-day recording backup; supervised from integrated operations control center). Award face 1.480.508 UF (~USD 62.7m per PortalPortuario). Distinct from siemens_efe_etcs_chile_2025 signaling award.",
    "1480508",
    "2025-12-10",
    "2025",
    "-33.45",
    "-70.65",
    "Santiago metropolitan EFE corridors (EFE award geography).",
    "efe_siemens_indra_adjudicacion_20251210",
    "En total, el sistema de señalización, adjudicado a Siemens Mobility (Alemania), alcanza una inversión de 2.968.596 UF, mientras que el sistema de comunicaciones, adjudicado a Indra Sistemas Chile S.A., filial del grupo español Indra, considera 1.480.508 UF.",
    "https://www.efe.cl/efe-avanza-en-modernizacion-ferroviaria-con-nuevas-adjudicaciones-tecnologicas-a-siemens-e-indra-para-los-proyectos-melipilla-y-batuco/",
    "Actor: Indra (Spain) via Indra Sistemas Chile — allied. EFE Spanish primary. CapEx face = 1.480.508 UF; USD 62.7m secondary conversion. Shuffle rail.",
    "hunt_cycle212",
    investment_type="equipment_supply",
    evidence="documented",
    currency="UF",
    value_usd="62700000",
    fx_usd="",
    bib_type="company",
    chicago='EFE Trenes de Chile. “EFE avanza en modernización ferroviaria con nuevas adjudicaciones tecnológicas a Siemens e Indra para los proyectos Melipilla y Batuco.” December 10, 2025. https://www.efe.cl/efe-avanza-en-modernizacion-ferroviaria-con-nuevas-adjudicaciones-tecnologicas-a-siemens-e-indra-para-los-proyectos-melipilla-y-batuco/.',
    annotation="Indra EFE communications 1.480.508 UF (~USD 62.7m). Supports indra_efe_comms_chile_2025.",
    evid_note="Opened EFE Spanish primary 2026-10-04; 1.480.508 UF Indra communications package confirmed. USD 62.7m from PortalPortuario secondary conversion entered as value_usd.",
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
    print(f"cycle212 added {len(added)}: {added}")
    print(f"cycle212 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
