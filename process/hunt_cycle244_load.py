#!/usr/bin/env python3
"""Cycle 244 hunt: shuffle_seed=20261244; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261244).shuffle):
bridges_roads, port_ownership, wind, fission_smr, rail, solar, port_cranes, niobium,
water, copper, power_plants_grid, building_materials, lithium, other_renewables,
nickel, graphite, engineering_epc, balsa.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: CapEx-fill Progress Rail VLI SD70 blank with ~R$200m
  (VLI company dual event); honest residual.
PRC equal-budget: NEW BYD Manaus bus-battery line expansion R$50m floor (Folha/Reuters).
Allied: NEW EDP Espírito Santo distribution CapEx ~R$5bn 2025–2030; NEW Neoenergia
  Cosern Estivas >R$100m nested.
Skipped: Ascenty Sumaré 3 USD 720m Valor breakout not on company English; Pacto
  Coronel Vivida R$30m Huawei-equipped but CapEx is Brazilian distributor (other);
  holdovers unsigned; thin dry.
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


# 1. rail / us — CapEx-fill Progress Rail VLI SD70 blank with ~R$200m
row_doc(
    "progress_rail_vli_sd70_2026",
    "infrastructure", "rail", "us",
    "Progress Rail (Caterpillar) — eight EMD SD70ACe-BB locomotives for VLI / FCA",
    "Brazil",
    "10 Feb 2026 Progress Rail English + VLI Portuguese same-day celebration: delivery of eight new EMD SD70ACe-BB locomotives for Ferrovia Centro-Atlântica; VLI states units acquired in 2024 with investment of about R$ 200 million (Sete Lagoas manufacture). CapEx-fill: enter R$200m face on Progress Rail company delivery row (companion progress_rail_vli_sd70_200m_brl_2024 already holds VLI CapEx; nested US seller row).",
    "200000000", "2026-02-10", "2026", "-19.47", "-44.25",
    "Progress Rail Sete Lagoas (MG) locomotive plant / FCA operations (Sete Lagoas pin).",
    "vli_progress_rail_sd70_200m_20260210",
    "As máquinas foram adquiridas em 2024, com um investimento de cerca de R$ 200 milhões, que reforça o compromisso da VLI de integrar regiões e impulsionar a indústria ferroviária nacional.",
    "https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/",
    "Actor: Progress Rail / Caterpillar (U.S.) — us. CapEx-fill blank Progress Rail delivery row with VLI ~R$200m acquisition CapEx (same event). Distinct from progress_rail_vli_msa_norte_500m_brl_2025 MSA. Shuffle rail / U.S. ≥1/3 budget.",
    "hunt_cycle244", investment_type="equipment_supply", evidence="documented", currency="BRL",
    value_usd=str(round(200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='VLI Logística. “VLI e Progress Rail celebram recebimento de locomotivas para operação na Ferrovia Centro-Atlântica.” February 10, 2026. https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/.',
    annotation="Progress Rail VLI SD70 CapEx-fill ~R$200m ~USD 38.52m via Fed H.10. Supports progress_rail_vli_sd70_2026.",
    evid_note="Opened VLI Portuguese (companion Progress Rail English confirms delivery/MSA without CapEx); ~R$200m eight SD70ACe-BB confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. other_renewables / prc — NEW BYD Manaus bus-battery line expansion R$50m floor
row_doc(
    "byd_manaus_bus_battery_50m_brl_2026",
    "energy", "other_renewables", "prc",
    "BYD — Manaus bus-battery production line expansion (R$50–60m)",
    "Brazil",
    "16 Jun 2026 Folha (Reuters interview with BYD SVP Alexandre Baldy): BYD is investing between R$ 50 million and R$ 60 million to expand a bus-battery production line (Manaus plant currently focused on bus batteries; separate from up-to-R$500m BESS factory decision and R$5.5bn Camaçari auto complex). CapEx: enter R$50m soft floor of stated range. Pin Manaus.",
    "50000000", "2026-06-16", "2026", "-3.12", "-60.02",
    "BYD Manaus bus-battery plant (municipal pin).",
    "folha_byd_manaus_battery_50m_20260616",
    "Paralelamente, a BYD está investindo entre R$ 50 milhões e R$ 60 milhões para expandir uma linha de produção de baterias para ônibus.",
    "https://www1.folha.uol.com.br/mercado/2026/06/byd-acelera-investimento-em-producao-de-baterias-no-brasil.shtml",
    "Actor: BYD (PRC) — prc. NEW row: Folha/Reuters CapEx range R$50–60m; enter R$50m soft floor (UNVERIFIED press citing Baldy). Distinct from byd_brazil_bess_factory_500m_2026 and archived Camaçari auto complex. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle244", investment_type="equipment_supply", evidence="press", currency="BRL",
    value_usd=str(round(50000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Magalhães, Luciana. “BYD acelera investimento em produção de baterias no Brasil.” Folha de S.Paulo, June 16, 2026. https://www1.folha.uol.com.br/mercado/2026/06/byd-acelera-investimento-em-producao-de-baterias-no-brasil.shtml.',
    annotation="BYD Manaus bus-battery NEW R$50m floor ~USD 9.63m via Fed H.10 (press). Supports byd_manaus_bus_battery_50m_brl_2026.",
    evid_note="Opened Folha Portuguese (Reuters); R$50–60m bus-battery line expansion / Manaus context / distinct from R$500m BESS confirmed. CapEx enter R$50m soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW EDP ES distribution CapEx ~R$5bn 2025–2030
row_doc(
    "edp_es_dist_5bn_brl_2025_2030",
    "energy", "power_plants_grid", "allied",
    "EDP Espírito Santo — distribution concession CapEx ~R$5bn (2025–2030)",
    "Brazil",
    "16 Jul 2025 EDP company: signed 30-year renewal of Espírito Santo distribution concession (70 of 78 municipalities; to 2055); will invest about R$ 5 billion in the state through 2030 (+40% vs 2019–2024). CapEx: enter R$5bn face. Distinct from edp_sp_dist_5bn_brl_2025_2030 (São Paulo twin).",
    "5000000000", "2025-07-16", "2025", "-20.32", "-40.34",
    "EDP Espírito Santo concession (Vitória / state pin).",
    "edp_es_dist_5bn_renewal_20250716",
    "Com o compromisso da qualidade de serviço e expansão da infraestrutura para os 1,7 milhão de consumidores, a EDP vai investir cerca de R$ 5 bilhões no estado até 2030. Um crescimento de 40% na comparação com os investimentos realizados entre 2019 e 2024.",
    "https://www.edp.com.br/noticias/artigo/edp-assina-renovacao-da-concessao-de-distribuicao-e-amplia-em-40-os-investimentos-no-espirito-santo/",
    "Actor: EDP (Portugal) — allied. NEW row: company Portuguese CapEx ~R$5bn ES distribution through 2030. Shuffle power_plants_grid.",
    "hunt_cycle244", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(5000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='EDP Brasil. “EDP assina renovação da concessão de Distribuição e amplia em 40% os investimentos no Espírito Santo.” July 16, 2025. https://www.edp.com.br/noticias/artigo/edp-assina-renovacao-da-concessao-de-distribuicao-e-amplia-em-40-os-investimentos-no-espirito-santo/.',
    annotation="EDP ES dist NEW ~R$5bn ~USD 962.99m via Fed H.10. Supports edp_es_dist_5bn_brl_2025_2030.",
    evid_note="Opened EDP Portuguese; ~R$5bn to 2030 / +40% / 70 municipalities / to 2055 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Cosern Estivas >R$100m nested
row_doc(
    "neoenergia_cosern_estivas_100m_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Cosern — Subestação Estivas + LD João Câmara II–Zabelê (Litoral Norte RN)",
    "Brazil",
    "8 May 2026 Neoenergia company (within R$50bn 2026–2030 cycle): Cosern Litoral Norte — entry into operation of Subestação Estivas and distribution line João Câmara II–Zabelê with investment of more than R$ 100 million, serving ~180 thousand clients. CapEx: enter R$100m soft floor. Distinct from neoenergia_dist_50bn envelope / Oeste Baiano / Ilhabela / Coelba litoral.",
    "100000000", "2026-05-08", "2026", "-5.54", "-35.82",
    "Neoenergia Cosern Litoral Norte RN (João Câmara / Estivas corridor pin).",
    "neoenergia_cosern_estivas_100m_20260508",
    "No Litoral Norte, a entrada em operação da Subestação Estivas e da linha de distribuição João Câmara II–Zabelê representa um reforço decisivo para o sistema elétrico regional. Com investimento de mais de R$ 100 milhões, a infraestrutura passa a atender cerca de 180 mil clientes, garantindo energia robusta para um amplo corredor turístico.",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW nested CapEx >R$100m Cosern Estivas. Shuffle power_plants_grid.",
    "hunt_cycle244", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia Cosern Estivas NEW >R$100m floor ~USD 19.26m via Fed H.10. Supports neoenergia_cosern_estivas_100m_brl_2026.",
    evid_note="Opened Neoenergia Portuguese; >R$100m Estivas + João Câmara II–Zabelê / ~180k clients confirmed. CapEx enter R$100m soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle244 added {len(added)}: {added}")
    print(f"cycle244 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
