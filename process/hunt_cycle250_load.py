#!/usr/bin/env python3
"""Cycle 250 hunt: shuffle_seed=20261250; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261250).shuffle):
other_renewables, port_ownership, wind, power_plants_grid, engineering_epc, nickel,
water, graphite, solar, niobium, fission_smr, bridges_roads, balsa, lithium,
building_materials, port_cranes, rail, copper.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Google Cloud LatAm USD 1.2bn commitment (company English).
PRC equal-budget: honest residual (State Grid / CPFL / SPIC / CTG / PowerChina CapEx
  already dense; GATE R$20bn acceleration without company primary confirming vs R$18bn).
Allied: NEW Enel Brasil Q1 2026 distribution CapEx R$1.5bn; NEW ISA Energia autorizado
  R$12.3bn through 2030.
Other: NEW Light SESA ~R$10bn 2026–2030 Material Fact.
Skipped: Cerro Verde USD 2.1bn Senace/press without Freeport primary; thin dry.
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


# 1. engineering_epc / us — NEW Google Cloud LatAm USD 1.2bn
row_doc(
    "google_latam_1p2bn_2022",
    "infrastructure", "engineering_epc", "us",
    "Google Cloud — five-year LatAm digital-infrastructure commitment",
    "Mexico",
    "4 Dec 2024 Google Cloud blog (Querétaro region opening): in 2022 announced a five-year USD 1.2 billion commitment to Latin America focusing on digital infrastructure, digital skills, entrepreneurship, and inclusive sustainable communities; Querétaro region is third LatAm cloud region (with Santiago and São Paulo). CapEx: enter USD 1.2bn commitment face. Distinct from AWS Mexico 5bn / Microsoft Mexico 1.3bn / Equinix rows.",
    "1200000000", "2022-01-01", "2022", "", "",
    "Google Cloud LatAm multi-region footprint (Querétaro / Santiago / São Paulo; multi-site — lat/lon blank).",
    "google_cloud_mexico_region_20241204",
    "In 2022, we announced a five-year, $1.2 billion commitment to Latin America, focusing on four key areas: digital infrastructure, digital skills, entrepreneurship, and inclusive, sustainable communities.",
    "https://cloud.google.com/blog/products/infrastructure/google-cloud-announces-41st-cloud-region-in-mexico",
    "Actor: Google / Alphabet (U.S.) — us. NEW row: company English LatAm USD 1.2bn commitment. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle250", investment_type="corporate_capex", evidence="documented", currency="USD",
    chicago='Google Cloud. “Google Cloud announces 41st cloud region in Mexico.” December 4, 2024. https://cloud.google.com/blog/products/infrastructure/google-cloud-announces-41st-cloud-region-in-mexico.',
    annotation="Google LatAm NEW USD 1.2bn. Supports google_latam_1p2bn_2022.",
    evid_note="Opened Google Cloud English blog; USD 1.2bn five-year LatAm commitment / Querétaro region opening confirmed.",
)

# 2. power_plants_grid / allied — NEW Enel Brasil Q1 2026 R$1.5bn
row_doc(
    "enel_brasil_1p5bn_brl_1q26",
    "energy", "power_plants_grid", "allied",
    "Enel Brasil — Q1 2026 distribution CapEx (~R$1.5bn)",
    "Brazil",
    "Enel Brasil company: invested R$ 1.5 billion in distribution in Q1 2026 (+31.3% YoY); Enel São Paulo alone R$690.3 million (+42.5%); part of broader distribution modernization / resilience program. CapEx: enter R$1.5bn face. Nested vs enel_brasil_25p3bn_brl_2025_2027 / enel_americas_brazil_grids_6p8bn_2026_28 plan envelopes.",
    "1500000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Enel Brasil distribution concessions SP/RJ/CE (São Paulo pin).",
    "enel_brasil_1q26_1p5bn",
    "No primeiro trimestre de 2026, a Enel Brasil investiu R$ 1,5 bilhão em suas distribuidoras de energia elétrica no país, registrando um crescimento de 31,3% em comparação ao mesmo período de 2025.",
    "https://www.enel.com.br/pt-saopaulo/investimentos/d2026-enel-brasil-eleva-investimentos-em-distribuicao-de-energia-no-primeiro-trimestre-de-2026.html",
    "Actor: Enel Brasil (Enel Italy) — allied. NEW nested Q1 2026 spent CapEx R$1.5bn. Shuffle power_plants_grid.",
    "hunt_cycle250", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Enel Brasil. “Enel Brasil eleva em 31% investimentos em distribuição de energia no primeiro trimestre de 2026.” 2026. https://www.enel.com.br/pt-saopaulo/investimentos/d2026-enel-brasil-eleva-investimentos-em-distribuicao-de-energia-no-primeiro-trimestre-de-2026.html.',
    annotation="Enel Q1 2026 NEW R$1.5bn ~USD 288.90m via Fed H.10. Supports enel_brasil_1p5bn_brl_1q26.",
    evid_note="Opened Enel Brasil Portuguese; R$1.5bn Q1 / SP R$690.3m / +31.3% confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW ISA Energia autorizado R$12.3bn
row_doc(
    "isa_energia_autorizado_12p3bn_brl_2030",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — authorized CapEx pipeline ~R$12.3bn through 2030",
    "Brazil",
    "24 Feb 2026 ISA Energia Brasil: possesses R$ 12.3 billion in authorized investments to be executed through 2030 — of which R$6 billion for four greenfield projects (Piraquê Blocos 2–3, Jacarandá, Serra Dourada, Itatiaia; RAP R$826m) and R$6.3 billion (Dec 2025 real terms) for ANEEL-authorized Reinforcements & Improvements. CapEx: enter R$12.3bn authorized pipeline face. Distinct from isa_energia_rm_carteira_7p2bn_2026 (R&M-only carteira) and isa_energia_fy2025_capex_5p1bn_brl (executed FY2025).",
    "12300000000", "2026-02-24", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil multi-state transmission (São Paulo pin).",
    "isa_energia_4t25_autorizado_12p3bn",
    "A ISA ENERGIA BRASIL possui ainda R$ 12,3 bilhões em investimentos autorizados, a serem realizados até 2030, dos quais R$ 6 bilhões são para a construção dos quatro projetos Greenfield – Piraquê Blocos 2 e 3 (MG/ES), Jacarandá (SP), Serra Dourada (BA/MG) e Itatiaia (MG/RJ), que possuem RAP de R$ 826 milhões cujo recebimento será habilitado conforme entrem em operação, e R$ 6,3 bilhões (termos reais dezembro/2025) para projetos de Reforços e Melhorias já autorizados pela ANEEL.",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-divulga-os-resultados-do-4t25-com-recorde-em-investimentos-de-r-51-bi-no-ano/",
    "Actor: ISA Energia Brasil (Colombian ISA) — allied. NEW row: company Portuguese authorized pipeline R$12.3bn. Shuffle power_plants_grid.",
    "hunt_cycle250", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(12300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “ISA ENERGIA BRASIL divulga os resultados do 4T25 com recorde em investimentos de R$ 5,1 bi no ano.” February 24, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-divulga-os-resultados-do-4t25-com-recorde-em-investimentos-de-r-51-bi-no-ano/.',
    annotation="ISA autorizado NEW R$12.3bn ~USD 2368.98m via Fed H.10. Supports isa_energia_autorizado_12p3bn_brl_2030.",
    evid_note="Opened ISA Energia Portuguese 4T25; R$12.3bn authorized / R$6bn greenfield / R$6.3bn R&M confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Light SESA ~R$10bn
row_doc(
    "light_sesa_10bn_brl_2026_2030",
    "energy", "power_plants_grid", "other",
    "Light SESA — distribution CapEx plan ~R$10bn (2026–2030)",
    "Brazil",
    "11 May 2026 Light S.A. / Light SESA Material Fact: reiterates projection of Light SESA nominal CapEx ~R$ 10 billion cumulative 2026–2030 across 31 municipalities (network modernization/digitalization/automation; legacy systems; resilience; quality; non-technical loss combat). CapEx: enter R$10bn soft floor. Distinct from Neoenergia/Energisa/Cemig concession CapEx rows.",
    "10000000000", "2026-05-11", "2026", "-22.91", "-43.17",
    "Light SESA Rio de Janeiro concession (Rio de Janeiro pin).",
    "light_fr_10bn_20260511",
    "Capex nominal da Light SESA ~R$10 bilhões",
    "https://investidor10.com.br/acoes/link_comunicado/LIGT3/41763/",
    "Actor: Light SESA (Brazilian distributor; Light S.A. group) — other. NEW row: company Material Fact ~R$10bn 2026–2030 (opened via CVM/Material Fact republisher). Shuffle power_plants_grid.",
    "hunt_cycle250", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(10000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Light S.A. / Light Serviços de Eletricidade S.A. “Fato Relevante” (5-year investment plan). May 11, 2026. https://investidor10.com.br/acoes/link_comunicado/LIGT3/41763/.',
    annotation="Light SESA NEW ~R$10bn floor ~USD 1926.00m via Fed H.10. Supports light_sesa_10bn_brl_2026_2030.",
    evid_note="Opened Light Material Fact text (11 May 2026); ~R$10bn SESA nominal CapEx 2026–2030 / 31 municipalities confirmed. CapEx enter R$10bn soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle250 added {len(added)}: {added}")
    print(f"cycle250 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
