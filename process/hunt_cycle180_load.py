#!/usr/bin/env python3
"""Cycle 180 hunt: shuffle_seed=20261180; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261180)):
rail, other_renewables, water, nickel, lithium, copper, bridges_roads,
graphite, port_ownership, engineering_epc, niobium, power_plants_grid,
balsa, building_materials, fission_smr, solar, wind, port_cranes.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (Plantabal/AIMA/WITS Ecuador balsa; Centaurus/BRN/Atlantic/
Fenix nickel; Meitner/Colombia/Peru FIRST fission already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
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
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
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


# Shuffle lead: rail — catalog dense (Wabtec/Progress Rail/PowerChina Chancay logged);
# Corentyne/CCECC Nicaragua still unsigned MoU/prefeasibility.

# 1. water / us — NADBank CESPT Tijuana sewer grant
row_doc(
    "nadbank_cespt_tijuana_sewer_4p2m_2026",
    "resources",
    "water",
    "us",
    "NADBank / CESPT — Tijuana River area sewer-line rehabilitation grant (USD 4.2m)",
    "Mexico",
    "27 Apr 2026 (NADBank): at ground-breaking for Lift Stations PB1A/PB1B rehabilitation, NADBank and Comisión Estatal de Servicios Públicos de Tijuana (CESPT) execute a grant agreement for replacement of 35,708 ft of deteriorated wastewater pipeline in 13 critical sections of the Tijuana River collection system to prevent sewage spills into the Tijuana River. Grant face = USD 4.2m. Distinct from broader BEIF PB1/PBCILA package (USD 13.44m BEIF + Mexican co-finance for USD 30.9m total project).",
    "4200000",
    "2026-04-27",
    "2026",
    "32.5149",
    "-117.0382",
    "Tijuana River wastewater corridor / CESPT collection system, Baja California (NADBank geography; approximate municipal pin).",
    "nadbank_cespt_tijuana_sewer_20260427",
    "During the event, the North American Development Bank (NADBank) and the local water utility, Comisión Estatal de Servicios Públicos de Tijuana (CESPT) executed a grant agreement to support a new project involving the replacement of 35,708 ft of deteriorated pipeline in 13 critical sections of the wastewater collection system… The US$4.2-million grant agreement signed by NADBank and CESPT will provide funding for the rehabilitation of sewer lines in the Tijuana River area.",
    "https://nadbank.org/news/press-release/ground-broken-to-rehabilitate-additional-wastewater-collection-and-conveyance-infrastructure-in-the-tijuana-river-area-of-baja-california",
    "Actor: NADBank (U.S.–Mexico binational; catalogued us) grant to CESPT — us. Opened NADBank English release 27 Apr 2026. U.S. side-balance water.",
    "hunt_cycle180",
    investment_type="grant",
    evidence="documented",
    bib_type="government",
    chicago='North American Development Bank. “Ground broken to rehabilitate additional wastewater collection and conveyance infrastructure in the Tijuana River Area of Baja California.” April 27, 2026. https://nadbank.org/news/press-release/ground-broken-to-rehabilitate-additional-wastewater-collection-and-conveyance-infrastructure-in-the-tijuana-river-area-of-baja-california.',
    annotation="NADBank: CESPT Tijuana sewer grant USD 4.2m. Supports nadbank_cespt_tijuana_sewer_4p2m_2026.",
    evid_note="Opened NADBank press release 2026-10-04.",
)

# 2. copper / us — Caterpillar via Finning for Glencore Alumbrera restart
row_doc(
    "caterpillar_finning_alumbrera_250m_2026",
    "resources",
    "copper",
    "us",
    "Caterpillar / Finning — Alumbrera (Glencore/MARA) Cat 793 fleet + services (~USD 250m UNVERIFIED)",
    "Argentina",
    "Feb–Jul 2026: Finning Q1 2026 primary (12 May 2026) confirms South America received a large Glencore order for Alumbrera copper-mine restart — >20 large Caterpillar mining trucks + ancillary equipment and technology support, delivery Q4 2026–2028. Panorama Minero / Finning Argentina detail (Jul 2026): integrated contract ~USD 250m for 22 new Cat units (22× Cat 793 trucks; 3× Cat 6060 FS shovels; D11 / 777 / 336 auxiliaries) plus maintenance covering 51 machines (incl. 29 on-site) and MineStar Fleet; 5-year 24/7 support; >180 jobs. CapEx = USD 250m UNVERIFIED proxy (trade press citing Finning Argentina); equipment scope documented by Finning IR.",
    "250000000",
    "2026-07-21",
    "2026",
    "-27.32",
    "-66.61",
    "Minera Alumbrera, Catamarca Province, Argentina (MARA / Glencore restart site; approximate mine pin).",
    "panorama_finning_alumbrera_250m_20260721",
    "According to the company, the agreement is valued at approximately US$250 million and covers both equipment and associated services. The contract includes the delivery of 22 new Caterpillar units and a maintenance agreement covering a total fleet of 51 machines, including 29 units already operating at the site. Among the new equipment are 22 Cat 793 mining trucks, three Cat 6060 FS hydraulic shovels…",
    "https://www.panorama-minero.com/en/news/alumbrera-awards-us-250-million-fleet-and-services-contract-to-finning",
    "UNVERIFIED CapEx proxy. Actor: Caterpillar Inc. (U.S.) via Finning (Cat dealer) for Glencore/MARA Alumbrera — us. Finning Q1 2026 IR corroborates >20 Cat trucks order (no USD on IR page). Opened Panorama Minero EN 21 Jul 2026 + Finning Q1 release.",
    "hunt_cycle180",
    investment_type="equipment_supply",
    evidence="unverified",
    bib_type="press",
    chicago='Panorama Minero. “Alumbrera Awards US$250 Million Fleet and Services Contract to Finning.” July 21, 2026. https://www.panorama-minero.com/en/news/alumbrera-awards-us-250-million-fleet-and-services-contract-to-finning.',
    annotation="Panorama Minero citing Finning: Alumbrera Cat fleet ~USD 250m. Supports caterpillar_finning_alumbrera_250m_2026.",
    evid_note="Opened Panorama Minero EN 2026-10-04; Finning Q1 2026 IR corroborates equipment order without USD face.",
)

# 3. bridges_roads / allied — World Bank Guyana ITC USD 156m
row_doc(
    "wb_guyana_itc_156m_2025",
    "infrastructure",
    "bridges_roads",
    "allied",
    "World Bank / IDA — Guyana Integrated Transport Corridors Project (USD 156m)",
    "Guyana",
    "27–28 Feb 2025 (World Bank Board): approves USD 156 million Integrated Transport Corridors Project (P501759) to upgrade/rehabilitate selected road corridors for climate resilience and road safety — drainage, slope stabilization, embankment raising, crash barriers, NMT lanes, road-asset management. Funded through IDA. Financing agreement later signed 14 Oct 2025 (GoG/IDA). CapEx = USD 156m Board approval face. Distinct from CRBC Corentyne (unsigned) / CRCC Demerara bridge.",
    "156000000",
    "2025-02-27",
    "2025",
    "",
    "",
    "Selected Guyana road corridors (WB press; no single named site pin — lat/lon left blank).",
    "wb_guyana_itc_pr_20250228",
    "Washington, D.C., February 27, 2025 - The World Bank’s Board of Executive Directors approved a new project to support Guyana in upgrading and rehabilitating the country’s road infrastructure. The $156 million Integrated Transport Corridors Project will focus on enhancing Guyana’s transport network in selected regions, ensuring it is better equipped to withstand natural hazards and provide safer, more reliable mobility for people… The project is funded through the World Bank’s International Development Association…",
    "https://www.worldbank.org/en/news/press-release/2025/02/28/guyana-to-enhance-transport-resilience-and-safety",
    "Actor: World Bank / IDA — allied. Opened WB English press release 28 Feb 2025. Guyana under-covered bridges_roads cell.",
    "hunt_cycle180",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='World Bank. “Guyana to Enhance Transport Resilience and Safety.” February 28, 2025. https://www.worldbank.org/en/news/press-release/2025/02/28/guyana-to-enhance-transport-resilience-and-safety.',
    annotation="WB Board: Guyana ITC USD 156m IDA. Supports wb_guyana_itc_156m_2025.",
    evid_note="Opened World Bank press release 2026-10-04.",
)

# 4. copper / allied — Sandvik Codelco Chuquicamata 13× LH515i
row_doc(
    "sandvik_codelco_chuqui_lh515i_13_2026",
    "resources",
    "copper",
    "allied",
    "Sandvik — 13 Toro LH515i LHD loaders for Codelco Chuquicamata Underground",
    "Chile",
    "31 Mar 2026 (Sandvik Mining press): awarded significant order from Codelco for Chuquicamata Underground — supply of 13 Toro LH515i 15-metric-ton LHD loaders; deliveries began Mar 2026 through Nov 2027 for new panel / MB S04 ramp-up; order includes capital spares, training, advisory services; AutoMine-ready. CapEx blank (not disclosed).",
    "",
    "",
    "2026",
    "-22.31",
    "-68.93",
    "Chuquicamata Underground, Codelco Chuquicamata Division, Antofagasta Region (Sandvik/Codelco geography; approximate mine pin).",
    "sandvik_codelco_chuqui_lh515i_20260331",
    "Sandvik has been awarded a significant order from Codelco for its Chuquicamata Underground operation in Chile, including the supply of 13 Toro® LH515i load-haul-dump (LHD) loaders. Deliveries began in March 2026 and are scheduled to continue through November 2027… The order includes capital spares, training programs and advisory services…",
    "https://www.mining.sandvik/en/news-and-media/news-archive/2026/03/sandvik-awarded-order-for-13-lh515i-loaders-from-codelco-in-chile/",
    "Actor: Sandvik (Sweden) — allied; Codelco host copper UG. Opened Sandvik Mining English press 31 Mar 2026. CapEx blank.",
    "hunt_cycle180",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Sandvik Mining. “Sandvik awarded order for 13 Toro® LH515i loaders from Codelco in Chile.” March 31, 2026. https://www.mining.sandvik/en/news-and-media/news-archive/2026/03/sandvik-awarded-order-for-13-lh515i-loaders-from-codelco-in-chile/.',
    annotation="Sandvik: 13 LH515i for Codelco Chuquicamata UG. Supports sandvik_codelco_chuqui_lh515i_13_2026.",
    evid_note="Opened Sandvik Mining press release 2026-10-04.",
)

# 5. power_plants_grid / allied — ISA Interconexiones Nueva Lagunas–Kimal
row_doc(
    "isa_nueva_lagunas_kimal_194p46m_2023",
    "energy",
    "power_plants_grid",
    "allied",
    "ISA / Interconexiones del Norte — Nueva Lagunas seccionadora + 2×500 kV Nueva Lagunas–Kimal (USD 194.46m)",
    "Chile",
    "Adjudicated under Ministerio de Energía decreto exento N°15T/2023 (published 16 Jun 2023) to Interconexiones del Norte S.A. (ISA vehicle): Nueva S/E Seccionadora Nueva Lagunas 500/220 kV + Línea 2×500 kV Nueva Lagunas–Kimal (~190 km; ~409 structures) plus related Tarapacá–Lagunas capacity increase and Kimal 500 kV expansion works. Company project page states referential investment USD 194,462,361 for the Nueva Lagunas + line package; construction start projected 2025; ~19 months post-RCA; decree execution window 48 months. CapEx = USD 194,462,361 referential. Distinct from xd_kimal_lo_aguirre_cs_2022 converter station.",
    "194462361",
    "2023-06-16",
    "2023",
    "-20.95",
    "-69.55",
    "Nueva Lagunas seccionadora area near existing Lagunas substation, Pozo Almonte commune, Tarapacá (company: within 5 km of Lagunas, west of Ruta 5 Norte; approximate pin).",
    "interconexiones_norte_proyecto_kila",
    "S/E SECCIONADORA NUEVA LAGUNAS Y LÍNEA 2X500 KV NUEVA LAGUNAS – KIMAL. Valor de inversión referencial: USD 194.462.361.- El proyecto consiste en la construcción de una nueva subestación seccionadora, denominada Nueva Lagunas… Adicionalmente, el proyecto considera la construcción de una nueva línea de transmisión de doble circuito en 500 kV… entre la nueva subestación Nueva Lagunas y la subestación Kimal…",
    "https://interconexionesdelnorte.cl/proyecto/",
    "Actor: Interconexiones del Norte S.A. (ISA Colombia group / Interchile) — allied. Opened company Spanish project page. Referential CapEx USD 194.46m.",
    "hunt_cycle180",
    investment_type="concession",
    evidence="documented",
    bib_type="company",
    chicago='Interconexiones del Norte S.A. “Proyecto – S/E Seccionadora Nueva Lagunas y Línea 2×500 kV Nueva Lagunas – Kimal.” Accessed October 4, 2026. https://interconexionesdelnorte.cl/proyecto/.',
    annotation="ISA vehicle: Nueva Lagunas–Kimal referential USD 194.46m. Supports isa_nueva_lagunas_kimal_194p46m_2023.",
    evid_note="Opened interconexionesdelnorte.cl/proyecto/ 2026-10-04; ISA ownership confirmed on company home page.",
)

# 6. port_cranes / allied — Kalmar Ottawa ×3 ITI Iquique
row_doc(
    "kalmar_ottawa_iti_iquique_600k_2026",
    "infrastructure",
    "port_cranes",
    "allied",
    "Kalmar Ottawa — three terminal tractors for ITI Iquique (>USD 600k)",
    "Chile",
    "24–25 May 2026 (DataPortuaria citing ITI / Hanseatic Global Terminals): Iquique Terminal Internacional receives three Kalmar Ottawa terminal tractors unloaded from Polar Chile at berth 4; investment exceeds USD 600,000 as part of ITI modernization (prior MHC + handlers; next electric handlers). CapEx = USD 600,000 floor. Distinct from kalmar_portonave_ers_2026 / kalmar_lechman_ech_2026 / kalmar_tcp_montevideo_straddle_2024.",
    "600000",
    "2026-05-24",
    "2026",
    "-20.205",
    "-70.152",
    "Iquique Terminal Internacional, Port of Iquique, Tarapacá Region (berth 4 unload; same pin family as konecranes_iquique_esp10_2025).",
    "dataportuaria_iti_kalmar_ottawa_20260524",
    "Iquique Terminal Internacional (ITI), recinto gestionado por Hanseatic Global Terminals, concretó un nuevo avance en su proceso de modernización con la recepción de tres tracto camiones Kalmar Ottawa de última generación… Su integración representa una inversión que supera los USD 600 mil, siendo parte del plan de inversiones y renovación que impulsa la compañía…",
    "https://dataportuaria.com/es/internacional/puertos/iti-avanza-en-modernizacion-con-tres-nuevos-tracto-camiones",
    "Actor: Kalmar (Cargotec / Finland; Ottawa brand) — allied; ITI / Hanseatic host. Opened DataPortuaria Spanish 24 May 2026. Floor face >USD 600k.",
    "hunt_cycle180",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="press",
    chicago='DataPortuaria. “ITI avanza en modernización con tres nuevos tracto camiones de última generación.” May 24, 2026. https://dataportuaria.com/es/internacional/puertos/iti-avanza-en-modernizacion-con-tres-nuevos-tracto-camiones.',
    annotation="DataPortuaria/ITI: three Kalmar Ottawa >USD 600k. Supports kalmar_ottawa_iti_iquique_600k_2026.",
    evid_note="Opened DataPortuaria Spanish article 2026-10-04.",
)

# Thin top-up + remaining shuffle slots dry: nickel, lithium, graphite, port_ownership,
# engineering_epc (McDermott BRAVA already logged), niobium, balsa, building_materials,
# fission_smr, solar, wind, other_renewables, rail (holdovers unsigned).


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
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
    print(f"Cycle 180 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
