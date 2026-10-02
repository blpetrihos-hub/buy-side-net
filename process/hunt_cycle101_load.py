#!/usr/bin/env python3
"""Cycle 101 hunt: shuffle_seed=20261101; equal budget; U.S./PRC split; thin after.

Order: lithium, other_renewables, fission_smr, copper, nickel, niobium,
port_cranes, engineering_epc, building_materials, power_plants_grid, graphite,
wind, solar, balsa, port_ownership, water, bridges_roads, rail.
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
# resources/lithium — Ganfeng Pozuelos–Pastos Grandes +$200m development (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ganfeng_pozuelos_dev_200m_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Ganfeng Lithium — Pozuelos–Pastos Grandes post-acquisition development spend",
        "country": "Argentina",
        "asset": "12 Aug 2025 Lithium Argentina SEC Exhibit 99.1: after acquiring Pozuelos–Pastos Grandes from Pluspetrol for USD 1.0 billion in 2022, Ganfeng has since invested an additional USD 200 million to advance development — infrastructure, production wellfield, and >2,000-person construction camp. Distinct from ganfeng_lithea_ppg_2022 acquisition envelope and ganfeng_lar_debt_130m_2026 facility.",
        "investment_type": "other",
        "value": "200000000",
        "currency": "USD",
        "value_usd": "200000000",
        "fx_usd": "1",
        "fx_date": "2025-08-12",
        "year": "2025",
        "status": "active",
        "lat": "-24.55",
        "lon": "-66.75",
        "geo_note": "Pozuelos–Pastos Grandes basin, Salta Province (Lithium Argentina / Ganfeng project geography; approximate).",
        "evidence": "documented",
        "source_id": "lar_edgar_ex991_ppg_jv_20250812",
        "note": "Actor: Ganfeng Lithium Group (PRC) — prc. Official Lithium Argentina SEC Exhibit 99.1 disclosing Ganfeng additional USD 200m development spend.",
    },
    {
        "id": "ganfeng_pozuelos_dev_200m_2025",
        "retrieved": "2026-10-02",
        "source_id": "lar_edgar_ex991_ppg_jv_20250812",
        "url": "https://www.sec.gov/Archives/edgar/data/1440972/000106299325015465/exhibit99-1.htm",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Ganfeng acquired the Pozuelos-Pastos Grandes project in 2022 from Pluspetrol Resources for $1.0 billion and has since invested an additional $200 million to advance development, including infrastructure, a production wellfield and an over 2,000-person construction camp.",
        "note": "Opened LAR SEC EX-99.1: Ganfeng post-acquisition USD 200m PPG development spend disclosed.",
    },
    {
        "id": "lar_edgar_ex991_ppg_jv_20250812",
        "type": "company",
        "chicago": "Lithium Argentina AG. “Lithium Argentina and Ganfeng to Form New Joint Venture to Consolidate the Pozuelos and Pastos Grandes Basins.” Exhibit 99.1 to Form 6-K. 12 August 2025. https://www.sec.gov/Archives/edgar/data/1440972/000106299325015465/exhibit99-1.htm.",
        "url": "https://www.sec.gov/Archives/edgar/data/1440972/000106299325015465/exhibit99-1.htm",
        "annotation": "LAR SEC primary: Ganfeng +USD 200m PPG development; also PPG New JV framework (67/33). Supports ganfeng_pozuelos_dev_200m_2025 and ganfeng_ppg_jv_framework_2025.",
        "supports": [
            "ganfeng_pozuelos_dev_200m_2025",
            "ganfeng_ppg_jv_framework_2025",
            "hunt_res_lithium",
        ],
    },
)

# ---------------------------------------------------------------------------
# resources/lithium — Ganfeng 67% PPG New JV framework (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ganfeng_ppg_jv_framework_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Ganfeng Lithium — PPG New JV framework (67% / Lithium Argentina 33%)",
        "country": "Argentina",
        "asset": "12 Aug 2025: Lithium Argentina and Ganfeng execute Framework Agreement to form New JV consolidating Ganfeng’s Pozuelos–Pastos Grandes with Lithium Argentina’s Pastos Grandes (85%) and Sal de la Puna (65%); upon closing Ganfeng 67% / Lithium Argentina 33%; targets up to 150,000 tpa LCE in three 50,000 tpa phases; New JV expected to close by Q1 2026 subject to definitive agreements and approvals. Distinct from ganfeng_pastos_grandes_stake_2024 14.9% PGCo equity and Stage 1 CAPEX scoping row.",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-24.55",
        "lon": "-66.75",
        "geo_note": "Pozuelos–Pastos Grandes / Sal de la Puna consolidated PPG footprint, Salta (framework geography; approximate).",
        "evidence": "documented",
        "source_id": "lar_edgar_ex991_ppg_jv_20250812",
        "note": "Actor: Ganfeng Lithium (PRC) majority partner under Framework Agreement — prc. Closing pending; ownership share disclosed; CapEx blank until definitive close/FS.",
    },
    {
        "id": "ganfeng_ppg_jv_framework_2025",
        "retrieved": "2026-10-02",
        "source_id": "lar_edgar_ex991_ppg_jv_20250812",
        "url": "https://www.sec.gov/Archives/edgar/data/1440972/000106299325015465/exhibit99-1.htm",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Upon closing, Ganfeng will hold 67% and Lithium Argentina 33% of PPG, with ownership based on resources, capital contributions and technology inputs. … The New JV is expected to close by Q1 2026.",
        "note": "Opened LAR SEC EX-99.1: Framework Agreement for Ganfeng 67% PPG New JV; close targeted Q1 2026.",
    },
    {
        "id": "lar_edgar_ex991_ppg_jv_20250812",
        "type": "company",
        "chicago": "Lithium Argentina AG. “Lithium Argentina and Ganfeng to Form New Joint Venture to Consolidate the Pozuelos and Pastos Grandes Basins.” Exhibit 99.1 to Form 6-K. 12 August 2025. https://www.sec.gov/Archives/edgar/data/1440972/000106299325015465/exhibit99-1.htm.",
        "url": "https://www.sec.gov/Archives/edgar/data/1440972/000106299325015465/exhibit99-1.htm",
        "annotation": "LAR SEC primary: Ganfeng +USD 200m PPG development; also PPG New JV framework (67/33). Supports ganfeng_pozuelos_dev_200m_2025 and ganfeng_ppg_jv_framework_2025.",
        "supports": [
            "ganfeng_pozuelos_dev_200m_2025",
            "ganfeng_ppg_jv_framework_2025",
            "hunt_res_lithium",
        ],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA JPI Añasco 2023 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_jpi_anasco_2023",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "JPI Construction LLC — FHWA Emergency Relief landslide roadway repairs (Añasco)",
        "country": "Puerto Rico",
        "asset": "27 Jun 2023: FHWA awards firm-fixed-price contract 693C7323C000011 to JPI Construction LLC for Project PR ER DOT PRMNT RPR(20) — repairing roadways damaged by landslides from Hurricanes Irma and Maria in Municipality of Añasco; obligated USD 3,258,365.49. Distinct from JPI Maunabo 2023 and JPI Naguabo 2021 awards.",
        "investment_type": "epc",
        "value": "3258365.49",
        "currency": "USD",
        "value_usd": "3258365.49",
        "fx_usd": "1",
        "fx_date": "2023-06-27",
        "year": "2023",
        "status": "active",
        "lat": "18.283",
        "lon": "-67.140",
        "geo_note": "Añasco Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_jpi_anasco_20230627",
        "note": "Actor: JPI Construction LLC (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_jpi_anasco_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jpi_anasco_20230627",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000011_6925_-NONE-_-NONE-/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "PR ER DOT PRMNT RPR(20) THE PROJECT CONSISTS OF REPAIRING ROADWAYS DAMAGED BY LANDSLIDES DURING HURRICANES IRMA AND MARIA IN THE MUNICIPALITY OF ANASCO, PUERTO RICO.",
        "note": "Opened USASpending Award API: JPI; USD 3,258,365.49; date_signed 2023-06-27; PoP Añasco, PR.",
    },
    {
        "id": "usaspending_jpi_anasco_20230627",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323C000011_6925_-NONE-_-NONE- (JPI Construction LLC; FHWA Emergency Relief Añasco). Signed 27 June 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000011_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000011_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 3.26m FHWA award to JPI for Añasco landslide roadway repairs. Supports fhwa_jpi_anasco_2023.",
        "supports": ["fhwa_jpi_anasco_2023", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA JPI Naguabo 2021 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_jpi_naguabo_2021",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "JPI Construction LLC — FHWA Emergency Relief PR-3/PR-1/PR-909 landslide repairs (Naguabo)",
        "country": "Puerto Rico",
        "asset": "28 Jul 2021: FHWA awards firm-fixed-price contract 693C7321C000019 to JPI Construction LLC for Project PR ER PRMNT RPR(8) — repairing landslide and washout damage on PR-3 km 69.3–70.6, PR-1 km 61.8, and PR-909 km 5.55 (gabion basket wall and related works); obligated USD 2,886,025.68; place of performance Naguabo. Distinct from JPI Maunabo/Añasco awards.",
        "investment_type": "epc",
        "value": "2886025.68",
        "currency": "USD",
        "value_usd": "2886025.68",
        "fx_usd": "1",
        "fx_date": "2021-07-28",
        "year": "2021",
        "status": "active",
        "lat": "18.219",
        "lon": "-65.736",
        "geo_note": "Naguabo Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_jpi_naguabo_20210728",
        "note": "Actor: JPI Construction LLC (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_jpi_naguabo_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jpi_naguabo_20210728",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000019_6925_-NONE-_-NONE-/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "PROJECT PR ER PRMNT RPR(8)  THE PROJECT CONSISTS OF REPAIRING LANDSLIDE AND WASHOUT DAMAGED BY HURRICANES IRMA AND MARIA ON PR-3 KM 69.3-70.6, PR-1 KM 61.8 AND PR-909 KM 5.55 AND OTHER MISCELLANEOUS WORK.",
        "note": "Opened USASpending Award API: JPI; USD 2,886,025.68; date_signed 2021-07-28; PoP Naguabo, PR.",
    },
    {
        "id": "usaspending_jpi_naguabo_20210728",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7321C000019_6925_-NONE-_-NONE- (JPI Construction LLC; FHWA Emergency Relief Naguabo PR-3/1/909). Signed 28 July 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000019_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000019_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 2.89m FHWA award to JPI for Naguabo multi-route landslide repairs. Supports fhwa_jpi_naguabo_2021.",
        "supports": ["fhwa_jpi_naguabo_2021", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — AtkinsRealis FHWA construction inspection (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atkinsrealis_fhwa_pr_inspect_2023",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "AtkinsRéalis USA Inc — FHWA construction inspection task order (PR ER signs packages)",
        "country": "Puerto Rico",
        "asset": "17 Mar 2023: FHWA awards task order 693C7323F00040N under IDIQ 693C7322D000002 to AtkinsRéalis USA Inc for Level II & III construction inspectors on Projects PR ER PRMNT RPR(7) and PR ER PRMNT RPR(11) to assist Eastern Federal Lands Highway Division field personnel with onsite inspection; obligated USD 8,518,874.11; place of performance San Juan. AtkinsRéalis HQ Canada — allied. Distinct from construction EPC FHWA awards to local contractors.",
        "investment_type": "epc",
        "value": "8518874.11",
        "currency": "USD",
        "value_usd": "8518874.11",
        "fx_usd": "1",
        "fx_date": "2023-03-17",
        "year": "2023",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "San Juan Municipality, Puerto Rico (USASpending place of performance; multi-project inspection scope).",
        "evidence": "documented",
        "source_id": "usaspending_atkinsrealis_pr_inspect_20230317",
        "note": "Actor: AtkinsRéalis USA Inc (Canadian AtkinsRéalis Group HQ) — allied. Official USASpending Award API.",
    },
    {
        "id": "atkinsrealis_fhwa_pr_inspect_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_atkinsrealis_pr_inspect_20230317",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323F00040N_6925_693C7322D000002_6925/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "NEW TASK ORDER TO PROCURE THE SERVICES OF CONSTRUCTION INSPECTORS ON PROJECTS PR ER PRMNT RPR (7) & PR ER PRMNT RPR(11) LEVEL II & LEVEL III TO ASSIST (EFLHD) FIELD PERSONNEL WITH ONSITE INSPECTION OF WORKS.",
        "note": "Opened USASpending Award API: AtkinsRéalis USA Inc; USD 8,518,874.11; date_signed 2023-03-17; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_atkinsrealis_pr_inspect_20230317",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323F00040N_6925_693C7322D000002_6925 (AtkinsRéalis USA Inc; FHWA construction inspection PR ER RPR(7)/(11)). Signed 17 March 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323F00040N_6925_693C7322D000002_6925/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323F00040N_6925_693C7322D000002_6925/",
        "annotation": "USASpending primary: USD 8.52m FHWA inspection task order to AtkinsRéalis USA. Supports atkinsrealis_fhwa_pr_inspect_2023.",
        "supports": ["atkinsrealis_fhwa_pr_inspect_2023", "hunt_infra_engineering_epc"],
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
        "hunt_res_lithium": "Cycle 101: logged ganfeng_pozuelos_dev_200m_2025 + ganfeng_ppg_jv_framework_2025 (PRC Ganfeng SEC EX-99.1).",
        "hunt_energy_other_renewables": "Cycle 101: equal budget; BYD Elena / Central Oasis / Sungrow dense (miss).",
        "hunt_energy_fission_smr": "Cycle 101: equal budget; CAREM / CNNC / CONUAR dense (miss). Thin spare dry.",
        "hunt_res_copper": "Cycle 101: equal budget; CMOC / Chinalco / Jiangxi dense (miss).",
        "hunt_res_nickel": "Cycle 101: equal budget; MMG / BRN / Jervois dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 101: equal budget; CBMM CapEx 630m / CMOC Catalão dense (miss).",
        "hunt_infra_port_cranes": "Cycle 101: equal budget; ZPMC Chancay / Santos dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 101: logged atkinsrealis_fhwa_pr_inspect_2023 (allied AtkinsRéalis inspection).",
        "hunt_infra_building_materials": "Cycle 101: equal budget; Sinoma dense (miss). Thin spare dry.",
        "hunt_br_power_equip": "Cycle 101: equal budget; GE Vernova / ENGIE / EXIM GTE dense (miss).",
        "hunt_res_graphite": "Cycle 101: equal budget; Graphcoa / Atlas dense (miss). Thin dry — shift.",
        "hunt_energy_wind": "Cycle 101: equal budget; Envision / Goldwind / Vestas dense (miss).",
        "hunt_energy_solar": "Cycle 101: equal budget; EXIM Olanchito / First Solar dense (miss).",
        "hunt_res_balsa": "Cycle 101: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 101: equal budget; APM / Hutchison / DP World dense (miss).",
        "hunt_res_water": "Cycle 101: equal budget; CCCC El Curval / Acciona dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 101: logged fhwa_jpi_anasco_2023 + fhwa_jpi_naguabo_2021 (U.S. FHWA).",
        "hunt_latam_rail_telecom": "Cycle 101: equal budget; USTDA Honduras / CRCC / PowerChina dense (miss).",
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
    print("Cycle 101 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
