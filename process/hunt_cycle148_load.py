#!/usr/bin/env python3
"""Cycle 148 hunt: shuffle_seed=20261148; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: nickel, niobium, lithium, water, balsa, rail,
engineering_epc, building_materials, graphite, solar, fission_smr, wind,
power_plants_grid, port_ownership, copper, port_cranes, other_renewables,
bridges_roads.

Also logs ContourGlobal HQ retag (London → allied) applied before load:
5 active rows us→allied (oasis_atacama, victor_jara, los_maitenes, quillagua, condor).

PRC ahead after Contour retag — keep equal US/PRC budget without padding.
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


# 1. solar / us — AES Colombia Parque Solar Brisas 26 MWp COD (Aipe, Huila)
row_doc(
    "aes_brisas_26mw_colombia_2023",
    "energy",
    "solar",
    "us",
    "AES Colombia — Parque Solar Brisas COD (Aipe, Huila)",
    "Colombia",
    "27 Jan 2023 Ecopetrol: AES Colombia put Brisas solar self-generation park into operation in Aipe, Huila — 26 MWp; 21 ha / >49k bifacial tracker panels; built under 15-year energy-supply contract for Ecopetrol Huila operations. Distinct from aes_san_fernando_61mw_colombia_2021 and aes_castilla_21mw_colombia_2019. CapEx blank on Ecopetrol primary (El Tiempo press cites ~USD 21.2m — UNVERIFIED proxy, not logged).",
    "",
    "",
    "2023",
    "3.222",
    "-75.240",
    "Aipe municipality, Huila Department, Colombia (Ecopetrol site naming).",
    "ecopetrol_aes_brisas_20230127",
    "Ecopetrol y AES Colombia pusieron en marcha el ecoparque de autogeneración de energía solar Brisas, ubicado en el municipio de Aipe, departamento del Huila, que tiene una capacidad instalada de 26 megavatios (MWp) una extensión de 21 hectáreas",
    "https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/ecopetrol-y-aes-inauguraron-ecoparque-solar-en-huila",
    "Actor: AES Colombia / AES Corporation (U.S.) — us. Ecopetrol official primary for COD + capacity. CapEx blank (no figure on primary).",
    "hunt_energy_solar",
    investment_type="epc",
    chicago='Ecopetrol S.A. “Ecopetrol y AES inauguraron ecoparque solar en Huila.” January 27, 2023. https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/ecopetrol-y-aes-inauguraron-ecoparque-solar-en-huila.',
    annotation="Ecopetrol: AES Colombia Brisas 26 MWp COD Aipe Huila. Supports aes_brisas_26mw_colombia_2023.",
    evid_note="Opened Ecopetrol Brisas COD primary (26 MWp; CapEx blank).",
)

# 2. wind / us — AES Dominicana Agua Clara acquisition USD 98m (2022)
row_doc(
    "aes_agua_clara_acquisition_98m_dr_2022",
    "energy",
    "wind",
    "us",
    "AES Dominicana Renewable Energy — Agua Clara wind acquisition (Monte Cristi)",
    "Dominican Republic",
    "17 Jun 2022 AES Corp. Form 10-Q: through AES Dominicana Renewable Energy and AES Andres DR, acquired 100% of Agua Clara, S.A.S. (operating wind project) for consideration of USD 98 million; reported in MCAC SBU. Asset is ~50–52.5 MW Agua Clara wind farm (Monte Cristi corridor; COD 2019 under prior owner Inkia). Distinct from aes_dr_mirasol_100mw_2025 / aes_dr_peravia_140mw_cod_2025.",
    "98000000",
    "2022-06-17",
    "2022",
    "19.850",
    "-71.650",
    "Agua Clara wind corridor spanning Monte Cristi / Puerto Plata / Valverde provinces, Dominican Republic (project geography).",
    "aes_10q_agua_clara_20220617",
    "Agua Clara — On June 17, 2022, the Company, through its subsidiaries AES Dominicana Renewable Energy and AES Andres DR, S.A., acquired 100% of the equity interests in Agua Clara, S.A.S., a wind project for consideration of $98 million.",
    "https://www.sec.gov/Archives/edgar/data/874761/000087476122000064/R26.htm",
    "Actor: AES Corporation (U.S.) via AES Dominicana — us. SEC 10-Q primary for USD 98m acquisition consideration. Operating wind asset acquisition (not greenfield CapEx).",
    "hunt_energy_wind",
    investment_type="acquisition",
    bib_type="regulator",
    chicago='The AES Corporation. Form 10-Q for the quarterly period ended June 30, 2022 (Exhibit R26 — Acquisitions: Agua Clara). https://www.sec.gov/Archives/edgar/data/874761/000087476122000064/R26.htm.',
    annotation="AES 10-Q: Agua Clara wind acquisition USD 98m (DR). Supports aes_agua_clara_acquisition_98m_dr_2022.",
    evid_note="Opened AES SEC 10-Q Agua Clara acquisition (USD 98m).",
)

# 3. solar / prc — SUMEC–XJ GUYSOL Prospect 3 MWp COD USD 5.5m
row_doc(
    "sumec_guyana_prospect_solar_5p5m_2025",
    "energy",
    "solar",
    "prc",
    "SUMEC–XJ Group JV — GUYSOL Prospect 3 MWp solar COD (Region Six)",
    "Guyana",
    "6–7 Dec 2025 DPI Guyana: PM Phillips commissioned Prospect Solar Farm in Prospect, Berbice, Region Six — 3 MWp / up to 2.4 MWac; 4,928 modules / 8 inverters; 13.8 kV spur to Canefield F3 feeder / DBIS; constructed at cost of US$5.5 million. EPC: SUMEC Complete Equipment and Engineering + XJ Group Corporation (named at ceremony). Distinct from sumec_guyana_onderneeming_solar_10p4m_2025 and sumec_guyana_linden_solar_22p58m_2025.",
    "5500000",
    "2025-12-06",
    "2025",
    "6.250",
    "-57.520",
    "Prospect, East Coast Berbice, Region Six, Guyana (DPI site naming).",
    "dpi_guyana_prospect_solar_20251206",
    "The Prospect Solar Farm, constructed at a cost of US$5.5 million, features 4,928 solar modules, eight PV inverters, and a new 13.8 kV spur connecting to the Canefield F3 distribution feeder backbone. With an installed capacity of 3 MWp… He further extended appreciation… to SUMEC Complete Equipment and Engineering Limited and the XJ Group Corporation for completing the project within the established timeline.",
    "https://dpi.gov.gy/govt-eying-100-mw-of-renewable-energy-over-the-next-five-years-pm-phillips/",
    "Actor: SUMEC (SINOMACH) + XJ Group (PRC) JV — prc. Official DPI English primary with US$5.5m CapEx and contractor naming. Prefer SUMEC–XJ over CREC company claim on overlapping GUYSOL portfolio.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="government",
    chicago='Department of Public Information, Guyana. “Govt eying 100 MW of renewable energy over the next five years – PM Phillips.” December 7, 2025. https://dpi.gov.gy/govt-eying-100-mw-of-renewable-energy-over-the-next-five-years-pm-phillips/.',
    annotation="DPI Guyana: SUMEC–XJ Prospect 3 MWp solar COD US$5.5m. Supports sumec_guyana_prospect_solar_5p5m_2025.",
    evid_note="Opened DPI Prospect COD primary (3 MWp; US$5.5m; SUMEC–XJ).",
)

# 4. solar / prc — SUMEC–XJ GUYSOL Hampshire 3 MWp COD (CapEx blank)
row_doc(
    "sumec_guyana_hampshire_3mw_2025",
    "energy",
    "solar",
    "prc",
    "SUMEC–XJ Group JV — GUYSOL Hampshire 3 MWp solar COD (Region Six)",
    "Guyana",
    "21 Nov 2025 DPI Guyana: PM Phillips commissioned 3 MWp Hampshire solar PV facility in East Berbice, Corentyne, Region Six (GUYSOL / GPL / IDB). EPC: SUMEC Complete Equipment and Engineering Limited + XJ Group Corporation (commended at ceremony for on-time completion). CapEx blank on plant-level primary (programme figure US$83.8m is multi-farm — not allocated). Distinct from sumec_guyana_prospect_solar_5p5m_2025 and sumec_guyana_onderneeming_solar_10p4m_2025.",
    "",
    "",
    "2025",
    "6.230",
    "-57.450",
    "Hampshire, East Coast Berbice / Corentyne, Region Six, Guyana (DPI site naming).",
    "dpi_guyana_hampshire_solar_20251121",
    "Prime Minister… commissioned the 3 MWp Hampshire solar photovoltaic facility in East Berbice, Corentyne, Region Six… He also commended the joint venture between SUMEC Complete Equipment and Engineering Limited and the XJ Group Corporation for completing the project within the established timeline.",
    "https://dpi.gov.gy/prime-minister-phillips-commissions-3mw-hampshire-solar-farm/",
    "Actor: SUMEC (SINOMACH) + XJ Group (PRC) JV — prc. Official DPI English primary for COD + contractor. CapEx blank (no plant-level figure on primary).",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="government",
    chicago='Department of Public Information, Guyana. “Prime Minister Phillips commissions 3MW Hampshire solar farm.” November 21, 2025. https://dpi.gov.gy/prime-minister-phillips-commissions-3mw-hampshire-solar-farm/.',
    annotation="DPI Guyana: SUMEC–XJ Hampshire 3 MWp solar COD. Supports sumec_guyana_hampshire_3mw_2025.",
    evid_note="Opened DPI Hampshire COD primary (3 MWp; SUMEC–XJ; CapEx blank).",
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
    print(f"Cycle 148 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
