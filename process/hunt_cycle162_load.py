#!/usr/bin/env python3
"""Cycle 162 hunt: shuffle_seed=20261162; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: niobium, nickel, graphite, lithium, rail, engineering_epc,
solar, other_renewables, port_cranes, power_plants_grid, bridges_roads, balsa,
port_ownership, fission_smr, building_materials, wind, copper, water.

Weight under-covered: Nicaragua, Paraguay, Colombia port_ownership, Mexico, Haiti.
PRC ahead by 3 — keep equal US/PRC budget without padding.
Thin top-up: nickel once (DFC TechMet equity); balsa/graphite/fission_smr dry → shift.
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


# 1. nickel / us — DFC equity USD 30m in TechMet / Brazilian Nickel (distinct from LOI USD 550m)
row_doc(
    "dfc_techmet_brazil_nickel_30m_equity",
    "resources",
    "nickel",
    "us",
    "DFC — equity investment in TechMet / Brazilian Nickel (Piauí Ni/Co mine)",
    "Brazil",
    "DFC investment-story profile (2024): USD 30 million DFC equity supporting TechMet Limited development of a critical-mineral mining facility in Brazil producing nickel and cobalt (Brazilian Nickel open-pit laterite / Piauí Nickel Project lineage). Distinct from brazilian_nickel_dfc_loi_2024 (up to USD 550m senior-loan LOI) and dfc_piaui_nickel_esia_followon_2026 (follow-on ESIA disclosure without restated loan face).",
    "30000000",
    "2024-12-31",
    "2024",
    "-8.10",
    "-42.50",
    "Piauí Nickel Project / Capitão Gervásio Oliveira area, Piauí, Brazil (project geography; approximate).",
    "dfc_techmet_cobalt_nickel_story_2024",
    "In Brazil, DFC’s $30 million investment is supporting the development of a critical mineral mining facility that will produce nickel and cobalt for the industries of the future. The project is designed to bolster U.S. supply chains for these essential minerals and strengthen U.S. relations with Brazil",
    "https://www.dfc.gov/investment-story/sourcing-cobalt-and-other-critical-minerals-countering-chinas-rare-earth-dominance",
    "Actor: U.S. International Development Finance Corporation equity into TechMet/Brazilian Nickel — us. Official DFC investment-story primary. USD 30m equity face. Thin nickel top-up this session.",
    "hunt_res_nickel",
    investment_type="financing",
    bib_type="government",
    chicago='U.S. International Development Finance Corporation. “Sourcing Cobalt and Other Critical Minerals by Countering China’s Rare Earth Dominance.” 2024. https://www.dfc.gov/investment-story/sourcing-cobalt-and-other-critical-minerals-countering-chinas-rare-earth-dominance.',
    annotation="DFC primary: USD 30m equity supporting TechMet Brazil nickel/cobalt mine. Supports dfc_techmet_brazil_nickel_30m_equity.",
    evid_note="Opened DFC investment-story page (USD 30m TechMet/Brazil nickel equity).",
)

# 2. bridges_roads / prc — CSCEC International Litoral del Pacífico Fase II credit RMB 1.805bn
row_doc(
    "cscec_litoral_pacifico_fase2_nicaragua_2024",
    "infrastructure",
    "bridges_roads",
    "prc",
    "CSCEC International — Carretera Litoral del Pacífico Fase II credit facilities (Masachapa–Poneloya)",
    "Nicaragua",
    "28 Jun 2024 credit facilities approved by Asamblea Nacional Decreto A.N. Nº 8885 (14 Aug 2024 / Gaceta 151 16 Aug 2024): CSCEC International Construction Co., Ltd. extends total RMB 1,804,754,237.15 to Nicaragua MHCP for Carretera Litoral del Pacífico Fase II — Tramo I Masachapa–Puente La Gloria RMB 918,896,364.95 + Tramo II Puente La Gloria–Poneloya RMB 885,857,872.20; MTI executing unit; ~96.7 km / 12 bridges per Asamblea press. CapEx stored as CNY credit face (USD conversion blank). Distinct from camce_punta_huete_road_71p96m_2025.",
    "1804754237.15",
    "",
    "2024",
    "11.790",
    "-86.510",
    "Masachapa–Poneloya Pacific littoral corridor, Nicaragua (Masachapa start pin; ~96.7 km).",
    "asamblea_cscec_litoral_fase2_decreto_8885_2024",
    "Apruébese el Acuerdo de Facilidad de Crédito Tramo I: Est. 0+000 (Masachapa) a Est. 49+500 (Puente La Gloria) por un monto de RMB 918,896,364.95 … y Acuerdo de Facilidad de Crédito Tramo II: Est. 49+500 (Puente La Gloria) a Est. 94+700 (Poneloya) por un monto de RMB 885,857,872.20 … para un monto total de RMB 1,804,754,237.15 … suscritos el 28 de junio de 2024 … con CSCEC International Construction Co., Ltd. (CSCEC International) de la República Popular de China, para financiar el Proyecto Construcción de la Carretera Litoral del Pacifico, Fase II",
    "http://legislacion.asamblea.gob.ni/normaweb.nsf/9e314815a08d4a6206257265005d21f9/fa84bfd254ad2a9c06258b7b0063a04e?OpenDocument",
    "Actor: CSCEC International (PRC SOE) lender/EPC financing — prc. Asamblea Nacional decree primary. Value = RMB credit face; USD blank. Undersampled Nicaragua×bridges_roads beyond CAMCE Punta Huete road.",
    "hunt_infra_bridges_roads",
    investment_type="financing",
    currency="CNY",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Asamblea Nacional de la República de Nicaragua. “Decreto A.N. Nº. 8885 — Aprobación de Acuerdos de Facilidad de Crédito CSCEC International (Carretera Litoral del Pacífico, Fase II).” August 14, 2024. http://legislacion.asamblea.gob.ni/normaweb.nsf/9e314815a08d4a6206257265005d21f9/fa84bfd254ad2a9c06258b7b0063a04e?OpenDocument.',
    annotation="Asamblea decree: CSCEC International RMB 1.805bn Litoral Pacífico Fase II. Supports cscec_litoral_pacifico_fase2_nicaragua_2024.",
    evid_note="Opened Asamblea Decreto A.N. 8885 (CSCEC Litoral Fase II credit RMB totals).",
)

# 3. port_ownership / allied — APM Terminals TCBUEN Buenaventura (fills Colombia empty cell)
row_doc(
    "apm_tcbuen_buenaventura_colombia",
    "infrastructure",
    "port_ownership",
    "allied",
    "APM Terminals — Terminal de Contenedores de Buenaventura (TCBUEN)",
    "Colombia",
    "APM Terminals Buenaventura terminal page (opened): TCBUEN Pacific container terminal — 440 m quay, 14 m depth at low tide, storage capacity up to 650,000 TEU/year; since 2016 part of APM Terminals with Colombian Infrastructure Equity Fund (CIEF) sponsor and >800 minority shareholders. CapEx blank (ownership/operation presence; no modernisation USD on opened page). Distinct from apm_moin / apm_callao / apm_suape rows. Fills Colombia×port_ownership empty cell.",
    "",
    "",
    "2016",
    "3.880",
    "-77.080",
    "TCBUEN / Terminal de Contenedores de Buenaventura, Valle del Cauca, Colombia.",
    "apm_tcbuen_terminal_page",
    "Ubicada en la costa oeste del Pacífico de Colombia, la Terminal de Contenedores de Buenaventura TCBUEN … contamos con una capacidad de almacenamiento de hasta 650,000 TEUS al año. … TCBUEN desde el año 2016 hace parte de APM Terminals, uno de los principales operadores mundiales que ofrece servicios portuarios en 58 países … junto con nuestro sponsor el Fondo de Capital Privado Colombian Infrastructure Equity Fund CIEF y más de 800 accionistas minoritarios",
    "https://www.apmterminals.com/es/buenaventura/about/our-terminal",
    "Actor: APM Terminals (A.P. Moller–Maersk, Copenhagen HQ) — allied. Company Spanish primary. CapEx blank. First Colombia US/allied/PRC-tagged port_ownership row.",
    "hunt_infra_port_ownership",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='APM Terminals. “Nuestra terminal de contenedores — TCBUEN Buenaventura.” Accessed October 2, 2026. https://www.apmterminals.com/es/buenaventura/about/our-terminal.',
    annotation="APM Terminals primary: TCBUEN ownership since 2016 / 650k TEU capacity. Supports apm_tcbuen_buenaventura_colombia.",
    evid_note="Opened APM Terminals Buenaventura terminal page (TCBUEN ownership).",
)

# 4. bridges_roads / allied — Sacyr Rutas 2 y 7 Paraguay PPP
row_doc(
    "sacyr_rutas_2_7_paraguay_530m",
    "infrastructure",
    "bridges_roads",
    "allied",
    "Sacyr Concesiones / Ocho A — Rutas del Este PPP (Rutas 2 y 7)",
    "Paraguay",
    "12 Jan 2022 IDB Invest: structures/purchases first U.S.-market project bond providing USD 219 million financing to Rutas del Este S.A. (Sacyr Concesiones + Ocho A) for design/construction of national roads 2 and 7; total project cost approximately USD 530 million; first PPP under Paraguay PPP Law; concession granted 2016; ~140 km extension/improvement Asunción–Ciudad del Este corridor; lane doubling on ~80% of routes. CapEx = stated ~USD 530m project cost. Distinct from caddell_asuncion_nec_2017. Fills Paraguay×bridges_roads empty cell.",
    "530000000",
    "2022-01-12",
    "2022",
    "-25.400",
    "-56.500",
    "Rutas 2 y 7 corridor Asunción–Ciudad del Este, Paraguay (approximate mid-corridor pin).",
    "idb_invest_rutas_2_7_paraguay_20220112",
    "IDB Invest has structured and purchased its first project bond in the U.S. market to provide $219 million worth of financing to Rutas del Este S.A. for the design and construction of national roads 2 and 7 in Paraguay. Rutas del Este is a consortium comprised of companies Sacyr Concesiones and Ocho A. … The project has a total cost of approximately $530 million and is the first public-private partnership (PPP) contract signed within the framework of Paraguay's PPP Law … The concession was granted in 2016 and consists of the extension and improvement of 140km of road.",
    "https://idbinvest.org/en/news-media/idb-invest-structures-its-first-project-bond-us-market-finance-paraguays-first-ppp-rutas-2",
    "Actor: Sacyr Concesiones (Spain) lead concessionaire — allied; local partner Ocho A. IDB Invest English primary. Value = ~USD 530m total project cost (bond face USD 219m also disclosed).",
    "hunt_infra_bridges_roads",
    investment_type="concession",
    bib_type="government",
    chicago='IDB Invest. “IDB Invest Structures Its First Project Bond in the U.S. Market to Finance Paraguay’s First PPP: Rutas 2 y 7.” January 12, 2022. https://idbinvest.org/en/news-media/idb-invest-structures-its-first-project-bond-us-market-finance-paraguays-first-ppp-rutas-2.',
    annotation="IDB Invest primary: Sacyr/Ocho A Rutas 2 y 7 ~USD 530m / USD 219m bond. Supports sacyr_rutas_2_7_paraguay_530m.",
    evid_note="Opened IDB Invest 12 Jan 2022 (Rutas 2 y 7 Paraguay PPP).",
)

# 5. solar / allied — Butler/Ciudad Luz Puerto Esperanza hybrid solar (Paraguay)
row_doc(
    "butler_ciudadluz_puerto_esperanza_solar_py",
    "energy",
    "solar",
    "allied",
    "Consorcio Esperanza 3 (Butler Corporation / Ciudad Luz / CONO) — Puerto Esperanza hybrid PV (Bahía Negra)",
    "Paraguay",
    "2 Aug 2022 Radio Nacional Paraguay citing ANDE: contract signed for first PV generation plant serving Yshyr community at Puerto Esperanza, Bahía Negra (Chaco) — hybrid on-grid PV with batteries; 700 kWp Jinko field, 700 kW MPPT inverters, 1,000 kW charger inverters, 2,520 kWh + 528 kWh batteries (3,048 kWh total); investment USD 2,072,852.26 plus Gs. 1,386,742,155 (~15.7bn guaraníes total) via LPI 1663/2021 IDB-financed; executed by Consorcio Esperanza 3 — CONO S.R.L (Paraguay), Servicio de Energía Ciudad Luz (Chile), Butler Corporation (Chile). CapEx = USD line disclosed (PYG leg left aside). Distinct from sacyr_rutas_2_7_paraguay_530m. Fills Paraguay×solar empty cell.",
    "2072852.26",
    "2022-08-02",
    "2022",
    "-20.230",
    "-58.170",
    "Puerto Esperanza / Bahía Negra, Alto Paraguay department, Paraguay (Yshyr community site).",
    "radio_nacional_ande_puerto_esperanza_20220802",
    "estas obras requerirán una inversión de USD 2.072.852,26 más Gs. 1.386.742.155, totalizando una inversión de unos 15.700 millones de guaraníes, a través de la Licitación Pública Internacional N° 1663/2021, financiada a través del Banco Interamericano de Desarrollo (BID) y serán ejecutadas por el Consorcio Esperanza 3, CONO S.R.L (Paraguay), SERVICIO DE ENERGÍA CIUDAD LUZ (Chile), BUTLER CORPORATION (Chile). … la planta solar contará con un campo fotovoltaico de 700 kWp (paneles fotovoltaicos JINKO)",
    "https://www.radionacional.gov.py/ande-firma-contrato-para-construccion-de-planta-de-generacion-fotovoltaica-para-comunidad-indigena-del-chaco/",
    "Actor: Butler Corporation + Ciudad Luz (Chile) consortium leads — allied; local CONO. Radio Nacional (state) primary citing ANDE contract. Value = USD component only.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="government",
    chicago='Radio Nacional del Paraguay. “ANDE firma contrato para construcción de planta de generación fotovoltaica para comunidad indígena del Chaco.” August 2, 2022. https://www.radionacional.gov.py/ande-firma-contrato-para-construccion-de-planta-de-generacion-fotovoltaica-para-comunidad-indigena-del-chaco/.',
    annotation="Radio Nacional/ANDE: Puerto Esperanza 700 kWp hybrid PV / USD 2.07m + Chilean EPC. Supports butler_ciudadluz_puerto_esperanza_solar_py.",
    evid_note="Opened Radio Nacional 2 Aug 2022 (ANDE Puerto Esperanza solar contract).",
)

# 6. solar / us — Pattern Energy Helios Generation 150 MW Zacatecas
row_doc(
    "pattern_helios_zacatecas_150mw_2022",
    "energy",
    "solar",
    "us",
    "Pattern Energy — Helios Generation solar (150 MW; Mazapil, Zacatecas)",
    "Mexico",
    "Pattern Energy 2025 Sustainability Report operational portfolio table lists Helios Generation 150 MW, commissioned 2022, Zacatecas, Mexico. Companion Pattern Helios Solar project page places the facility in Municipio de Mazapil, Zacatecas (Operativo sibling Tuli). CapEx blank on opened pages. Distinct from invenergy_la_toba_70m_2022 (BCS hybrid). Undersampled Mexico×US solar beyond prior set.",
    "",
    "",
    "2022",
    "23.858",
    "-101.715",
    "Helios Generation / Mazapil municipality, Zacatecas, Mexico (Pattern project geography; approximate).",
    "pattern_esg_2025_helios",
    "Helios Generation 150 2022 Zacatecas Mexico",
    "https://patternenergy.com/wp-content/uploads/2025/09/Pattern-Energy-2025-ESG-Report.pdf",
    "Actor: Pattern Energy (San Francisco HQ) — us. Company 2025 ESG PDF primary listing 150 MW Helios COD 2022. CapEx blank.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Pattern Energy Group. “2025 Sustainability Report.” September 2025. https://patternenergy.com/wp-content/uploads/2025/09/Pattern-Energy-2025-ESG-Report.pdf.',
    annotation="Pattern 2025 ESG: Helios Generation 150 MW Zacatecas COD 2022. Supports pattern_helios_zacatecas_150mw_2022.",
    evid_note="Opened Pattern 2025 ESG PDF (Helios Generation 150 MW portfolio line).",
)

# 7. wind / us — AES Mesa La Paz 306 MW Tamaulipas
row_doc(
    "aes_mesa_la_paz_mexico_306mw",
    "energy",
    "wind",
    "us",
    "AES México / EnerAB — Eólica Mesa La Paz (306 MW; Llera de Canales, Tamaulipas)",
    "Mexico",
    "AES México Our History page: 2018 construction began on Eólica Mesa La Paz Wind Farm in Tamaulipas; 2020 commercial operations. AES Q2 2025 Fact Sheet lists Mesa La Paz Mexico wind among portfolio assets (Peñoles offtake). CapEx blank on opened pages. Distinct from pattern_helios_zacatecas_150mw_2022. Fills Mexico wind presence with named AES EnerAB JV plant still active in 2025 IR.",
    "",
    "",
    "2020",
    "23.320",
    "-98.990",
    "Eólica Mesa La Paz / Llera de Canales, Tamaulipas, Mexico (AES/Peñoles geography; approximate).",
    "aes_mexico_history_mesa_la_paz",
    "2018: Construction began for our Eólica Mesa La Paz Wind Farm in Tamaulipas. … 2020: Eólica Mesa La Paz entered commercial operations",
    "https://www.aesmex.com/en/our-history",
    "Actor: AES Corporation via AES México / EnerAB JV — us. Company English primary. CapEx blank. Observation year = COD 2020; ownership reconfirmed on 2025 AES Fact Sheet.",
    "hunt_energy_wind",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES México. “Our History.” Accessed October 2, 2026. https://www.aesmex.com/en/our-history.',
    annotation="AES México primary: Mesa La Paz wind farm COD 2020. Supports aes_mesa_la_paz_mexico_306mw.",
    evid_note="Opened AES México history page (Mesa La Paz COD 2020).",
)

# 8. wind / us — Pattern Tuli Energy 150 MW Zacatecas (portfolio confirmed 2025)
row_doc(
    "pattern_tuli_zacatecas_150mw_2019",
    "energy",
    "wind",
    "us",
    "Pattern Energy — Tuli Energy wind (150 MW; Zacatecas)",
    "Mexico",
    "Pattern Energy 2025 Sustainability Report operational portfolio table lists Tuli Energy 150 MW, commissioned 2019, Zacatecas, Mexico alongside Helios Generation. CapEx blank. Distinct from pattern_helios_zacatecas_150mw_2022. Completes Pattern Mexico named wind/solar pair still held in 2025 ESG.",
    "",
    "",
    "2019",
    "23.850",
    "-101.700",
    "Tuli Energy / Mazapil–Zacatecas corridor, Mexico (Pattern portfolio geography; approximate near Helios).",
    "pattern_esg_2025_helios",
    "Tuli Energy 150 2019 Zacatecas Mexico",
    "https://patternenergy.com/wp-content/uploads/2025/09/Pattern-Energy-2025-ESG-Report.pdf",
    "Actor: Pattern Energy (San Francisco HQ) — us. Same 2025 ESG PDF primary. CapEx blank. Year = COD 2019; ownership reconfirmed in 2025 report.",
    "hunt_energy_wind",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Pattern Energy Group. “2025 Sustainability Report.” September 2025. https://patternenergy.com/wp-content/uploads/2025/09/Pattern-Energy-2025-ESG-Report.pdf.',
    annotation="Pattern 2025 ESG: Tuli Energy 150 MW Zacatecas COD 2019. Supports pattern_tuli_zacatecas_150mw_2019; pattern_helios_zacatecas_150mw_2022.",
    evid_note="Opened Pattern 2025 ESG PDF (Tuli Energy 150 MW portfolio line).",
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
    print(f"Cycle 162 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
