#!/usr/bin/env python3
"""Cycle 95 hunt: shuffle_seed=20261095; equal budget; U.S./PRC split; thin after.

Order: wind, solar, other_renewables, building_materials, nickel, rail, balsa,
port_ownership, engineering_epc, bridges_roads, water, fission_smr, lithium,
copper, port_cranes, power_plants_grid, niobium, graphite.
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
# energy/wind — Cox Santa Cruz Wind Panama PPA (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cox_santa_cruz_wind_panama_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Cox — Santa Cruz Wind 68.4 MW (Panama ETESA PPA)",
        "country": "Panama",
        "asset": "30 Jul 2026: Cox awarded long-term wind energy supply contract by Empresa de Transmisión Eléctrica, S.A. (ETESA) for Santa Cruz Wind — 68.4 MW (12 turbines; ~260 GWh/year) supplying ~5.22 TWh over 20 years for more than USD 350 million (PPA revenue/value, not disclosed construction CapEx — leave CapEx blank). Distinct from Cox Rosarito desal.",
        "investment_type": "greenfield_plant",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "8.50",
        "lon": "-80.00",
        "geo_note": "Santa Cruz Wind project, Panama (Cox company geography; approximate national pin).",
        "evidence": "documented",
        "source_id": "cox_santa_cruz_wind_20260730",
        "note": "Actor: Cox (Spanish HQ) — allied. Company primary. CapEx blank; >USD 350m is 20-year supply contract value.",
    },
    {
        "id": "cox_santa_cruz_wind_panama_2026",
        "retrieved": "2026-10-02",
        "source_id": "cox_santa_cruz_wind_20260730",
        "url": "https://grupocox.com/en/cox-awarded-20-year-wind-power-supply-contract-in-panama-for-more-than-350-million/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Cox … has been awarded, through its Santa Cruz Wind project, a long-term wind energy supply contract in Panama … The award contemplates the total supply of approximately 5.22 TWh of wind energy over a period of 20 years for more than 350 million dollars. … Santa Cruz Wind, which will have a capacity of 68.4 MW of installed power in a complex that includes 12 wind turbines",
        "note": "Opened Cox English release naming ETESA award, 68.4 MW Santa Cruz Wind, >USD 350m 20-year supply.",
    },
    {
        "id": "cox_santa_cruz_wind_20260730",
        "type": "company",
        "chicago": "Cox. “Cox Awarded 20-Year Wind Power Supply Contract in Panama for More Than $350 Million.” 30 July 2026.",
        "url": "https://grupocox.com/en/cox-awarded-20-year-wind-power-supply-contract-in-panama-for-more-than-350-million/",
        "annotation": "Cox primary: Santa Cruz Wind 68.4 MW ETESA PPA >USD 350m supply. Supports cox_santa_cruz_wind_panama_2026.",
        "supports": ["cox_santa_cruz_wind_panama_2026", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — First Solar / EXIM Zacapa panels (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "first_solar_zacapa_exim_guatemala_2021",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "First Solar — thin-film modules for Zacapa 9.5 MW (EXIM-backed)",
        "country": "Guatemala",
        "asset": "23 Sep 2021 (EXIM Deal of the Year announcement): EXIM approves 18-year guarantee of USD 8.7 million BankProv loan financing export of First Solar U.S.-manufactured thin-film panels to Kruger Energy’s Zacapa 9.5 MW solar project supplying a paper mill in Río Hondo, Guatemala — EXIM states financing helped First Solar win over Chinese panel competitors. CapEx figure is EXIM-guaranteed loan amount for panel export.",
        "investment_type": "equipment_supply",
        "value": "8700000",
        "currency": "USD",
        "value_usd": "8700000",
        "fx_usd": "1",
        "fx_date": "2021-09-23",
        "year": "2021",
        "status": "active",
        "lat": "15.07",
        "lon": "-89.55",
        "geo_note": "Zacapa / Río Hondo paper-mill solar site, Guatemala (EXIM geography).",
        "evidence": "documented",
        "source_id": "exim_first_solar_zacapa_20210923",
        "note": "Actor: First Solar (U.S. HQ) + EXIM U.S. government financing — us. Official EXIM release. Distinct from MASPV Estanzuela Zacapa solar+BESS.",
    },
    {
        "id": "first_solar_zacapa_exim_guatemala_2021",
        "retrieved": "2026-10-02",
        "source_id": "exim_first_solar_zacapa_20210923",
        "url": "https://www.exim.gov/news/first-solar-exports-zacapa-solar-energy-project-guatemala-exim-2021-deal-year",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "EXIM approved an 18-year guarantee of a $8.7 million loan from BankProv to finance the export of First Solar's U.S.-manufactured, thin-film solar panels to the Zacapa 9.5MW solar power project to supply power to a paper mill in Rio Hondo, Guatemala. … EXIM's financing helped First Solar to win the contract over solar-panel competitors from China.",
        "note": "Opened EXIM.gov Deal of the Year release naming First Solar Zacapa export and USD 8.7m guarantee.",
    },
    {
        "id": "exim_first_solar_zacapa_20210923",
        "type": "government",
        "chicago": "Export-Import Bank of the United States. “First Solar Exports to Zacapa Solar-Energy Project in Guatemala is EXIM 2021 Deal of the Year.” 23 September 2021.",
        "url": "https://www.exim.gov/news/first-solar-exports-zacapa-solar-energy-project-guatemala-exim-2021-deal-year",
        "annotation": "EXIM primary: USD 8.7m guarantee for First Solar panels to Zacapa 9.5 MW Guatemala. Supports first_solar_zacapa_exim_guatemala_2021.",
        "supports": ["first_solar_zacapa_exim_guatemala_2021", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — MASPV Estanzuela solar+BESS Guatemala (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "maspv_estanzuela_guatemala_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "MASPV — Estanzuela 130 MWp solar + 100 MWh BESS (Guatemala)",
        "country": "Guatemala",
        "asset": "Jul 2026: Spanish IPP MASPV signs 15-year PPAs with EEGSA and Deorsa for Estanzuela project in Zacapa — 130 MWp PV + 100 MWh BESS; company states total planned investment will exceed USD 100 million; COD before 2029; awarded under PEG-5 process. CapEx use USD 100m floor as company-stated planned investment (press). Distinct from First Solar Zacapa mill project.",
        "investment_type": "greenfield_plant",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2026-07-22",
        "year": "2026",
        "status": "active",
        "lat": "14.97",
        "lon": "-89.53",
        "geo_note": "Estanzuela / Zacapa Department (MASPV / El Digital Panamá geography).",
        "evidence": "proxy",
        "source_id": "eldigital_maspv_estanzuela_2026",
        "note": "Actor: MASPV (Spanish HQ) — allied. UNVERIFIED proxy for CapEx floor (>USD 100m company-stated via press). PPAs documented in same article.",
    },
    {
        "id": "maspv_estanzuela_guatemala_2026",
        "retrieved": "2026-10-02",
        "source_id": "eldigital_maspv_estanzuela_2026",
        "url": "https://eldigitalpanama.com/maspv-firma-el-contrato-ppa-a-15-anos-para-la-mayor-planta-solar-con-baterias-de-centroamerica/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El proyecto estará ubicado en el departamento de Zacapa y contará con 130 MWp de potencia fotovoltaica y un sistema de almacenamiento de 100 MWh. La inversión total prevista superará los 100 millones de dólares … suscritos con Empresa Eléctrica de Guatemala, S. A. (EEGSA) y Distribuidora de Electricidad de Oriente, S. A. (Deorsa)",
        "note": "Opened El Digital Panamá naming MASPV Estanzuela 130 MWp+100 MWh and >USD 100m planned investment with EEGSA/Deorsa PPAs.",
    },
    {
        "id": "eldigital_maspv_estanzuela_2026",
        "type": "press",
        "chicago": "El Digital Panamá. “MASPV Firma el Contrato PPA a 15 Años para la Mayor Planta Solar con Baterías de Centroamérica.” 2026.",
        "url": "https://eldigitalpanama.com/maspv-firma-el-contrato-ppa-a-15-anos-para-la-mayor-planta-solar-con-baterias-de-centroamerica/",
        "annotation": "Press: MASPV Estanzuela 130 MWp+100 MWh; >USD 100m planned; EEGSA/Deorsa 15-year PPAs. Supports maspv_estanzuela_guatemala_2026.",
        "supports": ["maspv_estanzuela_guatemala_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/port_cranes — ZPMC hybrid RTGs for Colon Container Terminal (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "zpmc_cct_hybrid_rtg_panama_2024",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — 12 hybrid RTGs for Colon Container Terminal (Panama)",
        "country": "Panama",
        "asset": "26 Aug 2024: Colon Container Terminal (CCT) incorporates 12 new hybrid rubber-tyred gantry cranes manufactured by ZPMC; CCT president states USD 23 million investment; units stack five-high plus one. Distinct from SSA MIT ASC/ZPMC and APMT/TIL Balboa–Cristóbal temporary concessions.",
        "investment_type": "equipment_supply",
        "value": "23000000",
        "currency": "USD",
        "value_usd": "23000000",
        "fx_usd": "1",
        "fx_date": "2024-08-26",
        "year": "2024",
        "status": "active",
        "lat": "9.35",
        "lon": "-79.88",
        "geo_note": "Colon Container Terminal, Colón Province (CCT / PortNews geography).",
        "evidence": "proxy",
        "source_id": "portnews_cct_zpmc_rtg_20240826",
        "note": "Actor: ZPMC (PRC SOE) OEM — prc; CCT terminal operator not dual-tagged. UNVERIFIED proxy: PortNews citing CCT company release for USD 23m and ZPMC manufacture.",
    },
    {
        "id": "zpmc_cct_hybrid_rtg_panama_2024",
        "retrieved": "2026-10-02",
        "source_id": "portnews_cct_zpmc_rtg_20240826",
        "url": "https://en.portnews.ru/news/367028/",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "Colon Container Terminal (CCT) has taken … incorporation of 12 new hybrid RTG … This strategic investment, amounting to $23 million … William Elliott, President of Colon Container Terminal (CCT), said: “The addition of these 12 hybrid RTG equipment, manufactured by ZPMC",
        "note": "Opened PortNews English citing CCT release: 12 ZPMC hybrid RTGs at USD 23m.",
    },
    {
        "id": "portnews_cct_zpmc_rtg_20240826",
        "type": "press",
        "chicago": "PortNews. “Colon Container Terminal Receives 12 New Rubber-Tyred Hybrid Gantry Cranes.” 26 August 2024.",
        "url": "https://en.portnews.ru/news/367028/",
        "annotation": "UNVERIFIED proxy citing CCT: 12 ZPMC hybrid RTGs; USD 23m. Supports zpmc_cct_hybrid_rtg_panama_2024.",
        "supports": ["zpmc_cct_hybrid_rtg_panama_2024", "hunt_infra_port_cranes"],
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
        "hunt_energy_wind": "Cycle 95: logged cox_santa_cruz_wind_panama_2026 (allied; CapEx blank PPA).",
        "hunt_energy_solar": "Cycle 95: logged first_solar_zacapa_exim_guatemala_2021 (U.S.; USD 8.7m EXIM).",
        "hunt_energy_other_renewables": "Cycle 95: logged maspv_estanzuela_guatemala_2026 (allied; >USD 100m proxy).",
        "hunt_infra_building_materials": "Cycle 95: equal budget; Sinoma / CHEC dense (miss).",
        "hunt_res_nickel": "Cycle 95: equal budget; BRN / Westwin dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 95: equal budget; Wabtec / Progress / PowerChina Chancay dense (miss).",
        "hunt_res_balsa": "Cycle 95: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 95: equal budget; APMT/TIL Panama already (miss).",
        "hunt_infra_engineering_epc": "Cycle 95: equal budget; Halliburton / PowerChina Vicuña dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 95: equal budget; CRCC Wismar already (miss).",
        "hunt_res_water": "Cycle 95: equal budget; desal stack dense (miss).",
        "hunt_energy_fission_smr": "Cycle 95: equal budget; CONUAR×Terra already (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 95: equal budget; EXIM/Zijin dense (miss).",
        "hunt_res_copper": "Cycle 95: equal budget; Vicuña / El Abra dense (miss).",
        "hunt_infra_port_cranes": "Cycle 95: logged zpmc_cct_hybrid_rtg_panama_2024 (PRC; USD 23m proxy).",
        "hunt_br_power_equip": "Cycle 95: equal budget; Crowley / Quanta / Excelerate dense (miss).",
        "hunt_fenb_araxa": "Cycle 95: equal budget; CMOC/CBMM dense (miss).",
        "hunt_res_graphite": "Cycle 95: equal budget; Graphcoa dense (miss). Thin dry — shift.",
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
    print("Cycle 95 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
