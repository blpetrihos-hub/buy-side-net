#!/usr/bin/env python3
"""Cycle 150 hunt: shuffle_seed=20261150; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: fission_smr, copper, engineering_epc, graphite, solar,
water, niobium, other_renewables, lithium, power_plants_grid, port_cranes, wind,
nickel, port_ownership, balsa, building_materials, rail, bridges_roads.

PRC ahead by 13 after 149 — keep equal US/PRC budget without padding.
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


# 1. other_renewables / us — AES Andes–Codelco 1.6 TWh/y renewable PPA
row_doc(
    "aes_andes_codelco_ppa_1p6twh_2023",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Codelco renewable PPA (Radomiro Tomic / Ministro Hales)",
    "Chile",
    "11 Jan 2023 AES Andes: agreement to replace coal supply to Codelco with renewable energy; supply up to 1.6 TWh/year of renewable energy between 2026 and 2040 for Radomiro Tomic and Ministro Hales (Antofagasta Region); energy equivalent to ~980 MW of renewable installed capacity from AES Andes renewables and batteries portfolio. CapEx blank (offtake/PPA).",
    "",
    "",
    "2023",
    "-22.350",
    "-68.900",
    "Codelco Radomiro Tomic / Ministro Hales divisions, Antofagasta Region, Chile (AES offtake naming).",
    "aes_andes_codelco_ppa_20230111",
    "Under the agreement, AES Andes will supply up to 1.6TWh/year of renewable energy between 2026 and 2040… The energy committed in the contract is equivalent to the production of approximately 980MW of renewable installed capacity from AES Andes' broad portfolio of renewables and batteries",
    "https://www.aesandes.com/en/press-release/aes-andes-signs-100-renewable-energy-contract-codelco",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for offtake volume + ~980 MW equivalent. CapEx blank (PPA).",
    "hunt_energy_other_renewables",
    investment_type="offtake",
    chicago='AES Andes. “AES Andes signs a 100% renewable energy contract with Codelco.” January 11, 2023. https://www.aesandes.com/en/press-release/aes-andes-signs-100-renewable-energy-contract-codelco.',
    annotation="AES Andes: Codelco 1.6 TWh/y renewable PPA 2026–2040. Supports aes_andes_codelco_ppa_1p6twh_2023.",
    evid_note="Opened AES Andes Codelco renewable PPA primary (1.6 TWh/y; CapEx blank).",
)

# 2. other_renewables / us — AES Andes–Microsoft Chile renewable PPA
row_doc(
    "aes_andes_microsoft_chile_ppa_2022",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Microsoft Chile datacenter renewable PPA (wind + solar)",
    "Chile",
    "6 Apr 2022 AES Andes: Microsoft Chile announces datacenter region will use 100% renewable energy via purchase agreement with AES Andes S.A.; supply from wind and solar — solar-plus-battery project in Antofagasta Region and wind project in Biobío Region (then impending construction). CapEx blank (offtake/PPA). Distinct from aes_andes_codelco_ppa_1p6twh_2023 and aes_andes_los_olmos_110mw_cod_2022 (Google hybrid).",
    "",
    "",
    "2022",
    "-33.450",
    "-70.650",
    "Microsoft Chile datacenter region / AES Andes renewable portfolio (Antofagasta solar+BESS and Biobío wind) — AES offtake naming.",
    "aes_andes_microsoft_ppa_20220406",
    "Microsoft Chile reported that the datacenter announced in December 2020… will use completely renewable energy thanks to a renewable energy purchase agreement with AES Andes S.A.… The project includes wind and solar energy… power supply will come from two projects that will begin construction soon: a solar plus battery project located in the Antofagasta region and a wind project located in the Biobío region.",
    "https://www.aesandes.com/en/blog/microsoft-chile-announces-its-datacenter-will-use-100-renewable-energy-aes-andes",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for Microsoft Chile renewable offtake. CapEx blank (PPA).",
    "hunt_energy_other_renewables",
    investment_type="offtake",
    chicago='AES Andes. “Microsoft Chile announces that its datacenter will use 100% renewable energy from AES Andes.” April 6, 2022. https://www.aesandes.com/en/blog/microsoft-chile-announces-its-datacenter-will-use-100-renewable-energy-aes-andes.',
    annotation="AES Andes: Microsoft Chile 100% renewable datacenter PPA. Supports aes_andes_microsoft_chile_ppa_2022.",
    evid_note="Opened AES Andes Microsoft Chile renewable PPA primary (CapEx blank).",
)

# 3. solar / prc — CTG Brasil Arinos first unit 78.4 MW COD
row_doc(
    "ctg_arinos_first_unit_78p4mw_2024",
    "energy",
    "solar",
    "prc",
    "CTG Brasil — Arinos Photovoltaic Project first unit COD (78.4 MW)",
    "Brazil",
    "23 Oct 2024 CTG: first grid-connected unit of CTG Brasil Arinos Photovoltaic Project enters commercial operation — installed capacity 78.4 MW; ~162 GWh/year. Independently developed/invested/operated by CTG Brasil. CapEx blank. Distinct from ctg_arinos_solar_full_cod_2025 (full complex COD ~337 MW / ~1 GW portfolio milestone) and huawei_ctg_arinos_inv_2022.",
    "",
    "",
    "2024",
    "-15.920",
    "-46.150",
    "Arinos Photovoltaic Project, Minas Gerais, Brazil (CTG site naming).",
    "ctg_arinos_first_unit_20241023",
    "CTG Brasil’s Arinos Photovoltaic Project recently commenced commercial operation for its first grid-connected unit. With an installed capacity of 78.4 MW, this unit will provide approximately 162 million kWh of clean electricity annually",
    "https://www.ctg.com.cn/ctgenglish/news_media/news37/2024102316474494820/index.html",
    "Actor: CTG Brasil / China Three Gorges (PRC SOE) — prc. Company English primary for first-unit COD. CapEx blank.",
    "hunt_energy_solar",
    investment_type="greenfield",
    chicago='China Three Gorges Corporation. “First grid-connected unit of CTG Brasil’s Arinos Photovoltaic Project enters commercial operation.” October 23, 2024. https://www.ctg.com.cn/ctgenglish/news_media/news37/2024102316474494820/index.html.',
    annotation="CTG: Arinos first unit 78.4 MW COD. Supports ctg_arinos_first_unit_78p4mw_2024.",
    evid_note="Opened CTG Arinos first-unit COD primary (78.4 MW; CapEx blank).",
)

# 4. solar / prc — SUMEC–XJ GUYSOL Trafalgar 4 MWp; CapEx USD 8m UNVERIFIED press proxy
row_doc(
    "sumec_guyana_trafalgar_8m_2025",
    "energy",
    "solar",
    "prc",
    "SUMEC–XJ Group JV — GUYSOL Trafalgar 4 MWp solar COD (Region Five)",
    "Guyana",
    "13 Dec 2025 News Room Guyana (GPL CEO cited): PM Phillips commissioned 4 MWp Trafalgar solar farm, Region Five; constructed at estimated cost of US$8 million (Guyana–Norway / GRIF / IDB); connects to DBIS via new 69 kV line; part of GUYSOL with Prospect/Hampshire/Onderneeming/Charity. EPC: SUMEC–XJ JV (same Regions 2/5/6 US$38m contract; named at Hampshire/Prospect). CapEx USD 8m is press-only figure quoting ceremony — logged as UNVERIFIED proxy. Distinct from sumec_guyana_prospect_solar_5p5m_2025 and sumec_guyana_hampshire_3mw_2025.",
    "8000000",
    "2025-12-13",
    "2025",
    "6.400",
    "-57.600",
    "Trafalgar, West Coast Berbice, Region Five, Guyana (commissioning site naming).",
    "newsroom_guyana_trafalgar_solar_20251213",
    "A four megawatt peak (MWp) solar farm was commissioned by Prime Minister Brigadier (Ret’d) Mark Phillips on Saturday at Trafalgar, Region Five… The Trafalgar Solar Farm was constructed at an estimated cost of US$8 million, fully financed through the Guyana–Norway climate partnership, under the Guyana REDD+ Investment Fund, administered by the Inter-American Development Bank.",
    "https://newsroom.gy/2025/12/13/millions-in-fuel-savings-expected-as-trafalgar-solar-farm-commissioned/",
    "Actor: SUMEC (SINOMACH) + XJ Group (PRC) JV — prc (programme EPC). Press primary with estimated CapEx — UNVERIFIED proxy. DPI OPM confirms Trafalgar among five farms online.",
    "hunt_energy_solar",
    investment_type="epc",
    evidence="proxy",
    bib_type="press",
    chicago='News Room Guyana. “Millions in fuel savings expected as Trafalgar solar farm commissioned.” December 13, 2025. https://newsroom.gy/2025/12/13/millions-in-fuel-savings-expected-as-trafalgar-solar-farm-commissioned/.',
    annotation="News Room Guyana: Trafalgar 4 MWp COD; estimated US$8m (UNVERIFIED proxy). Supports sumec_guyana_trafalgar_8m_2025.",
    evid_note="Opened News Room Trafalgar COD (4 MWp; USD 8m estimated CapEx — UNVERIFIED proxy).",
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
    print(f"Cycle 150 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
