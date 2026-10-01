#!/usr/bin/env python3
"""Cycle 13 hunt: shuffle_seed=20261013; equal budget across 18 subcategories."""
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


# seed 20261013 order:
# fission_smr, rail, other_renewables, engineering_epc, copper, building_materials,
# water, bridges_roads, port_ownership, wind, balsa, nickel, power_plants_grid,
# port_cranes, lithium, graphite, niobium, solar

# 1 energy/fission_smr — miss (FIRST / Brazil microreactor already logged)
# 2 infrastructure/rail — miss (PowerChina Chancay–Sierra Central press-only / IRJ Cloudflare)
# 3 energy/other_renewables — miss (La Gina / Ormat Dominica logged C12)
# 4 infrastructure/engineering_epc — miss
# 5 resources/copper — miss

# 6 infrastructure/building_materials — Heidelberg Cementos Inka Peru
A(
    {
        "id": "heidelberg_cementos_inka_peru_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Heidelberg Materials — 70% majority stake in Cementos Inka (Peru)",
        "country": "Peru",
        "asset": "Binding agreement for 70% of Caliza Cemento Inca S.A. (Cementos Inka): two grinding units ~1.3 Mtpa combined near Lima and Pisco + two ready-mix plants; asset-light import/grind model; close targeted by October 2026; financial terms undisclosed",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.05",
        "lon": "-77.04",
        "geo_note": "Lima / Pisco grinding footprint (Heidelberg Materials release).",
        "evidence": "documented",
        "source_id": "heidelberg_inka_20260908",
        "note": "Actor: Heidelberg Materials (German) — allied. Company 8 Sep 2026 release. Distinct from Holcim Pacasmayo / Comacsa / Cemex Colombia building-materials rows. No purchase price on opened page (EBITDA multiple ~6× noted without absolute USD).",
    },
    {
        "id": "heidelberg_cementos_inka_peru_2026",
        "retrieved": "2026-10-01",
        "source_id": "heidelberg_inka_20260908",
        "url": "https://www.heidelbergmaterials.com/en/pr-2026-09-08",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Heidelberg Materials has entered into a binding agreement to acquire a 70% majority stake in Cementos Inka, a family-owned cement producer in Peru. … The company operates two grinding units with a combined annual capacity of 1.3 million tonnes, as well as two ready-mixed concrete plants. Its state-of-the-art production sites are strategically located near Lima and Pisco",
        "note": "Opened Heidelberg Materials press release.",
    },
    {
        "id": "heidelberg_inka_20260908",
        "type": "official",
        "chicago": "Heidelberg Materials. “Expanding its trading operations with asset-light acquisition: Heidelberg Materials takes majority stake in Peru-based Cementos Inka.” 8 September 2026.",
        "url": "https://www.heidelbergmaterials.com/en/pr-2026-09-08",
        "annotation": "Company primary on Cementos Inka 70% stake. Supports heidelberg_cementos_inka_peru_2026.",
        "supports": ["heidelberg_cementos_inka_peru_2026", "hunt_infra_building_materials"],
    },
)

# 7 resources/water — Cox Rosarito desalination EPC
A(
    {
        "id": "cox_rosarito_desal_mexico_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Cox — Rosarito seawater desalination plant Phase 1 EPC (Conagua)",
        "country": "Mexico",
        "asset": "Public-tender award to build Rosarito (Baja California) SWRO plant; Phase 1 2,200 l/s (~190 million litres/day); final design capacity 4,400 l/s; company states US$304 million investment; ~3-year construction; National Water Plan priority for Tijuana/Playas de Rosarito",
        "investment_type": "epc",
        "value": "304000000",
        "currency": "USD",
        "value_usd": "304000000",
        "fx_usd": "1",
        "fx_date": "2026-08-18",
        "year": "2026",
        "status": "active",
        "lat": "32.33",
        "lon": "-117.05",
        "geo_note": "Playas de Rosarito / SW Tijuana, Baja California (Cox release).",
        "evidence": "documented",
        "source_id": "cox_rosarito_20260818",
        "note": "Actor: Cox (Spain) — allied. Company 18 Aug 2026 release citing Conagua public tender award and US$304m. Distinct from Acciona Los Cabos / Collahuasi / IDE desal rows.",
    },
    {
        "id": "cox_rosarito_desal_mexico_2026",
        "retrieved": "2026-10-01",
        "source_id": "cox_rosarito_20260818",
        "url": "https://grupocox.com/en/cox-to-build-latin-americas-largest-desalination-plant-in-mexico-304-million-project/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Cox … has been awarded, through a public tender process, the construction of the Rosarito desalination plant in Baja California, Mexico. The project, promoted by the National Water Commission (Conagua), represents an investment of US$304 million … The first phase of the project includes the construction of a desalination plant with the capacity to treat 2,200 litres per second",
        "note": "Opened Cox corporate release.",
    },
    {
        "id": "cox_rosarito_20260818",
        "type": "official",
        "chicago": "Cox. “Cox to build Latin America’s largest desalination plant in Mexico, a $304 million project.” 18 August 2026.",
        "url": "https://grupocox.com/en/cox-to-build-latin-americas-largest-desalination-plant-in-mexico-304-million-project/",
        "annotation": "Company primary Rosarito desal award. Supports cox_rosarito_desal_mexico_2026.",
        "supports": ["cox_rosarito_desal_mexico_2026", "hunt_res_water"],
    },
)

# 8 infrastructure/bridges_roads — CRBC Arequipa–La Joya Componente III
A(
    {
        "id": "crbc_arequipa_la_joya_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Consorcio Ejecutor La Joya (CRBC Perú + Integral Consultores) — Arequipa–La Joya Componente III",
        "country": "Peru",
        "asset": "Obras por Impuestos award for Vía Regional Arequipa–La Joya Componente III (Km 0+000–24+540, Cerro Colorado–La Joya); 570 calendar days; UNVERIFIED press award amount S/ 408,766,344.91",
        "investment_type": "epc",
        "value": "408766344.91",
        "currency": "PEN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-16.35",
        "lon": "-71.7",
        "geo_note": "Cerro Colorado–La Joya corridor, Arequipa region (Diario El Pueblo reporting MTC/Provías award).",
        "evidence": "proxy",
        "source_id": "elpueblo_arequipa_la_joya_20260702",
        "note": "Actor: China Road and Bridge Corporation (CRBC) Sucursal del Perú in Consorcio Ejecutor La Joya — prc. UNVERIFIED proxy: Diario El Pueblo 2 Jul 2026 reports MTC buena pro process 01-2026-MTC/21-OXI at S/ 408,766,344.91 (vs S/ 371.6m reference). Gob.pe RD opened only for bases approval, not award acta. Distinct from CRBC Ecuador Quinindé.",
    },
    {
        "id": "crbc_arequipa_la_joya_2026",
        "retrieved": "2026-10-01",
        "source_id": "elpueblo_arequipa_la_joya_20260702",
        "url": "https://diarioelpueblo.com.pe/2026/07/02/mtc-adjudica-componente-iii-de-via-arequipa-la-joya-a-empresa-con-antecedentes-internacionales/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "el Ministerio de Transportes y Comunicaciones (MTC) otorgó la buena pro para la ejecución del componente III de la vía Arequipa–La Joya al Consorcio Ejecutor La Joya, integrado por Integral Consultores S.A.C. y China Road and Bridge Corporation (CRBC) Sucursal del Perú … la buena pro fue adjudicada por S/ 408 766 344,91 … plazo de 570 días calendario",
        "note": "Opened Diario El Pueblo award report (MTC award PDF not opened this cycle).",
    },
    {
        "id": "elpueblo_arequipa_la_joya_20260702",
        "type": "press",
        "chicago": "Diario El Pueblo (Arequipa). “MTC adjudica componente III de vía Arequipa–La Joya a empresa con antecedentes internacionales.” 2 July 2026.",
        "url": "https://diarioelpueblo.com.pe/2026/07/02/mtc-adjudica-componente-iii-de-via-arequipa-la-joya-a-empresa-con-antecedentes-internacionales/",
        "annotation": "Local press report of MTC/Provías OxI award to CRBC consortium. Supports crbc_arequipa_la_joya_2026 (UNVERIFIED value).",
        "supports": ["crbc_arequipa_la_joya_2026", "hunt_infra_bridges_roads"],
    },
)

# 9 infrastructure/port_ownership — miss
# 10 energy/wind — miss
# 11 resources/balsa — miss
# 12 resources/nickel — miss
# 13 energy/power_plants_grid — miss
# 14 infrastructure/port_cranes — miss
# 15 resources/lithium — miss
# 16 resources/graphite — miss
# 17 resources/niobium — miss
# 18 energy/solar — miss


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
        "hunt_energy_fission_smr": "Cycle 13: equal budget; FIRST / Brazil microreactor already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 13: equal budget; PowerChina Chancay–Sierra Central press-only / IRJ Cloudflare (miss).",
        "hunt_energy_other_renewables": "Cycle 13: equal budget; Acciona La Gina / Ormat Dominica logged C12 (miss).",
        "hunt_infra_engineering_epc": "Cycle 13: equal budget; no new non-grid EPC beyond Worley Diablillos (miss).",
        "hunt_res_copper": "Cycle 13: equal budget; no new copper beyond FCX/FQM/Teck/Chinalco (miss).",
        "hunt_infra_building_materials": "Cycle 13: logged heidelberg_cementos_inka_peru_2026.",
        "hunt_res_water": "Cycle 13: logged cox_rosarito_desal_mexico_2026.",
        "hunt_infra_bridges_roads": "Cycle 13: logged crbc_arequipa_la_joya_2026.",
        "hunt_infra_port_ownership": "Cycle 13: equal budget; no new port ownership beyond APM/Hutchison/DP World/ICTSI (miss).",
        "hunt_energy_wind": "Cycle 13: equal budget; no new OEM beyond Vestas/Goldwind/Nordex/Envision (miss).",
        "hunt_res_balsa": "Cycle 13: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_nickel": "Cycle 13: equal budget; no distinct new Ni beyond IFC/Appian Santa Rita (miss).",
        "hunt_br_power_equip": "Cycle 13: equal budget; thick subcategory — miss.",
        "hunt_infra_port_cranes": "Cycle 13: equal budget; Konecranes Cartagena logged C12 (miss).",
        "hunt_res_lithium": "Cycle 13: equal budget; POSCO Sal de Oro II / Zijin RIGI logged prior (miss).",
        "hunt_res_graphite": "Cycle 13: equal budget; South Star PO logged C12 (miss).",
        "hunt_fenb_araxa": "Cycle 13: equal budget; no new FeNb beyond CBMM/CMOC (miss).",
        "hunt_energy_solar": "Cycle 13: equal budget; thick set — miss.",
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
    print("Cycle 13 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
