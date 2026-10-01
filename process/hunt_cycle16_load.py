#!/usr/bin/env python3
"""Cycle 16 hunt: shuffle_seed=20261016; equal budget across 18 subcategories."""
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


# seed 20261016 order:
# water, niobium, engineering_epc, graphite, port_ownership, balsa, wind, bridges_roads,
# solar, nickel, port_cranes, rail, lithium, other_renewables, copper, fission_smr,
# power_plants_grid, building_materials

# 1 resources/water — Sacyr Coquimbo desalination concession
A(
    {
        "id": "sacyr_coquimbo_desal_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Sacyr Water — Coquimbo desalination plant (first Chilean desal concession)",
        "country": "Chile",
        "asset": "Formalized award for design, financing, construction and operation of Coquimbo human-consumption desalination plant (MOP Concessions); initial 800 l/s expandable to 1,200 l/s; estimated investment ~USD 318 million; serves La Serena/Coquimbo (>540,000 people)",
        "investment_type": "concession",
        "value": "318000000",
        "currency": "USD",
        "value_usd": "318000000",
        "fx_usd": "1",
        "fx_date": "2026-04-14",
        "year": "2026",
        "status": "active",
        "lat": "-29.95",
        "lon": "-71.34",
        "geo_note": "Coquimbo / La Serena region, northern Chile (Sacyr Water release).",
        "evidence": "documented",
        "source_id": "sacyr_coquimbo_20260414",
        "note": "Actor: Sacyr Water (Spanish) — allied. Company 14 Apr 2026 release. Distinct from Cox Rosarito / Acciona Collahuasi / IDE Aconcagua / GS Inima Atacama desal rows.",
    },
    {
        "id": "sacyr_coquimbo_desal_2026",
        "retrieved": "2026-10-01",
        "source_id": "sacyr_coquimbo_20260414",
        "url": "https://sacyr.com/en/-/formalizacion-adjudicacion-desladora-coquimbo-sacyr-agua",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sacyr Water has formalized the award for the design, financing, construction, and operation of the new desalination plant in Coquimbo, located in northern Chile. … This project is the first concessioned desalination project in the country and foresees an estimated investment of $318 million. The desalination plant will have an initial capacity of 800 liters per second (l/s), with the possibility of expanding to 1,200 l/s.",
        "note": "Opened Sacyr corporate release.",
    },
    {
        "id": "sacyr_coquimbo_20260414",
        "type": "official",
        "chicago": "Sacyr. “Sacyr Water formalizes award for Chile’s first concessioned desalination plant.” 14 April 2026.",
        "url": "https://sacyr.com/en/-/formalizacion-adjudicacion-desladora-coquimbo-sacyr-agua",
        "annotation": "Company primary Coquimbo desal concession award. Supports sacyr_coquimbo_desal_2026.",
        "supports": ["sacyr_coquimbo_desal_2026", "hunt_res_water"],
    },
)

# 2 resources/niobium — CBMM / Echion XNO anode plant Araxá
A(
    {
        "id": "cbmm_echion_xno_araxa_2024",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM + Echion Technologies — XNO® niobium anode plant (Araxá)",
        "country": "Brazil",
        "asset": "World’s first volume manufacturing facility for Echion XNO® niobium-based battery anode active material at CBMM Araxá industrial complex; capacity 2,000 tpy XNO (~1 GWh Li-ion cell equivalent); inaugurated Nov 2024",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "CBMM Industrial Complex, Araxá, Minas Gerais (CBMM / Echion releases).",
        "evidence": "documented",
        "source_id": "cbmm_xno_facility_opening_pdf",
        "note": "Actors: CBMM (Brazilian) + Echion Technologies (UK) — allied. Company CBMM English press PDF + Echion news. No plant CAPEX USD on opened CBMM PDF (MG press cites R$2.2bn — not entered). Distinct from cbmm_araxa_presence / capex-plan and CMOC Catalão rows; battery-anode niobium chain.",
    },
    {
        "id": "cbmm_echion_xno_araxa_2024",
        "retrieved": "2026-10-01",
        "source_id": "cbmm_xno_facility_opening_pdf",
        "url": "https://cbmm.com/-/media/cbmm/media-center/noticias-internas/nova-planta-xno/press_release_eng_cbmm-facility-opening.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "CBMM … has officially inaugurated the world’s first volume manufacturing facility dedicated to producing Echion Technologies’ proprietary ultra-fast charging XNO® active anode material technology. The new plant, located in Araxá, Brazil, is the largest Niobium-based anode production facility in the world, capable of producing 2,000 tons per year of XNO®, equivalent to 1 GWh of lithium-ion (Li-ion) cells.",
        "note": "Opened CBMM English press-release PDF.",
    },
    {
        "id": "cbmm_xno_facility_opening_pdf",
        "type": "official",
        "chicago": "CBMM. “CBMM inaugurates world’s largest Niobium anode production facility dedicated to producing Echion’s leading XNO® technology.” Press release PDF, November 2024.",
        "url": "https://cbmm.com/-/media/cbmm/media-center/noticias-internas/nova-planta-xno/press_release_eng_cbmm-facility-opening.pdf",
        "annotation": "Company primary XNO anode plant inauguration. Supports cbmm_echion_xno_araxa_2024.",
        "supports": ["cbmm_echion_xno_araxa_2024", "hunt_fenb_araxa"],
    },
)

# 3 infrastructure/engineering_epc — miss (Sedgman/Lycopodium/M3 logged prior)
# 4 resources/graphite — miss
# 5 infrastructure/port_ownership — miss
# 6 resources/balsa — miss
# 7 energy/wind — miss

# 8 infrastructure/bridges_roads — CCECC Quinto Puente 1A (Ecuador)
A(
    {
        "id": "ccecc_quinto_puente_1a_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Civil Engineering Construction Corporation — Quinto Puente / Viaducto Sur tramo 1A (Guayaquil)",
        "country": "Ecuador",
        "asset": "MIT direct-award of Quinto Puente (Viaducto Sur) section 1A: viaduct over Av. Cacique Tomalá (Guasmo Sur) + grade separations at Av. 25 de Julio; 1,200 calendar days; UNVERIFIED press award USD 115.9 million (Sercop-registered 18 May 2026; contract signature pending per press)",
        "investment_type": "epc",
        "value": "115900000",
        "currency": "USD",
        "value_usd": "115900000",
        "fx_usd": "1",
        "fx_date": "2026-06-03",
        "year": "2026",
        "status": "active",
        "lat": "-2.25",
        "lon": "-79.9",
        "geo_note": "Guasmo Sur / southern Guayaquil port-access corridor (Primicias citing MIT/Sercop).",
        "evidence": "proxy",
        "source_id": "primicias_ccecc_quinto_puente_20260603",
        "note": "Actor: China Civil Engineering Construction Corporation (CCECC) — prc. UNVERIFIED proxy: Primicias 3 Jun 2026 reports MIT award USD 115.9m (Sercop resolution 18 May 2026); notes contract not yet signed. Distinct from CRBC Arequipa–La Joya and CRBC Ecuador Quinindé rows.",
    },
    {
        "id": "ccecc_quinto_puente_1a_2026",
        "retrieved": "2026-10-01",
        "source_id": "primicias_ccecc_quinto_puente_20260603",
        "url": "https://www.primicias.ec/guayaquil/empresa-china-elegida-construccion-quinto-puente-contrato-millonario-sercop-guayas-daniel-noboa-roberto-luque-puertos-guayaquil-124411/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A un costo de USD 115,9 millones, el viceministro Paolo Carpio adjudicó a la contratista China Civil Engineering Construction Corporation este tramo de la obra, que incluye el viaducto sobre la avenida Cacique Tomalá, en el Guasmo Sur, pasos a desnivel en la intersección con la avenida 25 de Julio … La obra tiene un plazo de ejecución de 1.200 días … según la resolución de la adjudicación del 18 de mayo del 2026, registrada en … Sercop",
        "note": "Opened Primicias award report (Sercop primary acta not opened this cycle).",
    },
    {
        "id": "primicias_ccecc_quinto_puente_20260603",
        "type": "press",
        "chicago": "Primicias. “Empresa china, la elegida para construir tramo 1A del Quinto Puente, por USD 115,9 millones.” 3 June 2026.",
        "url": "https://www.primicias.ec/guayaquil/empresa-china-elegida-construccion-quinto-puente-contrato-millonario-sercop-guayas-daniel-noboa-roberto-luque-puertos-guayaquil-124411/",
        "annotation": "Ecuador press on MIT/Sercop CCECC Quinto Puente 1A award. Supports ccecc_quinto_puente_1a_2026 (UNVERIFIED value).",
        "supports": ["ccecc_quinto_puente_1a_2026", "hunt_infra_bridges_roads"],
    },
)

# 9 energy/solar — miss
# 10 resources/nickel — miss (Centaurus BNDES/Glencore logged C15)
# 11 infrastructure/port_cranes — miss
# 12 infrastructure/rail — miss (PowerChina Chancay press uncorroborated)
# 13 resources/lithium — miss
# 14 energy/other_renewables — miss
# 15 resources/copper — miss
# 16 energy/fission_smr — miss
# 17 energy/power_plants_grid — miss
# 18 infrastructure/building_materials — miss (CSN sale not closed; Pacasmayo already logged)


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
        "hunt_res_water": "Cycle 16: logged sacyr_coquimbo_desal_2026.",
        "hunt_fenb_araxa": "Cycle 16: logged cbmm_echion_xno_araxa_2024.",
        "hunt_infra_engineering_epc": "Cycle 16: equal budget; Sedgman/Lycopodium/M3 logged prior (miss).",
        "hunt_res_graphite": "Cycle 16: equal budget; Graphcoa/South Star already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 16: equal budget; APM Callao Stage 3B logged C14 (miss).",
        "hunt_res_balsa": "Cycle 16: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_energy_wind": "Cycle 16: equal budget; Vestas Esquina / Goldwind Sento Sé logged C14 (miss).",
        "hunt_infra_bridges_roads": "Cycle 16: logged ccecc_quinto_puente_1a_2026.",
        "hunt_energy_solar": "Cycle 16: equal budget; thick set — miss.",
        "hunt_res_nickel": "Cycle 16: equal budget; Centaurus BNDES/Glencore logged C15 (miss).",
        "hunt_infra_port_cranes": "Cycle 16: equal budget; ZPMC Tecon Rio Grande logged C15 (miss).",
        "hunt_latam_rail_telecom": "Cycle 16: equal budget; PowerChina Chancay rail press uncorroborated (miss).",
        "hunt_res_lithium": "Cycle 16: equal budget; Ganfeng LAAC convertible logged C14 (miss).",
        "hunt_energy_other_renewables": "Cycle 16: equal budget; Acciona La Gina / Ormat Dominica logged C12 (miss).",
        "hunt_res_copper": "Cycle 16: equal budget; no new copper beyond FCX/FQM/Teck/Chinalco (miss).",
        "hunt_energy_fission_smr": "Cycle 16: equal budget; Meitner/FIRST/CAREM/Brazil microreactor already logged (miss).",
        "hunt_br_power_equip": "Cycle 16: equal budget; thick subcategory — miss.",
        "hunt_infra_building_materials": "Cycle 16: equal budget; CSN Cimentos sale not closed; Pacasmayo already logged (miss).",
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
    print("Cycle 16 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
