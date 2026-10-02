#!/usr/bin/env python3
"""Cycle 175 hunt: shuffle_seed=20261175; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261175)): other_renewables, nickel, rail,
copper, water, fission_smr, building_materials, port_cranes, balsa, engineering_epc,
port_ownership, niobium, power_plants_grid, lithium, wind, solar, graphite,
bridges_roads.

Thin top-up (recomputed after shuffle pass): nickel / balsa / fission_smr —
nickel filled (Centaurus Jaguar ONS 230kV grid approval); balsa/fission dry this
pass (AIMA/WITS Ecuador balsa and Meitner/Colombia fission already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail
past MoU (still prefeasibility/feasibility).
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


# 1. other_renewables / other — Verano Domeyko solar+BESS CapEx Chile
row_doc(
    "verano_domeyko_capex_247m_2025",
    "energy",
    "other_renewables",
    "other",
    "Verano Energy + Lumina Capital — Domeyko 83 MWp solar + 660 MWh BESS (Atacama)",
    "Chile",
    "27 Aug 2025 (Verano): Domeyko Solar + BESS (83 MWp PV / 660 MWh storage near Vallenar, Atacama) total CapEx USD 247 million; financing stack USD 176m project-finance term loan (SMBC, Société Générale, Scotiabank) + USD 12m VAT debt (Scotiabank) with Lumina Capital equity; Abastible long-term PPA; COD targeted end-2026; construction underway. Distinct from sungrow_verano_observatorio_bess_2026.",
    "247000000",
    "2025-08-27",
    "2025",
    "",
    "",
    "Domeyko / near Vallenar, Atacama Region — lat/lon blank pending verified worksite coords.",
    "verano_domeyko_financing_20250827",
    "Domeyko project will demand a total capex of USD 247 million, which will be financed through a project finance term-loan of USD 176 million provided by a consortium of leading international banks – SMBC, Société Générale, and Scotiabank –, and together with a USD 12 million in VAT debt financing provided by Scotiabank. Equity will be provided as part of Verano’s partnership with Lumina Capital Management… Located in northern Chile near Vallenar in the Atacama Region… Construction is underway, with commercial operations expected by the end of 2026.",
    "https://verano.energy/verano-energy-secures-usd-204-million-project-finance-facility-to-advance-domeyko-solar-storage-project-in-chile/",
    "Actor: Verano Energy (Chilean IPP) with Lumina Capital equity — other. Opened Verano company English release 27 Aug 2025. Solar+storage filed under other_renewables (shuffle lead). CapEx = USD 247m (financing close headline USD 204m = term loan + VAT debt).",
    "hunt_cycle175",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='Verano Energy. “Verano Energy secures USD 204 Million Project Finance facility to advance Domeyko Solar + Storage project in Chile.” August 27, 2025. https://verano.energy/verano-energy-secures-usd-204-million-project-finance-facility-to-advance-domeyko-solar-storage-project-in-chile/.',
    annotation="Verano: Domeyko solar+BESS CapEx USD 247m / financing close. Supports verano_domeyko_capex_247m_2025.",
    evid_note="Opened Verano Energy company press page 2026-10-02.",
)

# 2. nickel / allied — Centaurus Jaguar ONS 230kV grid approval (thin top-up)
row_doc(
    "centaurus_jaguar_ons_grid_2026",
    "resources",
    "nickel",
    "allied",
    "Centaurus Metals — Jaguar Ni ONS 230kV national grid connection approval (Pará)",
    "Brazil",
    "15 Jul 2026 (ASX): Centaurus Níquel Ltda. receives ONS approval to connect Jaguar Nickel Sulphide Project to Brazil’s national 230kV grid; initial 20MW allocation via 36km transmission-line extension to Jaguar main substation; environmental/mining approvals and mining easement already secured; R$9.7m (A$2.7m) ONS guarantee due within 90 days at FID. CapEx blank (grid-access approval; guarantee not project CapEx). Distinct from centaurus_jaguar_jvep_capex_2025 / BNDES LOI / Glencore offtake / intl finance rows.",
    "",
    "",
    "2026",
    "-6.65",
    "-49.0",
    "Jaguar Nickel Project, Carajás / Pará (Centaurus ASX; approximate pin shared with prior Jaguar rows).",
    "centaurus_jaguar_ons_20260715",
    "Centaurus Metals (ASX Code: CTM, OTCQX: CTTZF) is pleased to announce that its wholly-owned Brazilian subsidiary Centaurus Níquel Ltda., has received approval from the Operador Nacional do Sistema Elétrico – ONS (National Operator of the Electric Grid) to connect the Company’s flagship Jaguar Nickel Sulphide Project in Brazil to the national 230kV power grid. The approval secures an initial allocation of 20MW of power… The connection will be established via construction of a 36km extension from the existing 230kV transmission line to Jaguar´s main substation.",
    "https://www.centaurus.com.au/site/pdf/34d3a712-d857-4539-9f40-b2de8891eb76/Platform/ListPage/HV-National-Power-Grid-Connection-Approved-for-Jaguar.pdf",
    "Actor: Centaurus Metals (Australian ASX) — allied. Opened company ASX PDF 15 Jul 2026. Thin nickel top-up; infrastructure de-risking ahead of FID.",
    "hunt_cycle175",
    investment_type="other",
    evidence="documented",
    bib_type="company",
    chicago='Centaurus Metals Limited. “High-Voltage National Power Grid Connection Approved for the Jaguar Nickel Sulphide Project.” ASX release, July 15, 2026. https://www.centaurus.com.au/site/pdf/34d3a712-d857-4539-9f40-b2de8891eb76/Platform/ListPage/HV-National-Power-Grid-Connection-Approved-for-Jaguar.pdf.',
    annotation="Centaurus ASX: Jaguar ONS 230kV / 20MW grid approval. Supports centaurus_jaguar_ons_grid_2026.",
    evid_note="Opened Centaurus ASX PDF 2026-10-02.",
)

# 3. rail / us — Wabtec ES44 fleet for Arauco Sucuriú private rail
row_doc(
    "wabtec_arauco_sucuriu_26es44_2026",
    "infrastructure",
    "rail",
    "us",
    "Wabtec — 26× ES44 Evolution locomotives for Arauco Sucuriú EF-A35 (Inocência, MS)",
    "Brazil",
    "24–26 Mar 2026 (ABIFER / Tecnologística): Arauco receives first Wabtec ES44 locomotives for Projeto Sucuriú private shortline EF-A35 (Inocência, Mato Grosso do Sul); planned fleet 26 ES44 units + 721 wagons; 45 km main line + 9 km industrial tracks connecting mill to Rumo Malha Norte toward Porto de Santos; compositions up to 9,600 t; rail ops targeted with mill COD end-2027. CapEx blank (fleet count disclosed; locomotive contract USD not on opened ABIFER page). Distinct from ge_vernova_arauco_sucuriu_gis_2025.",
    "",
    "",
    "2026",
    "",
    "",
    "EF-A35 / Projeto Sucuriú, Inocência (MS) — lat/lon blank (shortline corridor + Contagem build).",
    "abifer_arauco_wabtec_sucuriu_20260326",
    "A Arauco dá mais um passo na implantação do Projeto Sucuriú, em Inocência (MS), ao receber as primeiras locomotivas da Wabtec que irão integrar a infraestrutura logística de sua futura fábrica de celulose. Ao todo, serão 26 unidades do modelo ES44 operando em uma ferrovia própria, a EF-A35… O projeto foi dimensionado para operar composições de até 9.600 toneladas, com uma frota de 26 locomotivas e 721 vagões. A ferrovia vai iniciar as operações ao mesmo tempo que a fábrica de celulose, no final de 2027.",
    "https://abifer.org.br/arauco-avanca-na-estrutura-logistica-do-projeto-sucuriu-com-recebimento-das-primeiras-locomotivas-da-wabtec/",
    "Actor: Wabtec Corporation (U.S.) — us; Arauco (Chilean) host mill. Opened ABIFER market note 26 Mar 2026 (sourced Hoje Mais 24 Mar 2026). U.S. side-balance for rail.",
    "hunt_cycle175",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="trade_press",
    chicago='ABIFER. “Arauco avança na estrutura logística do Projeto Sucuriú com recebimento das primeiras locomotivas da Wabtec.” March 26, 2026. https://abifer.org.br/arauco-avanca-na-estrutura-logistica-do-projeto-sucuriu-com-recebimento-das-primeiras-locomotivas-da-wabtec/.',
    annotation="ABIFER: Wabtec 26× ES44 for Arauco Sucuriú EF-A35. Supports wabtec_arauco_sucuriu_26es44_2026.",
    evid_note="Opened ABIFER Portuguese page 2026-10-02.",
)

# 4. copper / us — Caterpillar/Ferreyros Antamina Cat 798 fleet to 45
row_doc(
    "caterpillar_antamina_798_45_2026",
    "resources",
    "copper",
    "us",
    "Caterpillar + Ferreyros — Antamina Cat 798 ultra-class fleet to 45 units (Áncash)",
    "Peru",
    "3 Aug 2026 (Ferreyros): Antamina expands Cat 798 ultra-class haul-truck fleet to 45 units at Áncash (~4,300 masl) by purchasing 27 Cat 798 trucks (400 t payload) from Ferreyros, adding to 18 already on site; 24/7 on-site Ferreyros support. CapEx blank (unit count disclosed; USD not on opened Ferreyros page). Distinct from caterpillar_las_bambas_fleet_2026 and caterpillar_vale_northern_autonomous_2025.",
    "",
    "",
    "2026",
    "",
    "",
    "Antamina mine, Áncash (~4,300 masl) — lat/lon blank pending verified pit pin.",
    "ferreyros_antamina_798_20260803",
    "En línea con su apuesta por la excelencia operativa, Antamina expandió su flota de camiones ultraclass CAT 798, de máxima envergadura, hasta alcanzar las 45 unidades. La compañía minera adquirió a Ferreyros un total de 27 camiones de este modelo, los cuales se suman a los 18 con los que ya cuenta este yacimiento ubicado en la región Áncash, a 4,300 m.s.n.m.",
    "https://www.ferreyros.com.pe/noticia/antamina-elige-a-caterpillar-y-ferreyros-para-expansion-de-flota-de-camiones-ultraclass-de-400-toneladas/",
    "Actor: Caterpillar Inc. (U.S.) via Ferreyros dealer — us; Antamina (BHP/Glencore/Teck/Mitsubishi JV) host copper-zinc mine. Opened Ferreyros Spanish release 3 Aug 2026. U.S. side-balance for copper.",
    "hunt_cycle175",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Ferreyros. “Antamina elige a Caterpillar y Ferreyros para expansión de flota de camiones ultraclass de 400 toneladas.” August 3, 2026. https://www.ferreyros.com.pe/noticia/antamina-elige-a-caterpillar-y-ferreyros-para-expansion-de-flota-de-camiones-ultraclass-de-400-toneladas/.',
    annotation="Ferreyros: Antamina Cat 798 fleet to 45 units. Supports caterpillar_antamina_798_45_2026.",
    evid_note="Opened Ferreyros company news page 2026-10-02.",
)

# 5. water / miss; fission_smr / miss; building_materials / miss; port_cranes / miss; balsa / miss

# 6. engineering_epc / us — Caterpillar/Ferreyros Las Bambas ultra-class fleet
row_doc(
    "caterpillar_las_bambas_fleet_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Caterpillar + Ferreyros — Las Bambas ultra-class mining fleet (to 45 units)",
    "Peru",
    "1 Jun 2026 (Ferreyros): Minera Las Bambas awards Ferreyros/Caterpillar tender for large mining fleet expandable to 45 units, including full ultra-class haul fleet of 27 Cat 798 (400 t) trucks; 2026 deliveries >20 machines (12 trucks, Cat 7495 shovel, MD6380 drill, auxiliaries). CapEx blank (unit counts disclosed; USD not on opened Ferreyros page). Distinct from mmg_las_bambas_* CapEx rows and caterpillar_antamina_798_45_2026.",
    "",
    "",
    "2026",
    "-14.083",
    "-72.317",
    "Las Bambas, Cotabambas/Grau, Apurímac (shared MMG operations pin).",
    "ferreyros_las_bambas_fleet_20260601",
    "Minera Las Bambas otorgó a Ferreyros, líder en maquinaria pesada, la licitación de una extensa flota de máquinas para la gran minería, con la posibilidad de extenderse hasta las 45 unidades; entre ellas, la totalidad de la flota de camiones ultra class, que asciende a 27 unidades Cat 798 de 400 toneladas métricas. Este año, Ferreyros entregará más de 20 máquinas, que incluyen 12 camiones, una pala gigante Cat 7495, una perforadora MD6380 y equipos auxiliares de gran envergadura.",
    "https://www.ferreyros.com.pe/noticia/minera-las-bambas-otorga-a-ferreyros-y-caterpillar-licitacion-de-gran-flota-de-maquinas-gigantes/",
    "Actor: Caterpillar Inc. (U.S.) via Ferreyros dealer — us; Las Bambas (MMG) host. Opened Ferreyros Spanish release 1 Jun 2026. U.S. side-balance for engineering_epc.",
    "hunt_cycle175",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Ferreyros. “Minera Las Bambas otorga a Ferreyros y Caterpillar licitación de gran flota de máquinas gigantes.” June 1, 2026. https://www.ferreyros.com.pe/noticia/minera-las-bambas-otorga-a-ferreyros-y-caterpillar-licitacion-de-gran-flota-de-maquinas-gigantes/.',
    annotation="Ferreyros: Las Bambas Cat ultra-class fleet tender to 45 units. Supports caterpillar_las_bambas_fleet_2026.",
    evid_note="Opened Ferreyros company news page 2026-10-02.",
)

# 7. port_ownership / miss; niobium / miss; power_plants_grid / miss; lithium / miss

# 8. wind / other — Aluar La Flecha 336 MW Goldwind package CapEx
row_doc(
    "aluar_la_flecha_400m_2024",
    "energy",
    "wind",
    "other",
    "Aluar — La Flecha / Puerto Madryn Stage V wind park 336 MW (Goldwind GW165)",
    "Argentina",
    "8 Aug 2024 (Ámbito): Aluar announces USD 400 million Stage V expansion of Puerto Madryn wind park to install Goldwind 6 MW turbines adding 336 MW (56× GW165 after 2024 add-on from 52/312 MW plan); park total to 582 MW by end-2026 after cumulative ~USD 745m. 10 Jun 2026 (Data Energía): mounting of all 56 turbines complete; commercial ops targeted Oct 2026. CapEx = USD 400m Stage V. Distinct from goldwind_rio_cullen_argentina_2026.",
    "400000000",
    "2024-08-08",
    "2024",
    "",
    "",
    "Parque Eólico La Flecha / ~45 km from Puerto Madryn, Chubut — lat/lon blank pending verified turbine-field pin.",
    "ambito_aluar_flecha_400m_20240808",
    "Aluar anunció el inicio de las obras de ampliación para una quinta etapa de crecimiento de su parque eólico en Puerto Madryn, que demandará una inversión de u$s400 millones para instalar aerogeneradores Goldwind de 6 MW… Con una inversión de u$s400 millones para instalar aerogeneradores Goldwind de 6 MW, se sumarán 336 MW de potencia adicional al parque existente… Para fines de 2026, tras una inversión total de u$s745 millones, el Parque… con una potencia instalada de 582 MW.",
    "https://www.ambito.com/negocios/aluar-anuncio-una-inversion-us400-millones-ampliar-su-parque-eolico-puerto-madryn-n6045740",
    "Actor: Aluar (Argentine aluminum producer) — other; Goldwind (PRC OEM) turbine supply noted. Opened Ámbito 8 Aug 2024; mounting completion cross-checked Data Energía 10 Jun 2026. CapEx attributed to Aluar host investor.",
    "hunt_cycle175",
    investment_type="greenfield",
    evidence="documented",
    bib_type="trade_press",
    chicago='Ámbito. “Aluar anunció una inversión de u$s400 millones para ampliar su parque eólico en Puerto Madryn.” August 8, 2024. https://www.ambito.com/negocios/aluar-anuncio-una-inversion-us400-millones-ampliar-su-parque-eolico-puerto-madryn-n6045740.',
    annotation="Ámbito: Aluar La Flecha Stage V USD 400m / 336 MW Goldwind. Supports aluar_la_flecha_400m_2024.",
    evid_note="Opened Ámbito page 2026-10-02; mounting completion cross-checked Data Energía.",
)

# 9. solar / prc — CGN Brasil Lagoinha 165 MW COD (Russas, CE)
# ECB 2026-06-09: EURUSD=1.1573; EURBRL=5.9751 → USD/BRL = 1.1573/5.9751 ≈ 0.1936871349
row_doc(
    "cgn_lagoinha_165mw_cod_2026",
    "energy",
    "solar",
    "prc",
    "CGN Brasil — Complexo Solar Lagoinha I–IV 165 MW COD (Russas, Ceará)",
    "Brazil",
    "9 Jun 2026 (pv magazine Brasil): Aneel authorizes commercial operation of Lagoinha I–IV totaling 165 MW installed in Russas, Ceará — CGN Brasil’s first greenfield solar complex in Brazil (~304 ha; ~337k modules); estimated investment R$650 million; 17-year PPA with Rede D’Or for 57 MW average. Construction started Dec 2023; energization/tests 2025. USD 125,896,637.71 via ECB 2026-06-09 cross (USD/EUR 1.1573 ÷ BRL/EUR 5.9751).",
    "650000000",
    "2026-06-09",
    "2026",
    "",
    "",
    "Complexo Solar Lagoinha, Russas, Ceará — lat/lon blank pending verified plant pin.",
    "pv_mag_cgn_lagoinha_cod_20260609",
    "A Agência Nacional de Energia Elétrica (Aneel) autorizou a operação comercial das usinas fotovoltaicas Lagoinha I, II, III e IV, que somam 165 MW de capacidade instalada no município de Russas, no Ceará… O complexo é o primeiro projeto solar greenfield desenvolvido pela CGN Brasil no país… representa um investimento estimado em R$ 650 milhões. A energia gerada pelo complexo está vinculada a um contrato de compra e venda de longo prazo (PPA) firmado com a Rede D’Or, com fornecimento de 57 MW médios por um período de 17 anos.",
    "https://www.pv-magazine-brasil.com/2026/06/09/aneel-libera-operacao-comercial-de-165-mw-solares-da-cgn-no-ceara/",
    "Actor: CGN Brasil (China General Nuclear Power Group affiliate) — prc. Opened pv magazine Brasil 9 Jun 2026. FX: ECB EXR D.USD.EUR and D.BRL.EUR 2026-06-09. Distinct from cgn_goldwind_tanque_novo_bess_2025 and cgn_piaui_csp_mou_2026.",
    "hunt_cycle175",
    investment_type="greenfield",
    evidence="documented",
    currency="BRL",
    value_usd="125896637.71",
    fx_usd="0.1936871349",
    bib_type="trade_press",
    chicago='Neris, Alessandra. “Aneel libera operação comercial de 165 MW solares da CGN no Ceará.” pv magazine Brasil, June 9, 2026. https://www.pv-magazine-brasil.com/2026/06/09/aneel-libera-operacao-comercial-de-165-mw-solares-da-cgn-no-ceara/.',
    annotation="pv magazine Brasil: CGN Lagoinha 165 MW COD / R$650m. Supports cgn_lagoinha_165mw_cod_2026.",
    evid_note="Opened pv magazine Brasil page 2026-10-02; ECB FX cross 2026-06-09.",
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
    print(f"Cycle 175 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
