#!/usr/bin/env python3
"""Cycle 200 hunt: shuffle_seed=20261200; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261200).shuffle):
bridges_roads, other_renewables, nickel, copper, engineering_epc, balsa,
graphite, solar, niobium, wind, fission_smr, port_cranes, rail,
power_plants_grid, building_materials, port_ownership, water, lithium.

Thin top-up (recomputed): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on AWS Huechuraba CapEx, EXIM/DFC/AES/Freeport/
Wabtec/Equinix sweeps — 1 new U.S. row (AWS Huechuraba).
PRC equal-budget misses: GATE/SPIC/Goldwind/MMG/BYD BESS CapEx already
logged; holdovers unsigned.
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


# 1. bridges_roads / other — Azevedo & Travassos Rota Mogiana R$9.4bn
row_doc(
    "azevedo_rota_mogiana_9p4bn_brl_2026",
    "infrastructure",
    "bridges_roads",
    "other",
    "Consórcio Rota Mogiana (Azevedo & Travassos / Quimassa) — SP highway concession",
    "Brazil",
    "27 Feb 2026 Azevedo & Travassos: consortia wins 30-year Rota Mogiana concession for 520 km of São Paulo state highways (Campinas–Ribeirão Preto / MG border corridor); estimated CapEx R$ 9.4 billion for expansion, modernization and maintenance; winning fixed outorga R$ 1.084 billion. CapEx = R$9.4bn.",
    "9400000000",
    "2026-02-27",
    "2026",
    "-22.12",
    "-47.00",
    "Pinned to Campinas / Mogiana corridor start (company geography; multi-municipality — approximate municipal pin).",
    "azevedo_rota_mogiana_20260227",
    "O projeto prevê que 520 quilômetros de rodovias estaduais passem à iniciativa privada por 30 anos. A estimativa é de R$ 9,4 bilhões em investimentos para ampliar, modernizar e manter as estradas.",
    "https://azevedotravassos.com.br/noticias/2026/02/27/azevedo-travassos-investimentos-vence-leilao-da-concessao-rota-mogiana-com-520-km-de-rodovias/",
    "Actor: Azevedo & Travassos Investimentos (Brazilian) + Quimassa — other. Company Portuguese primary. CapEx = R$9.4bn (BRL stored without FX). Shuffle bridges_roads.",
    "hunt_cycle200",
    investment_type="concession_capex",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Azevedo & Travassos S.A. “Azevedo & Travassos Investimentos vence leilão da concessão Rota Mogiana, com 520 km de rodovias.” February 27, 2026. https://azevedotravassos.com.br/noticias/2026/02/27/azevedo-travassos-investimentos-vence-leilao-da-concessao-rota-mogiana-com-520-km-de-rodovias/.',
    annotation="Rota Mogiana: R$9.4bn CapEx. Supports azevedo_rota_mogiana_9p4bn_brl_2026.",
    evid_note="Opened Azevedo & Travassos Portuguese company primary 2026-10-04; R$9.4bn confirmed.",
)

# 2. bridges_roads / other — COVIPERÚ Nuevo Puente Asia USD 50.1m
row_doc(
    "coviperu_puente_asia_50p1m_2026",
    "infrastructure",
    "bridges_roads",
    "other",
    "COVIPERÚ (H&H group) — Nuevo Puente Asia 1 + Chilca/San Andrés (Red Vial 6)",
    "Peru",
    "8 Apr 2026 OSITRAN: Concesionaria Vial del Perú S.A. (Red Vial 6 Puente Pucusana–Cerro Azul–Ica) reports principal 2026 investment of USD 50.1 million for construction of Nuevo Puente Asia 1 and bridges at Chilca and San Andrés interchanges. CapEx = USD 50.1m. Actor historically H&H Ecuador majority — other.",
    "50100000",
    "2026-04-08",
    "2026",
    "-12.78",
    "-76.57",
    "Pinned to Asia / Panamericana Sur Red Vial 6 corridor (OSITRAN geography; approximate municipal pin).",
    "ositran_carreteras_2026_0408",
    "Empresa Concesionaria Vial del Perú S. A. a cargo de la Red Vial 6: Puente Pucusana-Cerro Azul-Ica informó que su principal inversión de USD 50,1 millones será para la construcción del Nuevo Puente Asia 1 y de puentes de los intercambios viales Chilca y San Andrés.",
    "https://www.gob.pe/institucion/ositran/noticias/1375740-principales-inversiones-en-carreteras-proyectan-mas-de-usd-400-millones-en-el-2026",
    "Actor: COVIPERÚ / H&H group (Ecuadorian majority historically) — other. OSITRAN Spanish government primary. CapEx = USD 50.1m. Shuffle bridges_roads.",
    "hunt_cycle200",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="50100000",
    fx_usd="1",
    bib_type="government",
    chicago='Organismo Supervisor de la Inversión en Infraestructura de Transporte (OSITRAN). “Principales inversiones en carreteras proyectan más de USD 400 millones en el 2026.” April 8, 2026. https://www.gob.pe/institucion/ositran/noticias/1375740-principales-inversiones-en-carreteras-proyectan-mas-de-usd-400-millones-en-el-2026.',
    annotation="COVIPERÚ Puente Asia: USD 50.1m. Supports coviperu_puente_asia_50p1m_2026.",
    evid_note="Opened OSITRAN Spanish government primary 2026-10-04; USD 50.1m confirmed.",
)

# 3. other_renewables / other — Copahue geothermal USD 46.1m (ADI-NQN via PiensaGeotermia)
row_doc(
    "adi_nqn_copahue_geothermal_46p1m_2026",
    "energy",
    "other_renewables",
    "other",
    "ADI-NQN SEP — Copahue geothermal initial 10 MW module (Neuquén)",
    "Argentina",
    "5 Mar 2026 PiensaGeotermia (direct ADI-NQN correspondence after GEOLAC 2026): Copahue geothermal initial modular 10 MW stage CapEx estimated USD 46.1 million (drilling USD 13.65m; plant USD 28.25m; 33 kV line USD 4.17m; social USD 16k); expandable to 30 MW; EIA for drilling still pending. CapEx = USD 46.1m. UNVERIFIED proxy summarizing ADI-NQN figures.",
    "46100000",
    "2026-03-05",
    "2026",
    "-37.85",
    "-71.10",
    "Las Mellizas de Copahue / NE flank Copahue volcano, Neuquén (ADI-NQN geography).",
    "piensageotermia_copahue_20260305",
    "La inversión total estimada para la etapa inicial de 10 MW es de USD 46,1 millones.",
    "https://www.piensageotermia.com/proyecto-geotermico-copahue-adi-nqn-describe-avances-del-desarrollo-geotermico-mas-avanzado-de-argentina/",
    "Actor: ADI-NQN SEP (Neuquén provincial investment agency) — other. UNVERIFIED proxy: PiensaGeotermia citing direct ADI-NQN correspondence. CapEx = USD 46.1m. Shuffle other_renewables.",
    "hunt_cycle200",
    investment_type="greenfield_generation",
    evidence="proxy",
    currency="USD",
    value_usd="46100000",
    fx_usd="1",
    bib_type="press",
    chicago='Llamosa Ardila, Oscar. “Proyecto Geotérmico Copahue: ADI-NQN describe avances del desarrollo geotérmico más avanzado de Argentina.” PiensaGeotermia, March 5, 2026. https://www.piensageotermia.com/proyecto-geotermico-copahue-adi-nqn-describe-avances-del-desarrollo-geotermico-mas-avanzado-de-argentina/.',
    annotation="Copahue: USD 46.1m initial CapEx. Supports adi_nqn_copahue_geothermal_46p1m_2026.",
    evid_note="Opened PiensaGeotermia Spanish press 2026-10-04; USD 46.1m cited from ADI-NQN; UNVERIFIED proxy.",
)

# 4. other_renewables / other — WEG Itajaí BESS factory R$280m
row_doc(
    "weg_itajai_bess_280m_brl_2026",
    "energy",
    "other_renewables",
    "other",
    "WEG — Itajaí BESS manufacturing plant (Santa Catarina)",
    "Brazil",
    "4 Feb 2026 WEG: announces new dedicated BESS manufacturing plant in Itajaí/SC financed with R$ 280 million from BNDES Mais Inovação (Finep strategic-minerals call); completion targeted 2H 2027; capacity up to 2 GWh/year (~400 × 5 MWh systems). CapEx financing face = R$280m.",
    "280000000",
    "2026-02-04",
    "2026",
    "-26.91",
    "-48.66",
    "Itajaí, Santa Catarina (WEG company geography).",
    "weg_itajai_bess_20260204",
    "Para viabilizar o projeto, a WEG contou com financiamento de R$ 280 milhões do programa BNDES Mais Inovação, aprovado no âmbito da chamada pública voltada à transformação de minerais estratégicos para transição energética e descarbonização, realizada em parceria com a Finep.",
    "https://www.weg.net/institutional/BR/pt/news/resultados-e-investimentos/weg-anuncia-nova-fabrica-de-sistemas-de-armazenamento-de-energia-em-baterias-bess-em-itajai-sc",
    "Actor: WEG S.A. (Brazilian) — other. Company Portuguese primary. CapEx financing = R$280m (BRL stored without FX). Shuffle other_renewables.",
    "hunt_cycle200",
    investment_type="manufacturing_capex",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='WEG. “WEG anuncia nova fábrica de sistemas de armazenamento de energia em baterias (BESS) em Itajaí/SC.” February 4, 2026. https://www.weg.net/institutional/BR/pt/news/resultados-e-investimentos/weg-anuncia-nova-fabrica-de-sistemas-de-armazenamento-de-energia-em-baterias-bess-em-itajai-sc.',
    annotation="WEG Itajaí BESS: R$280m. Supports weg_itajai_bess_280m_brl_2026.",
    evid_note="Opened WEG Portuguese company primary 2026-10-04; R$280m BNDES financing confirmed.",
)

# 5. engineering_epc / us — AWS Huechuraba data center USD 205m
row_doc(
    "aws_huechuraba_205m_chile_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Amazon Data Services Chile / AWS — Huechuraba data center CapEx",
    "Chile",
    "9 Apr 2026 Segundo Tribunal Ambiental: confirms RCA for Centro de Almacenamiento de Datos Huechuraba (Servicios Amazon Data Services Chile SpA); estimated investment USD 205,000,000; 10.9 ha; 21,350.07 m² construction; 30-year useful life; Américo Vespucio N° 1055, Huechuraba. CapEx = USD 205m. Distinct from aws_chile_region_4bn_2025 multi-AZ regional floor.",
    "205000000",
    "2026-04-09",
    "2026",
    "-33.36",
    "-70.68",
    "Huechuraba, Santiago RM / Américo Vespucio 1055 (Tribunal Ambiental geography).",
    "tribunal_ambiental_huechuraba_20260409",
    "El proyecto de Amazon consiste en la construcción y operación de un centro de almacenamiento de datos destinado a prestar servicios tecnológicos de almacenamiento y gestión de datos a usuarios locales. Considera una vida útil de 30 años, una inversión estimada de USD $205.000.000 y se emplazaría en una superficie de 10,9 hectáreas, con una construcción de 21.350,07 m², ubicada en caletera de Américo Vespucio N° 1055, comuna de Huechuraba.",
    "https://tribunalambiental.cl/tribunal-confirmo-la-aprobacion-del-proyecto-de-data-center-de-amazon-en-huechuraba-observaciones-ciudadanas-fueron-debidamente-consideradas/",
    "Actor: Amazon / AWS (U.S.) — us. Chilean Segundo Tribunal Ambiental Spanish primary. CapEx = USD 205m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle200",
    investment_type="greenfield_facility",
    evidence="documented",
    currency="USD",
    value_usd="205000000",
    fx_usd="1",
    bib_type="government",
    chicago='Segundo Tribunal Ambiental (Chile). “Tribunal confirmó la aprobación del proyecto de data center de Amazon en Huechuraba, observaciones ciudadanas fueron debidamente consideradas.” April 9, 2026. https://tribunalambiental.cl/tribunal-confirmo-la-aprobacion-del-proyecto-de-data-center-de-amazon-en-huechuraba-observaciones-ciudadanas-fueron-debidamente-consideradas/.',
    annotation="AWS Huechuraba: USD 205m. Supports aws_huechuraba_205m_chile_2026.",
    evid_note="Opened Tribunal Ambiental Spanish primary 2026-10-04; USD 205m confirmed.",
)

# 6. power_plants_grid / allied — EDP South America R$7bn 2025–2026
row_doc(
    "edp_south_america_7bn_brl_2025_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "EDP — South America energy-transition CapEx plan 2025–2026",
    "Brazil",
    "18 Jun 2025 EDP: Sustainability Report release states the company plans to invest R$ 7 billion between 2025 and 2026 across South America to accelerate the energy transition (solar/wind consolidation + grid segment expansion); cites Aneel Auction 01/2024 lots 2/7/13 under construction and >R$700m energized Norte lots. CapEx plan = R$7bn.",
    "7000000000",
    "2025-06-18",
    "2025",
    "",
    "",
    "EDP South America multi-country CapEx plan (Brazil/Chile footprint — lat/lon blank).",
    "edp_sa_7bn_20250618",
    "The company plans to invest R$ 7 billion between 2025 and 2026 to accelerate the energy transition, consolidating its operations in solar and wind projects and expanding its presence in the grid segment.",
    "https://edp.com/en/south-america/brazil/media/news/edp-reinforces-energy-transition-actions-investment-r-7-billion",
    "Actor: EDP (Portuguese) — allied. Company English primary. CapEx plan = R$7bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle200",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='EDP. “EDP reinforces energy transition actions with investment of R$ 7 billion in South America.” June 18, 2025. https://edp.com/en/south-america/brazil/media/news/edp-reinforces-energy-transition-actions-investment-r-7-billion.',
    annotation="EDP SA: R$7bn 2025–26 CapEx. Supports edp_south_america_7bn_brl_2025_2026.",
    evid_note="Opened EDP English company primary 2026-10-04; R$7bn 2025–2026 plan confirmed.",
)

# 7. rail / other — Metro SP Linha 17-Ouro phase 1 R$5.9bn
row_doc(
    "metro_sp_linha17_phase1_5p9bn_brl_2026",
    "infrastructure",
    "rail",
    "other",
    "Governo do Estado de São Paulo / Metrô — Linha 17-Ouro phase 1 CapEx",
    "Brazil",
    "30 Jun 2026 Prefeitura de São Paulo Sampa News (Washington Luís station inauguration completing phase 1): Linha 17-Ouro first stage investment R$ 5.9 billion; 6.7 km operational with eight stations linking Congonhas Airport to Lines 5/9. CapEx = R$5.9bn. Distinct from BYD Skyrail rolling-stock supply (no CapEx face opened as Metro primary here).",
    "5900000000",
    "2026-06-30",
    "2026",
    "-23.63",
    "-46.70",
    "Pinned to Estação Washington Luís / Av. Washington Luís × Roberto Marinho (city geography).",
    "prefeitura_sp_linha17_20260630",
    "Com investimento de R$ 5,9 bilhões na primeira etapa da Linha 17-Ouro, a nova estação acrescenta cerca de 800 metros ao sistema e passa a atender uma região estratégica no encontro das avenidas Washington Luís e Jornalista Roberto Marinho.",
    "https://prefeitura.sp.gov.br/web/sampa-news/w/primeira-fase-da-linha-17-ouro-%C3%A9-conclu%C3%ADda-com-inaugura%C3%A7%C3%A3o-da-esta%C3%A7%C3%A3o-washington-lu%C3%ADs-na-zona-sul",
    "Actor: São Paulo state Metro (Brazilian public) — other; BYD trains already noted separately without CapEx. City Portuguese primary. CapEx = R$5.9bn. Shuffle rail.",
    "hunt_cycle200",
    investment_type="greenfield_rail",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Prefeitura de São Paulo. “Primeira fase da Linha 17-Ouro é concluída com inauguração da Estação Washington Luís, na Zona Sul.” June 30, 2026. https://prefeitura.sp.gov.br/web/sampa-news/w/primeira-fase-da-linha-17-ouro-%C3%A9-conclu%C3%ADda-com-inaugura%C3%A7%C3%A3o-da-esta%C3%A7%C3%A3o-washington-lu%C3%ADs-na-zona-sul.',
    annotation="Linha 17 phase 1: R$5.9bn. Supports metro_sp_linha17_phase1_5p9bn_brl_2026.",
    evid_note="Opened Prefeitura SP Portuguese primary 2026-10-04; R$5.9bn confirmed.",
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
    print(f"cycle200 added {len(added)}: {added}")
    print(f"cycle200 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
