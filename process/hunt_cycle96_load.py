#!/usr/bin/env python3
"""Cycle 96 hunt: shuffle_seed=20261096; equal budget; U.S./PRC split; thin after.

Order (BRIEF numeric list): bridges_roads, copper, power_plants_grid, water,
nickel, building_materials, fission_smr, lithium, niobium, balsa, wind,
other_renewables, port_ownership, port_cranes, solar, rail, graphite,
engineering_epc.
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
# infrastructure/bridges_roads — CRBC Lima–Canta (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crbc_lima_canta_highway_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Road and Bridge Corporation — Lima–Canta highway reconstruction",
        "country": "Peru",
        "asset": "23 May 2025: PROVIAS NACIONAL signs Contrato N° 44-2025-MTC/20.2 with Consorcio Ejecutor Canta (China Road and Bridge Corporation Sucursal Perú + CMO Group S.A.C.) for Reconstrucción y Culminación de la Obra: Rehabilitación y Mejoramiento de la Carretera Lima – Canta - La Viuda-Unish; Tramo Lima–Canta — S/ 86,447,553.48 incl. taxes; 240 calendar days; official RD 038-2026-MTC/20 (21 Jan 2026) confirms contract terms and keeps end date 8 Apr 2026. Distinct from CRBC Arequipa–La Joya / Corentyne Lot 2.",
        "investment_type": "epc",
        "value": "86447553.48",
        "currency": "PEN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-11.47",
        "lon": "-76.62",
        "geo_note": "Lima–Canta highway corridor, Lima Region (PROVIAS geography; approximate Canta pin).",
        "evidence": "documented",
        "source_id": "mtc_rd038_lima_canta_crbc_20260121",
        "note": "Actor: China Road and Bridge Corporation (PRC SOE) — prc. Official PROVIAS/MTC Spanish primary PDF. PEN stored without FX.",
    },
    {
        "id": "crbc_lima_canta_highway_2025",
        "retrieved": "2026-10-02",
        "source_id": "mtc_rd038_lima_canta_crbc_20260121",
        "url": "https://cdn.www.gob.pe/uploads/document/file/9357697/7670928-rd_038_2026_mtc-20.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "el 23 de mayo de 2025, … PROVIAS NACIONAL y el CONSORCIO EJECUTOR CANTA, conformado por las empresas CHINA ROAD AND BRIDGE CORPORATION SUCURSAL PERÚ Y CMO GROUP S.A.C. … suscribieron el Contrato N° 44-2025-MTC/20.2 … para la ejecución de la Obra: “RECONSTRUCCIÓN Y CULMINACIÓN DE LA OBRA: REHABILITACIÓN Y MEJORAMIENTO DE LA CARRETERA LIMA – CANTA - LA VIUDA-UNISH; TRAMO: LIMA-CANTA” … por un monto ascendente a S/ 86 447 553,48 incluido todos los impuestos de Ley, con un plazo de ejecución de 240 días calendario",
        "note": "Opened official PROVIAS RD PDF naming CRBC consortium, contract number, S/ 86.45m, and 240-day term.",
    },
    {
        "id": "mtc_rd038_lima_canta_crbc_20260121",
        "type": "government",
        "chicago": "Proyecto Especial de Infraestructura de Transporte Nacional (PROVIAS NACIONAL). Resolución Directoral N.° 038-2026-MTC/20. Lima, 21 January 2026. https://cdn.www.gob.pe/uploads/document/file/9357697/7670928-rd_038_2026_mtc-20.pdf.",
        "url": "https://cdn.www.gob.pe/uploads/document/file/9357697/7670928-rd_038_2026_mtc-20.pdf",
        "annotation": "Official PROVIAS RD confirming CRBC Consorcio Ejecutor Canta Contrato N°44-2025-MTC/20.2 for Lima–Canta highway at S/86,447,553.48. Supports crbc_lima_canta_highway_2025.",
        "supports": ["crbc_lima_canta_highway_2025", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Novel Construction PR-155 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_novel_pr155_morovis_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Novel Construction LLC — FHWA Emergency Relief PR-155/PR-159 landslide repairs",
        "country": "Puerto Rico",
        "asset": "12 Dec 2024: U.S. DOT Federal Highway Administration awards firm-fixed-price contract 693C7325C000005 to Novel Construction LLC (San Juan HQ) for Project PR ER DOT PRMNT RPR(17) — repairing landslides and washouts from Hurricanes Irma and Maria on PR-155 (multiple km) and PR-159; obligated amount USD 12,048,986 after modification; performance in Morovis / Orocovis corridor; end date 13 Jun 2028. Distinct from Quanta LUMA / PREPA LM2500 rows.",
        "investment_type": "epc",
        "value": "12048986",
        "currency": "USD",
        "value_usd": "12048986",
        "fx_usd": "1",
        "fx_date": "2024-12-12",
        "year": "2024",
        "status": "active",
        "lat": "18.33",
        "lon": "-66.41",
        "geo_note": "PR-155 corridor, Morovis Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_novel_pr155_20241212",
        "note": "Actor: Novel Construction LLC (Puerto Rico / U.S.) + FHWA U.S. government Emergency Relief — us. Official USASpending award record.",
    },
    {
        "id": "fhwa_novel_pr155_morovis_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_novel_pr155_20241212",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7325C000005_6925_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(17) THE PROJECT CONSISTS OF REPAIRING LANDSLIDES AND WASHOUTS CAUSED BY HURRICANES IRMA AND MARIA ON PR-155 (KM: 37, 39.10, 40.30, 43, 43.25, 56.70, 45.50, 35, 36.15, 38.35), AND ON PR-159 (KM: 3.20, 3.50).",
        "note": "Opened USASpending Award API: Novel Construction LLC; USD 12,048,986; date_signed 2024-12-12; awarding agency DOT/FHWA.",
    },
    {
        "id": "usaspending_novel_pr155_20241212",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7325C000005_6925_-NONE-_-NONE- (Novel Construction LLC; FHWA Emergency Relief PR-155/PR-159). Signed 12 December 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7325C000005_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7325C000005_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 12.05m FHWA award to Novel Construction for PR-155/PR-159 landslide repairs. Supports fhwa_novel_pr155_morovis_2024.",
        "supports": ["fhwa_novel_pr155_morovis_2024", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA DDD-DVG Canóvanas (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_ddd_dvg_canovanas_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "DDD-DVG Joint Venture LLC — FHWA Emergency Relief design-build Canóvanas",
        "country": "Puerto Rico",
        "asset": "31 Mar 2026: U.S. DOT Federal Highway Administration awards firm-fixed-price design-build contract 693C7326C000008 to DDD-DVG Joint Venture LLC (Guaynabo) for Project PR ER PRMNT RPR(1) in Municipality of Canóvanas, Puerto Rico — highway/bridge Emergency Relief reconstruction; obligated USD 35,841,000. Distinct from Novel Construction PR-155 award.",
        "investment_type": "epc",
        "value": "35841000",
        "currency": "USD",
        "value_usd": "35841000",
        "fx_usd": "1",
        "fx_date": "2026-03-31",
        "year": "2026",
        "status": "active",
        "lat": "18.38",
        "lon": "-65.90",
        "geo_note": "Canóvanas Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_ddd_dvg_canovanas_20260331",
        "note": "Actor: DDD-DVG Joint Venture LLC (Puerto Rico / U.S.) + FHWA — us. Official USASpending award record.",
    },
    {
        "id": "fhwa_ddd_dvg_canovanas_2026",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_ddd_dvg_canovanas_20260331",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000008_6925_-NONE-_-NONE-/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "THIS IS A REQUEST FOR PROPOSAL (DESIGN BUILD) PROJECT NO. PR ER PRMNT RPR(1), LOCATED IN THE MUNICIPALITY OF CANOVANAS, PUERTO RICO",
        "note": "Opened USASpending Award API: DDD-DVG JV; USD 35,841,000; date_signed 2026-03-31; Canóvanas PR.",
    },
    {
        "id": "usaspending_ddd_dvg_canovanas_20260331",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7326C000008_6925_-NONE-_-NONE- (DDD-DVG Joint Venture LLC; FHWA Emergency Relief Canóvanas). Signed 31 March 2026. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000008_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7326C000008_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 35.84m FHWA design-build award in Canóvanas PR. Supports fhwa_ddd_dvg_canovanas_2026.",
        "supports": ["fhwa_ddd_dvg_canovanas_2026", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — ACCIONA Cagepa Paraíba (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "acciona_cagepa_paraiba_498m_eur_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "ACCIONA — Cagepa Paraíba sewerage PPP (85 municipalities)",
        "country": "Brazil",
        "asset": "2026: ACCIONA signs 25-year PPP with Companhia de Água e Esgotos da Paraíba (Cagepa) for sanitary sewerage in 85 municipalities (Litoral incl. João Pessoa + Alto Piranhas incl. Cajazeiras) — ~104 WWTPs and 2,800 km collection networks; planned investment approximately EUR 498 million; serves >1.7 million people; Cagepa retains water supply/customer service. Distinct from ACCIONA/BRK Pernambuco water+sewer concession.",
        "investment_type": "ppp_concession",
        "value": "498000000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-7.12",
        "lon": "-34.88",
        "geo_note": "João Pessoa / Paraíba Litoral concession geography (company signing location).",
        "evidence": "documented",
        "source_id": "acciona_paraiba_cagepa_2026",
        "note": "Actor: ACCIONA (Spain) — allied. Company English primary. EUR CapEx stored without FX. Distinct from acciona_brk_pernambuco_sanitation_2026.",
    },
    {
        "id": "acciona_cagepa_paraiba_498m_eur_2026",
        "retrieved": "2026-10-02",
        "source_id": "acciona_paraiba_cagepa_2026",
        "url": "https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-85-municipalities-paraiba-brasil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ACCIONA has signed a public-private partnership (PPP) contract with the Paraíba Water and Sewerage Company (Cagepa) to provide sanitary sewerage services in 85 municipalities in the state of Paraíba. … With a 25-year term and planned investment of approximately €498 million … construction of 104 wastewater treatment plants (WWTPs) and the installation of 2,800 kilometers of sewerage collection networks.",
        "note": "Opened ACCIONA English release naming Cagepa PPP, 85 municipalities, EUR 498m, 104 WWTPs.",
    },
    {
        "id": "acciona_paraiba_cagepa_2026",
        "type": "company",
        "chicago": "ACCIONA. “ACCIONA Signs Sanitation Contract for 85 Municipalities in Paraíba, Brasil.” 2026. https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-85-municipalities-paraiba-brasil.",
        "url": "https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-85-municipalities-paraiba-brasil",
        "annotation": "ACCIONA primary: Cagepa Paraíba sewerage PPP ~EUR 498m / 85 municipalities. Supports acciona_cagepa_paraiba_498m_eur_2026.",
        "supports": ["acciona_cagepa_paraiba_498m_eur_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# resources/lithium — Yahua / Grand Chen Bandeira offtake (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "yahua_grandchen_bandeira_offtake_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Sichuan Yahua / Grand Chen — Bandeira spodumene offtake + USD 20m prepayment",
        "country": "Brazil",
        "asset": "25 Mar 2026 Lithium Ionic release: binding five-year take-or-pay offtakes with Sichuan Yahua Industrial Group Co., Ltd. (PRC; one of world’s largest LiOH producers) and Grand Chen Resources Pte. Ltd. for combined 170,000 tpa SC6 spodumene concentrate from Bandeira Lithium Project, Minas Gerais; min price USD 1,000/t SC6; aggregate USD 20 million pre-payment facility subject to definitive agreements. Distinct from lithium_ionic_exim_loi_266m_2024 and hatch_bandeira_lithium_epc_2024.",
        "investment_type": "offtake",
        "value": "20000000",
        "currency": "USD",
        "value_usd": "20000000",
        "fx_usd": "1",
        "fx_date": "2026-03-25",
        "year": "2026",
        "status": "active",
        "lat": "-16.75",
        "lon": "-43.87",
        "geo_note": "Bandeira Lithium Project, Araçuaí / Minas Gerais Lithium Valley (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "lithium_ionic_yahua_offtake_20260325",
        "note": "Actor: Sichuan Yahua (PRC) + Grand Chen (offtake buyers) — prc (Yahua HQ). Value stores disclosed USD 20m combined prepayment; offtake volume 170 ktpa without total revenue CapEx. Seller Lithium Ionic is Canadian.",
    },
    {
        "id": "yahua_grandchen_bandeira_offtake_2026",
        "retrieved": "2026-10-02",
        "source_id": "lithium_ionic_yahua_offtake_20260325",
        "url": "https://www.lithiumionic.com/_resources/news/nr-20260325.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Lithium Ionic will supply a combined 170,000 tonnes per annum of spodumene concentrate under five-year binding take-or-pay offtake agreements to Yahua Group and Grand Chen … Minimum price of US$1,000/t (6% spodumene concentrate grade basis …) … US$20 million combined pre-payment facility associated with the offtake agreements",
        "note": "Opened Lithium Ionic PDF naming Yahua/Grand Chen offtakes, 170 ktpa, USD 20m prepayment.",
    },
    {
        "id": "lithium_ionic_yahua_offtake_20260325",
        "type": "company",
        "chicago": "Lithium Ionic Corp. “Lithium Ionic Secures Offtake Agreements with Leading Integrated Lithium Producers … for Bandeira Project Production.” 25 March 2026. https://www.lithiumionic.com/_resources/news/nr-20260325.pdf.",
        "url": "https://www.lithiumionic.com/_resources/news/nr-20260325.pdf",
        "annotation": "Lithium Ionic primary: Yahua/Grand Chen 170 ktpa Bandeira offtake + USD 20m prepayment. Supports yahua_grandchen_bandeira_offtake_2026.",
        "supports": ["yahua_grandchen_bandeira_offtake_2026", "hunt_res_lithium"],
    },
)


def upsert_bib(bib, bib_by, entry):
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
        "hunt_infra_bridges_roads": "Cycle 96: logged crbc_lima_canta_highway_2025 (PRC) + fhwa_novel_pr155_morovis_2024 + fhwa_ddd_dvg_canovanas_2026 (U.S.).",
        "hunt_res_copper": "Cycle 96: equal budget; FCX El Abra / Capstone Mantoverde / Vicuña dense (miss).",
        "hunt_br_power_equip": "Cycle 96: equal budget; GE Vernova / PowerChina / EXIM GTE dense (miss).",
        "hunt_res_water": "Cycle 96: logged acciona_cagepa_paraiba_498m_eur_2026 (allied; EUR 498m).",
        "hunt_res_nickel": "Cycle 96: equal budget; BRN / Centaurus / Westwin dense (miss). Thin dry — shift.",
        "hunt_infra_building_materials": "Cycle 96: equal budget; Holcim Pacasmayo / Sinoma dense (miss).",
        "hunt_energy_fission_smr": "Cycle 96: equal budget; CONUAR×Terra already (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 96: logged yahua_grandchen_bandeira_offtake_2026 (PRC; USD 20m prepay).",
        "hunt_fenb_araxa": "Cycle 96: equal budget; CMOC/CBMM dense (miss).",
        "hunt_res_balsa": "Cycle 96: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_energy_wind": "Cycle 96: equal budget; Cox Santa Cruz / AES JK dense (miss).",
        "hunt_energy_other_renewables": "Cycle 96: equal budget; AES Andes / MASPV dense (miss).",
        "hunt_infra_port_ownership": "Cycle 96: equal budget; APMT/TIL/Cosco dense (miss).",
        "hunt_infra_port_cranes": "Cycle 96: equal budget; ZPMC CCT / Tecon Santos dense (miss).",
        "hunt_energy_solar": "Cycle 96: equal budget; First Solar Zacapa / AES DR dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 96: equal budget; PowerChina Chancay / CRCC Batuco dense (miss).",
        "hunt_res_graphite": "Cycle 96: equal budget; Graphcoa / South Star dense (miss). Thin dry — shift.",
        "hunt_infra_engineering_epc": "Cycle 96: equal budget; Halliburton / CHEC Chancay dense (miss).",
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
    print("Cycle 96 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
