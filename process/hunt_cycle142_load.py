#!/usr/bin/env python3
"""Cycle 142 hunt: shuffle_seed=20261142; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: water, bridges_roads, balsa, building_materials, engineering_epc,
nickel, niobium, solar, port_cranes, rail, copper, fission_smr, port_ownership, wind,
graphite, lithium, power_plants_grid, other_renewables.

PRC ahead by 8 after 141 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr/nickel (dry → niobium).
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


# 1. bridges_roads / prc — CHEC Ruta 32 four-lane opening (distinct from contract row)
row_doc(
    "chec_ruta32_four_lane_open_2026",
    "infrastructure",
    "bridges_roads",
    "prc",
    "CHEC — Costa Rica Route 32 four-lane full opening (Río Frío–Limón)",
    "Costa Rica",
    "16 Jan 2026 CHEC Americas: Costa Rica MOPT/CONAVI announce full opening of Route 32 as four-lane highway — 104.24 km San José–Limón corridor; expanded from two to dual four lanes; 33 new bridges + rehabilitation of 33 existing bridges; multiple interchanges/overpasses/roundabouts; largest Chinese-company infrastructure project in Costa Rica / BRI Central America flagship. CapEx blank on opening page (contract USD already on chec_ruta32_costa_rica). Distinct COD/opening milestone vs 2024 contract observation.",
    "",
    "",
    "2026",
    "10.20",
    "-83.50",
    "Ruta 32 corridor Río Frío–Limón, Costa Rica (company geography; approximate mid-corridor pin).",
    "chec_ruta32_open_20260116",
    "Costa Rica’s Ministry of Public Works and Transport and the National Road Council recently announced the full opening of Route 32 as a four-lane highway… Stretching 104.24 kilometers, the Route 32 project is a key Belt and Road cooperation initiative between China and Central America and represents the largest infrastructure project undertaken by a Chinese company in Costa Rica. The project expanded the original two-lane road into a dual four-lane highway and included the construction of 33 new bridges, rehabilitation of 33 existing bridges",
    "https://www.checamerica.com/blog/2026/01/16/costa-rica-route-32-fully-opens-to-four-lane-traffic/",
    "Actor: CHEC / CCCC (PRC) — prc. Company English primary. CapEx blank (opening milestone; contract value on prior row). Distinct from chec_ruta32_costa_rica contract observation.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="company",
    chicago='China Harbour Engineering Company (CHEC Americas). “Costa Rica Route 32 Fully Opens to Four-Lane Traffic.” January 16, 2026. https://www.checamerica.com/blog/2026/01/16/costa-rica-route-32-fully-opens-to-four-lane-traffic/.',
    annotation="CHEC primary: Ruta 32 four-lane full opening Jan 2026; 104.24 km. Supports chec_ruta32_four_lane_open_2026.",
    evid_note="Opened CHEC Americas English post 16 Jan 2026 (Ruta 32 four-lane opening).",
)

# 2. solar / us — AES Dominicana Mirasol 100 MW COD
row_doc(
    "aes_dr_mirasol_100mw_2025",
    "energy",
    "solar",
    "us",
    "AES Dominicana Renewable Energy — Mirasol 100 MW solar COD (Guerra, Santo Domingo)",
    "Dominican Republic",
    "AES España B.V. consolidated IFRS 2025 (English): Mirasol solar plant in Santo Domingo province — 127 MW installed / 100 MW nominal; construction began 20 Jan 2023; operational since February 2025; 100% of generation to EDE Este. CapEx blank on financials. Distinct from aes_dr_peravia_140mw_cod_2025 and aes_dr_bess_138mw_94m_2025 (BESS co-located tranche naming Mirasol).",
    "",
    "",
    "2025",
    "18.55",
    "-69.70",
    "Guerra / Santo Domingo province, Dominican Republic (AES Mirasol site; approximate municipal pin).",
    "aes_espana_ifrs_2025_mirasol",
    "The \"Mirasol\" project began construction on January 20, 2023, of a solar power plant located in the province of Santo Domingo in the Dominican Republic, with an installed capacity of 127 MW (100 MW nominal). This plant has been operational since February 2025. 100% of the plant's generation is delivered to a single customer, EDE Este.",
    "https://www.aesdominicana.com/sites/aesvault.com/files/2026-06/NL63.%20EF%20AES%20Espa%C3%B1a%20BV%26Subs%20Consolidado%20IFRS%20-%20Emitido%202025%20%28Ingles%29.pdf",
    "Actor: AES Corporation via AES Dominicana Renewable Energy — us. Company English IFRS primary. CapEx blank. Distinct from Peravia COD and co-located BESS package rows.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago='AES España B.V. and Subsidiaries. Consolidated Financial Statements (IFRS) 2025 (English). Mirasol solar plant — 127 MW installed / 100 MW nominal; operational since February 2025. https://www.aesdominicana.com/sites/aesvault.com/files/2026-06/NL63.%20EF%20AES%20Espa%C3%B1a%20BV%26Subs%20Consolidado%20IFRS%20-%20Emitido%202025%20%28Ingles%29.pdf.',
    annotation="AES España IFRS 2025: Mirasol 100 MWn / 127 MWinst COD Feb 2025; EDE Este offtake. Supports aes_dr_mirasol_100mw_2025.",
    evid_note="Opened AES España IFRS 2025 English PDF (Mirasol COD Feb 2025; 100 MW nominal).",
)

# 3. solar / prc — Trina Solar Pampa del Infierno 150 MW (Argentina)
row_doc(
    "trina_pampa_del_infierno_150mw_argentina",
    "energy",
    "solar",
    "prc",
    "Trina Solar / TrinaTracker — Pampa del Infierno 150.18 MW PV + Vanguard-1P (Chaco)",
    "Argentina",
    "TrinaTracker product/case page: Pampa del Infierno solar project in Argentina — 150.18 MW capacity exclusively powered by Trina Solar NEG21C.20 675W modules with Vanguard-1P trackers. CapEx USD blank. Distinct from trina_colinas_vanguard_130mwp_2025 and trinatracker_cgn_lagoa_barro_2025.",
    "",
    "",
    "2024",
    "-26.52",
    "-61.17",
    "Pampa del Infierno, Chaco Province, Argentina (project namesake locality; approximate municipal pin).",
    "trina_pampa_del_infierno_case",
    "Announcing Pampa del Infierno, a transformative solar initiative located in Argentina. This project, exclusively powered by Trina Solar, boasts a remarkable capacity of 150MW. Anchored by Trina Solar's cutting-edge NEG21C.20 – 675W photovoltaic modules and employing the innovative Vanguard-1P tracker… Capacity：150.18 MW",
    "https://www.trinasolar.com/pt/trinatracker",
    "Actor: Trina Solar / TrinaTracker (PRC) — prc. Company English/PT product case. CapEx blank. Module+tracker supply at named Argentina utility-scale site.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Trina Solar (TrinaTracker). “Pampa del Infierno, Argentina” — 150.18 MW with NEG21C.20 675W modules and Vanguard-1P trackers. https://www.trinasolar.com/pt/trinatracker.',
    annotation="TrinaTracker primary case: Pampa del Infierno 150.18 MW Argentina. Supports trina_pampa_del_infierno_150mw_argentina.",
    evid_note="Opened TrinaTracker page (Pampa del Infierno 150.18 MW; Vanguard-1P + NEG21C.20).",
)

# 4. other_renewables / us — AES Andes Solar IV COD (hybrid PV+BESS)
row_doc(
    "aes_andes_solar_iv_cod_2024",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Andes Solar IV COD 211 MW PV + 130 MW / 5-hour BESS (Antofagasta)",
    "Chile",
    "22 Oct 2024 AES Andes: commercial operation of Andes Solar IV — 211 MW photovoltaic + 130 MW lithium BESS (5-hour) ~230 km east of Antofagasta in Atacama Desert; hub then cited as 667 MW solar + 259 MW batteries (largest operational BESS hub in LatAm at announcement). CapEx blank on COD release (hub cumulative investment narrative separate). Distinct from aes_andes_solar_iii_hub_2026 (Solar III COD Apr 2026 / hub 692+510 MW).",
    "",
    "",
    "2024",
    "-23.65",
    "-70.25",
    "Andes Solar Hub / Antofagasta Region, Chile (company geography; same approximate hub pin as Solar III).",
    "aes_andes_solar_iv_cod_20241022",
    "AES Andes announced today the start of commercial operation of Andes Solar IV, a park located 230 kilometers east of Antofagasta… With this milestone, an additional capacity of 211 MW of photovoltaic panels and 130 MW of energy storage for 5 hours based on lithium batteries is added, making it the hub with the largest operational battery system in Latin America.",
    "https://www.aesandes.com/en/press-release/aes-andes-begins-commercial-operation-andes-solar-iv-and-reaffirms-its-leadership",
    "Actor: AES Andes / AES Corporation — us. Company English primary. CapEx blank. Hybrid PV+BESS coded other_renewables. Distinct from Andes Solar III hub COD row.",
    "hunt_energy_other_renewables",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago='AES Andes. “AES Andes begins commercial operation of Andes Solar IV and reaffirms its leadership in battery storage in Latin America.” October 22, 2024. https://www.aesandes.com/en/press-release/aes-andes-begins-commercial-operation-andes-solar-iv-and-reaffirms-its-leadership.',
    annotation="AES Andes primary: Solar IV COD 211 MW PV + 130 MW/5h BESS Oct 2024. Supports aes_andes_solar_iv_cod_2024.",
    evid_note="Opened AES Andes English release 22 Oct 2024 (Andes Solar IV COD).",
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
    print(f"Cycle 142 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
