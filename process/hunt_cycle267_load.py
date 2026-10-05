#!/usr/bin/env python3
"""Cycle 267 hunt: shuffle_seed=20261267; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261267).shuffle):
solar, rail, wind, lithium, nickel, graphite, building_materials, copper,
port_ownership, other_renewables, niobium, water, power_plants_grid, balsa,
fission_smr, engineering_epc, bridges_roads, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Microsoft Chile Central region ~USD 3.3bn direct
  investment (IDC estimate cited on Microsoft Spanish News Center primary; proxy).
PRC equal-budget: CapEx-fill BYD Brazil BESS ≤R$500m — upgrade to company primary
  (bydbrasil.com.br) from prior press proxy.
Other: NEW Porto Itapoá Fase IV R$500m + Fase III R$815m; Motiva 2026 CapEx plan
  R$8.3bn + Linha 4 R$941m; Alupar 6M26 Custo de Infraestrutura R$649.2m.
Skipped: thin dry; holdovers unsigned; CPFL/Equinix/Ascenty/Wabtec/TAESA/ISA dense.
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
    status="active",
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": status,
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


# 1. engineering_epc / us — NEW Microsoft Chile Central ~USD 3.3bn (IDC on company page)
row_doc(
    "microsoft_chile_central_3p3bn_idc_2025",
    "infrastructure", "engineering_epc", "us",
    "Microsoft — Azure Chile Central datacenter region (IDC direct-investment estimate)",
    "Chile",
    "18 Jun 2025 Microsoft News Center Latinoamérica (Spanish): inaugurates first Chile datacenter region (Azure Chile Central; three independent sites in Región Metropolitana). Citing IDC: of ~USD 35.3bn net-new cloud revenues over four years, approximately USD 3.3 billion will be invested directly in Chile. CapEx: enter USD 3.3bn IDC direct-investment estimate as soft plan floor. Distinct from microsoft_mexico_ai_1p3bn_2024 / microsoft_brazil_cloud_ai_14p7bn_brl_2024 and aes_andes_microsoft_chile_ppa_2022 (PPA). UNVERIFIED proxy (IDC estimate on company page; not a Microsoft board CapEx authorization).",
    "3300000000", "2025-06-18", "2025", "-33.36", "-70.73",
    "Microsoft Azure Chile Central / Quilicura–Santiago RM datacenter geography (company region; approximate Quilicura pin).",
    "microsoft_chile_central_20250618",
    "De ese total, alrededor de 3.300 millones de dólares se invertirán directamente en Chile, lo que contribuirá al desarrollo económico local y la creación estimada de 81.041 empleos entre 2025 y 2029.",
    "https://news.microsoft.com/es-xl/microsoft-inaugura-su-primera-region-de-datacenters-en-chile-para-acelerar-la-innovacion-y-el-desarrollo-economico-local/",
    "Actor: Microsoft Corporation (U.S.) — us. NEW soft Chile CapEx floor ~USD 3.3bn (IDC via company Spanish). Shuffle engineering_epc; ≥1/3 U.S. hunt. UNVERIFIED proxy.",
    "hunt_cycle267", investment_type="capex_plan", evidence="proxy", currency="USD",
    chicago='Microsoft. “Microsoft inaugura su primera Región de Datacenters en Chile para acelerar la innovación y el desarrollo económico local” (citing IDC). June 18, 2025. https://news.microsoft.com/es-xl/microsoft-inaugura-su-primera-region-de-datacenters-en-chile-para-acelerar-la-innovacion-y-el-desarrollo-economico-local/.',
    annotation="Microsoft Chile Central IDC ~USD 3.3bn direct-investment estimate (proxy). Supports microsoft_chile_central_3p3bn_idc_2025.",
    evid_note="Opened Microsoft Spanish News Center; IDC ~USD 3.3bn direct Chile investment confirmed. Soft plan floor; UNVERIFIED proxy.",
    bib_type="company",
)

# 2. port_ownership / other — NEW Porto Itapoá Fase IV R$500m
row_doc(
    "porto_itapoa_fase_iv_500m_brl_2024",
    "infrastructure", "port_ownership", "other",
    "Porto Itapoá — Fase IV expansion CapEx R$500m",
    "Brazil",
    "1 Nov 2024 Porto Itapoá company: beginning Fase IV expansion with planned investments totaling R$ 500 million over the next 12 months — +120,000 m² yard, eighth STS, hybrid RTGs/TTs, reefer plugs, scanner; terminal in Baía da Babitonga, Santa Catarina. CapEx: enter R$500m Fase IV face. Distinct from zpmc_itapoa_* crane equipment rows (OEM) and Fase III R$815m on same page.",
    "500000000", "2024-11-01", "2024", "-26.18", "-48.61",
    "Porto Itapoá / Tecon Santa Catarina, Baía da Babitonga, SC (company geography).",
    "porto_itapoa_fase_iv_20241101",
    "O Porto Itapoá está dando início à sua Fase IV de expansão, com previsão de investimentos que somam R$ 500 milhões nos próximos 12 meses.",
    "https://www.portoitapoa.com/porto-itapoa-anuncia-fase-iv-de-expansao-com-investimentos-de-r-500-milhoes/",
    "Actor: Porto Itapoá / Itapoá Terminais Portuários (Brazilian private terminal) — other. NEW Fase IV CapEx R$500m. Shuffle port_ownership.",
    "hunt_cycle267", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Porto Itapoá. “Porto Itapoá anuncia Fase IV de expansão com Investimentos de R$ 500 milhões.” November 1, 2024. https://www.portoitapoa.com/porto-itapoa-anuncia-fase-iv-de-expansao-com-investimentos-de-r-500-milhoes/.',
    annotation="Porto Itapoá Fase IV R$500m + Fase III R$815m via Fed H.10. Supports porto_itapoa_fase_iv_500m_brl_2024; porto_itapoa_fase_iii_815m_brl_2024.",
    evid_note="Opened Porto Itapoá company Portuguese; Fase IV R$500m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. port_ownership / other — NEW Porto Itapoá Fase III R$815m (same company page)
row_doc(
    "porto_itapoa_fase_iii_815m_brl_2024",
    "infrastructure", "port_ownership", "other",
    "Porto Itapoá — Fase III expansion CapEx R$815m",
    "Brazil",
    "1 Nov 2024 Porto Itapoá company (same Fase IV release): inaugurated Fase III on 25 Apr with +200,000 m² yard and 8,000 m² warehouse, completing a R$ 815 million CapEx package; yard then 455,000 m². CapEx: enter R$815m Fase III face. Distinct from porto_itapoa_fase_iv_500m_brl_2024 and ZPMC crane rows.",
    "815000000", "2024-04-25", "2024", "-26.18", "-48.61",
    "Porto Itapoá / Tecon Santa Catarina, Baía da Babitonga, SC (company geography).",
    "porto_itapoa_fase_iv_20241101",
    "o Porto Itapoá inaugurou, em 25 de abril, a fase III de expansão do terminal, com mais 200 mil m² de pátio, contemplando o armazém de 8 mil m², finalizando um aporte de R$ 815 milhões.",
    "https://www.portoitapoa.com/porto-itapoa-anuncia-fase-iv-de-expansao-com-investimentos-de-r-500-milhoes/",
    "Actor: Porto Itapoá — other. NEW Fase III CapEx R$815m from company primary. Shuffle port_ownership.",
    "hunt_cycle267", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(815000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Porto Itapoá. “Porto Itapoá anuncia Fase IV de expansão com Investimentos de R$ 500 milhões.” November 1, 2024. https://www.portoitapoa.com/porto-itapoa-anuncia-fase-iv-de-expansao-com-investimentos-de-r-500-milhoes/.',
    annotation="Porto Itapoá Fase IV R$500m + Fase III R$815m via Fed H.10. Supports porto_itapoa_fase_iv_500m_brl_2024; porto_itapoa_fase_iii_815m_brl_2024.",
    evid_note="Opened Porto Itapoá company Portuguese; Fase III R$815m completion confirmed on same page. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. bridges_roads / other — NEW Motiva 2026 CapEx plan R$8.3bn (company)
row_doc(
    "motiva_2026_capex_plan_8p3bn_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 2026 CapEx plan R$8.3bn (ex-airports)",
    "Brazil",
    "Motiva company FY2025 results news: for 2026 the company forecasts investing R$ 8.3 billion — already excluding the Airports platform — of which R$ 7.2 billion in highways. CapEx: enter R$8.3bn total 2026 plan face. Distinct from motiva_2026_highways_plan_7167m_brl (prior OE proxy highways breakout) and 1S26/2T26 spent CapEx rows (not additive).",
    "8300000000", "2026-02-10", "2026", "-23.55", "-46.63",
    "Motiva Brazil roads+rails concession portfolio (São Paulo HQ pin; airports excluded).",
    "motiva_fy2025_results_8p3bn_2026",
    "Para 2026, a previsão da Companhia é investir R$ 8,3 bilhões – já sem contabilizar a plataforma de Aeroportos –, sendo R$ 7,2 bilhões em Rodovias.",
    "https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/",
    "Actor: Motiva S.A. — other. NEW company-primary 2026 CapEx plan R$8.3bn. Shuffle bridges_roads.",
    "hunt_cycle267", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(8300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva encerra 2025 com forte crescimento e resultados recordes.” 2026. https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/.',
    annotation="Motiva 2026 CapEx plan R$8.3bn + Linha 4 R$941m via Fed H.10. Supports motiva_2026_capex_plan_8p3bn_brl; motiva_linha4_2026_941m_brl.",
    evid_note="Opened Motiva company Portuguese FY2025/2026 plan news; R$8.3bn 2026 CapEx (ex-airports) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. rail / other — NEW Motiva Linha 4–Amarela 2026 CapEx R$941m
row_doc(
    "motiva_linha4_2026_941m_brl",
    "infrastructure", "rail", "other",
    "Motiva / ViaQuatro — Linha 4–Amarela 2026 CapEx R$941m",
    "Brazil",
    "Motiva company FY2025 results news: also projects R$ 941 million investment in Linha 4–Amarela in 2026, advancing system expansion including construction of two new metro stations. CapEx: enter R$941m 2026 Linha 4 face. Nested within motiva_2026_capex_plan_8p3bn_brl envelope (not additive); distinct from motiva_viaquatro_signaling_676m_brl.",
    "941000000", "2026-02-10", "2026", "-23.55", "-46.63",
    "São Paulo Metro Linha 4–Amarela / ViaQuatro (São Paulo pin).",
    "motiva_fy2025_results_8p3bn_2026",
    "A Motiva projeta também investimento de R$ 941 milhões na Linha 4 – Amarela, com o avanço das obras de expansão do sistema, incluindo a construção de duas novas estações de metrô.",
    "https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/",
    "Actor: Motiva / ViaQuatro — other. NEW nested Linha 4 2026 CapEx R$941m. Shuffle rail.",
    "hunt_cycle267", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(941000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva encerra 2025 com forte crescimento e resultados recordes.” 2026. https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/.',
    annotation="Motiva 2026 CapEx plan R$8.3bn + Linha 4 R$941m via Fed H.10. Supports motiva_2026_capex_plan_8p3bn_brl; motiva_linha4_2026_941m_brl.",
    evid_note="Opened Motiva company Portuguese; Linha 4 2026 CapEx R$941m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. power_plants_grid / other — NEW Alupar 6M26 Custo de Infraestrutura R$649.2m
row_doc(
    "alupar_6m26_custo_infra_649p2m_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — 6M26 Custo de Infraestrutura (CapEx) R$649.2m",
    "Brazil",
    "6 Aug 2026 Alupar Investimento 2T26 earnings release (company RI ZIP): Custo de Infraestrutura (CapEx under ICPC 01/CPC 47) totaled R$ 649.2 million in 6M26 vs R$ 325.9 million in 6M25 (+99.2%); of which R$379.2m in 2T26. CapEx: enter R$649.2m 6M26 face. Distinct from alupar_2t26_capex_354m_brl (prior OE proxy desembolsado figure) and project CapEx previsto rows (not additive).",
    "649200000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Alupar Brazil + LatAm transmission/generation footprint (São Paulo HQ pin).",
    "alupar_2t26_release_20260806",
    "Custo de Infraestrutura (270,0) (379,2) | (161,6) | 134,6% (649,2) (325,9) 99,2%",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento — other. NEW company-primary 6M26 CapEx R$649.2m. Shuffle power_plants_grid.",
    "hunt_cycle267", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(649200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26.” August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar 6M26 Custo de Infraestrutura R$649.2m via Fed H.10. Supports alupar_6m26_custo_infra_649p2m_brl.",
    evid_note="Opened Alupar 2T26 company RI ZIP / results tables; 6M26 Custo de Infraestrutura R$649.2m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. other_renewables / prc — CapEx-fill BYD BESS ≤R$500m to company primary
row_doc(
    "byd_brazil_bess_factory_500m_2026",
    "energy", "other_renewables", "prc",
    "BYD — industrial BESS production capacity in Brazil (≤R$500m)",
    "Brazil",
    "1 Sep 2026 BYD Brasil company: after announcing investments of up to R$ 500 million in BESS systems, company restates the CapEx commitment for industrial capacity to produce stationary storage in Brazil (location still under study; Manaus candidate historically). CapEx-fill: retain ≤R$500m ceiling; Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~96.30m. Evidence upgraded from prior Poder360 press proxy to company Portuguese primary.",
    "500000000", "2026-09-01", "2026", "-3.10", "-60.02",
    "BYD Brazil BESS industrial capacity (Manaus candidate pin; site not finalized on company page).",
    "byd_brasil_bess_500m_20260901",
    "Após anunciar investimentos de até R$ 500 milhões em sistemas BESS, a companhia reforça sua aposta no país … O investimento de R$ 500 milhões mostra a dimensão do nosso compromisso com o país",
    "https://bydbrasil.com.br/byd-avanca-em-estrategia-de-armazenamento-de-energia-no-brasil-apos-anunciar-investimento-de-ate-r-500-milhoes-no-pais/",
    "Actor: BYD (PRC) — prc. CapEx-fill + evidence upgrade to company primary ≤R$500m. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle267", investment_type="greenfield_plant", evidence="documented", currency="BRL",
    value_usd=str(round(500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='BYD Brasil. “BYD avança em estratégia de armazenamento de energia no Brasil após anunciar investimento de até R$ 500 milhões no país.” September 1, 2026. https://bydbrasil.com.br/byd-avanca-em-estrategia-de-armazenamento-de-energia-no-brasil-apos-anunciar-investimento-de-ate-r-500-milhoes-no-pais/.',
    annotation="BYD Brazil BESS ≤R$500m company primary via Fed H.10. Supports byd_brazil_bess_factory_500m_2026.",
    evid_note="Opened BYD Brasil company Portuguese; ≤R$500m BESS industrial CapEx restated. CapEx USD via Fed H.10 Sep 25 2026 5.1921. Evidence upgrade from press proxy.",
)


def upsert_bib(bib, bib_by, bib_e):
    sid = bib_e["id"]
    entry = {
        "id": sid,
        "type": bib_e.get("type", "company"),
        "chicago": bib_e["chicago"],
        "url": bib_e["url"],
        "annotation": bib_e.get("annotation", ""),
        "supports": bib_e.get("supports", []),
    }
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        old = existing.get("supports") or []
        new = entry["supports"] or []
        merged = list(dict.fromkeys(list(old) + list(new)))
        existing.update({k: v for k, v in entry.items() if k != "supports"})
        existing["supports"] = merged
    else:
        bib.append(entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("entries") or bib.get("sources") or []
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
    print(f"cycle267 added {len(added)}: {added}")
    print(f"cycle267 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
