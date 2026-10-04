#!/usr/bin/env python3
"""Cycle 194 hunt: shuffle_seed=20261194; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261194).shuffle):
engineering_epc, fission_smr, lithium, copper, graphite, wind, balsa,
power_plants_grid, port_cranes, other_renewables, nickel, rail,
port_ownership, water, bridges_roads, building_materials, niobium, solar.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Equinix/Ascenty/Scala/Digital Realty/SEC Freeport/
EXIM/DFC/NADBank — 4 new U.S. rows (Equinix SP6/ST5; Ascenty AI USD 1.2bn; Scala Chile PF).
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


# 1. engineering_epc / us — Equinix SP6 São Paulo USD 114m
row_doc(
    "equinix_sp6_114m_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Equinix — SP6 IBX data center (Santana de Parnaíba / Greater São Paulo)",
    "Brazil",
    "16 Apr 2026 Equinix Portuguese newsroom: SP6 begins operations in Santana de Parnaíba (Greater São Paulo metro); investment USD 114 million; AI/high-density ready; campus also plans SP7 + two further sites. Distinct from equinix_rj3_45m_2025 / MO2 / ST2 / Bogotá rows and Ascenty SPO05/SPO06.",
    "114000000",
    "2026-04-16",
    "2026",
    "-23.444",
    "-46.918",
    "Equinix SP6 campus, Santana de Parnaíba, SP, Brazil (company geography; approximate campus pin).",
    "equinix_sp6_ops_20260416",
    "Com investimento de US$ 114 milhões, a nova unidade em Santana de Parnaíba … Localizado em Santana de Parnaíba, o projeto recebeu investimento de US$ 114 milhões",
    "https://newsroom.equinix.com/2026-04-16-Equinix-fortalece-lideranca-na-America-Latina-com-inauguracao-de-novo-data-center-SP6-em-Sao-Paulo",
    "Actor: Equinix (U.S., Nasdaq: EQIX) — us. Company Portuguese primary. CapEx = USD 114m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle194",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="114000000",
    fx_usd="1",
    bib_type="company",
    chicago='Equinix. “Equinix fortalece liderança na América Latina com inauguração de novo data center SP6 em São Paulo.” April 16, 2026. https://newsroom.equinix.com/2026-04-16-Equinix-fortalece-lideranca-na-America-Latina-com-inauguracao-de-novo-data-center-SP6-em-Sao-Paulo.',
    annotation="Equinix: SP6 Santana de Parnaíba USD 114m. Supports equinix_sp6_114m_2026.",
    evid_note="Opened Equinix Portuguese newsroom 2026-10-04.",
)

# 2. engineering_epc / us — Equinix ST5 Chile SEA USD 130m
row_doc(
    "equinix_st5_130m_chile_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Equinix Chile SpA — Datacenter ST5 (Pudahuel, Santiago)",
    "Chile",
    "21 Apr 2025: Comisión de Evaluación Región Metropolitana califica favorablemente DIA “Datacenter ST5” (Equinix Chile SpA); RCA states Monto de inversión USD 130,000,000; Pudahuel industrial zone (Calle Los Olivos / ENEA). Distinct from equinix_st2_chile_42m_2025 phase-2 expansion.",
    "130000000",
    "2025-04-21",
    "2025",
    "-33.43",
    "-70.80",
    "Equinix ST5, Pudahuel (ENEA), Santiago, Chile (SEA RCA geography; approximate pin).",
    "sea_equinix_st5_rca_20250421",
    "Monto de inversión | USD $ 130.000.000.- … Califica Ambientalmente el proyecto “Datacenter ST5” … Equinix Chile SpA … comuna de Pudahuel",
    "https://firma.sea.gob.cl/publicaciones/2025/04/30/1746030090_2165053410",
    "Actor: Equinix Chile SpA (U.S. parent Equinix) — us. SEA RCA primary (Spanish). CapEx = USD 130m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle194",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="130000000",
    fx_usd="1",
    bib_type="government",
    chicago='Chile, Servicio de Evaluación Ambiental (Región Metropolitana). Resolución de Calificación Ambiental “Datacenter ST5” (Equinix Chile SpA). April 21, 2025 (published RCA packet). https://firma.sea.gob.cl/publicaciones/2025/04/30/1746030090_2165053410.',
    annotation="SEA RCA: Equinix ST5 Pudahuel USD 130m. Supports equinix_st5_130m_chile_2025.",
    evid_note="Opened SEA RCA PDF/text 2026-10-04; Monto de inversión USD 130m confirmed.",
)

# 3. engineering_epc / us — Ascenty AI package USD 1.2bn (4 DCs)
row_doc(
    "ascenty_ai_1p2bn_brazil_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Ascenty (Digital Realty–Brookfield JV) — four new AI hyperscale data centers (Sumaré/Vinhedo/São Paulo corridor)",
    "Brazil",
    "Ascenty English company release: 150 MW of new hyperscale AI contracts drive USD 1.2 billion of new data-center investment for four new facilities in the São Paulo region — Sumaré 3 (first LatAm AI-from-inception design; 90 MW initial + 90 MW expansion option; delivery 2H 2027), Vinhedo 2 expansion + Vinhedo 3 (90 MW AI), plus a sixth São Paulo site (+20 MW). Fully pre-leased. Distinct from ascenty_spo05_300m_brl_2025 / spo06 rows.",
    "1200000000",
    "2026-05-27",
    "2026",
    "",
    "",
    "Ascenty Sumaré/Vinhedo/São Paulo AI campus package (company multi-site — lat/lon blank).",
    "ascenty_ai_contracts_1p2bn",
    "These contracts will drive US$1.2 billion of new data center investment to accelerate the expansion of the company’s artificial intelligence infrastructure in Brazil. Ascenty will build four new hyperscale data centers.",
    "https://ascenty.com/en/blog/news-ascenty-en/ascenty-ai-contracts/",
    "Actor: Ascenty JV (Digital Realty U.S. + Brookfield) — us. Company English primary. CapEx package = USD 1.2bn. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle194",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="1200000000",
    fx_usd="1",
    bib_type="company",
    chicago='Ascenty. “Ascenty Secures 150 Megawatts of New AI Contracts with Leading Global Hyperscalers.” https://ascenty.com/en/blog/news-ascenty-en/ascenty-ai-contracts/.',
    annotation="Ascenty: four AI DCs USD 1.2bn. Supports ascenty_ai_1p2bn_brazil_2026.",
    evid_note="Opened Ascenty English newsroom 2026-10-04.",
)

# 4. engineering_epc / us — Scala Chile project finance USD 328m
row_doc(
    "scala_chile_pf_328m_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Scala Data Centers (DigitalBridge) — Chile hyperscale project finance (3 DCs + Nova Lampa substation)",
    "Chile",
    "28 Jul 2025 PR Newswire / Scala: first international project-finance package USD 328 million (USD 254m long-term debt + VAT facility) from MUFG/SMBC/BNP Paribas/Natixis to fund construction of three hyperscale data centers (Curauma expansion; Lampa; Huechuraba 2) plus Nova Lampa substation in Chile; 23 MW contracted IT + 30 MW reserved. DigitalBridge-backed LatAm hyperscale platform. Distinct from Equinix ST2/ST5 and Ascenty Chile SLC rows.",
    "328000000",
    "2025-07-28",
    "2025",
    "",
    "",
    "Scala Chile Lampa/Curauma/Huechuraba campus package (company multi-site — lat/lon blank).",
    "scala_chile_pf_20250728",
    "unlocking USD 254 million in long-term funding to support the construction of three hyperscale data centers and a major power substation in Chile. When combined with a VAT facility, the total financing package reaches USD 328 million",
    "https://www.prnewswire.com/news-releases/scala-data-centers-closes-usd-328m-international-deal-securing-funds-for-three-data-centers-and-a-power-substation-in-chile-302514973.html",
    "Actor: Scala Data Centers (DigitalBridge U.S.-backed) — us. Company/PR Newswire English. Financing package = USD 328m for Chile DC build. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle194",
    investment_type="project_finance",
    evidence="documented",
    currency="USD",
    value_usd="328000000",
    fx_usd="1",
    bib_type="company",
    chicago='Scala Data Centers. “Scala Data Centers closes USD 328M international deal, securing funds for three data centers and a power substation in Chile.” PR Newswire, July 28, 2025. https://www.prnewswire.com/news-releases/scala-data-centers-closes-usd-328m-international-deal-securing-funds-for-three-data-centers-and-a-power-substation-in-chile-302514973.html.',
    annotation="Scala: Chile PF USD 328m for 3 DCs + substation. Supports scala_chile_pf_328m_2025.",
    evid_note="Opened Scala/PR Newswire English release 2026-10-04.",
)

# 5. other_renewables / prc — PowerChina Ecuador renewables+storage USD 400m
row_doc(
    "powerchina_ecuador_renewables_400m_2025",
    "energy",
    "other_renewables",
    "prc",
    "PowerChina — Ecuador renewable-energy and storage investment commitment (Noboa China visit)",
    "Ecuador",
    "30 Jun 2025 Secretaría General de Comunicación (Boletín 39): of USD 1,000m FDI energy package after President Noboa China/Spain tour, USD 400 million to be invested by Power China in renewable-energy and storage projects, disbursed progressively through December 2026; also technical assistance to update Plan Maestro de Electricidad. Distinct from cox_ecuador_renewables_600m_2025 (Spanish COX) and from powerchina_coca_codo_om_2026 / aom_46m_yr O&M settlement rows.",
    "400000000",
    "2025-06-30",
    "2025",
    "",
    "",
    "PowerChina Ecuador renewables/storage package (presidential announcement; multi-site — lat/lon blank).",
    "ecuador_comunicacion_boletin39_20250630",
    "de este rubro global, USD 400 millones los invertirá Power China en proyectos de energía renovable y almacenamiento. Los recursos llegarán progresivamente hasta diciembre de 2026",
    "https://www.comunicacion.gob.ec/como-resultado-de-la-gira-presidencial-ecuador-recibira-usd-1-000-millones-de-inversion-extranjera-de-china-y-espana-para-el-sector-energetico/",
    "Actor: PowerChina (PRC SOE) — prc. Ecuador Presidential Communication Secretariat Spanish primary. Commitment = USD 400m. Shuffle other_renewables.",
    "hunt_cycle194",
    investment_type="fdi_commitment",
    evidence="documented",
    currency="USD",
    value_usd="400000000",
    fx_usd="1",
    bib_type="government",
    chicago='Ecuador, Secretaría General de Comunicación de la Presidencia. “Como resultado de la gira presidencial, Ecuador recibirá USD 1.000 millones de inversión extranjera de China y España para el sector energético” (Boletín N° 39). June 30, 2025. https://www.comunicacion.gob.ec/como-resultado-de-la-gira-presidencial-ecuador-recibira-usd-1-000-millones-de-inversion-extranjera-de-china-y-espana-para-el-sector-energetico/.',
    annotation="Ecuador Comunicacion: PowerChina USD 400m renewables/storage. Supports powerchina_ecuador_renewables_400m_2025.",
    evid_note="Opened Ecuador Comunicación Boletín 39 2026-10-04.",
)

# 6. bridges_roads / allied — BCIE Nicaragua XI roads Tramo B USD 97m
row_doc(
    "bcie_nicaragua_xi_tramo_b_97m_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "BCIE — Nicaragua XI Programa de Ampliación y Mejoramiento de Carreteras (Tramo B loan 2357)",
    "Nicaragua",
    "24 Feb 2026 Asamblea Nacional Decree A.N. Nº 8923 approves BCIE Loan Contract Nº 2357-Tramo B (signed 10 Feb 2026) for USD 97,000,000 to continue XI road expansion/improvement program; MTI executor; Tramo B includes Estelí circumvallation (12.02 km) and Las Manos–Dipilto border access widening (11.67 km). Distinct from cscec_litoral_pacifico_fase2_nicaragua_2024 (PRC CSCEC Costanera Fase II yuan credit).",
    "97000000",
    "2026-02-24",
    "2026",
    "13.09",
    "-86.35",
    "Estelí circumvallation / Nueva Segovia border access corridor, Nicaragua (Asamblea geography; approximate Estelí pin).",
    "asamblea_ni_bcie_2357_tramo_b_20260224",
    "Decreto de Préstamo por 97 millones de dólares con el Banco Centroamericano de Integración Económica BCIE … continuidad del XI Programa de Ampliación y Mejoramiento de Carreteras … circunvalación de la ciudad de Estelí (12.02 km) y la ampliación del acceso al Puesto Fronterizo Las Manos-Dipilto (11.67km)",
    "https://noticias.asamblea.gob.ni/aprobamos-decreto-de-prestamo-para-la-continuidad-del-xi-programa-de-ampliacion-y-mejoramiento-de-carreteras/",
    "Actor: BCIE (Central American Development Bank) — allied. Asamblea Nacional Spanish primary; Decreto A.N. 8923 / Gaceta corroborates USD 97m. Shuffle bridges_roads.",
    "hunt_cycle194",
    investment_type="sovereign_loan",
    evidence="documented",
    currency="USD",
    value_usd="97000000",
    fx_usd="1",
    bib_type="government",
    chicago='Asamblea Nacional de Nicaragua. “Aprobamos decreto de préstamo para la continuidad del XI Programa de Ampliación y Mejoramiento de Carreteras.” February 24, 2026. https://noticias.asamblea.gob.ni/aprobamos-decreto-de-prestamo-para-la-continuidad-del-xi-programa-de-ampliacion-y-mejoramiento-de-carreteras/.',
    annotation="Asamblea NI: BCIE Tramo B USD 97m roads. Supports bcie_nicaragua_xi_tramo_b_97m_2026.",
    evid_note="Opened Asamblea Nacional news page 2026-10-04; normaweb Decreto A.N. 8923 corroborates USD 97m loan 2357-Tramo B.",
)

# 7. building_materials / other — UNACEM FY2025 CapEx PEN 698.8m
row_doc(
    "unacem_fy2025_capex_698p8m_pen",
    "infrastructure",
    "building_materials",
    "other",
    "Grupo UNACEM — FY2025 consolidated CapEx (primarily Peru cement/lime)",
    "Peru",
    "Grupo UNACEM Integrated Report 2025: investments totaling approximately S/ 698.8 million (698,799 thousand soles CapEx) during 2025, mainly to strengthen operating efficiency, industrial asset reliability, and environmental/technology upgrades — concentrated at UNACEM Perú (Atocongo GSA/kilns, primary crusher, clinker storage; Condorcocha; CALCEM lime plant) with smaller fleet/NA items in consolidation. Distinct from unacem_q2_2026_capex_3531m_pen quarterly allocation and unacem_calcem_lime_peru_2025.",
    "698800000",
    "2025-12-31",
    "2025",
    "",
    "",
    "Grupo UNACEM Peru-centered CapEx program (Integrated Report; multi-site — lat/lon blank).",
    "unacem_ir_2025_capex",
    "during 2025, we made investments totaling approximately S/ 698.8 million … 698,799 thousands of Peruvian soles in CAPEX",
    "https://grupounacem.com/wp-content/uploads/2026/07/IR.Grupo-UNACEM-Integrated-Report-2025.pdf",
    "Actor: Grupo UNACEM (Peru) — other. Company English Integrated Report. CapEx = PEN 698.8m (leave value_usd blank; no stated USD). Shuffle building_materials.",
    "hunt_cycle194",
    investment_type="capex_plan",
    evidence="documented",
    currency="PEN",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Grupo UNACEM. Integrated Report 2025. https://grupounacem.com/wp-content/uploads/2026/07/IR.Grupo-UNACEM-Integrated-Report-2025.pdf.',
    annotation="UNACEM IR 2025: CapEx ~S/698.8m. Supports unacem_fy2025_capex_698p8m_pen.",
    evid_note="Opened UNACEM Integrated Report 2025 PDF 2026-10-04.",
)


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
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []

    for row, evid, bib_e in ITEMS:
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
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle194 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
