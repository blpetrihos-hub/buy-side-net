#!/usr/bin/env python3
"""Cycle 51 hunt: shuffle_seed=20261051; equal budget; U.S. side ≥1/3; thin_topup after.

Order: engineering_epc, building_materials, rail, copper, niobium, bridges_roads,
other_renewables, lithium, solar, water, nickel, fission_smr, power_plants_grid,
port_cranes, wind, port_ownership, balsa, graphite.
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
# 1 infrastructure/engineering_epc — McDermott BRAVA Papa-Terra/Atlanta (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "mcdermott_brava_papa_terra_atlanta_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "McDermott — BRAVA Energia Papa-Terra / Atlanta Phase 2 subsea T&I",
        "country": "Brazil",
        "asset": "7 Jul 2025: McDermott awarded sizeable offshore transportation and installation contract by BRAVA Energia for flexible pipelines, umbilicals and associated subsea equipment for two new wells at Papa-Terra (Campos Basin) and two new wells at Atlanta Phase 2 (Block BS-4, Santos Basin); scope includes pre-commissioning and onshore base support. McDermott defines “sizeable” as USD 1–50 million — exact contract USD not disclosed on opened page.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-22.50",
        "lon": "-40.50",
        "geo_note": "Papa-Terra / Campos Basin offshore pin (approximate; paired Atlanta Santos Basin wells in same award).",
        "evidence": "documented",
        "source_id": "rigzone_mcdermott_brava_20250714",
        "note": "Actor: McDermott (U.S.) — us. Rigzone 14 Jul 2025 citing company release; sizeable = USD 1–50m band only (no point CAPEX entered).",
    },
    {
        "id": "mcdermott_brava_papa_terra_atlanta_2025",
        "retrieved": "2026-10-01",
        "source_id": "rigzone_mcdermott_brava_20250714",
        "url": "https://www.rigzone.com/news/mcdermott_wins_contract_for_brava_energias_projects_offshore_brazil-14-jul-2025-181125-article/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "McDermott said it has been awarded a “sizeable” offshore transportation and installation contract by Brazilian oil and gas firm BRAVA Energia for the Papa-Terra field in the Campos Basin and the Atlanta field in Block BS-4 within the Santos Basin, both offshore Brazil. Under the contract scope, McDermott will execute the transportation and installation of flexible pipelines, umbilicals, and associated subsea equipment for two new wells at the Papa-Terra field and two new wells for the Atlanta Phase 2 development. … McDermott said it defines a sizeable contract as having a value between $1 million and $50 million.",
        "note": "Opened Rigzone coverage of McDermott BRAVA Energia Brazil award.",
    },
    {
        "id": "rigzone_mcdermott_brava_20250714",
        "type": "press",
        "chicago": "Rigzone. “McDermott Wins Contract for BRAVA Energia’s Projects Offshore Brazil.” 14 July 2025.",
        "url": "https://www.rigzone.com/news/mcdermott_wins_contract_for_brava_energias_projects_offshore_brazil-14-jul-2025-181125-article/",
        "annotation": "Trade press citing McDermott sizeable Papa-Terra/Atlanta subsea T&I award. Supports mcdermott_brava_papa_terra_atlanta_2025.",
        "supports": ["mcdermott_brava_papa_terra_atlanta_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 3 infrastructure/rail — Siemens Mobility Trivia SP ATO/ETCS L2 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "siemens_trivia_sp_ato_etcs_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Siemens Mobility / Trivia Trens — São Paulo Lines 11/12/13 ATO over ETCS L2",
        "country": "Brazil",
        "asset": "Siemens Mobility contract from Trivia Trens S.A. to deliver ATO over ETCS Level 2 digital signaling for São Paulo CPTM/Trivia lines 11-Coral, 12-Sapphire and 13-Jade: 140 km track, 46 stations; onboard Trainguard ETCS for 107 trains, 6 MRS locomotives, 3 Trivia locomotives and 17 auxiliary vehicles — stated as Latin America’s largest ATO-over-ETCS L2 implementation. Distinct from siemens_sp_line4_cbtc_2026 and Hitachi Trivia power row. CAPEX USD not disclosed on Siemens page.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "São Paulo metropolitan CPTM/Trivia network pin (Lines 11/12/13).",
        "evidence": "documented",
        "source_id": "siemens_trivia_ato_etcs_2026",
        "note": "Actor: Siemens Mobility (German) — allied. Company press release; contract value USD not on page.",
    },
    {
        "id": "siemens_trivia_sp_ato_etcs_2026",
        "retrieved": "2026-10-01",
        "source_id": "siemens_trivia_ato_etcs_2026",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-mobility-modernize-three-lines-sao-paulos-transport-network-latin-americas",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Siemens Mobility has secured a contract from Trivia Trens S.A. to deliver and implement a complete, digital signaling system featuring Automatic Train Operation (ATO) over ETCS Level 2 for São Paulo’s commuter rail lines 11-Coral, 12-Sapphire, and 13-Jade. The project covers 140 kilometers of track and 46 stations, marking Latin America’s largest implementation of this advanced rail signaling technology. The contract includes equipping 107 trains, six locomotives MRS, three locomotives TRIVIA and 17 auxiliary vehicles (yellow fleet) with Trainguard ETCS … on-board units.",
        "note": "Opened Siemens Mobility Trivia/São Paulo ATO-over-ETCS release.",
    },
    {
        "id": "siemens_trivia_ato_etcs_2026",
        "type": "company",
        "chicago": "Siemens Mobility. “Siemens Mobility to modernize three lines of São Paulo’s transport network in Latin America’s largest ATO over ETCS project.” 9 October 2025.",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-mobility-modernize-three-lines-sao-paulos-transport-network-latin-americas",
        "annotation": "Company primary on Trivia Lines 11/12/13 ATO-over-ETCS L2. Supports siemens_trivia_sp_ato_etcs_2026.",
        "supports": ["siemens_trivia_sp_ato_etcs_2026", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 15 energy/wind — AES / IDB Invest Vientos Bonaerenses III–IV (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aes_idb_vientos_bonaerenses_iii_iv_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "us",
        "counterpart": "AES Argentina / IDB Invest — Vientos Bonaerenses III & IV expansion",
        "country": "Argentina",
        "asset": "IDB Invest approves financing package of up to USD 100 million (A/B: up to USD 20m IDB Invest + up to USD 80m IFI tranche) for Vientos Bonaerenses S.A. (AES Argentina) to build VBIII/VBIV wind farms in southern Buenos Aires Province; adds ~102.4 MW bringing complex total to ~202.2 MW; ~370 GWh/year incremental. Companion project disclosure lists 99.1 MW / 16 turbines across Tornquist and Bahía Blanca. Distinct from aes_jk1_jk2_idb_invest_150m_2025 (Colombia).",
        "investment_type": "financing",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2026-01-08",
        "year": "2025",
        "status": "active",
        "lat": "-38.72",
        "lon": "-62.27",
        "geo_note": "Bahía Blanca / southern Buenos Aires Province (VBIII Tornquist / VBIV Bahía Blanca complex pin).",
        "evidence": "documented",
        "source_id": "idb_invest_vientos_bonaerenses_2026",
        "note": "Actor: AES Argentina (U.S. AES) with IDB Invest A/B package — us. IDB Invest news + project disclosure; package up to USD 100m.",
    },
    {
        "id": "aes_idb_vientos_bonaerenses_iii_iv_2026",
        "retrieved": "2026-10-01",
        "source_id": "idb_invest_vientos_bonaerenses_2026",
        "url": "https://idbinvest.org/en/news-media/idb-invest-and-vientos-bonaerenses-strengthen-energy-security-argentina",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "IDB Invest has approved a financing package of up to $100 million for Vientos Bonaerenses S.A., an AES Argentina company, to support the expansion of the Vientos Bonaerenses wind farm project in Argentina. … The new wind farms, Vientos Bonaerenses III and IV, located in the southern part of Buenos Aires Province, will provide approximately 370 GWh of additional electricity per year once operational … The project will add 102.4 MW of capacity to the Vientos Bonaerenses complex, bringing its total installed capacity to 202.2 MW. The financing will be provided through an A/B loan structure of up to $100 million, consisting of an IDB Invest tranche of up to $20 million and a tranche of up to $80 million from international financial institutions.",
        "note": "Opened IDB Invest Vientos Bonaerenses / AES Argentina financing release.",
    },
    {
        "id": "idb_invest_vientos_bonaerenses_2026",
        "type": "government",
        "chicago": "IDB Invest. “IDB Invest and Vientos Bonaerenses Strengthen Energy Security in Argentina.” 2026.",
        "url": "https://idbinvest.org/en/news-media/idb-invest-and-vientos-bonaerenses-strengthen-energy-security-argentina",
        "annotation": "IDB Invest primary on up-to-USD 100m AES Argentina VBIII/VBIV package. Supports aes_idb_vientos_bonaerenses_iii_iv_2026.",
        "supports": ["aes_idb_vientos_bonaerenses_iii_iv_2026", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# 17 resources/balsa — CoreLite Balsasud Ecuador processor (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "corelite_balsasud_ecuador_presence",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "CoreLite / Balsasud S.A. — Ecuador balsa core processing plant",
        "country": "Ecuador",
        "asset": "CoreLite (Miami, U.S.) states its main balsa wood factory is the Balsasud S.A. facility in Ecuador, sourcing only sustainably grown balsa for wind/marine core materials. U.S. processor presence in Ecuador wind-blade supply chain — distinct from Plantabal/3A and Gurit Balsaflex Quevedo; CAPEX USD not disclosed on sustainability page.",
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
        "geo_note": "Ecuador balsa processing (Los Ríos / Quevedo region pin; CoreLite Balsasud facility — approximate).",
        "evidence": "documented",
        "source_id": "corelite_sustainability_balsasud",
        "note": "Actor: CoreLite (U.S., Miami HQ) via Balsasud S.A. — us. Company sustainability page on Ecuador main balsa factory; processor angle not trade duplicate.",
    },
    {
        "id": "corelite_balsasud_ecuador_presence",
        "retrieved": "2026-10-01",
        "source_id": "corelite_sustainability_balsasud",
        "url": "https://www.corelitecomposites.com/sustainability",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Our main balsa wood factory, the Balsasud S.A. facility in Ecuador sources only sustainably grown balsa wood trees. Our goal is to deliver balsa wood that has been responsibly sourced, as our way to fight illegal logging, which is one of the largest causes for deforestation.",
        "note": "Opened CoreLite sustainability page naming Balsasud Ecuador factory.",
    },
    {
        "id": "corelite_sustainability_balsasud",
        "type": "company",
        "chicago": "CoreLite. “Sustainability.” Accessed 1 October 2026.",
        "url": "https://www.corelitecomposites.com/sustainability",
        "annotation": "Company primary naming Balsasud S.A. Ecuador as main balsa factory. Supports corelite_balsasud_ecuador_presence.",
        "supports": ["corelite_balsasud_ecuador_presence", "hunt_res_balsa"],
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
        "hunt_infra_engineering_epc": "Cycle 51: logged mcdermott_brava_papa_terra_atlanta_2025 (U.S.; sizeable Papa-Terra/Atlanta subsea T&I).",
        "hunt_infra_building_materials": "Cycle 51: equal budget; Holcim Nobsa / Tecomán already (miss).",
        "hunt_latam_rail_telecom": "Cycle 51: logged siemens_trivia_sp_ato_etcs_2026 (allied; ATO-over-ETCS L2 Lines 11/12/13).",
        "hunt_res_copper": "Cycle 51: equal budget; FCX El Abra / Chilean Cobalt EXIM already (miss).",
        "hunt_fenb_araxa": "Cycle 51: equal budget; CBMM XNO / R$13bn / 2025–26 spend already (miss).",
        "hunt_infra_bridges_roads": "Cycle 51: equal budget; CHEC already (miss).",
        "hunt_energy_other_renewables": "Cycle 51: equal budget; ContourGlobal / AES / CIP already (miss).",
        "hunt_res_lithium": "Cycle 51: equal budget; EnergyX EXIM / PPG already (miss).",
        "hunt_energy_solar": "Cycle 51: equal budget; ContourGlobal Víctor Jara already (miss).",
        "hunt_res_water": "Cycle 51: equal budget; AIIB Aguas Pacífico already prior cycle (miss).",
        "hunt_res_nickel": "Cycle 51: equal budget; DFC Piauí ESIA / Jervois already (miss).",
        "hunt_energy_fission_smr": "Cycle 51: equal budget; Peru FIRST bilateral / Argentina FIRST already (miss).",
        "hunt_br_power_equip": "Cycle 51: equal budget; USTDA Ecuador / GE Vernova Azulão already (miss).",
        "hunt_infra_port_cranes": "Cycle 51: equal budget; SSA Guaymas / Konecranes already (miss).",
        "hunt_energy_wind": "Cycle 51: logged aes_idb_vientos_bonaerenses_iii_iv_2026 (U.S.; IDB Invest up to USD 100m).",
        "hunt_infra_port_ownership": "Cycle 51: equal budget; DFC Yilport Bolívar already prior cycle (miss).",
        "hunt_res_balsa": "Cycle 51: logged corelite_balsasud_ecuador_presence (U.S.; Balsasud processor — not trade duplicate).",
        "hunt_res_graphite": "Cycle 51: equal budget; Atlas Malacacheta corridor/MRE already (miss).",
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
    print("Cycle 51 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
