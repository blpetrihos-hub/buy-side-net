#!/usr/bin/env python3
"""Cycle 139 hunt: shuffle_seed=20261139; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: other_renewables, fission_smr, building_materials, port_cranes,
rail, engineering_epc, lithium, bridges_roads, wind, water, solar, power_plants_grid,
nickel, graphite, balsa, niobium, port_ownership, copper.

PRC ahead by 6 after 138 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite/nickel (dry → fission_smr → niobium).
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


# 1. other_renewables / allied — ENGIE Chile BESS Libélula COD (USD 219m BESS tranche)
row_doc(
    "engie_bess_libelula_cod_219m_2026",
    "energy",
    "other_renewables",
    "allied",
    "ENGIE Chile — BESS Libélula 203 MW / 1,034 MWh COD (Colina/Tiltil)",
    "Chile",
    "28 Aug 2026 ENGIE Chile: commercial operation of BESS Libélula at hybrid PV+BESS complex in Colina and Tiltil (Región Metropolitana) — 203 MW / 1,034 MWh (208 Li-ion containers; 5-hour discharge); BESS CapEx USD 219 million of complex USD 320 million; PV 140 MW / 245,560 panels 100% energized pending COD; 220 kV / ~16 km line to El Manzano; complements Nextracker NX Horizon tracker supply row.",
    "219000000",
    "2026-08-28",
    "2026",
    "-33.20",
    "-70.80",
    "Colina / Tiltil, Región Metropolitana, Chile (ENGIE Libélula site; approximate).",
    "engie_bess_libelula_los_loros_cod_20260828",
    "ENGIE Chile anunció la entrada en operación comercial (COD) de BESS Libélula y BESS Los Loros… El complejo representa una inversión en su conjunto de US$320 millones, de los cuales US$ 219 millones corresponde a BESS… el BESS alcanza una potencia máxima bruta de 203 MW y una capacidad de almacenamiento de 1.034 MWh, conformado por 208 contenedores de baterías de ion litio",
    "https://www.engie.cl/impulsamos-la-transicion-energetica-con-la-entrada-en-operacion-de-dos-nuevos-parques-de-almacenamiento/",
    "Actor: ENGIE Chile (French ENGIE) — allied. Company Spanish primary. CapEx USD 219m BESS tranche documented. Distinct from nextracker_libelula_engie_chile_2025 (U.S. tracker OEM) and engie_bess_tocopilla_cod_170m_2026.",
    "hunt_energy_other_renewables",
    investment_type="greenfield",
    bib_type="company",
    chicago='ENGIE Chile. “Impulsamos la transición energética con la entrada en operación de dos nuevos parques de almacenamiento.” August 28, 2026. https://www.engie.cl/impulsamos-la-transicion-energetica-con-la-entrada-en-operacion-de-dos-nuevos-parques-de-almacenamiento/.',
    annotation="ENGIE Chile primary: BESS Libélula COD 203 MW/1,034 MWh; CapEx USD 219m. Supports engie_bess_libelula_cod_219m_2026 and engie_bess_los_loros_cod_64m_2026.",
    evid_note="Opened ENGIE Chile Spanish release 28 Aug 2026 (Libélula BESS COD + CapEx USD 219m).",
)

# 2. other_renewables / allied — ENGIE Chile BESS Los Loros COD (USD 64m)
row_doc(
    "engie_bess_los_loros_cod_64m_2026",
    "energy",
    "other_renewables",
    "allied",
    "ENGIE Chile — BESS Los Loros 48 MW / 275.23 MWh COD (Tierra Amarilla)",
    "Chile",
    "28 Aug 2026 ENGIE Chile: commercial operation of BESS Los Loros co-located at Parque Fotovoltaico Los Loros (Tierra Amarilla, Atacama) — 48 MW / 275.23 MWh; 63 LFP containers; CapEx USD 64 million; joint Libélula+Los Loros BESS investment USD 283 million stated on same release. Distinct from Libélula BESS COD row.",
    "64000000",
    "2026-08-28",
    "2026",
    "-27.48",
    "-70.27",
    "Tierra Amarilla, Región de Atacama, Chile (Los Loros PV + BESS; approximate).",
    "engie_bess_libelula_los_loros_cod_20260828",
    "BESS Los Loros está ubicado en el Parque Fotovoltaico Los Loros… El sistema representa una inversión de US$ 64 millones y cuenta con 48 MW de potencia máxima bruta y 275.23 MWh de capacidad de almacenamiento… 63 contenedores de baterías de litio-ferrofosfato… Se trata de BESS Libélula y BESS Los Loros… con una inversión conjunta de US$ 283 millones.",
    "https://www.engie.cl/impulsamos-la-transicion-energetica-con-la-entrada-en-operacion-de-dos-nuevos-parques-de-almacenamiento/",
    "Actor: ENGIE Chile (French ENGIE) — allied. Company Spanish primary. CapEx USD 64m. Distinct from engie_bess_libelula_cod_219m_2026 / engie_bess_tocopilla_cod_170m_2026.",
    "hunt_energy_other_renewables",
    investment_type="greenfield",
    bib_type="company",
    chicago='ENGIE Chile. “Impulsamos la transición energética con la entrada en operación de dos nuevos parques de almacenamiento.” August 28, 2026. https://www.engie.cl/impulsamos-la-transicion-energetica-con-la-entrada-en-operacion-de-dos-nuevos-parques-de-almacenamiento/.',
    annotation="ENGIE Chile primary: BESS Los Loros COD 48 MW/275.23 MWh; CapEx USD 64m. Supports engie_bess_los_loros_cod_64m_2026.",
    evid_note="Opened ENGIE Chile Spanish release 28 Aug 2026 (Los Loros BESS COD + CapEx USD 64m).",
)

# 3. solar / us — GameChange Solar 715 MWp LATAM tracker portfolio
row_doc(
    "gamechange_715mwp_latam_2025",
    "energy",
    "solar",
    "us",
    "GameChange Solar — 715 MWp trackers/fixed-tilt across 8 LatAm projects",
    "Colombia",
    "23 Jun 2025 GameChange Solar (Norwalk, CT): eight new solar projects totaling 715 MWp — four in Colombia, three in Chile (incl. Antofagasta desert conditions), one in El Salvador; seven Genius Tracker single-axis + one MaxSpan fixed-tilt. Project names/developers not disclosed on opened page — CapEx blank. Country pin = Colombia (plurality of sites).",
    "",
    "",
    "2025",
    "10.97",
    "-74.78",
    "Caribbean Colombia cluster (company geography; four of eight projects; approximate Barranquilla pin).",
    "gamechange_715mwp_latam_20250623",
    "June 23, 2025 – Norwalk, CT – GameChange Solar announced a significant expansion in Latin America today with eight new solar projects, including three in Chile, one in El Salvador, and four in Colombia, totaling 715 MWp. … The projects include seven with Genius Tracker™ single-axis trackers and one with a MaxSpan™ fixed-tilt system.",
    "https://www.gamechangesolar.com/news/gamechange-solar-expands-latam-footprint-with-eight-new-solar-projects-totaling-715-mwp",
    "Actor: GameChange Solar (Norwalk, CT HQ) — us. Company English primary. CapEx blank; sites unnamed beyond country mix. Distinct from Nextracker Casa dos Ventos / Array Lupi / Gonvarri SolarSteel rows.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='GameChange Solar. “GameChange Solar Expands LATAM Footprint with Eight New Solar Projects Totaling 715 MWp.” June 23, 2025. https://www.gamechangesolar.com/news/gamechange-solar-expands-latam-footprint-with-eight-new-solar-projects-totaling-715-mwp.',
    annotation="GameChange primary: 715 MWp trackers across 8 Chile/Colombia/El Salvador projects. Supports gamechange_715mwp_latam_2025.",
    evid_note="Opened GameChange Solar English release 23 Jun 2025 (715 MWp / 8 LatAm projects).",
)

# 4. solar / prc — TrinaTracker Vanguard 1P for Projeto Colinas 130 MWp (Pernambuco)
row_doc(
    "trina_colinas_vanguard_130mwp_2025",
    "energy",
    "solar",
    "prc",
    "TrinaTracker — Vanguard 1P trackers for Projeto Colinas 130 MWp (Pernambuco)",
    "Brazil",
    "27 Aug 2025 / published 8 Sep 2025 Trinasolar Brazil: TrinaTracker supply contract for Projeto Colinas (Kroma Energia + Elétron Energy PPP with Compesa) in Garanhuns and Brejão, Pernambuco — 130 MWp with Vanguard 1P + SuperTrack AI; FINAME-eligible locally manufactured equipment; COD targeted May 2026; >200k modules / 175 ha. Tracker CapEx USD not disclosed.",
    "",
    "",
    "2025",
    "-8.89",
    "-36.49",
    "Garanhuns / Brejão, Pernambuco, Brazil (Projeto Colinas; approximate municipal pin).",
    "trina_colinas_vanguard_20250908",
    "A Trina Tracker… anuncia a assinatura de um contrato para o fornecimento de seu sistema de rastreamento solar para o Projeto Colinas… Localizado nos municípios de Garanhuns e Brejão, Pernambuco, e com capacidade instalada de 130 MWp, o empreendimento contará com a solução Vanguard 1P, equipada com a tecnologia SuperTrack… Com previsão de operação para maio de 2026",
    "https://www.trinasolar.com/br/resources/newsroom/tue-20250909-0835/",
    "Actor: TrinaTracker / Trina Solar (PRC) — prc; developers Kroma/Elétron (Brazilian). Company Portuguese primary. CapEx blank. Distinct from trina_cemig_sim / trina_pillanco / trinatracker_cgn_lagoa_barro rows.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Trinasolar. “Trina Tracker fornecerá 130 MWp de rastreadores solares para o Projeto Colinas, situado em Pernambuco.” September 8, 2025. https://www.trinasolar.com/br/resources/newsroom/tue-20250909-0835/.',
    annotation="TrinaTracker primary: Vanguard 1P for Colinas 130 MWp (PE). Supports trina_colinas_vanguard_130mwp_2025.",
    evid_note="Opened Trinasolar Brazil Portuguese release 8 Sep 2025 (Colinas 130 MWp Vanguard 1P).",
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
    print(f"Cycle 139 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
