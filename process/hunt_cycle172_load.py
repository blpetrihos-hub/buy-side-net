#!/usr/bin/env python3
"""Cycle 172 hunt: shuffle_seed=20261172; equal budget; U.S./PRC split; thin after.

Canonical shuffle (codebook order + Random(20261172)): port_cranes,
power_plants_grid, rail, engineering_epc, balsa, other_renewables, wind,
fission_smr, niobium, port_ownership, solar, bridges_roads, copper, water,
lithium, building_materials, nickel, graphite.

Thin top-up (recomputed after shuffle pass): nickel / balsa / fission_smr —
fission filled (Diamante Jorge Lacerda SMR LOI); nickel/balsa dry this pass
(catalog dense; AIMA/WITS Ecuador balsa 2025 already logged).
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


# 1. port_cranes / prc — HHMC ships 3 STS to Puerto Antioquia
row_doc(
    "hhmc_puerto_antioquia_sts_2025",
    "infrastructure",
    "port_cranes",
    "prc",
    "Qingdao Haixi (HHMC) — 3 STS cranes to Puerto Antioquia",
    "Colombia",
    "20 Jan 2025: Qingdao Hisea Heavy-duty Machinery (HHMC) ships three large STS container cranes for Puerto Antioquia (Urabá, Colombia): 65 t under spreader, 60 m outreach, 54 m lift height above rail; post-Panamax capable; CapEx blank (equipment supply; no unit price on opened page).",
    "",
    "",
    "2025",
    "",
    "",
    "Puerto Antioquia, Gulf of Urabá — lat/lon blank pending single berth pin.",
    "hhmc_antioquia_sts_20250121",
    "On January 20, three large Ship-To-Shore container cranes(STS), manufactured by Qingdao Hisea Heavy-duty Machinery Co.,Ltd. for the Antioquia Port in Colombia, were successfully dispatched. These cranes have a rated lifting capacity of 65 tons under the spreader, a forward outreach of 60 meters, and a lifting height of 54 meters above the rail.",
    "https://en.qdhhmc.com/News/view/id/1616.html",
    "Actor: HHMC / Qingdao Haixi (PRC crane OEM) — prc. Opened HHMC English news 21 Jan 2025. Distinct from konecranes_puerto_antioquia_8rtg_2023 (allied RTGs) and cma_puerto_antioquia_colombia (port ownership).",
    "hunt_cycle172",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Qingdao Haixi Heavy-duty Machinery Co., Ltd. “3 Large STS Shipped to Colombia.” January 21, 2025. https://en.qdhhmc.com/News/view/id/1616.html.',
    annotation="HHMC: three STS dispatched to Puerto Antioquia. Supports hhmc_puerto_antioquia_sts_2025.",
    evid_note="Opened HHMC company English news page 2026-10-02.",
)

# 2. power_plants_grid / us — GE Vernova Neuquén aero repair center
row_doc(
    "ge_vernova_neuquen_aero_repair_2025",
    "energy",
    "power_plants_grid",
    "us",
    "GE Vernova — Aeroderivative gas-turbine Repair Service Center (Centenario, Neuquén)",
    "Argentina",
    "23 Oct 2025: GE Vernova inaugurates first Latin America Aeroderivative Repair Service Center in Parque Industrial Centenario, Neuquén; initially LMS100 maintenance, expanding to LM2500/LM6000 by end-2026; serves Argentina, Brazil, Chile, Uruguay fleets. CapEx blank (facility opening; no disclosed build cost).",
    "",
    "",
    "2025",
    "",
    "",
    "Parque Industrial Centenario, Neuquén Province — lat/lon blank pending verified worksite coords.",
    "ge_vernova_neuquen_repair_20251023",
    "GE Vernova Inc. (NYSE: GEV) today celebrated the opening of a new Repair Service Center in the Parque industrial Centenario, in the Neuquén Province, Argentina. The new facility marks GE Vernova’s first repair center for GE Vernova’s Aeroderivative business in Latin America and is expected to boost repair capabilities for GE Vernova’s aero derivatives gas turbines fleet based in Argentina, Brazil, Chile and Uruguay.",
    "https://www.gevernova.com/news/press-releases/ge-vernova-inaugurates-its-first-repair-center-enhanced-aero-derivative-gas-turbine",
    "Actor: GE Vernova (U.S.) — us. Opened GE Vernova press release 23 Oct 2025. U.S. side-balance for power_plants_grid.",
    "hunt_cycle172",
    investment_type="other",
    evidence="documented",
    bib_type="company",
    chicago='GE Vernova. “GE Vernova inaugurates its first repair center for enhanced aero-derivative gas turbine support in southern Latin America.” October 23, 2025. https://www.gevernova.com/news/press-releases/ge-vernova-inaugurates-its-first-repair-center-enhanced-aero-derivative-gas-turbine.',
    annotation="GE Vernova: Neuquén aeroderivative repair center opening. Supports ge_vernova_neuquen_aero_repair_2025.",
    evid_note="Opened GE Vernova press release 2026-10-02.",
)

# 3. rail / us — USTDA Brazil freight rail reverse trade mission
row_doc(
    "ustda_brazil_freight_rail_rtm_2024",
    "infrastructure",
    "rail",
    "us",
    "USTDA — Brazil freight-rail modernization reverse trade mission",
    "Brazil",
    "17 Oct 2024: USTDA funds reverse trade mission bringing Brazilian rail-sector leaders to the United States (Washington, Dallas, Chicago; 20–31 Oct) to accelerate modernization/decarbonization of Brazil’s freight rail network and connect U.S. suppliers (battery/hydrogen locomotives, digital technologies). CapEx blank (partnership-building RTM; no project award).",
    "",
    "",
    "2024",
    "",
    "",
    "Brazil national freight-rail network — lat/lon blank (mission; no single named worksite).",
    "ustda_brazil_freight_rtm_20241017",
    "The U.S. Trade and Development Agency is funding a reverse trade mission that will bring a delegation of Brazilian rail sector leaders to the United States, to build partnerships with U.S. industry and accelerate the modernization and decarbonization of Brazil’s freight rail network.",
    "https://www.ustda.gov/ustda-advances-freight-modernization-in-brazil/",
    "Actor: USTDA (U.S. agency) — us. Opened USTDA press release 17 Oct 2024. Distinct from progress_rail_vli_* and wabtec_mrs_254m_2026 equipment deals.",
    "hunt_cycle172",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='U.S. Trade and Development Agency. “USTDA Advances Freight Modernization in Brazil.” October 17, 2024. https://www.ustda.gov/ustda-advances-freight-modernization-in-brazil/.',
    annotation="USTDA: Brazil freight-rail RTM. Supports ustda_brazil_freight_rail_rtm_2024.",
    evid_note="Opened USTDA press release 2026-10-02.",
)

# 4. rail / prc — Guangzhou Metro + CCECC Regiotram O&M RMB 2.06bn
row_doc(
    "guangzhou_metro_regiotram_om_rmb2060m_2026",
    "infrastructure",
    "rail",
    "prc",
    "Guangzhou Metro Group + CCECC — RegioTram de Occidente O&M contract",
    "Colombia",
    "12 Jun 2026: Colombian Consulate Guangzhou reports signing of RegioTram de Occidente O&M contract between Guangzhou Metro Group and CCECC for RMB 2,060 million (~USD 302.5m at PBOC 6.8109 CNY/USD on 12 Jun 2026); Guangzhou Metro to operate/maintain Colombia’s first electric regional train (Bogotá–Funza–Mosquera–Madrid–Facatativá; 39.66 km / 17 stations) for 21.5 years; first segment targeted Oct 2027.",
    "2060000000",
    "2026-06-12",
    "2026",
    "",
    "",
    "RegioTram Occidente corridor (Bogotá–Facatativá) — lat/lon blank (multi-station line).",
    "consulado_gz_regiotram_om_20260612",
    "El contrato, suscrito entre el Grupo Metro de Guangzhou y China Civil Engineering Construction Corporation, asciende a 2.060 millones de RMB (aproximadamente 295 millones de dólares estadounidenses) y establece que la empresa Guangzhou Metro Group será la encargada de operar el RegioTram de Occidente… durante un periodo de 21.5 años… Se prevé que su primer tramo entre en funcionamiento en octubre de 2027.",
    "https://guangzhou.consulado.gov.co/sala-de-prensa/noticias/consulado-en-guangzhou-acompana-la-historica-firma-del-contrato-de-operacion-y-mantenimiento-del-regiotram-de-occidente",
    "Actor: Guangzhou Metro Group + CCECC (PRC) — prc. Opened Colombian Consulate Guangzhou Spanish release 12 Jun 2026. Value = RMB 2.06bn; USD via PBOC central parity 6.8109 CNY/USD (Xinhua/CFETS 12 Jun 2026). Consulate USD ~295m is approximate. Distinct from CHEC Bogotá Metro L1.",
    "hunt_cycle172",
    investment_type="other",
    evidence="documented",
    currency="CNY",
    value_usd="302456357",
    fx_usd="0.14682347",
    bib_type="government",
    chicago='Consulado General de Colombia en Guangzhou. “Consulado en Guangzhou acompaña la histórica firma del contrato de operación y mantenimiento del Regiotram de Occidente.” June 12, 2026. https://guangzhou.consulado.gov.co/sala-de-prensa/noticias/consulado-en-guangzhou-acompana-la-historica-firma-del-contrato-de-operacion-y-mantenimiento-del-regiotram-de-occidente.',
    annotation="Colombian Consulate Guangzhou: RegioTram O&M RMB 2.06bn. Supports guangzhou_metro_regiotram_om_rmb2060m_2026.",
    evid_note="Opened Consulate Guangzhou Spanish page 2026-10-02; FX from PBOC/CFETS 6.8109 CNY/USD 12 Jun 2026 (Xinhua).",
)

# 5. engineering_epc / allied — Eiffage + Jan De Nul Callao Muelle Norte >€100m
row_doc(
    "eiffage_jande_nul_callao_norte_2026",
    "infrastructure",
    "engineering_epc",
    "allied",
    "Eiffage + Jan De Nul — Callao Muelle Norte design-build expansion",
    "Peru",
    "16 Apr 2026: Eiffage (via Eiffage Génie Civil Marine) with Jan De Nul awarded design-build contract by APM Terminals Callao for Muelle Norte expansion: demolish docks 4 and 5C; build new piled dock 5C (441 m × 44 m); contract >€100 million; 21 months incl. 5-month study. Value stored as €100m floor (source: “more than €100 million”); USD via Fed H.10 euro 1.1783 on 16 Apr 2026.",
    "100000000",
    "2026-04-16",
    "2026",
    "",
    "",
    "APM Terminals Callao, Muelle Norte — lat/lon blank pending berth pin.",
    "eiffage_callao_muelle_norte_20260416",
    "Eiffage, through its subsidiary Eiffage Génie Civil Marine, has been awarded, in consortium with the Belgian company Jan de Nul, the design-build contract for the Port of Callao Muelle Norte expansion in Peru. The contract is worth more than €100 million.",
    "https://www.eiffage.com/files/live/sites/eiffagev2/files/M%C3%A9dias/Communiqu%C3%A9%20de%20presse/2026/PR_Eiffage_Port%20of%20Callao%20Muelle%20Norte_20260416.pdf",
    "Actor: Eiffage (France) + Jan De Nul (Belgium) — allied. Opened Eiffage PDF press release 16 Apr 2026. Floor CapEx €100m (source says more than). Distinct from CAF EPSA Puerto Exterior and COSCO Chancay rows.",
    "hunt_cycle172",
    investment_type="epc",
    evidence="documented",
    currency="EUR",
    value_usd="117830000",
    fx_usd="1.1783",
    bib_type="company",
    chicago='Eiffage. “Eiffage wins in consortium the contract for the Port of Callao Muelle Norte expansion project in Peru in a deal worth over €100 million.” April 16, 2026. https://www.eiffage.com/files/live/sites/eiffagev2/files/M%C3%A9dias/Communiqu%C3%A9%20de%20presse/2026/PR_Eiffage_Port%20of%20Callao%20Muelle%20Norte_20260416.pdf.',
    annotation="Eiffage PDF: Callao Muelle Norte >€100m design-build. Supports eiffage_jande_nul_callao_norte_2026.",
    evid_note="Opened Eiffage PDF press release 2026-10-02; FX Fed H.10 euro 1.1783 on 16 Apr 2026.",
)

# 6. fission_smr / other — Diamante Jorge Lacerda SMR Coal-to-Nuclear LOI (thin)
row_doc(
    "diamante_jorge_lacerda_smr_loi_2026",
    "energy",
    "fission_smr",
    "other",
    "Diamante Energia + IAEA + ABDAN — Jorge Lacerda Coal-to-Nuclear SMR LOI",
    "Brazil",
    "16 Sep 2026: Diamante Geração de Energia signs Letter of Intent in Vienna with IAEA and ABDAN to study converting a coal unit at Complexo Termelétrico Jorge Lacerda (Capivari de Baixo, SC; 740 MW complex) to an SMR under Coal-to-Nuclear (C2N); LOI covers studies, public awareness, SMR knowledge exchange, and decision-support activities — not a construction award. CapEx blank (study/LOI stage).",
    "",
    "",
    "2026",
    "",
    "",
    "Complexo Termelétrico Jorge Lacerda, Capivari de Baixo, Santa Catarina — lat/lon blank pending named unit pin.",
    "diamante_iaea_abdan_smr_loi_20260916",
    "A Agência Internacional de Energia Atômica (AIEA)… a Diamante Geração de Energia e a Associação Brasileira para Desenvolvimento de Atividades Nucleares (ABDAN) formalizaram… uma parceria… por meio da assinatura de uma Carta de Intenções em Viena… Colaborar nos estudos para conversão de usina termelétrica a carvão em instalação de Small Modular Reactor, no âmbito do projeto C2N…",
    "https://www.diamanteenergia.com/pt/noticias/diamante-energia-agencia-internacional-de-energia-atomica-e-abdan-formalizam-parceria-para-impulsionar-o-desenvolvimento-nuclear-no-brasil",
    "Actor: Diamante Energia (Brazilian private) + IAEA/ABDAN — other (host firm; no U.S./PRC vendor named). Opened Diamante company news 16 Sep 2026. Thin fission_smr top-up.",
    "hunt_cycle172",
    investment_type="other",
    evidence="documented",
    bib_type="company",
    chicago='Diamante Energia. “Diamante Energia, Agência Internacional de Energia Atômica e ABDAN formalizam parceria para impulsionar o desenvolvimento nuclear no Brasil.” September 16, 2026. https://www.diamanteenergia.com/pt/noticias/diamante-energia-agencia-internacional-de-energia-atomica-e-abdan-formalizam-parceria-para-impulsionar-o-desenvolvimento-nuclear-no-brasil.',
    annotation="Diamante: Jorge Lacerda C2N SMR LOI with IAEA/ABDAN. Supports diamante_jorge_lacerda_smr_loi_2026.",
    evid_note="Opened Diamante Energia Portuguese company news 2026-10-02.",
)

# 7. wind / allied — EDF Naupac Pescadores 348 MW / USD 393.5m
row_doc(
    "edf_naupac_pescadores_348mw_2026",
    "energy",
    "wind",
    "allied",
    "Naupac (EDF Renewables) — Parque Eólico Pescadores 348 MW",
    "Peru",
    "13 Jan 2026: MINEM RD 0006-2026-MINEM/DGAAE approves EIAsd for Parque Eólico Pescadores (348 MW; 58×6 MW turbines) by Naupac Generación Renovable Perú S.A.C. (EDF Renewables affiliate) in Ático/Ocoña, Arequipa, with 220 kV interconnection to SE Ocoña; MINEM evaluation report states total investment USD 393,546,635.70 (ex-IGV).",
    "393546636",
    "2026-01-13",
    "2026",
    "",
    "",
    "Ático and Ocoña districts, Arequipa — lat/lon blank pending turbine-array centroid.",
    "minem_rd_pescadores_eiasd_20260113",
    "APROBAR el Estudio de Impacto Ambiental semidetallado del proyecto “Parque Eólico Pescadores de 348 MW y su Interconexión al SEIN”, presentado por Naupac Generación Renovable Perú S.A.C.… La inversión total del Proyecto se estima en US$ 393 546 635,70",
    "https://www.gob.pe/institucion/minem/normas-legales/7643163-0006-2026-minem-dgaa6",
    "Actor: Naupac / EDF Renewables (France) — allied. Opened MINEM gob.pe RD page + evaluation PDF CapEx line. Distinct from vestas_emma_peru_72mw_2026.",
    "hunt_cycle172",
    investment_type="epc",
    evidence="documented",
    bib_type="government",
    chicago='Perú, Ministerio de Energía y Minas. “Resolución Directoral N.° 0006-2026-MINEM/DGAAE” (Parque Eólico Pescadores 348 MW EIAsd). January 13, 2026. https://www.gob.pe/institucion/minem/normas-legales/7643163-0006-2026-minem-dgaa6.',
    annotation="MINEM RD: approves Pescadores 348 MW EIAsd; CapEx USD 393.5m in evaluation report. Supports edf_naupac_pescadores_348mw_2026.",
    evid_note="Opened gob.pe RD page and MINEM evaluation PDF CapEx line 2026-10-02.",
)

# 8. wind / allied — ANDE–EDF Chaco wind studies (Paraguay under-covered)
row_doc(
    "ande_edf_chaco_wind_studies_2025",
    "energy",
    "wind",
    "allied",
    "ANDE + EDF — Chaco (Boquerón) wind-resource studies / technical cooperation",
    "Paraguay",
    "20 Oct 2025: La Nación reports ANDE developing strategic wind measurements in northwest Chaco (Boquerón) under technical cooperation with Électricité de France (EDF); ANDE renewables team visited EDF’s Fécamp offshore wind farm; exploration/study phase only — no implementation project yet. CapEx blank.",
    "",
    "",
    "2025",
    "",
    "",
    "Boquerón department, northwest Chaco — lat/lon blank (measurement campaign; no named farm site).",
    "lanacion_ande_edf_chaco_wind_20251020",
    "La Administración Nacional de Electricidad (Ande) se encuentra desarrollando mediciones estratégicas en la región noroeste del Chaco paraguayo, en el departamento de Boquerón… En el marco del acuerdo de cooperación técnica firmado con la empresa Électricité de France (EDF)… Esta misión forma parte de la fase de exploración y estudio… sin implicar aún una etapa de implementación de proyectos.",
    "https://www.lanacion.com.py/pais/2025/10/20/ande-evalua-alternativas-para-explotar-la-energia-eolica-en-el-chaco/",
    "Actor: EDF (France) technical partner with ANDE — allied. Opened La Nación Paraguay 20 Oct 2025. Paraguay×wind under-covered cell; CapEx blank (pre-project studies).",
    "hunt_cycle172",
    investment_type="other",
    evidence="documented",
    bib_type="press",
    chicago='La Nación (Paraguay). “Ande evalúa alternativas para explotar la energía eólica en el Chaco.” October 20, 2025. https://www.lanacion.com.py/pais/2025/10/20/ande-evalua-alternativas-para-explotar-la-energia-eolica-en-el-chaco/.',
    annotation="La Nación: ANDE–EDF Chaco wind measurement cooperation. Supports ande_edf_chaco_wind_studies_2025.",
    evid_note="Opened La Nación Paraguay article 2026-10-02.",
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
    print(f"Cycle 172 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
