#!/usr/bin/env python3
"""Cycle 164 hunt: shuffle_seed=20261164; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: engineering_epc, water, power_plants_grid, graphite,
building_materials, niobium, nickel, other_renewables, lithium, bridges_roads,
balsa, copper, fission_smr, port_ownership, solar, rail, port_cranes, wind.

Weight under-covered: Guatemala wind/grid; Haiti; Mexico power_plants_grid;
Mexico graphite trade. Thin: graphite scored via WITS; balsa/fission dry once;
nickel already used this session.
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


# 1. engineering_epc / us — Fluor Quellaveco EPCM (Peru)
row_doc(
    "fluor_quellaveco_epcm_peru",
    "infrastructure",
    "engineering_epc",
    "us",
    "Fluor — Quellaveco open-pit copper mine EPCM (Moquegua)",
    "Peru",
    "Fluor project case study: EPCM for Anglo American Quellaveco open-pit copper mine near Moquegua (3,000–3,500 masl); 127,500 tpd processing plant plus roads, dams, tunnels, pipelines, overland conveyors; first copper mid-2022; completed on budget/schedule despite COVID peak construction. CapEx blank on Fluor page (Anglo ownership CapEx logged separately as anglo_quellaveco_peru). Distinct EPCM contractor presence row.",
    "",
    "",
    "2022",
    "-17.090",
    "-70.630",
    "Quellaveco mine, Moquegua Department, Peru (company geography; approximate).",
    "fluor_quellaveco_case_study",
    "Fluor executed engineering, procurement and construction management services, with scope including the processing plant, roads, dams, tunnels, pipelines and overland conveyors. … Despite the challenge of a global pandemic hitting the project during the peak of construction, Quellaveco was completed in 2022, on budget and on schedule.",
    "https://www.fluor.com/projects/quellaveco-open-pit-copper-mine",
    "Actor: Fluor Corporation (Irving, Texas HQ) — us. Company English primary. CapEx blank. Peru engineering_epc presence.",
    "hunt_infra_engineering_epc",
    investment_type="epc",
    bib_type="company",
    chicago='Fluor Corporation. “Quellaveco Open Pit Copper Mine in Peru – Project Case Study.” Accessed October 2, 2026. https://www.fluor.com/projects/quellaveco-open-pit-copper-mine.',
    annotation="Fluor primary: Quellaveco EPCM completed 2022. Supports fluor_quellaveco_epcm_peru.",
    evid_note="Opened Fluor Quellaveco case study (EPCM / COD 2022).",
)

# 2. power_plants_grid / prc — POWERCHINA/江西电建 Mexico I20 Phase II Lot 1
row_doc(
    "powerchina_mexico_i20_p2_lot1_154m",
    "infrastructure",
    "power_plants_grid",
    "prc",
    "POWERCHINA Jiangxi Electric Power Construction — Mexico I20 Phase II Lot 1 transmission (Sinaloa)",
    "Mexico",
    "14 Jul 2026 GoalFore reprint of Jiangxi Electric Power Construction (POWERCHINA) notice: Mexico I20 Phase II Lot 1 transmission in Sinaloa energized 9 Jul 2026; 214.7 km line, 542 towers, two 400 kV substation expansions; contract amount USD 154 million (UNVERIFIED press figure attributed to company notice — stored as proxy). Fills Mexico×power_plants_grid empty cell. Distinct from other POWERCHINA Mexico renewables rows.",
    "154000000",
    "2026-07-09",
    "2026",
    "25.000",
    "-107.500",
    "Sinaloa I20 Phase II Lot 1 corridor (Culiacán–Los Mochis 400 kV axis; approximate midpoint).",
    "goalfore_jepcc_mexico_i20_20260714",
    "墨西哥当地时间2026年7月9日14时25分，由江西电建公司承建的墨西哥I20二期1标段输变电项目一次性成功并网送电。该项目位于墨西哥西北部锡那罗亚州，全线长214.7公里，新建542基铁塔及2个400千伏变电站扩建，合同金额1.54亿美元",
    "https://news.goalfore.cn/latest/detail/103573.html",
    "Actor: POWERCHINA Jiangxi Electric Power Construction (PRC SOE unit) — prc. Company-attributed GoalFore reprint. CapEx USD 154m UNVERIFIED proxy. First Mexico power_plants_grid row.",
    "hunt_energy_power_plants_grid",
    investment_type="epc",
    evidence="proxy",
    bib_type="company",
    chicago='Jiangxi Electric Power Construction Co., Ltd. (POWERCHINA), via GoalFore. “喜报！墨西哥I20二期1标段输变电项目一次性成功并网送电.” July 14, 2026. https://news.goalfore.cn/latest/detail/103573.html.',
    annotation="Jiangxi/POWERCHINA-attributed: I20 Phase II Lot 1 COD + USD 154m contract (UNVERIFIED). Supports powerchina_mexico_i20_p2_lot1_154m.",
    evid_note="Opened GoalFore 14 Jul 2026 Jiangxi Electric Power Construction I20 Lot 1 energization notice.",
)

# 3. wind / allied — Vestas Guatemala 63 MW order
row_doc(
    "vestas_guatemala_63mw_2024",
    "energy",
    "wind",
    "allied",
    "Vestas — 63 MW Guatemala order (14 × V150-4.5 MW)",
    "Guatemala",
    "30 Dec 2024 Vestas company news: Q4 order intake includes undisclosed Guatemala project, 63 MW, 14 × V150-4.5 MW turbines, 5-year AOM 5000 service agreement; commissioning planned Q4 2026; customer/project name undisclosed. CapEx blank. Fills Guatemala×wind empty cell.",
    "",
    "",
    "2024",
    "",
    "",
    "Guatemala (site undisclosed on Vestas order table; lat/lon left blank).",
    "vestas_q4_orders_guatemala_20241230",
    "Guatemala | Americas | Undisclosed | Undisclosed | 63 | 14 x V150-4.5 MW | 5-year AOM 5000 Service Agreement | Commissioning planned for Q4 of 2026",
    "https://www.vestas.com/en/media/company-news/2024/vestas-announces-three-new-orders-for-a-total-of-276-mw-c4086980",
    "Actor: Vestas Wind Systems A/S (Aarhus, Denmark HQ) — allied. Company English primary. CapEx blank. First Guatemala wind row.",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Vestas Wind Systems A/S. “Vestas Announces Three New Orders for a Total of 276 MW.” December 30, 2024. https://www.vestas.com/en/media/company-news/2024/vestas-announces-three-new-orders-for-a-total-of-276-mw-c4086980.',
    annotation="Vestas primary: Guatemala 63 MW / 14 V150-4.5 MW order. Supports vestas_guatemala_63mw_2024.",
    evid_note="Opened Vestas 30 Dec 2024 Q4 orders release (Guatemala 63 MW).",
)

# 4. power_plants_grid / allied — GEB Transnova IFC up to USD 65m (Guatemala)
row_doc(
    "geb_transnova_ifc_65m_guatemala",
    "energy",
    "power_plants_grid",
    "allied",
    "Grupo Energía Bogotá / Transnova — IFC loan up to USD 65m (San Juan Comalapa + Atlántico TX)",
    "Guatemala",
    "IFC ESRS disclosure project 49962: proposed investment of one or more loans aggregating up to USD 65.0 million to Transmisora de Energía Renovable S.A. (Transnova), subsidiary of Conecta Energías / Grupo Energía Bogotá (Colombia HQ); finances San Juan Comalapa 230/69 kV 150 MVA SE + ~5 km TL (construction began 2024; ops expected Aug 2026) and Atlántico 230/69 kV SE + ~52 km 230 kV Morales–Atlántico TL (ops ~Jan 2030). CapEx/financing = up to USD 65m IFC face. Fills Guatemala×power_plants_grid empty cell.",
    "65000000",
    "2026-02-01",
    "2026",
    "14.740",
    "-90.800",
    "San Juan Comalapa substation / Chimaltenango, Guatemala (SJC pin; Atlántico corridor separate).",
    "ifc_transnova_esrs_49962",
    "The proposed investment entails one or more loans, for an aggregate amount of up to US$65.0 million, to Transmisora de Energia Renovable S.A. (“Transnova” or the “Company”). … Construction of SJC began in 2024, and the subproject is expected to commence operations in August 2026. It includes a 230/69 kV substation with 150 MVA capacity and approximately 5 km of transmission line",
    "https://disclosures.ifc.org/project-detail/ESRS/49962/transnova",
    "Actor: Transnova / Grupo Energía Bogotá (Bogotá HQ) — allied. IFC English ESRS primary. Up to USD 65m IFC loans. First Guatemala power_plants_grid row.",
    "hunt_energy_power_plants_grid",
    investment_type="financing",
    bib_type="government",
    chicago='International Finance Corporation. “49962 – Transnova.” Environmental and Social Review Summary. Accessed October 2, 2026. https://disclosures.ifc.org/project-detail/ESRS/49962/transnova.',
    annotation="IFC ESRS: Transnova/GEB up to USD 65m for Guatemala SJC+Atlántico transmission. Supports geb_transnova_ifc_65m_guatemala.",
    evid_note="Opened IFC ESRS 49962 Transnova (up to USD 65m; SJC/Atlántico).",
)

# 5–6. graphite thin top-up / paired WITS Mexico HS 250410 2023 US vs China imports
row_doc(
    "wits_mexico_graphite_us_imp_2023",
    "resources",
    "graphite",
    "us",
    "United States — Mexico HS 250410 natural graphite imports (WITS/Comtrade)",
    "Mexico",
    "WITS/Comtrade Mexico 2023 imports of HS 250410 (natural graphite powder/flakes): USD 5,101.27 thousand from United States (3,087,900 kg). Trade-flow presence; not a mine CapEx. Paired same-year China origin (wits_mexico_graphite_china_imp_2023). Fills Mexico×graphite empty cell.",
    "5101270",
    "2023-12-31",
    "2023",
    "19.430",
    "-99.130",
    "Mexico import gateway proxy (national pin; not a single mill).",
    "wits_mex_250410_2023",
    "Mexico imported Natural graphite in powder or in flakes from United States ($5,101.27K , 3,087,900 Kg), China ($471.89K , 325,843 Kg)",
    "https://wits.worldbank.org/trade/comtrade/en/country/MEX/year/2023/tradeflow/Imports/partner/ALL/product/250410",
    "Actor: United States export origin into Mexico — us. WITS/Comtrade official trade mirror. Paired China row. Thin graphite top-up.",
    "hunt_res_graphite",
    investment_type="other",
    evidence="paired",
    bib_type="government",
    chicago='World Bank. “Mexico Natural Graphite in Powder or in Flakes Imports by Country | 2023.” World Integrated Trade Solution (WITS)/Comtrade. https://wits.worldbank.org/trade/comtrade/en/country/MEX/year/2023/tradeflow/Imports/partner/ALL/product/250410.',
    annotation="WITS Mexico HS 250410 2023 imports: US USD 5.101m. Supports wits_mexico_graphite_us_imp_2023.",
    evid_note="Opened WITS Mexico HS 250410 2023 imports-by-partner table.",
    pair_id="wits_mex_graphite_2023_us_cn",
    counterpart_side="prc",
    counterpart_actor="China",
    counterpart_value="471890",
    counterpart_currency="USD",
    counterpart_value_usd="471890",
    gap="10.806",
)

row_doc(
    "wits_mexico_graphite_china_imp_2023",
    "resources",
    "graphite",
    "prc",
    "China — Mexico HS 250410 natural graphite imports (WITS/Comtrade)",
    "Mexico",
    "WITS/Comtrade Mexico 2023 imports of HS 250410 (natural graphite powder/flakes): USD 471.89 thousand from China (325,843 kg). Trade-flow presence; not a mine CapEx. Paired same-year U.S. origin (wits_mexico_graphite_us_imp_2023).",
    "471890",
    "2023-12-31",
    "2023",
    "19.430",
    "-99.130",
    "Mexico import gateway proxy (national pin; not a single mill).",
    "wits_mex_250410_2023",
    "Mexico imported Natural graphite in powder or in flakes from United States ($5,101.27K , 3,087,900 Kg), China ($471.89K , 325,843 Kg)",
    "https://wits.worldbank.org/trade/comtrade/en/country/MEX/year/2023/tradeflow/Imports/partner/ALL/product/250410",
    "Actor: China export origin into Mexico — prc. WITS/Comtrade official trade mirror. Paired U.S. row. Thin graphite top-up.",
    "hunt_res_graphite",
    investment_type="other",
    evidence="paired",
    bib_type="government",
    chicago='World Bank. “Mexico Natural Graphite in Powder or in Flakes Imports by Country | 2023.” World Integrated Trade Solution (WITS)/Comtrade. https://wits.worldbank.org/trade/comtrade/en/country/MEX/year/2023/tradeflow/Imports/partner/ALL/product/250410.',
    annotation="WITS Mexico HS 250410 2023 imports: China USD 0.472m. Supports wits_mexico_graphite_china_imp_2023.",
    evid_note="Opened WITS Mexico HS 250410 2023 imports-by-partner table (China line).",
    pair_id="wits_mex_graphite_2023_us_cn",
    counterpart_side="us",
    counterpart_actor="United States",
    counterpart_value="5101270",
    counterpart_currency="USD",
    counterpart_value_usd="5101270",
    gap="-10.806",
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
    print(f"Cycle 164 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
