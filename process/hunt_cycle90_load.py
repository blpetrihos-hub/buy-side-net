#!/usr/bin/env python3
"""Cycle 90 hunt: shuffle_seed=20261090; equal budget; U.S./PRC split; thin after.

Order: nickel, copper, building_materials, bridges_roads, engineering_epc,
fission_smr, lithium, other_renewables, niobium, port_ownership, rail, solar,
power_plants_grid, water, graphite, wind, port_cranes, balsa.
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
# infrastructure/bridges_roads — CRBC East Bank Demerara Good Success–Timehri (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crbc_ebd_good_success_timehri_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Road and Bridge Corporation — East Bank Demerara Road (Good Success–Timehri)",
        "country": "Guyana",
        "asset": "Ministry of Public Works GY-L1081 East Bank Road Improvement: design-and-build contract with China Road and Bridge Corporation for ~23.7 km upgrade from Good Success to Timehri (including reconstruction/widening of bridges and culverts, drainage, lighting, sidewalks/cycle lanes); contract sum USD 75,887,907.67; 36-month term. First IDB-funded design-build road works of its kind in Guyana under Programme to Support Climate Resilient Road Infrastructure Development. Distinct from CRBC Ecuador Quinindé / Arequipa–La Joya rows.",
        "investment_type": "epc",
        "value": "75887907.67",
        "currency": "USD",
        "value_usd": "75887907.67",
        "fx_usd": "1",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "6.65",
        "lon": "-58.18",
        "geo_note": "East Bank Demerara corridor Good Success–Timehri mid-pin (MoPW project geography; Coverden campsite / Soesdyke–Timehri).",
        "evidence": "documented",
        "source_id": "mopw_ebd_foreign_projects",
        "note": "Actor: CRBC (PRC SOE) — prc. Official MoPW foreign-projects page states contract sum. Value = design-build road works face (supervision is separate Sheladia row).",
    },
    {
        "id": "crbc_ebd_good_success_timehri_2024",
        "retrieved": "2026-10-02",
        "source_id": "mopw_ebd_foreign_projects",
        "url": "https://mopw.gov.gy/about-foreign-projects",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Design-Build Road Works Contract — First contract of its kind with IDB funding in Guyana — China Road and Bridge Corporation — Contract sum US$75,887,907.67. — 36 months contract",
        "note": "Opened Guyana Ministry of Public Works foreign-projects page naming CRBC contract sum for Good Success–Timehri.",
    },
    {
        "id": "mopw_ebd_foreign_projects",
        "type": "government",
        "chicago": "Guyana Ministry of Public Works. “About Foreign Projects” (East Bank Road Improvement Project — Good Success to Timehri). Accessed 2 October 2026.",
        "url": "https://mopw.gov.gy/about-foreign-projects",
        "annotation": "Official MoPW page: CRBC design-build USD 75,887,907.67 and Sheladia supervision USD 7,967,000 for EBD Good Success–Timehri. Supports crbc_ebd_good_success_timehri_2024 and sheladia_ebd_supervision_2023.",
        "supports": [
            "crbc_ebd_good_success_timehri_2024",
            "sheladia_ebd_supervision_2023",
            "hunt_infra_bridges_roads",
            "hunt_infra_engineering_epc",
        ],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Sheladia EBD supervision (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sheladia_ebd_supervision_2023",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Sheladia Associates Inc. — East Bank Demerara Road design review & supervision",
        "country": "Guyana",
        "asset": "Ministry of Public Works GY-L1081: design review and supervision services contract with Sheladia Associates Inc. (USA) for East Bank Demerara Road Improvement (Good Success to Timehri); contract sum US$7,967,000 signed 1 December 2023; 48-month duration; already mobilized. Distinct from CRBC design-build works row on the same corridor.",
        "investment_type": "epc",
        "value": "7967000",
        "currency": "USD",
        "value_usd": "7967000",
        "fx_usd": "1",
        "fx_date": "2023-12-01",
        "year": "2023",
        "status": "active",
        "lat": "6.65",
        "lon": "-58.18",
        "geo_note": "Same East Bank Demerara Good Success–Timehri corridor as CRBC works (MoPW; supervision of full alignment).",
        "evidence": "documented",
        "source_id": "mopw_ebd_foreign_projects",
        "note": "Actor: Sheladia Associates Inc. (U.S.) — us. Official MoPW page; value = supervision contract face. Non-grid road engineering supervision.",
    },
    {
        "id": "sheladia_ebd_supervision_2023",
        "retrieved": "2026-10-02",
        "source_id": "mopw_ebd_foreign_projects",
        "url": "https://mopw.gov.gy/about-foreign-projects",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Design Review and Supervision Services — Contract already signed with Sheladia Associates Inc (USA) — Contract sum US$7,967,000 on December 1, 2023. — Duration 48 months — Already mobilized.",
        "note": "Opened MoPW foreign-projects page naming Sheladia USD 7.967m supervision contract.",
    },
    {
        "id": "mopw_ebd_foreign_projects",
        "type": "government",
        "chicago": "Guyana Ministry of Public Works. “About Foreign Projects” (East Bank Road Improvement Project — Good Success to Timehri). Accessed 2 October 2026.",
        "url": "https://mopw.gov.gy/about-foreign-projects",
        "annotation": "Official MoPW page: CRBC design-build USD 75,887,907.67 and Sheladia supervision USD 7,967,000 for EBD Good Success–Timehri. Supports crbc_ebd_good_success_timehri_2024 and sheladia_ebd_supervision_2023.",
        "supports": [
            "crbc_ebd_good_success_timehri_2024",
            "sheladia_ebd_supervision_2023",
            "hunt_infra_bridges_roads",
            "hunt_infra_engineering_epc",
        ],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — ENGIE Perú Grupo 1 transmission APP (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "engie_peru_grupo1_transmision_230m_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "ENGIE Energía Perú — Grupo 1 Plan de Transmisión 2025–2034 APP",
        "country": "Peru",
        "asset": "1 Jul 2026 ENGIE Energía Perú: awarded ProInversión PPP (buena pro) for Grupo 1 of the 2025–2034 Transmission Plan — four projects totaling >400 km lines, six new substations and expansions of ten existing substations in Piura, Lambayeque, Junín and Ayacucho (Enlace 500 kV Miguel Grau–Pariñas + SE Pariñas; Enlaces 220 kV Felam–Tierras Nuevas–Salitral; Nueva SE Palián 220/60 kV; Enlace 220 kV Muyurina–Mollepata). Offered investment USD 230.8 million; COD targeted 2031. Distinct from ENGIE Brasil Assú Sol / Asa Branca / Serra do Assuruá rows.",
        "investment_type": "concession",
        "value": "230800000",
        "currency": "USD",
        "value_usd": "230800000",
        "fx_usd": "1",
        "fx_date": "2026-07-01",
        "year": "2026",
        "status": "active",
        "lat": "-5.19",
        "lon": "-80.63",
        "geo_note": "Piura / Miguel Grau–Pariñas 500 kV primary link pin (ENGIE lists multi-department package; Piura is largest beneficiary corridor).",
        "evidence": "documented",
        "source_id": "engie_peru_grupo1_20260701",
        "note": "Actor: ENGIE Energía Perú / ENGIE (France) — allied. Company Spanish primary; value = offered investment USD 230.8m (ProInversión press also cites USD 339m program figure — use company offered amount).",
    },
    {
        "id": "engie_peru_grupo1_transmision_230m_2026",
        "retrieved": "2026-10-02",
        "source_id": "engie_peru_grupo1_20260701",
        "url": "https://engie-energia.pe/notas-de-prensa/engie-obtiene-adjudicacion-para-construir-y-operar-400-km-de-lineas-de-transmision",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El monto de inversión total ofertado para la ejecución de los proyectos asciende a USD 230.8 millones y comprende -además- el desarrollo de seis nuevas subestaciones eléctricas y la ampliación de diez subestaciones existentes.",
        "note": "Opened ENGIE Energía Perú Spanish press naming USD 230.8m offered investment for Grupo 1 TX APP.",
    },
    {
        "id": "engie_peru_grupo1_20260701",
        "type": "company",
        "chicago": "ENGIE Energía Perú. “ENGIE obtiene adjudicación para construir y operar 400 km de líneas de transmisión.” 1 July 2026.",
        "url": "https://engie-energia.pe/notas-de-prensa/engie-obtiene-adjudicacion-para-construir-y-operar-400-km-de-lineas-de-transmision",
        "annotation": "ENGIE Perú Grupo 1 transmission APP award; offered CapEx USD 230.8m. Supports engie_peru_grupo1_transmision_230m_2026.",
        "supports": ["engie_peru_grupo1_transmision_230m_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — MCC Belize Energy Project Ambergris cable (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "mcc_belize_energy_ambergris_41p7m_2024",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "MCC — Belize Compact Energy Project (Ambergris Caye HV submarine cable)",
        "country": "Belize",
        "asset": "MCC Belize Compact Energy Project totaling USD 41.7 million: high-voltage submarine transmission cable from Belize mainland to Ambergris Caye to strengthen the national transmission network and displace expensive emergency power for the rapidly growing economic zone; plus power-sector regulatory reforms (competitive PPAs, grid codes/dispatch, Energy Act). Compact signed 4 Sep 2024; Entry Into Force 18 Sep 2026. Education Project (USD 53.8m) is out of BRIEF scope — only Energy Project booked.",
        "investment_type": "financing",
        "value": "41700000",
        "currency": "USD",
        "value_usd": "41700000",
        "fx_usd": "1",
        "fx_date": "2024-09-04",
        "year": "2024",
        "status": "active",
        "lat": "17.92",
        "lon": "-87.96",
        "geo_note": "Ambergris Caye / San Pedro submarine-cable landing corridor (MCC Energy Project geography).",
        "evidence": "documented",
        "source_id": "mcc_belize_compact_page",
        "note": "Actor: U.S. Millennium Challenge Corporation — us. Official MCC program page; value = Energy Project Total Amount USD 41.7m (not full USD 125m compact).",
    },
    {
        "id": "mcc_belize_energy_ambergris_41p7m_2024",
        "retrieved": "2026-10-02",
        "source_id": "mcc_belize_compact_page",
        "url": "https://www.mcc.gov/where-we-work/program/belize-compact/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Energy Project — $41,700,000 Project Total Amount … The Energy Project aims to reduce the overall cost of electricity by installing a new high-voltage submarine cable from Belize mainland to nearby Ambergris Caye.",
        "note": "Opened MCC Belize Compact page stating Energy Project USD 41.7m and Ambergris Caye HV submarine cable.",
    },
    {
        "id": "mcc_belize_compact_page",
        "type": "government",
        "chicago": "Millennium Challenge Corporation. “Belize Compact.” Accessed 2 October 2026.",
        "url": "https://www.mcc.gov/where-we-work/program/belize-compact/",
        "annotation": "MCC Belize Compact Energy Project USD 41.7m for Ambergris Caye HV submarine cable + regulatory reforms. Supports mcc_belize_energy_ambergris_41p7m_2024.",
        "supports": ["mcc_belize_energy_ambergris_41p7m_2024", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — JA Solar Exel Solar 400 MW Mexico modules (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ja_solar_exel_400mw_mexico_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "JA Solar — 400 MW module supply to Exel Solar (Mexico)",
        "country": "Mexico",
        "asset": "14 Apr 2026 (announced 17 Apr): JA Solar signs strategic cooperation with Exel Solar at Mexico Solar and Energy Storage Expo (Guadalajara) to supply 400 MW of high-efficiency PV modules for distribution across the Mexican market. CapEx/contract USD not disclosed on opened PR Newswire. Distinct from prior JA Solar Mexico press-only misses without openable primary.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "20.66",
        "lon": "-103.35",
        "geo_note": "Guadalajara Expo announcement / national Mexico distribution (no single plant named — city process pin).",
        "evidence": "documented",
        "source_id": "prnewswire_ja_exel_400mw_20260417",
        "note": "Actor: JA Solar Technology (PRC) — prc; distributor Exel Solar (Mexico). Company PR Newswire Spanish primary. CapEx blank.",
    },
    {
        "id": "ja_solar_exel_400mw_mexico_2026",
        "retrieved": "2026-10-02",
        "source_id": "prnewswire_ja_exel_400mw_20260417",
        "url": "https://www.prnewswire.com/mx/comunicados-de-prensa/ja-solar-cierra-acuerdo-de-400-mw-con-exel-solar-para-impulsar-la-energia-solar-en-mexico-302745649.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "JA Solar suministrará a Exel Solar 400 MW de módulos solares de alta eficiencia, y Exel Solar se encargará de la distribución a gran escala de estos productos avanzados en el mercado mexicano.",
        "note": "Opened JA Solar PR Newswire Spanish release naming 400 MW Exel Solar Mexico module supply.",
    },
    {
        "id": "prnewswire_ja_exel_400mw_20260417",
        "type": "company",
        "chicago": "JA Solar Technology Co., Ltd. “JA Solar cierra acuerdo de 400 MW con Exel Solar para impulsar la energía solar en México.” PR Newswire, 17 April 2026.",
        "url": "https://www.prnewswire.com/mx/comunicados-de-prensa/ja-solar-cierra-acuerdo-de-400-mw-con-exel-solar-para-impulsar-la-energia-solar-en-mexico-302745649.html",
        "annotation": "JA Solar 400 MW module supply agreement with Exel Solar (Mexico). Supports ja_solar_exel_400mw_mexico_2026.",
        "supports": ["ja_solar_exel_400mw_mexico_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# energy/wind — Mingyang Copel / Brazil MySE orders (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "mingyang_copel_brazil_wind_2024",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Mingyang Smart Energy — Copel / Brazil MySE turbine orders",
        "country": "Brazil",
        "asset": "Mingyang 2024 ESG Report: (1) January preferred-supplier agreement for Brazilian onshore wind — 30× MySE4.0-156 + 19× MySE6.25-172 (240 MW total) plus 20-year O&M; (2) August procurement contract with Energy Company of Paraná (Copel) for MySE6.25-172 turbines, described as Mingyang’s second Brazil order, with first typhoon-resistant turbine installed in Latin America. CapEx USD not disclosed. Distinct from Goldwind / Envision / Sany Brazil–Chile wind rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-25.43",
        "lon": "-49.27",
        "geo_note": "Copel (Paraná) named buyer for second order; preferred-supplier farms unnamed — Curitiba / Paraná process pin.",
        "evidence": "documented",
        "source_id": "mingyang_esg_2024_brazil",
        "note": "Actor: Mingyang Smart Energy (PRC) — prc; Copel is Paraná state utility. Company English ESG primary. CapEx blank.",
    },
    {
        "id": "mingyang_copel_brazil_wind_2024",
        "retrieved": "2026-10-02",
        "source_id": "mingyang_esg_2024_brazil",
        "url": "https://mingyang.com/wp-content/uploads/2026/01/Ming-Yang-Smart-Energy-2024ESG-Report.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "In January, Mingyang Smart Energy signed a preferred supplier agreement with Brazilian wind power project developers, intended to supply 30 MySE4.0-156 sets and 19 MySE6.25-172 sets, with total installed capacity 240MW … In August, Mingyang Smart Energy secured its second order in the Brazilian market by signing a procurement contract with Energy Company of Paraná for MySE6.25-172 Wind Turbine.",
        "note": "Opened Mingyang 2024 ESG PDF naming Brazil 240 MW preferred supply and Copel MySE6.25-172 procurement.",
    },
    {
        "id": "mingyang_esg_2024_brazil",
        "type": "company",
        "chicago": "Mingyang Smart Energy. Ming Yang Smart Energy 2024 ESG Report. Zhongshan, 2025 (PDF posted January 2026).",
        "url": "https://mingyang.com/wp-content/uploads/2026/01/Ming-Yang-Smart-Energy-2024ESG-Report.pdf",
        "annotation": "Mingyang Brazil 240 MW preferred supplier + Copel MySE6.25-172 second order. Supports mingyang_copel_brazil_wind_2024.",
        "supports": ["mingyang_copel_brazil_wind_2024", "hunt_energy_wind"],
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
        "hunt_res_nickel": "Cycle 90: equal budget; DFC Piauí / Brazilian Nickel already (miss).",
        "hunt_res_copper": "Cycle 90: equal budget; FCX El Abra / Zijin La Arena / Southern Copper already (miss).",
        "hunt_infra_building_materials": "Cycle 90: equal budget; Sinoma / Holcim dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 90: logged crbc_ebd_good_success_timehri_2024 (PRC; USD 75.89m MoPW).",
        "hunt_infra_engineering_epc": "Cycle 90: logged sheladia_ebd_supervision_2023 (U.S.; USD 7.967m MoPW).",
        "hunt_energy_fission_smr": "Cycle 90: equal budget; USTDA / CAREM / FIRST already (miss). Thin top-up dry — shift.",
        "hunt_res_lithium": "Cycle 90: equal budget; Zijin 3Q / Atlas Neves / EXIM Argentina already (miss).",
        "hunt_energy_other_renewables": "Cycle 90: equal budget; Sungrow / AES Andes / Ormat already (miss).",
        "hunt_fenb_araxa": "Cycle 90: equal budget; CMOC / CBMM already (miss).",
        "hunt_infra_port_ownership": "Cycle 90: equal budget; COSCO / APM / SSA / DP World dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 90: equal budget; CRRC / CRCC Batuco / Wabtec already (miss).",
        "hunt_energy_solar": "Cycle 90: logged ja_solar_exel_400mw_mexico_2026 (PRC; 400 MW Exel).",
        "hunt_br_power_equip": "Cycle 90: logged engie_peru_grupo1_transmision_230m_2026 (allied) + mcc_belize_energy_ambergris_41p7m_2024 (U.S.).",
        "hunt_res_water": "Cycle 90: equal budget; NADBank Sonora / San Quintín / SADM already (miss).",
        "hunt_res_graphite": "Cycle 90: equal budget; Graphcoa / South Star / Atlas Malacacheta dense (miss). Thin top-up dry — shift.",
        "hunt_energy_wind": "Cycle 90: logged mingyang_copel_brazil_wind_2024 (PRC); Goldwind / Sany already.",
        "hunt_infra_port_cranes": "Cycle 90: equal budget; Kalmar Portonave / ZPMC Contecon / Konecranes already (miss).",
        "hunt_res_balsa": "Cycle 90: equal budget; Plantabal / AIMA dense (miss). Thin top-up dry — shift.",
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
    print("Cycle 90 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
