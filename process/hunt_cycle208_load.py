#!/usr/bin/env python3
"""Cycle 208 hunt: shuffle_seed=20261208; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261208).shuffle):
port_ownership, nickel, solar, rail, water, niobium, building_materials,
bridges_roads, lithium, wind, balsa, other_renewables, graphite, fission_smr,
copper, port_cranes, engineering_epc, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Argentina/DFC Patria/
EnergyX/Nextracker/Array/Wabtec/Progress Rail/SSA/Glenfarne/Bechtel/Fluence/
USTDA/GE Vernova sweeps (0 new U.S. rows — catalog dense post-Glenfarne).
PRC equal-budget: CapEx-fill upgrade CHEC Panama Fourth Bridge via MOP adenda;
Sinomach CAMCE Punta Huete toll road already logged as camce_punta_huete_road
(USD 71.96m). Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km;
CCECC Nicaragua rail; CHEC San Carlos central.
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


# 1. port_ownership / other — PC Terminals Port Royal Chinourette Phase 1 USD 60m (Haiti)
row_doc(
    "pc_terminals_port_royal_haiti_60m_2025",
    "infrastructure",
    "port_ownership",
    "other",
    "PC Terminals S.A. — Port Royal commercial port Phase 1 (Chinourette / Terrier Rouge)",
    "Haiti",
    "6 Sep 2025: PC Terminals S.A. and Autorité Portuaire Nationale (APN) lay foundation stone for Port Royal commercial port at Chinourette (communal section of Terrier Rouge, Nord-Est; bordering Fort Liberté). Full multi-phase program estimated USD 600 million over >1,000 ha; Phase 1 (Port Royal) financed by foreign and domestic investors at USD 60 million. APN DG targets Phase 1 inauguration in ~2 years. CapEx face = Phase 1 USD 60m (not full USD 600m program).",
    "60000000",
    "2025-09-06",
    "2025",
    "19.64",
    "-71.96",
    "Chinourette / Terrier Rouge, Nord-Est Department, Haiti (HaitiLibre geography; approximate Terrier Rouge pin).",
    "haitilibre_port_royal_terrier_rouge_20250909",
    "The total cost of this project, which will cover an area of over 1,000 hectares, is estimated at $600 million. The first phase of the project (Port Royal) will be financed by foreign and domestic investors to the tune of $60 million. … Construction of the \"Port Royal\" commercial port, named in tribute to King Henri Christophe, to relieve congestion at the port of Cap-Haïtien",
    "https://www.haitilibre.com/en/news-45735-haiti-flash-launch-of-a-$600m-port-project-in-terrier-rouge.html",
    "Actor: PC Terminals S.A. (Haitian private; Chairman Patrick Béliard) with APN PPP — other. HaitiLibre English primary 9 Sep 2025 (ceremony 6 Sep). CapEx = Phase 1 USD 60m face. Haiti under-covered weight. Shuffle port_ownership.",
    "hunt_cycle208",
    investment_type="greenfield",
    evidence="documented",
    currency="USD",
    value_usd="60000000",
    fx_usd="1",
    bib_type="press",
    chicago='HaitiLibre. “Haiti - FLASH : Launch of a $600M port project in Terrier Rouge.” September 9, 2025. https://www.haitilibre.com/en/news-45735-haiti-flash-launch-of-a-$600m-port-project-in-terrier-rouge.html.',
    annotation="PC Terminals Port Royal Chinourette Phase 1 USD 60m. Supports pc_terminals_port_royal_haiti_60m_2025.",
    evid_note="Opened HaitiLibre English primary 2026-10-04; Phase 1 USD 60m / full program USD 600m / PC Terminals+APN / Chinourette Terrier Rouge / 6 Sep 2025 foundation stone confirmed.",
)

# 2. rail / allied — Alstom Salvador metro 10 four-car trains R$632.7m (homologation; contract pending)
row_doc(
    "alstom_salvador_metro_10trains_632p7m_2026",
    "infrastructure",
    "rail",
    "allied",
    "Consórcio Grupo Alstom — 10 four-car metro trains (Salvador–Lauro de Freitas Lines 1–2)",
    "Brazil",
    "21–22 Sep 2026: CTB homologates Consórcio Grupo Alstom (Alstom Brasil Energia e Transporte Ltda. + Alstom Transport S.A.) as supplier of 10 four-car trains for Sistema Metroviário de Salvador e Lauro de Freitas Lines 1–2 at R$632,719,519.37 (lowest price; CRRC Changchun bid R$636.7m). Published in Diário Oficial 22 Sep 2026. Prior 2025 CRRC award (R$490.4m) was revoked; this is the re-tender. Contract formalization still pending documentation review / possible appeals — CapEx face from homologation proposal. Distinct from crrc_salvador_metro_2026 (revoked prior selection) and alstom_sp_line6_trains_2025.",
    "632719519.37",
    "",
    "2026",
    "-12.97",
    "-38.51",
    "Salvador–Lauro de Freitas metro Lines 1–2, Bahia (CTB/G1 geography; approximate Salvador pin).",
    "g1_alstom_salvador_metro_20260922",
    "A Companhia de Transportes do Estado da Bahia (CTB) divulgou que o Consórcio Grupo Alstom venceu uma licitação para o fornecimento de 10 novos trens para o Sistema Metroviário de Salvador e Lauro de Freitas (SMSL). … Segundo a CTB, a escolha foi tomada com base na proposta de menor preço. Serão investidos R$ 632.719.519,37 para a aquisição dos veículos.",
    "https://g1.globo.com/ba/bahia/noticia/2026/09/22/empresa-vence-licitacao-para-fornecimento-de-trens-para-metro-de-salvador-e-lauro-de-freitas.ghtml",
    "Actor: Alstom (France) Consórcio Grupo Alstom — allied. UNVERIFIED proxy: G1 22 Sep 2026 citing CTB Diário Oficial homologation; BNews notes contract formalization still pending documentation review. Value stored as BRL (Fed H.10 FX sheet unreachable this pass — USD blank). Distinct from revoked crrc_salvador_metro_2026.",
    "hunt_cycle208",
    investment_type="rolling_stock",
    evidence="proxy",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='g1 BA. “Consórcio vence licitação para compra de trens em Salvador e Lauro.” September 22, 2026. https://g1.globo.com/ba/bahia/noticia/2026/09/22/empresa-vence-licitacao-para-fornecimento-de-trens-para-metro-de-salvador-e-lauro-de-freitas.ghtml.',
    annotation="Alstom Salvador metro 10 trains R$632.7m CTB homologation. Supports alstom_salvador_metro_10trains_632p7m_2026.",
    evid_note="Opened G1 BA 22 Sep 2026 citing CTB DOE; R$632,719,519.37 / 10 four-car trains / Consórcio Grupo Alstom confirmed. Diário do Transporte corroborates CRRC rival bid and pending contract formalization. FX blank.",
)

# 3. bridges_roads / allied — Acciona Roberto Marinho–Imigrantes road link R$2.099bn
row_doc(
    "acciona_roberto_marinho_sp_2p099bn_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "ACCIONA — Avenida Roberto Marinho–Rodovia dos Imigrantes road link + linear park (São Paulo)",
    "Brazil",
    "15 Jan 2026 ACCIONA: City of São Paulo awards ACCIONA the contract to build the road section linking Avenida Jornalista Roberto Marinho with Rodovia dos Imigrantes — R$2.099 billion (€334 million). Scope: three new lanes each carriageway over 4.7 km, three viaducts, two tunnels, cycle lane, drainage diversion, and landscaped park. Distinct from acciona_sp_line6_epc_2025 (metro Line 6) and mota_engil_santos_guaruja_6p8bn_2026.",
    "2099000000",
    "",
    "2026",
    "-23.65",
    "-46.65",
    "Avenida Roberto Marinho / Rodovia dos Imigrantes corridor, southern São Paulo (company geography; approximate southern-zone pin).",
    "acciona_roberto_marinho_20260115",
    "The City Council of São Paulo (Brazil) has awarded ACCIONA the contract to build the road section linking Avenida Jornalista Roberto Marinho with Rodovia dos Imigrantes … The contract, valued at R$2.099 billion (€334 million), includes the construction of three new lanes in each carriageway along a 4.7 kilometer stretch, incorporating three viaducts and two tunnels, as well as a cycle lane.",
    "https://www.acciona.com/updates/news/acciona-awarded-road-link-southern-sao-paulo",
    "Actor: ACCIONA (Spain) — allied. Company English primary 15 Jan 2026. CapEx face = BRL 2.099bn; USD blank (Fed H.10 unreachable this pass; company also cites €334m). Shuffle bridges_roads.",
    "hunt_cycle208",
    investment_type="epc",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ACCIONA. “ACCIONA awarded road link project in southern São Paulo.” January 15, 2026. https://www.acciona.com/updates/news/acciona-awarded-road-link-southern-sao-paulo.',
    annotation="Acciona Roberto Marinho–Imigrantes R$2.099bn. Supports acciona_roberto_marinho_sp_2p099bn_2026.",
    evid_note="Opened ACCIONA English company primary 2026-10-04; R$2.099bn / €334m / 4.7 km / 3 viaducts / 2 tunnels confirmed.",
)

# 4. bridges_roads / prc — CapEx fill: CHEC/CCCC Panama Fourth Bridge MOP adenda USD 1,372.1m
row_doc(
    "chec_fourth_bridge_panama",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Harbour Engineering Company (CHEC) / CCCC — Fourth Bridge over the Panama Canal (CPCP)",
    "Panama",
    "30 Mar 2023 MOP: Adenda to contract AL-1-27-18 with Consorcio Panamá Cuarto Puente (CCCC + CHEC) sets net design+construction value at USD 1,372.1 million after separating Metro Line 3 scope; financing structure ~USD 716.5m (Santander/Mizuho/Banistmo) with disbursements starting 2026. Three-span cable-stayed main bridge 965 m (240+485+240 m). CapEx face filled from MOP Spanish primary (was blank on prior CHEC Americas page-only row).",
    "1372100000",
    "2023-03-30",
    "2023",
    "8.95",
    "-79.57",
    "Fourth Bridge over Panama Canal, Panama City area (MOP/CHEC geography).",
    "mop_panama_cuarto_puente_adenda_20230330",
    "La adenda incorpora modificaciones al contrato original para que el consorcio continúe con el diseño y construcción del proyecto por un valor neto de $1,372.1 millones, luego de separar su construcción de la Tercera Línea del Metro de Panamá. … La adenda incorpora también, la estructura de financiamiento del proyecto presentada por los bancos Santander, Mizuho y Banistmo por un costo aproximado de $716.5 millones … con un cronograma de pagos cuyos desembolsos inician en el año 2026",
    "http://www.mop.gob.pa/index.php/prensa/sala-de-prensa/item/2885-mop-y-consorcio-panama-cuarto-puente-cpcp-firman-adenda-que-permite-continuar-con-la-ejecucion-del-proyecto-cuarto-puente-sobre-el-canal",
    "Actor: CHEC + CCCC (PRC SOEs) via Consorcio Panamá Cuarto Puente — prc. CapEx-fill upgrade: MOP Spanish adenda primary USD 1,372.1m net construction (was blank). Year = adenda date 2023; financing disbursements from 2026. Distinct from ohla_panama_panamericana_este_2025.",
    "hunt_cycle208",
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd="1372100000",
    fx_usd="1",
    bib_type="government",
    chicago='Ministerio de Obras Públicas (Panamá). “MOP y Consorcio Panamá Cuarto Puente (CPCP) firman adenda que permite continuar con la ejecución del proyecto Cuarto Puente sobre el Canal.” March 30, 2023. http://www.mop.gob.pa/index.php/prensa/sala-de-prensa/item/2885-mop-y-consorcio-panama-cuarto-puente-cpcp-firman-adenda-que-permite-continuar-con-la-ejecucion-del-proyecto-cuarto-puente-sobre-el-canal.',
    annotation="MOP Panama Fourth Bridge adenda USD 1,372.1m. Supports chec_fourth_bridge_panama CapEx fill.",
    evid_note="Opened MOP Spanish press 2026-10-04; USD 1,372.1m net design+construction / Santander-Mizuho-Banistmo ~USD 716.5m financing / disbursements from 2026 confirmed. CapEx-fill upgrade of prior blank-value CHEC Americas row.",
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
    updated = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
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
    print(f"cycle208 added {len(added)}: {added}")
    print(f"cycle208 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
