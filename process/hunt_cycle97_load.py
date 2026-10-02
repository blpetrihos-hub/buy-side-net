#!/usr/bin/env python3
"""Cycle 97 hunt: shuffle_seed=20261097; equal budget; U.S./PRC split; thin after.

Order (BRIEF numeric list): wind, lithium, solar, fission_smr, niobium,
port_cranes, copper, building_materials, graphite, rail, balsa,
port_ownership, nickel, water, other_renewables, bridges_roads,
engineering_epc, power_plants_grid.
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
# infrastructure/bridges_roads — FHWA Maglez PR ER (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_maglez_pr108_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Maglez Engineerings & Contractors Corp — FHWA Emergency Relief PR-108/120/124/339 landslide repairs",
        "country": "Puerto Rico",
        "asset": "25 Jul 2025: U.S. DOT Federal Highway Administration awards firm-fixed-price contract 693C7325C000015 to Maglez Engineerings & Contractors Corp (Florida, PR HQ; U.S.-owned small business) for Project PR ER DOT PRMNT RPR(25) — repairing landslides and washouts from Hurricanes Irma and Maria on PR-108 km 16.9, PR-120 km 27.5, PR-124 km 2.4, and PR-339 km 1.7–1.8; obligated amount USD 20,160,481 after option exercise; place of performance San Sebastián; end date 10 Dec 2029. Distinct from Novel PR-155 and DDD-DVG Canóvanas FHWA rows.",
        "investment_type": "epc",
        "value": "20160481",
        "currency": "USD",
        "value_usd": "20160481",
        "fx_usd": "1",
        "fx_date": "2025-07-25",
        "year": "2025",
        "status": "active",
        "lat": "18.337",
        "lon": "-66.990",
        "geo_note": "San Sebastián Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_maglez_pr108_20250725",
        "note": "Actor: Maglez Engineerings & Contractors Corp (Puerto Rico / U.S.) + FHWA U.S. government Emergency Relief — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_maglez_pr108_2025",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_maglez_pr108_20250725",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7325C000015_6925_-NONE-_-NONE-/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(25)  THE PROJECT CONSISTS OF REPAIRING LANDSLIDES AND WASHOUTS DAMAGES CAUSED BY HURRICANES IRMA AND MARIA ON PR-108, KM. 16.9 (HWY-21), PR-120, KM. 27.5 (HWY-80), PR-124, KM. 2.4 (HWY-105), PR-339, KM. 1.7-1.8 (HWY-347)",
        "note": "Opened USASpending Award API: Maglez Engineerings & Contractors Corp; USD 20,160,481; date_signed 2025-07-25; awarding agency DOT/FHWA; PoP San Sebastián, PR.",
    },
    {
        "id": "usaspending_maglez_pr108_20250725",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7325C000015_6925_-NONE-_-NONE- (Maglez Engineerings & Contractors Corp; FHWA Emergency Relief PR-108/120/124/339). Signed 25 July 2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7325C000015_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7325C000015_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 20.16m FHWA award to Maglez for PR landslide/washout repairs. Supports fhwa_maglez_pr108_2025.",
        "supports": ["fhwa_maglez_pr108_2025", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA LPC Adjuntas (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_lpc_pr1_pr10_adjuntas_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "LPC Contractors Inc — FHWA Emergency Relief PR-1/PR-10 landslide repairs (Adjuntas)",
        "country": "Puerto Rico",
        "asset": "23 Jun 2026: FHWA awards firm-fixed-price contract 693C7326C000014 to LPC Contractors Inc (U.S.-owned) for Project PR ER DOT PRMNT RPR(23) — repairing landslides and washouts from Hurricanes Irma and Maria on PR-1 km 111.6–111.8 and km 24.8 and PR-10 km 52.3 and km 30.3–30.4; obligated USD 10,752,200; place of performance Adjuntas. Distinct from Maglez / Novel / DDD-DVG FHWA rows.",
        "investment_type": "epc",
        "value": "10752200",
        "currency": "USD",
        "value_usd": "10752200",
        "fx_usd": "1",
        "fx_date": "2026-06-23",
        "year": "2026",
        "status": "active",
        "lat": "18.163",
        "lon": "-66.722",
        "geo_note": "Adjuntas Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_lpc_adjuntas_20260623",
        "note": "Actor: LPC Contractors Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_lpc_pr1_pr10_adjuntas_2026",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_lpc_adjuntas_20260623",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000014_6925_-NONE-_-NONE-/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(23):  THE PROJECT CONSISTS OF REPAIRING LANDSLIDES AND WASHOUTS DAMAGES CAUSED BY HURRICANES IRMA AND MARIA ON PR-1 KM. 111.6 - 111.8 (HWY-3), PR-1 KM. 24.8 (HWY-4), PR-10 KM. 52.3 (HWY-11), PR-10, KM. 30.3-30.4 (HWY-12)",
        "note": "Opened USASpending Award API: LPC Contractors Inc; USD 10,752,200; date_signed 2026-06-23; PoP Adjuntas, PR.",
    },
    {
        "id": "usaspending_lpc_adjuntas_20260623",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7326C000014_6925_-NONE-_-NONE- (LPC Contractors Inc; FHWA Emergency Relief PR-1/PR-10 Adjuntas). Signed 23 June 2026. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000014_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000014_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 10.75m FHWA award to LPC for PR-1/PR-10 landslide repairs in Adjuntas. Supports fhwa_lpc_pr1_pr10_adjuntas_2026.",
        "supports": ["fhwa_lpc_pr1_pr10_adjuntas_2026", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Caribbean Sign (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_caribbean_sign_pr_er27_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Caribbean Sign Supplies Manufacturers, Inc. — FHWA Emergency Relief signs/guardrails (Metro/North/South)",
        "country": "Puerto Rico",
        "asset": "27 Feb 2026: FHWA awards firm-fixed-price contract 693C7326C000007 to Caribbean Sign Supplies Manufacturers, Inc. (U.S.-owned HUBZone/woman-owned small business) for Project PR ER DOT PRMNT RPR(27) — repairing signs, guardrails, and miscellaneous hurricane damages in Metro, North, and South regions; obligated USD 14,969,047; place of performance Aibonito. Distinct from Maglez/LPC landslide awards.",
        "investment_type": "epc",
        "value": "14969047",
        "currency": "USD",
        "value_usd": "14969047",
        "fx_usd": "1",
        "fx_date": "2026-02-27",
        "year": "2026",
        "status": "active",
        "lat": "18.140",
        "lon": "-66.266",
        "geo_note": "Aibonito Municipality, Puerto Rico (USASpending place of performance; multi-region Metro/North/South scope).",
        "evidence": "documented",
        "source_id": "usaspending_caribbean_sign_20260227",
        "note": "Actor: Caribbean Sign Supplies Manufacturers, Inc. (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_caribbean_sign_pr_er27_2026",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caribbean_sign_20260227",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000007_6925_-NONE-_-NONE-/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(27) THE PROJECT CONSISTS OF REPAIRING SIGNS, GUARDRAILS, AND OTHER MISCELLANEOUS DAMAGES CAUSED BY HURRICANES IRMA AND MARIA IN THE METRO, NORTH, AND SOUTH REGIONS. THE WORK INCLUDES TRAFFIC SIGN ASSEMBLIES (SMALL SIGNS,",
        "note": "Opened USASpending Award API: Caribbean Sign Supplies Manufacturers, Inc.; USD 14,969,047; date_signed 2026-02-27; PoP Aibonito, PR.",
    },
    {
        "id": "usaspending_caribbean_sign_20260227",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7326C000007_6925_-NONE-_-NONE- (Caribbean Sign Supplies Manufacturers, Inc.; FHWA Emergency Relief signs/guardrails). Signed 27 February 2026. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000007_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000007_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 14.97m FHWA award for PR Metro/North/South signs and guardrails. Supports fhwa_caribbean_sign_pr_er27_2026.",
        "supports": ["fhwa_caribbean_sign_pr_er27_2026", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA JC & Associates West Region (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_jc_associates_pr_er16_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "JC & Associates Property Management Group Inc — FHWA Emergency Relief signs/guardrails (West Region)",
        "country": "Puerto Rico",
        "asset": "22 Jan 2026: FHWA awards firm-fixed-price contract 693C7326C000003 to JC & Associates Property Management Group Inc (U.S.-owned small business) for Project PR ER DOT PRMNT RPR(16) — repairing signs, guardrails, and miscellaneous hurricane damages in the West Region; obligated USD 13,296,665; place of performance Añasco. Distinct from Caribbean Sign Metro/North/South award.",
        "investment_type": "epc",
        "value": "13296665",
        "currency": "USD",
        "value_usd": "13296665",
        "fx_usd": "1",
        "fx_date": "2026-01-22",
        "year": "2026",
        "status": "active",
        "lat": "18.283",
        "lon": "-67.140",
        "geo_note": "Añasco Municipality, Puerto Rico (USASpending place of performance; West Region scope).",
        "evidence": "documented",
        "source_id": "usaspending_jc_associates_20260122",
        "note": "Actor: JC & Associates Property Management Group Inc (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_jc_associates_pr_er16_2026",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jc_associates_20260122",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000003_6925_-NONE-_-NONE-/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "PR ER DOT PRMNT RPR(16)  THE PROJECT CONSISTS OF REPAIRING SIGNS, GUARDRAILS, AND OTHER MISCELLANEOUS DAMAGES CAUSED BY HURRICANES IRMA AND MARIA IN THE WEST REGION. THE WORK INCLUDES TRAFFIC SIGN ASSEMBLIES (SMALL SIGNS, GROUND MOUNTED, OVERHEAD),",
        "note": "Opened USASpending Award API: JC & Associates; USD 13,296,665; date_signed 2026-01-22; PoP Añasco, PR.",
    },
    {
        "id": "usaspending_jc_associates_20260122",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7326C000003_6925_-NONE-_-NONE- (JC & Associates Property Management Group Inc; FHWA Emergency Relief West Region signs/guardrails). Signed 22 January 2026. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000003_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000003_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 13.30m FHWA award for PR West Region signs and guardrails. Supports fhwa_jc_associates_pr_er16_2026.",
        "supports": ["fhwa_jc_associates_pr_er16_2026", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — CHEXIM Guyana East Coast Phase II loan (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "chexim_guyana_east_coast_192m_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Export-Import Bank of China — Framework Concessional Loan for East Coast Demerara Road Phase II",
        "country": "Guyana",
        "asset": "30 Dec 2022: Guyana Finance Minister Ashni Singh and PRC Ambassador Guo Haiyan sign Framework Concessional Loan Agreement for USD 192 million from Exim Bank of China to finance Phase II East Coast Road — four-lane Railway Embankment Sheriff Street–Orange Nassau, new Enmore–Mahaica carriageway, Belfield–Orange Nassau rehab, ~48 bridges + 22 culverts and Hope Canal bridge. Distinct from crfg_guyana_east_coast_184m_2022 (CRFG EPC award proxy) — this row is the CHEXIM financing instrument documented on DPI.",
        "investment_type": "financing",
        "value": "192000000",
        "currency": "USD",
        "value_usd": "192000000",
        "fx_usd": "1",
        "fx_date": "2022-12-30",
        "year": "2022",
        "status": "active",
        "lat": "6.80",
        "lon": "-58.05",
        "geo_note": "East Coast Demerara corridor / Sheriff Street–Mahaica (DPI project geography; approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "dpi_guyana_chexim_ecd_192m_20221230",
        "note": "Actor: Export-Import Bank of China (PRC state lender) — prc. Official Guyana DPI release naming CHEXIM concessional loan USD 192m. Complements CRFG EPC presence row.",
    },
    {
        "id": "chexim_guyana_east_coast_192m_2022",
        "retrieved": "2026-10-02",
        "source_id": "dpi_guyana_chexim_ecd_192m_20221230",
        "url": "https://dpi.gov.gy/us192-million-phase-2-east-coast-road-project-to-commence-under-governments-expansive-aggressive-transport-infrastructure-initiative/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Senior Finance Minister Dr. Ashni Singh and Her Excellency Guo Haiyan, Ambassador of the People’s Republic of China to Guyana today signed a Framework Concessional Loan Agreement to the tune of US$192 Million to finance Phase II of the East Coast Road Project. … The loan for the project is being provided by the Exim Bank of China.",
        "note": "Opened Guyana DPI primary: CHEXIM Framework Concessional Loan USD 192m for East Coast Phase II; corridor scope named.",
    },
    {
        "id": "dpi_guyana_chexim_ecd_192m_20221230",
        "type": "government",
        "chicago": "Department of Public Information, Guyana. “US$192 Million Phase 2 East Coast Road Project to commence under Government’s expansive, aggressive transport infrastructure initiative.” 30 December 2022. https://dpi.gov.gy/us192-million-phase-2-east-coast-road-project-to-commence-under-governments-expansive-aggressive-transport-infrastructure-initiative/.",
        "url": "https://dpi.gov.gy/us192-million-phase-2-east-coast-road-project-to-commence-under-governments-expansive-aggressive-transport-infrastructure-initiative/",
        "annotation": "Official DPI: CHEXIM USD 192m Framework Concessional Loan for East Coast Demerara Phase II. Supports chexim_guyana_east_coast_192m_2022.",
        "supports": ["chexim_guyana_east_coast_192m_2022", "hunt_infra_bridges_roads"],
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
        "hunt_energy_wind": "Cycle 97: equal budget; Goldwind Sento Sé / Vestas Esquina / Envision dense (miss).",
        "hunt_res_lithium": "Cycle 97: equal budget; Yahua Bandeira / Atlas Neves / EnergyX EXIM dense (miss).",
        "hunt_energy_solar": "Cycle 97: equal budget; CCCC ENESOLAR / SUMEC Linden / First Solar dense (miss).",
        "hunt_energy_fission_smr": "Cycle 97: equal budget; CONUAR×Terra / USTDA nuclear tour dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 97: equal budget; CMOC/CBMM/St George dense (miss). Thin spare dry.",
        "hunt_infra_port_cranes": "Cycle 97: equal budget; ZPMC Santos / Konecranes Cartagena–Arica dense (miss).",
        "hunt_res_copper": "Cycle 97: equal budget; CMOC Cangrejos / Chinalco Toromocho ITS-3 / Jiangxi SolGold dense (miss).",
        "hunt_infra_building_materials": "Cycle 97: equal budget; Sinoma Cibao / Cruz Azul / Panam dense (miss). Thin spare dry.",
        "hunt_res_graphite": "Cycle 97: equal budget; Graphcoa Jordânia / Atlas Malacacheta dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 97: equal budget; PowerChina Chancay / CRCC Batuco / CRI TAM-TSB dense (miss).",
        "hunt_res_balsa": "Cycle 97: equal budget; Plantabal / EIA wind-blade chain dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 97: equal budget; COSCO Chancay / Hutchison / CMP Paranaguá dense (miss).",
        "hunt_res_nickel": "Cycle 97: equal budget; MMG Anglo / BRN DFC / BNDES dense (miss). Thin dry — shift.",
        "hunt_res_water": "Cycle 97: equal budget; CCCC El Curval / Sacyr Coquimbo / Acciona Cagepa dense (miss).",
        "hunt_energy_other_renewables": "Cycle 97: equal budget; Sungrow Observatorio / Trina Alma Sur / AES Andes dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 97: logged fhwa_maglez_pr108_2025 + fhwa_lpc_pr1_pr10_adjuntas_2026 + fhwa_caribbean_sign_pr_er27_2026 + fhwa_jc_associates_pr_er16_2026 (U.S. FHWA) + chexim_guyana_east_coast_192m_2022 (PRC CHEXIM).",
        "hunt_infra_engineering_epc": "Cycle 97: equal budget; Halliburton GranMorgu / Bechtel EIMISA / Fluor Toromocho dense (miss).",
        "hunt_br_power_equip": "Cycle 97: equal budget; GE Vernova Azulão / ENGIE Peru Grupo 1 / EXIM GTE dense (miss).",
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
    print("Cycle 97 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
