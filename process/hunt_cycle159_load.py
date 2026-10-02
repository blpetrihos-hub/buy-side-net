#!/usr/bin/env python3
"""Cycle 159 hunt: shuffle_seed=20261159; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: fission_smr, niobium, rail, port_ownership, graphite,
bridges_roads, wind, other_renewables, power_plants_grid, water, port_cranes,
lithium, copper, building_materials, solar, engineering_epc, balsa, nickel.

Weight under-covered: El Salvador, Honduras, Ecuador.
PRC ahead by 9 — keep equal US/PRC budget without padding.
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


# 1. other_renewables / prc — POWERCHINA Patuca III Honduras 104 MW
row_doc(
    "powerchina_patuca_iii_honduras_104mw",
    "energy",
    "other_renewables",
    "prc",
    "POWERCHINA / Sinohydro — Patuca III Hydropower Station (104 MW)",
    "Honduras",
    "27 Mar 2023 POWERCHINA: Patuca III hydropower (eastern Honduras) — first large-scale hydro in Honduras in 30+ years; construction from 21 Sep 2015; connected to national grid 20 Dec 2020; 104 MW; ~326 GWh/yr; ~4% of national electricity. CapEx blank. Distinct from powerchina_honduras_enee_230kv_2025 transmission row.",
    "",
    "",
    "2020",
    "14.950",
    "-85.950",
    "Patuca III / Patuca corridor, eastern Honduras (company city-of-Patuca naming; approximate).",
    "powerchina_honduras_hydro_20230327",
    "POWERCHINA built the Patuca III Hydropower Station, the first large-scale hydropower project built in Honduras over three decades … The project started construction on Sept 21, 2015 and the plant was connected to the national grid on Dec 20, 2020. The hydroelectric station has an installed power capacity of 104 MW and an average annual power generation of 326 million kWh. Moreover, it supplies 4 percent of the electricity to the country's power grid",
    "https://en.powerchina.cn/2023-03/27/c_828296.htm",
    "Actor: POWERCHINA / Sinohydro Bureau 11 — prc. Company English primary (Mar 2023) documenting Dec 2020 COD / 104 MW. CapEx blank. Undersampled Honduras other_renewables.",
    "hunt_energy_other_renewables",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “POWERCHINA helps galvanize Honduras power project.” March 27, 2023. https://en.powerchina.cn/2023-03/27/c_828296.htm.',
    annotation="POWERCHINA primary: Patuca III 104 MW COD Dec 2020. Supports powerchina_patuca_iii_honduras_104mw; powerchina_el_arenal_honduras_60mw.",
    evid_note="Opened POWERCHINA English 27 Mar 2023 (Patuca III 104 MW / El Arenal 60 MW).",
)

# 2. other_renewables / prc — POWERCHINA El Arenal Honduras 60 MW
row_doc(
    "powerchina_el_arenal_honduras_60mw",
    "energy",
    "other_renewables",
    "prc",
    "POWERCHINA — El Arenal Hydropower Station (60 MW; Yoro)",
    "Honduras",
    "27 Mar 2023 POWERCHINA: El Arenal Hydropower Station in Yoro province — dam storage 52 million m³; 60 MW installed; construction from 15 Feb 2019; completed 26 Apr 2022; ~360 GWh/yr serving ~1 million people. CapEx blank. Distinct from powerchina_patuca_iii_honduras_104mw.",
    "",
    "",
    "2022",
    "15.140",
    "-87.130",
    "Yoro province, northern Honduras (El Arenal hydropower; provincial pin).",
    "powerchina_honduras_hydro_20230327",
    "The El Arenal Hydropower Station located in Yoro province, in northern Honduras, which has a dam with a storage capacity of 52 million cubic meters of water and a total installed capacity of 60 MW. The project started construction on Feb 15, 2019 and was completed on April 26, 2022. It can generate 360 million kWh of electricity every year, serving about 1 million people.",
    "https://en.powerchina.cn/2023-03/27/c_828296.htm",
    "Actor: POWERCHINA — prc. Same company English primary as Patuca III. CapEx blank. Undersampled Honduras hydro.",
    "hunt_energy_other_renewables",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “POWERCHINA helps galvanize Honduras power project.” March 27, 2023. https://en.powerchina.cn/2023-03/27/c_828296.htm.',
    annotation="POWERCHINA primary: El Arenal 60 MW completed Apr 2022. Supports powerchina_el_arenal_honduras_60mw; powerchina_patuca_iii_honduras_104mw.",
    evid_note="Opened POWERCHINA English 27 Mar 2023 (El Arenal 60 MW COD Apr 2022).",
)

# 3. solar / us — AES Opico Power 5.2 MWp El Salvador
row_doc(
    "aes_opico_power_5p2mwp_elsalvador",
    "energy",
    "solar",
    "us",
    "AES El Salvador — Opico Power solar plant (5.2 MWp; Armenia, Sonsonate)",
    "El Salvador",
    "AES El Salvador Opico Power Plant page: inaugurated 2020 in Armenia, Sonsonate; 12,834 PV modules over 50,000 m²; 24 inverters; 5.2 MWp injected to distribution network; ~2,371 t CO2 avoided/yr. CapEx blank. Distinct from aes_metapan_apopa_1p5mwp_2022 / aes_holcim_el_ronco_21p4mw_2023 / aes_meanguera_golfo_solar_bess_2023.",
    "",
    "",
    "2020",
    "13.745",
    "-89.501",
    "Armenia municipality, Sonsonate department, El Salvador (Opico Power PV plant).",
    "aes_elsalvador_opico_plant",
    "Located in the municipality of Armenia in the department of Sonsonate, Opico Power is our most recent commitment to contribute to the generation of clean and non-polluting energy based on solar sources. Inaugurated in 2020, it counts on 12,834 last-generation photovoltaic modules … Opico Power generates 5.2 megawatts (MWp)",
    "https://www.aes-elsalvador.com/en/opico-power-plant",
    "Actor: AES El Salvador (U.S. HQ parent) — us. Company English plant page. CapEx blank. Undersampled El Salvador solar named sites.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES El Salvador. “Opico Power Plant.” Accessed October 2, 2026. https://www.aes-elsalvador.com/en/opico-power-plant.',
    annotation="AES El Salvador primary: Opico Power 5.2 MWp inaugurated 2020. Supports aes_opico_power_5p2mwp_elsalvador.",
    evid_note="Opened AES El Salvador Opico Power plant page (5.2 MWp / 2020 inauguration).",
)

# 4. solar / us — AES Cuscatlán Solar 10 MW El Salvador
row_doc(
    "aes_cuscatlan_solar_10mw_elsalvador",
    "energy",
    "solar",
    "us",
    "AES El Salvador — Cuscatlán Solar (10 MW; Santa Ana)",
    "El Salvador",
    "AES El Salvador Sobre AES page: Generation Division lists Cuscatlán Solar at 10 MW among owned solar plants (with Opico 5.2 MW, Meanguera 1.3 MW, Moncagua 2.5 MW, Bósforo 100 MW, Nejapa 6 MW biogas). CapEx blank. Distinct from aes_opico_power_5p2mwp_elsalvador / aes_santa_ana_iv_55mw_2026.",
    "",
    "",
    "2022",
    "13.995",
    "-89.557",
    "Santa Ana department, El Salvador (Cuscatlán Solar; departmental pin per company Santa Ana placement).",
    "aes_elsalvador_sobre_aes",
    "A través de nuestro proyecto solar fotovoltaico de 100 MW Bósforo (asocio AES-CMI), que consta de 10 plantas de 10 MW cada una; de nuestras plantas solares Cuscatlán Solar, Opico Power, AES Meanguera del Golfo –la cual combina un innovador sistema de generación solar con almacenamiento de baterías– y Moncagua, de 10 MW, 5.2 MW, 1.3 MW y 2.5 MW, respectivamente",
    "https://www.aes-elsalvador.com/es/sobre-aes",
    "Actor: AES El Salvador (U.S. HQ parent) — us. Company Spanish About page documenting 10 MW Cuscatlán Solar in generation portfolio. CapEx blank.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES El Salvador. “Sobre AES.” Accessed October 2, 2026. https://www.aes-elsalvador.com/es/sobre-aes.',
    annotation="AES El Salvador About page: Cuscatlán Solar 10 MW portfolio listing. Supports aes_cuscatlan_solar_10mw_elsalvador.",
    evid_note="Opened AES El Salvador Sobre AES page (Cuscatlán Solar 10 MW).",
)

# 5. solar / prc — POWERCHINA Guayasamín Museum solar+storage Ecuador
row_doc(
    "powerchina_guayasamin_solar_ecuador_2026",
    "energy",
    "solar",
    "prc",
    "POWERCHINA / PRC Embassy — Guayasamín Museum solar-plus-storage demonstration (Quito)",
    "Ecuador",
    "13 Jul 2026 POWERCHINA: Guayasamín Museum Solar-Plus-Storage Demonstration Project begins generating electricity; spearheaded/co-funded by Chinese Embassy in Ecuador with Chinese and Ecuadorian enterprises; ~100,000 kWh/yr; museum 100% green energy. CapEx blank (demonstration). Distinct from prior POWERCHINA Ecuador hydro/solar portfolio rows.",
    "",
    "",
    "2026",
    "-0.190",
    "-78.469",
    "Museo Oswaldo Guayasamín, Bellavista, Quito, Ecuador.",
    "powerchina_guayasamin_20260713",
    "The Guayasamín Museum's Solar-Plus-Storage Demonstration Project recently began generating electricity. The project was spearheaded and co-funded by the Chinese Embassy in Ecuador, with joint support from Chinese and Ecuadorian enterprises. Capable of reliably generating nearly 100,000 kWh of electricity annually, the project allows the museum to run on 100 percent green energy",
    "https://en.powerchina.cn/2026-07/13/c_829087.htm",
    "Actor: POWERCHINA / PRC Embassy co-funded demonstration — prc. Company English primary. CapEx blank. Undersampled Ecuador solar demonstration presence.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “POWERCHINA-built solar-storage project launches in Ecuador.” July 13, 2026. https://en.powerchina.cn/2026-07/13/c_829087.htm.',
    annotation="POWERCHINA primary: Guayasamín Museum solar+storage launch. Supports powerchina_guayasamin_solar_ecuador_2026.",
    evid_note="Opened POWERCHINA English 13 Jul 2026 (Guayasamín solar+storage COD).",
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
    print(f"Cycle 159 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
