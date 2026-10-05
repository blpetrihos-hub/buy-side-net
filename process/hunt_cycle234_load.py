#!/usr/bin/env python3
"""Cycle 234 hunt: shuffle_seed=20261234; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261234).shuffle):
balsa, other_renewables, nickel, lithium, rail, building_materials, fission_smr,
engineering_epc, water, niobium, port_cranes, wind, power_plants_grid, graphite,
copper, bridges_roads, port_ownership, solar.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; 0 new US CapEx — honest residual).
PRC equal-budget: CAMCE Punta Huete; CSCEC Litoral Pacífico Fase 2; Jiangxi Cascabel.
Skipped: RAP-as-CapEx (State Grid); Huaxin–CSN pre-close; Xinhai MoU; Aldesa EUR
(no EUR on company page); ISA Madeira equity unwind; DOP/COP/CLP/PEN (no Fed H.10).
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

BRL_USD = "5.1921"
BRL_FX_DATE = "2026-09-25"
CNY_USD = "6.7110"
CNY_FX_DATE = "2026-09-25"
GBP_USD = "1.3250"  # Fed H.10 asterisk USD per GBP
GBP_FX_DATE = "2026-09-25"
CAD_USD = "1.4140"
CAD_FX_DATE = "2026-09-25"
SEK_USD = "9.9047"
SEK_FX_DATE = "2026-09-25"


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid, "layer": layer, "subcategory": subcategory, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": currency,
            "value_usd": value_usd, "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
            "lat": lat, "lon": lon, "geo_note": geo, "evidence": evidence,
            "source_id": source_id, "note": note, "pair_id": "", "counterpart_side": "",
            "counterpart_actor": "", "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-05", "source_id": source_id, "url": url,
            "price_year": year, "evidence": evidence, "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id, "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url, "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. rail / allied — CapEx-fill ACA Transnordestina SPS 04 R$312.8m
row_doc(
    "aca_transnordestina_sps04_2026",
    "infrastructure", "rail", "allied",
    "ACA (Alberto Couto Alves) — Ferrovia Transnordestina Lot SPS 04",
    "Brazil",
    "27 Jul 2026 ECO (Portugal): Portuguese builder ACA signs with Infra S.A. for executive engineering + remaining infrastructure on Ferrovia Transnordestina Lot SPS 04 in Pernambuco — 73.32 km; contract value R$312.8 million (company dual €61.4m). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~60.25m.",
    "312800000", BRL_FX_DATE, "2026", "-8.5", "-37.2",
    "Ferrovia Transnordestina Lot SPS 04, Pernambuco (press geography).",
    "eco_aca_transnordestina_20260727",
    "A construtora de Famalicão ACA (Alberto Couto Alves) ganhou um contrato no valor de 312,8 milhões de reais (61,4 milhões de euros) para desenvolver um troço de 73,32 quilómetros da Ferrovia Transnordestina, em Pernambuco",
    "https://eco.sapo.pt/2026/07/27/grupo-aca-de-famalicao-ganha-contrato-de-61-milhoes-na-ferrovia-do-brasil/",
    "Actor: ACA / Alberto Couto Alves (Portugal) — allied. CapEx-fill: retain R$312.8m; add Fed H.10 Sep 25 2026 FX to USD ~60.25m. Shuffle rail.",
    "hunt_cycle234", investment_type="epc", evidence="proxy", currency="BRL",
    value_usd=str(round(312800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='ECO. “Grupo ACA de Famalicão ganha contrato de 61 milhões na ferrovia do Brasil.” July 27, 2026. https://eco.sapo.pt/2026/07/27/grupo-aca-de-famalicao-ganha-contrato-de-61-milhoes-na-ferrovia-do-brasil/.',
    annotation="ACA Transnordestina CapEx-fill ~USD 60.25m via Fed H.10 (proxy). Supports aca_transnordestina_sps04_2026.",
    evid_note="Opened ECO Portuguese; R$312.8m / 73.32 km SPS 04 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. engineering_epc / prc — CapEx-fill CAMCE Punta Huete RMB ~2.875bn
row_doc(
    "camce_punta_huete_airport_credit_2p875bn_rmb_2024",
    "infrastructure", "engineering_epc", "prc",
    "CAMCE — Punta Huete International Airport credit facilities",
    "Nicaragua",
    "3 Jan 2024 credit facilities (National Assembly approval 9 Feb 2024): CAMCE deferred-payment agreements with Nicaragua MHCP totaling RMB 2,874,652,142.91 for Reconstruction, Expansion and Upgrading of Punta Huete International Airport. CapEx-fill: Fed H.10 Sep 25 2026 China Yuan 6.7110 → USD ~428.35m.",
    "2874652142.91", CNY_FX_DATE, "2024", "12.35", "-86.20",
    "Punta Huete International Airport, Managua department (AidData geography).",
    "aiddata_camce_punta_huete_section_a_107086",
    "UN MONTO DE RMB 1,436,231,236.69 PARA UN MONTO TOTAL DE RMB 2,874,652,142.91, SUSCRITOS EL 03 DE ENERO DE 2024 ENTRE LA REPÚBLICA DE NICARAGUA, REPRESENTADA POR EL MINISTERIO DE HACIENDA Y CRÉDITO PÚBLICO Y CHINA CAMC EN",
    "https://china.aiddata.org/projects/107086",
    "Actor: China CAMC Engineering (CAMCE) — prc. CapEx-fill: retain RMB 2,874,652,142.91; add Fed H.10 Sep 25 2026 FX to USD ~428.35m. Shuffle engineering_epc / PRC equal-budget.",
    "hunt_cycle234", investment_type="export_credit", evidence="documented", currency="CNY",
    value_usd=str(round(2874652142.91 / float(CNY_USD), 2)), fx_usd=CNY_USD, bib_type="gov",
    chicago='AidData / Asamblea Nacional de Nicaragua. “CAMCE Punta Huete International Airport credit facilities (project 107086).” 2024. https://china.aiddata.org/projects/107086.',
    annotation="CAMCE Punta Huete CapEx-fill ~USD 428.35m via Fed H.10. Supports camce_punta_huete_airport_credit_2p875bn_rmb_2024.",
    evid_note="Opened AidData/assembly Spanish; RMB 2,874,652,142.91 total CAMCE facilities confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 6.7110 CNY/USD.",
)

# 3. power_plants_grid / allied — CapEx-fill Neoenergia Guará 2 R$32m
row_doc(
    "neoenergia_guara2_32m_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Brasília — Subestação Guará 2 (R$32m)",
    "Brazil",
    "6 Aug 2026 Neoenergia Brasília: Subestação Guará 2 delivered as first major work of the new DF cycle — total investment R$ 32 million; +66.6 MVA. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~6.16m.",
    "32000000", BRL_FX_DATE, "2026", "-15.82", "-47.98",
    "Guará, Distrito Federal (company geography).",
    "neoenergia_brasilia_3p1bn_20260806",
    "A nova subestação, que recebeu investimento total de R$ 32 milhões, acrescenta 66,6 MVA de potência ao sistema elétrico e beneficia cerca de 180 mil moradores diretamente.",
    "https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df",
    "Actor: Neoenergia Brasília (Iberdrola) — allied. CapEx-fill: retain R$32m; add Fed H.10 Sep 25 2026 FX to USD ~6.16m. Shuffle power_plants_grid.",
    "hunt_cycle234", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(32000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Neoenergia. “Neoenergia anuncia plano recorde de R$ 3,1 bilhões para fortalecer a infraestrutura elétrica do DF.” August 6, 2026. https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df.',
    annotation="Neoenergia Guará 2 CapEx-fill ~USD 6.16m via Fed H.10. Supports neoenergia_guara2_32m_brl_2026.",
    evid_note="Opened Neoenergia Portuguese; R$32m Guará 2 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. bridges_roads / other — CapEx-fill EPR Régis Bittencourt R$7.2bn
row_doc(
    "epr_regis_bittencourt_7p2bn_2026",
    "infrastructure", "bridges_roads", "other",
    "EPR Participações — Autopista Régis Bittencourt concession",
    "Brazil",
    "23 Jul 2026 ANTT: EPR Participações S.A. wins competitive process for Autopista Régis Bittencourt (BR-116/SP/PR, 383 km); contract contemplates estimated investments of R$7.2 billion through 2041. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1386.72m.",
    "7200000000", BRL_FX_DATE, "2026", "", "",
    "BR-116/SP/PR Régis Bittencourt corridor (official geography; no single pin).",
    "antt_epr_regis_bittencourt_20260723",
    "o contrato prevê investimentos estimados em R$ 7,2 bilhões destinados à ampliação da capacidade da rodovia, recuperação da infraestrutura e prestação dos serviços previstos no edital",
    "https://www.gov.br/antt/pt-br/assuntos/noticias-defeso-eleitoral/epr-vence-o-leilao-da-concessao-da-regis-bittencourt-com-desagio-de-22-53",
    "Actor: EPR Participações S.A. (Brazilian) — other. CapEx-fill: retain R$7.2bn; add Fed H.10 Sep 25 2026 FX to USD ~1386.72m. Shuffle bridges_roads.",
    "hunt_cycle234", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(7200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ANTT. “EPR vence o leilão da concessão da Régis Bittencourt com deságio de 22,53%.” July 23, 2026. https://www.gov.br/antt/pt-br/assuntos/noticias-defeso-eleitoral/epr-vence-o-leilao-da-concessao-da-regis-bittencourt-com-desagio-de-22-53.',
    annotation="EPR Régis Bittencourt CapEx-fill ~USD 1386.72m via Fed H.10. Supports epr_regis_bittencourt_7p2bn_2026.",
    evid_note="Opened ANTT Portuguese; R$7.2bn estimated investments / 22.53% discount confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. bridges_roads / prc — CapEx-fill CSCEC Litoral Pacífico Fase 2 RMB ~1.805bn
row_doc(
    "cscec_litoral_pacifico_fase2_nicaragua_2024",
    "infrastructure", "bridges_roads", "prc",
    "CSCEC — Carretera Litoral Pacífico Fase 2 credit facilities",
    "Nicaragua",
    "28 Jun 2024 credit facilities approved by Asamblea Nacional Decreto A.N. Nº 8885 (14 Aug 2024): CSCEC International Construction extends total RMB 1,804,754,237.15 to Nicaragua MHCP for Litoral Pacífico Fase 2 (Masachapa–Puente La Gloria–Puerto Sandino). CapEx-fill: Fed H.10 Sep 25 2026 China Yuan 6.7110 → USD ~268.92m.",
    "1804754237.15", CNY_FX_DATE, "2024", "11.790", "-86.510",
    "Litoral Pacífico Fase 2 Masachapa–Puerto Sandino (decree geography).",
    "asamblea_cscec_litoral_fase2_decreto_8885_2024",
    "Apruébese el Acuerdo de Facilidad de Crédito Tramo I: Est. 0+000 (Masachapa) a Est. 49+500 (Puente La Gloria) por un monto de RMB 918,896,364.95 … y Acuerdo de Facilidad de Crédito Tramo II",
    "http://legislacion.asamblea.gob.ni/normaweb.nsf/9e314815a08d4a6206257265005d21f9/fa84bfd254ad2a9c06258b7b0063a04e?OpenDocument",
    "Actor: CSCEC International Construction (PRC) — prc. CapEx-fill: retain RMB 1,804,754,237.15; add Fed H.10 Sep 25 2026 FX to USD ~268.92m. Shuffle bridges_roads / PRC equal-budget.",
    "hunt_cycle234", investment_type="export_credit", evidence="documented", currency="CNY",
    value_usd=str(round(1804754237.15 / float(CNY_USD), 2)), fx_usd=CNY_USD, bib_type="gov",
    chicago='Asamblea Nacional de Nicaragua. “Decreto A.N. Nº 8885 — Facilidades de crédito CSCEC Litoral Pacífico Fase 2.” August 14, 2024. http://legislacion.asamblea.gob.ni/normaweb.nsf/9e314815a08d4a6206257265005d21f9/fa84bfd254ad2a9c06258b7b0063a04e?OpenDocument.',
    annotation="CSCEC Litoral Pacífico Fase 2 CapEx-fill ~USD 268.92m via Fed H.10. Supports cscec_litoral_pacifico_fase2_nicaragua_2024.",
    evid_note="Opened Asamblea decree Spanish; RMB 1,804,754,237.15 CSCEC Fase 2 facilities confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 6.7110 CNY/USD.",
)

# 6. copper / prc — CapEx-fill Jiangxi Copper SolGold Cascabel ~GBP 867m
row_doc(
    "jiangxi_copper_solgold_cascabel_2026",
    "resources", "copper", "prc",
    "Jiangxi Copper — SolGold Cascabel / Alpala acquisition",
    "Ecuador",
    "4 Mar 2026: Jiangxi Copper (Hong Kong) Investment Company Limited scheme of arrangement becomes effective — acquires entire issued share capital of SolGold plc (Cascabel / Alpala Cu-Au, Imbabura). Recommended cash offer implies equity value approximately GBP 867 million. CapEx-fill: Fed H.10 Sep 25 2026 GBP 1.3250 → USD ~1148.78m.",
    "867000000", GBP_FX_DATE, "2026", "0.50", "-78.50",
    "Cascabel / Alpala deposit, Imbabura (company geography).",
    "jiangxi_solgold_effective_20260305",
    "the Offer has become effective on the day of submission. The core asset of the Target Company, the Alpala deposit of Cascabel Project, has completed a pre-feasibility study.",
    "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0305/2026030500033.pdf",
    "Actor: Jiangxi Copper (PRC) — prc. CapEx-fill: retain ~GBP 867m equity value; add Fed H.10 Sep 25 2026 FX to USD ~1148.78m. Shuffle copper / PRC equal-budget.",
    "hunt_cycle234", investment_type="acquisition", evidence="documented", currency="GBP",
    value_usd=str(round(867000000 * float(GBP_USD), 2)), fx_usd=GBP_USD,
    chicago='Jiangxi Copper Company Limited. “Announcement — SolGold plc scheme of arrangement becomes effective.” March 5, 2026. https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0305/2026030500033.pdf.',
    annotation="Jiangxi Cascabel CapEx-fill ~USD 1148.78m via Fed H.10. Supports jiangxi_copper_solgold_cascabel_2026.",
    evid_note="Opened HKEX English; SolGold scheme effective / Cascabel Alpala confirmed; retain stored GBP 867m. CapEx-fill USD via Fed H.10 Sep 25 2026 1.3250 USD/GBP.",
)

# 7. copper / allied — CapEx-fill Fortescue Alta Copper ~CAD 139m
row_doc(
    "fortescue_canariaco_alta_copper_2026",
    "resources", "copper", "allied",
    "Fortescue — Alta Copper / Cañariaco acquisition",
    "Peru",
    "10 Mar 2026 Fortescue ASX: Nascent Exploration Pty Ltd completes Plan of Arrangement acquiring all Alta Copper Corp. shares; cash C$1.40/share implying total equity value approximately C$139 million; Fortescue now 100% of Cañariaco copper project. CapEx-fill: Fed H.10 Sep 25 2026 Canada dollar 1.4140 → USD ~98.30m.",
    "139000000", CAD_FX_DATE, "2026", "-6.05", "-79.25",
    "Cañariaco copper project, Lambayeque (company geography).",
    "fortescue_alta_copper_asx_20260310",
    "Alta Copper shareholders received cash consideration of C$1.40 per share, implying a total equity value of approximately C$139 million.",
    "https://content.fortescue.com/fortescue17114-fortescueeb60-productionbbdb-8be5/media/project/fortescueportal/shared/documents/regulatory/asx-announcements/automated/03066248-fortescue-completes-acquisition-of-alta-copper.pdf",
    "Actor: Fortescue (Australia) — allied. CapEx-fill: retain ~CAD 139m equity value; add Fed H.10 Sep 25 2026 FX to USD ~98.30m. Shuffle copper.",
    "hunt_cycle234", investment_type="acquisition", evidence="documented", currency="CAD",
    value_usd=str(round(139000000 / float(CAD_USD), 2)), fx_usd=CAD_USD,
    chicago='Fortescue. “Fortescue completes acquisition of Alta Copper.” March 10, 2026. https://content.fortescue.com/fortescue17114-fortescueeb60-productionbbdb-8be5/media/project/fortescueportal/shared/documents/regulatory/asx-announcements/automated/03066248-fortescue-completes-acquisition-of-alta-copper.pdf.',
    annotation="Fortescue Cañariaco CapEx-fill ~USD 98.30m via Fed H.10. Supports fortescue_canariaco_alta_copper_2026.",
    evid_note="Opened Fortescue ASX PDF; C$139m equity value / Cañariaco 100% confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.4140 CAD/USD.",
)

# 8. copper / allied — CapEx-fill Sandvik CoMinVi Mexico ~SEK 340m
row_doc(
    "sandvik_cominvi_mexico_sek340m_2026",
    "resources", "copper", "allied",
    "Sandvik — CoMinVi Mexico underground fleet (~SEK 340m)",
    "Mexico",
    "3 Jul 2026 Sandvik AB: large underground equipment order from Constructora Minera Villagómez (CoMinVi) for several Mexico contract sites; valued around SEK 340 million, booked Q2 2026. CapEx-fill: Fed H.10 Sep 25 2026 Sweden krona 9.9047 → USD ~34.33m. Multi-site — lat/lon blank.",
    "340000000", SEK_FX_DATE, "2026", "", "",
    "Multiple CoMinVi Mexico contract sites (company; no single pin).",
    "sandvik_cominvi_mexico_20260703",
    "Sandvik has received a large underground equipment order from the Mexico-based mining contractor Constructora Minera Villagómez S.A. de C.V. (CoMinVi), for use at several of its contract sites across Mexico. The order is valued at around SEK 340 million",
    "https://www.home.sandvik/en/news-and-media/news/2026/07/sandvik-wins-large-underground-equipment-order-in-mexico-from-mining-contractor-cominvi/",
    "Actor: Sandvik (Sweden) — allied. CapEx-fill: retain ~SEK 340m; add Fed H.10 Sep 25 2026 FX to USD ~34.33m. Shuffle copper.",
    "hunt_cycle234", investment_type="equipment_supply", evidence="documented", currency="SEK",
    value_usd=str(round(340000000 / float(SEK_USD), 2)), fx_usd=SEK_USD,
    chicago='Sandvik. “Sandvik wins large underground equipment order in Mexico from mining contractor CoMinVi.” July 3, 2026. https://www.home.sandvik/en/news-and-media/news/2026/07/sandvik-wins-large-underground-equipment-order-in-mexico-from-mining-contractor-cominvi/.',
    annotation="Sandvik CoMinVi CapEx-fill ~USD 34.33m via Fed H.10. Supports sandvik_cominvi_mexico_sek340m_2026.",
    evid_note="Opened Sandvik English; ~SEK 340m / CoMinVi Mexico confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 9.9047 SEK/USD.",
)

# 9. copper / allied — CapEx-fill Epiroc Peru Pit Viper ~SEK 210m
row_doc(
    "epiroc_peru_pit_viper_sek210m_2026",
    "resources", "copper", "allied",
    "Epiroc — Peru copper mine Pit Viper 351 fleet (~SEK 210m)",
    "Peru",
    "15 Jul 2026 Epiroc: large order for Pit Viper 351 surface blasthole drill rigs for a major Peru copper mine; valued around SEK 210 million, booked Q2 2026. CapEx-fill: Fed H.10 Sep 25 2026 Sweden krona 9.9047 → USD ~21.20m. Mine unnamed — lat/lon blank.",
    "210000000", SEK_FX_DATE, "2026", "", "",
    "Unnamed major Peru copper mine (company; no pin).",
    "epiroc_peru_pit_viper_20260715",
    "Epiroc AB… has won a large order for mining equipment for a major copper mine in Peru. The Peruvian mine is operated by a consortium comprising leading Chinese investment companies and a globally recognized mining company headquartered in Australia, which also serves as the mine operator. The customer ordered a fleet of Pit Viper 351 surface blasthole drill rigs that will support the mine’s expansion… The equipment order is valued at around SEK 210 million and was booked in the second quarter 2026.",
    "https://www.epirocgroup.com/en/media/corporate-press-releases/2026/20260715-epiroc-wins-large-order-for-mining-equipment-in-peru",
    "Actor: Epiroc (Sweden) — allied. CapEx-fill: retain ~SEK 210m; add Fed H.10 Sep 25 2026 FX to USD ~21.20m. Shuffle copper.",
    "hunt_cycle234", investment_type="equipment_supply", evidence="documented", currency="SEK",
    value_usd=str(round(210000000 / float(SEK_USD), 2)), fx_usd=SEK_USD,
    chicago='Epiroc. “Epiroc wins large order for mining equipment in Peru.” July 15, 2026. https://www.epirocgroup.com/en/media/corporate-press-releases/2026/20260715-epiroc-wins-large-order-for-mining-equipment-in-peru.',
    annotation="Epiroc Peru Pit Viper CapEx-fill ~USD 21.20m via Fed H.10. Supports epiroc_peru_pit_viper_sek210m_2026.",
    evid_note="Opened Epiroc English; ~SEK 210m / Peru copper mine Pit Viper order confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 9.9047 SEK/USD.",
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
    added, updated = [], []
    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k != "id" and v != "" and v is not None:
                    existing[k] = v
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
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
    print(f"cycle234 added {len(added)}: {added}")
    print(f"cycle234 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
