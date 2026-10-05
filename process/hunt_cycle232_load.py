#!/usr/bin/env python3
"""Cycle 232 hunt: shuffle_seed=20261232; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261232).shuffle):
port_ownership, building_materials, copper, rail, balsa, engineering_epc, bridges_roads,
port_cranes, fission_smr, lithium, niobium, graphite, other_renewables, nickel, solar,
water, wind, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; 0 new US CapEx — honest residual).
PRC equal-budget: CRRC México–Pachuca CapEx-fill; holdovers unsigned.
Huaxin–CSN bid skipped (pre-close M&A).
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
MXN_USD = "17.6932"
MXN_FX_DATE = "2026-09-25"
EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"


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


# 1. rail / other — CapEx-fill Metro SP Linha 17 Phase 1 R$5.9bn
row_doc(
    "metro_sp_linha17_phase1_5p9bn_brl_2026",
    "infrastructure", "rail", "other",
    "São Paulo Metro — Linha 17-Ouro Phase 1",
    "Brazil",
    "30 Jun 2026 Prefeitura SP: Phase 1 of Linha 17-Ouro completed/inaugurated with investment of R$ 5.9 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1136.34m.",
    "5900000000", BRL_FX_DATE, "2026", "-23.63", "-46.70",
    "Linha 17-Ouro, São Paulo (official geography).",
    "prefeitura_sp_linha17_20260630",
    "Com investimento de R$ 5,9 bilhões na primeira etapa da Linha 17-Ouro, a nova estação acrescenta cerca de 800 metros ao sistema",
    "https://prefeitura.sp.gov.br/web/sampa-news/w/primeira-fase-da-linha-17-ouro-%C3%A9-conclu%C3%ADda-com-inaugura%C3%A7%C3%A3o",
    "Actor: São Paulo Metro / Prefeitura (host) — other. CapEx-fill: retain R$5.9bn Phase 1; add Fed H.10 Sep 25 2026 FX to USD ~1136.34m. Shuffle rail.",
    "hunt_cycle232", investment_type="greenfield_rail", evidence="documented", currency="BRL",
    value_usd=str(round(5900000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Prefeitura de São Paulo. “Primeira fase da Linha 17-Ouro é concluída com inauguração.” June 30, 2026. https://prefeitura.sp.gov.br/web/sampa-news/w/primeira-fase-da-linha-17-ouro-%C3%A9-conclu%C3%ADda-com-inaugura%C3%A7%C3%A3o.',
    annotation="Metro SP Linha 17 CapEx-fill ~USD 1136.34m via Fed H.10. Supports metro_sp_linha17_phase1_5p9bn_brl_2026.",
    evid_note="Opened Prefeitura SP Portuguese; R$5.9bn Phase 1 Linha 17-Ouro confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. rail / allied — CapEx-fill FCC/CICSA Saltillo–Santa Catarina MXN 31.844bn
row_doc(
    "fcc_cicsa_saltillo_santa_catarina_2025",
    "infrastructure", "rail", "allied",
    "FCC Construcción / CICSA — Saltillo–Santa Catarina passenger rail (Seg. 13–14)",
    "Mexico",
    "15 Sep 2025 Grupo Carso: SICT/ARTF awards CICSA–FCC Construcción consortium MXN 31,844 million (incl. 16% VAT) for construction/design of 111 km Saltillo–Santa Catarina (Saltillo–Nuevo Laredo segments 13–14); 50/50; 960 calendar days from 30 Sep. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~1799.79m.",
    "31844000000", MXN_FX_DATE, "2025", "25.43", "-101.00",
    "Saltillo–Santa Catarina passenger rail segments 13–14 (company geography).",
    "carso_fcc_saltillo_santa_catarina_20250915",
    "adjudicó al consorcio conformado por su subsidiaria Operadora Cicsa, S.A. de C.V. (CICSA) y la empresa FCC Construcción, S.A. (FCC), un contrato … por un monto de $31,844 millones de pesos incluyendo el 16% de IVA",
    "https://www.carso.com.mx/contrato-de-construccion-y-diseno-tren-de-pasajeros-segmentos-13-14-saltillo-santa-catarina/",
    "Actor: FCC Construcción (Spain) 50% with CICSA — allied (FCC). CapEx-fill: retain MXN 31.844bn incl. VAT; add Fed H.10 Sep 25 2026 FX to USD ~1799.79m. Shuffle rail.",
    "hunt_cycle232", investment_type="epc", evidence="documented", currency="MXN",
    value_usd=str(round(31844000000 / float(MXN_USD), 2)), fx_usd=MXN_USD,
    chicago='Grupo Carso. “Contrato de construcción y diseño tren de pasajeros segmentos 13-14 Saltillo-Santa Catarina.” September 15, 2025. https://www.carso.com.mx/contrato-de-construccion-y-diseno-tren-de-pasajeros-segmentos-13-14-saltillo-santa-catarina/.',
    annotation="FCC/CICSA Saltillo CapEx-fill ~USD 1799.79m via Fed H.10. Supports fcc_cicsa_saltillo_santa_catarina_2025.",
    evid_note="Opened Carso Spanish; MXN 31,844m incl. VAT / CICSA–FCC 50/50 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 3. rail / allied — CapEx-fill COMSA Querétaro–Irapuato Tramo 3 MXN 3.412bn
row_doc(
    "comsa_qi_tramo3_3411p8m_mxn_2026",
    "infrastructure", "rail", "allied",
    "COMSA consortium — Querétaro–Irapuato Tramo 3",
    "Mexico",
    "15 Feb 2026 El Economista: COMSA / COMSA Infraestructuras / Recsa / Vise consortium wins Tramo 3 of Tren Querétaro–Irapuato; stored face MXN 3,411.8 million. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~192.83m.",
    "3411800000", MXN_FX_DATE, "2026", "20.52", "-100.81",
    "Querétaro–Irapuato Tramo 3 (press geography).",
    "eleconomista_comsa_qi_t3_20260215",
    "El consorcio integrado por COMSA, COMSA Infraestructuras, Regiomontana de Construcción y Servicios (Recsa) y Vise ganó … el contrato",
    "https://www.eleconomista.com.mx/empresas/consorcio-comsa-gana-tramo-3-tren-queretaro-irapuato-20260215-800027.html",
    "Actor: COMSA (Spain) consortium — allied. CapEx-fill: retain MXN 3.4118bn; add Fed H.10 Sep 25 2026 FX to USD ~192.83m. Shuffle rail.",
    "hunt_cycle232", investment_type="rail_epc", evidence="documented", currency="MXN",
    value_usd=str(round(3411800000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='El Economista. “Consorcio COMSA gana Tramo 3 del tren Querétaro–Irapuato.” February 15, 2026. https://www.eleconomista.com.mx/empresas/consorcio-comsa-gana-tramo-3-tren-queretaro-irapuato-20260215-800027.html.',
    annotation="COMSA QI Tramo 3 CapEx-fill ~USD 192.83m via Fed H.10. Supports comsa_qi_tramo3_3411p8m_mxn_2026.",
    evid_note="Opened El Economista Spanish; COMSA consortium / stored MXN 3.4118bn CapEx-filled via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 4. rail / prc — CapEx-fill CRRC México–Pachuca MXN ~5.846bn
row_doc(
    "crrc_mexico_pachuca_trains_2025",
    "infrastructure", "rail", "prc",
    "CRRC Zhuzhou — 15 electric trains México–Pachuca",
    "Mexico",
    "12 Sep 2025 El Financiero: CRRC Zhuzhou Locomotive wins contract to supply 15 electric trains for México–Pachuca route; stored adjudicated face MXN 5,846,410,431.88. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~330.43m. UNVERIFIED proxy press.",
    "5846410431.88", MXN_FX_DATE, "2025", "19.85", "-98.95",
    "México–Pachuca passenger rail (press geography).",
    "elfinanciero_crrc_pachuca_20250912",
    "CRRC Zhuzhou Locomotive … ganó el contrato para suministrar 15 trenes eléctricos para la ruta México-Pachuca … el contrato adjudicado",
    "https://www.elfinanciero.com.mx/empresas/2025/09/12/china-mete-las-manos-en-la-obra-mexico-pachuca-crrc-zhuzhou-locomotive/",
    "Actor: CRRC Zhuzhou (PRC) — prc. CapEx-fill: retain stored MXN ~5.846bn; add Fed H.10 Sep 25 2026 FX to USD ~330.43m. Shuffle rail.",
    "hunt_cycle232", investment_type="equipment_supply", evidence="proxy", currency="MXN",
    value_usd=str(round(5846410431.88 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='El Financiero. “China mete las manos en la obra México-Pachuca: CRRC Zhuzhou Locomotive.” September 12, 2025. https://www.elfinanciero.com.mx/empresas/2025/09/12/china-mete-las-manos-en-la-obra-mexico-pachuca-crrc-zhuzhou-locomotive/.',
    annotation="CRRC Pachuca CapEx-fill ~USD 330.43m via Fed H.10 (proxy). Supports crrc_mexico_pachuca_trains_2025.",
    evid_note="Opened El Financiero Spanish; CRRC 15 trains / stored MXN ~5.846bn CapEx-filled via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 5. bridges_roads / other — CapEx-fill Ecorodovias Rota das Gerais >R$13bn
row_doc(
    "ecorodovias_rota_gerais_13bn_2026",
    "infrastructure", "bridges_roads", "other",
    "Ecorodovias — Rota das Gerais federal highway concession",
    "Brazil",
    "31 Mar 2026 ANTT: Ecorodovias wins first 2026 federal highway auction for Rota das Gerais (BR-116/251/MG); 30-year contract with more than R$ 13 billion in investments. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~2503.80m for stored R$13bn floor.",
    "13000000000", BRL_FX_DATE, "2026", "-16.72", "-43.86",
    "Rota das Gerais BR-116/251/MG (official geography).",
    "antt_rota_gerais_20260331",
    "Com prazo de 30 anos, o contrato prevê mais de R$ 13 bilhões em investimentos, concentrados nos primeiros anos, antecipando benefícios à população",
    "https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/ecorodovias-vence-primeiro-leilao-rodoviario-federal-de-2026-com-a-rota-das-gerais",
    "Actor: Ecorodovias (Brazilian) — other. CapEx-fill: retain >R$13bn floor; add Fed H.10 Sep 25 2026 FX to USD ~2503.80m. Shuffle bridges_roads.",
    "hunt_cycle232", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(13000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ANTT. “Ecorodovias vence primeiro leilão rodoviário federal de 2026 com a Rota das Gerais.” March 31, 2026. https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/ecorodovias-vence-primeiro-leilao-rodoviario-federal-de-2026-com-a-rota-das-gerais.',
    annotation="Ecorodovias Rota das Gerais CapEx-fill ~USD 2503.80m via Fed H.10. Supports ecorodovias_rota_gerais_13bn_2026.",
    evid_note="Opened ANTT Portuguese; >R$13bn / 30-year Rota das Gerais confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. bridges_roads / other — CapEx-fill DNIT Porto Murtinho access R$472m
row_doc(
    "dnit_porto_murtinho_access_472m_brl_2025",
    "infrastructure", "bridges_roads", "other",
    "DNIT — Porto Murtinho access to Brazil–Paraguay international bridge",
    "Brazil",
    "19 Sep 2025 DNIT: access works to international bridge at Porto Murtinho (MS) with federal investment of approximately R$ 472 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~90.91m.",
    "472000000", BRL_FX_DATE, "2025", "-21.70", "-57.88",
    "Porto Murtinho, Mato Grosso do Sul (official geography).",
    "dnit_porto_murtinho_access_20250919",
    "O empreendimento conta com investimento do governo federal de aproximadamente R$ 472 milhões.",
    "https://www.gov.br/dnit/pt-br/assuntos/noticias/em-porto-murtinho-ms-avancam-as-obras-do-acesso-a-ponte-internacional-binacional",
    "Actor: DNIT (Brazil federal) — other. CapEx-fill: retain ~R$472m; add Fed H.10 Sep 25 2026 FX to USD ~90.91m. Shuffle bridges_roads.",
    "hunt_cycle232", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(472000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='DNIT. “Em Porto Murtinho (MS) avançam as obras do acesso à ponte internacional binacional.” September 19, 2025. https://www.gov.br/dnit/pt-br/assuntos/noticias/em-porto-murtinho-ms-avancam-as-obras-do-acesso-a-ponte-internacional-binacional.',
    annotation="DNIT Porto Murtinho CapEx-fill ~USD 90.91m via Fed H.10. Supports dnit_porto_murtinho_access_472m_brl_2025.",
    evid_note="Opened DNIT Portuguese; ~R$472m Porto Murtinho access confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. water / allied — CapEx-fill ACCIONA Los Cabos EUR 134.5m
row_doc(
    "acciona_los_cabos_desal_mexico",
    "resources", "water", "allied",
    "ACCIONA — Los Cabos seawater RO desalination plant",
    "Mexico",
    "14 May 2021 ACCIONA: build-and-operate Los Cabos desalination plant; overall budget €134.5 million; 250 l/s; 25-year PPP O&M. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD ~153.33m.",
    "134500000", EUR_FX_DATE, "2021", "22.89", "-109.91",
    "Los Cabos, Baja California Sur (company geography).",
    "acciona_los_cabos_desal_page",
    "ACCIONA will build and operate a desalination plant in the municipality of Los Cabos, in Baja California (Mexico). The project has an overall budget of €134.5 million.",
    "https://www.acciona.com/updates/news/acciona-build-operate-cabos-desalination-plant-mexico",
    "Actor: ACCIONA (Spain) — allied. CapEx-fill: retain EUR 134.5m; add Fed H.10 Sep 25 2026 FX to USD ~153.33m. Shuffle water.",
    "hunt_cycle232", investment_type="concession", evidence="documented", currency="EUR",
    value_usd=str(round(134500000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='ACCIONA. “ACCIONA to build and operate Los Cabos desalination plant in Mexico.” May 14, 2021. https://www.acciona.com/updates/news/acciona-build-operate-cabos-desalination-plant-mexico.',
    annotation="ACCIONA Los Cabos CapEx-fill ~USD 153.33m via Fed H.10. Supports acciona_los_cabos_desal_mexico.",
    evid_note="Opened ACCIONA English; EUR 134.5m / 250 l/s / 25-year PPP confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 8. power_plants_grid / allied — CapEx-fill Neoenergia Brasília R$3.1bn
row_doc(
    "neoenergia_brasilia_3p1bn_brl_2026_2030",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Brasília — DF distribution CapEx plan R$3.1bn (2026–2030)",
    "Brazil",
    "6 Aug 2026 Neoenergia: De 2026 até 2030, serão aplicados R$ 3,1 bilhões in DF distribution expansion/modernization/digitalization. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~597.06m. Distinct from neoenergia_dist_50bn_brl_2026_2030 national cycle.",
    "3100000000", BRL_FX_DATE, "2026", "-15.78", "-47.93",
    "Distrito Federal distribution footprint (Brasília pin).",
    "neoenergia_brasilia_3p1bn_20260806",
    "De 2026 até 2030, serão aplicados R$ 3,1 bilhões em obras de expansão, modernização e digitalização da rede de distribuição de energia.",
    "https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df",
    "Actor: Neoenergia Brasília (Iberdrola) — allied. CapEx-fill: retain R$3.1bn DF plan; add Fed H.10 Sep 25 2026 FX to USD ~597.06m. Shuffle power_plants_grid.",
    "hunt_cycle232", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(3100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Neoenergia. “Neoenergia anuncia plano recorde de R$ 3,1 bilhões para fortalecer a infraestrutura elétrica do DF.” August 6, 2026. https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df.',
    annotation="Neoenergia Brasília CapEx-fill ~USD 597.06m via Fed H.10. Supports neoenergia_brasilia_3p1bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Portuguese; R$3.1bn 2026–2030 DF plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 9. power_plants_grid / allied — CapEx-fill Neoenergia Coelba litoral >R$7bn
row_doc(
    "neoenergia_coelba_litoral_7bn_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Coelba — Bahia litoral grid package (>R$7bn)",
    "Brazil",
    "8 May 2026 Neoenergia: Bahia litoral package of more than R$ 7 billion — 18 new substations + modernization/expansion of 10 units. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1348.19m for stored R$7bn floor. Nested within neoenergia_dist_50bn cycle but distinct coastal package row.",
    "7000000000", BRL_FX_DATE, "2026", "-12.97", "-38.51",
    "Neoenergia Coelba Bahia litoral (Salvador pin).",
    "neoenergia_50bn_dist_20260508",
    "O projeto, de mais de R$ 7 bilhões, contempla a implantação de 18 novas subestações e a modernização e ampliação de outras 10 unidades",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia Coelba (Iberdrola) — allied. CapEx-fill: retain >R$7bn floor; add Fed H.10 Sep 25 2026 FX to USD ~1348.19m. Shuffle power_plants_grid.",
    "hunt_cycle232", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(7000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia Coelba litoral CapEx-fill ~USD 1348.19m via Fed H.10. Supports neoenergia_coelba_litoral_7bn_brl_2026.",
    evid_note="Opened Neoenergia Portuguese; >R$7bn Bahia litoral package confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle232 added {len(added)}: {added}")
    print(f"cycle232 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
