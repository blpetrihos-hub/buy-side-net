#!/usr/bin/env python3
"""Cycle 47 hunt: shuffle_seed=20261047; equal budget; U.S. side ≥1/3; thin_topup after.

Order: water, lithium, balsa, rail, engineering_epc, copper, power_plants_grid,
port_cranes, nickel, wind, graphite, fission_smr, bridges_roads, other_renewables,
niobium, port_ownership, solar, building_materials.
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
# 1 resources/water — Newmont Yanacocha water-transition investment ~USD 2bn (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "newmont_yanacocha_water_2bn_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Newmont — Yanacocha site-wide water transition / treatment program",
        "country": "Peru",
        "asset": "Hatch 2025 performance note on Newmont Yanacocha (Cajamarca): cumulative ~USD 2 billion invested in water management/transition, including modification of three water treatment plants, 42 km of pipelines, and ~1,500 m³/h plant flow capacity to manage acidic leach-pad flows during mine closure transition. Distinct from acciona_yanacocha_wtp_commission_2026 (ACCIONA commissioning services only).",
        "investment_type": "other",
        "value": "2000000000",
        "currency": "USD",
        "value_usd": "2000000000",
        "fx_usd": "1",
        "fx_date": "2025-03-02",
        "year": "2025",
        "status": "active",
        "lat": "-6.98",
        "lon": "-78.51",
        "geo_note": "Yanacocha mine, Cajamarca Region (site pin).",
        "evidence": "documented",
        "source_id": "hatch_yanacocha_water_2025",
        "note": "Actor: Newmont (U.S.) — us. Cumulative investment figure from Hatch project write-up. Complements ACCIONA commissioning row without duplicating it.",
    },
    {
        "id": "newmont_yanacocha_water_2bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "hatch_yanacocha_water_2025",
        "url": "https://www.hatch.com/en/About-Us/Publications/Performance-Innovations/2025/0302-Yanacocha-Water-Transition-Projects",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "With $2 billion invested, the Yanacocha site now has a proactive water management approach. … We modified three out-of-commission water treatment plants to treat highly acidic water and installed 42 kilometers of pipelines, with plant flow capacities of 1,500 cubic meters per hour.",
        "note": "Opened Hatch Annual Review 2025 Yanacocha water-transition feature.",
    },
    {
        "id": "hatch_yanacocha_water_2025",
        "type": "company",
        "chicago": "Hatch. “Newmont’s Yanacocha Water Transition Projects.” Performance Innovations / Annual Review 2025.",
        "url": "https://www.hatch.com/en/About-Us/Publications/Performance-Innovations/2025/0302-Yanacocha-Water-Transition-Projects",
        "annotation": "EPC partner write-up on Newmont Yanacocha ~USD 2bn water-transition investment. Supports newmont_yanacocha_water_2bn_2025.",
        "supports": ["newmont_yanacocha_water_2bn_2025", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 3 resources/balsa — Plantabal 2025 processor revenue USD 60.76m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "plantabal_ingresos_2025_60p8m",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "Plantabal S.A. (3A Composites) — 2025 reported revenue (Ecuador processor)",
        "country": "Ecuador",
        "asset": "Ecuador company registry aggregate (encuentra.ec / SCVS filing mirror): Plantaciones de Balsa Plantabal S.A. reported 2025 ingresos USD 60.756 million (net result USD 4.572 million; 737 employees). Processor/financial presence for plantation-to-BALTEK wind-blade core supply chain — not a trade-flow or financing duplicate of WITS/AIMA/Plantabal planting rows.",
        "investment_type": "other",
        "value": "60756466",
        "currency": "USD",
        "value_usd": "60756466",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Plantabal Quevedo operations, Los Ríos (processing site pin).",
        "evidence": "documented",
        "source_id": "encuentra_plantabal_2025",
        "note": "Actor: Plantabal / 3A Composites (Switzerland) — allied. Revenue from public company-registry aggregate; not CAPEX.",
    },
    {
        "id": "plantabal_ingresos_2025_60p8m",
        "retrieved": "2026-10-01",
        "source_id": "encuentra_plantabal_2025",
        "url": "https://encuentra.ec/empresa/plantaciones-de-balsa-plantabal-sa-0990533105001/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Ingresos 2025: $ 60,76 millones.",
        "note": "Opened encuentra.ec Plantabal company page (RUC 0990533105001) summarizing SCVS balance filings; table lists 2025 ingresos $60,756,466.",
    },
    {
        "id": "encuentra_plantabal_2025",
        "type": "official",
        "chicago": "encuentra.ec (SCVS filing mirror). “Plantaciones de Balsa Plantabal Sa · RUC 0990533105001.” Company financial summary for ejercicio 2025.",
        "url": "https://encuentra.ec/empresa/plantaciones-de-balsa-plantabal-sa-0990533105001/",
        "annotation": "Ecuador registry aggregate of Plantabal 2025 revenue. Supports plantabal_ingresos_2025_60p8m.",
        "supports": ["plantabal_ingresos_2025_60p8m", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# 4 infrastructure/rail — Wabtec–MRS Logística fleet package USD 254m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "wabtec_mrs_254m_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "us",
        "counterpart": "Wabtec — MRS Logística locomotive / parts / maintenance package",
        "country": "Brazil",
        "asset": "23 Sep 2026: Wabtec announces agreement with MRS Logística worth approximately USD 254 million (R$1.3 billion), phased through 2032, covering new Evolution Series locomotives (incl. ES44ACi), spare parts, and specialized maintenance services for MRS’s 1,643 km MG–RJ–SP freight network.",
        "investment_type": "equipment_supply",
        "value": "254000000",
        "currency": "USD",
        "value_usd": "254000000",
        "fx_usd": "1",
        "fx_date": "2026-09-23",
        "year": "2026",
        "status": "active",
        "lat": "-19.92",
        "lon": "-43.94",
        "geo_note": "MRS network / Contagem–MG Wabtec manufacturing geography (approximate operational pin).",
        "evidence": "documented",
        "source_id": "wabtec_mrs_20260923",
        "note": "Actor: Wabtec (U.S.) — us. Company primary. Distinct from Contagem plant expansion and TRANSAP Chile locomotive order.",
    },
    {
        "id": "wabtec_mrs_254m_2026",
        "retrieved": "2026-10-01",
        "source_id": "wabtec_mrs_20260923",
        "url": "https://www.wabteccorp.com/newsroom/press-releases/mrs-log-stica-invests-us254m-to-strengthen-brazil-s-logistics-infrastructure-and-renew-its-fleet-with-wabtec",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "MRS Logística has taken another decisive step … by signing an agreement worth approximately US$254 million (R$1.3 billion) with Wabtec. The investment, which will be made in phases through 2032, includes the acquisition of new advanced-technology locomotives, spare parts and specialized maintenance services.",
        "note": "Opened Wabtec company release 23 Sep 2026.",
    },
    {
        "id": "wabtec_mrs_20260923",
        "type": "company",
        "chicago": "Wabtec Corporation. “MRS Logística invests US$254M to strengthen Brazil’s logistics infrastructure and renew its fleet with Wabtec.” 23 September 2026.",
        "url": "https://www.wabteccorp.com/newsroom/press-releases/mrs-log-stica-invests-us254m-to-strengthen-brazil-s-logistics-infrastructure-and-renew-its-fleet-with-wabtec",
        "annotation": "Wabtec primary on USD 254m MRS locomotive package. Supports wabtec_mrs_254m_2026.",
        "supports": ["wabtec_mrs_254m_2026", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 5 infrastructure/engineering_epc — Wabtec Contagem Global Engineering Center R$20m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "wabtec_contagem_r20m_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Wabtec — Contagem Global Engineering Center / plant expansion",
        "country": "Brazil",
        "asset": "5 Nov 2025: Wabtec investing R$20 million to expand Brazil operations — first LatAm Global Engineering Center (~9,000 m²; labs/workstations for ~300 engineers) near Contagem locomotive factory (Cidade Industrial, MG), plus new locomotive production line (+28% capacity) and logistics centers in Governador Valadares (MG) and Monte Alto (SP). Engineering-center opening targeted Dec 2025.",
        "investment_type": "greenfield_plant",
        "value": "20000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.93",
        "lon": "-44.05",
        "geo_note": "Contagem, Minas Gerais — Cidade Industrial Wabtec plant (company geography).",
        "evidence": "documented",
        "source_id": "wabtec_contagem_20251105",
        "note": "Actor: Wabtec (U.S.) — us. BRL stored without FX. Distinct from MRS USD 254m equipment package.",
    },
    {
        "id": "wabtec_contagem_r20m_2025",
        "retrieved": "2026-10-01",
        "source_id": "wabtec_contagem_20251105",
        "url": "https://www.wabteccorp.com/newsroom/press-releases/wabtec-to-expand-operations-and-workforce-in-brazil-with-r20-million-investment",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Wabtec Corporation (NYSE: WAB) is investing R$20 million to expand its operations, capabilities, and workforce in Brazil. … Wabtec plans to establish a Global Engineering Center – the company’s first in Latin America – and the launch of a new locomotive production line.",
        "note": "Opened Wabtec company release 5 Nov 2025.",
    },
    {
        "id": "wabtec_contagem_20251105",
        "type": "company",
        "chicago": "Wabtec Corporation. “Wabtec to Expand Operations and Workforce in Brazil with R$20 Million Investment.” 5 November 2025.",
        "url": "https://www.wabteccorp.com/newsroom/press-releases/wabtec-to-expand-operations-and-workforce-in-brazil-with-r20-million-investment",
        "annotation": "Wabtec primary on Contagem Global Engineering Center / R$20m Brazil expansion. Supports wabtec_contagem_r20m_2025.",
        "supports": ["wabtec_contagem_r20m_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 9 resources/nickel — Jervois SMP EU CRMA Strategic Project designation (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "jervois_smp_eu_crma_status_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "Jervois — São Miguel Paulista refinery EU CRMA Strategic Project status",
        "country": "Brazil",
        "asset": "Jervois company asset page (2026 project update): São Miguel Paulista Class 1 Ni–Co electrolytic refinery restart selected as a Strategic Project by the European Commission under the Critical Raw Materials Act; company reiterates 12,000 tpa Ni and 2,000 tpa Co cathode targets with construction/refurbishment continuing through 2026–2027. Regulatory/supply-chain designation angle — distinct from jervois_smp_restart_2025 (USD 130m FID) and ausenco_jervois_smp_epcm_2026.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.50",
        "lon": "-46.44",
        "geo_note": "São Miguel Paulista refinery, São Paulo municipality.",
        "evidence": "documented",
        "source_id": "jervois_smp_crma_page_2026",
        "note": "Actor: Jervois (coded us with prior SMP restart row) — us. No new CAPEX on page; CRMA Strategic Project status is the observation.",
    },
    {
        "id": "jervois_smp_eu_crma_status_2026",
        "retrieved": "2026-10-01",
        "source_id": "jervois_smp_crma_page_2026",
        "url": "https://jervoisglobal.com/assets/sao-miguel-paulista-refinery/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "We are proud that the restart of the Sao Miguel Paulista nickel cobalt refinery has been selected as a Strategic Project by the European Commission under the Critical Raw Materials Act. … Work has commenced on the refurbishment and restart project, which we anticipate will continue across 2026 and 2027.",
        "note": "Opened Jervois São Miguel Paulista asset page.",
    },
    {
        "id": "jervois_smp_crma_page_2026",
        "type": "company",
        "chicago": "Jervois. “São Miguel Paulista Refinery.” Company asset page (project update / EU CRMA Strategic Project status).",
        "url": "https://jervoisglobal.com/assets/sao-miguel-paulista-refinery/",
        "annotation": "Company primary on SMP EU CRMA Strategic Project designation and 2026–27 restart work. Supports jervois_smp_eu_crma_status_2026.",
        "supports": ["jervois_smp_eu_crma_status_2026", "hunt_res_nickel"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

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
        "hunt_res_water": "Cycle 47: logged newmont_yanacocha_water_2bn_2025 (U.S.; ~USD 2bn cumulative water transition).",
        "hunt_res_lithium": "Cycle 47: equal budget; PPG Stage 1 / Albemarle TED / EnergyX EXIM already (miss).",
        "hunt_res_balsa": "Cycle 47: logged plantabal_ingresos_2025_60p8m (allied; processor 2025 revenue — not trade duplicate).",
        "hunt_latam_rail_telecom": "Cycle 47: logged wabtec_mrs_254m_2026 (U.S.; USD 254m fleet package).",
        "hunt_infra_engineering_epc": "Cycle 47: logged wabtec_contagem_r20m_2025 (U.S.; R$20m Engineering Center).",
        "hunt_res_copper": "Cycle 47: equal budget; FCX El Abra / MMG Las Bambas already (miss).",
        "hunt_br_power_equip": "Cycle 47: equal budget; GE Vernova / Hitachi already dense (miss).",
        "hunt_infra_port_cranes": "Cycle 47: equal budget; SSA Manzanillo STS just prior cycle (miss).",
        "hunt_res_nickel": "Cycle 47: logged jervois_smp_eu_crma_status_2026 (U.S.; CRMA Strategic Project — not financing duplicate).",
        "hunt_energy_wind": "Cycle 47: equal budget; Vestas/Goldwind already dense (miss).",
        "hunt_res_graphite": "Cycle 47: equal budget; Graphcoa expand / South Star already (miss).",
        "hunt_energy_fission_smr": "Cycle 47: equal budget; Rosatom engagement / El Salvador 123 already (miss).",
        "hunt_infra_bridges_roads": "Cycle 47: equal budget; CHEC/Mota-Engil already (miss).",
        "hunt_energy_other_renewables": "Cycle 47: equal budget; ContourGlobal Oasis just prior cycle (miss).",
        "hunt_fenb_araxa": "Cycle 47: equal budget; Codemig/CBMM already (miss).",
        "hunt_infra_port_ownership": "Cycle 47: equal budget; SSA Isla Palma just prior cycle (miss).",
        "hunt_energy_solar": "Cycle 47: equal budget; COX Ecuador just prior cycle (miss).",
        "hunt_infra_building_materials": "Cycle 47: equal budget; Holcim–Cemex Colombia already (miss).",
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
    print("Cycle 47 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
