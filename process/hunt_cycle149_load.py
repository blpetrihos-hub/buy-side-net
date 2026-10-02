#!/usr/bin/env python3
"""Cycle 149 hunt: shuffle_seed=20261149; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: balsa, power_plants_grid, solar, fission_smr,
engineering_epc, port_ownership, niobium, building_materials, rail, graphite,
port_cranes, bridges_roads, other_renewables, copper, nickel, wind, water,
lithium.

PRC ahead by 13 after 148 — keep equal US/PRC budget without padding.
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


# 1. solar / us — AES Dominicana Bayasol ~USD 60m / 58 MWp
row_doc(
    "aes_bayasol_60m_dr_2021",
    "energy",
    "solar",
    "us",
    "AES Dominicana — Parque Solar Bayasol NTP (Matanzas, Peravia)",
    "Dominican Republic",
    "16 Mar 2021 AES Dominicana: groundbreaking for AES Bayasol solar park in Angostura, Matanzas, Peravia — peak installed capacity 58 MW; approximate investment USD 60 million; ~145k panels / 405 Wp; EPC TSK (Spain). First AES DR utility-scale renewable (private PPAs with Cemex / Multiquímica / Nestlé). Distinct from aes_dr_mirasol_100mw_2025 and aes_dr_peravia_140mw_cod_2025. Investor presentation later lists Bayasol COD Q2 2021.",
    "60000000",
    "2021-03-16",
    "2021",
    "18.250",
    "-70.420",
    "Angostura / Matanzas, Peravia Province, Dominican Republic (AES site naming).",
    "aes_dr_bayasol_ntp_20210316",
    "Con una inversión aproximada a los U$60 millones, el Grupo AES Dominicana dejó iniciados los trabajos para la construcción del parque AES Bayasol, que tendrá una capacidad pico instalada de 58 megavatios de fuente solar",
    "https://www.aesdominicana.com/en/press-release/inicia-la-construccion-del-parque-solar-aes-bayasol-con-inversion-de-us60-mm-0",
    "Actor: AES Dominicana / AES Corporation (U.S.) — us. Company primary for CapEx + peak capacity at NTP. EPC TSK is allied contractor (not side tag).",
    "hunt_energy_solar",
    investment_type="greenfield",
    chicago='AES Dominicana. “Inicia la construcción del parque solar AES Bayasol con inversión de US$60 MM.” March 16, 2021. https://www.aesdominicana.com/en/press-release/inicia-la-construccion-del-parque-solar-aes-bayasol-con-inversion-de-us60-mm-0.',
    annotation="AES Dominicana: Bayasol ~USD 60m / 58 MWp NTP. Supports aes_bayasol_60m_dr_2021.",
    evid_note="Opened AES Dominicana Bayasol NTP primary (USD 60m; 58 MWp).",
)

# 2. solar / us — AES Dominicana Santanasol ~USD 45m / 50 MW
row_doc(
    "aes_santanasol_45m_dr_2021",
    "energy",
    "solar",
    "us",
    "AES Dominicana — Parque Solar Santanasol financing (Peravia)",
    "Dominican Republic",
    "23 Jun 2021 AES Dominicana: Scotiabank green loan USD 36m / 5 years for Santanasol solar construction; estimated project investment USD 45 million; generation capacity 50 MW; Peravia Province. Investor presentation lists Santanasol COD Q2 2022. Distinct from aes_bayasol_60m_dr_2021 and aes_dr_peravia_140mw_cod_2025.",
    "45000000",
    "2021-06-23",
    "2021",
    "18.280",
    "-70.380",
    "Peravia Province, Dominican Republic (AES site naming; south of country).",
    "aes_dr_santanasol_scotiabank_20210623",
    "The photovoltaic plant will involve an estimated investment of US$45 million and is part of AES Dominicana's sustainability strategy to reduce its environmental footprint. It will have a generation capacity of 50 MW",
    "https://www.aesdominicana.com/en/press-release/aes-dominicana-y-scotiabank-suscriben-acuerdo-de-prestamo-verde-por-us36-millones",
    "Actor: AES Dominicana / AES Corporation (U.S.) — us. Company primary for estimated CapEx + capacity at green-loan signing.",
    "hunt_energy_solar",
    investment_type="greenfield",
    chicago='AES Dominicana. “AES Dominicana y Scotiabank suscriben acuerdo de préstamo verde por US$36 millones para proyecto de energía solar.” June 23, 2021. https://www.aesdominicana.com/en/press-release/aes-dominicana-y-scotiabank-suscriben-acuerdo-de-prestamo-verde-por-us36-millones.',
    annotation="AES Dominicana: Santanasol estimated USD 45m / 50 MW. Supports aes_santanasol_45m_dr_2021.",
    evid_note="Opened AES Dominicana Santanasol financing primary (USD 45m est.; 50 MW).",
)

# 3. solar / prc — CREC / China Railway International GUYSOL portfolio 18 MW / 12 MWh
row_doc(
    "crec_guyana_guysol_18mw_2025",
    "energy",
    "solar",
    "prc",
    "China Railway International (CREC) — Guyana Solar Power and Energy Storage portfolio COD unveil",
    "Guyana",
    "1 Nov 2025 CREC: completion/unveil of Onderneeming Station as first station of Guyana Solar Power and Energy Storage Project jointly constructed by China Railway International Group under China Railway Group Limited — five independent solar plants across three regions; total 18 MW PV + 12 MWh storage; Onderneeming 5 MW / 7.5 MWh. CapEx blank on CREC primary. Prefer plant-level CapEx rows already logged to SUMEC–XJ (sumec_guyana_onderneeming_solar_10p4m_2025 etc.); this row records CREC portfolio-level COD claim only.",
    "",
    "",
    "2025",
    "7.250",
    "-58.480",
    "Onderneeming Station (first of five), Essequibo Coast, Guyana (CREC naming); portfolio spans three administrative regions.",
    "crec_guyana_guysol_onderneeming_20251101",
    "The Guyana Solar Power and Energy Storage Project, jointly constructed by China Railway International Group under China Railway Group Limited, is the largest solar photovoltaic project in Guyana’s history. The project consists of five independent solar power plants distributed across three administrative regions of Guyana, with a total installed capacity of 18 MW and an energy storage capacity of 12 MWh. The first completed and commissioned station—Onderneeming Station—is the largest among the five, with an installed capacity of 5 MW and 7.5 MWh of energy storage.",
    "https://www.crecg.com/zgztywz/cs11/10210606/2025111313575088155/index.html",
    "Actor: China Railway International / China Railway Group (PRC SOE) — prc. Company English primary for portfolio COD unveil. CapEx blank; SUMEC–XJ remains plant-level EPC per DPI.",
    "hunt_energy_solar",
    investment_type="epc",
    chicago='China Railway Group Limited (CREC). “First Station of Guyana Solar Power and Energy Storage Project Delivered and Put into Operation.” November 14, 2025. https://www.crecg.com/zgztywz/cs11/10210606/2025111313575088155/index.html.',
    annotation="CREC: Guyana GUYSOL portfolio 18 MW / 12 MWh COD unveil. Supports crec_guyana_guysol_18mw_2025.",
    evid_note="Opened CREC Guyana GUYSOL portfolio COD primary (18 MW / 12 MWh; CapEx blank).",
)

# 4. solar / prc — SUMEC–XJ GUYSOL Charity 3 MWp COD (CapEx blank)
row_doc(
    "sumec_guyana_charity_3mw_2025",
    "energy",
    "solar",
    "prc",
    "SUMEC–XJ Group JV — GUYSOL Charity 3 MWp solar COD (Region Two)",
    "Guyana",
    "14 Sep 2026 DPI Guyana (OPM review): five GUYSOL solar farms now feeding the grid — Onderneeming, Hampshire, Prospect, Trafalgar and Charity — together 18 MW; Charity listed as 3 MWp solar farm in Region Two. EPC for Essequibo/Berbice GUYSOL lots is SUMEC–XJ JV (named at Hampshire/Prospect commissionings; same US$38m Regions 2/5/6 contract). CapEx blank on plant-level primary (programme/contract figures not allocated to Charity alone). Distinct from sumec_guyana_prospect_solar_5p5m_2025 / sumec_guyana_hampshire_3mw_2025 / sumec_guyana_onderneeming_solar_10p4m_2025.",
    "",
    "",
    "2026",
    "7.380",
    "-58.600",
    "Charity, Pomeroon / Region Two, Guyana (DPI site naming).",
    "dpi_guyana_charity_solar_opm_20260914",
    "Five new solar farms are now feeding power into the national grid. Onderneeming, Hampshire, Prospect, Trafalgar and Charity together add 18 megawatts of renewable energy… The 3 MWp solar farm at Charity in Region Two",
    "https://dpi.gov.gy/opm-continues-to-deliver-affordable-reliable-energy-to-communities/",
    "Actor: SUMEC (SINOMACH) + XJ Group (PRC) JV — prc (programme EPC). Official DPI English primary for Charity COD status + 3 MWp. CapEx blank.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="government",
    chicago='Department of Public Information, Guyana. “OPM continues to deliver affordable, reliable energy to communities.” September 14, 2026. https://dpi.gov.gy/opm-continues-to-deliver-affordable-reliable-energy-to-communities/.',
    annotation="DPI Guyana: Charity 3 MWp among five GUYSOL farms online. Supports sumec_guyana_charity_3mw_2025.",
    evid_note="Opened DPI OPM Charity COD status primary (3 MWp; CapEx blank).",
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
    print(f"Cycle 149 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
