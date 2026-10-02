#!/usr/bin/env python3
"""Cycle 154 hunt: shuffle_seed=20261154; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: building_materials, niobium, copper, wind, fission_smr,
graphite, power_plants_grid, engineering_epc, port_ownership, solar, lithium,
nickel, rail, water, other_renewables, port_cranes, balsa, bridges_roads.

PRC ahead by 13 after 153 — keep equal US/PRC budget without padding.
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


# 1. solar / us — AES Andes Solar IIa 81 MW COD
row_doc(
    "aes_andes_solar_iia_81mw_cod_2021",
    "energy",
    "solar",
    "us",
    "AES Andes — Andes Solar IIa COD (81 MW PV, Antofagasta)",
    "Chile",
    "28 Feb 2022 AES Andes (2021 results): commercial operation of Andes Solar IIa with 81 MW began during 2021 in northern Chile; later BESS add-on (80 MW × 3h) noted in green-bond impact materials but CapEx blank here. Distinct from aes_andes_solar_iib_180mw_cod_2023 and Andes Solar IV.",
    "",
    "",
    "2021",
    "-23.650",
    "-70.250",
    "Andes Solar Hub / Antofagasta Region, Chile (company geography; approximate hub pin).",
    "aes_andes_2021_results_20220228",
    "Meanwhile, in the north of Chile, the commercial operation of Andes Solar IIa with 81MW began during 2021 and Andes Solar IIb - the largest solar + storage system in Latin America - continues to advance to complete construction in the second half of 2022.",
    "https://www.aesandes.com/en/blog/aes-andes-ended-2021-strong-progress-its-renewable-transformation",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for IIa COD capacity. CapEx blank.",
    "hunt_energy_solar",
    investment_type="greenfield",
    chicago='AES Andes. “AES Andes ended 2021 with strong progress in its renewable transformation.” February 28, 2022. https://www.aesandes.com/en/blog/aes-andes-ended-2021-strong-progress-its-renewable-transformation.',
    annotation="AES Andes 2021 results: Andes Solar IIa COD + Gecelca 438 GWh/y PPA. Supports aes_andes_solar_iia_81mw_cod_2021; aes_andes_gecelca_438gwh_ppa_2021.",
    evid_note="Opened AES Andes 2021 results primary for Andes Solar IIa 81 MW COD (CapEx blank).",
)

# 2. other_renewables / us — AES Andes–Gecelca 438 GWh/y Colombia PPA
row_doc(
    "aes_andes_gecelca_438gwh_ppa_2021",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Gecelca renewable supply agreement (438 GWh/y, 15 years from 2025)",
    "Colombia",
    "28 Feb 2022 AES Andes: signed 438 GWh/year supply agreement with Gecelca for 15 years from 2025 (Colombia renewable offtake). CapEx blank (PPA). Distinct from aes_jk1_jk2_idb_invest_150m_2025 and San Fernando/Brisas self-gen rows.",
    "",
    "",
    "2021",
    "6.250",
    "-75.570",
    "Gecelca offtake / AES Andes Colombia renewable portfolio (company offtake naming; approximate Medellín-area pin).",
    "aes_andes_2021_results_20220228",
    "Meanwhile, in Colombia, AES Andes signed a 438 GWh/year supply agreement with Gecelca for 15 years from 2025.",
    "https://www.aesandes.com/en/blog/aes-andes-ended-2021-strong-progress-its-renewable-transformation",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for offtake volume. CapEx blank (PPA).",
    "hunt_energy_other_renewables",
    investment_type="offtake",
    chicago='AES Andes. “AES Andes ended 2021 with strong progress in its renewable transformation.” February 28, 2022. https://www.aesandes.com/en/blog/aes-andes-ended-2021-strong-progress-its-renewable-transformation.',
    annotation="AES Andes 2021 results: Andes Solar IIa COD + Gecelca 438 GWh/y PPA. Supports aes_andes_solar_iia_81mw_cod_2021; aes_andes_gecelca_438gwh_ppa_2021.",
    evid_note="Opened AES Andes 2021 results primary for Gecelca 438 GWh/y PPA (CapEx blank).",
)

# 3. water / prc — POWERCHINA Malabar WWTP Trinidad (40,000 m3/d)
row_doc(
    "powerchina_malabar_wwtp_trinidad_2019",
    "resources",
    "water",
    "prc",
    "POWERCHINA — Malabar Wastewater Treatment Plant and pipeline network (40,000 m³/d)",
    "Trinidad and Tobago",
    "POWERCHINA English: Malabar Wastewater Treatment Plant and Pipeline Network in Trinidad and Tobago — designed capacity 40,000 m³/d; covers ~27 km² catchment; serves >110,000 households; plant plus O&M year. Company latest index (19 Jul 2019): officially put into operation on 12 Jul 2019. CapEx blank. Distinct from powerchina_piarco_trinidad_2024 and powerchina_santo_domingo_water_ecuador_2026.",
    "",
    "",
    "2019",
    "10.620",
    "-61.300",
    "Malabar catchment / Trinidad, Trinidad and Tobago (POWERCHINA geography; approximate pin).",
    "powerchina_malabar_wwtp_catalog",
    "Malabar Wastewater Treatment Plant and Pipeline Network, Trinidad and Tobago (40,000 m 3 /d). Located in the catchment area of Malabar, the project covers an area of 27 square kilometers and can treat the domestic sewage of more than 110,000 households… The main content of the project includes the wastewater treatment plant with a designed capacity of 40,000 m 3 /d and a year of O&M.",
    "https://en.powerchina.cn/2025-05/20/c_817809.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English wastewater catalog primary for capacity; COD date corroborated on company Latest index 19 Jul 2019. CapEx blank.",
    "hunt_resources_water",
    investment_type="epc",
    chicago='POWERCHINA. “Wastewater/Solid Waste Disposal” (Malabar Wastewater Treatment Plant and Pipeline Network, Trinidad and Tobago). May 20, 2025. https://en.powerchina.cn/2025-05/20/c_817809.htm.',
    annotation="POWERCHINA: Malabar WWTP Trinidad 40,000 m³/d. Supports powerchina_malabar_wwtp_trinidad_2019.",
    evid_note="Opened POWERCHINA wastewater catalog primary for Malabar 40,000 m³/d (CapEx blank; COD 12 Jul 2019 per company Latest index).",
)

# 4. bridges_roads / prc — CREC Espino Highway Bolivia opening
row_doc(
    "crec_espino_highway_bolivia_2023",
    "infrastructure",
    "bridges_roads",
    "prc",
    "CREC consortium — Espino Highway (Ruta 36) opening (Santa Cruz)",
    "Bolivia",
    "21 Sep (CREC English): Espino Highway Project in Bolivia constructed by CREC with First Engineering Bureau, China Railway Seventh Group, China Railway No.9 Group and China Railway International Group completed and opened; President Luis Arce attended; south of Santa Cruz / Guaraní indigenous area; core of Bolivian Highway Network No.36 passenger/freight dedicated line connecting South American international transport corridors. CapEx blank on opened page (CHEXIM preferential loan noted on related CREC Bid III release — not used as CapEx here). Distinct from chec_sucre_yamparaez_bolivia_2025.",
    "",
    "",
    "2023",
    "-20.450",
    "-63.200",
    "Espino Highway / southern Santa Cruz Department, Bolivia (CREC geography; approximate corridor pin).",
    "crec_espino_highway_bolivia_2023",
    "On September 21, local time, the Espino Highway Project in Bolivia, which was constructed by CREC and participated by The First Engineering Bureau of CREC, China Railway Seventh Group Co., Ltd, China Railway No.9 Group Co., Ltd and China Railway International Group, was completed and opened to traffic… Located in the south of Santa Cruz… the Espino Highway Project is the core component of the passenger and freight dedicated line of the Bolivian Highway Network No.36",
    "https://www.crecg.com/zgztywz/cs11/10210606/2025021110100534141/index.html",
    "Actor: CREC / China Railway International Group consortium (PRC SOE) — prc. Company English primary for opening. CapEx blank.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    chicago='China Railway Group Limited. “Bolivia\'s Espino highway completed and opened to traffic.” October 22, 2023. https://www.crecg.com/zgztywz/cs11/10210606/2025021110100534141/index.html.',
    annotation="CREC: Espino Highway Bolivia opening (Ruta 36). Supports crec_espino_highway_bolivia_2023.",
    evid_note="Opened CREC Espino Highway Bolivia opening primary (CapEx blank).",
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
    print(f"Cycle 154 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
