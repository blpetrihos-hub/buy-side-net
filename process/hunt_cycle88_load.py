#!/usr/bin/env python3
"""Cycle 88 hunt: shuffle_seed=20261088; equal budget; U.S./PRC split; thin after.

Order: port_cranes, solar, niobium, fission_smr, balsa, rail, other_renewables,
water, power_plants_grid, copper, port_ownership, bridges_roads, wind,
engineering_epc, nickel, lithium, graphite, building_materials.
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
# 2 energy/solar — Atlas Renewable Energy USD 3bn LatAm refinancing (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atlas_latam_3bn_refi_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "Atlas Renewable Energy — USD 3bn corporate refinancing (Chile/Brazil/Mexico solar+BESS portfolio)",
        "country": "Chile",
        "asset": "23 Feb 2026 Atlas (Miami HQ) announces ~USD 3 billion corporate refinancing for non-conventional renewable energy in Latin America — largest such corporate refinancing in the region per company; covers high-performing solar and storage assets in Chile, Brazil and Mexico; sponsor Global Infrastructure Partners (GIP/BlackRock); lenders include BNP Paribas, Crédit Agricole, Goldman Sachs, Morgan Stanley, MUFG, Natixis CIB, Santander CIB. Distinct from atlas_vista_alegre_solar_br_2025 and Trina Atlas Copiapó BESS OEM row.",
        "investment_type": "financing",
        "value": "3000000000",
        "currency": "USD",
        "value_usd": "3000000000",
        "fx_usd": "1",
        "fx_date": "2026-02-23",
        "year": "2026",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Multi-country portfolio (Chile, Brazil, Mexico); no single named site on refinancing release — lat/lon left blank.",
        "evidence": "documented",
        "source_id": "atlas_latam_refi_20260223",
        "note": "Actor: Atlas Renewable Energy (Miami HQ; GIP-backed) — us. Company English primary. Portfolio value = stated refinancing total.",
    },
    {
        "id": "atlas_latam_3bn_refi_2026",
        "retrieved": "2026-10-02",
        "source_id": "atlas_latam_refi_20260223",
        "url": "https://atlasrenewableenergy.com/news-and-insights/atlas-renewable-energy-secures-landmark-usd-3-billion-refinancing-for-its-portfolio-in-latin-america/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Totaling approximately USD 3 billion, the transaction was executed by Atlas with support from its sponsor Global Infrastructure Partners (GIP) … The transaction covers a portfolio of high-performing solar and storage assets located in Chile, Brazil and Mexico.",
        "note": "Opened Atlas Renewable Energy company press release on USD 3bn LatAm refinancing.",
    },
    {
        "id": "atlas_latam_refi_20260223",
        "type": "company",
        "chicago": "Atlas Renewable Energy. “Atlas Renewable Energy Secures Landmark USD 3 Billion Refinancing for its Portfolio in Latin America.” Press release, 23 February 2026.",
        "url": "https://atlasrenewableenergy.com/news-and-insights/atlas-renewable-energy-secures-landmark-usd-3-billion-refinancing-for-its-portfolio-in-latin-america/",
        "annotation": "Atlas Miami HQ USD 3bn solar/storage portfolio refinancing (Chile/Brazil/Mexico). Supports atlas_latam_3bn_refi_2026.",
        "supports": ["atlas_latam_3bn_refi_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 2 energy/solar — DFC Solararomo 200 MW Manta Ecuador proposed loan (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "dfc_solaramo_manta_200mw_ecuador",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "DFC — proposed USD 144m loan to Solararomo S.A. (200 MW PV near Manta)",
        "country": "Ecuador",
        "asset": "DFC Public Information Summary 9000104243: proposed up to USD 144 million / ≤18-year loan to Solararomo S.A. for development, construction and operation of a 200 MW solar PV plant near Manta, Manabí province; all-source funding total USD 192 million; expected ~344 GWh/year; framed as Ecuador’s first large-scale solar power project. Proposed disclosure — not a closed commitment on the opened PIS.",
        "investment_type": "financing",
        "value": "144000000",
        "currency": "USD",
        "value_usd": "144000000",
        "fx_usd": "1",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-0.95",
        "lon": "-80.73",
        "geo_note": "Near Manta, Manabí province, Ecuador (DFC PIS geography; approximate coastal pin).",
        "evidence": "documented",
        "source_id": "dfc_solaramo_pis_9000104243",
        "note": "Actor: U.S. DFC proposed financing — us. Official DFC PIS PDF; proposed loan amount entered as stated ceiling.",
    },
    {
        "id": "dfc_solaramo_manta_200mw_ecuador",
        "retrieved": "2026-10-02",
        "source_id": "dfc_solaramo_pis_9000104243",
        "url": "https://www.dfc.gov/sites/default/files/media/documents/9000104243.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Development, construction and operation of a 200-megawatt solar photovoltaic power plant near the city of Manta in the Manabí province of Ecuador. … $144,000,000 and up to 18-year term … All-Source Funding Total $192,000,000",
        "note": "Opened DFC Public Information Summary PDF for Solararomo S.A. proposed loan.",
    },
    {
        "id": "dfc_solaramo_pis_9000104243",
        "type": "official",
        "chicago": "U.S. International Development Finance Corporation. “Public Information Summary — Solararomo S.A. (9000104243).” Project disclosure PDF.",
        "url": "https://www.dfc.gov/sites/default/files/media/documents/9000104243.pdf",
        "annotation": "DFC proposed USD 144m loan for 200 MW Solararomo PV near Manta, Ecuador. Supports dfc_solaramo_manta_200mw_ecuador.",
        "supports": ["dfc_solaramo_manta_200mw_ecuador", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 7 energy/other_renewables — Sungrow Librillo BESS Sonnedix Chile (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_sonnedix_librillo_bess_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Sungrow — PowerTitan 2.0 supply for Sonnedix Librillo 643.8 MWh standalone BESS",
        "country": "Chile",
        "asset": "28 May 2026 Sonnedix/Sungrow: supply agreement for 643.8 MWh Sungrow PowerTitan 2.0 (128 liquid-cooled units + 32 MVS) for Sonnedix Librillo standalone BESS in Taltal, Antofagasta — 117 MW / 5-hour system; delivery/installation Q1 2027; COD targeted Apr 2027 (separate Copec EMOAC PPA). Contract USD not disclosed. Distinct from sungrow Aurora / Tocopilla / Observatorio rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-25.40",
        "lon": "-70.48",
        "geo_note": "Librillo BESS / Taltal, Antofagasta Region, Chile (Sonnedix PPA geography; approximate municipal pin).",
        "evidence": "documented",
        "source_id": "sonnedix_sungrow_librillo_20260528",
        "note": "Actor: Sungrow (PRC) — prc; developer Sonnedix (Spain) — allied counterpart not dual-sided. Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_sonnedix_librillo_bess_2026",
        "retrieved": "2026-10-02",
        "source_id": "sonnedix_sungrow_librillo_20260528",
        "url": "https://www.sonnedix.com/news/sungrow-and-sonnedix-sign-a-supply-agreement-for-the-643.8-mwh-librillo-standalone-bess-project-in-chile",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sungrow … and Sonnedix … have signed a supply agreement for 643.8 MWh of Sungrow’s PowerTitan 2.0 solution for the Sonnedix Librillo BESS Project in Chile. … Sungrow will supply 128 units of its PowerTitan 2.0 liquid-cooled system and 32 medium-voltage cells (MVS)",
        "note": "Opened Sonnedix English release on Sungrow Librillo BESS supply agreement.",
    },
    {
        "id": "sonnedix_sungrow_librillo_20260528",
        "type": "company",
        "chicago": "Sonnedix. “Sungrow and Sonnedix Sign a Supply Agreement for the 643.8 MWh Librillo Standalone BESS Project in Chile.” 28 May 2026.",
        "url": "https://www.sonnedix.com/news/sungrow-and-sonnedix-sign-a-supply-agreement-for-the-643.8-mwh-librillo-standalone-bess-project-in-chile",
        "annotation": "Sungrow PowerTitan 2.0 for Sonnedix Librillo 643.8 MWh BESS (Taltal, Chile). Supports sungrow_sonnedix_librillo_bess_2026.",
        "supports": ["sungrow_sonnedix_librillo_bess_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 7 energy/other_renewables — Sungrow Observatorio BESS Verano Chile (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_verano_observatorio_bess_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Sungrow — PowerTitan 2.0 152 MW / 606 MWh BESS + LTSA for Verano Observatorio",
        "country": "Chile",
        "asset": "17 Aug 2026 Sungrow: selected by Verano Energy to supply PowerTitan 2.0 ESS for Observatorio hybrid in Marchigüe, O’Higgins — 152 MW / 606 MWh four-hour BESS plus 25-year LTSA; co-located 135 MW PV with Sungrow SG350HX-20 inverters. Contract USD not disclosed. Distinct from Librillo / Aurora / Tocopilla Sungrow rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-34.40",
        "lon": "-71.67",
        "geo_note": "Observatorio / Marchigüe, Cardenal Caro, O’Higgins Region, Chile (pv magazine LatAm / company geography; approximate municipal pin).",
        "evidence": "documented",
        "source_id": "sungrow_observatorio_20260817",
        "note": "Actor: Sungrow (PRC) — prc; developer Verano Energy — other/allied counterpart not dual-sided. Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_verano_observatorio_bess_2026",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_observatorio_20260817",
        "url": "https://www.sungrowpower.com/en/sungrow-to-deliver-606-mwh-energy-storage-system-for-verano-energys-observatorio-project-in-chile",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sungrow … has been selected by Verano Energy … to supply its PowerTitan 2.0 ESS solution for the Observatorio project in Chile. The agreement includes the deployment of a 152 MW / 606 MWh battery energy storage system (BESS) with a four-hour duration, together with a 25-year Long-Term Service Agreement (LTSA)",
        "note": "Opened Sungrow English newsroom on Observatorio BESS supply.",
    },
    {
        "id": "sungrow_observatorio_20260817",
        "type": "company",
        "chicago": "Sungrow. “Sungrow to Deliver 606 MWh Energy Storage System for Verano Energy’s Observatorio Project in Chile.” 17 August 2026.",
        "url": "https://www.sungrowpower.com/en/sungrow-to-deliver-606-mwh-energy-storage-system-for-verano-energys-observatorio-project-in-chile",
        "annotation": "Sungrow 152 MW/606 MWh PowerTitan 2.0 + LTSA for Verano Observatorio (Chile). Supports sungrow_verano_observatorio_bess_2026.",
        "supports": ["sungrow_verano_observatorio_bess_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 13 energy/wind — POWERCHINA Jiangxi Ingenio 2×1.5 MW retrofit EPC Mexico (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_jiangxi_ingenio_wind_epc_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "POWERCHINA Jiangxi — EPC reconstruction of 2×1.5 MW turbines at Ingenio Wind Farm",
        "country": "Mexico",
        "asset": "7 Oct 2025 Zuma Energía / SPIC Mexico tender result (Req478PEI): POWERCHINA Jiangxi Electric Power Construction Co., Ltd. recommended as successful bidder for EPC reconstruction/restoration of turbines A3.04 and A6.02 (2×1.5 MW) at Ingenio Wind Farm, Santo Domingo Ingenio, Oaxaca; bid opening 23 Sep 2025; evaluation ended 10 Oct 2025; tendering agent China Power Complete Equipment Co., Ltd. Contract USD not disclosed.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "16.59",
        "lon": "-94.77",
        "geo_note": "Parque Eólico Ingenio, Santo Domingo Ingenio, Oaxaca, Mexico (Zuma Energía project page; approximate pin).",
        "evidence": "documented",
        "source_id": "zuma_ingenio_epc_tender_20251007",
        "note": "Actor: POWERCHINA Jiangxi (PRC SOE) — prc; purchaser Zuma Energía / SPIC Mexico. Company English tender-result page. CapEx blank.",
    },
    {
        "id": "powerchina_jiangxi_ingenio_wind_epc_2025",
        "retrieved": "2026-10-02",
        "source_id": "zuma_ingenio_epc_tender_20251007",
        "url": "https://zumaenergia.com/en/press-center-view?id=110",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "POWERCHINA Jiangxi Electric Power Construction Co., Ltd. was recommended as the successful bidder to carry out the reconstruction and restoration of turbines A3.04 and A6.02 at the Ingenio Wind Farm, located in Mexico.",
        "note": "Opened Zuma Energía / SPIC Mexico English tender-result page for Ingenio EPC.",
    },
    {
        "id": "zuma_ingenio_epc_tender_20251007",
        "type": "company",
        "chicago": "Zuma Energía / SPIC Mexico. “Result of the Tender for the EPC Contract of Ingenio Wind Farm 2×1.5MW Wind Turbines Reconstruction and Restoration Project.” 7 October 2025.",
        "url": "https://zumaenergia.com/en/press-center-view?id=110",
        "annotation": "POWERCHINA Jiangxi recommended winner for Ingenio 2×1.5 MW turbine retrofit EPC (Oaxaca). Supports powerchina_jiangxi_ingenio_wind_epc_2025.",
        "supports": ["powerchina_jiangxi_ingenio_wind_epc_2025", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# 12 infrastructure/bridges_roads — CRBC Corentyne Lot 2 Guyana (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crbc_corentyne_lot2_guyana_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "CRBC — Palmyra–Moleson Creek Highway Lot 2 (Bloomfield–No. 54 Village)",
        "country": "Guyana",
        "asset": "26 Aug 2026 Guyana DPI: paving underway on Lot 2 of Palmyra–Moleson Creek four-lane highway (Bloomfield to Number 54 Village), executed by China Road and Bridge Corporation (CRBC); Lot 2 valued at over $2.9 billion (Guyana-dollar convention when not prefixed US$ in same article that states corridor US$604 million). Corridor is part of Region Six Corentyne upgrade. Distinct from CRCC Demerara Harbour Bridge and stalled Corentyne River Bridge preferred-contractor notices.",
        "investment_type": "epc",
        "value": "2900000000",
        "currency": "GYD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "6.05",
        "lon": "-57.25",
        "geo_note": "Bloomfield–Number 54 Village corridor, Corentyne, Region Six, Guyana (DPI geography; approximate mid-lot pin).",
        "evidence": "documented",
        "source_id": "dpi_crbc_corentyne_lot2_20260826",
        "note": "Actor: CRBC (PRC SOE) — prc. Official DPI Guyana notice. Value stored as GYD >2.9bn per local $-without-US$ convention in same article that prefixes corridor as US$604m; USD conversion left blank. Amount phrasing “over $2.9 billion” — treat figure as UNVERIFIED proxy scale if cross-checked later.",
    },
    {
        "id": "crbc_corentyne_lot2_guyana_2026",
        "retrieved": "2026-10-02",
        "source_id": "dpi_crbc_corentyne_lot2_20260826",
        "url": "https://dpi.gov.gy/paving-commences-on-lot-2-of-palmyra-moleson-creek-road-project/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Lot 2, running from Bloomfield to Number 54 Village, is valued at over $2.9 billion and is being executed by China Road and Bridge Corporation (CRBC). The lot forms part of the wider US$604 million Palmyra to Moleson Creek four-lane highway project",
        "note": "Opened Guyana Department of Public Information notice on CRBC Lot 2 paving.",
    },
    {
        "id": "dpi_crbc_corentyne_lot2_20260826",
        "type": "official",
        "chicago": "Guyana. Department of Public Information. “Paving Commences on Lot 2 of Palmyra-Moleson Creek Road Project.” 26 August 2026.",
        "url": "https://dpi.gov.gy/paving-commences-on-lot-2-of-palmyra-moleson-creek-road-project/",
        "annotation": "CRBC executing Palmyra–Moleson Creek Lot 2 (Bloomfield–No. 54); >GYD 2.9bn lot within US$604m corridor. Supports crbc_corentyne_lot2_guyana_2026.",
        "supports": ["crbc_corentyne_lot2_guyana_2026", "hunt_infra_bridges_roads"],
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
        "hunt_infra_port_cranes": "Cycle 88: equal budget; Sany Suape / SSA Guaymas / Konecranes Arica already (miss).",
        "hunt_energy_solar": "Cycle 88: logged atlas_latam_3bn_refi_2026 (U.S.) + dfc_solaramo_manta_200mw_ecuador (U.S.); Nextracker Casa dos Ventos already.",
        "hunt_fenb_araxa": "Cycle 88: equal budget; CMOC Boa Vista / CBMM already (miss). Thin top-up candidate dry — shift.",
        "hunt_energy_fission_smr": "Cycle 88: equal budget; USTDA LAC nuclear / FIRST / CAREM already (miss). Thin top-up dry — shift.",
        "hunt_res_balsa": "Cycle 88: equal budget; Plantabal / AIMA / Sino Composites already (miss). Thin top-up dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 88: equal budget; USTDA Honduras CONFI / USACE Quetzal rail already (miss).",
        "hunt_energy_other_renewables": "Cycle 88: logged sungrow_sonnedix_librillo_bess_2026 + sungrow_verano_observatorio_bess_2026 (PRC).",
        "hunt_res_water": "Cycle 88: equal budget; NADBank Sonora / Acciona Pernambuco already (miss).",
        "hunt_br_power_equip": "Cycle 88: equal budget; GE Vernova / XD / Siemens set already (miss).",
        "hunt_res_copper": "Cycle 88: equal budget; FCX El Abra / Southern Copper / Zijin La Arena already (miss).",
        "hunt_infra_port_ownership": "Cycle 88: equal budget; CHEC Kingston yard logged as engineering_epc; APM/DP World/Jinzhao already (miss).",
        "hunt_infra_bridges_roads": "Cycle 88: logged crbc_corentyne_lot2_guyana_2026 (PRC); USACE Guatemala roads already.",
        "hunt_energy_wind": "Cycle 88: logged powerchina_jiangxi_ingenio_wind_epc_2025 (PRC); Vestas/Goldwind/Envision already.",
        "hunt_infra_engineering_epc": "Cycle 88: equal budget; Halliburton Bumerangue / Baker Hughes Petrobras already (miss).",
        "hunt_res_nickel": "Cycle 88: equal budget; DFC Piauí / Fenix El Estor / Corex Cerro Matoso already (miss). Next-thinnest after fission/balsa/graphite dry.",
        "hunt_res_lithium": "Cycle 88: equal budget; Zijin Tres Quebradas RIGI already (miss).",
        "hunt_res_graphite": "Cycle 88: equal budget; Atlas Malacacheta / Graphcoa already (miss). Thin top-up dry — shift to nickel then miss.",
        "hunt_infra_building_materials": "Cycle 88: equal budget; Holcim / Huaxin / Cemex already (miss).",
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
    print("Cycle 88 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
