#!/usr/bin/env python3
"""Cycle 50 hunt: shuffle_seed=20261050; equal budget; U.S. side ≥1/3; thin_topup after.

Order: water, port_cranes, graphite, nickel, building_materials, bridges_roads,
niobium, engineering_epc, fission_smr, copper, balsa, other_renewables, solar,
wind, port_ownership, power_plants_grid, lithium, rail.
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
# 1 resources/water — AIIB USD 10m Aguas Pacífico equity co-investment (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aiib_aguas_pacifico_equity_10m_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "other",
        "counterpart": "AIIB / Patria Infrastructure Fund V — Aguas Pacífico (Project Aqua) equity co-investment",
        "country": "Chile",
        "asset": "19 Mar 2025: Asian Infrastructure Investment Bank approves USD 10 million equity co-investment alongside Patria Infrastructure Fund V in Aguas Pacífico desalination (Project Aqua) — Phase I 1,000 l/s plant + 104 km aqueduct + substation in Chile’s central region; Phase II to 2,000 l/s. Distinct financing layer from aguas_pacifico_desal_capex_1p2bn_2025 and Veolia O&M.",
        "investment_type": "financing",
        "value": "10000000",
        "currency": "USD",
        "value_usd": "10000000",
        "fx_usd": "1",
        "fx_date": "2025-03-19",
        "year": "2025",
        "status": "active",
        "lat": "-32.73",
        "lon": "-71.42",
        "geo_note": "Puchuncaví desal plant, Valparaíso Region (Aguas Pacífico / Project Aqua pin).",
        "evidence": "documented",
        "source_id": "aiib_aqua_chile_20250319",
        "note": "Actor: AIIB (multilateral) with Patria fund — other. AIIB news 19 Mar 2025; equity co-investment USD 10m.",
    },
    {
        "id": "aiib_aguas_pacifico_equity_10m_2025",
        "retrieved": "2026-10-01",
        "source_id": "aiib_aqua_chile_20250319",
        "url": "https://www.aiib.org/en/news-events/news/2025/aiib-approves-first-investment-chile-support-climate-resilient-water-infrastructure.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Asian Infrastructure Investment Bank (AIIB) approved a USD10-million equity co-investment alongside Patria Infrastructure Fund V to support the development of the Aguas Pacifico project (Project Aqua). … Phase I includes the construction of a 1,000 liters-per-second (l/s) desalination plant, a 104 km aqueduct, and an electricity substation. Phase II will double the plant’s capacity to 2,000 l/s.",
        "note": "Opened AIIB 19 Mar 2025 Chile Aguas Pacífico equity release.",
    },
    {
        "id": "aiib_aqua_chile_20250319",
        "type": "government",
        "chicago": "Asian Infrastructure Investment Bank. “AIIB Approves First Investment in Chile to Support Climate-Resilient Water Infrastructure.” 19 March 2025.",
        "url": "https://www.aiib.org/en/news-events/news/2025/aiib-approves-first-investment-chile-support-climate-resilient-water-infrastructure.html",
        "annotation": "AIIB primary on USD 10m Aguas Pacífico equity co-investment. Supports aiib_aguas_pacifico_equity_10m_2025.",
        "supports": ["aiib_aguas_pacifico_equity_10m_2025", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 4 resources/nickel — DFC Piauí Nickel follow-on ESIA (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "dfc_piaui_nickel_esia_followon_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "DFC / Techmet — Piauí Nickel Project follow-on ESIA disclosure",
        "country": "Brazil",
        "asset": "2026: DFC publishes updated Initial Project Summary for follow-on investment in Piauí Nickel (Brejo Seco, Capitão Gervásio Oliveira, PI); applicant Techmet, Ltd.; open-pit laterite heap-leach targeting 24,500 tpy Ni and 1,100 tpy Co in hydroxide; footprint ~1,587 ha; ~3,500 construction workers; February 2026 layout changes (water pipeline critical habitat, gravel quarry, resettlement). Distinct from brazilian_nickel_dfc_loi_2024 LOI — documentary step toward closed financing; loan amount not restated on this IPS page.",
        "investment_type": "financing",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.10",
        "lon": "-42.50",
        "geo_note": "Brejo Seco / Capitão Gervásio Oliveira, Piauí (PNP mine pin; approximate).",
        "evidence": "documented",
        "source_id": "dfc_piaui_ips_2026",
        "note": "Actor: DFC (U.S.) financing track for Techmet/PNP — us. Opened DFC Initial Project Summary PDF; follow-on to 2022 ESIA; CAPEX/loan USD not restated here (prior LOI up to USD 550m separately logged).",
    },
    {
        "id": "dfc_piaui_nickel_esia_followon_2026",
        "retrieved": "2026-10-01",
        "source_id": "dfc_piaui_ips_2026",
        "url": "https://www.dfc.gov/sites/default/files/esia/2026/piauinickel/02_Initial%20Project%20Summary_Piaui_508.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "This is a follow-on investment in the Project. DFC previously disclosed the Project ESIA in 2022 … Below are maps showing the original 2022 layout … and the layout and Direct AOI as of February 2026. The Project will construct and operate an open-pit nickel and cobalt mine … to produce 24,500 metric tonnes per year of nickel and 1,100 metric tonnes per year of cobalt contained in hydroxide products.",
        "note": "Opened DFC Piauí Nickel Initial Project Summary PDF (2026 follow-on).",
    },
    {
        "id": "dfc_piaui_ips_2026",
        "type": "government",
        "chicago": "U.S. International Development Finance Corporation. “Initial Project Summary – Piauí Nickel Project.” 2026.",
        "url": "https://www.dfc.gov/sites/default/files/esia/2026/piauinickel/02_Initial%20Project%20Summary_Piaui_508.pdf",
        "annotation": "DFC primary IPS on Piauí Nickel follow-on investment / Feb 2026 layout. Supports dfc_piaui_nickel_esia_followon_2026.",
        "supports": ["dfc_piaui_nickel_esia_followon_2026", "hunt_res_nickel"],
    },
)

# ---------------------------------------------------------------------------
# 5 infrastructure/building_materials — Holcim/Geocycle Nobsa USD 2m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "holcim_geocycle_nobsa_2m_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim Colombia / Geocycle — Nobsa co-processing platform upgrade",
        "country": "Colombia",
        "asset": "Jul 2025: Holcim Colombia invests USD 2 million to modernise Geocycle co-processing platform at Nobsa cement plant (Boyacá); capacity to process 100,000 t/yr waste (paper/cardboard/plastics/biomass) into alternative fuels; shredder >10 t/h and dosing up to 20 t/h; thermal substitution to 40% short-term with >70% target by 2030. Distinct from Holcim Tecomán MXN 200m / Guayaquil calcined clay.",
        "investment_type": "capex",
        "value": "2000000",
        "currency": "USD",
        "value_usd": "2000000",
        "fx_usd": "1",
        "fx_date": "2025-07-03",
        "year": "2025",
        "status": "active",
        "lat": "5.77",
        "lon": "-72.94",
        "geo_note": "Nobsa cement plant, Boyacá (Holcim/Geocycle co-processing pin).",
        "evidence": "documented",
        "source_id": "globalcement_nobsa_20250710",
        "note": "Actor: Holcim (Swiss) / Geocycle — allied. Global Cement 10 Jul 2025 citing Holcim Colombia USD 2m Nobsa upgrade.",
    },
    {
        "id": "holcim_geocycle_nobsa_2m_2025",
        "retrieved": "2026-10-01",
        "source_id": "globalcement_nobsa_20250710",
        "url": "https://globalcement.com/news/19611-holcim-colombia-upgrades-nobsa-cement-plant-s-co-processing-platform",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Colombia: Holcim Colombia has invested US$2m to modernise its co-processing platform at its Nobsa cement plant in Boyacá. The upgraded facility will process 100,000t/yr of waste into alternative fuels for the cement plant, raising thermal substitution to 40% in the short term, with a target of 70% by 2030.",
        "note": "Opened Global Cement 10 Jul 2025 Nobsa co-processing coverage.",
    },
    {
        "id": "globalcement_nobsa_20250710",
        "type": "press",
        "chicago": "Global Cement. “Holcim Colombia upgrades Nobsa cement plant’s co-processing platform.” 10 July 2025.",
        "url": "https://globalcement.com/news/19611-holcim-colombia-upgrades-nobsa-cement-plant-s-co-processing-platform",
        "annotation": "Trade press on Holcim Colombia USD 2m Nobsa Geocycle upgrade. Supports holcim_geocycle_nobsa_2m_2025.",
        "supports": ["holcim_geocycle_nobsa_2m_2025", "hunt_infra_building_materials"],
    },
)

# ---------------------------------------------------------------------------
# 8 infrastructure/engineering_epc — KBR Pampa Bahía Blanca ammonia (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "kbr_pampa_bahia_blanca_ammonia_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "KBR — Pampa Energía Bahía Blanca ammonia-urea complex (technology license / BED)",
        "country": "Argentina",
        "asset": "20 Jul 2026: KBR (NYSE: KBR) selected to provide Purifier® technology licensing, basic engineering design package, and proprietary equipment for Pampa Energía’s 3,430 tpd ammonia plant within a new ammonia-urea complex at Bahía Blanca; operations targeted end-2029; described as largest single-train ammonia plant in Latin America. CAPEX USD for full complex not disclosed on KBR page.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-38.72",
        "lon": "-62.27",
        "geo_note": "Bahía Blanca, Buenos Aires Province (Pampa ammonia-urea complex pin).",
        "evidence": "documented",
        "source_id": "kbr_pampa_ammonia_20260720",
        "note": "Actor: KBR (U.S.) — us. Company release; license/BED/equipment award; full-complex CAPEX not on page.",
    },
    {
        "id": "kbr_pampa_bahia_blanca_ammonia_2026",
        "retrieved": "2026-10-01",
        "source_id": "kbr_pampa_ammonia_20260720",
        "url": "https://www.kbr.com/en/insights-news/press-release/kbr-ammonia-technology-selected-pampa-energia-its-facility-argentina",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "KBR (NYSE: KBR) announced today that its Purifier® technology has been selected for Pampa Energía’s new ammonia-urea complex in Argentina. Under the terms of the contract, KBR will provide technology licensing, basic engineering design package, and proprietary equipment for the 3,430 tons per day ammonia plant, which is expected to commence operations by the end of 2029. The plant will be part of the ammonia and urea complex in Bahía Blanca, Argentina. Upon completion, it will include the largest single-train ammonia plant in Latin America.",
        "note": "Opened KBR 20 Jul 2026 Pampa Energía ammonia release.",
    },
    {
        "id": "kbr_pampa_ammonia_20260720",
        "type": "company",
        "chicago": "KBR. “KBR Ammonia Technology Selected by Pampa Energía for its Facility in Argentina.” 20 July 2026.",
        "url": "https://www.kbr.com/en/insights-news/press-release/kbr-ammonia-technology-selected-pampa-energia-its-facility-argentina",
        "annotation": "Company primary on Purifier license/BED for 3,430 tpd Bahía Blanca ammonia. Supports kbr_pampa_bahia_blanca_ammonia_2026.",
        "supports": ["kbr_pampa_bahia_blanca_ammonia_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 11 resources/balsa — Gurit Balsaflex Quevedo processor presence (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "gurit_balsaflex_quevedo_presence",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "Gurit Balsaflex Cia. Ltda. — Quevedo end-grain balsa core plant",
        "country": "Ecuador",
        "asset": "Active Gurit Balsaflex processing presence at Km 19 Vía Quevedo–Ventanas, Quevedo (Los Ríos): SRI-registered matriz open for end-grain balsa core used in wind-blade / marine composites; commercial name BALSAFLEX. Processor/plant-presence angle — not a trade-flow or Plantabal duplicate; CAPEX USD not disclosed on registry page.",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.45",
        "geo_note": "Quevedo, Los Ríos — Km 19 Vía Quevedo–Ventanas (Gurit Balsaflex matriz pin).",
        "evidence": "documented",
        "source_id": "encuentra_guritbalsaflex_2025",
        "note": "Actor: Gurit (Swiss) via Guritbalsaflex Cia. Ltda. — allied. Ecuador company registry (Encuentra/SRI) confirming open Quevedo plant; wind-blade core processor angle.",
    },
    {
        "id": "gurit_balsaflex_quevedo_presence",
        "retrieved": "2026-10-01",
        "source_id": "encuentra_guritbalsaflex_2025",
        "url": "https://encuentra.ec/empresa/guritbalsaflex-cia-ltda-0992500670001/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Razón social GURITBALSAFLEX CIA. LTDA. Nombre comercial BALSAFLEX … Dirección KM 19 de la Via Quevedo Ventanas, Via Principal Ubicación Quevedo, Los Rios … Establecimientos · 2 registrados, 1 abierto MATRIZ Los Rios / Quevedo / San Carlos / KM 19 Via a Ventanas S/N y SN Abierto … Último año con balance presentado 2025.",
        "note": "Opened Encuentra.ec / SRI company fiche for Guritbalsaflex Quevedo matriz.",
    },
    {
        "id": "encuentra_guritbalsaflex_2025",
        "type": "government",
        "chicago": "Encuentra.ec (SRI registry extract). “Guritbalsaflex Cia. Ltda. · RUC 0992500670001.” Accessed 1 October 2026.",
        "url": "https://encuentra.ec/empresa/guritbalsaflex-cia-ltda-0992500670001/",
        "annotation": "Ecuador company-registry fiche confirming open Quevedo Balsaflex plant. Supports gurit_balsaflex_quevedo_presence.",
        "supports": ["gurit_balsaflex_quevedo_presence", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# 15 infrastructure/port_ownership — DFC Yilport Puerto Bolívar USD 150m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "dfc_yilport_puerto_bolivar_150m_2023",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "DFC — Yilport Terminal Operations Puerto Bolívar expansion loan",
        "country": "Ecuador",
        "asset": "5 May 2023: DFC commits USD 150 million loan to Yilport Terminal Operations S.A. to expand/modernize Puerto Bolívar container port (El Oro); JPMorgan arranging; projected up to 1,250 direct/indirect jobs and up to USD 750 million FDI catalyzed. U.S. DFI financing of Pacific Ecuador container terminal — distinct from Konecranes Yilport Acajutla crane row.",
        "investment_type": "financing",
        "value": "150000000",
        "currency": "USD",
        "value_usd": "150000000",
        "fx_usd": "1",
        "fx_date": "2023-05-05",
        "year": "2023",
        "status": "active",
        "lat": "-3.26",
        "lon": "-80.00",
        "geo_note": "Puerto Bolívar, El Oro (Yilport container terminal pin).",
        "evidence": "documented",
        "source_id": "dfc_yilport_bolivar_20230505",
        "note": "Actor: DFC (U.S.) loan — us. Agency release; Yilport is operator/borrower.",
    },
    {
        "id": "dfc_yilport_puerto_bolivar_150m_2023",
        "retrieved": "2026-10-01",
        "source_id": "dfc_yilport_bolivar_20230505",
        "url": "https://www.dfc.gov/media/press-releases/dfc-commits-150-million-yilport-terminal-expand-and-upgrade-port",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "The U.S. International Development Finance Corporation (DFC) today announced it has committed a $150 million loan to Yilport Terminal Operations S.A. to finance the expansion and modernization of the Puerto Bolivar container port in Ecuador’s El Oro province. JPMorgan Chase Bank, N.A. is arranging the transaction. … The expansion of the port is projected to create up to 1,250 direct and indirect jobs; catalyze up to $750 million of foreign direct investment.",
        "note": "Opened DFC 5 May 2023 Puerto Bolívar USD 150m release.",
    },
    {
        "id": "dfc_yilport_bolivar_20230505",
        "type": "government",
        "chicago": "U.S. International Development Finance Corporation. “DFC Commits $150 Million to Yilport Terminal to Expand and Upgrade Port Infrastructure in Ecuador.” 5 May 2023.",
        "url": "https://www.dfc.gov/media/press-releases/dfc-commits-150-million-yilport-terminal-expand-and-upgrade-port",
        "annotation": "DFC primary on USD 150m Puerto Bolívar expansion loan. Supports dfc_yilport_puerto_bolivar_150m_2023.",
        "supports": ["dfc_yilport_puerto_bolivar_150m_2023", "hunt_infra_port_ownership"],
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
        "hunt_res_water": "Cycle 50: logged aiib_aguas_pacifico_equity_10m_2025 (other; USD 10m equity — distinct from CapEx/O&M).",
        "hunt_infra_port_cranes": "Cycle 50: equal budget; SSA Guaymas STS/eRTG / Konecranes Manaus/Arica already (miss).",
        "hunt_res_graphite": "Cycle 50: equal budget; Atlas Malacacheta corridor/MRE already (miss).",
        "hunt_res_nickel": "Cycle 50: logged dfc_piaui_nickel_esia_followon_2026 (U.S.; DFC follow-on IPS — not duplicate offtake/LOI).",
        "hunt_infra_building_materials": "Cycle 50: logged holcim_geocycle_nobsa_2m_2025 (allied; USD 2m Nobsa co-processing).",
        "hunt_infra_bridges_roads": "Cycle 50: equal budget; CHEC/Mota-Engil already (miss).",
        "hunt_fenb_araxa": "Cycle 50: equal budget; CBMM 2025 spend / Codemig / St George already (miss).",
        "hunt_infra_engineering_epc": "Cycle 50: logged kbr_pampa_bahia_blanca_ammonia_2026 (U.S.; 3,430 tpd Purifier license/BED).",
        "hunt_energy_fission_smr": "Cycle 50: equal budget; USTDA LAC nuclear / FIRST workshop already (miss).",
        "hunt_res_copper": "Cycle 50: equal budget; FCX El Abra Continuidad already (miss).",
        "hunt_res_balsa": "Cycle 50: logged gurit_balsaflex_quevedo_presence (allied; processor/plant — not trade duplicate).",
        "hunt_energy_other_renewables": "Cycle 50: equal budget; ContourGlobal / AES / CIP already (miss).",
        "hunt_energy_solar": "Cycle 50: equal budget; ContourGlobal Víctor Jara already (miss).",
        "hunt_energy_wind": "Cycle 50: equal budget; Vestas/Nordex/Goldwind already (miss).",
        "hunt_infra_port_ownership": "Cycle 50: logged dfc_yilport_puerto_bolivar_150m_2023 (U.S.; DFC USD 150m).",
        "hunt_br_power_equip": "Cycle 50: equal budget; USTDA ARCONEL/CNEL already prior cycle (miss).",
        "hunt_res_lithium": "Cycle 50: equal budget; PPG / Albemarle already (miss).",
        "hunt_latam_rail_telecom": "Cycle 50: equal budget; CRRC Araraquara / Wabtec already (miss).",
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
    print("Cycle 50 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
