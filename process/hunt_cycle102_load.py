#!/usr/bin/env python3
"""Cycle 102 hunt: shuffle_seed=20261102; equal budget; U.S./PRC split; thin after.

Order: power_plants_grid, wind, other_renewables, balsa, nickel, building_materials,
solar, lithium, copper, fission_smr, bridges_roads, graphite, port_ownership,
niobium, port_cranes, engineering_epc, water, rail.
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
# infrastructure/engineering_epc — AtkinsRéalis El Yunque inspection 2022 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atkinsrealis_fhwa_yunque_inspect_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "AtkinsRéalis USA Inc — FHWA construction inspection task order (El Yunque ERFO)",
        "country": "Puerto Rico",
        "asset": "17 Mar 2022: FHWA awards task order 693C7322F000046 under IDIQ to AtkinsRéalis USA Inc for Level II construction inspector services on Project PR ERFO FS 2017-1(3) (El Yunque forest-road Emergency Relief); obligated USD 4,119,272.04; place of performance Río Grande. Distinct from AtkinsRéalis 2023 dual signs-package inspection task order.",
        "investment_type": "epc",
        "value": "4119272.04",
        "currency": "USD",
        "value_usd": "4119272.04",
        "fx_usd": "1",
        "fx_date": "2022-03-17",
        "year": "2022",
        "status": "active",
        "lat": "18.380",
        "lon": "-65.831",
        "geo_note": "Río Grande Municipality near El Yunque, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_atkinsrealis_yunque_20220317",
        "note": "Actor: AtkinsRéalis USA Inc (Canadian HQ) — allied. Official USASpending Award API.",
    },
    {
        "id": "atkinsrealis_fhwa_yunque_inspect_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_atkinsrealis_yunque_20220317",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322F000046_6925_693C7322D000002_6925/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "NEW INSPECTION SERVICES TASK ORDER PR ERFO FS 2017-1(3) CONSTRUCTION INSPECTOR, LEVEL II",
        "note": "Opened USASpending Award API: AtkinsRéalis USA; USD 4,119,272.04; date_signed 2022-03-17; PoP Río Grande, PR.",
    },
    {
        "id": "usaspending_atkinsrealis_yunque_20220317",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7322F000046_6925_693C7322D000002_6925 (AtkinsRéalis USA Inc; FHWA El Yunque ERFO inspection). Signed 17 March 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322F000046_6925_693C7322D000002_6925/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322F000046_6925_693C7322D000002_6925/",
        "annotation": "USASpending primary: USD 4.12m FHWA inspection task order to AtkinsRéalis for El Yunque ERFO. Supports atkinsrealis_fhwa_yunque_inspect_2022.",
        "supports": ["atkinsrealis_fhwa_yunque_inspect_2022", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — AtkinsRéalis PR ER RPR(12) 2024 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atkinsrealis_fhwa_pr12_inspect_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "AtkinsRéalis USA Inc — FHWA construction inspection task order PR ER RPR(12)",
        "country": "Puerto Rico",
        "asset": "20 Feb 2024: FHWA awards task order 693C7324F00042N to AtkinsRéalis USA Inc for construction inspection services on Project PR ER PRMNT RPR(12); obligated USD 2,784,506.22; place of performance Corozal. Distinct from 2022 El Yunque and 2023 dual signs-package inspection awards.",
        "investment_type": "epc",
        "value": "2784506.22",
        "currency": "USD",
        "value_usd": "2784506.22",
        "fx_usd": "1",
        "fx_date": "2024-02-20",
        "year": "2024",
        "status": "active",
        "lat": "18.341",
        "lon": "-66.317",
        "geo_note": "Corozal Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_atkinsrealis_pr12_20240220",
        "note": "Actor: AtkinsRéalis USA Inc (Canadian HQ) — allied. Official USASpending Award API.",
    },
    {
        "id": "atkinsrealis_fhwa_pr12_inspect_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_atkinsrealis_pr12_20240220",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324F00042N_6925_693C7322D000002_6925/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "NEW CONSTRUCTION INSPECTION SERVICES TASK ORDER FOR PROJECT PR ER PRMNT RPR (12).",
        "note": "Opened USASpending Award API: AtkinsRéalis USA; USD 2,784,506.22; date_signed 2024-02-20; PoP Corozal, PR.",
    },
    {
        "id": "usaspending_atkinsrealis_pr12_20240220",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7324F00042N_6925_693C7322D000002_6925 (AtkinsRéalis USA Inc; FHWA PR ER RPR(12) inspection). Signed 20 February 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324F00042N_6925_693C7322D000002_6925/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324F00042N_6925_693C7322D000002_6925/",
        "annotation": "USASpending primary: USD 2.78m FHWA inspection task order to AtkinsRéalis for PR ER RPR(12). Supports atkinsrealis_fhwa_pr12_inspect_2024.",
        "supports": ["atkinsrealis_fhwa_pr12_inspect_2024", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Jacobs Project Management PR RPR(25) 2026 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "jacobs_fhwa_pr25_inspect_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Jacobs Project Management Co — FHWA construction inspection task order PR ER DOT PRMNT RPR(25)",
        "country": "Puerto Rico",
        "asset": "9 Jul 2026: FHWA awards task order 693C7326F00079N under IDIQ to Jacobs Project Management Co for construction inspection (CI-LV II and Project Office Engineer) on Project PR ER DOT PRMNT RPR(25) (PRHTA West Region C1 landslide repairs); obligated USD 2,200,226.00; place of performance Mayagüez. Distinct from AtkinsRéalis and M&J–Cardno inspection task orders.",
        "investment_type": "epc",
        "value": "2200226",
        "currency": "USD",
        "value_usd": "2200226",
        "fx_usd": "1",
        "fx_date": "2026-07-09",
        "year": "2026",
        "status": "active",
        "lat": "18.201",
        "lon": "-67.140",
        "geo_note": "Mayagüez Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_jacobs_pr25_20260709",
        "note": "Actor: Jacobs Project Management Co (U.S. HQ, Arlington VA) — us. Official USASpending Award API.",
    },
    {
        "id": "jacobs_fhwa_pr25_inspect_2026",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jacobs_pr25_20260709",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326F00079N_6925_693C7322D000004_6925/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "THE PURPOSE OF THIS CONTRACT ACTION IS TO PROCURE THE SERVICES OF CONSTRUCTION INSPECTION (CI-LV II AND POE) FOR PROJECT PR ER DOT PRMNT RPR(25)",
        "note": "Opened USASpending Award API: Jacobs Project Management Co; USD 2,200,226.00; date_signed 2026-07-09; PoP Mayagüez, PR.",
    },
    {
        "id": "usaspending_jacobs_pr25_20260709",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7326F00079N_6925_693C7322D000004_6925 (Jacobs Project Management Co; FHWA inspection PR ER DOT PRMNT RPR(25)). Signed 9 July 2026. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326F00079N_6925_693C7322D000004_6925/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326F00079N_6925_693C7322D000004_6925/",
        "annotation": "USASpending primary: USD 2.20m FHWA inspection task order to Jacobs for PR RPR(25) West Region. Supports jacobs_fhwa_pr25_inspect_2026.",
        "supports": ["jacobs_fhwa_pr25_inspect_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — CDB–BNDES RMB 5bn facility 2024 (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cdb_bndes_rmb5bn_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "prc",
        "counterpart": "China Development Bank — RMB 5 billion loan facility to BNDES (Brazil)",
        "country": "Brazil",
        "asset": "Nov 2024 (Xi Jinping Brazil state visit outcomes list): China Development Bank and BNDES sign a RMB 5 billion loan agreement — first BNDES borrowing in renminbi — to deepen China–Brazil development-finance cooperation supporting infrastructure and related sectors. Distinct from 2023 CDB–BNDES USD 500m fully disbursed facility and from chexim_bndes_fund_600m_2025.",
        "investment_type": "financing",
        "value": "5000000000",
        "currency": "CNY",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2024-11-21",
        "year": "2024",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Nationwide Brazil on-lending facility (no single named project site on opened CDB page).",
        "evidence": "documented",
        "source_id": "cdb_bndes_rmb5bn_20241128",
        "note": "Actor: China Development Bank (PRC policy bank) — prc. Official CDB-hosted Belt and Road portal reprint naming RMB 5bn BNDES loan in Xi visit outcomes. CapEx stored as CNY; USD blank (no cited FX on opened page).",
    },
    {
        "id": "cdb_bndes_rmb5bn_2024",
        "retrieved": "2026-10-02",
        "source_id": "cdb_bndes_rmb5bn_20241128",
        "url": "https://www.cdb.com.cn/ep/202411/t20241128_12218.html",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "中国国开行与巴西开发银行日前签署的50亿元人民币贷款协议，纳入了此次习近平主席对巴西国事访问成果文件清单。",
        "note": "Opened CDB page: RMB 5 billion CDB–BNDES loan cited in Xi Brazil visit outcomes list.",
    },
    {
        "id": "cdb_bndes_rmb5bn_20241128",
        "type": "government",
        "chicago": "China Development Bank. “中国一带一路网：携手服务深化中巴战略对接 中国国开行与巴西开发银行合作不断深化.” 28 November 2024. https://www.cdb.com.cn/ep/202411/t20241128_12218.html.",
        "url": "https://www.cdb.com.cn/ep/202411/t20241128_12218.html",
        "annotation": "CDB primary reprint: RMB 5bn CDB–BNDES loan in Xi Brazil visit outcomes. Supports cdb_bndes_rmb5bn_2024.",
        "supports": ["cdb_bndes_rmb5bn_2024", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — M&J Engineering-Cardno PR-10 inspection (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "mj_cardno_fhwa_pr10_inspect_2023",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "M&J Engineering – Cardno, LLC — FHWA construction inspection on LPC PR-10 Utuado award",
        "country": "Puerto Rico",
        "asset": "7 Feb 2023: FHWA awards task order 693C7323F00027N to M&J Engineering – Cardno, LLC for Level II, Level III, and Project Office Engineer construction inspection services on Project PR ER PRMNT RPR(10) under construction contract 693C7322C000008 (LPC PR-10 Utuado); obligated USD 3,321,199.12; place of performance Ángeles. Cardno lineage now under Stantec (Canada) — allied. Distinct from AtkinsRéalis inspection task orders.",
        "investment_type": "epc",
        "value": "3321199.12",
        "currency": "USD",
        "value_usd": "3321199.12",
        "fx_usd": "1",
        "fx_date": "2023-02-07",
        "year": "2023",
        "status": "active",
        "lat": "18.292",
        "lon": "-66.799",
        "geo_note": "Ángeles barrio, Utuado Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_mj_cardno_pr10_20230207",
        "note": "Actor: M&J Engineering – Cardno, LLC (Cardno/Stantec allied lineage) — allied. Official USASpending Award API.",
    },
    {
        "id": "mj_cardno_fhwa_pr10_inspect_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_mj_cardno_pr10_20230207",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323F00027N_6925_693C7322D000008_6925/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "NEW TASK ORDER FOR CONSTRUCTION INSPECTION SERVICES. THIS ACTION WILL ACQUIRE THE SERVICES OF A LEVEL II,  LEVEL III AND POE FOR PROJECT PR ER PRMNT RPR(10) UNDER CONTRACT 693C7322C000008.",
        "note": "Opened USASpending Award API: M&J Engineering–Cardno; USD 3,321,199.12; date_signed 2023-02-07; PoP Ángeles, PR.",
    },
    {
        "id": "usaspending_mj_cardno_pr10_20230207",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323F00027N_6925_693C7322D000008_6925 (M&J Engineering – Cardno, LLC; FHWA inspection PR ER RPR(10)). Signed 7 February 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323F00027N_6925_693C7322D000008_6925/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323F00027N_6925_693C7322D000008_6925/",
        "annotation": "USASpending primary: USD 3.32m FHWA inspection task order to M&J–Cardno for PR-10 Utuado package. Supports mj_cardno_fhwa_pr10_inspect_2023.",
        "supports": ["mj_cardno_fhwa_pr10_inspect_2023", "hunt_infra_engineering_epc"],
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
        "hunt_br_power_equip": "Cycle 102: equal budget; State Grid NE UHV / Mantiqueira / Aneel RAP already logged or excluded (miss).",
        "hunt_energy_wind": "Cycle 102: equal budget; Envision / Goldwind / Vestas dense (miss).",
        "hunt_energy_other_renewables": "Cycle 102: equal budget; BYD / Sungrow dense (miss).",
        "hunt_res_balsa": "Cycle 102: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_res_nickel": "Cycle 102: equal budget; MMG / BRN / Jervois dense (miss). Thin dry — shift.",
        "hunt_infra_building_materials": "Cycle 102: equal budget; Sinoma dense (miss). Thin spare dry.",
        "hunt_energy_solar": "Cycle 102: equal budget; EXIM Olanchito / First Solar dense (miss).",
        "hunt_res_lithium": "Cycle 102: equal budget; Ganfeng PPG / Zijin 3Q dense (miss).",
        "hunt_res_copper": "Cycle 102: equal budget; CMOC / Chinalco dense (miss).",
        "hunt_energy_fission_smr": "Cycle 102: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_infra_bridges_roads": "Cycle 102: equal budget; FHWA construction backlog ≥USD 2.5m exhausted (miss).",
        "hunt_res_graphite": "Cycle 102: equal budget; Graphcoa / Atlas dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 102: equal budget; APM / Hutchison dense (miss).",
        "hunt_fenb_araxa": "Cycle 102: equal budget; CBMM CapEx / CMOC Catalão dense (miss).",
        "hunt_infra_port_cranes": "Cycle 102: equal budget; ZPMC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 102: logged jacobs_fhwa_pr25_inspect_2026 (us) + cdb_bndes_rmb5bn_2024 (prc) + atkinsrealis_fhwa_yunque_inspect_2022 + atkinsrealis_fhwa_pr12_inspect_2024 + mj_cardno_fhwa_pr10_inspect_2023 (allied inspection).",
        "hunt_res_water": "Cycle 102: equal budget; CCCC El Curval / Acciona dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 102: equal budget; USTDA Honduras / CRCC dense (miss).",
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
    print("Cycle 102 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
