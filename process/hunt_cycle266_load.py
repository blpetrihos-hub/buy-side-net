#!/usr/bin/env python3
"""Cycle 266 hunt: shuffle_seed=20261266; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261266).shuffle):
building_materials, engineering_epc, wind, rail, lithium, nickel, niobium, port_cranes,
power_plants_grid, fission_smr, solar, graphite, port_ownership, copper, bridges_roads,
balsa, water, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Atlas LatAm ~USD 2bn 3–4yr investment plan (CEO press
  proxy via Naturenews; soft floor). Equinix/Ascenty/ODATA CapEx dense.
PRC equal-budget: CapEx-fill CTG Arinos R$2.1bn on blank COD row (company balanço).
Other: NEW Votorantim Cimentos 1T26 CapEx R$742m; Energisa 2T26 R$1.713bn + 6M26
  R$3.267bn; Santos Brasil Tecon Santos R$2.6bn 2019–2031 program + R$1.6bn invested.
Skipped: thin dry; holdovers unsigned; Votorantim 2T26/Brazil plan already nested.
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


# 1. building_materials / other — NEW Votorantim Cimentos 1T26 CapEx R$742m
row_doc(
    "votorantim_cimentos_1t26_capex_742m_brl",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — 1T26 CapEx R$742m",
    "Brazil",
    "Votorantim Cimentos English company results (1Q26): investments (Capex) in the quarter totaled R$742 million, up 35% vs 1Q25; 21% directed to expansion; Edealina mill startup cited. CapEx: enter R$742m 1T26 face. Distinct from votorantim_cimentos_2t26_capex_803m_brl and Brazil plan cumulative rows.",
    "742000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Votorantim Cimentos Brazil footprint (São Paulo HQ pin; Edealina GO expansion cited).",
    "votorantim_cimentos_1q26_results",
    "Investments (Capex) in the quarter totaled R$742 million, 35% higher than in 1Q25. … Of the total amount, 21% was directed to expansion projects.",
    "https://www.votorantimcimentos.com/news/our-financial-results-in-the-first-quarter-of-2026/",
    "Actor: Votorantim Cimentos (Brazilian) — other. NEW 1T26 CapEx R$742m. Shuffle building_materials.",
    "hunt_cycle266", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(742000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Votorantim Cimentos. “Our Financial Results in the First Quarter of 2026.” 2026. https://www.votorantimcimentos.com/news/our-financial-results-in-the-first-quarter-of-2026/.',
    annotation="Votorantim Cimentos 1T26 CapEx R$742m via Fed H.10. Supports votorantim_cimentos_1t26_capex_742m_brl.",
    evid_note="Opened Votorantim Cimentos English company 1Q26 results; CapEx R$742m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. solar / us — NEW Atlas LatAm ~USD 2bn 3–4yr investment plan (proxy)
row_doc(
    "atlas_latam_2bn_plan_2026",
    "energy", "solar", "us",
    "Atlas Renewable Energy — LatAm investment plan ~USD 2bn (3–4 years)",
    "Chile",
    "9 Mar 2026 Naturenews (citing Atlas CEO Carlos Barrera): Atlas plans to invest about US$2bn in Latin America over the next three to four years; expected focus mainly Chile and Mexico as Brazil faces curtailment. CapEx: enter USD 2bn soft plan floor. Distinct from atlas_latam_3bn_refi_2026 refinancing and project-level finance rows. UNVERIFIED proxy (press citing CEO).",
    "2000000000", "2026-03-09", "2026", "-33.45", "-70.66",
    "Atlas LatAm solar/BESS footprint (Santiago pin; Chile/Mexico focus cited).",
    "naturenews_atlas_2bn_20260309",
    "Atlas Renewable Energy plans to invest about US$2bn in Latin America over the next three to four years, with investments expected to focus mainly on Chile and Mexico as Brazil faces ongoing power curtailment challenges, according to the company’s CEO Carlos Barrera.",
    "https://naturenews.africa/atlas-renewable-energy-plans-2bn-investment-in-latin-america/",
    "Actor: Atlas Renewable Energy (GIP/U.S.-backed) — us. NEW soft LatAm CapEx plan ~USD 2bn. Shuffle solar; ≥1/3 U.S. hunt. UNVERIFIED proxy.",
    "hunt_cycle266", investment_type="capex_plan", evidence="proxy", currency="USD",
    chicago='Naturenews Africa. “Atlas renewable energy plans $2bn investment in latin America” (citing CEO Carlos Barrera). March 9, 2026. https://naturenews.africa/atlas-renewable-energy-plans-2bn-investment-in-latin-america/.',
    annotation="Atlas LatAm ~USD 2bn 3–4yr plan via CEO press (proxy). Supports atlas_latam_2bn_plan_2026.",
    evid_note="Opened Naturenews English article citing Atlas CEO; ~USD 2bn LatAm over 3–4 years confirmed. Soft plan floor; UNVERIFIED proxy.",
    bib_type="press",
)

# 3. solar / prc — CapEx-fill CTG Arinos R$2.1bn on blank COD row
row_doc(
    "ctg_arinos_solar_full_cod_2025",
    "energy", "solar", "prc",
    "CTG Brasil — Complexo Solar Fotovoltaico Arinos CapEx R$2.1bn",
    "Brazil",
    "China Three Gorges Brasil Energia S.A. 2024 balanço (Estadão RI republication of company filing): Complexo Solar Fotovoltaico Arinos — investimento total estimado de R$2.1 bilhões; 412 MWp (340 MWac); first greenfield built by CTG Brasil; last stage completed Dec 2024. CapEx-fill: enter R$2.1bn face on prior CapEx-blank COD row. Distinct from huawei_ctg_arinos_inv_2022 inverter package.",
    "2100000000", "2024-12-31", "2025", "-15.92", "-46.11",
    "Arinos, Minas Gerais, Brazil (Complexo Solar Arinos; municipal pin).",
    "ctg_brasil_balanco_2024_arinos_21bn",
    "Com investimento total estimado de R$ 2,1 bilhões e capacidade instalada de 412 MWp (340 MWac), representa o primeiro projeto greenfield construído pela CTG Brasil.",
    "https://estadaori.estadao.com.br/wp-content/uploads/2025/03/china-three-gorges-brasil-energia-sa-balanco-2025-03-14_01-46-59.pdf",
    "Actor: CTG Brasil / China Three Gorges — prc. CapEx-fill upgrade: R$2.1bn company balanço face on prior blank COD row. Shuffle solar / PRC equal-budget.",
    "hunt_cycle266", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(2100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='China Three Gorges Brasil Energia S.A. “Demonstrações financeiras / Balanço 2024” (Arinos CapEx). Republished Estadão RI, March 2025. https://estadaori.estadao.com.br/wp-content/uploads/2025/03/china-three-gorges-brasil-energia-sa-balanco-2025-03-14_01-46-59.pdf.',
    annotation="CTG Arinos CapEx R$2.1bn via Fed H.10. Supports ctg_arinos_solar_full_cod_2025.",
    evid_note="Opened CTG Brasil company balanço PDF (Estadão RI republication); Arinos investimento total estimado R$2.1bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Energisa 2T26 CapEx R$1.713bn
row_doc(
    "energisa_2t26_capex_1713m_brl",
    "energy", "power_plants_grid", "other",
    "Energisa — 2T26 CapEx R$1.713bn",
    "Brazil",
    "6 Aug 2026 Energisa S.A. Release de Resultados 2T26 (company MZ IQ PDF): Investimentos R$1.713 billion in 2T26 (+7% vs 2T25 R$1.604bn); mainly distribution networks and gas. CapEx: enter R$1.713bn 2T26 face. Nested vs 6M26 / 2026 plan R$7.091bn (not additive).",
    "1713000000", "2026-06-30", "2026", "-21.39", "-42.70",
    "Energisa Brazil multi-concession distribution footprint (Cataguases HQ pin).",
    "energisa_2t26_release_20260806",
    "Investimentos 1.713 1.604 + 7 3.267 2.932 + 11 … No 2T26, os investimentos consolidados totalizaram R$ 1,7 bilhão (+7% vs. 2T25)",
    "https://api.mziq.com/mzfilemanager/v2/d/60f49a2d-bd8c-4fd9-95ab-bdf833097a83/c4a851a2-10c3-3c55-3d68-fcf7f6306b96?origin=2",
    "Actor: Energisa S.A. (Brazilian utility) — other. NEW 2T26 CapEx R$1.713bn. Shuffle power_plants_grid.",
    "hunt_cycle266", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1713000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Energisa S.A. “Release de Resultados 2T26.” August 6, 2026. https://api.mziq.com/mzfilemanager/v2/d/60f49a2d-bd8c-4fd9-95ab-bdf833097a83/c4a851a2-10c3-3c55-3d68-fcf7f6306b96?origin=2.',
    annotation="Energisa 2T26/6M26 CapEx via Fed H.10. Supports energisa_2t26_capex_1713m_brl; energisa_6m26_capex_3267m_brl.",
    evid_note="Opened Energisa company 2T26 MZ IQ PDF; CapEx R$1.713bn 2T26 / R$3.267bn 6M26 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / other — NEW Energisa 6M26 CapEx R$3.267bn
row_doc(
    "energisa_6m26_capex_3267m_brl",
    "energy", "power_plants_grid", "other",
    "Energisa — 6M26 CapEx R$3.267bn",
    "Brazil",
    "Energisa 2T26 earnings release: Investimentos 6M26 R$3.267 billion (+11% vs 6M25 R$2.932bn). CapEx: enter R$3.267bn 6M26 face. Nested vs 2T26 spent and energisa_2026_capex_plan_7p091bn_brl (not additive).",
    "3267000000", "2026-06-30", "2026", "-21.39", "-42.70",
    "Energisa Brazil multi-concession distribution footprint (Cataguases HQ pin).",
    "energisa_2t26_release_20260806",
    "Investimentos … 3.267 2.932 + 11",
    "https://api.mziq.com/mzfilemanager/v2/d/60f49a2d-bd8c-4fd9-95ab-bdf833097a83/c4a851a2-10c3-3c55-3d68-fcf7f6306b96?origin=2",
    "Actor: Energisa S.A. — other. NEW nested 6M26 CapEx R$3.267bn. Shuffle power_plants_grid.",
    "hunt_cycle266", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3267000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Energisa S.A. “Release de Resultados 2T26.” August 6, 2026. https://api.mziq.com/mzfilemanager/v2/d/60f49a2d-bd8c-4fd9-95ab-bdf833097a83/c4a851a2-10c3-3c55-3d68-fcf7f6306b96?origin=2.',
    annotation="Energisa 2T26/6M26 CapEx via Fed H.10. Supports energisa_2t26_capex_1713m_brl; energisa_6m26_capex_3267m_brl.",
    evid_note="Opened Energisa company 2T26 release; 6M26 CapEx R$3.267bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. port_ownership / other — NEW Santos Brasil Tecon Santos R$2.6bn program
row_doc(
    "santos_brasil_tecon_2p6bn_brl_2019_2031",
    "infrastructure", "port_ownership", "other",
    "Santos Brasil — Tecon Santos CapEx program R$2.6bn (2019–2031)",
    "Brazil",
    "Santos Brasil company Portuguese news (Jul 2025 traffic record): between 2019 and 2031 the company will allocate cerca de R$2.6 bilhões to Tecon Santos (quay deepening/extension; yard expansion toward 3m TEU/year; electric RTGs / remote STS). CapEx: enter R$2.6bn program face. Distinct from ZPMC equipment package rows and invested R$1.6bn nested row.",
    "2600000000", "2025-07-01", "2025", "-23.95", "-46.30",
    "Tecon Santos, Porto de Santos, São Paulo (company geography).",
    "santos_brasil_tecon_record_202507",
    "Entre 2019 e 2031, a empresa destinará cerca de R$ 2,6 bilhões ao Tecon Santos, dos quais R$ 1,6 bilhão já investido até maio de 2025.",
    "https://www.santosbrasil.com.br/v2021/noticia/santos-brasil-movimenta-135-mil-conteineres-no-tecon-santos-em-julho-e-bate-novo-recorde-historico",
    "Actor: Santos Brasil Participações — other. NEW Tecon Santos CapEx program R$2.6bn. Shuffle port_ownership.",
    "hunt_cycle266", investment_type="capex_program", evidence="documented", currency="BRL",
    value_usd=str(round(2600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Santos Brasil. “Santos Brasil movimenta 135 mil contêineres no Tecon Santos em julho e bate novo recorde histórico.” 2025. https://www.santosbrasil.com.br/v2021/noticia/santos-brasil-movimenta-135-mil-conteineres-no-tecon-santos-em-julho-e-bate-novo-recorde-historico.',
    annotation="Santos Brasil Tecon R$2.6bn program + R$1.6bn invested via Fed H.10. Supports santos_brasil_tecon_2p6bn_brl_2019_2031; santos_brasil_tecon_invested_1p6bn_may2025.",
    evid_note="Opened Santos Brasil company Portuguese news; Tecon Santos R$2.6bn 2019–2031 and R$1.6bn invested through May 2025 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. port_ownership / other — NEW Santos Brasil Tecon invested R$1.6bn through May 2025
row_doc(
    "santos_brasil_tecon_invested_1p6bn_may2025",
    "infrastructure", "port_ownership", "other",
    "Santos Brasil — Tecon Santos CapEx spent R$1.6bn through May 2025",
    "Brazil",
    "Santos Brasil company news: of the R$2.6bn 2019–2031 Tecon Santos program, R$1.6 billion already invested through May 2025. CapEx: enter R$1.6bn spent face. Nested within santos_brasil_tecon_2p6bn_brl_2019_2031 (not additive).",
    "1600000000", "2025-05-31", "2025", "-23.95", "-46.30",
    "Tecon Santos, Porto de Santos, São Paulo (company geography).",
    "santos_brasil_tecon_record_202507",
    "dos quais R$ 1,6 bilhão já investido até maio de 2025",
    "https://www.santosbrasil.com.br/v2021/noticia/santos-brasil-movimenta-135-mil-conteineres-no-tecon-santos-em-julho-e-bate-novo-recorde-historico",
    "Actor: Santos Brasil — other. NEW nested Tecon spent CapEx R$1.6bn through May 2025. Shuffle port_ownership.",
    "hunt_cycle266", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Santos Brasil. “Santos Brasil movimenta 135 mil contêineres no Tecon Santos em julho e bate novo recorde histórico.” 2025. https://www.santosbrasil.com.br/v2021/noticia/santos-brasil-movimenta-135-mil-conteineres-no-tecon-santos-em-julho-e-bate-novo-recorde-historico.',
    annotation="Santos Brasil Tecon R$2.6bn program + R$1.6bn invested via Fed H.10. Supports santos_brasil_tecon_2p6bn_brl_2019_2031; santos_brasil_tecon_invested_1p6bn_may2025.",
    evid_note="Opened Santos Brasil company news; R$1.6bn invested through May 2025 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle266 added {len(added)}: {added}")
    print(f"cycle266 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
