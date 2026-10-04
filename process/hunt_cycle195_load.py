#!/usr/bin/env python3
"""Cycle 195 hunt: shuffle_seed=20261195; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261195).shuffle):
rail, niobium, engineering_epc, power_plants_grid, fission_smr, port_cranes,
bridges_roads, other_renewables, nickel, copper, building_materials, lithium,
port_ownership, water, wind, balsa, solar, graphite.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Progress Rail/VLI CapEx, AWS Chile Region, Microsoft
Mexico AI/cloud, EXIM/DFC/SEC Freeport sweeps — 3 new U.S. rows.
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


# 1. rail / us — Progress Rail (Caterpillar) eight SD70ACe-BB CapEx ~R$200m
row_doc(
    "progress_rail_vli_sd70_200m_brl_2024",
    "infrastructure",
    "rail",
    "us",
    "Progress Rail (Caterpillar) — eight EMD SD70ACe-BB locomotives CapEx for VLI (FCA)",
    "Brazil",
    "10 Feb 2026 VLI: celebrates delivery of final units of eight EMD SD70ACe-BB locomotives from Progress Rail for Centro-Atlântica Railway; machines acquired in 2024 with investment of about R$ 200 million; manufactured Sete Lagoas (MG). CapEx = ~R$200m locomotive package. Distinct from progress_rail_vli_sd70_2026 (delivery presence; CapEx blank on Progress Rail page) and progress_rail_vli_msa_norte_500m_brl_2025 (MSA services).",
    "200000000",
    "2024-01-01",
    "2024",
    "-19.466",
    "-44.247",
    "Progress Rail Sete Lagoas plant / FCA delivery, Minas Gerais, Brazil (VLI/InvestMinas geography; approximate plant pin).",
    "vli_progress_rail_delivery_20260210",
    "As máquinas foram adquiridas em 2024, com um investimento de cerca de R$ 200 milhões, que reforça o compromisso da VLI de integrar regiões e impulsionar a indústria ferroviária nacional.",
    "https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/",
    "Actor: Progress Rail (Caterpillar Inc., U.S.) OEM — us; buyer VLI (Brazil). VLI Portuguese primary CapEx ~R$200m. Shuffle rail; ≥1/3 U.S. hunt.",
    "hunt_cycle195",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='VLI Logística. “VLI e Progress Rail celebram recebimento de locomotivas para operação na Ferrovia Centro-Atlântica.” February 10, 2026. https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/.',
    annotation="VLI: eight Progress Rail SD70 CapEx ~R$200m. Supports progress_rail_vli_sd70_200m_brl_2024.",
    evid_note="Opened VLI Portuguese release 2026-10-04; CapEx ~R$200m confirmed.",
)

# 2. engineering_epc / us — AWS Chile Region >USD 4bn
row_doc(
    "aws_chile_region_4bn_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Amazon Web Services — AWS South America (Chile) Region data-center build",
    "Chile",
    "7 May 2025 Amazon/AWS: plans to launch AWS South America (Chile) Region by end-2026 with three Availability Zones; as part of long-term commitment Amazon plans to invest more than USD 4 billion in Chile to support construction, connection, operation, and maintenance of its data centers. CapEx floor = USD 4bn. Distinct from Equinix ST2/ST5 Santiago and Ascenty Chile rows.",
    "4000000000",
    "2025-05-07",
    "2025",
    "",
    "",
    "AWS South America (Chile) Region multi-AZ campus package (company; multi-site — lat/lon blank).",
    "amazon_aws_chile_region_20250507",
    "As part of its long-term commitment, Amazon is planning to invest more than $4 billion in Chile to support the construction, connection, operation, and maintenance of its data centers in the country.",
    "https://press.aboutamazon.com/aws/2025/5/amazon-to-invest-more-than-4-billion-to-launch-infrastructure-region-in-chile",
    "Actor: Amazon / AWS (U.S.) — us. Company English primary. CapEx floor >USD 4bn (stored as 4e9 floor). Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle195",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="4000000000",
    fx_usd="1",
    bib_type="company",
    chicago='Amazon Web Services. “Amazon to Invest More Than $4 Billion to Launch Infrastructure Region in Chile.” May 7, 2025. https://press.aboutamazon.com/aws/2025/5/amazon-to-invest-more-than-4-billion-to-launch-infrastructure-region-in-chile.',
    annotation="AWS: Chile Region >USD 4bn. Supports aws_chile_region_4bn_2025.",
    evid_note="Opened Amazon AWS English press room 2026-10-04.",
)

# 3. engineering_epc / us — Microsoft Mexico AI/cloud USD 1.3bn
row_doc(
    "microsoft_mexico_ai_1p3bn_2024",
    "infrastructure",
    "engineering_epc",
    "us",
    "Microsoft — Mexico cloud and AI infrastructure package (3 years)",
    "Mexico",
    "24 Sep 2024 Microsoft Source LATAM: CEO Satya Nadella announces USD 1.3 billion investment over the next three years to enhance AI infrastructure and digital/AI skills in Mexico, including expanding local computing capacity (Querétaro datacenter region context) plus National Skills program. CapEx package = USD 1.3bn (infrastructure + skilling envelope as stated). Distinct from Equinix MO2 Monterrey and CloudHQ Querétaro rows.",
    "1300000000",
    "2024-09-24",
    "2024",
    "",
    "",
    "Microsoft Mexico AI/cloud infrastructure package (company national; multi-site — lat/lon blank).",
    "microsoft_mexico_1p3bn_20240924",
    "He revealed a new investment of $1.3 billion over the next three years to enhance AI infrastructure and initiatives aimed at promoting digital and AI skills. … Microsoft is expanding its AI infrastructure in Mexico. This involves a significant investment to increase local computing capacity and encourage innovation.",
    "https://news.microsoft.com/source/latam/company-news-es/microsoft-announces-1-3-billion-usd-investment-in-cloud-and-ai-infrastructure-supporting-inclusive-growth-through-technology-and-skilling-programs-in-mexico/",
    "Actor: Microsoft Corporation (U.S.) — us. Company English Source LATAM primary. CapEx package = USD 1.3bn. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle195",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="1300000000",
    fx_usd="1",
    bib_type="company",
    chicago='Microsoft. “Microsoft announces $1.3 billion USD investment in Cloud and AI infrastructure supporting inclusive growth through technology and skilling programs in Mexico.” September 24, 2024. https://news.microsoft.com/source/latam/company-news-es/microsoft-announces-1-3-billion-usd-investment-in-cloud-and-ai-infrastructure-supporting-inclusive-growth-through-technology-and-skilling-programs-in-mexico/.',
    annotation="Microsoft: Mexico AI/cloud USD 1.3bn. Supports microsoft_mexico_ai_1p3bn_2024.",
    evid_note="Opened Microsoft Source LATAM English release 2026-10-04.",
)

# 4. power_plants_grid / allied — ISA Energia FY2025 CapEx R$5.1bn
row_doc(
    "isa_energia_fy2025_capex_5p1bn_brl",
    "energy",
    "power_plants_grid",
    "allied",
    "ISA ENERGIA BRASIL — FY2025 record transmission CapEx",
    "Brazil",
    "24 Feb 2026 ISA ENERGIA BRASIL: record CapEx R$ 5.1 billion in 2025 (+40.4% YoY / +R$1.46bn); of which R$ 3.4bn greenfield concessions (Piraquê MG/ES; Serra Dourada BA/MG) and R$ 1.69bn Reforços & Melhorias; energized Água Vermelha, Riacho Grande, Piraquê Bloco 1. Distinct from isa_energia_serra_dourada_3p2bn_2025 project envelope and isa_energia_rm_370m_brl_1t26 quarterly R&M.",
    "5100000000",
    "2025-12-31",
    "2025",
    "",
    "",
    "ISA ENERGIA BRASIL national transmission CapEx program (company; multi-site — lat/lon blank).",
    "isa_energia_4t25_results_20260224",
    "No acumulado de 2025, a Companhia atingiu um novo patamar de execução com o CapEx recorde de R$ 5,1 bilhões, um crescimento expressivo de R$ 1,46 bilhão (+40,4%). Desse montante, R$ 3,4 bilhões foram dedicados a projetos em concessões licitadas (Greenfield) … Em projetos de Reforços & Melhorias, o investimento somou R$ 1,69 bilhão",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-divulga-os-resultados-do-4t25-com-recorde-em-investimentos-de-r-51-bi-no-ano/",
    "Actor: ISA ENERGIA BRASIL (Colombian ISA control) — allied. Company Portuguese primary. CapEx = R$5.1bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle195",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ISA ENERGIA BRASIL. “ISA ENERGIA BRASIL divulga os resultados do 4T25 com recorde em investimentos de R$ 5,1 bi no ano.” February 24, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-divulga-os-resultados-do-4t25-com-recorde-em-investimentos-de-r-51-bi-no-ano/.',
    annotation="ISA Energia: FY2025 CapEx R$5.1bn. Supports isa_energia_fy2025_capex_5p1bn_brl.",
    evid_note="Opened ISA Energia Brasil Portuguese newsroom 2026-10-04.",
)

# 5. power_plants_grid / prc — SGBH GATE UHV CapEx R$18bn
row_doc(
    "sgbh_gate_uhv_18bn_brl_2025",
    "energy",
    "power_plants_grid",
    "prc",
    "State Grid Brazil Holding — GATE ±800 kV UHVDC CapEx (Graça Aranha–Silvânia)",
    "Brazil",
    "30 Jun 2025 SGBH: launches foundation stone in Silvânia (GO) for Northeast Brazil UHV project administered by Graça Aranha Transmissora de Energia (GATE); CapEx R$ 18 billion for ±800 kV HVDC line 1,468 km Graça Aranha (MA)–Silvânia (GO) via Tocantins + two converter stations; 5 GW; COD targeted 2029; 30-year concession. CapEx = R$18bn company primary. Distinct from state_grid_ne_uhv_construction_2026 (construction-start milestone; CapEx blank) and aneel_state_grid_rap_2023 (RAP exclude).",
    "18000000000",
    "2025-06-30",
    "2025",
    "-16.66",
    "-48.61",
    "Silvânia (GO) receiving-end converter station area, Brazil (SGBH geography; approximate pin).",
    "sgbh_gate_silvania_20250630",
    "lançará em 30/6, em Silvânia (GO), a pedra fundamental do “Projeto de Ultra Alta Tensão no Nordeste do Brasil”, para o qual serão destinados R$ 18 bilhões. … linha de transmissão em corrente contínua em ultra alta tensão (800 kV), com 1.468 km —entre as cidades de Graça Aranha (Maranhão) e Silvânia (Goiás)",
    "https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/",
    "Actor: State Grid Brazil Holding / SGCC (PRC) — prc. Company Portuguese primary CapEx R$18bn. Shuffle power_plants_grid.",
    "hunt_cycle195",
    investment_type="concession_construction",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='State Grid Brazil Holding. “Município goiano de Silvânia sedia lançamento do mais caro projeto de Ultra Alta Tensão (800Kv) da história do setor elétrico do Brasil.” June 2025. https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/.',
    annotation="SGBH: GATE UHV CapEx R$18bn. Supports sgbh_gate_uhv_18bn_brl_2025.",
    evid_note="Opened SGBH Portuguese release 2026-10-04; CapEx R$18bn confirmed (press R$23bn not used).",
)

# 6. port_cranes / allied — Portonave 14 e-RTG CapEx ~R$210m
row_doc(
    "portonave_ertg_210m_brl_2026",
    "infrastructure",
    "port_cranes",
    "allied",
    "Portonave (TIL) — 14 Konecranes electric RTG CapEx (Navegantes)",
    "Brazil",
    "8 Jul 2026 Portonave: first seven of 14 new electric Rubber Tyred Gantry (e-RTG) cranes arrive Navegantes; Konecranes design (Finland) / China assembly; acquisition represents investment of approximately R$ 210 million; part of >R$2bn works+equipment plan. CapEx = ~R$210m buyer face. Distinct from konecranes_portonave_rtg_2025 (OEM order; CapEx blank) and zpmc_portonave_sts_2025 (STS package).",
    "210000000",
    "2026-07-08",
    "2026",
    "-26.89",
    "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina, Brazil (company geography).",
    "portonave_ertg_arrival_20260708",
    "A aquisição destes RTGs representa um investimento de aproximadamente R$ 210 milhões. … Da marca Konecranes, projetados na Finlândia e fabricados na China",
    "https://www.portonave.com.br/pt/todas-as-noticias/portonave-amplia-frota-de-patio-com-sete-novos-guindastes-eletricos",
    "Actor: Portonave under TIL (MSC/Swiss) — allied; equipment Konecranes (Finland). Company Portuguese primary CapEx ~R$210m. Shuffle port_cranes.",
    "hunt_cycle195",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Portonave. “Portonave amplia frota de pátio com sete novos guindastes elétricos.” July 8, 2026. https://www.portonave.com.br/pt/todas-as-noticias/portonave-amplia-frota-de-patio-com-sete-novos-guindastes-eletricos.',
    annotation="Portonave: 14 e-RTG CapEx ~R$210m. Supports portonave_ertg_210m_brl_2026.",
    evid_note="Opened Portonave Portuguese newsroom 2026-10-04.",
)

# 7. copper / other — Codelco FY2025 CapEx USD 5.073bn
row_doc(
    "codelco_fy2025_capex_5073m",
    "resources",
    "copper",
    "other",
    "Codelco — FY2025 record copper CapEx (Chile)",
    "Chile",
    "27 Mar 2026 Codelco: closed 2025 with record CapEx US$ 5.073 billion — largest annual deployment in Codelco history; project portfolio 98% physical/financial progress vs budget; Rajo Inca / El Teniente structural / Chuquicamata Subterránea among execution highlights. CapEx = USD 5.073bn. Distinct from codelco_anglo_andina_bronces_2025 MoU and Novandino Litio JV rows.",
    "5073000000",
    "2025-12-31",
    "2025",
    "",
    "",
    "Codelco Chile multi-division CapEx program (company; multi-site — lat/lon blank).",
    "codelco_resultados_2025_20260327",
    "El año cerró con cifras históricas en materia de inversión al sumar US$ 5.073 millones en Capex, el mayor despliegue anual en la historia de Codelco. En términos globales, la cartera de proyectos de la Corporación tuvo un avance físico y financiero de 98% respecto a lo presupuestado.",
    "https://www.codelco.com/prensa/2026/codelco-cerro-2025-con-un-ebitda-de-us-6-670-millones-una-utilidad",
    "Actor: Codelco (Chilean state copper) — other. Company Spanish primary. CapEx = USD 5.073bn. Shuffle copper.",
    "hunt_cycle195",
    investment_type="capex_plan",
    evidence="documented",
    currency="USD",
    value_usd="5073000000",
    fx_usd="1",
    bib_type="company",
    chicago='Codelco. “Codelco cerró 2025 con un Ebitda de US$ 6.670 millones, una utilidad consolidada de US$ 2.423 millones y un aporte al Fisco de US$ 1.778 millones.” March 27, 2026. https://www.codelco.com/prensa/2026/codelco-cerro-2025-con-un-ebitda-de-us-6-670-millones-una-utilidad.',
    annotation="Codelco: FY2025 CapEx USD 5.073bn. Supports codelco_fy2025_capex_5073m.",
    evid_note="Opened Codelco Spanish press room 2026-10-04.",
)

# 8. building_materials / allied — Holcim Zapopan electric ready-mix MXN 51m
row_doc(
    "holcim_zapopan_electric_51m_mxn_2025",
    "infrastructure",
    "building_materials",
    "allied",
    "Holcim México — first 100% electric ready-mix plant (Zapopan, Jalisco)",
    "Mexico",
    "26 Nov 2025 Holcim México: inaugurates first 100% electric ready-mix concrete plant in Mexico at Zapopan, Jalisco; investment of almost MXN 51 million; 8 electric mixer trucks + front loader with own charging infrastructure; NextGen Growth 2030 frame. CapEx = ~MXN 51m. Distinct from holcim_comosa_mexico_2025 ready-mix network and holcim_pacasmayo_peru_2025.",
    "51000000",
    "2025-11-26",
    "2025",
    "20.72",
    "-103.39",
    "Holcim Zapopan electric ready-mix plant, Jalisco, Mexico (company geography; approximate Zapopan pin).",
    "holcim_mx_zapopan_electric_20251126",
    "Con una inversión de casi 51 millones de pesos, esta planta ubicada en Jalisco representa el inicio de la electrificación de las operaciones de Holcim México. … inaugurar en Zapopan, Jalisco la primera planta de concreto premezclado 100% eléctrica en México",
    "https://www.holcim.com.mx/holcim-inaugura-la-primera-planta-de-concreto-100-electrica-en-mexico",
    "Actor: Holcim México (Swiss Holcim) — allied. Company Spanish primary. CapEx ≈ MXN 51m (MXN stored without FX). Shuffle building_materials.",
    "hunt_cycle195",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="MXN",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Holcim México. “Holcim inaugura la primera planta de concreto 100% eléctrica en México.” November 26, 2025. https://www.holcim.com.mx/holcim-inaugura-la-primera-planta-de-concreto-100-electrica-en-mexico.',
    annotation="Holcim MX: Zapopan electric plant ~MXN 51m. Supports holcim_zapopan_electric_51m_mxn_2025.",
    evid_note="Opened Holcim México Spanish release 2026-10-04.",
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
    print(f"cycle195 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
