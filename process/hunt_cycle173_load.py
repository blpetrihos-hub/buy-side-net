#!/usr/bin/env python3
"""Cycle 173 hunt: shuffle_seed=20261173; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261173)): graphite, building_materials,
wind, fission_smr, bridges_roads, copper, nickel, port_ownership, other_renewables,
port_cranes, water, niobium, power_plants_grid, lithium, engineering_epc, rail,
balsa, solar.

Thin top-up (recomputed after shuffle pass): nickel / balsa / fission_smr —
fission filled (CNNC–IEN Centena visit); nickel/balsa dry this pass (catalog
dense; AIMA/WITS Ecuador balsa 2025 and Brazilian nickel DFC/Westwin already
logged). Graphite filled via INGEMMET Alto Chicama resource estimate (Peru).
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


# 1. graphite / other — INGEMMET Alto Chicama graphite resource estimate (Peru)
row_doc(
    "ingemmet_alto_chicama_graphite_2026",
    "resources",
    "graphite",
    "other",
    "INGEMMET — Alto Chicama basin graphite prospectivity (La Libertad)",
    "Peru",
    "27 Aug 2026 (ProActivo citing INGEMMET Boletín Serie B N.° 101): geological prospecting in the Alto Chicama basin (La Libertad) identifies five graphite-favorable segments (Baños Chimú; Huaranchal–Quiruvilca; Huamachuco–Sanagorán; Huamachuco–Angasmarca; Sarín); Huamachuco–Angasmarca estimated at 2.6 million metric tonnes of graphite resources. CapEx blank (state geological survey; no mine CapEx or FID).",
    "",
    "",
    "2026",
    "",
    "",
    "Alto Chicama basin / Huamachuco–Angasmarca segment, La Libertad — lat/lon blank (regional survey; no single mine pin).",
    "proactivo_ingemmet_graphite_20260827",
    "El Instituto Geológico, Minero y Metalúrgico (INGEMMET) identificó nuevas zonas con potencial de grafito en la cuenca del Alto Chicama, en la región La Libertad… Huamachuco–Angasmarca presenta los resultados más destacados, con una estimación de 2.6 millones de toneladas métricas de recursos de grafito.",
    "https://proactivo.com.pe/ingemmet-identifica-mas-de-2-6-millones-de-toneladas-de-recursos-de-grafito-en-la-libertad/",
    "Actor: INGEMMET (Peruvian state geological survey) — other. Opened ProActivo 27 Aug 2026 summarizing INGEMMET Boletín Serie B N.° 101. Thin graphite fill; Peru×graphite priority cell. Distinct from Brazilian Graphcoa/South Star catalog.",
    "hunt_cycle173",
    investment_type="other",
    evidence="documented",
    bib_type="press",
    chicago='ProActivo. “INGEMMET identifica más de 2.6 millones de toneladas de recursos de grafito en La Libertad.” August 27, 2026. https://proactivo.com.pe/ingemmet-identifica-mas-de-2-6-millones-de-toneladas-de-recursos-de-grafito-en-la-libertad/.',
    annotation="ProActivo: INGEMMET Alto Chicama 2.6 Mt graphite resources. Supports ingemmet_alto_chicama_graphite_2026.",
    evid_note="Opened ProActivo article 2026-10-02 (INGEMMET bulletin cited; repository bot-gated).",
)

# 2. building_materials / other — Votorantim Edealina mortar plant
row_doc(
    "votorantim_edealina_argamassa_2026",
    "infrastructure",
    "building_materials",
    "other",
    "Votorantim Cimentos — new mortar (argamassa) plant at Edealina (GO)",
    "Brazil",
    "19 Feb 2026: Votorantim Cimentos announces a new mortar plant at Edealina (Goiás) with 300,000 tpy capacity and inauguration targeted for mid-2027, within the company’s R$5bn 2024–2028 Brazil competitiveness program. CapEx blank on opened company page (no plant-specific reais figure; secretary-interview R$300m+ is secondary and unused).",
    "",
    "",
    "2026",
    "",
    "",
    "Edealina, Goiás — lat/lon blank pending verified worksite coords.",
    "votorantim_edealina_argamassa_20260219",
    "Dentro da nossa estratégia de aumento de produção e competitividade, também anunciamos a implantação de uma nova fábrica de argamassas em Edealina (GO). A nova operação terá capacidade de produção anual de 300 mil toneladas de argamassas, com inauguração prevista para meados de 2027.",
    "https://www.votorantimcimentos.com.br/noticia/avancamos-em-nosso-programa-de-investimentos-de-r-5-bilhoes-em-competitividade-estrutural/",
    "Actor: Votorantim Cimentos (Brazilian) — other. Opened company Portuguese release 19 Feb 2026. Distinct from sinoma_votorantim_z02_br_2024 (grind) and votorantim_xambioa_grind_2026 / votorantim_nobres_cuiaba_330m_2025.",
    "hunt_cycle173",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='Votorantim Cimentos. “Avançamos em nosso programa de investimentos de R$ 5 bilhões em competitividade estrutural.” February 19, 2026. https://www.votorantimcimentos.com.br/noticia/avancamos-em-nosso-programa-de-investimentos-de-r-5-bilhoes-em-competitividade-estrutural/.',
    annotation="Votorantim: Edealina 300 ktpy mortar plant mid-2027. Supports votorantim_edealina_argamassa_2026.",
    evid_note="Opened Votorantim Cimentos Portuguese company page 2026-10-02.",
)

# 3. wind / prc — Sinoma Wind Power Blade Camaçari factory (R$104m)
# ECB 2023-03-24: BRL/EUR 5.7298; USD/EUR 1.0745 → USD/BRL = 1.0745/5.7298 ≈ 0.18752836
row_doc(
    "sinoma_blade_camacari_104m_2023",
    "energy",
    "wind",
    "prc",
    "Sinoma Wind Power Blade (Brazil) — Camaçari wind-blade factory (ex-Tecsis)",
    "Brazil",
    "24–25 Mar 2023: Camaçari mayor signs protocol of intent with Sinoma Wind Power Blade (Brazil) LTDA for a wind-turbine blade factory on the former Tecsis site (Via Atlântica / BA-530); reported investment ~R$104 million; ~550 direct / 1,600 indirect jobs; first Sinoma blade plant outside China. USD 19,502,949.49 via ECB 2023-03-24 cross (USD/EUR 1.0745 ÷ BRL/EUR 5.7298).",
    "104000000",
    "2023-03-24",
    "2023",
    "",
    "",
    "Former Tecsis site, Via Atlântica (BA-530), Camaçari, Bahia — lat/lon blank pending verified plant pin.",
    "bahia_noticias_sinoma_camacari_20230325",
    "O prefeito de Camaçari, Elinaldo Araújo (União), assinou protocolo de intenções com a empresa chinesa Sinoma Wind Power Blade (Brazil) LTDA para instalação de uma fábrica de pás eólicas no município… A Sinoma investirá cerca de R$ 104 milhões para implantação da unidade… A unidade fabril será a primeira deste tipo a se instalar fora da China e funcionará na área da antiga empresa Tecsis, na Via Atlântica (BA-530).",
    "https://www.bahianoticias.com.br/municipios/noticia/33404-prefeitura-de-camacari-assina-protocolo-de-intencoes-com-a-sinoma-empresa-chinesa-vai-investir-rdollar-104-mi-em-fabrica-no-municipio",
    "Actor: Sinoma Wind Power Blade / CNBM family (PRC) — prc. Opened Bahia Notícias 25 Mar 2023. Distinct from goldwind_camacari_turbine_factory_2024 (nacelle/turbine). FX: ECB EXR D.USD.EUR and D.BRL.EUR 2023-03-24.",
    "hunt_cycle173",
    investment_type="greenfield",
    evidence="documented",
    currency="BRL",
    value_usd="19502949.49",
    fx_usd="0.1875283605",
    bib_type="press",
    chicago='Bahia Notícias. “Prefeitura de Camaçari assina protocolo de intenções com a Sinoma; empresa chinesa vai investir R$ 104 mi em fábrica no município.” March 25, 2023. https://www.bahianoticias.com.br/municipios/noticia/33404-prefeitura-de-camacari-assina-protocolo-de-intencoes-com-a-sinoma-empresa-chinesa-vai-investir-rdollar-104-mi-em-fabrica-no-municipio.',
    annotation="Bahia Notícias: Sinoma Camaçari blade plant R$104m protocol. Supports sinoma_blade_camacari_104m_2023.",
    evid_note="Opened Bahia Notícias municipal coverage 2026-10-02; FX from ECB EXR 2023-03-24.",
)

# 4. wind / us — GE Vernova / LM Wind Power Suape blade plant closure
row_doc(
    "ge_vernova_lm_suape_closure_2025",
    "energy",
    "wind",
    "us",
    "GE Vernova / LM Wind Power — Suape (PE) wind-blade plant closure",
    "Brazil",
    "11 Feb 2025: GE Vernova announces closure of LM Wind Power wind-blade factory at Suape (Pernambuco) citing Latin American demand decline; ~1,000 jobs affected; company statement quoted in local press. CapEx blank (closure / exit of manufacturing footprint; no disclosed exit cost).",
    "",
    "",
    "2025",
    "",
    "",
    "Suape industrial complex, Pernambuco — lat/lon blank (plant closure; site pin not required).",
    "movimento_economico_ge_suape_20250211",
    "Devido à queda na demanda no mercado latino-americano, nossa fábrica de pás eólicas LM Wind Power em Suape, Brasil, encerrará suas operações. Esta foi uma decisão difícil, e estamos totalmente comprometidos em apoiar nossos funcionários impactados e faremos tudo o que pudermos para fornecer a eles benefícios abrangentes de rescisão e transição.",
    "https://movimentoeconomico.com.br/geral/redacao/2025/02/11/ge-vernova-encerra-fabrica-de-pas-eolicas-em-suape-e-demite-1000/",
    "Actor: GE Vernova / LM Wind Power (U.S.) — us. Opened Movimento Econômico 11 Feb 2025 quoting company note. U.S. side-balance for wind. Distinct from ge_vernova_neuquen_aero_repair_2025 and goldwind_camacari_turbine_factory_2024.",
    "hunt_cycle173",
    investment_type="other",
    evidence="documented",
    bib_type="press",
    chicago='Movimento Econômico. “GE Vernova encerra fábrica de pás eólicas em Suape e demite 1.000.” February 11, 2025. https://movimentoeconomico.com.br/geral/redacao/2025/02/11/ge-vernova-encerra-fabrica-de-pas-eolicas-em-suape-e-demite-1000/.',
    annotation="Movimento Econômico: GE Vernova/LM Suape blade plant closure. Supports ge_vernova_lm_suape_closure_2025.",
    evid_note="Opened Movimento Econômico article quoting GE Vernova note 2026-10-02.",
)

# 5. fission_smr / prc — CNNC technical visit to IEN/CNEN (Centena follow-on)
row_doc(
    "cnnc_ien_cnen_centena_visit_202603",
    "energy",
    "fission_smr",
    "prc",
    "CNNC — technical visit to IEN/CNEN for Centena radioactive-waste repository cooperation",
    "Brazil",
    "16–19 Mar 2026 (CNEN/IEN 24 Mar 2026): China National Nuclear Corporation (CNNC) and subsidiaries CNOS/CEPC complete technical exchange at CNEN headquarters (Rio), CDTN (Minas Gerais), Eletronuclear (Angra), and IEN/CNEN (Argonauta reactor / LabRV) on radioactive-waste management under the Nov 2025 CNEN–CNNC MoU, aimed at enabling Centena (first Latin America low-/intermediate-level waste repository). CapEx blank (technical visit / MoU implementation; no disclosed Centena build cost).",
    "",
    "",
    "2026",
    "",
    "",
    "IEN/CNEN (Rio) / CDTN (MG) / Angra — lat/lon blank (multi-site technical mission).",
    "cnen_ien_cnnc_visit_20260324",
    "O Instituto de Engenharia Nuclear (IEN/CNEN) foi o local de encerramento da viagem de representantes da empresa China National Nuclear Corporation (CNNC) e de duas de suas subsidiárias (CNOS e a CEPC) ao Brasil, durante o intercâmbio realizada entre os dias 16 e 19 de março voltado ao compartilhamento de informações entre os países sobre a gestão de resíduos nucleares… A presença do corpo técnico da China National Nuclear Corporation no Brasil está prevista no Memorando de Entendimento (MoU) firmado pela empresa junto à CNEN, em novembro de 2025… perspectiva central a viabilização da construção do Centro Tecnológico Nuclear e Ambiental (Centena).",
    "https://www.gov.br/ien/pt-br/assuntos/noticias/delegacao-do-setor-nuclear-chines-realiza-visita-tecnica-ao-ien-cnen",
    "Actor: CNNC (PRC) with CNEN/IEN — prc. Opened gov.br IEN/CNEN notice 24 Mar 2026. Thin fission_smr top-up. Distinct from cnnc_cnen_centena_mou_2025 (MoU signing) and brazil_mme_cnnc_smr_dialogue_2026.",
    "hunt_cycle173",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='Instituto de Engenharia Nuclear / CNEN. “Delegação do setor nuclear chinês realiza visita técnica ao IEN/CNEN.” March 24, 2026. https://www.gov.br/ien/pt-br/assuntos/noticias/delegacao-do-setor-nuclear-chines-realiza-visita-tecnica-ao-ien-cnen.',
    annotation="IEN/CNEN: CNNC Centena technical visit Mar 2026. Supports cnnc_ien_cnen_centena_visit_202603.",
    evid_note="Opened gov.br IEN/CNEN Portuguese notice 2026-10-02.",
)

# 6. other_renewables / prc — CGN–Goldwind Tanque Novo BESS pilot
row_doc(
    "cgn_goldwind_tanque_novo_bess_2025",
    "energy",
    "other_renewables",
    "prc",
    "CGN Brasil + Goldwind — Tanque Novo wind-complex BESS pilot (745 kW / 1.49 MWh)",
    "Brazil",
    "Nov 2025 (Aranda Fotovolt 7 Nov 2025): CGN Brasil Energia and Goldwind sign cooperation contract for a battery energy storage (BESS) pilot at Complexo Eólico Tanque Novo (Bahia), 745 kW / 1.49 MWh, installed on one wind turbine to reduce curtailment and test grid flexibility. CapEx blank (pilot; no disclosed CapEx on opened page).",
    "",
    "",
    "2025",
    "",
    "",
    "Complexo Eólico Tanque Novo, Bahia — lat/lon blank pending turbine-05 / worksite pin.",
    "aranda_cgn_goldwind_bess_20251107",
    "A geradora CGN Brasil Energia e a fabricante chinesa de aerogeradores Goldwind assinaram um contrato de cooperação para a implantação de um projeto piloto de armazenamento de energia em baterias (BESS) no Complexo Eólico Tanque Novo, na Bahia. O sistema terá potência de 745 kW e capacidade de 1,49 MWh.",
    "https://www.arandanet.com.br/revista/fotovolt/noticia/11924-CGN-e-Goldwind-firmam-parceria-para-BESS-contra-curtailment.html",
    "Actor: CGN Brasil (PRC SOE affiliate) + Goldwind (PRC OEM) — prc. Opened Aranda Fotovolt 7 Nov 2025 (CGN Brazil company page timed out 504). Distinct from goldwind_camacari_turbine_factory_2024.",
    "hunt_cycle173",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="press",
    chicago='Aranda Editora / Fotovolt. “CGN e Goldwind firmam parceria para BESS contra curtailment.” November 7, 2025. https://www.arandanet.com.br/revista/fotovolt/noticia/11924-CGN-e-Goldwind-firmam-parceria-para-BESS-contra-curtailment.html.',
    annotation="Aranda: CGN–Goldwind Tanque Novo 745 kW/1.49 MWh BESS pilot. Supports cgn_goldwind_tanque_novo_bess_2025.",
    evid_note="Opened Aranda Fotovolt article 2026-10-02 (CGN Brazil primary 504).",
)

# 7. rail / us — U.S.–Argentina Andes-Atlantic Corridor launch
row_doc(
    "us_argentina_andes_atlantic_corridor_2026",
    "infrastructure",
    "rail",
    "us",
    "U.S. + Argentina — Andes-Atlantic Corridor (PGII) launch (freight rail / ports / pipelines)",
    "Argentina",
    "23 Sep 2026: U.S. Deputy Secretary of State Christopher Landau and Argentine Foreign Minister Pablo Quirno launch the Andes-Atlantic Corridor (first Western Hemisphere PGII corridor) to modernize rail, waterways, ports, pipelines, power, and digital links from northwest critical-minerals and Vaca Muerta to Atlantic/Hidrovía ports; EXIM/DFC/USTDA tools cited; freight-rail 50-year Belgrano/San Martín/Urquiza concession tenders highlighted. CapEx blank (corridor framework launch; project-level CapEx on separate rows where sourced).",
    "",
    "",
    "2026",
    "",
    "",
    "Argentina northwest–Vaca Muerta–Atlantic/Hidrovía corridor — lat/lon blank (national corridor; no single worksite).",
    "state_andes_atlantic_joint_20260923",
    "Today, U.S. Deputy Secretary of State Christopher Landau and Argentine Minister of Foreign Affairs Pablo Quirno launched the Andes-Atlantic Corridor, a joint initiative to strengthen and modernize infrastructure linking Argentina’s vital economic sectors to major Atlantic ports and Western markets… Mineral, oil, and gas exports will increase via U.S. and U.S.-backed investments in rail, waterways, ports, pipelines, and energy generation and transmission infrastructure.",
    "https://www.state.gov/releases/office-of-the-spokesman/2026/09/joint-statement-on-the-launch-of-the-andes-atlantic-corridor",
    "Actor: U.S. Government (State/EXIM/DFC/USTDA) with Argentina — us. Opened State Department joint statement 23 Sep 2026 (English fact sheet intermittently 403; Spanish translation also opened). Distinct from exim_argentina_build_future_7bn_2026 and pumpco_bonatti_argentina_lng_epc_2026. U.S. side-balance for rail.",
    "hunt_cycle173",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='U.S. Department of State, Office of the Spokesman. “Joint Statement on the Launch of the Andes-Atlantic Corridor.” September 23, 2026. https://www.state.gov/releases/office-of-the-spokesman/2026/09/joint-statement-on-the-launch-of-the-andes-atlantic-corridor.',
    annotation="State Dept: Andes-Atlantic Corridor launch with Argentina. Supports us_argentina_andes_atlantic_corridor_2026.",
    evid_note="Opened State Department joint statement 2026-10-02; Spanish fact sheet cross-checked.",
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
    print(f"Cycle 173 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
