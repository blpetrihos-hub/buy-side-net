#!/usr/bin/env python3
"""Cycle 132 hunt: shuffle_seed=20261132; equal budget; U.S./PRC split; thin after.

Order: bridges_roads, wind, building_materials, fission_smr, nickel, rail,
other_renewables, copper, solar, water, port_ownership, power_plants_grid,
lithium, balsa, engineering_epc, niobium, port_cranes, graphite.

PRC push (still slightly behind US post-audit). Thin top-up: balsa/graphite/nickel.
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


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. bridges_roads / prc — CCECC Cajamarca highland highway rehab (Peru)
row_doc(
    "ccecc_cajamarca_highway_246km_2026",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Civil Engineering Construction Corporation (CCECC) — Cajamarca Region highway rehab/maintenance (~246 km)",
    "Peru",
    "3 Aug 2026 Belt and Road / People’s Daily report (opened BRI portal): CCECC-built Cajamarca highland highway rehabilitation and maintenance project passes acceptance; ~246 km of upgraded asphalt roads at 1,500–2,800 m elevation connecting remote Andean villages; benefits cited as 32 communities / 200,000+ residents (Cutervo mayor quoted). CapEx USD not disclosed on opened page. Distinct from CCECC Quinto Puente / Querétaro–Irapuato rows.",
    "",
    "",
    "2026",
    "-6.37",
    "-78.65",
    "Cajamarca Region highland corridor / Cutervo area (BRI geography; approximate).",
    "bri_ccecc_cajamarca_highway_20260803",
    "日前，由中国土木工程集团有限公司承建的秘鲁卡哈马卡大区公路改造与维护项目顺利通过交验。该项目位于秘鲁高原山区，沿线海拔在1500米至2800米之间。改造维护后的公路全长约246公里",
    "https://www.yidaiyilu.gov.cn/p/0I8FISU5.html",
    "Actor: CCECC / China Civil Engineering (PRC SOE) — prc. Official Belt and Road portal reprint of People’s Daily. CapEx blank.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="press",
    chicago="Belt and Road Portal / People’s Daily. “中企承建秘鲁高原公路改造与维护项目惠及20余万人.” 3 August 2026. https://www.yidaiyilu.gov.cn/p/0I8FISU5.html.",
    annotation="BRI portal primary (People’s Daily). Supports ccecc_cajamarca_highway_246km_2026.",
    evid_note="Opened BRI Chinese page; CCECC Cajamarca ~246 km acceptance; CapEx blank.",
)

# 2. bridges_roads / prc — CRCC Demerara River Bridge opens to traffic
row_doc(
    "crcc_demerara_bridge_open_2025",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Railway Construction Corporation (International) — New Demerara River Bridge opening (Georgetown)",
    "Guyana",
    "5 Oct 2025 (SASAC English 15 Oct): New Demerara River Bridge constructed by CRCCI opens to traffic; ~2,900 m dual-tower double-cable-plane prestressed concrete cable-stayed bridge with 300 m main span, four lanes, design speed 80 km/h; claimed 75% cut in cross-river travel time and doubled navigational capacity. Opening milestone distinct from crcc_demerara_bridge_2022 award (~USD 260m) and boc_demerara_bridge_loan rows — CapEx not restated on opening page.",
    "",
    "",
    "2025",
    "6.81",
    "-58.17",
    "New Demerara River Bridge, Georgetown corridor (SASAC geography).",
    "sasac_crcc_demerara_open_20251015",
    "The New Demerara River Bridge in Guyana, constructed by China Railway Construction Corporation (International) Limited (CRCCI), was officially opened to traffic on October 5 local time.",
    "http://en.sasac.gov.cn/2025/10/15/c_19909.htm",
    "Actor: CRCC International (PRC SOE) — prc. Official SASAC English primary. CapEx blank (award already priced on 2022 row).",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="company",
    chicago="State-owned Assets Supervision and Administration Commission of the State Council (SASAC). “New Demerara River Bridge in Guyana Opens to Traffic.” English news, 15 October 2025. http://en.sasac.gov.cn/2025/10/15/c_19909.htm.",
    annotation="SASAC English primary. Supports crcc_demerara_bridge_open_2025.",
    evid_note="Opened SASAC English page; Demerara bridge opened 5 Oct 2025; CapEx blank.",
)

# 3. wind / prc — Goldwind Río Cullen hybrid (Argentina)
row_doc(
    "goldwind_rio_cullen_argentina_2026",
    "energy",
    "wind",
    "prc",
    "Goldwind — Río Cullen off-grid wind + storage (2× GW136-4.2 MW) for TotalEnergies (Tierra del Fuego)",
    "Argentina",
    "15 Jun 2026 Goldwind PR Newswire (Portuguese/LatAm wire): TotalEnergies partners with Goldwind on Río Cullen wind-plus-storage project on Isla Grande de Tierra del Fuego; two GW136-4.2 MW turbines with BESS in off-grid architecture generating ~50 GWh/year (~half of nearby industrial electricity needs). Distinct from goldwind_pemuco / Sento Sé / FINAME Brazil rows. CapEx USD not on opened wire.",
    "",
    "",
    "2026",
    "-52.82",
    "-68.33",
    "Río Cullen / Cañadón Alfa area, Tierra del Fuego (~130 km N of Río Grande; Goldwind/TotalEnergies geography; approximate).",
    "goldwind_3gw_south_america_pr_20260615",
    "Na Isla Grande de Tierra del Fuego, na Argentina, a ilha mais ao sul do mundo fora da Antártida e lar de um ecossistema subantártico único, a TotalEnergies fez parceria com a Goldwind no projeto Río Cullen de vento mais armazenamento. Duas turbinas GW136-4.2MW trabalham em conjunto com um sistema de armazenamento em baterias",
    "https://www.prnewswire.com/br/comunicados-para-a-imprensa/goldwind-ultrapassa-3-gw-de-capacidade-instalada-na-america-do-sul-302799977.html",
    "Actor: Goldwind (PRC) turbine OEM — prc; offtaker/operator TotalEnergies (allied) not dual-tagged. Company PR Newswire primary (FONTE Goldwind). CapEx blank.",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    bib_type="company",
    chicago="Goldwind. “Goldwind ultrapassa 3 GW de capacidade instalada na América do Sul.” PR Newswire (Brazil), 15 June 2026. https://www.prnewswire.com/br/comunicados-para-a-imprensa/goldwind-ultrapassa-3-gw-de-capacidade-instalada-na-america-do-sul-302799977.html.",
    annotation="Goldwind PR Newswire primary. Supports goldwind_rio_cullen_argentina_2026.",
    evid_note="Opened Goldwind PR Newswire; Río Cullen 2×4.2 MW + BESS named; CapEx blank.",
)

# 4. wind / prc — Goldwind Kallpa 342 MW Chile (ENGIE)
row_doc(
    "goldwind_kallpa_chile_342mw_2026",
    "energy",
    "wind",
    "prc",
    "Goldwind — Kallpa 342 MW wind farm (57× GW165-6.0 MW) with ENGIE Chile (Atacama)",
    "Chile",
    "15 Jun 2026 Goldwind PR Newswire: Kallpa 342 MW wind farm in Atacama Desert co-developed with ENGIE Chile — 57 GW165-6.0 MW turbines; >1 year stable operation cited with 98.53% availability and >800 GWh/year generation. Distinct from goldwind_pemuco_chile and Chequenes milestone on same wire. CapEx USD not on opened page.",
    "",
    "",
    "2026",
    "-24.50",
    "-69.25",
    "Kallpa wind farm, Atacama Desert (Goldwind/ENGIE geography; approximate).",
    "goldwind_3gw_south_america_pr_20260615",
    "Localizado no altamente sísmico Deserto do Atacama, no Chile, o parque eólico Kallpa de 342 MW — composto por 57 turbinas GW165-6.0MW desenvolvidas em conjunto com a ENGIE Chile — mantém operações estáveis há mais de um ano. Ele alcançou uma impressionante disponibilidade de 98,53%",
    "https://www.prnewswire.com/br/comunicados-para-a-imprensa/goldwind-ultrapassa-3-gw-de-capacidade-instalada-na-america-do-sul-302799977.html",
    "Actor: Goldwind (PRC) — prc; partner ENGIE Chile (allied) not dual-tagged. Same Goldwind PR Newswire primary as Río Cullen (multi-asset wire). CapEx blank.",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    bib_type="company",
    chicago="Goldwind. “Goldwind ultrapassa 3 GW de capacidade instalada na América do Sul.” PR Newswire (Brazil), 15 June 2026. https://www.prnewswire.com/br/comunicados-para-a-imprensa/goldwind-ultrapassa-3-gw-de-capacidade-instalada-na-america-do-sul-302799977.html.",
    annotation="Goldwind PR Newswire primary (Kallpa tranche). Supports goldwind_kallpa_chile_342mw_2026.",
    evid_note="Opened Goldwind PR Newswire; Kallpa 342 MW / 57×6.0 MW named; CapEx blank.",
)

# 5. lithium / prc — CBC/YLB Uyuni DLE USD 1.03bn service contract
row_doc(
    "cbc_ylb_uyuni_dle_1p03bn_2024",
    "resources",
    "lithium",
    "prc",
    "Hong Kong CBC Investment (CATL–BRUNP–CMOC) — YLB Uyuni DLE lithium carbonate plants (USD 1.03bn)",
    "Bolivia",
    "Nov 2024 (YLB official 21 Oct 2025 recapitulation): YLB and Hong Kong CBC sign service contract for two EDL/DLE lithium-carbonate plants at Salar de Uyuni (10,000 tpa residual-brine + 25,000 tpa well-brine; staggered 35,000 tpa) with investment USD 1.030 billion; YLB selection page (10 Jul 2025) confirms CBC = Catl Brunp & Cmoc consortium. Contracts remitted to Legislative Assembly Nov 2024 and remain pending approval as of YLB release — UNVERIFIED as to construction start. Distinct from cmec_uyuni evaporitic plant completion.",
    "1030000000",
    "2024-11-01",
    "2024",
    "-20.133",
    "-67.489",
    "Salar de Uyuni, Potosí (YLB geography).",
    "ylb_arce_cbc_uyuni_20251021",
    "Luego, en noviembre de ese año, YLB y la empresa china Hong Kong CBC suscribieron otro contrato para el emplazamiento de dos plantas de producción de carbonato de litio, también con tecnología EDL, de 10.000 y 25.000 toneladas anuales de capacidad con una inversión de $us 1.030 millones.",
    "https://www.ylb.gob.bo/index.php/nota_prensa/presidente-arce-espera-que-paz-mantenga-los-contratos-para-industrializar-el-litio-porque-son-favorables/",
    "Actor: Hong Kong CBC / CATL–BRUNP–CMOC (PRC) — prc; counterpart YLB (Bolivia). Official YLB press. Value = USD 1.03bn contract investment (pending Assembly approval — construction not verified on page).",
    "hunt_res_lithium",
    investment_type="epc",
    evidence="proxy",
    bib_type="government",
    chicago="Yacimientos de Litio Bolivianos (YLB). “Arce espera que el próximo gobierno mantenga los contratos para industrializar el litio porque son favorables.” Nota de prensa, 21 October 2025. https://www.ylb.gob.bo/index.php/nota_prensa/presidente-arce-espera-que-paz-mantenga-los-contratos-para-industrializar-el-litio-porque-son-favorables/.",
    annotation="YLB official press. Supports cbc_ylb_uyuni_dle_1p03bn_2024.",
    evid_note="Opened YLB Spanish press; USD 1.03bn CBC Uyuni DLE contract; Assembly pending — proxy evidence.",
)

# 6. lithium / prc — CMEC Uyuni lithium carbonate plant completion
row_doc(
    "cmec_uyuni_lithium_plant_bolivia_2023",
    "resources",
    "lithium",
    "prc",
    "CMEC (Sinomach) — Uyuni battery-grade lithium carbonate plant (15,000 tpa) completion",
    "Bolivia",
    "29 Dec 2023 Sinomach English: CMEC concludes construction of Uyuni lithium carbonate plant — Bolivia’s first salt-lake lithium extraction facility; battery-grade line capacity 15,000 tpa; completion ceremony attended by President Luis Arce. Distinct from CBC DLE USD 1.03bn service contract (still pending Assembly). CapEx USD not on opened Sinomach page.",
    "",
    "",
    "2023",
    "-20.133",
    "-67.489",
    "Uyuni salt-flat industrial complex, Potosí (Sinomach/CMEC geography).",
    "sinomach_cmec_uyuni_lithium_20231229",
    "Sinomach subsidiary China Machinery Engineering Corporation (CMEC) has concluded construction of the Uyuni lithium carbonate plant in Bolivia. The cutting-edge facility boasts a battery-grade lithium carbonate production line capable of generating an impressive annual output of 15,000 tons.",
    "https://www.sinomach.com.cn/en/MediaCenter/News/202401/t20240111_428584.html",
    "Actor: CMEC / Sinomach (PRC SOE) — prc. Company English primary. CapEx blank.",
    "hunt_res_lithium",
    investment_type="epc",
    bib_type="company",
    chicago="Sinomach / China Machinery Engineering Corporation. “Sinomach CMEC completes Uyuni Lithium plant in Bolivia.” Company English news, 29 December 2023. https://www.sinomach.com.cn/en/MediaCenter/News/202401/t20240111_428584.html.",
    annotation="Sinomach English primary. Supports cmec_uyuni_lithium_plant_bolivia_2023.",
    evid_note="Opened Sinomach English page; CMEC Uyuni 15,000 tpa plant completed; CapEx blank.",
)

# 7. lithium / prc — Zijin Tres Quebradas Phase 1 COD 20ktpa
row_doc(
    "zijin_tres_quebradas_phase1_cod_2025",
    "resources",
    "lithium",
    "prc",
    "Zijin Mining — Tres Quebradas Phase 1 lithium carbonate COD (20,000 tpa, Catamarca)",
    "Argentina",
    "12 Sep 2025 (Zijin English 16 Sep): Zijin celebrates start of production at Tres Quebradas (3Q) lithium project in Fiambalá, Catamarca — Phase 1 initial capacity 20,000 tpa lithium carbonate; Phase II permitting underway to add 40,000 tpa adsorption DLE (combined 60–80 ktpa design). Distinct from zijin_liex_tres_quebradas_rigi_2026 (RIGI Phase II assets USD 594m). CapEx for Phase 1 COD not restated on opened page.",
    "",
    "",
    "2025",
    "-27.48",
    "-68.08",
    "Tres Quebradas / Fiambalá, Catamarca (Zijin geography).",
    "zijin_tres_quebradas_cod_20250916",
    "On September 12, 2025, Zijin Mining, a major global metals miner, celebrated the start of production at its Tres Quebradas lithium project, which has an initial Phase 1 production capacity of 20,000 tonnes of lithium carbonate per year.",
    "https://www.zijinmining.com/news/news-detail-122311.htm",
    "Actor: Zijin Mining (PRC) — prc. Official company English news. CapEx blank (RIGI Phase II priced separately).",
    "hunt_res_lithium",
    investment_type="ownership_equity",
    bib_type="company",
    chicago="Zijin Mining Group Co., Ltd. “Zijin Commences Production at 20,000-tonne-per-annum Lithium Carbonate Project in Argentina.” Company English news, 16 September 2025. https://www.zijinmining.com/news/news-detail-122311.htm.",
    annotation="Zijin English primary. Supports zijin_tres_quebradas_phase1_cod_2025.",
    evid_note="Opened Zijin English page; Phase 1 20ktpa COD 12 Sep 2025; CapEx blank.",
)

# 8. water / us — Freeport El Abra desal + aqueduct (component of Continuidad Operacional)
row_doc(
    "fcx_el_abra_desal_aqueduct_2026",
    "resources",
    "water",
    "us",
    "Freeport-McMoRan / Minera El Abra — desalination plant + water conveyance (Continuidad Operacional)",
    "Chile",
    "18 Mar 2026 Minera El Abra company release: Continuidad Operacional SEIA filing includes a desalination plant and water pumping/conveyance system alongside new concentrator, thickened tailings, mine expansion, and leach continuity; preliminary total project investment ~USD 7.5 billion (Full CapEx already logged under fcx_el_abra_mill_chile_2026 copper row — desal share not separately disclosed). Freeport 51% / Codelco 49%. Water-transition presence row only; CapEx blank to avoid double-count.",
    "",
    "",
    "2026",
    "-22.19",
    "-68.85",
    "El Abra mine / Tocopilla coastal desal corridor (company geography; approximate).",
    "el_abra_continuidad_seia_20260318",
    "La inversión preliminar estimada del proyecto asciende aproximadamente a US$7.500 millones e incluye el desarrollo de una planta concentradora, una planta desalinizadora y un sistema de impulsión de agua, un depósito de relaves espesados, la expansión de la mina y la continuidad de las operaciones de lixiviación.",
    "https://www.elabra.cl/minera-el-abra-filial-de-freeport-mcmoran-ingresa-proyecto-de-continuidad-operacional-para-evaluacion-ambiental/",
    "Actor: Freeport-McMoRan (NYSE:FCX; U.S. HQ) via Minera El Abra — us. Company Spanish primary. CapEx blank (desal share undisclosed; full USD 7.5bn on copper row).",
    "hunt_res_water",
    investment_type="epc",
    bib_type="company",
    chicago="Minera El Abra / Freeport-McMoRan. “Minera El Abra, filial de Freeport-McMoRan ingresa Proyecto de Continuidad Operacional para evaluación ambiental.” Company news, 18 March 2026. https://www.elabra.cl/minera-el-abra-filial-de-freeport-mcmoran-ingresa-proyecto-de-continuidad-operacional-para-evaluacion-ambiental/.",
    annotation="El Abra company primary. Supports fcx_el_abra_desal_aqueduct_2026.",
    evid_note="Opened El Abra Spanish page; desal + impulsión named in SEIA package; CapEx blank.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
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

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 132 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
