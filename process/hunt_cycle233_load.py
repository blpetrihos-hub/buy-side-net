#!/usr/bin/env python3
"""Cycle 233 hunt: shuffle_seed=20261233; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261233).shuffle):
engineering_epc, niobium, lithium, rail, fission_smr, power_plants_grid, balsa, wind,
nickel, bridges_roads, graphite, water, building_materials, copper, other_renewables,
solar, port_ownership, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; 0 new US CapEx — honest residual).
PRC equal-budget: CDB–BNDES RMB 5bn CapEx-fill; holdovers unsigned.
Huaxin–CSN / Aldesa EUR solar / RAP-as-CapEx / COP-CLP-PEN (no Fed H.10) skipped.
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
EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"
CNY_USD = "6.7110"
CNY_FX_DATE = "2026-09-25"
JPY_USD = "157.1800"
JPY_FX_DATE = "2026-09-25"


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


# 1. engineering_epc / prc — CapEx-fill CDB–BNDES RMB 5bn
row_doc(
    "cdb_bndes_rmb5bn_2024",
    "infrastructure", "engineering_epc", "prc",
    "China Development Bank — BNDES RMB 5bn loan facility",
    "Brazil",
    "Nov 2024 (Xi Jinping Brazil state visit outcomes list): China Development Bank and BNDES sign a RMB 5 billion loan agreement — first BNDES borrowing in renminbi — to deepen China–Brazil development-finance cooperation supporting infrastructure and related sectors. CapEx-fill: Fed H.10 Sep 25 2026 China Yuan 6.7110 → USD ~745.05m.",
    "5000000000", CNY_FX_DATE, "2024", "", "",
    "Brazil national development-finance facility (no single site pin).",
    "cdb_bndes_rmb5bn_20241128",
    "中国国开行与巴西开发银行日前签署的50亿元人民币贷款协议，纳入了此次习近平主席对巴西国事访问成果文件清单。",
    "https://www.cdb.com.cn/ep/202411/t20241128_12218.html",
    "Actor: China Development Bank (PRC policy bank) — prc. CapEx-fill: retain RMB 5bn; add Fed H.10 Sep 25 2026 FX to USD ~745.05m. Shuffle engineering_epc / PRC equal-budget.",
    "hunt_cycle233", investment_type="development_finance", evidence="documented", currency="CNY",
    value_usd=str(round(5000000000 / float(CNY_USD), 2)), fx_usd=CNY_USD,
    chicago='China Development Bank. “中国国开行与巴西开发银行签署50亿元人民币贷款协议.” November 28, 2024. https://www.cdb.com.cn/ep/202411/t20241128_12218.html.',
    annotation="CDB–BNDES RMB 5bn CapEx-fill ~USD 745.05m via Fed H.10. Supports cdb_bndes_rmb5bn_2024.",
    evid_note="Opened CDB Chinese; RMB 5bn BNDES loan in Xi visit outcomes confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 6.7110 CNY/USD.",
)

# 2. rail / allied — CapEx-fill CAF Medellín + Santiago >EUR 200m
row_doc(
    "caf_medellin_santiago_metro_2024",
    "infrastructure", "rail", "allied",
    "CAF — Medellín metro INNEO + Santiago Line 6 trains",
    "Colombia",
    "9 Dec 2024 CAF: combined contracts exceeding €200 million — 13 three-car INNEO metro trains for Medellín Lines A/B plus 6 five-car GoA4 units for Santiago Line 6 extensions. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD 228.00m for stored EUR 200m floor. Multi-country award pin at Medellín.",
    "200000000", EUR_FX_DATE, "2024", "6.25", "-75.57",
    "Medellín Metro Lines A/B (company geography; Santiago portion co-awarded).",
    "caf_medellin_santiago_20241209",
    "CAF has secured two new contracts to supply metro units based on its INNEO platform. The company will manufacture 13 units for the Medellín Metro and 6 units for the Santiago de Chile metro. The combined contracts exceed €200 million.",
    "https://www.cafmobility.com/en/press-room/caf-to-supply-metro-units-colombia-and-chile/",
    "Actor: CAF (Spain) — allied. CapEx-fill: retain >EUR 200m floor; add Fed H.10 Sep 25 2026 FX to USD 228.00m. Shuffle rail.",
    "hunt_cycle233", investment_type="equipment_supply", evidence="documented", currency="EUR",
    value_usd=str(round(200000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='CAF. “CAF to supply metro units to Colombia and Chile.” December 9, 2024. https://www.cafmobility.com/en/press-room/caf-to-supply-metro-units-colombia-and-chile/.',
    annotation="CAF Medellín/Santiago CapEx-fill USD 228.00m via Fed H.10. Supports caf_medellin_santiago_metro_2024.",
    evid_note="Opened CAF English; >EUR 200m / 13 Medellín + 6 Santiago units confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 3. rail / allied — CapEx-fill CAF Trivia SP maintenance ~EUR 500m
row_doc(
    "caf_trivia_sp_maint_2025",
    "infrastructure", "rail", "allied",
    "CAF — Trivia Trens São Paulo 24-year maintenance (~EUR 500m)",
    "Brazil",
    "20 Nov 2025 CAF: 24-year comprehensive maintenance contract with Trivia Trens S.A. (Comporte) for 107 electric trains on Lines 11-Coral, 12-Safira, 13-Jade; valued at approximately EUR 500 million. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD 570.00m.",
    "500000000", EUR_FX_DATE, "2025", "-23.55", "-46.63",
    "São Paulo CPTM Lines 11/12/13 (company geography).",
    "caf_trivia_maint_20251120",
    "CAF has signed a contract with Trivia Trens S.A. … for the comprehensive maintenance of 107 electric trains. … The 24-year contract is valued at approximately EUR500 million",
    "https://www.cafmobility.com/en/press-room/caf-awarded-maintenance-of-rains-operating-on-s%C3%A3o-paulo-commuter-lines/",
    "Actor: CAF (Spain) — allied. CapEx-fill: retain ~EUR 500m; add Fed H.10 Sep 25 2026 FX to USD 570.00m. Shuffle rail.",
    "hunt_cycle233", investment_type="maintenance_contract", evidence="documented", currency="EUR",
    value_usd=str(round(500000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='CAF. “CAF awarded maintenance of trains operating on São Paulo commuter lines.” November 20, 2025. https://www.cafmobility.com/en/press-room/caf-awarded-maintenance-of-rains-operating-on-s%C3%A3o-paulo-commuter-lines/.',
    annotation="CAF Trivia SP CapEx-fill USD 570.00m via Fed H.10. Supports caf_trivia_sp_maint_2025.",
    evid_note="Opened CAF English; ~EUR 500m / 107 trains / 24-year Trivia contract confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 4. rail / allied — CapEx-fill Alstom Salvador metro 10 trains R$632.7m
row_doc(
    "alstom_salvador_metro_10trains_632p7m_2026",
    "infrastructure", "rail", "allied",
    "Alstom — Salvador metro 10 four-car trains (R$632.7m)",
    "Brazil",
    "21–22 Sep 2026: CTB homologates Consórcio Grupo Alstom as supplier of 10 four-car trains for Sistema Metroviário de Salvador e Lauro de Freitas Lines 1–2 at R$632,719,519.37. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~121.86m.",
    "632719519.37", BRL_FX_DATE, "2026", "-12.97", "-38.51",
    "Salvador–Lauro de Freitas metro (press geography).",
    "g1_alstom_salvador_metro_20260922",
    "Serão investidos R$ 632.719.519,37 para a aquisição dos veículos.",
    "https://g1.globo.com/ba/bahia/noticia/2026/09/22/empresa-vence-licitacao-para-fornecimento-de-trens-para-metro-de-salvador-e-lauro-de-freitas.ghtml",
    "Actor: Alstom (France) Consórcio Grupo Alstom — allied. CapEx-fill: retain R$632.72m; add Fed H.10 Sep 25 2026 FX to USD ~121.86m. Shuffle rail.",
    "hunt_cycle233", investment_type="equipment_supply", evidence="proxy", currency="BRL",
    value_usd=str(round(632719519.37 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='G1 Bahia. “Empresa vence licitação para fornecimento de trens para metrô de Salvador e Lauro de Freitas.” September 22, 2026. https://g1.globo.com/ba/bahia/noticia/2026/09/22/empresa-vence-licitacao-para-fornecimento-de-trens-para-metro-de-salvador-e-lauro-de-freitas.ghtml.',
    annotation="Alstom Salvador CapEx-fill ~USD 121.86m via Fed H.10 (proxy). Supports alstom_salvador_metro_10trains_632p7m_2026.",
    evid_note="Opened G1 Portuguese; R$632,719,519.37 / 10 trains / Consórcio Grupo Alstom confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. power_plants_grid / allied — CapEx-fill Neoenergia Ilhabela R$200m
row_doc(
    "neoenergia_ilhabela_200m_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Elektro — Ilhabela substation + undersea/underground line (R$200m)",
    "Brazil",
    "8 May 2026 Neoenergia (within Elektro concession renewal package): named Ilhabela project with R$ 200 million investment for a new substation and underground/subaquatic transmission line. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~38.52m.",
    "200000000", BRL_FX_DATE, "2026", "-23.78", "-45.36",
    "Ilhabela, São Paulo (company geography).",
    "neoenergia_50bn_dist_20260508",
    "Com um investimento de R$ 200 milhões, está prevista a construção de uma nova subestação e de uma linha de transmissão subterrânea e subaquática",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia Elektro (Iberdrola) — allied. CapEx-fill: retain R$200m; add Fed H.10 Sep 25 2026 FX to USD ~38.52m. Shuffle power_plants_grid.",
    "hunt_cycle233", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia Ilhabela CapEx-fill ~USD 38.52m via Fed H.10. Supports neoenergia_ilhabela_200m_brl_2026.",
    evid_note="Opened Neoenergia Portuguese; R$200m Ilhabela substation/line confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. wind / allied — CapEx-fill Statkraft Gran Sul >R$1.5bn
row_doc(
    "statkraft_gran_sul_280mw_2026",
    "energy", "wind", "allied",
    "Statkraft — Gran Sul 280 MW onshore wind (>R$1.5bn)",
    "Brazil",
    "8 Jul 2026 Statkraft: investment decision for Gran Sul 280 MW onshore wind in Santa Vitória do Palmar, Rio Grande do Sul; construction scheduled to begin January next year; investment exceeding R$ 1.5 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~288.90m for stored R$1.5bn floor.",
    "1500000000", BRL_FX_DATE, "2026", "-33.519", "-53.368",
    "Santa Vitória do Palmar, Rio Grande do Sul (press geography).",
    "gauchazh_statkraft_gran_sul_15bn_20260723",
    "Com investimento superior a R$ 1,5 bilhão, o Projeto Gran Sul, da empresa norueguesa Statkraft, tem início das obras previsto para janeiro do próximo ano.",
    "https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/07/santa-vitoria-do-palmar-tera-novo-parque-eolico-com-investimento-de-r-15-bilhao-cmrwjwq0701370163akppasn7.html",
    "Actor: Statkraft (Norway) — allied. CapEx-fill: retain >R$1.5bn floor; add Fed H.10 Sep 25 2026 FX to USD ~288.90m. Shuffle wind.",
    "hunt_cycle233", investment_type="greenfield", evidence="proxy", currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='GaúchaZH. “Santa Vitória do Palmar terá novo parque eólico com investimento de R$ 1,5 bilhão.” July 23, 2026. https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/07/santa-vitoria-do-palmar-tera-novo-parque-eolico-com-investimento-de-r-15-bilhao-cmrwjwq0701370163akppasn7.html.',
    annotation="Statkraft Gran Sul CapEx-fill ~USD 288.90m via Fed H.10 (proxy). Supports statkraft_gran_sul_280mw_2026.",
    evid_note="Opened GaúchaZH Portuguese; >R$1.5bn / 280 MW Gran Sul confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. bridges_roads / allied — CapEx-fill Mota-Engil Rota dos Sertões R$4.3bn CapEx
row_doc(
    "mota_engil_rota_dos_sertoes_43bn_2026",
    "infrastructure", "bridges_roads", "allied",
    "Mota-Engil consortium — Rota dos Sertões highway concession CapEx",
    "Brazil",
    "29 Sep 2026: ANTT signs 30-year concession with Concessionária 116 Sertões S.A. (Neo Invest/Novonor, Portuguese Mota-Engil, Galápagos) for Rota dos Sertões — ~502 km BR-116/BA/PE + BR-324/BA; approximately R$4.3 billion infrastructure CapEx. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~828.18m.",
    "4300000000", BRL_FX_DATE, "2026", "-12.27", "-38.97",
    "Rota dos Sertões BR-116/BA/PE (press geography).",
    "estradas_rota_dos_sertoes_antt_20260929",
    "A Agência Nacional de Transportes Terrestres (ANTT) assinou em 29 de setembro de 2026 o contrato de concessão da Rota dos Sertões, sistema rodoviário formado por trechos das BR-116 na Bahia e em Pernambuco e da BR-324 na Bahia.",
    "https://estradas.com.br/antt-assina-concessao-da-rota-dos-sertoes-por-30-anos-entre-bahia-e-pernambuco/",
    "Actor: Mota-Engil (Portugal) + Neo Invest/Novonor + Galápagos — allied (Mota-Engil). CapEx-fill: retain R$4.3bn infrastructure CapEx; add Fed H.10 Sep 25 2026 FX to USD ~828.18m. Shuffle bridges_roads.",
    "hunt_cycle233", investment_type="concession", evidence="proxy", currency="BRL",
    value_usd=str(round(4300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Estradas. “ANTT assina concessão da Rota dos Sertões por 30 anos entre Bahia e Pernambuco.” September 29, 2026. https://estradas.com.br/antt-assina-concessao-da-rota-dos-sertoes-por-30-anos-entre-bahia-e-pernambuco/.',
    annotation="Mota-Engil Rota dos Sertões CapEx-fill ~USD 828.18m via Fed H.10 (proxy). Supports mota_engil_rota_dos_sertoes_43bn_2026.",
    evid_note="Opened Estradas Portuguese; ANTT 29 Sep 2026 Rota dos Sertões signing confirmed; retain stored R$4.3bn CapEx. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 8. water / other — CapEx-fill Cagece Fortaleza desal >R$3.1bn
row_doc(
    "cagece_dessal_fortaleza_auth_2026",
    "resources", "water", "other",
    "Cagece — Fortaleza seawater desalination plant (>R$3.1bn)",
    "Brazil",
    "16–17 Jul 2026: Cagece authorizes start of works on Planta de Dessalinização de Fortaleza at Praia do Futuro; PPP Consórcio Águas de Fortaleza; >R$3.1bn investment; 1,000 lps. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~597.06m for stored R$3.1bn floor.",
    "3100000000", BRL_FX_DATE, "2026", "-3.745", "-38.447",
    "Praia do Futuro, Fortaleza, Ceará (association geography).",
    "aesbe_cagece_dessal_20260717",
    "Com investimento superior a R$ 3,1 bilhões, o empreendimento será o maior projeto de dessalinização de água do mar para consumo humano já implantado no país",
    "https://aesbe.org.br/cagece-autoriza-inicio-das-obras-da-planta-de-dessalinizacao-de-fortaleza-marco-para-a-seguranca-hidrica-do-brasil/",
    "Actor: Cagece (Ceará state) + PPP consortium — other. CapEx-fill: retain >R$3.1bn floor; add Fed H.10 Sep 25 2026 FX to USD ~597.06m. Shuffle water.",
    "hunt_cycle233", investment_type="concession", evidence="proxy", currency="BRL",
    value_usd=str(round(3100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='AESBE. “Cagece autoriza início das obras da Planta de Dessalinização de Fortaleza.” July 17, 2026. https://aesbe.org.br/cagece-autoriza-inicio-das-obras-da-planta-de-dessalinizacao-de-fortaleza-marco-para-a-seguranca-hidrica-do-brasil/.',
    annotation="Cagece Fortaleza desal CapEx-fill ~USD 597.06m via Fed H.10 (proxy). Supports cagece_dessal_fortaleza_auth_2026.",
    evid_note="Opened AESBE Portuguese; >R$3.1bn / 1,000 lps Fortaleza desal confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 9. other_renewables / allied — CapEx-fill JICA Chachimbiro JPY 6.582bn
row_doc(
    "jica_chachimbiro_ecuador_2024",
    "energy", "other_renewables", "allied",
    "JICA — Chachimbiro Geothermal Development Project Phase I loan",
    "Ecuador",
    "24–25 Oct 2024 JICA: ODA yen loan with CELEC EP for Chachimbiro Geothermal Development Project (Phase I exploratory wells + engineering); maximum loan amount JPY 6,582 million. CapEx-fill: Fed H.10 Sep 25 2026 Japan Yen 157.1800 → USD ~41.88m.",
    "6582000000", JPY_FX_DATE, "2024", "0.47", "-78.25",
    "Chachimbiro geothermal field, Imbabura (JICA geography).",
    "jica_chachimbiro_20241025",
    "On October 24, the Japan International Cooperation Agency (JICA) signed a loan agreement with the Empresa Pública Estratégica Corporación Eléctrica del Ecuador … Maximum Loan Amount 6,582 million Japanese Yen … Chachimbiro Geothermal Development Project (Phase I)",
    "https://www.jica.go.jp/english/information/press/2024/20241025_41.html",
    "Actor: JICA (Japan) financing CELEC EP — allied. CapEx-fill: retain JPY 6.582bn max loan; add Fed H.10 Sep 25 2026 FX to USD ~41.88m. Shuffle other_renewables.",
    "hunt_cycle233", investment_type="development_finance", evidence="documented", currency="JPY",
    value_usd=str(round(6582000000 / float(JPY_USD), 2)), fx_usd=JPY_USD,
    chicago='Japan International Cooperation Agency (JICA). “Signing of Japanese ODA Loan Agreement with Ecuador: Supporting geothermal development toward the country’s first geothermal power plant.” October 25, 2024. https://www.jica.go.jp/english/information/press/2024/20241025_41.html.',
    annotation="JICA Chachimbiro CapEx-fill ~USD 41.88m via Fed H.10. Supports jica_chachimbiro_ecuador_2024.",
    evid_note="Opened JICA English; JPY 6,582m max loan / Chachimbiro Phase I confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 157.1800 JPY/USD.",
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
    print(f"cycle233 added {len(added)}: {added}")
    print(f"cycle233 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
