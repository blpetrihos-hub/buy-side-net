#!/usr/bin/env python3
"""Cycle 145 hunt: shuffle_seed=20261145; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: solar, port_ownership, other_renewables, graphite, balsa, wind,
lithium, rail, water, engineering_epc, nickel, port_cranes, copper, niobium,
bridges_roads, fission_smr, building_materials, power_plants_grid.

PRC ahead by 8 after 144 — keep equal US/PRC budget without padding.
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


# 1. solar / us — DFC IEnova Mexico 4-solar loan up to USD 241m (Board 11 Mar 2020)
row_doc(
    "dfc_ienova_mexico_4solar_241m_2020",
    "energy",
    "solar",
    "us",
    "DFC / IEnova (Sempra) — Mexico four-plant solar corporate loan",
    "Mexico",
    "DFC Public Information Summary 9000093572: corporate unsecured loan up to USD 241 million to Infraestructura Energética Nova, S.A.B. de C.V. (IEnova; Sempra Energy affiliate) for development/construction of four Mexico solar plants totaling 426 MW nameplate; total project costs USD 441 million. Board Resolution BDR(20)12 approved financing 11 Mar 2020. CapEx proxy = DFC loan ceiling (project-cost figure disclosed but loan is the documented U.S. public commitment).",
    "241000000",
    "2020-03-11",
    "2020",
    "32.560",
    "-116.050",
    "Rumorosa Solar area, Baja California, Mexico (one of four IEnova plants named in related E&S review; multi-site package pin).",
    "dfc_ienova_pis_9000093572",
    "Corporate unsecured loan to support the Borrower’s development and construction of four solar power plants in Mexico totaling 426 megawatts of aggregate nameplate capacity. Up to USD $241 million. Total Project Costs $441 million.",
    "https://www.dfc.gov/sites/default/files/media/documents/9000093572.pdf",
    "Actor: DFC (U.S. government) financing IEnova / Sempra — us. DFC PIS primary; Board BDR(20)12 confirms 11 Mar 2020 approval of up to USD 241m. Distinct from IFC/NADB IEnova solar facility.",
    "hunt_energy_solar",
    investment_type="financing",
    bib_type="government",
    chicago='U.S. International Development Finance Corporation. “Public Information Summary — IEnova (9000093572).” Accessed 2026. https://www.dfc.gov/sites/default/files/media/documents/9000093572.pdf.',
    annotation="DFC PIS: up to USD 241m loan for IEnova 426 MW Mexico solar package. Supports dfc_ienova_mexico_4solar_241m_2020.",
    evid_note="Opened DFC Public Information Summary 9000093572 (USD 241m / 426 MW / USD 441m project costs); Board BDR(20)12 dated 11 Mar 2020.",
)

# 2. wind / us — AES Andes Los Olmos 110 MW COD 19 Jan 2022
row_doc(
    "aes_andes_los_olmos_110mw_cod_2022",
    "energy",
    "wind",
    "us",
    "AES Andes — Los Olmos Wind Farm COD (Mulchén, Biobío)",
    "Chile",
    "AES Andes/AES Chile blog: Los Olmos wind farm in Mulchén, Biobío Region — 110 MW via 23 × 4.8 MW turbines; commercial operation began 19 Jan 2022; first self-built AES Chile wind farm; supplies Google Quilicura data center under 2019 hybrid wind+solar contract (with Andes Solar IIa). CapEx blank on COD release.",
    "",
    "",
    "2022",
    "-37.720",
    "-72.240",
    "Mulchén, Biobío Region, Chile (company geography).",
    "aes_andes_los_olmos_cod_202201",
    "The initiative located in Mulchén, Biobío Region, has an installed capacity of 110 MW, through 23 wind turbines of 4.8 MW of individual power. Its commercial operation began on January 19, 2022.",
    "https://www.aesandes.com/es/blog/aes-chile-puts-operation-los-olmos-wind-farm",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company primary. CapEx blank. Distinct from aes_andes_campo_lindo_cod_2023 and aes_andes_san_matias_cod_2024.",
    "hunt_energy_wind",
    investment_type="greenfield_generation",
    chicago='AES Andes. “AES Chile puts into operation Los Olmos wind farm.” January 2022. https://www.aesandes.com/es/blog/aes-chile-puts-operation-los-olmos-wind-farm.',
    annotation="AES Andes primary: Los Olmos 110 MW wind COD 19 Jan 2022. Supports aes_andes_los_olmos_110mw_cod_2022.",
    evid_note="Opened AES Andes Los Olmos COD blog (110 MW; 19 Jan 2022).",
)

# 3. wind / prc — POWERCHINA Las Acacias Colombia 240 MW wind EPC (25 Sep 2024)
row_doc(
    "powerchina_las_acacias_colombia_240mw_epc_2024",
    "energy",
    "wind",
    "prc",
    "POWERCHINA — Las Acacias Wind Farm EPC (Cundinamarca, Colombia)",
    "Colombia",
    "25 Sep 2024 (China Electric Power News via Sina 27 Sep): POWERCHINA Colombia branch signs EPC contract with Dewu (德务) for Las Acacias wind project in Cundinamarca Department — 240 MW total installed capacity; intended to supply clean power to central Colombia. CapEx blank on signing notice. Distinct from POWERCHINA Colombia solar EPCs.",
    "",
    "",
    "2024",
    "4.850",
    "-74.050",
    "Cundinamarca Department, Colombia (department-level pin; project municipality not named on CPNN relay).",
    "cpnn_powerchina_las_acacias_20240927",
    "当地时间9月25日，中国电建哥伦比亚分公司与德务公司签订了拉斯阿卡西亚斯风电项目EPC合同…该项目位于昆迪纳马卡省，总装机240兆瓦，项目建成后将为哥伦比亚中部地区提供稳定的清洁电力。",
    "https://finance.sina.com.cn/jjxw/2024-09-27/doc-incqqumy1612190.shtml",
    "Actor: POWERCHINA (PRC SOE) — prc. China Electric Power News (中国电力新闻网) relay via Sina; powerchina-intl.com WAF-blocked this cycle. CapEx blank. EPC signing — UNVERIFIED CapEx.",
    "hunt_energy_wind",
    investment_type="epc",
    bib_type="press",
    chicago='China Electric Power News (中国电力新闻网), via Sina Finance. “中国电建签约哥伦比亚拉斯阿卡西亚斯风电项目.” September 27, 2024. https://finance.sina.com.cn/jjxw/2024-09-27/doc-incqqumy1612190.shtml.',
    annotation="CPNN/Sina: POWERCHINA–Dewu Las Acacias 240 MW Colombia wind EPC signed 25 Sep 2024. Supports powerchina_las_acacias_colombia_240mw_epc_2024.",
    evid_note="Opened Sina relay of 中国电力新闻网 (Las Acacias 240 MW EPC; 25 Sep 2024 signing).",
)

# 4. rail / prc — CREC Seventh Group Alameda–Melipilla rail depot USD 90m (groundbreaking 26 Mar 2025)
row_doc(
    "crec7_alameda_melipilla_depot_90m_2025",
    "infrastructure",
    "rail",
    "prc",
    "China Railway Seventh Group — Alameda–Melipilla Rail Depot (EFE, Chile)",
    "Chile",
    "14 Apr 2025 CREC English: 26 Mar 2025 groundbreaking for Alameda–Melipilla Rail Depot Project in Chile, co-constructed by China Railway Seventh Group (CREC) for EFE Trenes de Chile — 17.83 ha site / ~22,000 m² construction; total investment USD 90 million; comprehensive train maintenance (signal/track/OCS); automatic train washing; completion expected end-2026. Distinct from cri_efe_tam_tsb_electrification_2026 and efe_crrc_emu_2023.",
    "90000000",
    "2025-03-26",
    "2025",
    "-33.606",
    "-70.877",
    "Peñaflor / Alameda–Melipilla corridor, Santiago Metropolitan Region, Chile (mayor of Peñaflor attended groundbreaking; depot geography).",
    "crec_alameda_melipilla_depot_20250414",
    "The Alameda - Melipilla Rail Depot Project covers an area of 17.83 hectares with a construction area of about 22,000 square meters and a total investment of USD 90 million. It will provide comprehensive train maintenance… Completion is expected by the end of 2026.",
    "https://www.crecg.com/zgztywz/cs11/10210606/2025040717013624378/index.html",
    "Actor: China Railway Seventh Group / CREC (PRC SOE) — prc. Company English primary. CapEx = stated USD 90m total investment.",
    "hunt_infra_rail",
    investment_type="epc",
    chicago='China Railway Engineering Corporation. “Construction Officially Began on Chile’s Alameda - Melipilla Rail Depot Project.” April 14, 2025. https://www.crecg.com/zgztywz/cs11/10210606/2025040717013624378/index.html.',
    annotation="CREC primary: Alameda–Melipilla rail depot USD 90m groundbreaking. Supports crec7_alameda_melipilla_depot_90m_2025.",
    evid_note="Opened CREC English release 14 Apr 2025 (USD 90m Melipilla depot; groundbreaking 26 Mar 2025).",
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
    print(f"Cycle 145 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
