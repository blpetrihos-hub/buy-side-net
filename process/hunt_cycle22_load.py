#!/usr/bin/env python3
"""Cycle 22 hunt: shuffle_seed=20261022; equal budget across 18 subcategories."""
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


# seed 20261022 order (canonical BRIEF list):
# building_materials, niobium, graphite, lithium, wind, port_cranes, power_plants_grid,
# rail, copper, solar, other_renewables, water, bridges_roads, fission_smr,
# port_ownership, engineering_epc, nickel, balsa

# 1 infrastructure/building_materials — Holcim completes Pacasmayo majority stake
A(
    {
        "id": "holcim_pacasmayo_complete_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim — completed majority stake acquisition of Cementos Pacasmayo (Peru)",
        "country": "Peru",
        "asset": "Completion of majority-stake acquisition of Cementos Pacasmayo (~5 Mtpy cement across three plants + 28 ready-mix/precast; 2025 net sales USD 630m; 7.1x 2025 EBITDA multiple after ~USD 40m year-three synergies stated); mandatory tender offer for additional shares planned under Peruvian law",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-7.4",
        "lon": "-79.55",
        "geo_note": "Pacasmayo cement operations, northern Peru (Holcim completion release).",
        "evidence": "documented",
        "source_id": "holcim_pacasmayo_completion_pr_2026",
        "note": "Actor: Holcim (Swiss) — allied. Company completion release. Closing consideration not restated as a single USD figure on opened page (prior agreement row holcim_pacasmayo_peru_2025 carried ~USD 1.5bn EV on 100% basis) — value blank here. Distinct completion event from agreement announcement.",
    },
    {
        "id": "holcim_pacasmayo_complete_2026",
        "retrieved": "2026-10-01",
        "source_id": "holcim_pacasmayo_completion_pr_2026",
        "url": "https://www.holcim.com/media/media-releases/holcim-completes-acquisition-majority-stake-cementos-pacasmayo",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Holcim has completed the acquisition of a majority stake in Cementos Pacasmayo, a leading Peruvian producer of building materials with reported 2025 net sales of USD 630 million and an adjusted EBITDA margin of 28%. … The transaction value implies a 2025 EBITDA multiple of 7.1x after expected run-rate synergies of around USD 40 million realized in year three.",
        "note": "Opened Holcim company media release (completion).",
    },
    {
        "id": "holcim_pacasmayo_completion_pr_2026",
        "type": "company",
        "chicago": "Holcim. “Holcim completes acquisition of majority stake in Cementos Pacasmayo.” Media release, 2026.",
        "url": "https://www.holcim.com/media/media-releases/holcim-completes-acquisition-majority-stake-cementos-pacasmayo",
        "annotation": "Company primary on Pacasmayo majority-stake completion. Supports holcim_pacasmayo_complete_2026.",
        "supports": ["holcim_pacasmayo_complete_2026", "hunt_infra_building_materials"],
    },
)

# 2 resources/niobium — miss (CBMM R$13bn plan press-only / prior R$10bn proxy exists)
# 3 resources/graphite — miss

# 4 resources/lithium — Eramet Centenario brownfield expansion / RIGI (pre-FID)
A(
    {
        "id": "eramet_centenario_rigi_exp_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Eramet — Centenario-Ratones brownfield expansion PFS / planned RIGI application (Salta)",
        "country": "Argentina",
        "asset": "Pre-feasibility brownfield expansion adding 11 kt-LCE/year to existing 24 kt-LCE nameplate; potential additional investment ~USD 350 million subject to FID (possible by end-2027); planned RIGI application; plant reached ~90% nameplate in June 2026",
        "investment_type": "expansion_pfs",
        "value": "350000000",
        "currency": "USD",
        "value_usd": "350000000",
        "fx_usd": "1",
        "fx_date": "2026-10-01",
        "year": "2026",
        "status": "active",
        "lat": "-24.1",
        "lon": "-66.6",
        "geo_note": "Centenario-Ratones salar, Salta Province (Eramet release).",
        "evidence": "documented",
        "source_id": "eramet_centenario_rigi_20261001",
        "note": "Actor: Eramet (French) — allied. Company 1 Oct 2026 news. Pre-FID / subject to final investment decision. Distinct from eramet_centenario_phase1_2024 (Phase 1 ~USD 870m inauguration) and Rio Tinto Rincon financing rows.",
    },
    {
        "id": "eramet_centenario_rigi_exp_2026",
        "retrieved": "2026-10-01",
        "source_id": "eramet_centenario_rigi_20261001",
        "url": "https://www.eramet.com/en/news/eramet-plans-to-apply-under-argentinas-large-investment-incentive-regime-rigi-for-a-first-expansion-of-centenario-ratones/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The contemplated expansion would add 11 kt-LCE per year of lithium carbonate production capacity, on top of the existing 24 kt-LCE annual nameplate capacity. The project would represent a potential additional investment of around US$350 million, subject to final investment decision … A final investment decision could be made by end-2027",
        "note": "Opened Eramet English company news 1 Oct 2026.",
    },
    {
        "id": "eramet_centenario_rigi_20261001",
        "type": "company",
        "chicago": "Eramet. “Eramet plans to apply under Argentina’s Large Investment Incentive Regime (RIGI) for a first expansion of Centenario-Ratones.” 1 October 2026.",
        "url": "https://www.eramet.com/en/news/eramet-plans-to-apply-under-argentinas-large-investment-incentive-regime-rigi-for-a-first-expansion-of-centenario-ratones/",
        "annotation": "Company primary on Centenario brownfield expansion / RIGI intent. Supports eramet_centenario_rigi_exp_2026.",
        "supports": ["eramet_centenario_rigi_exp_2026", "hunt_res_lithium"],
    },
)

# 5 energy/wind — Statkraft Emma 72 MW Peru (first wind in portfolio)
A(
    {
        "id": "statkraft_emma_peru_72mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Statkraft Peru — Emma 72 MW wind project (Piura)",
        "country": "Peru",
        "asset": "Construction of 72 MW Emma wind farm in Piura; expected ~325 GWh/year and capacity factors >50%; Statkraft’s first wind investment in Peru (adds to hydro + Lupi solar pipeline)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-5.2",
        "lon": "-80.6",
        "geo_note": "Piura region, northern Peru (Statkraft release; approximate).",
        "evidence": "documented",
        "source_id": "statkraft_emma_peru_20260630",
        "note": "Actor: Statkraft (Norwegian state-owned) — allied. Company 30 Jun 2026 newsroom. No CAPEX USD on opened page. Vestas later announced as turbine OEM in separate Vestas order listing (not entered as duplicate OEM row this cycle). Distinct from Vestas Esquina do Vento Brazil / Chile 128 MW rows.",
    },
    {
        "id": "statkraft_emma_peru_72mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "statkraft_emma_peru_20260630",
        "url": "https://www.statkraft.com/newsroom/news-and-stories/2026/statkraft-adds-first-wind-project-to-its-renewable-portfolio-in-peru/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Statkraft … is expanding its renewable energy portfolio in Peru with the construction of the high-performing 72 MW Emma wind project in Piura. The project marks Statkraft’s first investment in wind power in the country … The project is expected to have an annual energy production of 325 GWh and achieve capacity factors above 50 percent",
        "note": "Opened Statkraft company newsroom 30 Jun 2026.",
    },
    {
        "id": "statkraft_emma_peru_20260630",
        "type": "company",
        "chicago": "Statkraft. “Statkraft adds first wind project to its renewable portfolio in Peru.” 30 June 2026.",
        "url": "https://www.statkraft.com/newsroom/news-and-stories/2026/statkraft-adds-first-wind-project-to-its-renewable-portfolio-in-peru/",
        "annotation": "Company primary on Emma 72 MW wind FID/construction in Peru. Supports statkraft_emma_peru_72mw_2026.",
        "supports": ["statkraft_emma_peru_72mw_2026", "hunt_energy_wind"],
    },
)

# 6 infrastructure/port_cranes — miss (Cartagena / MultiRio / Aracruz already logged)
# 7 energy/power_plants_grid — State Grid NE Brazil UHVDC construction start
A(
    {
        "id": "state_grid_ne_uhv_construction_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "prc",
        "counterpart": "State Grid Brazil Holding — ±800 kV Northeast Brazil UHVDC (Graça Aranha–Silvânia)",
        "country": "Brazil",
        "asset": "All-around construction start (24 Jun 2026) of 1,468 km ±800 kV / 5 GW UHVDC line + converter stations (Maranhão–Tocantins–Goiás–Minas Gerais corridor); 30-year franchise; COD targeted 2029; third overseas UHV project for State Grid after Belo Monte I/II",
        "investment_type": "concession_construction",
        "value": "",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-16.66",
        "lon": "-48.61",
        "geo_note": "Silvânia (GO) receiving-end converter area pin (SASAC / project corridor).",
        "evidence": "documented",
        "source_id": "sasac_state_grid_ne_uhv_20260706",
        "note": "Actor: State Grid Brazil Holding (PRC SOE subsidiary) — prc. SASAC English release 6 Jul 2026. CAPEX left blank (press R$23bn / NDB BRL 20.2bn figures not opened as primary PDF here). Distinct from excluded RAP auction row aneel_state_grid_rap_2023 and XD converter-transformer one_sided equipment row. Construction milestone for franchise build-own-operate.",
    },
    {
        "id": "state_grid_ne_uhv_construction_2026",
        "retrieved": "2026-10-01",
        "source_id": "sasac_state_grid_ne_uhv_20260706",
        "url": "http://en.sasac.gov.cn/2026/07/06/c_20881.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Construction of the ±800 kilovolt ultra-high-voltage direct-current electricity transmission project in northeastern Brazil began on June 24. The UHVDC electricity transmission project is solely invested, built and operated by State Grid Brazil Holding S.A. … The UHVDC electricity transmission project has a 1,468-kilometer transmission line … rated transmission capacity of 5 gigawatts",
        "note": "Opened SASAC English release 6 Jul 2026.",
    },
    {
        "id": "sasac_state_grid_ne_uhv_20260706",
        "type": "government",
        "chicago": "China. State-owned Assets Supervision and Administration Commission. “State Grid Begins Construction on UHVDC Electricity Transmission Project in Northeast Brazil.” 6 July 2026.",
        "url": "http://en.sasac.gov.cn/2026/07/06/c_20881.htm",
        "annotation": "Official SASAC English notice of State Grid Brazil NE UHVDC construction start. Supports state_grid_ne_uhv_construction_2026.",
        "supports": ["state_grid_ne_uhv_construction_2026", "hunt_br_power_equip"],
    },
)

# 8 infrastructure/rail — miss
# 9 resources/copper — miss
# 10 energy/solar — miss
# 11 energy/other_renewables — miss (Celda Solar logged C21)
# 12 resources/water — miss
# 13 infrastructure/bridges_roads — miss (Salvador–Itaparica logged C21)
# 14 energy/fission_smr — miss
# 15 infrastructure/port_ownership — miss
# 16 infrastructure/engineering_epc — miss (STRACON logged C21)

# 17 resources/nickel — BNDES R$100m machines financing for Piauí Níquel
A(
    {
        "id": "bndes_piaui_nickel_maq_100m_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "BNDES Máquinas e Serviços — R$100 million financing to Piauí Níquel Metais (Brazilian Nickel)",
        "country": "Brazil",
        "asset": "Approved BNDES financing of R$100 million for machines/equipment/services to support high-purity Ni/Co precipitate (MHP) production at Capitão Gervásio Oliveira (PI); selected under BNDES–Finep strategic minerals call; project targets 27,000 t Ni + 900 t Co/year with production start 2028",
        "investment_type": "financing",
        "value": "100000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.1",
        "lon": "-42.5",
        "geo_note": "Capitão Gervásio Oliveira, Piauí (BNDES release).",
        "evidence": "documented",
        "source_id": "bndes_piaui_niquel_20260713",
        "note": "Actors: Piauí Níquel Metais (wholly owned by UK-domiciled Brazilian Nickel Limited) borrower — allied; lender BNDES. Official BNDES Agência 13 Jul 2026. Distinct from brazilian_nickel_dfc_loi_2024 (U.S. DFC LOI up to USD 550m) and Centaurus Jaguar BNDES LOI. Value stored as BRL (no FX).",
    },
    {
        "id": "bndes_piaui_nickel_maq_100m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bndes_piaui_niquel_20260713",
        "url": "https://agenciadenoticias.bndes.gov.br/noticia/BNDES-aprova-R$-100-mi-para-apoiar-processamento-de-niquel-no-Piaui/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "O Banco Nacional de Desenvolvimento Econômico e Social (BNDES) aprovou financiamento no valor de R$ 100 milhões para a Piauí Níquel Metais S/A adquirir máquinas, equipamentos ou serviços industriais para apoiar a produção de precipitados de níquel e cobalto de alta pureza, em Capitão Gervásio Oliveira (PI)",
        "note": "Opened BNDES official news agency page 13 Jul 2026.",
    },
    {
        "id": "bndes_piaui_niquel_20260713",
        "type": "government",
        "chicago": "Banco Nacional de Desenvolvimento Econômico e Social. “BNDES aprova R$ 100 mi para apoiar processamento de níquel no Piauí.” Agência BNDES de Notícias, 13 July 2026.",
        "url": "https://agenciadenoticias.bndes.gov.br/noticia/BNDES-aprova-R$-100-mi-para-apoiar-processamento-de-niquel-no-Piaui/",
        "annotation": "Official BNDES financing approval for Piauí Níquel Metais. Supports bndes_piaui_nickel_maq_100m_2026.",
        "supports": ["bndes_piaui_nickel_maq_100m_2026", "hunt_res_nickel"],
    },
)

# 18 resources/balsa — miss


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
        "hunt_infra_building_materials": "Cycle 22: logged holcim_pacasmayo_complete_2026.",
        "hunt_fenb_araxa": "Cycle 22: equal budget; CBMM R$13bn plan press-only / prior R$10bn proxy exists (miss).",
        "hunt_res_graphite": "Cycle 22: equal budget; Graphcoa Jordânia / South Star set already logged (miss).",
        "hunt_res_lithium": "Cycle 22: logged eramet_centenario_rigi_exp_2026.",
        "hunt_energy_wind": "Cycle 22: logged statkraft_emma_peru_72mw_2026.",
        "hunt_infra_port_cranes": "Cycle 22: equal budget; Cartagena / MultiRio / Aracruz crane set already logged (miss).",
        "hunt_br_power_equip": "Cycle 22: logged state_grid_ne_uhv_construction_2026.",
        "hunt_latam_rail_telecom": "Cycle 22: equal budget; CRRC AIFA–Pachuca press-only / Alstom Mexico already logged (miss).",
        "hunt_res_copper": "Cycle 22: equal budget; Vicuña / El Abra already logged (miss).",
        "hunt_energy_solar": "Cycle 22: equal budget; no new named-project solar OEM award opened (miss).",
        "hunt_energy_other_renewables": "Cycle 22: equal budget; Tesla/Colbún Celda logged C21 (miss).",
        "hunt_res_water": "Cycle 22: equal budget; Veolia Aguas Pacífico logged C21 (miss).",
        "hunt_infra_bridges_roads": "Cycle 22: equal budget; Salvador–Itaparica logged C21 (miss).",
        "hunt_energy_fission_smr": "Cycle 22: equal budget; Meitner/CAREM/Nuclearis set already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 22: equal budget; ICTSI Cortés logged C21; DP World San Antonio still talks-only (miss).",
        "hunt_infra_engineering_epc": "Cycle 22: equal budget; STRACON Pérez Caldera logged C21 (miss).",
        "hunt_res_nickel": "Cycle 22: logged bndes_piaui_nickel_maq_100m_2026.",
        "hunt_res_balsa": "Cycle 22: equal budget; no new named exporter/importer stake beyond WITS years (miss).",
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
    print("Cycle 22 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
