#!/usr/bin/env python3
"""Cycle 163 hunt: shuffle_seed=20261163; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: niobium, lithium, fission_smr, copper, port_cranes, nickel,
building_materials, port_ownership, other_renewables, engineering_epc, rail, wind,
solar, water, graphite, balsa, bridges_roads, power_plants_grid.

Weight under-covered: Colombia copper empty; Mexico rail; Haiti/Venezuela dry.
Sides tied us325/prc325 — keep equal US/PRC budget without padding.
Thin: balsa/graphite/fission once (dry); nickel already used this session.
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


# 1. copper / prc — JCHX completes USD 100m earn-in for 50% Alacrán (Colombia empty cell)
row_doc(
    "jchx_alacran_50pct_100m_earn_in_2025",
    "resources",
    "copper",
    "prc",
    "JCHX Mining Management — 50% earn-in Alacrán copper-gold (Puerto Libertador)",
    "Colombia",
    "3 Jul 2025 Cordoba Minerals: JCHX completes final USD 20m installment under 8 Dec 2022 framework agreement, fulfilling entire USD 100m consideration for 50% of CMH Colombia S.A.S. (Alacrán Project holder); prior installments USD 40m (8 May 2023) and USD 40m (4 Jan 2024). CapEx/investment = USD 100m earn-in face. Distinct from jchx_veritas_alacran_128m_closing_2026 (remaining 50% sale). Fills Colombia×copper empty cell.",
    "100000000",
    "2025-07-03",
    "2025",
    "7.890",
    "-75.670",
    "Alacrán Project / Puerto Libertador, Córdoba Department, Colombia (company geography; approximate).",
    "cordoba_jchx_50pct_earn_in_20250703",
    "Under the Initial Framework Agreement, JCHX committed to acquire and maintain a 50% interest in CMH for total consideration of US$100 million, paid in three installments. The first two installments of US$40 million each were paid on May 8, 2023, and January 4, 2024, respectively, and earned JCHX its 50% interest in CMH. JCHX has now completed the final installment payment of US$20 million, thereby fulfilling its entire US$100 million investment obligation",
    "https://cordobaminerals.com/news/cordoba-and-jchx-mark-50-earn-in-completion-paving-the-way-for-100-ownership-transition-at-alacran/",
    "Actor: JCHX Mining Management Co., Ltd. (Beijing) — prc. Cordoba company English primary. USD 100m earn-in. First Colombia copper row.",
    "hunt_res_copper",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Cordoba Minerals Corp. “Cordoba and JCHX Mark 50% Earn-In Completion, Paving the Way for 100% Ownership Transition at Alacrán.” July 3, 2025. https://cordobaminerals.com/news/cordoba-and-jchx-mark-50-earn-in-completion-paving-the-way-for-100-ownership-transition-at-alacran/.',
    annotation="Cordoba primary: JCHX completes USD 100m / 50% Alacrán earn-in. Supports jchx_alacran_50pct_100m_earn_in_2025.",
    evid_note="Opened Cordoba 3 Jul 2025 (JCHX USD 100m Alacrán 50% earn-in complete).",
)

# 2. copper / prc — JCHX-led Veritas closes remaining 50% Alacrán for USD 128m
row_doc(
    "jchx_veritas_alacran_128m_closing_2026",
    "resources",
    "copper",
    "prc",
    "JCHX-led Veritas Resources — 100% Alacrán Project closing (USD 128m)",
    "Colombia",
    "6 Mar 2026 Cordoba Minerals: closes sale of remaining 50% Alacrán interest plus other Colombia exploration assets to Veritas Resources AG (consortium led by JCHX) for USD 128m cash Closing Cash Payment; Veritas now holds 100% of Alacrán and full operational responsibility. Distinct from jchx_alacran_50pct_100m_earn_in_2025 (prior 50% earn-in).",
    "128000000",
    "2026-03-06",
    "2026",
    "7.890",
    "-75.670",
    "Alacrán Project / Puerto Libertador, Córdoba Department, Colombia.",
    "cordoba_alacran_sale_closing_20260306",
    "Cordoba Minerals Corp. … has closed the sale of its remaining 50% interest in the Alacrán Project in Colombia, along with all other exploration assets in Colombia and certain accounts receivable (the “Transaction”) to Veritas Resources AG (“Veritas”), an entity owned by a consortium of experienced mining investors (the “Consortium”) led by JCHX Mining Management Co., Ltd. (“JCHX”). Upon closing of the Transaction, Cordoba received cash proceeds of US$128 million (the “Closing Cash Payment”). … Veritas now holds a 100% interest in the Alacrán Project",
    "https://cordobaminerals.com/news/cordoba-minerals-announces-closing-of-alacran-asset-sale/",
    "Actor: JCHX-led Veritas consortium — prc control. Cordoba company English primary. USD 128m for remaining 50% + assets. Completes PRC 100% Alacrán ownership milestone.",
    "hunt_res_copper",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Cordoba Minerals Corp. “Cordoba Minerals Announces Closing Of Alacrán Asset Sale.” March 6, 2026. https://cordobaminerals.com/news/cordoba-minerals-announces-closing-of-alacran-asset-sale/.',
    annotation="Cordoba primary: Veritas/JCHX closes Alacrán remaining 50% for USD 128m / 100% ownership. Supports jchx_veritas_alacran_128m_closing_2026.",
    evid_note="Opened Cordoba 6 Mar 2026 (Alacrán USD 128m closing / 100% Veritas-JCHX).",
)

# 3. rail / prc — CRRC ZELC Mexico City Metro Line 1 full opening
row_doc(
    "crrc_cdmx_linea1_full_open_2025",
    "infrastructure",
    "rail",
    "prc",
    "CRRC Zhuzhou Locomotive (ZELC) — Mexico City Metro Line 1 modernization full opening",
    "Mexico",
    "16 Nov 2025 (CRRC English 21/28 Nov): Juanacatlán–Observatorio section of CDMX Metro Línea 1 modernization undertaken by CRRC ZELC inaugurated; all 20 stations along the line fully operational. CapEx blank on opened CRRC page (press elsewhere cites ~MXN 37bn / ~USD 1.84bn package — left UNVERIFIED / not stored). Distinct from crrc_mexico_pachuca_trains_2025 (AIFA–Pachuca EMUs).",
    "",
    "",
    "2025",
    "19.420",
    "-99.180",
    "Mexico City Metro Line 1 corridor (Juanacatlán–Observatorio western section pin; full line 20 stations).",
    "crrc_cdmx_linea1_open_20251121",
    "On November 16 local time, the section between Juanacatlán Station and Observatorio Station of the Mexico City Metro Line 1 modernization project, undertaken by CRRC ZELC (CRRC Zhuzhou Locomotive Co., Ltd.), was officially inaugurated. With this, all 20 stations along the line are now fully operational, marking a milestone achievement for the Mexico City Metro Line 1 project.",
    "https://www.crrcgc.cc/zjen/2025-11/21/article_2025112111480272511.html",
    "Actor: CRRC Zhuzhou Locomotive / CRRC ZELC (PRC SOE) — prc. Company English primary. CapEx blank. Opening milestone for CDMX Line 1 modernization.",
    "hunt_infra_rail",
    investment_type="epc",
    bib_type="company",
    chicago='CRRC Corporation Limited. “CRRC Supports Full Opening of Mexico City Metro Line 1.” November 21, 2025. https://www.crrcgc.cc/zjen/2025-11/21/article_2025112111480272511.html.',
    annotation="CRRC primary: CDMX Metro Line 1 full opening after ZELC modernization. Supports crrc_cdmx_linea1_full_open_2025.",
    evid_note="Opened CRRC English 21 Nov 2025 (Line 1 full opening).",
)

# 4. port_cranes / allied — Konecranes 8 electric RTGs Puerto Antioquia
row_doc(
    "konecranes_puerto_antioquia_8rtg_2023",
    "infrastructure",
    "port_cranes",
    "allied",
    "Konecranes — 8 electric cable-reel RTGs (Puerto Antioquia / Urabá)",
    "Colombia",
    "19 Sep 2023 Konecranes: order booked August 2023 for eight fully electric cable-reel RTGs for new container terminal at Puerto Antioquia, ordered by Puerto Bahía Colombia de Urabá (key shareholder CMA CGM Group). CapEx blank. Distinct from konecranes_cartagena_rtg_2025 (25 RTGs Cartagena).",
    "",
    "",
    "2023",
    "8.020",
    "-76.740",
    "Puerto Antioquia / Gulf of Urabá near Nueva Colonia, Turbo, Antioquia, Colombia.",
    "konecranes_puerto_antioquia_8rtg_20230919",
    "The 8 Rubber-Tired Gantry (RTG) cranes will be delivered to a new container terminal at Puerto Antioquia, Colombia … The order was booked in August 2023. The eight RTGs for Puerto Antioquia were ordered by Puerto Bahia Colombia de Uraba, whose key shareholder is the CMA CGM Group … They are fully electric, powered by cable reels connected to the local grid.",
    "https://www.konecranes.com/en-us/press-releases/konecranes-wins-8-rtg-order-for-new-container-terminal-in-colombia-in-drive-for-sustainable-globalization",
    "Actor: Konecranes (Nasdaq Helsinki; Finland HQ) — allied. Company English primary. CapEx blank.",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Konecranes. “Konecranes Wins 8 RTG Order for a New Container Terminal in Colombia in Drive for Sustainable Globalization.” September 19, 2023. https://www.konecranes.com/en-us/press-releases/konecranes-wins-8-rtg-order-for-new-container-terminal-in-colombia-in-drive-for-sustainable-globalization.',
    annotation="Konecranes primary: 8 electric RTGs for Puerto Antioquia Aug 2023 order. Supports konecranes_puerto_antioquia_8rtg_2023.",
    evid_note="Opened Konecranes 19 Sep 2023 (Puerto Antioquia 8 RTG order).",
)

# 5. port_ownership / allied — CMA Terminals shareholder Puerto Antioquia
row_doc(
    "cma_puerto_antioquia_colombia",
    "infrastructure",
    "port_ownership",
    "allied",
    "CMA Terminals / CMA CGM — Puerto Antioquia deep-water terminal (Urabá)",
    "Colombia",
    "11 Feb 2026 CMA CGM: first large containership (CMA CGM FIORDLAND, 5,900 TEU) calls at Puerto Antioquia; CMA Terminals is shareholder/contributor to the new multipurpose deep-water terminal (3.8 km viaduct to offshore platform; designed for up to 15,000 TEU vessels; expected ~650,000 TEU/y; 3 STS + 8 electric RTGs). CapEx blank on opened page (IDB Invest elsewhere cites ~USD 650–706m total project — not stored from this primary). Distinct from apm_tcbuen_buenaventura_colombia. Complements konecranes_puerto_antioquia_8rtg_2023.",
    "",
    "",
    "2026",
    "8.020",
    "-76.740",
    "Puerto Antioquia / Bahía Colombia, Gulf of Urabá, Nueva Colonia–Turbo, Antioquia, Colombia.",
    "cma_cgm_puerto_antioquia_20260211",
    "CMA Terminals, in partnership with local pure players and international investors, is a shareholder and contributor to the development of the new facility of Puerto Antioquia. … Construction of the terminal began in 2022. … a 3.8-kilometer viaduct connects the onshore yard to an offshore platform capable of accommodating up to five container vessels simultaneously. … The terminal’s expected annual handling capacity includes: 650,000 TEUs per year … To support efficient and sustainable operations, the terminal is equipped with: 3 Ship-to-Shore (STS) cranes and 8 electric Rubber-Tired Gantry (RTG) cranes",
    "https://www.cmacgm-group.com/en/news-media/cma-cgm-group-welcomes-first-large-containership-puerto-antioquia-new-gateway-colombia",
    "Actor: CMA Terminals / CMA CGM Group (Marseille HQ) — allied. Company English primary. CapEx blank. Caribbean Colombia gateway ownership presence.",
    "hunt_infra_port_ownership",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='CMA CGM Group. “CMA CGM Group Welcomes First Large Containership at Puerto Antioquia, a New Gateway for Colombia’s Export Growth.” February 11, 2026. https://www.cmacgm-group.com/en/news-media/cma-cgm-group-welcomes-first-large-containership-puerto-antioquia-new-gateway-colombia.',
    annotation="CMA CGM primary: CMA Terminals shareholder at Puerto Antioquia / first large boxship call. Supports cma_puerto_antioquia_colombia.",
    evid_note="Opened CMA CGM 11 Feb 2026 (Puerto Antioquia shareholder + first call).",
)

# 6. solar / us — AES ADRE IDB Invest ~USD 368m Caribbean renewables package
row_doc(
    "aes_adre_idb_368m_dr_2023",
    "energy",
    "solar",
    "us",
    "AES Dominicana Renewable Energy (ADRE) — IDB Invest ~USD 368m NCRE financing package",
    "Dominican Republic",
    "22 Nov 2023 IDB Invest: ~USD 368m loan package to AES Dominicana Renewable Energy S.A. (AES Corp subsidiary) to finance design/construction/operation of three new NCRE projects totaling 240 MWac and refinance short-term debt on three additional renewable projects totaling 150 MWac (expand portfolio 150→390 MWac); USD 37m IDB Invest + USD 331m mobilized; JP Morgan among joint lead arrangers. CapEx/financing = ~USD 368m package face. Distinct from plant-level aes_dr_peravia / mirasol / bayasol / santanasol / bess rows.",
    "368000000",
    "2023-11-22",
    "2023",
    "18.430",
    "-69.970",
    "AES Dominicana renewable portfolio / Dominican Republic (national pin; Bayasol pictured on IDB Invest page).",
    "idb_invest_aes_adre_368m_20231122",
    "IDB Invest provided a loan package of approximately $368 million to AES Dominicana Renewable Energy S.A. (ADRE), a subsidiary of The AES Corporation in the Dominican Republic, to finance the design, construction and operation of three new non-conventional renewable energy (NCRE) projects totaling 240MWac of installed capacity, and to refinance the short-term debt of three additional renewable energy projects totaling 150MWac of installed capacity. The financing package consists of $37 million from IDB Invest and $331 million mobilized from 21 financial institutions.",
    "https://idbinvest.org/en/news-media/idb-invest-mobilizes-largest-renewable-energy-financing-caribbean-aes",
    "Actor: AES Corporation via ADRE (U.S. HQ) borrower/owner — us. IDB Invest English primary. USD ~368m financing package. Largest Caribbean renewables financing per IDB Invest.",
    "hunt_energy_solar",
    investment_type="financing",
    bib_type="government",
    chicago='IDB Invest. “IDB Invest Mobilizes the Largest Renewable Energy Financing in the Caribbean for AES.” November 22, 2023. https://idbinvest.org/en/news-media/idb-invest-mobilizes-largest-renewable-energy-financing-caribbean-aes.',
    annotation="IDB Invest primary: ~USD 368m ADRE/AES DR renewables package (240 MWac new + 150 MWac refinance). Supports aes_adre_idb_368m_dr_2023.",
    evid_note="Opened IDB Invest 22 Nov 2023 (AES ADRE ~USD 368m package).",
)

# 7. engineering_epc / us — Sheladia-style already dense; use USACE Quetzal? already.
# Add JCHX June earn-in bridge is enough. One more US: check Fluor.
# Actually add Global Infrastructure Partners if we open IDB page - skip.
# Use Cordoba seller Ivanhoe Electric? Weak.
# Add second US: AES ADRE is one. Search showed little Haiti.
# Log nothing else rather than pad.


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
    print(f"Cycle 163 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
