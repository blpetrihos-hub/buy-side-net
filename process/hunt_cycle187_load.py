#!/usr/bin/env python3
"""Cycle 187 hunt: shuffle_seed=20261187; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261187)):
bridges_roads, building_materials, power_plants_grid, graphite, engineering_epc,
fission_smr, nickel, other_renewables, copper, lithium, balsa, water, port_cranes,
port_ownership, wind, niobium, solar, rail.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (Plantabal/AIMA dense; Centaurus/Atlantic Nickel dense;
Meitner Atucha / FIRST MoUs already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
≥1/3 U.S. hunt budget spent on DFC/EXIM/USTDA/AES/Atlas/Fluor/Caterpillar/Progress
Rail/Wabtec/NADBank/GE Vernova — catalog dense; no net-new U.S. CapEx row this cycle.
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


# 1. bridges_roads / allied — IDB Haiti Les Cayes + RN2 USD 69m
row_doc(
    "idb_haiti_les_cayes_rn2_69m_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "IDB — Les Cayes Airport + RN2 southern Haiti corridor grant",
    "Haiti",
    "24 Jun 2026: IDB Board approves up to USD 69 million non-reimbursable investment financing to modernize Les Cayes (Antoine Simon) Airport and rehabilitate priority RN2 pavement (11 km Étang de Miragoâne–Carrefour Moussignac). CapEx/financing face = USD 69m grant package. Coded bridges_roads for RN2 corridor component within integrated southern transport program. Distinct from wb_haiti_resilient_corridors_80m_2025.",
    "69000000",
    "2026-06-24",
    "2026",
    "18.27",
    "-73.55",
    "RN2 Étang de Miragoâne–Carrefour Moussignac / Les Cayes corridor, southern Haiti (program geography; approximate Miragoâne pin).",
    "haitilibre_idb_les_cayes_rn2_20260624",
    "On Wednesday, June 24, 2026, the Board of Executive Directors of the Inter-American Development Bank (IDB) approved up to $69 million in non-reimbursable investment financing to modernize Les Cayes Airport and improve the transportation network in southern Haiti. … The program will support the structural rehabilitation of 11 kilometers of pavement along the Étang de Miragoâne–Carrefour Moussignac section",
    "https://www.haitilibre.com/en/news-47842-haiti-investments-usd$69-for-the-modernization-of-les-cayes-airport-and-the-rehabilitation-of-rn2.html",
    "Actor: Inter-American Development Bank — allied multilateral. HaitiLibre English report of IDB Board approval (IDB project HA-J0014 / 6149/GR-HA). Haiti under-covered weight. Shuffle bridges_roads.",
    "hunt_cycle187",
    investment_type="financing",
    evidence="proxy",
    bib_type="press",
    chicago='HaitiLibre. “Haiti - Investments: USD$69 for the modernization of Les Cayes airport and the rehabilitation of RN2.” June 25, 2026. https://www.haitilibre.com/en/news-47842-haiti-investments-usd$69-for-the-modernization-of-les-cayes-airport-and-the-rehabilitation-of-rn2.html.',
    annotation="HaitiLibre: IDB USD 69m Les Cayes + RN2. Supports idb_haiti_les_cayes_rn2_69m_2026.",
    evid_note="Opened HaitiLibre English page 2026-10-04 summarizing IDB Board 24 Jun 2026 approval; UNVERIFIED proxy pending direct IDB press fetch (Cloudflare).",
)

# 2. bridges_roads / other — DNIT Porto Murtinho Bioceanic access R$472m
row_doc(
    "dnit_porto_murtinho_access_472m_brl_2025",
    "infrastructure",
    "bridges_roads",
    "other",
    "DNIT — BR-267 Porto Murtinho access to Bioceanic Bridge",
    "Brazil",
    "19 Sep 2025 DNIT: federal Novo PAC works for 13.1 km BR-267/MS access (km 678.1–691.2) to the international Bioceanic Bridge linking Porto Murtinho (MS) to Carmelo Peralta (PY) — six bridges + one viaduct; investment approximately R$ 472 million; completion targeted end-2026. CapEx = R$472m DNIT face (BRL stored without FX). Distinct from Itaipu-financed bridge row.",
    "472000000",
    "2025-09-19",
    "2025",
    "-21.70",
    "-57.88",
    "BR-267 km 678.1–691.2 access, Porto Murtinho, Mato Grosso do Sul, Brazil (DNIT geography).",
    "dnit_porto_murtinho_access_20250919",
    "O empreendimento conta com investimento do governo federal de aproximadamente R$ 472 milhões. … As obras contemplam a implantação de um trecho de 13,1 quilômetros de extensão, seis pontes e um viaduto, assegurando uma ligação mais segura à ponte que conecta Porto Murtinho (MS) a Carmelo Peralta (PY).",
    "https://www.gov.br/dnit/pt-br/assuntos/noticias/em-porto-murtinho-ms-avancam-as-obras-do-acesso-a-ponte-internacional-bioceanica-na-br-267",
    "Actor: DNIT (Brazil federal) — other. Official Portuguese DNIT news. Shuffle bridges_roads.",
    "hunt_cycle187",
    investment_type="greenfield",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Departamento Nacional de Infraestrutura de Transportes (DNIT). “Em Porto Murtinho (MS), avançam as obras do acesso à Ponte Internacional Bioceânica, na BR-267.” September 19, 2025. https://www.gov.br/dnit/pt-br/assuntos/noticias/em-porto-murtinho-ms-avancam-as-obras-do-acesso-a-ponte-internacional-bioceanica-na-br-267.',
    annotation="DNIT: BR-267 Bioceanic access ~R$472m. Supports dnit_porto_murtinho_access_472m_brl_2025.",
    evid_note="Opened DNIT Portuguese news page 2026-10-04.",
)

# 3. bridges_roads / allied — MOPC PY15 Tramo 3 Fonplata USD 354.2m
row_doc(
    "mopc_py15_fonplata_354m_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "MOPC Paraguay — PY15 Bioceanic Tramo 3 (Fonplata)",
    "Paraguay",
    "24 Jul 2026 MOPC: Corredor Vial Bioceánico Tramo 3 on ruta PY15 — four lots totaling ~219.5 km between Mariscal Estigarribia and Pozo Hondo plus accesses; estimated investment USD 354.2 million financed by Fonplata (Banco de Desarrollo). CapEx = USD 354.2m MOPC face. Distinct from Itaipu bridge and DNIT Brazilian access rows.",
    "354200000",
    "2026-07-24",
    "2026",
    "-22.03",
    "-60.57",
    "PY15 Mariscal Estigarribia–Pozo Hondo corridor, Boquerón, Paraguay (MOPC geography; approximate Mariscal Estigarribia pin).",
    "mopc_py15_fonplata_20260724",
    "La inversión estimada en esta carretera asciende a USD 354,2 millones, con financiamiento del Banco de Desarrollo (Fonplata). … Todas estas obras forman parte del tercer tramo del Corredor Vial Bioceánico, adjudicado en 4 lotes que totalizan 219,5 kilómetros entre Mariscal Estigarribia y Pozo Hondo, además de sus accesos.",
    "https://mopc.gov.py/corredor-bioceanico-gana-terreno-en-el-chaco-con-11-km-continuos-de-base-asfaltica/",
    "Actor: MOPC Paraguay with Fonplata multilateral financing — allied (Fonplata). Official Spanish MOPC page. Shuffle bridges_roads.",
    "hunt_cycle187",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='Ministerio de Obras Públicas y Comunicaciones (MOPC). “Corredor Bioceánico gana terreno en el Chaco con 11 km continuos de base asfáltica.” July 24, 2026. https://mopc.gov.py/corredor-bioceanico-gana-terreno-en-el-chaco-con-11-km-continuos-de-base-asfaltica/.',
    annotation="MOPC: PY15 Tramo 3 USD 354.2m Fonplata. Supports mopc_py15_fonplata_354m_2026.",
    evid_note="Opened MOPC Spanish news page 2026-10-04.",
)

# 4. bridges_roads / other — Itaipu Bioceanic Bridge ~USD 103m
row_doc(
    "itaipu_ponte_bioceanica_103m_2026",
    "infrastructure",
    "bridges_roads",
    "other",
    "Itaipu Binacional (PY margin) — Ponte Bioceânica Porto Murtinho–Carmelo Peralta",
    "Paraguay",
    "16 Jul 2026 Rota Bioceânica / Itaipu Binacional disclosure: 1,294 m cable-stayed international bridge over Río Paraguay linking Carmelo Peralta (PY) and Porto Murtinho (BR); investment G 684,615,904,566 ≈ USD 103 million financed by Paraguayan margin of Itaipu; MOPC executor; PYBRA consortium. CapEx = USD 103m stated equivalent. Distinct from DNIT access and PY15 pavement rows.",
    "103000000",
    "2026-07-16",
    "2026",
    "-21.70",
    "-57.89",
    "Ponte Bioceânica over Río Paraguay, Carmelo Peralta (PY)–Porto Murtinho (BR) (Itaipu/MOPC geography).",
    "rota_bioceanica_itaipu_ponte_20260716",
    "A construção da Ponte Bioceânica representa um investimento de G 684.615.904.566, equivalente a aproximadamente USD 103 milhões, financiado com recursos do lado paraguaio do ITAIPU. O Ministério de Obras Públicas e Comunicações (MOPC) atua como órgão executor.",
    "https://rotabioceanica.com.br/2026/07/momentos-finais-da-conexao-fisica-da-ponte-bioceanica-financiada-pela-itaipu/",
    "Actor: Itaipu Binacional (Paraguayan margin) / MOPC — other. Rota Bioceânica Portuguese page citing Itaipu Binacional source. Shuffle bridges_roads.",
    "hunt_cycle187",
    investment_type="greenfield",
    evidence="documented",
    bib_type="press",
    chicago='Rota Bioceânica. “Momentos finais da conexão física da Ponte Bioceânica financiada pela ITAIPU.” July 16, 2026. https://rotabioceanica.com.br/2026/07/momentos-finais-da-conexao-fisica-da-ponte-bioceanica-financiada-pela-itaipu/.',
    annotation="Rota Bioceânica/Itaipu: bridge ~USD 103m. Supports itaipu_ponte_bioceanica_103m_2026.",
    evid_note="Opened Rota Bioceânica Portuguese page citing Itaipu Binacional 2026-10-04.",
)

# 5. power_plants_grid / allied — ISA Energia Brasil R&M R$370m 1T26
row_doc(
    "isa_energia_rm_370m_brl_1t26",
    "energy",
    "power_plants_grid",
    "allied",
    "ISA Energia Brasil — Q1 2026 Reforços e Melhorias transmission CapEx",
    "Brazil",
    "23 Jun 2026 ISA Energia Brasil: invested R$ 370 million in Reforços e Melhorias (R&M) transmission projects in 1Q26 (+20.9% YoY) — >250 equipment items (transformers, breakers, disconnectors, protection, lines); authorized R&M portfolio ~R$ 7.2bn at end-1T26. CapEx = R$370m executed face (BRL stored without FX). ISA (Colombia) controlling shareholder — allied. Distinct from isa_energia_serra_dourada_3p2bn_2025 greenfield.",
    "370000000",
    "2026-06-23",
    "2026",
    "-23.55",
    "-46.63",
    "ISA Energia Brasil transmission network (São Paulo-centric); approximate São Paulo pin — multi-asset R&M program.",
    "isa_energia_rm_370m_20260623",
    "A ISA ENERGIA BRASIL … investiu R$ 370 milhões em projetos de Reforços e Melhorias (R&M) no primeiro trimestre de 2026, valor 20,9% superior ao registrado no mesmo período do ano anterior, voltado para a implementação de mais de 250 equipamentos para ampliar a capacidade e confiabilidade do sistema elétrico nacional.",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-370-milhoes-em-reforcos-e-melhorias-na-rede-de-transmissao-nacional/",
    "Actor: ISA Energia Brasil (ISA Colombia group) — allied. Company Portuguese press. Shuffle power_plants_grid.",
    "hunt_cycle187",
    investment_type="capex",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ISA Energia Brasil. “ISA ENERGIA BRASIL investe R$ 370 milhões em Reforços e Melhorias na rede de transmissão nacional.” June 23, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-370-milhoes-em-reforcos-e-melhorias-na-rede-de-transmissao-nacional/.',
    annotation="ISA Energia Brasil: 1T26 R&M CapEx R$370m. Supports isa_energia_rm_370m_brl_1t26.",
    evid_note="Opened ISA Energia Brasil Portuguese company press 2026-10-04.",
)

# 6. power_plants_grid / other — Copel 2026 CapEx plan R$3.0213bn
row_doc(
    "copel_capex_2026_plan_3021m_brl",
    "energy",
    "power_plants_grid",
    "other",
    "Copel — Board-approved 2026 CapEx program (R$3.021bn)",
    "Brazil",
    "19 Nov 2025 Copel Fato Relevante 15/25: Board approves CapEx program R$17.8 billion for 2026–2030; 2026 planned CapEx approximately R$3.0213 billion (Distribuição R$1,942.80m; GeT R$971.6m of which transmissão R$449.8m / geração R$441.5m; holding/other remainder). CapEx = R$3,021.3m 2026 plan face (BRL stored without FX). Brazilian utility — other. Coded power_plants_grid for generation/transmission-heavy utility CapEx plan.",
    "3021300000",
    "2025-11-19",
    "2026",
    "-25.43",
    "-49.27",
    "Copel Paraná concession / GeT asset base — lat/lon blank-ish; approximate Curitiba HQ pin.",
    "copel_fr_15_25_capex_20251119",
    "Para 2026, o plano de investimento prevê um Capex de, aproximadamente, R$ 3,0 bilhões … Total Geral 3.021,3",
    "https://api.mziq.com/mzfilemanager/v2/d/16a31b1b-5ecd-4214-a2e0-308a2393e330/b4fe8c81-c5ea-c309-59d7-a14974bd35ad?origin=1",
    "Actor: Companhia Paranaense de Energia (Copel) — other. Official Fato Relevante PDF. Shuffle power_plants_grid.",
    "hunt_cycle187",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Companhia Paranaense de Energia (Copel). “Fato Relevante | 15/25 — CAPEX de R$ 17,8 bilhões para os próximos 5 anos.” November 19, 2025. https://api.mziq.com/mzfilemanager/v2/d/16a31b1b-5ecd-4214-a2e0-308a2393e330/b4fe8c81-c5ea-c309-59d7-a14974bd35ad?origin=1.',
    annotation="Copel: 2026 CapEx plan R$3,021.3m. Supports copel_capex_2026_plan_3021m_brl.",
    evid_note="Opened Copel Fato Relevante 15/25 PDF 2026-10-04.",
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
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle187 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
