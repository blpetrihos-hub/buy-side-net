#!/usr/bin/env python3
"""Cycle 239 hunt: shuffle_seed=20261239; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261239).shuffle):
power_plants_grid, building_materials, engineering_epc, port_cranes, copper,
bridges_roads, rail, water, port_ownership, other_renewables, niobium, balsa,
fission_smr, wind, graphite, solar, nickel, lithium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: CapEx-fill Halliburton YPF ZEUS multibillion soft floor
  USD 2bn; honest residual Oceaneering/Wabtec/Progress Rail/Equinix/AES sweeps
  (US blank-USD CapEx residual exhausted after cycle 235; Progress Rail VLI R$200m
  already CapEx-filled).
PRC equal-budget: CapEx-fill Envision Casa dos Ventos 630 MW MME USD 800m floor.
NEW allied: ArcelorMittal/Casa dos Ventos Babilônia Centro wind R$4.2bn COD;
  nested Babilônia Centro solar R$700m (same JV complex).
Skipped: RAP-as-CapEx; Huaxin–CSN; Xinhai MoU; Aldesa EUR; Baker Hughes
  turbomachinery USD (BriefGlance $500m+ not on company primary); COP/CLP/PEN;
  holdovers unsigned; thin balsa/nickel/fission dry.
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


# 1. engineering_epc / us — CapEx-fill Halliburton YPF ZEUS multibillion soft floor USD 2bn
row_doc(
    "halliburton_ypf_zeus_vaca_muerta_2026",
    "infrastructure", "engineering_epc", "us",
    "Halliburton — multibillion YPF Vaca Muerta ZEUS electric frac completions (Argentina)",
    "Argentina",
    "13 Apr 2026 Halliburton: YPF awards Halliburton a multibillion-dollar exclusive multi-year bundled unconventional completions contract in Vaca Muerta; first international deployment of ZEUS electric fracturing services plus OCTIV Auto Frac. CapEx-fill: enter USD 2bn soft floor of company-stated multibillion-dollar range (multi ≥ 2).",
    "2000000000", "2026-04-13", "2026", "-38.95", "-69.20",
    "Vaca Muerta / Neuquén Basin (YPF unconventional geography; approximate basin pin).",
    "halliburton_ypf_zeus_20260413",
    "Halliburton (NYSE: HAL) announced today it was awarded a multibillion-dollar contract by YPF to provide bundled unconventional completions services in the Vaca Muerta… Under the contract, Halliburton will utilize its ZEUS® electric fracturing services in its first international deployment.",
    "https://www.halliburton.com/en/about-us/press-release/ypf-awards-halliburton-multibillion-dollar-long-term-unconventional-completions-contract-argentina",
    "Actor: Halliburton (U.S.) — us; client YPF. CapEx-fill: enter USD 2bn soft floor of company multibillion-dollar face (analogous to ANDRITZ mid-three-digit EUR → EUR 300m). Exact USD still undisclosed beyond multibillion. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle239", investment_type="epc", evidence="documented", currency="USD",
    value_usd="2000000000", fx_usd="1",
    chicago='Halliburton. “YPF Awards Halliburton Multibillion-Dollar Long-Term Unconventional Completions Contract in Argentina.” Press release, April 13, 2026. https://www.halliburton.com/en/about-us/press-release/ypf-awards-halliburton-multibillion-dollar-long-term-unconventional-completions-contract-argentina.',
    annotation="Halliburton YPF ZEUS CapEx-fill USD 2bn multibillion soft floor. Supports halliburton_ypf_zeus_vaca_muerta_2026.",
    evid_note="Opened Halliburton English primary; multibillion-dollar / ZEUS first international / OCTIV Auto Frac confirmed. CapEx-fill enter USD 2bn soft floor of multibillion.",
)

# 2. wind / prc — CapEx-fill Envision Casa dos Ventos 630 MW USD 800m MME floor
row_doc(
    "envision_casa_ventos_630mw_2026",
    "energy", "wind", "prc",
    "Envision Energy — 630 MW wind turbine supply + 30-year service to Casa dos Ventos (Brazil)",
    "Brazil",
    "8 Jan 2026 Envision: 630 MW supply of customized 8.x MW Galileo AI turbines with 30-year LTSA to Casa dos Ventos (first large Brazil net-zero wind partnership). CapEx-fill: MME (via MegaWhat 20 Jan 2026) states equipment + associated services commitment may exceed USD 800 million over the contractual cycle — enter USD 800m floor (UNVERIFIED proxy; not on Envision PR Newswire page).",
    "800000000", "2026-01-20", "2026", "-8.0", "-45.0",
    "Casa dos Ventos Brazil wind partnership (Envision PR); no single farm pin on the opened release — approximate NE Brazil wind belt.",
    "megawhat_mme_envision_800m_20260120",
    "Para o MME, o contrato de serviços de longo prazo firmado com a Envision é um sinal concreto de confiança no mercado brasileiro. Segundo a pasta, o conjunto do fornecimento de equipamentos e dos serviços associados representa um compromisso econômico que pode ultrapassar US$ 800 milhões ao longo do ciclo contratual.",
    "https://megawhat.uol.com.br/economia-e-politica/envision-energy-quer-ampliar-investimentos-em-energia-no-brasil-diz-mme/",
    "Actor: Envision Energy (PRC) — prc; customer Casa dos Ventos. CapEx-fill: enter USD 800m MME floor (UNVERIFIED proxy via MegaWhat citing MME). Distinct from Vestas Dom Inocêncio / Goldwind Sento Sé OEM rows. Shuffle wind / PRC equal-budget.",
    "hunt_cycle239", investment_type="equipment_supply", evidence="proxy", currency="USD",
    value_usd="800000000", fx_usd="1", bib_type="press",
    chicago='Souto, Poliana. “Envision Energy quer ampliar investimentos em energia no Brasil, diz MME.” MegaWhat, January 20, 2026. https://megawhat.uol.com.br/economia-e-politica/envision-energy-quer-ampliar-investimentos-em-energia-no-brasil-diz-mme/.',
    annotation="Envision Casa dos Ventos CapEx-fill USD 800m MME floor (proxy). Supports envision_casa_ventos_630mw_2026.",
    evid_note="Opened MegaWhat Portuguese citing MME; >USD 800m equipment+services cycle / 630 MW / 30-year LTSA confirmed. CapEx-fill enter USD 800m floor as UNVERIFIED proxy.",
)

# 3. wind / allied — NEW ArcelorMittal / Casa dos Ventos Babilônia Centro R$4.2bn COD
row_doc(
    "arcelormittal_babilonia_centro_wind_4p2bn_2025",
    "energy", "wind", "allied",
    "ArcelorMittal / Casa dos Ventos JV — Complexo Babilônia Centro wind (Bahia)",
    "Brazil",
    "25 Nov 2025 ArcelorMittal Brasil: full commercial operation of Complexo Babilônia Centro wind park in Várzea Nova (Bahia) — 123 turbines, 553.5 MW, ANEEL 35-year grant; total investment R$4.2 billion; JV with Casa dos Ventos (formed Apr 2023; ArcelorMittal 55% / Casa 45% on original corporate announcement). CapEx: enter R$4.2bn COD face; Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~808.54m. Distinct from Vestas 2023 Casa dos Ventos OEM row and Atlas Luiz Carlos solar (Paracatu).",
    "4200000000", BRL_FX_DATE, "2025", "-11.25", "-40.95",
    "Complexo Babilônia Centro, Várzea Nova, Bahia (company geography; municipal pin).",
    "arcelormittal_babilonia_centro_cod_20251125",
    "O parque eólico foi concluído de forma antecipada em julho, com 123 aerogeradores e completamente conectado ao Sistema Interligado Nacional, tendo sua operação comercial plena autorizada em outubro. O investimento total foi de R$ 4,2 bilhões, e a capacidade de geração é de 553,5 MW de energia.",
    "https://brasil.arcelormittal.com/box_templates/NEWS/809e49d6-0be9-4644-93af-ea6b781afa43",
    "Actor: ArcelorMittal (Luxembourg HQ / Europe steel) — allied; JV partner Casa dos Ventos (Brazil). Company Portuguese primary COD CapEx R$4.2bn. Shuffle wind.",
    "hunt_cycle239", investment_type="greenfield_generation", evidence="documented", currency="BRL",
    value_usd=str(round(4200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ArcelorMittal Brasil. “ArcelorMittal e Casa dos Ventos antecipam operação comercial plena de parque eólico.” November 25, 2025. https://brasil.arcelormittal.com/box_templates/NEWS/809e49d6-0be9-4644-93af-ea6b781afa43.',
    annotation="ArcelorMittal Babilônia Centro wind NEW ~USD 808.54m via Fed H.10. Supports arcelormittal_babilonia_centro_wind_4p2bn_2025.",
    evid_note="Opened ArcelorMittal Brasil Portuguese; R$4.2bn / 553.5 MW / 123 turbines / Várzea Nova COD confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. solar / allied — NEW nested Babilônia Centro solar R$700m (same JV complex)
row_doc(
    "arcelormittal_babilonia_centro_solar_700m_2025",
    "energy", "solar", "allied",
    "ArcelorMittal / Casa dos Ventos JV — Babilônia Centro solar expansion (Bahia)",
    "Brazil",
    "25 Nov 2025 ArcelorMittal Brasil (same COD release): second JV with Casa dos Ventos for ~200 MW solar at Complexo Babilônia Centro between Morro do Chapéu and Várzea Nova; approximately R$700 million invested; commercial operation targeted December 2025. CapEx: enter R$700m face; Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~134.82m. Nested within Babilônia Centro hybrid complex (distinct from wind R$4.2bn row).",
    "700000000", BRL_FX_DATE, "2025", "-11.55", "-41.15",
    "Babilônia Centro solar / Morro do Chapéu–Várzea Nova, Bahia (company geography).",
    "arcelormittal_babilonia_centro_cod_20251125",
    "Em agosto do ano passado, a parceria entre as partes foi ampliada com a criação de mais uma joint venture para a implantação de um projeto de energia solar, também no Complexo Babilônia Centro, entre os municípios de Morro do Chapéu e Várzea Nova, na Bahia. Neste novo acordo, estão sendo investidos aproximadamente R$ 700 milhões para uma usina de 200 MW de potência instalada.",
    "https://brasil.arcelormittal.com/box_templates/NEWS/809e49d6-0be9-4644-93af-ea6b781afa43",
    "Actor: ArcelorMittal — allied; JV partner Casa dos Ventos. Nested solar CapEx within Babilônia Centro hybrid. Distinct from atlas_luiz_carlos_side_b (Paracatu) and nextracker_casa_dos_ventos tracker OEM. Shuffle solar.",
    "hunt_cycle239", investment_type="greenfield_generation", evidence="documented", currency="BRL",
    value_usd=str(round(700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ArcelorMittal Brasil. “ArcelorMittal e Casa dos Ventos antecipam operação comercial plena de parque eólico.” November 25, 2025. https://brasil.arcelormittal.com/box_templates/NEWS/809e49d6-0be9-4644-93af-ea6b781afa43.',
    annotation="ArcelorMittal Babilônia Centro solar NEW ~USD 134.82m via Fed H.10. Supports arcelormittal_babilonia_centro_solar_700m_2025.",
    evid_note="Opened ArcelorMittal Brasil Portuguese; ~R$700m / 200 MW solar / Morro do Chapéu–Várzea Nova confirmed on same COD page. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle239 added {len(added)}: {added}")
    print(f"cycle239 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
