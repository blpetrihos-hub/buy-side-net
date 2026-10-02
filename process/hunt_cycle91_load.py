#!/usr/bin/env python3
"""Cycle 91 hunt: shuffle_seed=20261091; equal budget; U.S./PRC split; thin after.

Order: fission_smr, solar, wind, building_materials, balsa, nickel, lithium,
copper, niobium, engineering_epc, other_renewables, bridges_roads,
port_ownership, rail, power_plants_grid, port_cranes, water, graphite.
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
# resources/water — CWE Embalse Zapallar (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cwe_zapallar_embalse_chile_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "prc",
        "counterpart": "China International Water & Electric Corp. (CWE) — Embalse Zapallar (Ñuble)",
        "country": "Chile",
        "asset": "MOP Dirección de Obras Hidráulicas multipurpose Embalse Zapallar on Río Diguillín (comuna El Carmen, Región de Ñuble): construction by China International Water & Electric Corporation (CWE) – Agencia en Chile; ~USD 158 million works investment; ~80 Mm³ storage; irrigation for ~10,000 ha in El Carmen and San Ignacio (~2,000+ producers); 1,620 calendar-day build; ops targeted 2030. First blast / works start Aug 2026 (MOP). Distinct from CHEC Embalse Las Palmas and Sacyr Coquimbo desal rows.",
        "investment_type": "epc",
        "value": "158000000",
        "currency": "USD",
        "value_usd": "158000000",
        "fx_usd": "1",
        "fx_date": "2026-08-20",
        "year": "2026",
        "status": "active",
        "lat": "-36.90",
        "lon": "-72.03",
        "geo_note": "Embalse Zapallar / El Carmen, Región de Ñuble (MOP geography; approximate Río Diguillín pin).",
        "evidence": "documented",
        "source_id": "mop_zapallar_tronadura_20260821",
        "note": "Actor: CWE (PRC SOE / PowerChina group) — prc. Official MOP 21 Aug 2026 names CWE and ~USD 158m; Feb 2026 MOP start notice corroborates CWE + 1,620 days / COD 2030. Value = dam works face (channels separately ~USD 300m program total — not dual-entered).",
    },
    {
        "id": "cwe_zapallar_embalse_chile_2026",
        "retrieved": "2026-10-02",
        "source_id": "mop_zapallar_tronadura_20260821",
        "url": "https://www.mop.gob.cl/gobierno-da-un-paso-decisivo-para-la-seguridad-hidrica-de-nuble-con-primera-tronadura-del-embalse-zapallar/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "embalse multipropósito, que representa una inversión cercana a los US$158 millones, marca un hito en la materialización de la construcción del embalse, a cargo de la Dirección de Obras Hidráulicas del Ministerio de Obras Públicas y del consorcio China International Water & Electric Corporation (CWE) – Agencia en Chile.",
        "note": "Opened MOP primary naming CWE contractor and ~USD 158m Zapallar dam investment at first blast.",
    },
    {
        "id": "mop_zapallar_tronadura_20260821",
        "type": "government",
        "chicago": "Chile Ministerio de Obras Públicas. “Gobierno da un paso decisivo para la seguridad hídrica de Ñuble con primera tronadura del Embalse Zapallar.” 21 August 2026.",
        "url": "https://www.mop.gob.cl/gobierno-da-un-paso-decisivo-para-la-seguridad-hidrica-de-nuble-con-primera-tronadura-del-embalse-zapallar/",
        "annotation": "Official MOP: CWE builds Embalse Zapallar; ~USD 158m; 80 Mm³; El Carmen/San Ignacio irrigation. Supports cwe_zapallar_embalse_chile_2026.",
        "supports": ["cwe_zapallar_embalse_chile_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — SolarMax Puerto Rico BESS EPC (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "solarmax_pr_bess_epc_158m_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "SolarMax Technology — Puerto Rico BESS EPC (Ceiba + Humacao)",
        "country": "Puerto Rico",
        "asset": "31 Dec 2025: SolarMax Renewable Energy Provider (wholly owned subsidiary of SolarMax Technology, Inc., NASDAQ: SMXT, Riverside CA) enters two EPC agreements for utility-scale BESS in Puerto Rico — (1) Naguabo BESS LLC facility in Ceiba Municipality, ~320 MWh, expected EPC revenues ~USD 122.3 million, SolarMax 9% membership interest; (2) Yabucoa BESS LLC facility in Humacao Municipality, ~80 MWh, expected EPC revenues ~USD 35.9 million, SolarMax 9% membership interest. Combined ~400 MWh / ~USD 158.2 million EPC revenues. Distinct from GE Vernova PREPA LM2500 and USACE Río Puerto Nuevo rows.",
        "investment_type": "epc",
        "value": "158200000",
        "currency": "USD",
        "value_usd": "158200000",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "18.264",
        "lon": "-65.648",
        "geo_note": "Ceiba Municipality BESS site (larger of two PR EPCs; Humacao/Yabucoa second site ~18.15,-65.82).",
        "evidence": "documented",
        "source_id": "solarmax_8k_20260106",
        "note": "Actor: SolarMax Technology (U.S.) — us. SEC Form 8-K Item 1.01; value = sum of stated expected PR EPC revenues (122.3+35.9). Texas Navboot EPC excluded (outside LAC).",
    },
    {
        "id": "solarmax_pr_bess_epc_158m_2025",
        "retrieved": "2026-10-02",
        "source_id": "solarmax_8k_20260106",
        "url": "https://www.sec.gov/Archives/edgar/data/1519472/000164033426000032/solarmax_8k.htm",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Pursuant to an EPC agreement with Naguabo BESS LLC … Ceiba Municipality, Puerto Rico. The contract is expected to generate revenues of approximately $122.3 million … 320 megawatt-hours. … Pursuant to an EPC agreement with Yabucoa BESS LLC … Humacao Municipality, Puerto Rico. The contract is expected to generate revenues of approximately $35.9 million … 80 megawatt-hours.",
        "note": "Opened SolarMax SEC Form 8-K stating two Puerto Rico BESS EPC revenue figures.",
    },
    {
        "id": "solarmax_8k_20260106",
        "type": "sec_filing",
        "chicago": "SolarMax Technology, Inc. Form 8-K (Item 1.01 Entry into a Material Definitive Agreement). Filed 6 January 2026 (event date 31 December 2025). SEC EDGAR.",
        "url": "https://www.sec.gov/Archives/edgar/data/1519472/000164033426000032/solarmax_8k.htm",
        "annotation": "SEC 8-K: SolarMax PR BESS EPCs Ceiba USD 122.3m / Humacao USD 35.9m. Supports solarmax_pr_bess_epc_158m_2025.",
        "supports": ["solarmax_pr_bess_epc_158m_2025", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Stem PowerTrack EMS Granja Solar Chile (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "stem_granja_powertrack_ems_chile_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Stem, Inc. — PowerTrack EMS at Copec Flux Granja Solar hybrid (Chile)",
        "country": "Chile",
        "asset": "27 May 2026 Stem, Inc. (NYSE: STEM): Copec Flux deploys Stem PowerTrack Energy Management System as master control at Granja Solar (Tarapacá) — existing ~135 MW PV retrofitted with 420 MWh BESS hybrid; Stem provides PowerTrack edge and cloud monitoring/controls. CapEx USD for EMS not disclosed. Distinct from Tesla Copec Cousiño BESS and ContourGlobal Víctor Jara / Quillagua hybrid rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-20.25",
        "lon": "-69.80",
        "geo_note": "Granja Solar PV park, Región de Tarapacá (Stem/Copec geography; approximate).",
        "evidence": "documented",
        "source_id": "stem_granja_ems_20260527",
        "note": "Actor: Stem, Inc. (U.S.) — us; site owner Copec Flux (Chile). Company IR primary; EMS contract USD blank.",
    },
    {
        "id": "stem_granja_powertrack_ems_chile_2026",
        "retrieved": "2026-10-02",
        "source_id": "stem_granja_ems_20260527",
        "url": "https://investors.stem.com/news-events/press-releases/detail/210/stem-brings-powertrack-ems-to-latin-americas-utility-scale-hybrid-market-with-granja-solar-project-in-chile",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Copec Flux, the renewable energy subsidiary of Copec S.A., is deploying Stem’s PowerTrack™ Energy Management System (EMS) at the Granja Solar project in Chile. … The Granja project is an existing 135 MW PV project that Copec is retrofitting with a 420 MWh BESS … Stem’s PowerTrack Energy Management System (EMS) will serve as the site’s master control system.",
        "note": "Opened Stem IR release naming PowerTrack EMS deployment at Granja Solar hybrid.",
    },
    {
        "id": "stem_granja_ems_20260527",
        "type": "company",
        "chicago": "Stem, Inc. “Stem Brings PowerTrack EMS to Latin America’s Utility-Scale Hybrid Market with Granja Solar Project in Chile.” Investor news release, 27 May 2026.",
        "url": "https://investors.stem.com/news-events/press-releases/detail/210/stem-brings-powertrack-ems-to-latin-americas-utility-scale-hybrid-market-with-granja-solar-project-in-chile",
        "annotation": "Stem IR: PowerTrack EMS at Copec Flux Granja Solar 135 MW + 420 MWh BESS. Supports stem_granja_powertrack_ems_chile_2026.",
        "supports": ["stem_granja_powertrack_ems_chile_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — CB&I VMOS Punta Colorada storage (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cbi_vmos_punta_colorada_storage_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "CB&I — VMOS Vaca Muerta Sur crude export storage (Punta Colorada)",
        "country": "Argentina",
        "asset": "16 Jan 2025 CB&I: awarded significant EPC contract by VMOS, S.A. for engineering, procurement, fabrication and construction of 630,000 m³ (4 million barrels) total crude storage at the Vaca Muerta Sur exportation facility, Punta Colorada, Río Negro Province; construction start targeted Q2 2025; completion targeted Q4 2026. VMOS led by YPF with Pan American Energy, Vista Energy, and Pampa Energía. CB&I defines “significant” as USD 100–250 million — exact USD not disclosed. Distinct from Halliburton YPF ZEUS / Pumpco–Bonatti Argentina LNG pipeline rows.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-41.70",
        "lon": "-65.02",
        "geo_note": "Punta Colorada crude export terminal, Río Negro Province (CB&I/VMOS geography; approximate coastal pin).",
        "evidence": "documented",
        "source_id": "cbi_vmos_punta_colorada_20250116",
        "note": "Actor: CB&I (U.S., The Woodlands TX) — us. Company PDF primary; value blank (significant = USD 100–250m band only).",
    },
    {
        "id": "cbi_vmos_punta_colorada_storage_2025",
        "retrieved": "2026-10-02",
        "source_id": "cbi_vmos_punta_colorada_20250116",
        "url": "https://www.cbi.com/wp-content/uploads/2025/01/CBI-Awarded-Crude-Oil-Exportation-Storage-Contract-for-Vaca-Muerta-Sur-Project-in-Argentina-FINAL.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "CB&I today announced that it has been awarded a significant* contract by VMOS, S.A., for the engineering, procurement, fabrication, and construction (EPC) of 630,000 cubic meters (4 million barrels) of total storage for the Vaca Muerta crude oil exportation facility, located in Punta Colorada, Rio Negro Province, Argentina. … *CB&I defines a significant contract as between USD $100 million and $250 million.",
        "note": "Opened CB&I PDF naming VMOS Punta Colorada storage EPC and significant USD band.",
    },
    {
        "id": "cbi_vmos_punta_colorada_20250116",
        "type": "company",
        "chicago": "CB&I. “CB&I Awarded Crude Oil Exportation Storage Contract for Vaca Muerta Oil Sur Project in Argentina.” News release PDF, 16 January 2025.",
        "url": "https://www.cbi.com/wp-content/uploads/2025/01/CBI-Awarded-Crude-Oil-Exportation-Storage-Contract-for-Vaca-Muerta-Sur-Project-in-Argentina-FINAL.pdf",
        "annotation": "CB&I primary: VMOS Punta Colorada 630,000 m³ storage EPC; significant = USD 100–250m. Supports cbi_vmos_punta_colorada_storage_2025.",
        "supports": ["cbi_vmos_punta_colorada_storage_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Trina Storage Luz del Norte Chile (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "trina_luz_del_norte_bess_722mwh_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Trina Storage — Luz del Norte BESS 141 MW / 722 MWh (Copiapó)",
        "country": "Chile",
        "asset": "Jan 2026 Trina Storage (Trinasolar): BESS supply contract with T-Power (Toesca Asset Management) for Luz del Norte energy storage at Copiapó, Atacama — 141 MW / 722 MWh using Elementa 2 containers; co-located with existing ~141 MW Luz del Norte PV. Part of Trina’s disclosed 1,203 MWh Chile+Argentina contract package. CapEx USD not disclosed. Distinct from trina_atlas_copiapo_bess_2025 (Atlas Copiapó GFM) and Sungrow Observatorio rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-27.37",
        "lon": "-70.33",
        "geo_note": "Luz del Norte / Copiapó, Atacama Region (Trina Storage release).",
        "evidence": "documented",
        "source_id": "trina_storage_latam_1203mwh_20260122",
        "note": "Actor: Trina Storage / Trinasolar (PRC) — prc; buyer T-Power/Toesca (Chile). Company English newsroom; contract USD blank.",
    },
    {
        "id": "trina_luz_del_norte_bess_722mwh_2026",
        "retrieved": "2026-10-02",
        "source_id": "trina_storage_latam_1203mwh_20260122",
        "url": "https://www.trinasolar.com/en-glb/newsroom202601220619/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In Chile, Trina Storage is partnering with T-Power on the Luz del Norte energy storage project in Copiapó, Atacama Region. The 141MW / 722MWh system is designed to enhance the operational efficiency of the associated photovoltaic plant",
        "note": "Opened Trina English newsroom naming Luz del Norte 141 MW / 722 MWh BESS.",
    },
    {
        "id": "trina_storage_latam_1203mwh_20260122",
        "type": "company",
        "chicago": "Trina Storage / Trinasolar. “Trina Storage Strengthens Its Global Energy Storage Portfolio with 1.203GWh of New BESS Contracts in Latin America.” Newsroom, 22 January 2026.",
        "url": "https://www.trinasolar.com/en-glb/newsroom202601220619/",
        "annotation": "Trina primary: Luz del Norte Chile 141 MW/722 MWh and Alma Sur Argentina 90 MW/481 MWh. Supports trina_luz_del_norte_bess_722mwh_2026 and trina_alma_sur_bess_481mwh_2026.",
        "supports": [
            "trina_luz_del_norte_bess_722mwh_2026",
            "trina_alma_sur_bess_481mwh_2026",
            "hunt_energy_other_renewables",
        ],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Trina Storage Alma Sur Argentina (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "trina_alma_sur_bess_481mwh_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Trina Storage — Alma Sur BESS 90 MW / 481 MWh (Dock Sud / ALMA GBA)",
        "country": "Argentina",
        "asset": "Jan 2026 Trina Storage: BESS supply agreement with Central Dock Sud S.A. (YPF Luz) for Alma Sur project under ALMA GBA program — 90 MW / 481 MWh Elementa 2; targets seasonal capacity for Buenos Aires Province / AMBA. CapEx USD not disclosed. Distinct from trina_luz_del_norte_bess_722mwh_2026 and YPF Luz El Quemado solar row.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-34.64",
        "lon": "-58.34",
        "geo_note": "Central Dock Sud / Alma Sur BESS, Buenos Aires Province (Trina/YPF Luz geography; approximate).",
        "evidence": "documented",
        "source_id": "trina_storage_latam_1203mwh_20260122",
        "note": "Actor: Trina Storage (PRC) — prc; buyer Central Dock Sud / YPF Luz. Same Trina English newsroom as Luz del Norte; contract USD blank.",
    },
    {
        "id": "trina_alma_sur_bess_481mwh_2026",
        "retrieved": "2026-10-02",
        "source_id": "trina_storage_latam_1203mwh_20260122",
        "url": "https://www.trinasolar.com/en-glb/newsroom202601220619/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In Argentina, Trina Storage has signed an agreement with Central Dock Sud S.A., a subsidiary of YPF Luz, for the Alma Sur project, a key component of the ALMA GBA program … The 90MW / 481MWh system is designed to address seasonal capacity shortages in the Province of Buenos Aires",
        "note": "Opened Trina English newsroom naming Alma Sur 90 MW / 481 MWh BESS.",
    },
    {
        "id": "trina_storage_latam_1203mwh_20260122",
        "type": "company",
        "chicago": "Trina Storage / Trinasolar. “Trina Storage Strengthens Its Global Energy Storage Portfolio with 1.203GWh of New BESS Contracts in Latin America.” Newsroom, 22 January 2026.",
        "url": "https://www.trinasolar.com/en-glb/newsroom202601220619/",
        "annotation": "Trina primary: Luz del Norte Chile 141 MW/722 MWh and Alma Sur Argentina 90 MW/481 MWh. Supports trina_luz_del_norte_bess_722mwh_2026 and trina_alma_sur_bess_481mwh_2026.",
        "supports": [
            "trina_luz_del_norte_bess_722mwh_2026",
            "trina_alma_sur_bess_481mwh_2026",
            "hunt_energy_other_renewables",
        ],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]] = entry
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8"))
    assert isinstance(bib, list)
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
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
        "hunt_energy_fission_smr": "Cycle 91: equal budget; USTDA / CAREM / FIRST / Meitner already (miss). Thin top-up dry — shift.",
        "hunt_energy_solar": "Cycle 91: equal budget; JA Solar Exel / Array Lupi / ContourGlobal already (miss).",
        "hunt_energy_wind": "Cycle 91: equal budget; Mingyang Copel / Goldwind / Envision / Sany already (miss).",
        "hunt_infra_building_materials": "Cycle 91: equal budget; Holcim Colombia / Sinoma Cruz Azul dense (miss).",
        "hunt_res_balsa": "Cycle 91: equal budget; Plantabal / AIMA dense (miss). Thin top-up dry — shift.",
        "hunt_res_nickel": "Cycle 91: equal budget; DFC Piauí / Brazilian Nickel / Centaurus already (miss). Next-thinnest after fission/balsa/graphite dry.",
        "hunt_res_lithium": "Cycle 91: equal budget; Zijin 3Q / Atlas Neves / EXIM Argentina / PPG already (miss).",
        "hunt_res_copper": "Cycle 91: equal budget; FCX El Abra / Zijin La Arena / Southern Copper already (miss).",
        "hunt_fenb_araxa": "Cycle 91: equal budget; CMOC / CBMM / St George already (miss).",
        "hunt_infra_engineering_epc": "Cycle 91: logged cbi_vmos_punta_colorada_storage_2025 (U.S.; significant USD 100–250m band).",
        "hunt_energy_other_renewables": "Cycle 91: logged solarmax_pr_bess_epc_158m_2025 (U.S.) + stem_granja_powertrack_ems_chile_2026 (U.S.) + trina_luz_del_norte_bess_722mwh_2026 (PRC) + trina_alma_sur_bess_481mwh_2026 (PRC).",
        "hunt_infra_bridges_roads": "Cycle 91: equal budget; CRBC Corentyne / EBD / CHEC already (miss).",
        "hunt_infra_port_ownership": "Cycle 91: equal budget; COSCO / APM / SSA / Hutchison dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 91: equal budget; CRRC / CRCC Batuco / Wabtec already (miss).",
        "hunt_br_power_equip": "Cycle 91: equal budget; ENGIE Peru Grupo 1 / MCC Belize / AES Andes already (miss).",
        "hunt_infra_port_cranes": "Cycle 91: equal budget; ZPMC Contecon / Kalmar / Konecranes already (miss).",
        "hunt_res_water": "Cycle 91: logged cwe_zapallar_embalse_chile_2026 (PRC; ~USD 158m MOP).",
        "hunt_res_graphite": "Cycle 91: equal budget; Graphcoa / South Star / Atlas Malacacheta dense (miss). Thin top-up dry — shift.",
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
    print("Cycle 91 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
