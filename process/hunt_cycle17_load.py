#!/usr/bin/env python3
"""Cycle 17 hunt: shuffle_seed=20261017; equal budget across 18 subcategories."""
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


# seed 20261017 order:
# balsa, power_plants_grid, wind, niobium, bridges_roads, water, building_materials,
# engineering_epc, nickel, fission_smr, other_renewables, lithium, port_cranes, graphite,
# rail, solar, port_ownership, copper

# 1 resources/balsa — miss
# 2 energy/power_plants_grid — miss (Hitachi Dosquebradas / Brazil xfmr already logged)
# 3 energy/wind — miss
# 4 resources/niobium — miss (CBMM XNO logged C16)
# 5 infrastructure/bridges_roads — miss (CCECC Quinto Puente logged C16)
# 6 resources/water — miss (Sacyr Coquimbo logged C16)
# 7 infrastructure/building_materials — miss (CSN Cimentos sale not closed)
# 8 infrastructure/engineering_epc — miss
# 9 resources/nickel — miss

# 10 energy/fission_smr — Nuclearis N1 microreactor licensing (Argentina design / US path)
A(
    {
        "id": "nuclearis_n1_smr_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "Nuclearis — N1 17 MWe microreactor (Argentine design; US patent/NRC path)",
        "country": "Argentina",
        "asset": "N1 pressurized-water microreactor (~17 MWe); US patent sought H1 2026; initial NRC filing; engineering in Argentina; FOAK targeted US or Argentina; UNVERIFIED press FOAK investment estimate US$600 million (CEO interview)",
        "investment_type": "other",
        "value": "600000000",
        "currency": "USD",
        "value_usd": "600000000",
        "fx_usd": "1",
        "fx_date": "2026-01-01",
        "year": "2026",
        "status": "active",
        "lat": "-34.6",
        "lon": "-58.38",
        "geo_note": "Nuclearis HQ / Argentina program pin Buenos Aires (EconoJournal interview); FOAK site not fixed.",
        "evidence": "proxy",
        "source_id": "econojournal_nuclearis_n1_2026",
        "note": "Actor: Nuclearis (Argentine) with Nuclearis Energy US licensing vehicle — coded other (host design). UNVERIFIED proxy: EconoJournal interview with CEO Santiago Badran on USPTO patent, NRC initial filing, and US$600m FOAK estimate. Distinct from CAREM/Meitner ACR-300/FIRST/Brazil microreactor rows. Pre-construction.",
    },
    {
        "id": "nuclearis_n1_smr_2026",
        "retrieved": "2026-10-01",
        "source_id": "econojournal_nuclearis_n1_2026",
        "url": "https://econojournal.com.ar/energia/nuclearis-microrreactor-argentino/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Nuclearis … espera obtener en los próximos meses en los EE.UU. la patente definitiva del N1, un reactor modular micro de 17 MW eléctricos. … ya han presentado formalmente la inscripción inicial [ante la NRC]. La inversión estimada para llegar a un first of a kind (FOAK) … asciende a los US$ 600 millones. … “La ingeniería se hará íntegramente en Argentina. Mi ambición es por lo menos el primer FOAK instalarlo en nuestro país,” dijo.",
        "note": "Opened EconoJournal interview/report (company primary not opened this cycle).",
    },
    {
        "id": "econojournal_nuclearis_n1_2026",
        "type": "press",
        "chicago": "EconoJournal. “Nuclearis avanza hacia el licenciamiento de su microrreactor nuclear de diseño argentino.” 2026.",
        "url": "https://econojournal.com.ar/energia/nuclearis-microrreactor-argentino/",
        "annotation": "Trade press interview on Nuclearis N1 US patent/NRC path and FOAK CAPEX estimate. Supports nuclearis_n1_smr_2026 (UNVERIFIED value).",
        "supports": ["nuclearis_n1_smr_2026", "hunt_energy_fission_smr"],
    },
)

# 11 energy/other_renewables — miss
# 12 resources/lithium — miss
# 13 infrastructure/port_cranes — miss
# 14 resources/graphite — miss (Nacional/South Star/Graphcoa already logged)

# 15 infrastructure/rail — Hitachi Energy power supply for Trívia Trens SP Lines 11–13
A(
    {
        "id": "hitachi_trivia_sp_metro_power_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Hitachi Energy — power supply for Trívia Trens Lines 11/12/13 (São Paulo)",
        "country": "Brazil",
        "asset": "Contract with Trívia Trens (Comporte) to supply high-voltage grid connections + DC rail power infrastructure (rectifiers, DC switchgear) for Metropolitan Trains Lines 11-Coral, 12-Safira, 13-Jade (Alto Tietê Lot); serves ~1.3m daily passengers; Hitachi contract USD not disclosed (concession modernization cited ~USD 2.66bn / R$14.3bn over 25 years — not Hitachi package)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "São Paulo metropolitan train Lines 11/12/13 / Alto Tietê Lot (Hitachi Energy feature).",
        "evidence": "documented",
        "source_id": "hitachi_trivia_trens_202601",
        "note": "Actor: Hitachi Energy — allied; customer Trívia Trens (Brazilian). Company Jan 2026 feature. Distinct from Siemens SP Line 4 CBTC / Alstom SP Line 6 / CRRC Salvador rail rows. No Hitachi contract USD on page.",
    },
    {
        "id": "hitachi_trivia_sp_metro_power_2026",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_trivia_trens_202601",
        "url": "https://www.hitachienergy.com/us/en/news-and-events/features/2026/01/hitachi-energy-and-tr-via-trens-to-modernize-the-railway-electrical-network-improving-daily-travel-for-1-3-million-commuters-in-brazil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Hitachi Energy … has signed a contract with rail concessionaire Trívia Trens (Comporte Group) to provide power supply for Lines 11, 12, and 13 of the Metropolitan Trains … Hitachi Energy’s scope encompasses high-voltage grid connections and a range of direct current (DC) electrical infrastructure solutions, including rectifiers and DC switchgear",
        "note": "Opened Hitachi Energy company feature.",
    },
    {
        "id": "hitachi_trivia_trens_202601",
        "type": "official",
        "chicago": "Hitachi Energy. “Hitachi Energy and Trívia Trens to modernize the railway electrical network, improving daily travel for 1.3 million commuters in Brazil.” January 2026.",
        "url": "https://www.hitachienergy.com/us/en/news-and-events/features/2026/01/hitachi-energy-and-tr-via-trens-to-modernize-the-railway-electrical-network-improving-daily-travel-for-1-3-million-commuters-in-brazil",
        "annotation": "Company primary Trívia Trens rail power-supply contract. Supports hitachi_trivia_sp_metro_power_2026.",
        "supports": ["hitachi_trivia_sp_metro_power_2026", "hunt_latam_rail_telecom"],
    },
)

# 16 energy/solar — miss
# 17 infrastructure/port_ownership — miss
# 18 resources/copper — miss (Cerro Verde extension press-only / FCX primary not opened)


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
        "hunt_res_balsa": "Cycle 17: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_br_power_equip": "Cycle 17: equal budget; Hitachi Dosquebradas / Brazil xfmr already logged (miss).",
        "hunt_energy_wind": "Cycle 17: equal budget; Vestas Esquina / Goldwind Sento Sé logged C14 (miss).",
        "hunt_fenb_araxa": "Cycle 17: equal budget; CBMM XNO anode plant logged C16 (miss).",
        "hunt_infra_bridges_roads": "Cycle 17: equal budget; CCECC Quinto Puente logged C16 (miss).",
        "hunt_res_water": "Cycle 17: equal budget; Sacyr Coquimbo logged C16 (miss).",
        "hunt_infra_building_materials": "Cycle 17: equal budget; CSN Cimentos sale not closed; Cementir–Votorantim offer lapsed (miss).",
        "hunt_infra_engineering_epc": "Cycle 17: equal budget; Sedgman/Lycopodium/M3 logged prior (miss).",
        "hunt_res_nickel": "Cycle 17: equal budget; Centaurus BNDES/Glencore logged C15 (miss).",
        "hunt_energy_fission_smr": "Cycle 17: logged nuclearis_n1_smr_2026.",
        "hunt_energy_other_renewables": "Cycle 17: equal budget; Acciona La Gina / Ormat Dominica logged C12 (miss).",
        "hunt_res_lithium": "Cycle 17: equal budget; Ganfeng LAAC convertible logged C14 (miss).",
        "hunt_infra_port_cranes": "Cycle 17: equal budget; ZPMC Tecon Rio Grande logged C15 (miss).",
        "hunt_res_graphite": "Cycle 17: equal budget; Nacional/South Star/Graphcoa already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 17: logged hitachi_trivia_sp_metro_power_2026.",
        "hunt_energy_solar": "Cycle 17: equal budget; thick set — miss.",
        "hunt_infra_port_ownership": "Cycle 17: equal budget; APM Callao Stage 3B logged C14 (miss).",
        "hunt_res_copper": "Cycle 17: equal budget; Cerro Verde life-extension press without FCX/Senace primary opened (miss).",
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
    print("Cycle 17 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
