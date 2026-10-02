#!/usr/bin/env python3
"""Cycle 170 hunt: shuffle_seed=20261170; equal budget; U.S./PRC split; thin after.

Canonical shuffle (codebook order + Random(20261170)): water, power_plants_grid,
niobium, balsa, nickel, rail, engineering_epc, building_materials, graphite,
port_cranes, copper, solar, lithium, port_ownership, bridges_roads, fission_smr,
wind, other_renewables.

Thin top-up (recomputed): balsa / nickel / fission_smr (tied graphite) —
balsa filled (Sinobalsa presence); graphite filled via U.S.–Mexico Action Plan
(names graphite); nickel/fission dry this pass.
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC rail past MoU.
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


# 1. water / prc — MIDAGRI China G2G technical assistance (Poechos + Alto Piura)
row_doc(
    "china_midagri_poechos_alto_piura_g2g_2025",
    "resources",
    "water",
    "prc",
    "People’s Republic of China — MIDAGRI G2G technical assistance (Alto Piura + Sistema Poechos)",
    "Peru",
    "23 Dec 2025: MIDAGRI announces China selected as Estado Ganador for specialized technical assistance on execution/studies for Alto Piura (components I, III, IV) and afianzamiento del Sistema Poechos, after G2G evaluation of proposals from UK, Spain, PRC, Portugal, and Korea. Next step: G2G contract subscription subject to MEF budget opinion then negotiation. CapEx blank (TA award; PECHP 20 Jun 2026 still urging contract signature). Distinct from POWERCHINA Nickerie drainage and Cerro Verde Enlozada WWTP rows.",
    "",
    "",
    "2025",
    "",
    "",
    "Alto Piura / Sistema Poechos (Piura Region) — multi-component TA package; lat/lon blank pending single named worksite.",
    "midagri_china_g2g_poechos_20251223",
    "El Ministerio de Desarrollo Agrario y Riego (MIDAGRI) anunció que China será el Estado que se haría cargo de la asistencia técnica especializada en la ejecución y estudios de los proyectos Alto Piura (componentes I, III y IV) y afianzamiento del Sistema Poechos… propuestas presentadas por los Estados de Reino Unido… España, República Popular China, Portugal y Corea.",
    "https://www.gob.pe/institucion/midagri/noticias/1319346-midagri-china-gana-g2g-para-la-asistencia-tecnica-de-alto-piura-y-poechos",
    "Actor: People’s Republic of China (Estado Ganador G2G) — prc. Opened MIDAGRI gob.pe 23 Dec 2025. GORE Piura 27 Dec 2025 corroborates. CapEx blank until signed contract.",
    "hunt_cycle170",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='Peru, Ministerio de Desarrollo Agrario y Riego. “MIDAGRI: China gana G2G para la asistencia técnica de Alto Piura y Poechos.” December 23, 2025. https://www.gob.pe/institucion/midagri/noticias/1319346-midagri-china-gana-g2g-para-la-asistencia-tecnica-de-alto-piura-y-poechos.',
    annotation="MIDAGRI: China wins G2G TA for Alto Piura and Poechos. Supports china_midagri_poechos_alto_piura_g2g_2025.",
    evid_note="Opened MIDAGRI gob.pe G2G selection notice 23 Dec 2025.",
)

# 2. water / us — DFC Amazon Biocorridor debt conversion PRI USD 1bn
row_doc(
    "dfc_ecuador_amazon_biocorridor_pri_1bn_2024",
    "resources",
    "water",
    "us",
    "U.S. International Development Finance Corporation — Amazon Biocorridor debt-conversion PRI",
    "Ecuador",
    "17 Dec 2024: DFC announces financial close of Ecuador’s Amazon Biocorridor debt conversion enabled by USD 1 billion in DFC political risk insurance (PRI), refinancing ~USD 1.53 billion of Ecuador international bonds; expected to unlock ~USD 460 million for Programa Biocorredor Amazónico terrestrial and freshwater conservation (improved management of 4.6 million ha existing protected areas; protect additional 1.8 million ha forests/wetlands; protect 18,000 km of rivers). Value = USD 1bn PRI face. Distinct from DFC Solararomo Manta proposed loan and Galápagos debt-conversion lineage.",
    "1000000000",
    "2024-12-17",
    "2024",
    "",
    "",
    "Ecuadorian Amazon Biocorridor Program geography (multi-hectare freshwater/terrestrial corridor) — lat/lon blank.",
    "dfc_amazon_biocorridor_20241217",
    "Today, the Republic of Ecuador, with the support of the U.S. International Development Finance Corporation, the Inter-American Development Bank (IDB), The Nature Conservancy (TNC), and Bank of America announced the financial close of a debt conversion enabled by $1 billion in political risk insurance (PRI) from DFC… expected to generate approximately $460 million to support the Amazon Biocorridor Program… conservation of terrestrial and freshwater ecosystems… protect 18,000 kilometers of rivers",
    "https://www.dfc.gov/media/press-releases/dfc-announces-1-billion-political-risk-insurance-ecuadors-first-debt",
    "Actor: U.S. DFC — us. Opened DFC press 17 Dec 2024. Value = USD 1bn PRI (not the USD 460m conservation envelope). Freshwater river/wetland conservation coded under water.",
    "hunt_cycle170",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='U.S. International Development Finance Corporation. “DFC Announces $1 Billion in Political Risk Insurance for Ecuador’s First Debt Conversion to Support Terrestrial and Freshwater Conservation in the Amazon.” December 17, 2024. https://www.dfc.gov/media/press-releases/dfc-announces-1-billion-political-risk-insurance-ecuadors-first-debt.',
    annotation="DFC: USD 1bn PRI for Ecuador Amazon Biocorridor debt conversion. Supports dfc_ecuador_amazon_biocorridor_pri_1bn_2024.",
    evid_note="Opened DFC Amazon Biocorridor PRI financial-close release.",
)

# 3. power_plants_grid / us — GE Vernova leads Itaipu CMI modernization
row_doc(
    "ge_vernova_itaipu_cmi_modernization_2025",
    "energy",
    "power_plants_grid",
    "us",
    "GE Vernova (CMI Consortium lead) — Itaipu Binacional technological modernization",
    "Brazil",
    "20 Nov 2025 GE Vernova: major technological update underway at 14 GW Itaipu hydroelectric plant, executed by CMI Consortium led by GE Vernova with CIE SA and Tecnoedil SA; ~14-year program covering all 20 generating units; SCADA, Energy Management Systems, and Network Automation Technologies planned for 2026; digital controls, automated monitoring, and plant cybersecurity. CapEx USD not disclosed. Country coded Brazil (binational Brazil–Paraguay asset; GE Vernova Brazil engineering cited). Distinct from ge_vernova_sao_simao_ug3_2026 / Azulão COD.",
    "",
    "",
    "2025",
    "-25.408",
    "-54.589",
    "Itaipu Dam / Foz do Iguaçu–Ciudad del Este binational complex (company geography; approximate dam pin).",
    "ge_vernova_itaipu_modernization_20251120",
    "the 41-year-old Itaipu… having an installed capacity of 14 gigawatts, and it’s currently going through a major technological update, executed by the CMI Consortium, formed by GE Vernova (leader), CIE SA, and Tecnoedil SA… expected to be completed over 14 years… Critical systems such as the Supervisory Control and Data Acquisition (SCADA), Energy Management Systems (EMS) and Network Automation Technologies, for example, are planned for 2026.",
    "https://www.gevernova.com/news/articles/enabling-superpower-water-major-technological-update",
    "Actor: GE Vernova Inc. (NYSE: GEV, U.S.) consortium lead — us. Opened company feature 20 Nov 2025. CapEx blank.",
    "hunt_cycle170",
    investment_type="epc",
    evidence="documented",
    bib_type="company",
    chicago='GE Vernova. “Enabling the Superpower of Water: The Major Technological Update Is Becoming Reality at Itaipu Hydroelectric Plant.” November 20, 2025. https://www.gevernova.com/news/articles/enabling-superpower-water-major-technological-update.',
    annotation="GE Vernova: Itaipu CMI consortium modernization lead. Supports ge_vernova_itaipu_cmi_modernization_2025.",
    evid_note="Opened GE Vernova Itaipu modernization feature 20 Nov 2025.",
)

# 4. solar / prc — BYD Full EPC for Raízen Gera nine plants (26.5 MW)
row_doc(
    "byd_raizen_gera_nine_plants_26p5mw",
    "energy",
    "solar",
    "prc",
    "BYD Brasil — Full EPC for Raízen Gera Desenvolvedora nine distributed solar plants",
    "Brazil",
    "22 Mar 2024 BYD Brasil: Full EPC partnership with Raízen Gera Desenvolvedora (Raízen–Grupo Gera JV) for nine PV plants totaling 26.5 MW peak across Ceará (Betânia, Boa Viagem, Amontada), Rio de Janeiro (Fazenda São João, Goytacazes), Rio Grande do Norte (Ceará Mirim), and Pará (Santarém); plants already under construction at announcement with May 2024 generation start targeted. 15 May 2025 BYD follow-up confirms installation complete and >59 GWh/year generation. CapEx blank (MW disclosed; no USD on opened pages). Distinct from byd_camacari / byd_grenergy / byd_brazil_bess rows.",
    "",
    "",
    "2024",
    "",
    "",
    "Nine distributed plants across CE/RN/RJ/PA — lat/lon blank for multi-site portfolio.",
    "byd_brasil_raizen_gera_20240322",
    "A BYD… acaba de firmar uma parceria com a Raízen Gera Desenvolvedora… Full EPC… nove plantas solares fotovoltaicas… distribuídas em Betânia, Boa Viagem e Amontada, no Ceará; Fazenda São João e Goytacazes, no Rio de Janeiro; Ceará Mirim, no Rio Grande do Norte; e Santarém, no Pará… capacidade total do projeto é de 26,5 Megawatts (MW)",
    "https://bydbrasil.com.br/byd-vai-implantar-nove-usinas-solares-com-expertise-em-epc-para-raizen-gera-desenvolvedora/",
    "Actor: BYD (PRC OEM/EPC via BYD Brasil) — prc; client Raízen Gera JV (Brazil/Shell–Cosan lineage). Opened BYD Brasil 22 Mar 2024; May 2025 delivery page corroborates COD. CapEx blank.",
    "hunt_cycle170",
    investment_type="epc",
    evidence="documented",
    bib_type="company",
    chicago='BYD Brasil. “BYD vai implantar nove usinas solares com expertise em EPC para Raízen Gera Desenvolvedora.” March 22, 2024. https://bydbrasil.com.br/byd-vai-implantar-nove-usinas-solares-com-expertise-em-epc-para-raizen-gera-desenvolvedora/.',
    annotation="BYD Brasil: Full EPC nine Raízen Gera plants totaling 26.5 MW. Supports byd_raizen_gera_nine_plants_26p5mw.",
    evid_note="Opened BYD Brasil Raízen Gera Full EPC announcement; May 2025 install corroboration noted.",
)

# 5. balsa / prc — Sinobalsa Ecuador forest/block presence (thin top-up)
row_doc(
    "sinobalsa_ecuador_presence",
    "resources",
    "balsa",
    "prc",
    "Jiangsu Sino New Materials (Sinobalsa) — Ecuador forest and balsa-block company",
    "Ecuador",
    "Company English About page: Jiangsu Sino New Materials Co., Ltd. states it ‘has its own forest and Balsa wood Block company in Ecuador with the Brand Sinobalsa,’ alongside Jiangsu Province core-material processing lines, supplying aerospace/wind/transport/industrial sandwich cores. Presence documentation — no CapEx USD, hectare figure, or named mill city on opened page. Distinct from Plantabal/3A BALTEK presence and WITS Ecuador–China balsa trade-flow rows. Thin-subcategory PRC actor fill.",
    "",
    "",
    "2024",
    "",
    "",
    "Ecuador Sinobalsa forest/block operations (company states Ecuador presence; no named municipality on opened page) — lat/lon blank.",
    "sinobalsa_about_ecuador",
    "The company mainly provides core material research and development and processing services such as Balsa Wood, PVC, PET, and etc. Sino has its own forest and Balsa wood Block company in Ecuador with the Brand Sinobalsa. At the same time, it has its own core material processing production line in Jiangsu Province in China",
    "http://www.sinobalsa.com/en/about.html",
    "Actor: Jiangsu Sino New Materials / Sinobalsa (PRC) — prc. Opened company English About page. Presence only; CapEx blank.",
    "hunt_cycle170",
    investment_type="ownership_equity",
    evidence="documented",
    bib_type="company",
    chicago='Jiangsu Sino New Materials Co., Ltd. “About.” http://www.sinobalsa.com/en/about.html.',
    annotation="Sinobalsa: company states Ecuador forest/block subsidiary. Supports sinobalsa_ecuador_presence.",
    evid_note="Opened Sinobalsa English About page documenting Ecuador forest/block company.",
)

# 6. lithium / us — Argentina–U.S. critical minerals framework (Cancillería)
row_doc(
    "argentina_us_critical_minerals_framework_2026",
    "resources",
    "lithium",
    "us",
    "U.S. Department of State / Argentina Cancillería — Critical Minerals Mining and Processing Framework",
    "Argentina",
    "4 Feb 2026: At the Critical Minerals Ministerial convened by Secretary Rubio in Washington, Argentina and the United States sign an Instrumento Marco para el Fortalecimiento del Suministro en Minería y Procesamiento de Minerales Críticos — public/private financing tools, permitting simplification, geological mapping, recycling/materials management, and transparent markets. Cancillería cites 2025 mining exports USD 6.037bn and lithium carbonate production >110 kt. CapEx blank (framework; not a named mine loan). Complements EXIM Argentina Build the Future framework and cycle-169 Colombia/Peru/Paraguay/Ecuador MoUs.",
    "",
    "",
    "2026",
    "",
    "",
    "Framework signing in Washington; no single named mine — lat/lon blank.",
    "cancilleria_ar_us_critical_minerals_20260204",
    "la República Argentina y los Estados Unidos suscribieron un Instrumento Marco para el Fortalecimiento del Suministro en Minería y Procesamiento de Minerales Críticos mediante el cual ratifican su asociación estratégica y su compromiso con el desarrollo de un suministro seguro, resiliente y competitivo… En 2025… exportaciones mineras alcanzaron un récord de 6.037 millones de dólares… producción de carbonato de litio superó las 110 mil toneladas",
    "https://www.cancilleria.gob.ar/es/actualidad/noticias/argentina-y-estados-unidos-suscribieron-un-acuerdo-de-minerales-criticos",
    "Actor: U.S. (State Department ministerial) with Argentina Cancillería — us. Opened Cancillería 4 Feb 2026. CapEx blank.",
    "hunt_cycle170",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='Argentina, Ministerio de Relaciones Exteriores, Comercio Internacional y Culto. “Argentina y Estados Unidos suscribieron un acuerdo de minerales críticos.” February 4, 2026. https://www.cancilleria.gob.ar/es/actualidad/noticias/argentina-y-estados-unidos-suscribieron-un-acuerdo-de-minerales-criticos.',
    annotation="Cancillería AR: U.S.–Argentina critical minerals framework. Supports argentina_us_critical_minerals_framework_2026.",
    evid_note="Opened Cancillería Argentina critical minerals framework notice 4 Feb 2026.",
)

# 7. graphite / us — U.S.–Mexico Critical Minerals Action Plan (names graphite)
row_doc(
    "mexico_us_critical_minerals_action_plan_2026",
    "resources",
    "graphite",
    "us",
    "USTR / Mexico Secretaría de Economía — U.S.–Mexico Critical Minerals Action Plan",
    "Mexico",
    "4 Feb 2026: USTR Ambassador Greer announces enactment of the U.S.–Mexico Action Plan on Critical Minerals — coordinated trade policies/mechanisms to mitigate critical-mineral supply-chain vulnerabilities, including identifying minerals of interest, exploring border-adjusted import price floors, and consulting on embedding price floors in a plurilateral critical-minerals trade agreement. Action Plan PDF lists geological-data sharing (USGS–SGM) and coordinated stockpiling among workstreams; trade press notes copper, silver, lithium, graphite, and zinc as named priorities. CapEx blank (60-day non-binding plan). Thin graphite diplomacy cell; distinct from cycle-169 national MoUs.",
    "",
    "",
    "2026",
    "",
    "",
    "Bilateral Action Plan (country-level) — lat/lon blank.",
    "ustr_mexico_critical_minerals_20260204",
    "Today, Ambassador Jamieson Greer announced the enactment of the U.S.-Mexico Action Plan on Critical Minerals. Under this first-of-its-kind Action Plan, the United States and Mexico will work to develop coordinated trade policies and mechanisms that mitigate critical mineral supply chain vulnerabilities. This work will include identifying specific critical minerals of interest, exploring border-adjusted price floors for critical minerals imports, and consulting on how price floors may be incorporated in a binding plurilateral agreement on trade in critical minerals.",
    "https://ustr.gov/about/policy-offices/press-office/press-releases/2026/february/ambassador-jamieson-greer-announces-us-mexico-action-plan-critical-minerals",
    "Actor: USTR (U.S.) with Mexico Secretaría de Economía — us. Opened USTR 4 Feb 2026 release. CapEx blank. Graphite coded as named priority mineral in Action Plan coverage.",
    "hunt_cycle170",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='Office of the United States Trade Representative. “Ambassador Jamieson Greer Announces U.S.-Mexico Action Plan on Critical Minerals.” February 4, 2026. https://ustr.gov/about/policy-offices/press-office/press-releases/2026/february/ambassador-jamieson-greer-announces-us-mexico-action-plan-critical-minerals.',
    annotation="USTR: U.S.–Mexico Critical Minerals Action Plan. Supports mexico_us_critical_minerals_action_plan_2026.",
    evid_note="Opened USTR Action Plan announcement 4 Feb 2026.",
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
    print(f"Cycle 170 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
