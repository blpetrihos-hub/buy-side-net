#!/usr/bin/env python3
"""Cycle 245 hunt: shuffle_seed=20261245; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261245).shuffle):
niobium, wind, building_materials, solar, copper, port_cranes, lithium,
power_plants_grid, bridges_roads, port_ownership, rail, graphite,
other_renewables, nickel, engineering_epc, water, balsa, fission_smr.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Wabtec Contagem locomotive production-line CapEx
  R$150m (Valor via Revista Ferroviária; distinct from R$20m Engineering Center).
PRC equal-budget: NEW CTG Brasil Flex BESS lab Ilha Solteira R$15m (company).
Allied: NEW ISA Energia R&M 1H2026 spent R$815.4m; NEW Neoenergia Cosern
  R$4.1bn 2026–2030 cycle; NEW Cosern Tabatinga nested R$40m (same company page).
Skipped: Pacto Coronel Vivida CapEx is Brazilian distributor; Goldwind Camaçari
  R$100m already filled; holdovers unsigned; thin dry.
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


# 1. rail / us — NEW Wabtec Contagem locomotive production line R$150m
row_doc(
    "wabtec_contagem_loco_line_150m_brl_2025",
    "infrastructure", "rail", "us",
    "Wabtec — Contagem locomotive production-line activation (R$150m)",
    "Brazil",
    "13 Oct 2025 Valor Econômico (republished Revista Ferroviária): Wabtec activated a new locomotive production line at its Contagem (MG) industrial complex, fruit of R$ 150 million investments; separately investing R$ 20 million in workforce expansion and first LatAm Global Engineering Center. CapEx: enter R$150m production-line face. Distinct from wabtec_contagem_r20m_2025 Engineering Center row.",
    "150000000", "2025-10-13", "2025", "-19.93", "-44.05",
    "Wabtec Contagem (MG) Cidade Industrial locomotive plant (municipal pin).",
    "valor_wabtec_contagem_150m_20251013",
    "A americana Wabtec Corporation, fornecedora de equipamentos ferroviários, ativou uma nova linha de produção de locomotivas no complexo industrial instalado em Contagem (MG), fruto de investimentos de R$ 150 milhões. Agora, a empresa investe R$ 20 milhões na ampliação de sua equipe e na implantação de um centro global de engenharia, o primeiro da América Latina.",
    "https://revistaferroviaria.com.br/2025/10/apos-ampliacao-wabtec-monta-centro-de-engenharia-no-pais/",
    "Actor: Wabtec (U.S.) — us. NEW row: Valor/Revista Ferroviária CapEx R$150m Contagem locomotive line (UNVERIFIED press citing Valor). Distinct from R$20m Engineering Center. Shuffle rail / U.S. ≥1/3 budget.",
    "hunt_cycle245", investment_type="greenfield_plant", evidence="press", currency="BRL",
    value_usd=str(round(150000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Revista Ferroviária (citing Valor Econômico). “Após ampliação, Wabtec monta centro de engenharia no país.” October 13, 2025. https://revistaferroviaria.com.br/2025/10/apos-ampliacao-wabtec-monta-centro-de-engenharia-no-pais/.',
    annotation="Wabtec Contagem loco line NEW R$150m ~USD 28.89m via Fed H.10 (press). Supports wabtec_contagem_loco_line_150m_brl_2025.",
    evid_note="Opened Revista Ferroviária Portuguese (Valor republish); R$150m Contagem locomotive line / distinct R$20m engineering center confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. other_renewables / prc — NEW CTG Flex BESS Ilha Solteira R$15m
row_doc(
    "ctg_flex_bess_ilha_solteira_15m_brl_2026",
    "energy", "other_renewables", "prc",
    "CTG Brasil — Flex BESS lab at UHE Ilha Solteira (692 kWp PV + Huawei 215 kWh)",
    "Brazil",
    "29 Jan 2026 CTG Brasil company: inaugurates Flex BESS laboratory at UHE Ilha Solteira (SP) — 1,248-module 692 kWp PV plus Huawei 215 kWh BESS for connected electrochemical storage tests; partners SENAI-PE ISI-TICs, Thymos, Wisebyte, HDT. CapEx: enter R$15m Aneel P&D / SENAI / partners face. Distinct from ctg_ilha_solteira_ug1_2026 Unit-1 upgrade (blank CapEx).",
    "15000000", "2026-01-29", "2026", "-20.43", "-51.34",
    "UHE Ilha Solteira (SP/MS border) Flex BESS lab pin.",
    "ctg_flex_bess_ilha_solteira_20260129",
    "A iniciativa recebeu investimento de R$ 15 milhões por meio de recursos do programa de Pesquisa e Desenvolvimento da Aneel, do SENAI e de parceiros.",
    "https://www.ctgbr.com.br/inauguramos-laboratorio-para-testes-de-sistema-de-armazenamento-de-energia-com-baterias/",
    "Actor: CTG Brasil (China Three Gorges) — prc. NEW row: company Portuguese Flex BESS R$15m. Huawei equipment noted; CapEx is CTG/P&D envelope. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle245", investment_type="pilot", evidence="documented", currency="BRL",
    value_usd=str(round(15000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CTG Brasil. “Inauguramos laboratório para testes de sistema de armazenamento de energia com baterias.” January 29, 2026. https://www.ctgbr.com.br/inauguramos-laboratorio-para-testes-de-sistema-de-armazenamento-de-energia-com-baterias/.',
    annotation="CTG Flex BESS NEW R$15m ~USD 2.89m via Fed H.10. Supports ctg_flex_bess_ilha_solteira_15m_brl_2026.",
    evid_note="Opened CTG Brasil Portuguese; R$15m / 692 kWp / Huawei 215 kWh / Ilha Solteira confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW ISA Energia R&M 1H2026 spent R$815.4m
row_doc(
    "isa_energia_rm_815m_brl_1s26",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Reinforcements & Improvements (R&M) CapEx spent 1H2026",
    "Brazil",
    "3 Sep 2026 ISA Energia Brasil company: invested R$ 815.4 million in R&M / installed-base renewal in 1H2026 (+19% YoY); Q2 alone R$ 445.4 million (+17.4% vs 2Q25); energized 16 projects / replaced 312 equipment items. CapEx: enter R$815.4m 1H spent face. Nested vs isa_energia_rm_370m_brl_1t26 (Q1) and isa_energia_rm_carteira_7p2bn_2026 (authorized carteira ~R$7.2bn).",
    "815400000", "2026-09-03", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil São Paulo concession / multi-state transmission (São Paulo pin).",
    "isa_energia_rm_815m_1s26_20260903",
    "A ISA ENERGIA BRASIL – líder em transmissão de energia no País e responsável por cerca de 95% da energia transmitida no Estado de São Paulo – investiu R$ 815,4 milhões em projetos de renovação de seu parque instalado no primeiro semestre de 2026, crescimento de 19% em relação ao mesmo período do ano passado.",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-8154-milhoes-na-modernizacao-da-rede-de-transmissao-no-1-semestre/",
    "Actor: ISA Energia Brasil (Colombian ISA) — allied. NEW nested 1H2026 R&M spent R$815.4m. Shuffle power_plants_grid.",
    "hunt_cycle245", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(815400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “ISA ENERGIA BRASIL investe R$ 815,4 milhões na modernização da rede de transmissão no 1º semestre.” September 3, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-8154-milhoes-na-modernizacao-da-rede-de-transmissao-no-1-semestre/.',
    annotation="ISA R&M 1H2026 NEW R$815.4m ~USD 157.05m via Fed H.10. Supports isa_energia_rm_815m_brl_1s26.",
    evid_note="Opened ISA Energia Brasil Portuguese; R$815.4m 1H2026 / +19% / Q2 R$445.4m / 16 projects confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Cosern R$4.1bn 2026–2030
row_doc(
    "neoenergia_cosern_4p1bn_brl_2026_2030",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Cosern — RN distribution CapEx cycle R$4.1bn (2026–2030)",
    "Brazil",
    "12 May 2026 Neoenergia Cosern company: new investment cycle of R$ 4.1 billion in Rio Grande do Norte through 2030 after MME concession renewal to 2057 (+81% vs 2021–2025 R$2.2bn). CapEx: enter R$4.1bn face. Distinct from neoenergia_dist_50bn group envelope / Estivas nested / Brasília 3.1bn.",
    "4100000000", "2026-05-12", "2026", "-5.79", "-35.21",
    "Neoenergia Cosern Rio Grande do Norte concession (Natal pin).",
    "neoenergia_cosern_4p1bn_20260512",
    "A Neoenergia Cosern anunciou nesta terça-feira (12) um novo ciclo de investimentos de R$ 4,1 bilhões no Rio Grande do Norte até 2030.",
    "https://www.neoenergia.com/web/rn/w/ampliacao-ivestimentos-bilhoes-rede-eletrica-cosern-1",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW row: company Portuguese Cosern R$4.1bn through 2030. Shuffle power_plants_grid.",
    "hunt_cycle245", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(4100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia Cosern. “Neoenergia Cosern anuncia investimento recorde de R$ 4,1 bilhões no RN.” May 12, 2026. https://www.neoenergia.com/web/rn/w/ampliacao-ivestimentos-bilhoes-rede-eletrica-cosern-1.',
    annotation="Neoenergia Cosern NEW R$4.1bn ~USD 789.66m via Fed H.10. Supports neoenergia_cosern_4p1bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Cosern Portuguese; R$4.1bn to 2030 / +81% / concession to 2057 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / allied — NEW Cosern Tabatinga nested R$40m
row_doc(
    "neoenergia_cosern_tabatinga_40m_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Cosern — Subestação Tabatinga + 19 km line (Litoral Sul RN)",
    "Brazil",
    "12 May 2026 Neoenergia Cosern company (within R$4.1bn cycle): Litoral Sul — Subestação Tabatinga and a 19 km line with investments of R$ 40 million, benefiting ~21 thousand consumers. CapEx: enter R$40m face. Nested vs neoenergia_cosern_4p1bn_brl_2026_2030 envelope and Estivas >R$100m.",
    "40000000", "2026-05-12", "2026", "-6.07", "-35.12",
    "Neoenergia Cosern Litoral Sul RN (Tabatinga / Nísia Floresta corridor pin).",
    "neoenergia_cosern_tabatinga_40m_20260512",
    "Já no Litoral Sul, a Subestação Tabatinga e uma linha de 19 quilômetros terão investimentos de R$ 40 milhões, beneficiando aproximadamente 21 mil consumidores.",
    "https://www.neoenergia.com/web/rn/w/ampliacao-ivestimentos-bilhoes-rede-eletrica-cosern-1",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW nested CapEx R$40m Cosern Tabatinga. Shuffle power_plants_grid.",
    "hunt_cycle245", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(40000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia Cosern. “Neoenergia Cosern anuncia investimento recorde de R$ 4,1 bilhões no RN.” May 12, 2026. https://www.neoenergia.com/web/rn/w/ampliacao-ivestimentos-bilhoes-rede-eletrica-cosern-1.',
    annotation="Neoenergia Cosern Tabatinga NEW R$40m ~USD 7.70m via Fed H.10. Supports neoenergia_cosern_tabatinga_40m_brl_2026.",
    evid_note="Opened Neoenergia Cosern Portuguese; R$40m Tabatinga + 19 km / ~21k consumers confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle245 added {len(added)}: {added}")
    print(f"cycle245 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
