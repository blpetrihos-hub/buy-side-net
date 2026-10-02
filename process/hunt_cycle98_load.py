#!/usr/bin/env python3
"""Cycle 98 hunt: shuffle_seed=20261098; equal budget; U.S./PRC split; thin after.

Order (BRIEF taxonomy shuffle): lithium, nickel, power_plants_grid, rail, balsa,
fission_smr, graphite, bridges_roads, water, niobium, engineering_epc,
other_renewables, wind, port_cranes, solar, building_materials, port_ownership,
copper.
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

# Frankfurter/ECB EURUSD 2022-12-30 = 1.0666 (BOC Demerara loan signing date)
EUR_BOC = 160800000
USD_BOC = int(round(EUR_BOC * 1.0666))


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA LPC Ciales PR-144/146/149 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_lpc_pr144_ciales_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "LPC Contractors Inc — FHWA Emergency Relief PR-144/146/149 landslide repairs (Ciales)",
        "country": "Puerto Rico",
        "asset": "7 Jun 2024: FHWA awards firm-fixed-price contract 693C7324C000010 to LPC Contractors Inc (U.S.-owned) for Project PR ER DOT PRMNT RPR(18) — repairing landslides from Hurricanes Irma and Maria on PR-144 (km 18.2, 14.35), PR-146 (km 9.8, 14.1, 16.4, 19.3), and PR-149 (km 42.8, 42.9); obligated USD 7,212,477.12; place of performance Ciales. Distinct from LPC Adjuntas 2026 and LPC Utuado 2023 awards.",
        "investment_type": "epc",
        "value": "7212477.12",
        "currency": "USD",
        "value_usd": "7212477.12",
        "fx_usd": "1",
        "fx_date": "2024-06-07",
        "year": "2024",
        "status": "active",
        "lat": "18.336",
        "lon": "-66.469",
        "geo_note": "Ciales Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_lpc_ciales_20240607",
        "note": "Actor: LPC Contractors Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_lpc_pr144_ciales_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_lpc_ciales_20240607",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000010_6925_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(18) THE PROJECT CONSISTS OF REPAIRING LANDSLIDES CAUSED BY HURRICANES IRMA AND MARIA ON PR-144 (KM: 18.2, 14.35); PR-146 (KM: 9.8, 14.1, 16.4, 19.3); AND PR-149 (KM: 42.8, 42.9).",
        "note": "Opened USASpending Award API: LPC Contractors Inc; USD 7,212,477.12; date_signed 2024-06-07; PoP Ciales, PR.",
    },
    {
        "id": "usaspending_lpc_ciales_20240607",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7324C000010_6925_-NONE-_-NONE- (LPC Contractors Inc; FHWA Emergency Relief PR-144/146/149 Ciales). Signed 7 June 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000010_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000010_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 7.21m FHWA award to LPC for PR-144/146/149 landslide repairs in Ciales. Supports fhwa_lpc_pr144_ciales_2024.",
        "supports": ["fhwa_lpc_pr144_ciales_2024", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Obratec Barranquitas (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_obratec_barranquitas_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Obratec Contratista General Inc — FHWA Emergency Relief PR-152 landslide repairs (Barranquitas)",
        "country": "Puerto Rico",
        "asset": "22 Jan 2024: FHWA awards firm-fixed-price contract 693C7324C000005 to Obratec Contratista General Inc (U.S.-owned) for Project PR ER DOT PRMNT RPR(15) — repairing landslides from Hurricanes Irma and Maria on PR-152R km 1.2 and PR-152 km 1.2, 3.05, 3.4, 3.1, and 5.30–5.40 in Barranquitas Municipality; obligated USD 8,249,000.80. Distinct from Maglez / LPC / Novel FHWA rows.",
        "investment_type": "epc",
        "value": "8249000.8",
        "currency": "USD",
        "value_usd": "8249000.8",
        "fx_usd": "1",
        "fx_date": "2024-01-22",
        "year": "2024",
        "status": "active",
        "lat": "18.187",
        "lon": "-66.306",
        "geo_note": "Barranquitas Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_obratec_barranquitas_20240122",
        "note": "Actor: Obratec Contratista General Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_obratec_barranquitas_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_obratec_barranquitas_20240122",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000005_6925_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(15): THE PROJECT CONSISTS OF REPAIRING LANDSLIDES CAUSED BY HURRICANES IRMA AND MARIA ON PR-152R KM 1.2; AND PR-152 KM1.2, 3.05, 3.4, 3.1, AND 5.30-5.40 IN THE MUNICIPALITY OF BARRANQUITAS, PUERTO RICO.",
        "note": "Opened USASpending Award API: Obratec Contratista General Inc; USD 8,249,000.80; date_signed 2024-01-22; PoP Barranquitas, PR.",
    },
    {
        "id": "usaspending_obratec_barranquitas_20240122",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7324C000005_6925_-NONE-_-NONE- (Obratec Contratista General Inc; FHWA Emergency Relief PR-152 Barranquitas). Signed 22 January 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000005_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000005_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 8.25m FHWA award to Obratec for PR-152 landslide repairs in Barranquitas. Supports fhwa_obratec_barranquitas_2024.",
        "supports": ["fhwa_obratec_barranquitas_2024", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA LPC Utuado 46 landslides (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_lpc_utuado_46slides_2023",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "LPC Contractors Inc — FHWA Emergency Relief 46 landslide/washout repairs (Utuado / PR-111)",
        "country": "Puerto Rico",
        "asset": "6 Sep 2023: FHWA awards firm-fixed-price contract 693C7323C000017 to LPC Contractors Inc for Project PR ER DOT PRMNT RPR(14) — repairing 46 landslides, pavement washouts, and miscellaneous hurricane damages on PR-111 corridor; obligated USD 41,115,000; place of performance Utuado. Distinct from LPC PR-10 Utuado 2022 (693C7322C000008) and LPC Adjuntas/Ciales awards.",
        "investment_type": "epc",
        "value": "41115000",
        "currency": "USD",
        "value_usd": "41115000",
        "fx_usd": "1",
        "fx_date": "2023-09-06",
        "year": "2023",
        "status": "active",
        "lat": "18.266",
        "lon": "-66.700",
        "geo_note": "Utuado Municipality, Puerto Rico (USASpending place of performance; PR-111 corridor).",
        "evidence": "documented",
        "source_id": "usaspending_lpc_utuado_20230906",
        "note": "Actor: LPC Contractors Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_lpc_utuado_46slides_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_lpc_utuado_20230906",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000017_6925_-NONE-_-NONE-/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "PR ER DOT PRMNT RPR(14) - LANDSLIDE REPAIRS, WASHOUTS AND MISC WORK. THE PROJECT CONSISTS OF THE REPAIRS 46 LANDSLIDES, PAVEMENT WASHOUTS, AND OTHER MISCELLANEOUS DAMAGES CAUSED BY HURRICANES IRMA AND MARIA. THE DAMAGES ARE LOCATED IN PR-111 BETWEEN",
        "note": "Opened USASpending Award API: LPC Contractors Inc; USD 41,115,000; date_signed 2023-09-06; PoP Utuado, PR.",
    },
    {
        "id": "usaspending_lpc_utuado_20230906",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323C000017_6925_-NONE-_-NONE- (LPC Contractors Inc; FHWA Emergency Relief PR-111 Utuado 46 landslides). Signed 6 September 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000017_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000017_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 41.12m FHWA award to LPC for 46 landslide/washout repairs in Utuado. Supports fhwa_lpc_utuado_46slides_2023.",
        "supports": ["fhwa_lpc_utuado_46slides_2023", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Novel Ciales multi-route (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_novel_ciales_multi_2023",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Novel Construction LLC — FHWA Emergency Relief PR-5568/568/157/155/156 repairs (Ciales)",
        "country": "Puerto Rico",
        "asset": "25 Jul 2023: FHWA awards firm-fixed-price contract 693C7323C000013 to Novel Construction LLC for hurricane damage repairs on PR-5568 (km 0.7–0.8), PR-568 (km 25.85), PR-157 (km 1.2, 10.4, 16.4, 21.3), PR-155 (km 30.1–30.2), and PR-156 (km 3.6, 4.4, 6.3–6.4, 3.7–3.8); obligated USD 15,510,660.50; place of performance Ciales. Distinct from Novel PR-155 Morovis 2024 award.",
        "investment_type": "epc",
        "value": "15510660.5",
        "currency": "USD",
        "value_usd": "15510660.5",
        "fx_usd": "1",
        "fx_date": "2023-07-25",
        "year": "2023",
        "status": "active",
        "lat": "18.336",
        "lon": "-66.469",
        "geo_note": "Ciales Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_novel_ciales_20230725",
        "note": "Actor: Novel Construction LLC (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_novel_ciales_multi_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_novel_ciales_20230725",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000013_6925_-NONE-_-NONE-/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "THE PROJECT CONSISTS OF REPAIRING DAMAGE CAUSED BY HURRICANES IRMA AND MARIA ON PR-5568, KMS 0.7 AND 0.8; PR 568 KM 25.85; PR-157, KMS 1.2, 10.4, 16.4, AND 21.3; PR-155, KM 30.1 AND 30.2; AND PR-156, KMS 3.6, 4.4, 6.3-6.4, AND 3.7-3.8.",
        "note": "Opened USASpending Award API: Novel Construction LLC; USD 15,510,660.50; date_signed 2023-07-25; PoP Ciales, PR.",
    },
    {
        "id": "usaspending_novel_ciales_20230725",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323C000013_6925_-NONE-_-NONE- (Novel Construction LLC; FHWA Emergency Relief multi-route Ciales). Signed 25 July 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000013_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000013_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 15.51m FHWA award to Novel for multi-route hurricane repairs in Ciales. Supports fhwa_novel_ciales_multi_2023.",
        "supports": ["fhwa_novel_ciales_multi_2023", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Professional Design/Builders USVI (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_professional_stx_bridges_2023",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Professional Design/Builders, Inc. — FHWA temporary bridges / structural repairs (St. Croix)",
        "country": "U.S. Virgin Islands",
        "asset": "23 May 2023: FHWA awards firm-fixed-price contract 693C7323C000009 to Professional Design/Builders, Inc. (U.S.-owned) for Project VI DPW STX(001) — installation of temporary bridges and structural repairs (embankment, aggregate base, approach work, riprap, guardrail); obligated USD 4,765,496.42; place of performance Christiansted, St. Croix. Distinct from Island Roads / VI Paving FHWA rows.",
        "investment_type": "epc",
        "value": "4765496.42",
        "currency": "USD",
        "value_usd": "4765496.42",
        "fx_usd": "1",
        "fx_date": "2023-05-23",
        "year": "2023",
        "status": "active",
        "lat": "17.746",
        "lon": "-64.702",
        "geo_note": "Christiansted, St. Croix, U.S. Virgin Islands (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_professional_stx_20230523",
        "note": "Actor: Professional Design/Builders, Inc. (U.S. Virgin Islands / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_professional_stx_bridges_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_professional_stx_20230523",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000009_6925_-NONE-_-NONE-/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "PROJECT VI DPW STX(001): THE PROJECT CONSISTS OF THE INSTALLATION OF TEMPORARY BRIDGES AND STRUCTURAL REPAIRS. THE WORK INCLUDES EMBANKMENT CONSTRUCTION, AGGREGATE BASE, STRUCTURAL REPAIRS, APPROACH WORK, RIPRAP PLACEMENT, GUARDRAIL INSTALLATION,",
        "note": "Opened USASpending Award API: Professional Design/Builders, Inc.; USD 4,765,496.42; date_signed 2023-05-23; PoP Christiansted, VI.",
    },
    {
        "id": "usaspending_professional_stx_20230523",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323C000009_6925_-NONE-_-NONE- (Professional Design/Builders, Inc.; FHWA VI DPW STX temporary bridges). Signed 23 May 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000009_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000009_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 4.77m FHWA award for temporary bridges/structural repairs on St. Croix. Supports fhwa_professional_stx_bridges_2023.",
        "supports": ["fhwa_professional_stx_bridges_2023", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — Bank of China Demerara bridge loan (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "boc_demerara_bridge_loan_160p8m_eur_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Bank of China — facility loan for New Demerara River Bridge",
        "country": "Guyana",
        "asset": "30 Dec 2022: Government of Guyana completes electronic signing of loan agreement with Bank of China for EUR 160.8 million to advance construction of the New Demerara River Bridge (four-lane hybrid, ~2.65 km). Distinct from crcc_demerara_bridge_2022 (USD 260m CRCC JV EPC award) — this row is the Bank of China financing instrument. DPI 9 May 2024 tables a 29 Dec 2023 Supplemental Agreement restating the Original Facility at EUR 160.85 million.",
        "investment_type": "financing",
        "value": str(EUR_BOC),
        "currency": "EUR",
        "value_usd": str(USD_BOC),
        "fx_usd": "1.0666",
        "fx_date": "2022-12-30",
        "year": "2022",
        "status": "active",
        "lat": "6.8045",
        "lon": "-58.1551",
        "geo_note": "Demerara River crossing at Greater Georgetown / west bank corridor (MoF project geography; same pin family as CRCC EPC row).",
        "evidence": "documented",
        "source_id": "mof_guyana_boc_demerara_20221230",
        "note": "Actor: Bank of China Ltd (PRC state-owned commercial bank) — prc. Official Guyana Ministry of Finance release. FX: Frankfurter/ECB EURUSD 1.0666 on 2022-12-30.",
    },
    {
        "id": "boc_demerara_bridge_loan_160p8m_eur_2022",
        "retrieved": "2026-10-02",
        "source_id": "mof_guyana_boc_demerara_20221230",
        "url": "https://finance.gov.gy/government-signs-loan-agreement-with-bank-of-china-for-advancement-of-construction-of-historic-new-demerara-river-bridge/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Senior Minister in the Office of the President with Responsibility for Finance Dr. Ashni Singh today announced that Government had today completed the electronic signing of the loan agreement with the Bank of China for 160.8 Million Euros for the advancement of the construction of the New Demerara River Bridge.",
        "note": "Opened Guyana MoF primary: Bank of China EUR 160.8m facility for New Demerara River Bridge; CRCC JV named as EPC contractor (separate row).",
    },
    {
        "id": "mof_guyana_boc_demerara_20221230",
        "type": "government",
        "chicago": "Ministry of Finance, Guyana. “Government signs loan agreement with Bank of China for advancement of construction of historic New Demerara River Bridge.” 30 December 2022. https://finance.gov.gy/government-signs-loan-agreement-with-bank-of-china-for-advancement-of-construction-of-historic-new-demerara-river-bridge/.",
        "url": "https://finance.gov.gy/government-signs-loan-agreement-with-bank-of-china-for-advancement-of-construction-of-historic-new-demerara-river-bridge/",
        "annotation": "Official MoF: Bank of China EUR 160.8m loan for New Demerara River Bridge. Supports boc_demerara_bridge_loan_160p8m_eur_2022.",
        "supports": ["boc_demerara_bridge_loan_160p8m_eur_2022", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/rail — USTDA Honduras interoceanic corridor study (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ustda_honduras_interoceanic_rail_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "us",
        "counterpart": "USTDA / ShorelineHudson — Honduras Caribbean–Pacific interoceanic rail/port feasibility study",
        "country": "Honduras",
        "asset": "5 Mar 2026: U.S. Trade and Development Agency signs agreement with Honduras’ National Commission for the Construction of the Interoceanic Railway (CONFI) to fund a feasibility study for an overland Caribbean–Pacific transportation corridor; New Jersey-based Hudson-Arvon LLC d/b/a ShorelineHudson selected to assess Port of San Lorenzo upgrades and an inland intermodal rail terminal to relieve Port of Cortés congestion, plus standards and U.S.-supplier financing plan. Study grant amount not disclosed on the USTDA release.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "15.504",
        "lon": "-88.025",
        "geo_note": "Port of Cortés / northern Honduras corridor focus (USTDA release geography; approximate port pin).",
        "evidence": "documented",
        "source_id": "ustda_honduras_interoceanic_20260305",
        "note": "Actor: USTDA (U.S. government) + ShorelineHudson (U.S.) — us. Official USTDA release. CapEx not disclosed — feasibility study only.",
    },
    {
        "id": "ustda_honduras_interoceanic_rail_2026",
        "retrieved": "2026-10-02",
        "source_id": "ustda_honduras_interoceanic_20260305",
        "url": "https://ustda.gov/ustda-hosts-honduran-president-signs-agreement-to-diversify-u-s-supply-chain-routes-in-the-western-hemisphere/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Under the agreement, USTDA will fund a feasibility study to support new port and rail infrastructure that will also protect America’s access to vital trade routes. … CONFI selected New Jersey-based Hudson-Arvon, LLC d/b/a ShorelineHudson to carry out the study.",
        "note": "Opened USTDA primary: feasibility study for Honduras interoceanic rail/port corridor; ShorelineHudson named; grant amount not printed.",
    },
    {
        "id": "ustda_honduras_interoceanic_20260305",
        "type": "government",
        "chicago": "U.S. Trade and Development Agency. “USTDA Hosts Honduran President, Signs Agreement to Diversify U.S. Supply Chain Routes in the Western Hemisphere.” 5 March 2026. https://ustda.gov/ustda-hosts-honduran-president-signs-agreement-to-diversify-u-s-supply-chain-routes-in-the-western-hemisphere/.",
        "url": "https://ustda.gov/ustda-hosts-honduran-president-signs-agreement-to-diversify-u-s-supply-chain-routes-in-the-western-hemisphere/",
        "annotation": "Official USTDA: feasibility study for Honduras Caribbean–Pacific rail/port corridor with ShorelineHudson. Supports ustda_honduras_interoceanic_rail_2026.",
        "supports": ["ustda_honduras_interoceanic_rail_2026", "hunt_latam_rail_telecom"],
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
        "hunt_res_lithium": "Cycle 98: equal budget; Ganfeng LAR/Lithea / Yahua Bandeira / Rio Tinto Rincón dense (miss).",
        "hunt_res_nickel": "Cycle 98: equal budget; MMG Anglo / BRN DFC / Westwin / BNDES dense (miss). Thin dry — shift.",
        "hunt_br_power_equip": "Cycle 98: equal budget; GE Vernova / ENGIE Peru / EXIM GTE / PowerChina DBIS dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 98: logged ustda_honduras_interoceanic_rail_2026 (U.S. USTDA feasibility).",
        "hunt_res_balsa": "Cycle 98: equal budget; Plantabal / EIA wind-blade chain dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 98: equal budget; CONUAR×Terra / CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_res_graphite": "Cycle 98: equal budget; Graphcoa Jordânia / Atlas Malacacheta dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 98: logged fhwa_lpc_pr144_ciales_2024 + fhwa_obratec_barranquitas_2024 + fhwa_lpc_utuado_46slides_2023 + fhwa_novel_ciales_multi_2023 + fhwa_professional_stx_bridges_2023 (U.S. FHWA) + boc_demerara_bridge_loan_160p8m_eur_2022 (PRC Bank of China).",
        "hunt_res_water": "Cycle 98: equal budget; CCCC El Curval / Acciona Cagepa / Sacyr Coquimbo dense (miss).",
        "hunt_fenb_araxa": "Cycle 98: equal budget; CMOC/CBMM/St George dense (miss). Thin spare dry.",
        "hunt_infra_engineering_epc": "Cycle 98: equal budget; Halliburton / Bechtel / Fluor dense (miss).",
        "hunt_energy_other_renewables": "Cycle 98: equal budget; Sungrow Observatorio / Trina Alma Sur dense (miss).",
        "hunt_energy_wind": "Cycle 98: equal budget; Goldwind Sento Sé / Vestas Esquina / Envision dense (miss).",
        "hunt_infra_port_cranes": "Cycle 98: equal budget; ZPMC / Konecranes dense (miss).",
        "hunt_energy_solar": "Cycle 98: equal budget; CCCC ENESOLAR / SUMEC / First Solar dense (miss).",
        "hunt_infra_building_materials": "Cycle 98: equal budget; Sinoma Cibao / Cruz Azul dense (miss). Thin spare dry.",
        "hunt_infra_port_ownership": "Cycle 98: equal budget; COSCO Chancay / Hutchison / CMP dense (miss).",
        "hunt_res_copper": "Cycle 98: equal budget; CMOC Cangrejos / Chinalco / Jiangxi SolGold dense (miss).",
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
    print("Cycle 98 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
