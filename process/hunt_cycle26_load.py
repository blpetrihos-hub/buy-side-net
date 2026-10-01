#!/usr/bin/env python3
"""Cycle 26 hunt: shuffle_seed=20261026; equal budget across 18 subcategories."""
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


# seed 20261026 order:
# nickel, other_renewables, wind, solar, graphite, balsa, rail, engineering_epc,
# water, port_ownership, port_cranes, copper, niobium, power_plants_grid,
# fission_smr, building_materials, lithium, bridges_roads

# 1 resources/nickel — miss (Centaurus BNDES LOI / Glencore offtake / MMG Anglo already logged)
# 2 energy/other_renewables — BYD Energy Storage / Grenergy Central Oasis 2.6 GWh
A(
    {
        "id": "byd_grenergy_central_oasis_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "BYD Energy Storage — 2.6 GWh MC Cube T BESS supply for Grenergy Central Oasis (Chile)",
        "country": "Chile",
        "asset": "Agreement to supply 2.6 GWh / 468 MC Cube T (Blade Battery) units for Central Oasis phases I–IV: Gran Teno (939 MWh), Planchón (402 MWh), Tamango (168 MWh), Monte Águila (1.1 GWh); follows May 2025 3.5 GWh Elena/Oasis de Atacama supply; Central Oasis platform ~1.1 GW solar + 4 GWh storage, est. investment USD 900m (platform, not BYD contract USD)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-35.1",
        "lon": "-71.3",
        "geo_note": "Central Chile Central Oasis cluster (Gran Teno / Maule corridor approximate; Grenergy release).",
        "evidence": "documented",
        "source_id": "grenergy_byd_central_oasis_20260326",
        "note": "Actor: BYD Energy Storage (PRC) — prc; buyer/developer Grenergy (Spanish) — allied counterpart not dual-sided here. Company Grenergy English PDF 26 Mar 2026. No BYD contract USD on page (platform USD 900m not entered as BYD value). Distinct from trina_atlas_copiapo_bess_2025 / catl_cip_alegria_bess_2026 / tesla_colbun_celda_solar_2024.",
    },
    {
        "id": "byd_grenergy_central_oasis_2026",
        "retrieved": "2026-10-01",
        "source_id": "grenergy_byd_central_oasis_20260326",
        "url": "https://grenergy.eu/wp-content/uploads/2026/03/pr-grenergy-acquires-2-6-gwh-of-batteries-from-byd-energy-storage-for-central-oasis-v5.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Grenergy has signed a new agreement with BYD Energy Storage … to supply 2.6 GWh of energy storage systems for its Central Oasis platform, located in central Chile. … This new purchase of 468 MC Cube T batteries",
        "note": "Opened Grenergy company English press PDF 26 Mar 2026.",
    },
    {
        "id": "grenergy_byd_central_oasis_20260326",
        "type": "company",
        "chicago": "Grenergy. “Grenergy acquires 2.6 GWh of batteries from BYD Energy Storage for Central Oasis.” 26 March 2026.",
        "url": "https://grenergy.eu/wp-content/uploads/2026/03/pr-grenergy-acquires-2-6-gwh-of-batteries-from-byd-energy-storage-for-central-oasis-v5.pdf",
        "annotation": "Company primary on BYD 2.6 GWh Central Oasis Chile BESS supply. Supports byd_grenergy_central_oasis_2026.",
        "supports": ["byd_grenergy_central_oasis_2026", "hunt_energy_other_renewables"],
    },
)

# 3 energy/wind — miss (Statkraft Emma / Vestas Esquina / Goldwind / Envision already logged)
# 4 energy/solar — miss (Hanersun Solfácil logged C25; JA Solar Mexico page blocked)

# 5 resources/graphite — South Star selected for BNDES/FINEP strategic minerals program
A(
    {
        "id": "south_star_bndes_finep_select_2025",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "South Star Battery Metals — selected for BNDES/FINEP Transformation of Strategic Minerals initiative (Santa Cruz)",
        "country": "Brazil",
        "asset": "Selection into R$5bn (company cites US$895m) BNDES–FINEP Transformation of Strategic Minerals initiative for graphite/critical-minerals processing; company to submit Phase 2/3 + downstream graphite business plan; potential structures may include credit, equity, grants (no committed facility USD on page); maiden Santa Cruz flake shipment to North America 5 Jun 2025",
        "investment_type": "financing",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-16.6",
        "lon": "-39.4",
        "geo_note": "Santa Cruz Graphite Mine, southern Bahia (South Star release).",
        "evidence": "documented",
        "source_id": "south_star_bndes_finep_20250616",
        "note": "Actor: South Star Battery Metals (Canadian) — allied; Brazilian public banks BNDES/FINEP as program sponsors. Company PDF 16 Jun 2025. Selection/eligibility — not a closed loan; value blank. Distinct from south_star_santa_cruz_graphite_2024 presence / south_star_santa_cruz_po_36t_2026 purchase order / Graphcoa rows.",
    },
    {
        "id": "south_star_bndes_finep_select_2025",
        "retrieved": "2026-10-01",
        "source_id": "south_star_bndes_finep_20250616",
        "url": "https://southstarbatterymetals.com/wp-content/uploads/2025/06/STS_06_2025_-Producer_R1.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "South Star’s flagship graphite mine Santa Cruz was selected by Brazilian National Development Bank (“BNDES”) and Brazil’s Innovation Agency (“FINEP”) as part of the Transformation of Strategic Minerals initiative. … selected by the R$5B (US$895M) Transformation of Strategic Minerals initiative",
        "note": "Opened South Star company PDF 16 Jun 2025.",
    },
    {
        "id": "south_star_bndes_finep_20250616",
        "type": "company",
        "chicago": "South Star Battery Metals Corp. “South Star Battery Metals Announces Selection by BNDES and FINEP for Strategic Minerals Funding Program, Maiden Shipment of Flake Graphite from the Santa Cruz Mine and Operational Update.” 16 June 2025.",
        "url": "https://southstarbatterymetals.com/wp-content/uploads/2025/06/STS_06_2025_-Producer_R1.pdf",
        "annotation": "Company primary on BNDES/FINEP strategic-minerals selection for Santa Cruz graphite. Supports south_star_bndes_finep_select_2025.",
        "supports": ["south_star_bndes_finep_select_2025", "hunt_res_graphite"],
    },
)

# 6 resources/balsa — miss (no new named processing stake with openable primary)
# 7 infrastructure/rail — miss (CAF Trivia logged C25)
# 8 infrastructure/engineering_epc — miss (Worley Diablillos / Bechtel EIMISA already logged)
# 9 resources/water — miss (Techint/Sacyr/Acciona set)
# 10 infrastructure/port_ownership — miss (APM Callao / ICTSI Aratu / Suape already logged)

# 11 infrastructure/port_cranes — Kalmar electric empty handlers / Lechman Terminais
A(
    {
        "id": "kalmar_lechman_ech_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Kalmar — six electric empty container handlers for Lechman Terminais (Guarujá / Santos hinterland)",
        "country": "Brazil",
        "asset": "Order for six Kalmar electric empty container handlers (7-high stack; 400 kWh batteries; MyKalmar INSIGHT); booked Q2 2026; delivery Q1 2027; first new-generation electric empty handlers to Latin America per Kalmar; depot in Guarujá near Port of Santos",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.99",
        "lon": "-46.26",
        "geo_note": "Guarujá container depot, Santos hinterland (Kalmar release).",
        "evidence": "documented",
        "source_id": "kalmar_lechman_ech_20260428",
        "note": "Actor: Kalmar (Finnish / Cargotec spin) — allied; buyer Lechman Terminais (Brazilian). Company GlobeNewswire trade press 28 Apr 2026. No contract USD on opened page. Distinct from kalmar_portonave_ers_2026 reachstackers.",
    },
    {
        "id": "kalmar_lechman_ech_2026",
        "retrieved": "2026-10-01",
        "source_id": "kalmar_lechman_ech_20260428",
        "url": "https://www.globenewswire.com/news-release/2026/04/28/3282217/0/en/Kalmar-secured-an-order-of-electric-empty-container-handlers-from-Lechman-Terminais.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Kalmar has secured an order from long-term customer Lechman Terminais in Brazil for six Kalmar electric empty container handlers. The order was booked in Kalmar's Q2 2026 order intake with delivery scheduled for Q1 of 2027.",
        "note": "Opened Kalmar Corporation GlobeNewswire trade press 28 Apr 2026.",
    },
    {
        "id": "kalmar_lechman_ech_20260428",
        "type": "company",
        "chicago": "Kalmar Corporation. “Kalmar secured an order of electric empty container handlers from Lechman Terminais.” 28 April 2026.",
        "url": "https://www.globenewswire.com/news-release/2026/04/28/3282217/0/en/Kalmar-secured-an-order-of-electric-empty-container-handlers-from-Lechman-Terminais.html",
        "annotation": "Company primary on Kalmar electric empty handlers for Lechman Brazil. Supports kalmar_lechman_ech_2026.",
        "supports": ["kalmar_lechman_ech_2026", "hunt_infra_port_cranes"],
    },
)

# 12 resources/copper — NFC Metal completes Raura Peru acquisition
A(
    {
        "id": "nfc_raura_peru_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "NFC Metal Pte. Ltd. (中色股份) — completed ~99.9% acquisition of Compañía Minera Raura (Peru)",
        "country": "Peru",
        "asset": "Closing 17 Apr 2026 (Peru time) of SPA to acquire ~99.9004% of Compañía Minera Raura S.A. from Breca Minería for USD 105,924,416; operating underground Zn-Pb-Ag-Cu skarn polymetallic mine (ACUMULACION RAURA, Oyón, Lima region; ~1 Mtpy / 3,000 tpd; Cu concentrate sales disclosed) + mine hydropower; PRC filings + Peru antitrust cleared; consolidated into NFC Metal parent 中色股份",
        "investment_type": "ownership_equity",
        "value": "105924416",
        "currency": "USD",
        "value_usd": "105924416",
        "fx_usd": "1",
        "fx_date": "2025-12-19",
        "year": "2026",
        "status": "active",
        "lat": "-10.57",
        "lon": "-76.75",
        "geo_note": "Raura mine, Oyón Province, Lima Region, Peru (NFC Metal CNINFO acquisition notices; approximate).",
        "evidence": "documented",
        "source_id": "nfc_raura_completion_20260420",
        "note": "Actor: NFC Metal Pte. Ltd. / China Nonferrous Metal Industry’s Foreign Engineering and Construction Co. (中色股份, PRC) — prc. Company CNINFO completion notice 2026-018 (20 Apr 2026) + prior SPA notice 2025-085 (USD 105.924416m). Zn-primary polymetallic with Cu byproduct/concentrate sales — coded copper subcategory for LatAm Cu-bearing critical-minerals ownership map; note Zn/Pb/Ag co-products. Distinct from Chinalco Toromocho / MMG Las Bambas.",
    },
    {
        "id": "nfc_raura_peru_2026",
        "retrieved": "2026-10-01",
        "source_id": "nfc_raura_completion_20260420",
        "url": "https://static.cninfo.com.cn/finalpage/2026-04-20/1225124242.PDF",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "中色新加坡拟以 10,592.4416 万美元收购 … Compañía Minera Raura S.A. … 约99.9004%股权。 … 秘鲁时间2026 年4 月17 日，本次交易已经完成交割，中色新加坡持有 Raura 公司99.9004%股权",
        "note": "Opened 中色股份 CNINFO PDF announcement 2026-018 (20 Apr 2026).",
    },
    {
        "id": "nfc_raura_completion_20260420",
        "type": "company",
        "chicago": "China Nonferrous Metal Industry’s Foreign Engineering and Construction Co., Ltd. (中色股份). “关于全资子公司收购 Raura 公司股权涉及矿业权投资的进展公告” (Announcement 2026-018). 20 April 2026.",
        "url": "https://static.cninfo.com.cn/finalpage/2026-04-20/1225124242.PDF",
        "annotation": "CNINFO company primary on NFC Metal Raura Peru closing / USD 105.92m. Supports nfc_raura_peru_2026.",
        "supports": ["nfc_raura_peru_2026", "hunt_res_copper"],
    },
)

# 13 resources/niobium — miss (Taboca logged C25; CBMM R$13bn press overlaps prior proxy)
# 14 energy/power_plants_grid — miss (thick)
# 15 energy/fission_smr — miss (CNEN–INVAP / Candu / Meitner already logged)
# 16 infrastructure/building_materials — miss (Votorantim Xambioá logged C25)
# 17 resources/lithium — miss (CUH Arizaro logged C25; Eramet RIGI expansion already logged)
# 18 infrastructure/bridges_roads — miss (OHLA BR-040 logged C25; Silk Road Eixo SP press without openable CVM primary)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]] = full
        else:
            by_id[rid] = len(rows)
            rows.append(full)
        added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            supports = set(existing.get("supports") or [])
            supports.update(bib_entry.get("supports") or [])
            existing["supports"] = sorted(supports)
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    hunt_updates = {
        "hunt_res_nickel": "Cycle 26: equal budget; Centaurus BNDES/Glencore / MMG Anglo already logged (miss).",
        "hunt_energy_other_renewables": "Cycle 26: logged byd_grenergy_central_oasis_2026.",
        "hunt_energy_wind": "Cycle 26: equal budget; Statkraft Emma / Vestas Esquina / Goldwind / Envision already logged (miss).",
        "hunt_energy_solar": "Cycle 26: equal budget; Hanersun Solfácil logged C25; JA Solar Mexico page blocked (miss).",
        "hunt_res_graphite": "Cycle 26: logged south_star_bndes_finep_select_2025.",
        "hunt_res_balsa": "Cycle 26: equal budget; no new named exporter/processor stake beyond WITS years (miss).",
        "hunt_latam_rail_telecom": "Cycle 26: equal budget; CAF Trivia logged C25 (miss).",
        "hunt_infra_engineering_epc": "Cycle 26: equal budget; Worley Diablillos / Bechtel EIMISA already logged (miss).",
        "hunt_res_water": "Cycle 26: equal budget; Techint/Sacyr/Acciona set already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 26: equal budget; APM Callao / ICTSI Aratu / Suape already logged (miss).",
        "hunt_infra_port_cranes": "Cycle 26: logged kalmar_lechman_ech_2026.",
        "hunt_res_copper": "Cycle 26: logged nfc_raura_peru_2026.",
        "hunt_fenb_araxa": "Cycle 26: equal budget; Taboca logged C25; CBMM R$13bn press overlaps prior proxy (miss).",
        "hunt_br_power_equip": "Cycle 26: equal budget; thick grid set (miss).",
        "hunt_energy_fission_smr": "Cycle 26: equal budget; CNEN–INVAP / Candu / Meitner already logged (miss).",
        "hunt_infra_building_materials": "Cycle 26: equal budget; Votorantim Xambioá logged C25 (miss).",
        "hunt_res_lithium": "Cycle 26: equal budget; CUH Arizaro logged C25; Eramet RIGI expansion already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 26: equal budget; OHLA BR-040 logged C25; Silk Road Eixo SP without openable CVM primary (miss).",
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
    print("Cycle 26 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
