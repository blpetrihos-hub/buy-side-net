#!/usr/bin/env python3
"""Cycle 99 hunt: shuffle_seed=20261099; equal budget; U.S./PRC split; thin after.

Order: bridges_roads, other_renewables, graphite, port_cranes, wind, fission_smr,
water, nickel, port_ownership, solar, lithium, copper, niobium, balsa,
power_plants_grid, building_materials, rail, engineering_epc.
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


# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA LPC PR-10 Utuado 2022 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_lpc_pr10_utuado_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "LPC Contractors Inc — FHWA Emergency Relief PR-10 km 41.6–47.5 (Utuado)",
        "country": "Puerto Rico",
        "asset": "10 Mar 2022: FHWA awards firm-fixed-price contract 693C7322C000008 to LPC Contractors Inc for Project PR ER PRMNT RPR(10) — repairing hurricane damage on PR-10 between km 41.6 and 47.5 (embankment reconstruction, reinforced soil slopes, drainage); obligated USD 84,195,124.82; place of performance Utuado. Distinct from LPC Utuado 46-slide 2023 and LPC Adjuntas/Ciales awards.",
        "investment_type": "epc",
        "value": "84195124.82",
        "currency": "USD",
        "value_usd": "84195124.82",
        "fx_usd": "1",
        "fx_date": "2022-03-10",
        "year": "2022",
        "status": "active",
        "lat": "18.266",
        "lon": "-66.700",
        "geo_note": "Utuado Municipality, Puerto Rico (USASpending place of performance; PR-10 corridor).",
        "evidence": "documented",
        "source_id": "usaspending_lpc_pr10_utuado_20220310",
        "note": "Actor: LPC Contractors Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_lpc_pr10_utuado_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_lpc_pr10_utuado_20220310",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000008_6925_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "PROJECT PR ER PRMNT RPR (10)  THE PROJECT CONSISTS OF REPAIRING DAMAGE CAUSED BY HURRICANES IRMA AND MARIA ON PR-10 BETWEEN KMS 41.6 AND 47.5.  THE WORK INCLUDES EMBANKMENT RECONSTRUCTION, REINFORCED SOIL SLOPE SYSTEMS CONSTRUCTION, DRAINAGE SYSTEM",
        "note": "Opened USASpending Award API: LPC; USD 84,195,124.82; date_signed 2022-03-10; PoP Utuado, PR.",
    },
    {
        "id": "usaspending_lpc_pr10_utuado_20220310",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7322C000008_6925_-NONE-_-NONE- (LPC Contractors Inc; FHWA Emergency Relief PR-10 Utuado). Signed 10 March 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000008_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000008_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 84.20m FHWA award to LPC for PR-10 km 41.6–47.5 repairs in Utuado. Supports fhwa_lpc_pr10_utuado_2022.",
        "supports": ["fhwa_lpc_pr10_utuado_2022", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA JM Caribbean signs East/Metro (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_jm_caribbean_signs_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "J.M. Caribbean Builders Corp — FHWA Emergency Relief signs/guardrails (East & Metro)",
        "country": "Puerto Rico",
        "asset": "26 May 2022: FHWA awards firm-fixed-price contract 693C7322C000014 to J.M. Caribbean Builders Corp for Project PR ER PRMNT RPR(7) — repairing signs and guardrails damaged by Hurricanes Irma and Maria in East & Metro regions; obligated USD 22,614,111.42; place of performance Adjuntas (multi-region scope). Distinct from Caribbean Sign 2026 Metro/North/South and JC Associates West awards.",
        "investment_type": "epc",
        "value": "22614111.42",
        "currency": "USD",
        "value_usd": "22614111.42",
        "fx_usd": "1",
        "fx_date": "2022-05-26",
        "year": "2022",
        "status": "active",
        "lat": "18.163",
        "lon": "-66.722",
        "geo_note": "Adjuntas Municipality, Puerto Rico (USASpending place of performance; East & Metro regional scope).",
        "evidence": "documented",
        "source_id": "usaspending_jm_caribbean_20220526",
        "note": "Actor: J.M. Caribbean Builders Corp (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_jm_caribbean_signs_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jm_caribbean_20220526",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000014_6925_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "PROJECT PR ER PRMNT RPR(7): THE PROJECT CONSISTS OF REPAIRING SIGNS AND GUARDRAILS DAMAGED BY HURRICANES IRMA AND MARIA ON EAST & METRO REGIONS AND OTHER MISCELLANEOUS WORK.",
        "note": "Opened USASpending Award API: J.M. Caribbean Builders Corp; USD 22,614,111.42; date_signed 2022-05-26.",
    },
    {
        "id": "usaspending_jm_caribbean_20220526",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7322C000014_6925_-NONE-_-NONE- (J.M. Caribbean Builders Corp; FHWA Emergency Relief East & Metro signs/guardrails). Signed 26 May 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000014_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000014_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 22.61m FHWA award to J.M. Caribbean for East & Metro signs/guardrails. Supports fhwa_jm_caribbean_signs_2022.",
        "supports": ["fhwa_jm_caribbean_signs_2022", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA DDD-DVG Aibonito multi-route (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_ddd_dvg_aibonito_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "DDD-DVG Joint Venture LLC — FHWA Emergency Relief PR-14/722/796/179/181 (Aibonito)",
        "country": "Puerto Rico",
        "asset": "16 Sep 2022: FHWA awards firm-fixed-price contract 693C7322C000021 to DDD-DVG Joint Venture LLC for Project PR ER DOT PRMNT RPR(13) — repairing hurricane damage on PR-14 km 54.3–54.4, PR-722 km 5.7, PR-796 km 4.4, PR-179 km 13.25, and PR-181 km 8.7 and 46.4; obligated USD 12,983,224.75; place of performance Aibonito. Distinct from DDD-DVG Canóvanas 2026 design-build award.",
        "investment_type": "epc",
        "value": "12983224.75",
        "currency": "USD",
        "value_usd": "12983224.75",
        "fx_usd": "1",
        "fx_date": "2022-09-16",
        "year": "2022",
        "status": "active",
        "lat": "18.140",
        "lon": "-66.266",
        "geo_note": "Aibonito Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_ddd_dvg_aibonito_20220916",
        "note": "Actor: DDD-DVG Joint Venture LLC (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_ddd_dvg_aibonito_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_ddd_dvg_aibonito_20220916",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000021_6925_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(13):  THE PROJECT CONSISTS OF REPAIRING DAMAGE CAUSED BY HURRICANES IRMA AND MARIA ON PR-14, KM 54.3-54.4; PR-722, KM 5.7; PR-796, KM 4.4; PR-179, KM 13.25; AND PR-181, KMS 8.7 AND 46.4.",
        "note": "Opened USASpending Award API: DDD-DVG JV; USD 12,983,224.75; date_signed 2022-09-16; PoP Aibonito, PR.",
    },
    {
        "id": "usaspending_ddd_dvg_aibonito_20220916",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7322C000021_6925_-NONE-_-NONE- (DDD-DVG Joint Venture LLC; FHWA Emergency Relief Aibonito multi-route). Signed 16 September 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000021_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000021_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 12.98m FHWA award to DDD-DVG for multi-route repairs in Aibonito. Supports fhwa_ddd_dvg_aibonito_2022.",
        "supports": ["fhwa_ddd_dvg_aibonito_2022", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Nieves Ángeles / Utuado (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_nieves_angeles_utuado_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Nieves & Nieves Engineers & Contractors Inc — FHWA Emergency Relief PR-2/119/123/128/440 (Ángeles)",
        "country": "Puerto Rico",
        "asset": "30 Jan 2022: FHWA awards firm-fixed-price contract 693C7322C000005 to Nieves & Nieves Engineers & Contractors Inc for Project PR ER PRMNT RPR(9) — repairing landslide and washout damage on PR-2, PR-119, PR-123, PR-128, and PR-440 (embankment restoration, gravity retaining walls, gabion baskets); obligated USD 7,005,307.72; place of performance Ángeles, Utuado. Distinct from Nieves Lares 2024 award.",
        "investment_type": "epc",
        "value": "7005307.72",
        "currency": "USD",
        "value_usd": "7005307.72",
        "fx_usd": "1",
        "fx_date": "2022-01-30",
        "year": "2022",
        "status": "active",
        "lat": "18.292",
        "lon": "-66.799",
        "geo_note": "Ángeles barrio, Utuado Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_nieves_angeles_20220130",
        "note": "Actor: Nieves & Nieves Engineers & Contractors Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_nieves_angeles_utuado_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_nieves_angeles_20220130",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000005_6925_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "PROJECT PR ER PRMNT RPR(9)  THE PROJECT CONSISTS OF REPAIRING LANDSLIDE AND WASHOUT DAMAGE BY HURRICANES IRMA AND MARIA ON PR-2, PR-119, PR-123, PR-128 AND PR-440.",
        "note": "Opened USASpending Award API: Nieves & Nieves; USD 7,005,307.72; date_signed 2022-01-30; PoP Ángeles, PR.",
    },
    {
        "id": "usaspending_nieves_angeles_20220130",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7322C000005_6925_-NONE-_-NONE- (Nieves & Nieves Engineers & Contractors Inc; FHWA Emergency Relief Ángeles/Utuado). Signed 30 January 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000005_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000005_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 7.01m FHWA award to Nieves & Nieves for multi-route landslide repairs. Supports fhwa_nieves_angeles_utuado_2022.",
        "supports": ["fhwa_nieves_angeles_utuado_2022", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Caribe Tecno El Yunque (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_caribe_tecno_yunque_2021",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Caribe Tecno CRL — FHWA/USFS Emergency Relief El Yunque forest roads",
        "country": "Puerto Rico",
        "asset": "9 Sep 2021: FHWA awards firm-fixed-price contract 693C7321C000021 to Caribe Tecno CRL for Project PR ERFO FS 2017-1(3) — repairing multiple storm-damaged sites on PR-191, PR-930, PR-988, PR-9938, PR-9966, and PR-186 within El Yunque National Forest for the U.S. Forest Service; obligated USD 13,974,869.23; place of performance Palmer / Río Grande. Distinct from Maglez / LPC / Novel FHWA highway ER awards.",
        "investment_type": "epc",
        "value": "13974869.23",
        "currency": "USD",
        "value_usd": "13974869.23",
        "fx_usd": "1",
        "fx_date": "2021-09-09",
        "year": "2021",
        "status": "active",
        "lat": "18.374",
        "lon": "-65.764",
        "geo_note": "Palmer / Río Grande near El Yunque National Forest, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_caribe_tecno_yunque_20210909",
        "note": "Actor: Caribe Tecno CRL (Puerto Rico / U.S.) + FHWA/USFS — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_caribe_tecno_yunque_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caribe_tecno_yunque_20210909",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000021_6925_-NONE-_-NONE-/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "PROJECT PR ERFO FS 2017 - 1(3) THE PROJECT CONSISTS OF REPAIRING MULTIPLE STORM DAMAGED SITES IN PR-191, PR-930, PR-988, PR-9938, PR-9966, AND PR-186 WITHIN EL YUNQUE NATIONAL FOREST FOR THE UNITED STATES FOREST SERVICE.",
        "note": "Opened USASpending Award API: Caribe Tecno CRL; USD 13,974,869.23; date_signed 2021-09-09; PoP Palmer, PR.",
    },
    {
        "id": "usaspending_caribe_tecno_yunque_20210909",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7321C000021_6925_-NONE-_-NONE- (Caribe Tecno CRL; FHWA/USFS El Yunque forest-road Emergency Relief). Signed 9 September 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000021_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000021_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 13.97m FHWA/USFS award to Caribe Tecno for El Yunque forest-road repairs. Supports fhwa_caribe_tecno_yunque_2021.",
        "supports": ["fhwa_caribe_tecno_yunque_2021", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/port_cranes — ZPMC Chancay STS/RMG/RTG package (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "zpmc_chancay_sts_rmg_rtg_2024",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — Chancay Port quay cranes, RMGs, and multi-purpose RTGs",
        "country": "Peru",
        "asset": "Nov 2024 opening / CCCC 27 Feb 2025 release: Shanghai Zhenhua Heavy Industries (ZPMC) supplied Chancay Port with six quay cranes, 15 rail-mounted gantry cranes, and six multi-purpose rubber-tyred gantry cranes with seismic-resistance features for the CCCC-built smart port (initial design capacity 1 million TEU, 6 million tons bulk, 160,000 vehicles). CapEx for the crane package not disclosed on the opened CCCC page. Distinct from COSCO Chancay ownership and CHEC Chancay EPC rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-11.575",
        "lon": "-77.270",
        "geo_note": "Chancay Port, Lima Region, Peru (CCCC project geography).",
        "evidence": "documented",
        "source_id": "cccc_chancay_zpmc_cranes_20250227",
        "note": "Actor: ZPMC (PRC OEM) — prc. Official CCCC English release naming crane counts. No package USD on page.",
    },
    {
        "id": "zpmc_chancay_sts_rmg_rtg_2024",
        "retrieved": "2026-10-02",
        "source_id": "cccc_chancay_zpmc_cranes_20250227",
        "url": "https://en.ccccltd.cn/xwzx/ywfb/202502/t20250228_219359.html",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "ZPMC supplied Chancay port with six quay cranes, 15 rail-mounted gantry cranes, and six multi-purpose rubber-tyred gantry cranes, all equipped with strong seismic resistance capabilities.",
        "note": "Opened CCCC primary: ZPMC 6 quay + 15 RMG + 6 RTG at Chancay; port opened Nov 2024.",
    },
    {
        "id": "cccc_chancay_zpmc_cranes_20250227",
        "type": "company",
        "chicago": "China Communications Construction Company Limited. “CCCC’s smart innovation powers the construction of Chancay port.” 27 February 2025. https://en.ccccltd.cn/xwzx/ywfb/202502/t20250228_219359.html.",
        "url": "https://en.ccccltd.cn/xwzx/ywfb/202502/t20250228_219359.html",
        "annotation": "CCCC primary naming ZPMC 6 quay + 15 RMG + 6 RTG package at Chancay. Supports zpmc_chancay_sts_rmg_rtg_2024.",
        "supports": ["zpmc_chancay_sts_rmg_rtg_2024", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — EXIM Banco Atlántida / First Solar Olanchito (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_atlantida_olanchito_solar_2022",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "U.S. EXIM / First Solar — Banco Atlántida Olanchito 53.4 MW solar (Honduras)",
        "country": "Honduras",
        "asset": "22 Sep 2022: EXIM Board approves structured-finance transaction AP089465XX for Banco Atlántida S.A. (Tegucigalpa) to procure U.S.-made First Solar panels for a 53.4 MW carbon-free solar project in Olanchito (Parque Solar San José / Olanchito), Honduras; EXIM structured-finance transactions table lists authorized amount USD 52 million; Deal-of-the-Year release (13 Dec 2022) names First Solar as primary exporter and J.P. Morgan as facilitator. Distinct from first_solar_zacapa_exim_guatemala_2021.",
        "investment_type": "financing",
        "value": "52000000",
        "currency": "USD",
        "value_usd": "52000000",
        "fx_usd": "1",
        "fx_date": "2022-09-22",
        "year": "2022",
        "status": "active",
        "lat": "15.481",
        "lon": "-86.574",
        "geo_note": "Olanchito / San José, Yoro Department, Honduras (EXIM environmental listing / project geography).",
        "evidence": "documented",
        "source_id": "exim_olanchito_deal_year_20221213",
        "note": "Actor: U.S. EXIM + First Solar (U.S.) — us. Official EXIM Deal-of-the-Year release + Board minutes AP089465XX; USD 52m from EXIM structured-finance transactions table.",
    },
    {
        "id": "exim_atlantida_olanchito_solar_2022",
        "retrieved": "2026-10-02",
        "source_id": "exim_olanchito_deal_year_20221213",
        "url": "https://www.exim.gov/news/2022-renewable-energy-deal-year-awarded-stakeholders-honduran-solar-project-export-import-bank",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Banco Atlántida, Honduras’ largest bank, will receive financing facilitated by J.P. Morgan to procure American-made solar panels from First Solar to power a 53.4-megawatt carbon-free solar power project in Olanchito, Honduras.",
        "note": "Opened EXIM Deal-of-the-Year primary: First Solar panels for 53.4 MW Olanchito; Board approved Sep 2022 (AP089465XX). USD 52m from EXIM transactions table for Banco Atlantida Honduras solar.",
    },
    {
        "id": "exim_olanchito_deal_year_20221213",
        "type": "government",
        "chicago": "Export-Import Bank of the United States. “2022 Renewable Energy Deal of the Year Awarded to Stakeholders in Honduran Solar Project at Export-Import Bank of the United States Annual Conference.” 13 December 2022. https://www.exim.gov/news/2022-renewable-energy-deal-year-awarded-stakeholders-honduran-solar-project-export-import-bank.",
        "url": "https://www.exim.gov/news/2022-renewable-energy-deal-year-awarded-stakeholders-honduran-solar-project-export-import-bank",
        "annotation": "Official EXIM: First Solar / Banco Atlántida 53.4 MW Olanchito solar; complements USD 52m on EXIM transactions table. Supports exim_atlantida_olanchito_solar_2022.",
        "supports": ["exim_atlantida_olanchito_solar_2022", "hunt_energy_solar"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
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

    hunt_updates = {
        "hunt_infra_bridges_roads": "Cycle 99: logged fhwa_lpc_pr10_utuado_2022 + fhwa_jm_caribbean_signs_2022 + fhwa_ddd_dvg_aibonito_2022 + fhwa_nieves_angeles_utuado_2022 + fhwa_caribe_tecno_yunque_2021 (U.S. FHWA).",
        "hunt_energy_other_renewables": "Cycle 99: equal budget; Sungrow Observatorio / Trina Alma Sur dense (miss).",
        "hunt_res_graphite": "Cycle 99: equal budget; Graphcoa / Atlas Malacacheta dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 99: logged zpmc_chancay_sts_rmg_rtg_2024 (PRC ZPMC at Chancay).",
        "hunt_energy_wind": "Cycle 99: equal budget; Goldwind / Vestas / Envision dense (miss).",
        "hunt_energy_fission_smr": "Cycle 99: equal budget; CAREM / CNNC / CONUAR dense (miss). Thin spare dry.",
        "hunt_res_water": "Cycle 99: equal budget; CCCC El Curval / Acciona / Sacyr dense (miss).",
        "hunt_res_nickel": "Cycle 99: equal budget; MMG / BRN / Westwin dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 99: equal budget; COSCO / Hutchison / CMP dense (miss).",
        "hunt_energy_solar": "Cycle 99: logged exim_atlantida_olanchito_solar_2022 (U.S. EXIM First Solar Honduras).",
        "hunt_res_lithium": "Cycle 99: equal budget; Ganfeng / Yahua / Rio Tinto dense (miss).",
        "hunt_res_copper": "Cycle 99: equal budget; CMOC / Chinalco / Jiangxi dense (miss).",
        "hunt_fenb_araxa": "Cycle 99: equal budget; CMOC/CBMM dense (miss). Thin spare dry.",
        "hunt_res_balsa": "Cycle 99: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_br_power_equip": "Cycle 99: equal budget; GE Vernova / ENGIE / EXIM GTE dense (miss).",
        "hunt_infra_building_materials": "Cycle 99: equal budget; Sinoma dense (miss). Thin spare dry.",
        "hunt_latam_rail_telecom": "Cycle 99: equal budget; USTDA Honduras / PowerChina Chancay / CRCC Batuco dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 99: equal budget; Halliburton / Bechtel / Fluor dense (miss).",
    }
    for hid, note in hunt_updates.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 99 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
