#!/usr/bin/env python3
"""Cycle 211 hunt: shuffle_seed=20261211; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261211).shuffle):
copper, engineering_epc, port_ownership, nickel, port_cranes, fission_smr, lithium,
other_renewables, rail, water, graphite, niobium, balsa, solar, power_plants_grid,
bridges_roads, building_materials, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Black Giant/DFC Serra/
EnergyX/Nextracker/Array/Wabtec MRS/GE Vernova São Simão/Bechtel Pelambres/
Fluence/USTDA/Equinix/Freeport El Abra/Newmont Yanacocha sweeps; CapEx-fill
bechtel_los_pelambres_inco_2024 (USD 2.2bn) + fluor_toromocho (USD 1.355bn)
count toward U.S. engineering_epc. PRC equal-budget: ZPMC MultiRio/Tecon RG /
CAMCE Bluefields / PowerChina Chile Decree 4 / State Grid UHV already logged;
holdovers unsigned.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. copper / other — Codelco buys Enami 10% of Teck Quebrada Blanca for USD 520m
row_doc(
    "codelco_enami_qb_10pct_520m_2024",
    "resources",
    "copper",
    "other",
    "Codelco — acquisition of Enami’s 10% stake in Compañía Minera Teck Quebrada Blanca",
    "Chile",
    "18 Dec 2024 Codelco/ENAMI: complete due diligence and second payment of USD 338 million, bringing total purchase price for Enami’s 10% of Compañía Minera Teck Quebrada Blanca to USD 520 million (first payment USD 182m at signing Sep 2024). Keeps stake in Chilean state ownership; Codelco joins Teck (60%) / Sumitomo (30%) ownership. Distinct from teck_quebrada_blanca_chile and teck_qb_tmf_420m_2026.",
    "520000000",
    "2024-12-18",
    "2024",
    "-20.95",
    "-68.85",
    "Quebrada Blanca mine, Tarapacá Region, Chile (company geography; approximate pin).",
    "codelco_enami_qb_20241218",
    "Codelco y ENAMI culminaron el proceso de due diligence por la compra del 10% de la Compañía Minera Teck Quebrada Blanca. Con el desembolso de US$ 338 millones se completó el precio de compra, el cual ascendió a un monto total de US$ 520 millones.",
    "https://www.codelco.com/codelco-y-enami-culminan-proceso-de-compraventa-del-10-de-la-compania",
    "Actor: Codelco (Chilean state copper SOE) buying from ENAMI (Chilean state) — other. Opened Codelco Spanish primary 18 Dec 2024. CapEx/transaction face = USD 520m. Shuffle copper.",
    "hunt_cycle211",
    investment_type="ownership_equity",
    evidence="documented",
    currency="USD",
    value_usd="520000000",
    fx_usd="1",
    bib_type="company",
    chicago='Codelco. “Codelco y ENAMI culminan proceso de compraventa del 10% de la Compañía Minera Teck Quebrada Blanca.” December 18, 2024. https://www.codelco.com/codelco-y-enami-culminan-proceso-de-compraventa-del-10-de-la-compania.',
    annotation="Codelco–ENAMI Quebrada Blanca 10% USD 520m. Supports codelco_enami_qb_10pct_520m_2024.",
    evid_note="Opened Codelco Spanish primary 2026-10-04; USD 520m total / USD 338m second payment / 10% Enami stake / Teck Quebrada Blanca confirmed.",
)

# 2. water / allied — Antofagasta Minera Los Pelambres water infrastructure financing USD 2bn
row_doc(
    "antofagasta_pelambres_water_financing_2bn_2025",
    "resources",
    "water",
    "allied",
    "Antofagasta Minerals / Minera Los Pelambres — water infrastructure project financing (desal expansion + transport)",
    "Chile",
    "18 Feb 2025 Antofagasta FY2024 results presentation: announces Los Pelambres infrastructure financing of USD 2 billion with two tranches (~9 years and 20 years) to fund water-infrastructure assets supporting desalination plant expansion to 800 l/s and associated transport/pumping (Future Growth Enabling Projects). LatinFinance later cites package as USD 1.55bn US private placement + USD 450m syndicated loan. Distinct from antofagasta_zaldivar_water_900m_2026 and antofagasta_2026_capex_guidance_3p4bn (group CapEx).",
    "2000000000",
    "2025-02-18",
    "2025",
    "-31.75",
    "-71.2",
    "Los Pelambres desalination / water transport corridor, Coquimbo Region, Chile (company geography; approximate coastal pin).",
    "antofagasta_fy24_results_pres_20250218",
    "Los Pelambres: New financing • Announced February 2025 • Infrastructure financing ($2 billion) with two tranches (c.9 years and 20 years)",
    "https://www.antofagasta.co.uk/media/4748/20250218_anto-fy24-results-presentation-feb25-vf-low-res.pdf",
    "Actor: Antofagasta plc / Antofagasta Minerals (UK-listed Chilean copper major) — allied. Company FY2024 results presentation 18 Feb 2025. Financing face = USD 2bn for Los Pelambres water infrastructure (desal expansion to 800 l/s + transport). Shuffle water.",
    "hunt_cycle211",
    investment_type="financing",
    evidence="documented",
    currency="USD",
    value_usd="2000000000",
    fx_usd="1",
    bib_type="company",
    chicago='Antofagasta plc. “Focused on copper” FY2024 Results Presentation. February 18, 2025. https://www.antofagasta.co.uk/media/4748/20250218_anto-fy24-results-presentation-feb25-vf-low-res.pdf.',
    annotation="Antofagasta Los Pelambres water infrastructure financing USD 2bn. Supports antofagasta_pelambres_water_financing_2bn_2025.",
    evid_note="Opened Antofagasta FY2024 results presentation PDF 2026-10-04; Infrastructure financing ($2 billion) / two tranches ~9y and 20y / Feb 2025 / Los Pelambres desal-to-800 l/s context confirmed.",
)

# 3. engineering_epc / us — CapEx-fill Bechtel Los Pelambres INCO Phase 1 USD 2.2bn
row_doc(
    "bechtel_los_pelambres_inco_2024",
    "infrastructure",
    "engineering_epc",
    "us",
    "Antofagasta Minerals — Los Pelambres INCO MLP expansion",
    "Chile",
    "Bechtel EPC for Los Pelambres INCO MLP (concentrator expansion + 400 l/s desal + pipeline); inaugurated March 2024. CapEx-fill: Antofagasta HY2022 results raised Phase 1 capital cost estimate to USD 2.2 billion (from USD 1.7bn). Distinct from antofagasta_pelambres_water_financing_2bn_2025 (later desal-to-800 l/s financing).",
    "2200000000",
    "2022-08-17",
    "2024",
    "-31.72",
    "-71.25",
    "Los Pelambres / Coquimbo Region (Bechtel project page).",
    "antofagasta_hy2022_inco_capex",
    "A detailed review of the project schedule and costs was completed in Q1 2022 resulting in the capital cost estimate for Phase 1 being increased to $2.2 billion (from $1.7 billion).",
    "https://www.antofagasta.co.uk/media/4399/antofagasta-hy-2022-results-announcement.pdf",
    "Actor: Bechtel (U.S.) EPC for Antofagasta Minerals INCO — us. CapEx-fill upgrade from blank using Antofagasta HY2022 Phase 1 capital cost estimate USD 2.2bn. Shuffle engineering_epc.",
    "hunt_cycle211",
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd="2200000000",
    fx_usd="1",
    bib_type="company",
    chicago='Antofagasta plc. “Half Year Results for the Six Months Ended 30 June 2022.” August 17, 2022. https://www.antofagasta.co.uk/media/4399/antofagasta-hy-2022-results-announcement.pdf.',
    annotation="Los Pelambres INCO Phase 1 CapEx USD 2.2bn. Supports bechtel_los_pelambres_inco_2024 CapEx-fill.",
    evid_note="Opened Antofagasta HY2022 PDF 2026-10-04; Phase 1 capital cost estimate increased to $2.2 billion (from $1.7 billion) confirmed. CapEx-fill on prior Bechtel presence row.",
)

# 4. engineering_epc / us — CapEx-fill Fluor Toromocho expansion USD 1.355bn
row_doc(
    "fluor_toromocho_expansion_peru",
    "infrastructure",
    "engineering_epc",
    "us",
    "Fluor — Toromocho Expansion Project EPCm for Minera Chinalco Perú",
    "Peru",
    "Fluor EPCm for Toromocho copper mine expansion designed to raise copper output ~45% (toward ~300,000 tpy). CapEx-fill: Peruvian MINEM states expansion investment US$ 1,355 million for plant capacity increase toward 170,000 t/d. Distinct from chinalco_toromocho_peru ownership presence.",
    "1355000000",
    "2023-07-01",
    "2024",
    "-11.6",
    "-76.15",
    "Junín Region, Peru (Fluor project page; high-altitude Toromocho).",
    "minem_toromocho_ampliacion_1355m",
    "La ampliación del proyecto minero Toromocho… con inversión de US$ 1,355 millones.",
    "https://www.gob.pe/institucion/minem/noticias/759704-minem-ampliacion-del-proyecto-minero-toromocho-ingresa-a-su-etapa-final",
    "Actor: Fluor (U.S.) EPCm for Chinalco Perú (PRC owner) — us. CapEx-fill upgrade from blank using MINEM US$1.355bn expansion investment figure. Shuffle engineering_epc.",
    "hunt_cycle211",
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd="1355000000",
    fx_usd="1",
    bib_type="government",
    chicago='Ministerio de Energía y Minas (Perú). “MINEM: Ampliación del proyecto minero Toromocho ingresa a su etapa final.” https://www.gob.pe/institucion/minem/noticias/759704-minem-ampliacion-del-proyecto-minero-toromocho-ingresa-a-su-etapa-final.',
    annotation="Toromocho expansion CapEx USD 1.355bn. Supports fluor_toromocho_expansion_peru CapEx-fill.",
    evid_note="Opened MINEM Spanish primary 2026-10-04; US$ 1,355 millones expansion investment confirmed. CapEx-fill on prior Fluor EPCm presence row.",
)

# 5. wind / allied — CapEx-fill Statkraft Gran Sul R$1.5bn
row_doc(
    "statkraft_gran_sul_280mw_2026",
    "energy",
    "wind",
    "allied",
    "Statkraft — Gran Sul 280 MW onshore wind FID (Santa Vitória do Palmar, RS)",
    "Brazil",
    "8 Jul 2026 Statkraft: investment decision for Gran Sul 280 MW onshore wind in Santa Vitória do Palmar, Rio Grande do Sul; construction scheduled to begin January 2027; commercial operation targeted 2029. CapEx-fill: GaúchaZH 23 Jul 2026 reports investment superior to R$ 1.5 billion for first-phase 280 MW (Statkraft confirmed implementation schedule to the outlet). Distinct from vestas_emma_peru / statkraft_emma_peru rows.",
    "1500000000",
    "2026-07-23",
    "2026",
    "-33.519",
    "-53.368",
    "Santa Vitória do Palmar municipality, Rio Grande do Sul (company geography; municipal pin).",
    "gauchazh_statkraft_gran_sul_15bn_20260723",
    "Com investimento superior a R$ 1,5 bilhão, o Projeto Gran Sul, da empresa norueguesa Statkraft, tem início das obras previsto para janeiro do próximo ano. A primeira etapa contará com capacidade instalada de 280 megawatts (MW).",
    "https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/07/santa-vitoria-do-palmar-tera-novo-parque-eolico-com-investimento-de-r-15-bilhao-cmrwjwq0701370163akppasn7.html",
    "Actor: Statkraft AS (Norway) — allied. CapEx-fill: press R$1.5bn first-phase figure (company primary FID page omitted CapEx). USD blank (Fed H.10 unreachable). Shuffle wind.",
    "hunt_cycle211",
    investment_type="fid",
    evidence="proxy",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='Cosme, Laura. “Santa Vitória do Palmar terá novo parque eólico com investimento de R$ 1,5 bilhão.” GaúchaZH, July 23, 2026. https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/07/santa-vitoria-do-palmar-tera-novo-parque-eolico-com-investimento-de-r-15-bilhao-cmrwjwq0701370163akppasn7.html.',
    annotation="Statkraft Gran Sul CapEx-fill R$1.5bn (press). Supports statkraft_gran_sul_280mw_2026.",
    evid_note="Opened GaúchaZH 2026-10-04; R$1.5bn first-phase / 280 MW / Jan 2027 construction / 2029 COD confirmed. UNVERIFIED proxy vs company CapEx silence; CapEx-fill on prior FID row.",
)

# 6. other_renewables / other — Codelco MIGA-guaranteed climate financing USD 600m
row_doc(
    "codelco_miga_climate_financing_600m_2025",
    "energy",
    "other_renewables",
    "other",
    "Codelco — MIGA-guaranteed climate financing for energy-matrix decarbonization (HSBC / Santander)",
    "Chile",
    "31 Dec 2025 Codelco: secures USD 600 million climate financing from HSBC and Banco Santander, guaranteed by World Bank Group MIGA, to finance transition to a 100% renewable electricity mix by 2030 (PPA renewals with Engie, Colbún, AES Andes and new renewable tenders totaling 1.8 TWh/year). Adds to prior USD 532 million Crédit Agricole/MIGA climate financing in 2024. Distinct from codelco_enami_qb_10pct_520m_2024 copper stake purchase.",
    "600000000",
    "2025-12-31",
    "2025",
    "-33.45",
    "-70.66",
    "Codelco HQ / Chile system-wide renewable PPA program (Santiago pin; no single plant site).",
    "codelco_miga_climate_600m_20251231",
    "Codelco successfully secured US$600 million in climate financing from The Hongkong and Shanghai Banking Corporation Limited (HSBC) and Banco Santander, guaranteed by the Multilateral Investment Guarantee Agency (MIGA) of the World Bank Group, for the complete decarbonization of its energy matrix.",
    "https://www.codelco.com/codelco-completa-su-programa-de-financiamiento-climatico-asegurando",
    "Actor: Codelco (Chilean state copper SOE) borrower — other. Opened Codelco Spanish/English primary 31 Dec 2025. Financing face = USD 600m for renewable energy-matrix transition. Shuffle other_renewables.",
    "hunt_cycle211",
    investment_type="financing",
    evidence="documented",
    currency="USD",
    value_usd="600000000",
    fx_usd="1",
    bib_type="company",
    chicago='Codelco. “Codelco completa su programa de financiamiento climático asegurando nuevo crédito por US$ 600 millones.” December 31, 2025. https://www.codelco.com/codelco-completa-su-programa-de-financiamiento-climatico-asegurando.',
    annotation="Codelco MIGA climate financing USD 600m. Supports codelco_miga_climate_financing_600m_2025.",
    evid_note="Opened Codelco primary 2026-10-04; USD 600m HSBC/Santander / MIGA guarantee / renewable matrix to 2030 / prior USD 532m 2024 tranche mentioned confirmed.",
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
    added = []
    updated = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
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
    print(f"cycle211 added {len(added)}: {added}")
    print(f"cycle211 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
