#!/usr/bin/env python3
"""Cycle 265 hunt: shuffle_seed=20261265; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261265).shuffle):
engineering_epc, water, niobium, wind, nickel, fission_smr, building_materials,
lithium, other_renewables, bridges_roads, solar, balsa, copper, power_plants_grid,
graphite, port_cranes, rail, port_ownership.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW ODATA/Aligned Colombia BG02+BG03 CapEx USD 1.3bn
  (company English Aligned press). John Deere Canoas electronics/pulverizer already
  archived cycle-86 out_of_scope ag manufacturing — not reactivated.
PRC equal-budget: honest residual (CPFL/State Grid/BYD CapEx dense).
Other: NEW Metro SP 2T26 CapEx R$1,061m + 6M26 R$2,132m + 2026 plan R$6,336m +
  Linha 2-Verde 2026 plan R$2.8bn; Motiva ViaQuatro signaling R$676m + Motiva 2T26
  consolidated CapEx R$1.83bn; TAESA ANEEL Despacho 200 reforços+melhorias R$193.4m.
Skipped: thin dry; holdovers unsigned; Equinix/Ascenty/Wabtec/Cemig CapEx dense.
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


# 1. engineering_epc / us — NEW ODATA Colombia BG02+BG03 CapEx USD 1.3bn
row_doc(
    "odata_colombia_bg02_bg03_1p3bn_2024",
    "infrastructure", "engineering_epc", "us",
    "ODATA (Aligned Data Centers) — Colombia BG02+BG03 CapEx USD 1.3bn",
    "Colombia",
    "23 Oct 2024 Aligned/ODATA English press: two new Cundinamarca data centers — DC BG02 (Mosquera Zona Franca de Occidente; 24 MW IT) and DC BG03 (Tenjo Zona Franca Metropolitana; 120 MW IT); combined 144 MW; initial construction phases targeted end-2026; total investment USD 1.3 billion in the region. CapEx: enter USD 1.3bn face. Distinct from odata_aligned_green_financing_1p02bn_2025 and odata_deltaflow_630m_2026.",
    "1300000000", "2024-10-23", "2024", "4.87", "-74.15",
    "ODATA BG03 Tenjo / BG02 Mosquera, Cundinamarca (company geography; Bogotá-metro pin).",
    "odata_aligned_colombia_1p3bn_20241023",
    "The initial phases of construction for the Company’s new facilities are expected to be completed by the end of 2026 and represent a total investment of $1.3 billion in the region. DC BG02 will provide 24MW of IT capacity, while DC BG03 will offer a substantial 120MW.",
    "https://aligneddc.com/press-release/odata-announces-1-3b-expansion-in-colombia-boosting-digital-development-in-the-country/",
    "Actor: ODATA / Aligned Data Centers (U.S.-backed Aligned) — us. NEW Colombia CapEx USD 1.3bn. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle265", investment_type="greenfield_plant", evidence="documented", currency="USD",
    chicago='Aligned Data Centers. “ODATA Announces $1.3B Expansion in Colombia, Boosting Digital Development in the Country.” October 23, 2024. https://aligneddc.com/press-release/odata-announces-1-3b-expansion-in-colombia-boosting-digital-development-in-the-country/.',
    annotation="ODATA Colombia BG02+BG03 CapEx USD 1.3bn company English. Supports odata_colombia_bg02_bg03_1p3bn_2024.",
    evid_note="Opened Aligned/ODATA English press; Colombia BG02+BG03 total investment USD 1.3bn confirmed.",
)

# 2. rail / other — NEW Metro SP 2T26 CapEx R$1,061m
row_doc(
    "metro_sp_2t26_capex_1061m_brl",
    "infrastructure", "rail", "other",
    "Metrô São Paulo — 2T26 CapEx R$1,061m",
    "Brazil",
    "Companhia do Metropolitano de São Paulo — Metrô 2T26 earnings release: CapEx totaled R$1,061 million in 2T26 (stable vs 2T25), mainly Lines 2-Verde (R$473m), 17-Ouro (R$297m), 15-Prata (R$206m). CapEx: enter R$1,061m 2T26 face. Nested vs 6M26 / 2026 plan (not additive).",
    "1061000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "São Paulo Metro network (city pin; Lines 2/15/17 expansion cited).",
    "metro_sp_2t26_release_2026",
    "No 2T26, o CAPEX da Companhia totalizou o montante de R$ 1.061 milhões … Total 1.061 1.062 (0,1%) 2.132 2.147 (0,7%)",
    "https://af0020-61294dc44a8f38122c35-endpoint.azureedge.net/blobaf00201eecb0af9a/wp-content/uploads/2026/05/Release-de-resultado_2T26.pdf",
    "Actor: Companhia do Metropolitano de São Paulo — Metrô (state utility) — other. NEW 2T26 CapEx R$1,061m. Shuffle rail.",
    "hunt_cycle265", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1061000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia do Metropolitano de São Paulo — Metrô. “Release de resultados 2T26.” 2026. https://af0020-61294dc44a8f38122c35-endpoint.azureedge.net/blobaf00201eecb0af9a/wp-content/uploads/2026/05/Release-de-resultado_2T26.pdf.',
    annotation="Metro SP 2T26/6M26 CapEx via Fed H.10. Supports metro_sp_2t26_capex_1061m_brl; metro_sp_6m26_capex_2132m_brl.",
    evid_note="Opened Metro SP company 2T26 release PDF; CapEx R$1,061m 2T26 / R$2,132m 6M26 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. rail / other — NEW Metro SP 6M26 CapEx R$2,132m
row_doc(
    "metro_sp_6m26_capex_2132m_brl",
    "infrastructure", "rail", "other",
    "Metrô São Paulo — 6M26 CapEx R$2,132m",
    "Brazil",
    "Metro SP 2T26 earnings release CapEx table: Total additions 6M26 R$2,132 million (vs R$2,147m 6M25); Line 2-Verde R$904m; Line 17-Ouro R$616m; Line 15-Prata R$448m among largest. CapEx: enter R$2,132m 6M26 face. Nested vs 2T26 / 2026 plan (not additive).",
    "2132000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "São Paulo Metro network (city pin; Lines 2/15/17 expansion cited).",
    "metro_sp_2t26_release_2026",
    "Adições do imobilizado/intangível … Total 1.061 1.062 (0,1%) 2.132 2.147 (0,7%)",
    "https://af0020-61294dc44a8f38122c35-endpoint.azureedge.net/blobaf00201eecb0af9a/wp-content/uploads/2026/05/Release-de-resultado_2T26.pdf",
    "Actor: Metrô São Paulo — other. NEW nested 6M26 CapEx R$2,132m. Shuffle rail.",
    "hunt_cycle265", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2132000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia do Metropolitano de São Paulo — Metrô. “Release de resultados 2T26.” 2026. https://af0020-61294dc44a8f38122c35-endpoint.azureedge.net/blobaf00201eecb0af9a/wp-content/uploads/2026/05/Release-de-resultado_2T26.pdf.',
    annotation="Metro SP 2T26/6M26 CapEx via Fed H.10. Supports metro_sp_2t26_capex_1061m_brl; metro_sp_6m26_capex_2132m_brl.",
    evid_note="Opened Metro SP company 2T26 release; 6M26 CapEx Total R$2,132m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. rail / other — NEW Metro SP 2026 CapEx plan R$6,336m
row_doc(
    "metro_sp_2026_capex_plan_6336m_brl",
    "infrastructure", "rail", "other",
    "Metrô São Paulo — 2026 CapEx plan R$6,336m",
    "Brazil",
    "Companhia do Metropolitano de São Paulo DF 2025 / investment program: Board approved CapEx program of R$6,336 million for FY2026 (Diretoria Res. 442 26 Nov 2025; Board Res. 041 17 Dec 2025); LOA published R$5,487m + restos a pagar R$441m = R$5,928m bridge toward R$6,336m. CapEx: enter R$6,336m plan face. Distinct from 2T26/6M26 spent and Linha 17 phase-1 envelope.",
    "6336000000", "2025-12-17", "2026", "-23.55", "-46.63",
    "São Paulo Metro 2026 expansion/recapacitation program (city pin).",
    "metro_sp_df2025_capex_plan_2026",
    "a Companhia do Metropolitano de São Paulo – Metrô aprovou o programa de investimentos na ordem de R$ 6.336 milhões para o exercício 2026. … Linha 2- Verde – Extensão Vila Prudente – Dutra – R$ 2,8 bilhões; Linha 15 – Prata – R$ 1,1 bilhão; e Linha 17 – Ouro – R$ 997 milhões.",
    "https://ri.metrosp.com.br/wp-content/uploads/2025/11/Demonstracao-financeira-Metro-2025.pdf",
    "Actor: Metrô São Paulo — other. NEW 2026 CapEx plan R$6,336m. Shuffle rail.",
    "hunt_cycle265", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(6336000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia do Metropolitano de São Paulo — Metrô. “Demonstrações financeiras 2025” (2026 CapEx program). https://ri.metrosp.com.br/wp-content/uploads/2025/11/Demonstracao-financeira-Metro-2025.pdf.',
    annotation="Metro SP 2026 CapEx plan R$6,336m + Linha 2-Verde R$2.8bn via Fed H.10. Supports metro_sp_2026_capex_plan_6336m_brl; metro_sp_linha2_verde_2026_plan_28bn_brl.",
    evid_note="Opened Metro SP DF 2025 PDF; 2026 investment program R$6,336m and Linha 2-Verde R$2.8bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. rail / other — NEW Metro SP Linha 2-Verde 2026 plan R$2.8bn
row_doc(
    "metro_sp_linha2_verde_2026_plan_28bn_brl",
    "infrastructure", "rail", "other",
    "Metrô São Paulo — Linha 2-Verde 2026 CapEx plan R$2.8bn",
    "Brazil",
    "Metro SP DF 2025 investment program: Linha 2-Verde extension Vila Prudente–Dutra allocated R$2.8 billion within FY2026 CapEx program. CapEx: enter R$2.8bn line-level plan face. Nested within metro_sp_2026_capex_plan_6336m_brl (not additive).",
    "2800000000", "2025-12-17", "2026", "-23.55", "-46.63",
    "Linha 2-Verde extension Vila Prudente–Dutra (São Paulo metro pin).",
    "metro_sp_df2025_capex_plan_2026",
    "Linha 2- Verde – Extensão Vila Prudente – Dutra – R$ 2,8 bilhões",
    "https://ri.metrosp.com.br/wp-content/uploads/2025/11/Demonstracao-financeira-Metro-2025.pdf",
    "Actor: Metrô São Paulo — other. NEW nested Linha 2-Verde 2026 plan R$2.8bn. Shuffle rail.",
    "hunt_cycle265", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(2800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia do Metropolitano de São Paulo — Metrô. “Demonstrações financeiras 2025” (2026 CapEx program). https://ri.metrosp.com.br/wp-content/uploads/2025/11/Demonstracao-financeira-Metro-2025.pdf.',
    annotation="Metro SP 2026 CapEx plan R$6,336m + Linha 2-Verde R$2.8bn via Fed H.10. Supports metro_sp_2026_capex_plan_6336m_brl; metro_sp_linha2_verde_2026_plan_28bn_brl.",
    evid_note="Opened Metro SP DF 2025; Linha 2-Verde 2026 allocation R$2.8bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. rail / other — NEW Motiva ViaQuatro signaling CapEx ~R$676m
row_doc(
    "motiva_viaquatro_signaling_676m_brl_2026",
    "infrastructure", "rail", "other",
    "Motiva / ViaQuatro — 11º Termo Aditivo signaling CapEx ~R$676m",
    "Brazil",
    "29 Jul 2026 Motiva company news (2T26): celebrated 11º Termo Aditivo da ViaQuatro enabling cerca de R$676 milhões in new signaling investments (reequilibrated via aporte); part of Linha 4-Amarela expansion works toward Taboão da Serra (SP). CapEx: enter R$676m face. Distinct from motiva_2t26_rails_capex_175m_brl spent rails and Motiva consolidated CapEx rows.",
    "676000000", "2026-07-29", "2026", "-23.55", "-46.63",
    "ViaQuatro Linha 4-Amarela (São Paulo metro pin; Taboão da Serra extension cited).",
    "motiva_2t26_company_news_20260729",
    "Também foi celebrado o 11º Termo Aditivo da ViaQuatro, viabilizando cerca de R$ 676 milhões em novos investimentos em sinalização, que serão reequilibrados por meio de aporte de recursos.",
    "https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/",
    "Actor: Motiva S.A. / ViaQuatro — other. NEW ViaQuatro signaling CapEx ~R$676m. Shuffle rail.",
    "hunt_cycle265", investment_type="concession_addendum", evidence="documented", currency="BRL",
    value_usd=str(round(676000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva amplia resultado em 57,5% e mantém trajetória de crescimento” (2T26). July 29, 2026. https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/.',
    annotation="Motiva 2T26 CapEx R$1.83bn + ViaQuatro signaling R$676m via Fed H.10. Supports motiva_2t26_capex_1830m_brl; motiva_viaquatro_signaling_676m_brl_2026.",
    evid_note="Opened Motiva company Portuguese 2T26 news; ViaQuatro signaling ~R$676m and consolidated CapEx R$1.83bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. bridges_roads / other — NEW Motiva 2T26 consolidated CapEx R$1.83bn
row_doc(
    "motiva_2t26_capex_1830m_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 2T26 CapEx R$1.83bn (roads+rails)",
    "Brazil",
    "29 Jul 2026 Motiva company news (2T26): executed Capex of R$1.83 billion on highway and rail concessions (+13.2% vs R$1.62bn 2T25). CapEx: enter R$1.83bn 2T26 consolidated face. Nested vs motiva_2t26_roads_capex_1640m_brl / motiva_2t26_rails_capex_175m_brl / motiva_1s26_capex_3304m_brl (not additive).",
    "1830000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Motiva Brazil roads+rails concession portfolio (São Paulo HQ pin).",
    "motiva_2t26_company_news_20260729",
    "No segundo trimestre de 2026, a Companhia executou um Capex de R$ 1,83 bilhão em suas concessões de rodovias e trilhos, crescimento de 13,2% na comparação com o R$ 1,62 bilhão apurado em igual intervalo de 2025.",
    "https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/",
    "Actor: Motiva S.A. — other. NEW nested 2T26 consolidated CapEx R$1.83bn. Shuffle bridges_roads.",
    "hunt_cycle265", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1830000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva amplia resultado em 57,5% e mantém trajetória de crescimento” (2T26). July 29, 2026. https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/.',
    annotation="Motiva 2T26 CapEx R$1.83bn + ViaQuatro signaling R$676m via Fed H.10. Supports motiva_2t26_capex_1830m_brl; motiva_viaquatro_signaling_676m_brl_2026.",
    evid_note="Opened Motiva company Portuguese 2T26 news; CapEx R$1.83bn 2T26 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 8. power_plants_grid / other — NEW TAESA reforços+melhorias CapEx R$193.4m
row_doc(
    "taesa_reforcos_melhorias_193p4m_brl_2026",
    "energy", "power_plants_grid", "other",
    "TAESA — ANEEL Despacho 200/2026 reforços+melhorias CapEx R$193.4m",
    "Brazil",
    "TAESA 2T26 earnings release: ANEEL Despacho nº 200 (Jan 2026) authorized 48 POTEE reinforcements + 25 PMI improvements with estimated CapEx R$184.5 million (reforços) + R$8.9 million (melhorias) = R$193.4m; 36-month execution. CapEx: enter R$193.4m combined face. Distinct from taesa_6m26_capex_445p3m_brl spent and taesa_greenfield_4p3bn_brl_aneel.",
    "193400000", "2026-01-01", "2026", "-23.55", "-46.63",
    "TAESA Brazil transmission reinforcement/improvement portfolio (São Paulo HQ pin; multi-concession).",
    "taesa_2t26_release_2026",
    "Esses empreendimentos foram autorizados pela ANEEL em janeiro de 2026, por meio do Despacho nº 200, totalizando um CAPEX estimado de R$ 184,5 MM e R$ 8,9 MM para reforços e melhorias, respectivamente, com prazo de execução de 36 meses.",
    "https://ri.taesa.com.br/wp-content/uploads/2018/11/TAESA_Release-2T26.pdf",
    "Actor: TAESA — other. NEW ANEEL-authorized reforços+melhorias CapEx R$193.4m. Shuffle power_plants_grid.",
    "hunt_cycle265", investment_type="reinforcement", evidence="documented", currency="BRL",
    value_usd=str(round(193400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='TAESA. “Divulgação de Resultados 2T26.” 2026. https://ri.taesa.com.br/wp-content/uploads/2018/11/TAESA_Release-2T26.pdf.',
    annotation="TAESA Despacho 200 reforços R$184.5m + melhorias R$8.9m via Fed H.10. Supports taesa_reforcos_melhorias_193p4m_brl_2026.",
    evid_note="Opened TAESA company 2T26 release PDF; Despacho 200 CapEx R$184.5m + R$8.9m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle265 added {len(added)}: {added}")
    print(f"cycle265 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
