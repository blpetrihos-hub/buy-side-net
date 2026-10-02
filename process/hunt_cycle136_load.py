#!/usr/bin/env python3
"""Cycle 136 hunt: shuffle_seed=20261136; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: bridges_roads, other_renewables, engineering_epc, graphite,
copper, fission_smr, port_cranes, nickel, wind, water, building_materials,
port_ownership, solar, balsa, niobium, rail, lithium, power_plants_grid.

PRC push (PRC ahead by 3 after 135). Thin top-up: balsa/graphite/nickel.
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


# 1. port_ownership / us — NFE Terminal de Gás Sul lease commercialization
row_doc(
    "nfe_tgs_lease_brazil_2026",
    "infrastructure",
    "port_ownership",
    "us",
    "New Fortress Energy — Terminal de Gás Sul (TGS) LNG import terminal lease",
    "Brazil",
    "31 Mar 2026 NFE IR: Brazil platform enters long-term lease and capacity agreement for Terminal de Gás Sul (TGS) LNG import terminal in Santa Catarina; lease expected to commence August 2026; commercialization expected to generate USD 50 million annual EBITDA by 2027. CapEx blank (EBITDA is not CapEx; historical build CapEx not restated). Distinct from NFE Barcarena / Puerto Sandino rows.",
    "",
    "",
    "2026",
    "-28.48",
    "-48.77",
    "Terminal de Gás Sul, Santa Catarina, Brazil (approximate LNG terminal pin near southern SC coast).",
    "nfe_tgs_lease_20260331",
    "New Fortress Energy Inc. … today announced that its Brazil platform has entered into a long-term lease and capacity agreement (“Lease Agreement”) for its Terminal de Gás Sul (“TGS”) LNG import terminal in Santa Catarina, Brazil. The Lease Agreement is expected to commence in August 2026. The agreement marks the commercialization of TGS and is expected to generate $50 million in annual EBITDA by 2027.",
    "https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-brazil-enters-terminal-lease-agreement-tgs",
    "Actor: New Fortress Energy Inc. (U.S. HQ) — us. Company IR primary opened. CapEx blank; USD 50m is projected annual EBITDA (not stored as CapEx).",
    "hunt_infra_port_ownership",
    investment_type="concession",
    bib_type="company",
    chicago='New Fortress Energy Inc. “New Fortress Energy Brazil Enters into Terminal Lease Agreement for TGS.” Investor Relations, March 31, 2026. https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-brazil-enters-terminal-lease-agreement-tgs.',
    annotation="NFE TGS lease start Aug 2026; CapEx blank. Supports nfe_tgs_lease_brazil_2026.",
    evid_note="Opened NFE IR lease-agreement release for TGS Santa Catarina.",
)

# 2. power_plants_grid / us — NFE UTE Lins 2 greenfield (same primary)
row_doc(
    "nfe_ute_lins2_brazil_2031",
    "energy",
    "power_plants_grid",
    "us",
    "New Fortress Energy — UTE Lins 2 gas power project (TGS-supplied)",
    "Brazil",
    "31 Mar 2026 NFE IR (TGS lease release): TGS terminal will supply the Company’s UTE Lins 2 power project, a greenfield capacity award from Brazil’s recent auction expected to commence operations in 2031. CapEx blank on this primary. Distinct from NFE CELBA2 / Portocem / Sandino.",
    "",
    "",
    "2026",
    "-21.68",
    "-49.74",
    "Lins, São Paulo State, Brazil (approximate municipal pin for UTE Lins 2).",
    "nfe_tgs_lease_20260331",
    "In addition to these contracted cash flows, TGS is also expected to underpin NFE’s long-term growth in Brazil. The terminal will supply the Company’s UTE Lins 2 power project, a greenfield capacity award from Brazil’s recent auction that is expected to commence operations in 2031.",
    "https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-brazil-enters-terminal-lease-agreement-tgs",
    "Actor: New Fortress Energy Inc. (U.S. HQ) — us. Same IR primary as TGS lease. CapEx blank.",
    "hunt_energy_power_plants_grid",
    investment_type="greenfield",
    bib_type="company",
    chicago='New Fortress Energy Inc. “New Fortress Energy Brazil Enters into Terminal Lease Agreement for TGS.” Investor Relations, March 31, 2026. https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-brazil-enters-terminal-lease-agreement-tgs.',
    annotation="NFE UTE Lins 2 COD ~2031 via TGS supply; CapEx blank. Supports nfe_ute_lins2_brazil_2031.",
    evid_note="Opened NFE IR release naming UTE Lins 2 greenfield auction award / 2031 COD.",
)

# 3. solar / prc — Zijin Longking Rosebel Phase II Suriname USD 150m
row_doc(
    "zijin_longking_rosebel_p2_suriname_150m_2026",
    "energy",
    "solar",
    "prc",
    "Zijin Longking Clean Energy — Rosebel gold mine Phase II solar+storage (Suriname)",
    "Suriname",
    "23 Sep 2026 Zijin Longking (SSE 600388) cninfo announcement 2026-072: invest ~USD 150 million in Rosebel Phase II PV+storage — 170 MWp PV + 120 MW/120 MWh storage; COD planned Q3 2027; self-use for Rosebel/Saramacca mines (Zijin Gold International 95% of Rosebel Gold Mines N.V.). Phase I 25 MWp + 12.5 MW/25 MWh COD Dec 2025. Distinct from gold-mine OOS rows — this is solar/storage CapEx.",
    "150000000",
    "2026-09-23",
    "2026",
    "5.07",
    "-55.17",
    "Rosebel / Saramacca mine area, northern Suriname (approximate mine-complex pin).",
    "zijin_longking_rosebel_p2_cninfo_2026",
    "项目建设规模为 170MWp 光伏 +120MW/120MWh 储能，项目总投资金额约为 1.50 亿美元，拟由公司自筹。… 计划于 2027 年第三季度完成建设。",
    "http://static.cninfo.com.cn/finalpage/2026-09-24/1225578350.PDF",
    "Actor: Zijin Longking (紫金龙净; SSE 600388; PRC; Zijin Mining affiliate) via wholly owned Zijin Longking Clean Energy — prc. Company cninfo primary. CapEx ~USD 150m.",
    "hunt_energy_solar",
    investment_type="greenfield",
    bib_type="company",
    chicago='Zijin Longking Environmental Protection New Energy Co., Ltd. “关于投资建设苏里南罗斯贝尔金矿二期光储项目的公告.” Announcement 2026-072, September 23, 2026. http://static.cninfo.com.cn/finalpage/2026-09-24/1225578350.PDF.',
    annotation="Cninfo primary: Rosebel P2 170 MWp + 120 MW/120 MWh; ~USD 150m. Supports zijin_longking_rosebel_p2_suriname_150m_2026.",
    evid_note="Opened Zijin Longking cninfo PDF 1225578350 (Rosebel Phase II CapEx and MW).",
)

# 4. solar / prc — Zijin Longking Aurora underground plant Guyana USD 55.24m
row_doc(
    "zijin_longking_aurora_ug_guyana_55p24m_2026",
    "energy",
    "solar",
    "prc",
    "Zijin Longking Clean Energy — Aurora underground mining plant solar+storage (Guyana)",
    "Guyana",
    "23 Sep 2026 Zijin Longking cninfo: invest ~USD 55.24 million for Aurora underground (地采厂) solar+storage — 45 MWp PV + 50 MW/100 MWh storage; COD planned Q4 2027; self-use for Zijin Gold International Aurora operations. Distinct from concentrator Phase III row.",
    "55240000",
    "2026-09-23",
    "2026",
    "6.79",
    "-59.75",
    "Aurora gold mine area, Guyana (approximate mine pin).",
    "zijin_longking_aurora_ug_cninfo_2026",
    "项目建设规模为 45MWp 光伏+50MW/100MWh 储能，项目总投资金额约为5,524 万美元，拟由公司自筹。… 计划于2027 年第四季度完成建设。",
    "http://static.cninfo.com.cn/finalpage/2026-09-24/1225578342.PDF",
    "Actor: Zijin Longking Clean Energy (PRC) — prc. Company cninfo primary. CapEx ~USD 55.24m.",
    "hunt_energy_solar",
    investment_type="greenfield",
    bib_type="company",
    chicago='Zijin Longking Environmental Protection New Energy Co., Ltd. “关于投资建设圭亚那奥罗拉金矿地采厂光储项目的公告.” September 23, 2026. http://static.cninfo.com.cn/finalpage/2026-09-24/1225578342.PDF.',
    annotation="Cninfo primary: Aurora UG 45 MWp + 50 MW/100 MWh; ~USD 55.24m. Supports zijin_longking_aurora_ug_guyana_55p24m_2026.",
    evid_note="Opened Zijin Longking cninfo PDF 1225578342 (Aurora underground plant CapEx).",
)

# 5. solar / prc — Zijin Longking Aurora concentrator Phase III Guyana USD 26.62m
row_doc(
    "zijin_longking_aurora_conc_p3_guyana_26p62m_2026",
    "energy",
    "solar",
    "prc",
    "Zijin Longking Clean Energy — Aurora concentrator Phase III solar+storage (Guyana)",
    "Guyana",
    "23 Sep 2026 Zijin Longking cninfo: invest ~USD 26.62 million for Aurora concentrator Phase III solar+storage — 15 MWp PV + 20 MW/80 MWh storage; COD planned Q4 2027; prior Phase I/II at concentrator totaled 46.67 MWp + 84.5 MWh (COD Oct 2024 / Dec 2025). Distinct from underground plant row.",
    "26620000",
    "2026-09-23",
    "2026",
    "6.79",
    "-59.75",
    "Aurora gold mine concentrator area, Guyana (approximate mine pin; shared with UG plant row).",
    "zijin_longking_aurora_conc_p3_cninfo_2026",
    "项目新增建设规模为15MWp 光伏+20MW/80MWh 储能。… 合计总投资金额约为2,662 万美元。… 计划于2027 年第四季度完成建设。",
    "http://static.cninfo.com.cn/finalpage/2026-09-24/1225578337.PDF",
    "Actor: Zijin Longking Clean Energy (PRC) — prc. Company cninfo primary. CapEx ~USD 26.62m.",
    "hunt_energy_solar",
    investment_type="expansion",
    bib_type="company",
    chicago='Zijin Longking Environmental Protection New Energy Co., Ltd. “关于投资建设圭亚那奥罗拉金矿选矿厂三期光储项目的公告.” September 23, 2026. http://static.cninfo.com.cn/finalpage/2026-09-24/1225578337.PDF.',
    annotation="Cninfo primary: Aurora concentrator P3 15 MWp + 20 MW/80 MWh; ~USD 26.62m. Supports zijin_longking_aurora_conc_p3_guyana_26p62m_2026.",
    evid_note="Opened Zijin Longking cninfo PDF 1225578337 (Aurora concentrator Phase III CapEx).",
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
    print(f"Cycle 136 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
