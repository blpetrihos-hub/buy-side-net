#!/usr/bin/env python3
"""Cycle 39 hunt: shuffle_seed=20261039; equal budget across 18 subcategories."""
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


# seed 20261039 order:
# wind, lithium, graphite, port_cranes, building_materials, other_renewables,
# bridges_roads, power_plants_grid, rail, nickel, water, niobium, port_ownership,
# fission_smr, solar, copper, balsa, engineering_epc

# 1 energy/wind — miss
# 2 resources/lithium — BID Invest Posco Sal de Oro up to USD 700m
A(
    {
        "id": "bid_invest_posco_sal_de_oro_700m_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "BID Invest — financing package for Posco Sal de Oro expansion",
        "country": "Argentina",
        "asset": "28 Aug 2026 Bloomberg Línea: BID Invest announces financing package of up to USD 700 million for Posco Argentina Sal de Oro (Salar del Hombre Muerto, Salta/Catamarca) — A loan up to USD 250 million plus potential A/B mobilization of up to USD 450 million from IFIs; supports ramp-up of LiOH/Li2CO3 toward ~48 ktpa lithium products. Distinct from posco_sal_de_oro_ii_rigi_2026 (RIGI plan)",
        "investment_type": "project_finance",
        "value": "700000000",
        "currency": "USD",
        "value_usd": "700000000",
        "fx_usd": "1",
        "fx_date": "2026-08-28",
        "year": "2026",
        "status": "active",
        "lat": "-25.4",
        "lon": "-67.1",
        "geo_note": "Salar del Hombre Muerto, Salta/Catamarca (company geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "bloomberg_linea_bid_posco_20260828",
        "note": "Actor: BID Invest (IDB Group — allied multilateral) financing Posco (Korea — allied). UNVERIFIED proxy: Bloomberg Línea 28 Aug 2026 summarizing BID Invest announcement. Facility up-to amounts; not all closed.",
    },
    {
        "id": "bid_invest_posco_sal_de_oro_700m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bloomberg_linea_bid_posco_20260828",
        "url": "https://www.bloomberglinea.com/latinoamerica/argentina/el-litio-argentino-tambien-consigue-financiamiento-internacional-us700-millones-para-posco/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La entidad anunció un paquete de financiamiento de hasta US$700 millones para Posco Argentina, destinado a acompañar la expansión de la extracción y producción de litio de Sal de Oro",
        "note": "Opened Bloomberg Línea Spanish 28 Aug 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "bloomberg_linea_bid_posco_20260828",
        "type": "trade_press",
        "chicago": "Lendoiro, Florencia. “El litio argentino también consigue financiamiento internacional: US$700 millones para Posco.” Bloomberg Línea, 28 August 2026.",
        "url": "https://www.bloomberglinea.com/latinoamerica/argentina/el-litio-argentino-tambien-consigue-financiamiento-internacional-us700-millones-para-posco/",
        "annotation": "Press on BID Invest up to USD 700m for Posco Sal de Oro. Supports bid_invest_posco_sal_de_oro_700m_2026.",
        "supports": ["bid_invest_posco_sal_de_oro_700m_2026", "hunt_res_lithium"],
    },
)

# 3–6 graphite, port_cranes, building, other_renewables — miss

# 7 infrastructure/bridges_roads — Mota-Engil Santos–Guarujá immersed tunnel PPP
A(
    {
        "id": "mota_engil_santos_guaruja_6p8bn_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "Mota-Engil — Túnel Santos–Guarujá PPP (São Paulo)",
        "country": "Brazil",
        "asset": "28 Jan 2026: São Paulo state signs PPP contract with Portuguese Mota-Engil for Brazil’s first immersed tunnel Santos–Guarujá — ~870 m under port channel, three lanes each way + pedestrian/cycle; total investment estimated R$ 6.8 billion (~R$ 7bn cited); 30-year contract incl. O&M; COD targeted 2031; auction won Sep 2025 on B3",
        "investment_type": "ppp_concession",
        "value": "6800000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.98",
        "lon": "-46.3",
        "geo_note": "Santos–Guarujá channel, São Paulo coast (press geography).",
        "evidence": "proxy",
        "source_id": "g1_santos_guaruja_20260128",
        "note": "Actor: Mota-Engil (Portugal) — allied. UNVERIFIED proxy: g1/TV Globo 28 Jan 2026. Distinct from OHLA BR-040 / ERG Popayán road rows.",
    },
    {
        "id": "mota_engil_santos_guaruja_6p8bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "g1_santos_guaruja_20260128",
        "url": "https://g1.globo.com/sp/sao-paulo/noticia/2026/01/28/governo-de-sp-assina-contrato-para-construir-o-tunel-santos-guaruja.ghtml",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Com investimento total estimado em R$ 6,8 bilhões, o projeto prevê a construção de um túnel de 870 metros sob o canal portuário, com três faixas por sentido, passagem para pedestres e ciclistas e galeria de serviços.",
        "note": "Opened g1 Portuguese 28 Jan 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "g1_santos_guaruja_20260128",
        "type": "trade_press",
        "chicago": "Simonato, Sabina. “Governo de SP assina contrato para construir o Túnel Santos-Guarujá.” g1 / TV Globo, 28 January 2026.",
        "url": "https://g1.globo.com/sp/sao-paulo/noticia/2026/01/28/governo-de-sp-assina-contrato-para-construir-o-tunel-santos-guaruja.ghtml",
        "annotation": "Press on Mota-Engil Santos–Guarujá tunnel PPP R$6.8bn. Supports mota_engil_santos_guaruja_6p8bn_2026.",
        "supports": ["mota_engil_santos_guaruja_6p8bn_2026", "hunt_infra_bridges_roads"],
    },
)

# 8 energy/power_plants_grid — miss

# 9 infrastructure/rail — ACA Transnordestina + Tren Macho
A(
    {
        "id": "aca_transnordestina_sps04_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "ACA (Alberto Couto Alves) — Transnordestina Lot SPS 04",
        "country": "Brazil",
        "asset": "27 Jul 2026 ECO (Portugal): Portuguese builder ACA signs with Infra S.A. (Ministério dos Transportes) for executive engineering + remaining infrastructure on Ferrovia Transnordestina Lot SPS 04 in Pernambuco — 73.32 km Custódia–Arcoverde toward Salgueiro–Suape corridor; contract R$ 312.8 million (~EUR 61.4m); 57-month term; earthworks, drainage, bridges/viaducts",
        "investment_type": "rail_epc",
        "value": "312800000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.5",
        "lon": "-37.2",
        "geo_note": "Custódia–Arcoverde, Pernambuco (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "eco_aca_transnordestina_20260727",
        "note": "Actor: ACA Portugal — allied. UNVERIFIED proxy: ECO 27 Jul 2026 citing company communiqué. Distinct from PowerChina Chancay rail.",
    },
    {
        "id": "aca_transnordestina_sps04_2026",
        "retrieved": "2026-10-01",
        "source_id": "eco_aca_transnordestina_20260727",
        "url": "https://eco.sapo.pt/2026/07/27/grupo-aca-de-famalicao-ganha-contrato-de-61-milhoes-na-ferrovia-do-brasil/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A construtora de Famalicão ACA (Alberto Couto Alves) ganhou um contrato no valor de 312,8 milhões de reais (61,4 milhões de euros) para desenvolver um troço de 73,32 quilómetros da Ferrovia Transnordestina, em Pernambuco, no Brasil.",
        "note": "Opened ECO Portuguese 27 Jul 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "eco_aca_transnordestina_20260727",
        "type": "trade_press",
        "chicago": "Abreu, Patrícia. “Grupo ACA de Famalicão ganha contrato de 61 milhões na ferrovia do Brasil.” ECO, 27 July 2026.",
        "url": "https://eco.sapo.pt/2026/07/27/grupo-aca-de-famalicao-ganha-contrato-de-61-milhoes-na-ferrovia-do-brasil/",
        "annotation": "Press on ACA Transnordestina SPS 04 R$312.8m. Supports aca_transnordestina_sps04_2026.",
        "supports": ["aca_transnordestina_sps04_2026", "hunt_latam_rail_telecom"],
    },
)

A(
    {
        "id": "tren_macho_huancayo_339m_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "other",
        "counterpart": "Cofeperú — Ferrocarril Huancayo–Huancavelica (Tren Macho) modernization APP",
        "country": "Peru",
        "asset": "Jun 2026 La República / Ositrán context: Huancayo–Huancavelica Tren Macho modernization valued USD 339 million; 128.2 km, 7 stations, 20 stops, 15 bridges, 38 tunnels; 30-year cofinanced APP with Concesionaria Ferroviaria del Perú (Cofeperú); EDI civil works ~67% as of May 2026; financial close Apr 2027; works start May 2027",
        "investment_type": "ppp_concession",
        "value": "339000000",
        "currency": "USD",
        "value_usd": "339000000",
        "fx_usd": "1",
        "fx_date": "2026-06-22",
        "year": "2026",
        "status": "active",
        "lat": "-12.07",
        "lon": "-75.2",
        "geo_note": "Huancayo–Huancavelica corridor (press geography; approximate pin at Huancayo).",
        "evidence": "proxy",
        "source_id": "larepublica_tren_macho_20260622",
        "note": "Actor: Cofeperú concession (Peruvian APP — other). UNVERIFIED proxy: La República 22/24 Jun 2026. Distinct from PowerChina Chancay / ACA Transnordestina.",
    },
    {
        "id": "tren_macho_huancayo_339m_2026",
        "retrieved": "2026-10-01",
        "source_id": "larepublica_tren_macho_20260622",
        "url": "https://larepublica.pe/sociedad/2026/06/22/asi-avanza-el-tren-macho-tras-casi-100-anos-nueva-ruta-costara-us339-millones-e-iniciara-obras-en-mayo-de-2027-506506",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La obra, valorizada en US$339 millones, tiene previsto iniciar trabajos en mayo de 2027 y apunta a una renovación integral del sistema ferroviario entre Junín y Huancavelica.",
        "note": "Opened La República Spanish Jun 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "larepublica_tren_macho_20260622",
        "type": "trade_press",
        "chicago": "Tosso, Valeria. “Así avanza el Tren Macho tras casi 100 años: nueva ruta costará US$339 millones e iniciará obras en mayo de 2027.” La República (Peru), 22 June 2026.",
        "url": "https://larepublica.pe/sociedad/2026/06/22/asi-avanza-el-tren-macho-tras-casi-100-anos-nueva-ruta-costara-us339-millones-e-iniciara-obras-en-mayo-de-2027-506506",
        "annotation": "Press on Tren Macho modernization USD 339m. Supports tren_macho_huancayo_339m_2026.",
        "supports": ["tren_macho_huancayo_339m_2026", "hunt_latam_rail_telecom"],
    },
)

# 10–15 nickel, water, niobium, port_ownership, fission, solar — miss

# 16 resources/copper — McEwen Los Azules USD 240m financing (cited in same Bloomberg piece)
A(
    {
        "id": "mcewen_los_azules_240m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "McEwen Copper — Los Azules financing before FID",
        "country": "Argentina",
        "asset": "28 Aug 2026 Bloomberg Línea (same article as BID/Posco): McEwen Copper recently closed USD 240 million financing to advance Los Azules copper project in San Juan toward final investment decision. UNVERIFIED secondary mention — company details not opened this cycle",
        "investment_type": "project_finance",
        "value": "240000000",
        "currency": "USD",
        "value_usd": "240000000",
        "fx_usd": "1",
        "fx_date": "2026-08-28",
        "year": "2026",
        "status": "active",
        "lat": "-31.2",
        "lon": "-70.0",
        "geo_note": "Los Azules, San Juan (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "bloomberg_linea_bid_posco_20260828",
        "note": "Actor: McEwen Copper (Canada/US-linked — allied). UNVERIFIED proxy: Bloomberg Línea secondary mention 28 Aug 2026. Distinct from Vicuña / El Abra / Las Bambas copper rows.",
    },
    {
        "id": "mcewen_los_azules_240m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bloomberg_linea_bid_posco_20260828",
        "url": "https://www.bloomberglinea.com/latinoamerica/argentina/el-litio-argentino-tambien-consigue-financiamiento-internacional-us700-millones-para-posco/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "McEwen Copper cerró recientemente un financiamiento por US$240 millones para continuar avanzando con Los Azules, el proyecto de cobre ubicado en San Juan, antes de alcanzar su decisión final de inversión.",
        "note": "Opened Bloomberg Línea Spanish 28 Aug 2026. Mark UNVERIFIED proxy (secondary mention).",
    },
    {
        "id": "bloomberg_linea_mcewen_azules_20260828",
        "type": "trade_press",
        "chicago": "Lendoiro, Florencia. “El litio argentino también consigue financiamiento internacional: US$700 millones para Posco.” Bloomberg Línea, 28 August 2026.",
        "url": "https://www.bloomberglinea.com/latinoamerica/argentina/el-litio-argentino-tambien-consigue-financiamiento-internacional-us700-millones-para-posco/",
        "annotation": "Same article notes McEwen Los Azules USD 240m financing. Supports mcewen_los_azules_240m_2026.",
        "supports": ["mcewen_los_azules_240m_2026", "hunt_res_copper"],
    },
)

# 17–18 balsa, engineering_epc — miss


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    updated = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
            updated.append(rid)
        else:
            rows.append({k: row.get(k, "") for k in FIELDS})
            by_id[rid] = len(rows) - 1
            added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
            if bib_entry.get("supports"):
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(bib_entry["supports"])
                )
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    hunt_updates = {
        "hunt_energy_wind": "Cycle 39: equal budget; Goldwind/Vestas already (miss).",
        "hunt_res_lithium": "Cycle 39: logged bid_invest_posco_sal_de_oro_700m_2026.",
        "hunt_res_graphite": "Cycle 39: equal budget; Graphcoa already (miss).",
        "hunt_infra_port_cranes": "Cycle 39: equal budget; Kalmar/ZPMC Montevideo already (miss).",
        "hunt_infra_building_materials": "Cycle 39: equal budget; Holcim rows already (miss).",
        "hunt_energy_other_renewables": "Cycle 39: equal budget; Acciona El Romero already (miss).",
        "hunt_infra_bridges_roads": "Cycle 39: logged mota_engil_santos_guaruja_6p8bn_2026.",
        "hunt_br_power_equip": "Cycle 39: equal budget; Hitachi already (miss).",
        "hunt_latam_rail_telecom": "Cycle 39: logged aca_transnordestina_sps04_2026 + tren_macho_huancayo_339m_2026.",
        "hunt_res_nickel": "Cycle 39: equal budget; PNP/Canada ECA already (miss).",
        "hunt_res_water": "Cycle 39: equal budget; Zaldívar water already (miss).",
        "hunt_fenb_araxa": "Cycle 39: equal budget; CBMM/St George already (miss).",
        "hunt_infra_port_ownership": "Cycle 39: equal budget; Katoen/ICAVE already (miss).",
        "hunt_energy_fission_smr": "Cycle 39: equal budget; Peru law/Ecuador MoU already (miss).",
        "hunt_energy_solar": "Cycle 39: equal budget; PowerChina Mauriti already (miss).",
        "hunt_res_copper": "Cycle 39: logged mcewen_los_azules_240m_2026.",
        "hunt_res_balsa": "Cycle 39: equal budget; AIMA shares already (miss).",
        "hunt_infra_engineering_epc": "Cycle 39: equal budget; GES Pampas already (miss).",
    }
    for hid, note in hunt_updates.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 39 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 39 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
