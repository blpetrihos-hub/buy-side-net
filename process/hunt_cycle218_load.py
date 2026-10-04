#!/usr/bin/env python3
"""Cycle 218 hunt: shuffle_seed=20261218; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261218).shuffle):
nickel, fission_smr, wind, port_cranes, engineering_epc, niobium, bridges_roads,
balsa, rail, graphite, lithium, solar, other_renewables, power_plants_grid,
building_materials, copper, port_ownership, water.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry this cycle; next-thinnest niobium CapEx-fill (CBMM Araxá 2026 spend R$2bn).
≥1/3 U.S. hunt budget spent on Progress Rail VLI SD70 + Wabtec Vale EFC MSA
CapEx-fills + Jervois / DFC Piauí / Freeport / EnergyX / EXIM / Bechtel / Fluor /
Wabtec Contagem / SSA / USTDA / Nextracker sweeps (2 US CapEx-fills; catalog dense).
PRC equal-budget: Goldwind Sento Sé / Envision Casa / Sungrow BHP / ZPMC /
PowerChina / CAMCE already logged; holdovers unsigned. No distinct new CapEx rows
opened this pass beyond CapEx-fills (catalog dense mid-200s).
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


# 1. rail / us — CapEx-fill Progress Rail VLI eight SD70 ~R$200m
row_doc(
    "progress_rail_vli_sd70_200m_brl_2024",
    "infrastructure",
    "rail",
    "us",
    "Progress Rail (Caterpillar) — eight EMD SD70ACe-BB locomotives CapEx for VLI (FCA)",
    "Brazil",
    "10 Feb 2026 VLI: celebrates delivery of final units of eight EMD SD70ACe-BB locomotives from Progress Rail for Centro-Atlântica Railway; machines acquired in 2024 with investment of about R$ 200 million; manufactured Sete Lagoas (MG). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~38.52m for stored R$200m face. Distinct from progress_rail_vli_sd70_2026 (delivery presence; CapEx blank on Progress Rail page) and progress_rail_vli_msa_norte_500m_brl_2025 (MSA services).",
    "200000000",
    BRL_FX_DATE,
    "2024",
    "-19.466",
    "-44.247",
    "Progress Rail Sete Lagoas plant / FCA delivery, Minas Gerais, Brazil (VLI/InvestMinas geography; approximate plant pin).",
    "vli_progress_rail_delivery_20260210",
    "As máquinas foram adquiridas em 2024, com um investimento de cerca de R$ 200 milhões, que reforça o compromisso da VLI de integrar regiões e impulsionar a indústria ferroviária nacional.",
    "https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/",
    "Actor: Progress Rail (Caterpillar Inc., U.S.) OEM — us; buyer VLI (Brazil). VLI Portuguese primary. CapEx-fill: retain R$200m; add Fed H.10 Sep 25 2026 FX to USD ~38.52m. ≥1/3 U.S. hunt / shuffle rail.",
    "hunt_cycle218",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(200000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="company",
    chicago='VLI Logística. “VLI e Progress Rail celebram recebimento de locomotivas para operação na Ferrovia Centro-Atlântica.” February 10, 2026. https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/.',
    annotation="Progress Rail VLI SD70 CapEx-fill ~USD 38.52m via Fed H.10. Supports progress_rail_vli_sd70_200m_brl_2024.",
    evid_note="Opened VLI Portuguese release; ~R$200m / eight SD70ACe-BB / Sete Lagoas confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. rail / us — CapEx-fill Wabtec Vale EFC MSA R$1.8bn
row_doc(
    "wabtec_vale_efc_msa_1p8bn_brl_2024",
    "infrastructure",
    "rail",
    "us",
    "Wabtec — 10-year MSA for Vale EFC Evolution Series locomotive fleet",
    "Brazil",
    "5 Jun 2024 Wabtec: master service agreement with Vale valued at R$ 1.8 billion over 10 years to optimize maintenance of Evolution Series (EVO) locomotives on Estrada de Ferro Carajás (EFC); real-time monitoring of 5,000 parameters; Global Performance Optimization Centers; jobs/training in São Luís. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~346.68m for stored R$1.8bn face. Distinct from wabtec_vale_ptc_brl1bn_2026 (I-ETMS PTC) and wabtec_vale_50_locos_2026 (new locomotives).",
    "1800000000",
    BRL_FX_DATE,
    "2024",
    "-2.53",
    "-44.30",
    "Pinned to São Luís / EFC Maranhão terminus (company geography; approximate).",
    "wabtec_vale_efc_msa_20240605",
    "The strategic 10-year deal, valued at R$1.8 billion, will optimize the maintenance services for Vale’s fleet increasing performance, reliability, and the potential for expanded freight transport on the EFC connecting the southeast of Pará to the capital of Maranhão, São Luís.",
    "https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-an-r18b-services-agreement-to-enhance-caraj-s-railway-locomotive-fleet",
    "Actor: Wabtec Corporation (U.S., NYSE:WAB) — us; customer Vale. Company English primary. CapEx-fill: retain R$1.8bn; add Fed H.10 Sep 25 2026 FX to USD ~346.68m. ≥1/3 U.S. hunt / shuffle rail.",
    "hunt_cycle218",
    investment_type="services_contract",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(1800000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="company",
    chicago='Wabtec Corporation. “Vale and Wabtec Sign an R$1.8B Services Agreement to Enhance Carajás Railway Locomotive Fleet.” June 5, 2024. https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-an-r18b-services-agreement-to-enhance-caraj-s-railway-locomotive-fleet.',
    annotation="Wabtec Vale EFC MSA CapEx-fill ~USD 346.68m via Fed H.10. Supports wabtec_vale_efc_msa_1p8bn_brl_2024.",
    evid_note="Opened Wabtec English primary; R$1.8bn / 10-year MSA / EFC EVO fleet confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. wind / allied — CapEx-fill Vestas Dom Inocêncio >R$5bn floor
row_doc(
    "vestas_dom_inocencio_br_2025",
    "energy",
    "wind",
    "allied",
    "Vestas — Dom Inocêncio 828 MW turbine supply (Casa dos Ventos / Piauí)",
    "Brazil",
    "17 Dec 2025 Vestas: Casa dos Ventos orders 184 × V150-4.5 MW turbines (828 MW) for Dom Inocêncio wind complex (Lagoa do Barro / Queimada Nova, Piauí) with construction management + 25-year AOM 5000; company states total investment over BRL 5 billion; construction 2026–2028. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~963.00m for stored R$5bn floor face. Distinct from vestas_esquina_do_vento_230mw_2026 and Envision/Goldwind Casa dos Ventos rows.",
    "5000000000",
    BRL_FX_DATE,
    "2025",
    "-8.75",
    "-41.20",
    "Dom Inocêncio / Lagoa do Barro–Queimada Nova, Piauí (company geography; approximate complex pin).",
    "vestas_dom_inocencio_20251217",
    "Casa dos Ventos ... and Vestas ... announce ... the 828 MW order for the Dom Inocêncio wind complex. ... The project will feature 184 V150-4.5 MW turbines ... The project represents a total investment of over BRL 5 billion",
    "https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083",
    "Actor: Vestas (Denmark) — allied; developer Casa dos Ventos (Brazil). Company English primary. CapEx-fill: retain R$5bn floor; add Fed H.10 Sep 25 2026 FX to USD ~963.00m. Shuffle wind.",
    "hunt_cycle218",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(5000000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="company",
    chicago='Vestas. “Casa dos Ventos and Vestas announce new partnership for the 828 MW Dom Inocêncio Wind Complex in Brazil.” December 17, 2025. https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083.',
    annotation="Vestas Dom Inocêncio CapEx-fill ~USD 963.00m via Fed H.10. Supports vestas_dom_inocencio_br_2025.",
    evid_note="Opened Vestas company primary; >BRL 5bn / 184×V150-4.5 MW / 828 MW / AOM 5000 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. power_plants_grid / allied — CapEx-fill ENGIE Brasil ANEEL 01/2026 ~R$1.5bn
row_doc(
    "engie_brasil_aneel_01_2026_15bn",
    "energy",
    "power_plants_grid",
    "allied",
    "ENGIE Brasil — ANEEL Transmission Auction 01/2026 Lots 2 + 3A–3D",
    "Brazil",
    "27 Mar 2026 ENGIE Brasil: subsidiary ENGIE Transmissão de Energia Participações wins Lot 2 (PR/SC ~143 km 230 kV) and Lots 3A–3D synchronous compensators (RN/CE) at ANEEL Transmission Auction 01/2026 (B3); contracted RAP R$122.7 million; ANEEL-estimated total CapEx about R$1.5 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~288.90m for stored R$1.5bn face. 30-year concessions; 42-month build. Distinct from engie_peru_grupo1_transmision_230m_2026.",
    "1500000000",
    BRL_FX_DATE,
    "2026",
    "",
    "",
    "Multi-state transmission package (PR/SC Lot 2; RN/CE Lot 3) — lat/lon blank (multi-site).",
    "engie_brasil_aneel_01_20260327",
    "O lote 2 e os sublotes 3A, 3B, 3C e 3D foram arrematados com uma Receita Anual Permitida (RAP) de R$ 122,7 milhões e investimentos totais estimados pela ANEEL em cerca de R$ 1,5 bilhão",
    "https://www.engie.com.br/imprensa/press-releases/engie-arremata-lote-2-e-sublotes-do-3-no-leilao-da-aneel/",
    "Actor: ENGIE Brasil / ENGIE (France) — allied. Company Portuguese primary. CapEx-fill: retain R$1.5bn ANEEL estimate; add Fed H.10 Sep 25 2026 FX to USD ~288.90m. Shuffle power_plants_grid.",
    "hunt_cycle218",
    investment_type="concession",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="company",
    chicago='ENGIE Brasil. “ENGIE arremata Lote 2 e sublotes do 3 no Leilão da ANEEL.” March 27, 2026. https://www.engie.com.br/imprensa/press-releases/engie-arremata-lote-2-e-sublotes-do-3-no-leilao-da-aneel/.',
    annotation="ENGIE Brasil ANEEL 01/2026 CapEx-fill ~USD 288.90m via Fed H.10. Supports engie_brasil_aneel_01_2026_15bn.",
    evid_note="Opened ENGIE Brasil Portuguese release; ~R$1.5bn ANEEL CapEx / RAP R$122.7m / Lots 2+3A–3D confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. niobium / allied — CapEx-fill CBMM Araxá 2026 spend R$2bn (thin next-thinnest)
row_doc(
    "cbmm_araxa_2026_spend_2bn",
    "resources",
    "niobium",
    "allied",
    "CBMM — Araxá 2026 industrial Capex already executed",
    "Brazil",
    "Diário do Comércio 18 Sep 2026 citing CBMM note: company already invested R$ 2 billion in 2026 at Araxá industrial complex (new lines/plants; equipment acquisition/modernization), within broader R$13 billion multi-year program. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~385.20m for stored R$2bn face (UNVERIFIED proxy CapEx retained). Distinct from cbmm_araxa_13bn_plan_2026 multi-year envelope and cbmm_araxa_2025_spend_1p1bn.",
    "2000000000",
    BRL_FX_DATE,
    "2026",
    "-19.59",
    "-46.94",
    "CBMM Araxá complex, Minas Gerais.",
    "diario_comercio_cbmm_13bn_20260918",
    "Somente neste ano, a companhia já investiu R$ 2 bilhões em seu complexo industrial localizado em Araxá, no Alto Paranaíba, incluindo novas linhas e plantas, além da aquisição e modernização de equipamentos.",
    "https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/",
    "Actor: CBMM — allied. UNVERIFIED proxy CapEx R$2bn retained; CapEx-fill adds Fed H.10 Sep 25 2026 FX to USD ~385.20m. Thin niobium top-up (balsa/nickel/fission_smr dry).",
    "hunt_cycle218",
    investment_type="brownfield_expansion",
    evidence="proxy",
    currency="BRL",
    value_usd=str(round(2000000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="press",
    chicago='Diário do Comércio. “CBMM investe R$ 2 bilhões em 2026 no complexo de Araxá.” September 18, 2026. https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/.',
    annotation="CBMM Araxá 2026 spend CapEx-fill ~USD 385.20m via Fed H.10. Supports cbmm_araxa_2026_spend_2bn.",
    evid_note="Opened Diário do Comércio citing CBMM note; R$2bn 2026 executed spend confirmed (UNVERIFIED proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k == "id":
                    continue
                if v != "" and v is not None:
                    existing[k] = v
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
    print(f"cycle218 added {len(added)}: {added}")
    print(f"cycle218 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
