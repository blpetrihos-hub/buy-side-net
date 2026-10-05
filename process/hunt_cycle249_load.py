#!/usr/bin/env python3
"""Cycle 249 hunt: shuffle_seed=20261249; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261249).shuffle):
nickel, lithium, building_materials, rail, port_ownership, solar, fission_smr,
port_cranes, bridges_roads, power_plants_grid, engineering_epc, niobium, water,
graphite, wind, copper, balsa, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AWS Mexico Region >USD 5bn (company English).
PRC equal-budget: NEW SGBH cumulative CapEx >R$30bn since 2010 (RS 2025 PDF).
Other: NEW Cemig R$44bn 2026–2030 plan; NEW Energisa four-state ~R$18bn.
Skipped: CBMM/Progress Rail/holdovers dense; thin balsa/nickel/fission dry.
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


# 1. engineering_epc / us — NEW AWS Mexico Region >USD 5bn
row_doc(
    "aws_mexico_5bn_2025",
    "infrastructure", "engineering_epc", "us",
    "Amazon Web Services — AWS Mexico (Central) Region data-center build",
    "Mexico",
    "14 Jan 2025 Amazon/AWS: launches AWS Mexico (Central) Region with three Availability Zones; as part of long-term commitment AWS plans to invest more than USD 5 billion in Mexico over 15 years to support construction, connection, operation, and maintenance of its data centers. CapEx: enter USD 5bn floor. Distinct from aws_chile_region_4bn_2025 and Equinix/Ascenty Mexico rows.",
    "5000000000", "2025-01-14", "2025", "", "",
    "AWS Mexico (Central) Region multi-AZ campus package (Querétaro footprint; multi-site — lat/lon blank).",
    "amazon_aws_mexico_region_20250114",
    "As part of its long-term commitment, AWS is planning to invest more than $5 billion in Mexico over 15 years.",
    "https://press.aboutamazon.com/2025/1/aws-launches-infrastructure-region-in-mexico",
    "Actor: Amazon / AWS (U.S.) — us. NEW row: company English >USD 5bn Mexico Region CapEx floor. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle249", investment_type="greenfield_plant", evidence="documented", currency="USD",
    chicago='Amazon Web Services. “AWS Launches Infrastructure Region in Mexico.” January 14, 2025. https://press.aboutamazon.com/2025/1/aws-launches-infrastructure-region-in-mexico.',
    annotation="AWS Mexico NEW >USD 5bn floor. Supports aws_mexico_5bn_2025.",
    evid_note="Opened Amazon/AWS English press; >USD 5bn / 15 years / Mexico Central Region / three AZs confirmed. CapEx enter USD 5bn floor.",
)

# 2. power_plants_grid / prc — NEW SGBH cumulative CapEx >R$30bn since 2010
row_doc(
    "sgbh_cumulative_30bn_brl_2010_2025",
    "energy", "power_plants_grid", "prc",
    "State Grid Brazil Holding — cumulative CapEx >R$30bn (2010–2025)",
    "Brazil",
    "SGBH Sustentabilidade 2025 PDF: with investments exceeding R$ 30 billion since 2010, consolidated ~16,000 km of transmission lines across 14 states, including XRTE, BMTE, and GATE under construction. CapEx: enter R$30bn soft floor of stated “superiores a R$ 30 bilhões.” Distinct from project-level GATE R$18bn / Mantiqueira R$7bn rows (nested within cumulative envelope — not additive).",
    "30000000000", "2025-12-31", "2025", "", "",
    "SGBH Brazil multi-state transmission footprint (nationwide; lat/lon blank).",
    "sgbh_rs2025_cumulative_30bn",
    "Com investimentos superiores a R$ 30 bilhões desde 2010, consolidamos uma infraestrutura de 16 mil quilômetros de linhas ao longo de 14 estados, com projetos emblemáticos como as transmissoras de energia em corrente contínua: Xingu Rio (XRTE), Belo Monte (BMTE) e a mais recente, em fase de implantação, Graça Aranha Silvânia (GATE).",
    "https://stategrid.com.br/wp-content/uploads/2026/04/SGBH_RS25_VFb.pdf",
    "Actor: State Grid Brazil Holding / SGCC (PRC) — prc. NEW row: company Portuguese RS 2025 cumulative CapEx >R$30bn floor. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle249", investment_type="capex_program", evidence="documented", currency="BRL",
    value_usd=str(round(30000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='State Grid Brazil Holding. “Sustentabilidade 2025.” 2026. https://stategrid.com.br/wp-content/uploads/2026/04/SGBH_RS25_VFb.pdf.',
    annotation="SGBH cumulative NEW >R$30bn floor ~USD 5776.85m via Fed H.10. Supports sgbh_cumulative_30bn_brl_2010_2025.",
    evid_note="Opened SGBH RS 2025 PDF; >R$30bn since 2010 / 16k km / 14 states / XRTE+BMTE+GATE confirmed. CapEx enter R$30bn soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / other — NEW Cemig R$44bn 2026–2030
row_doc(
    "cemig_capex_plan_44bn_brl_2026_2030",
    "energy", "power_plants_grid", "other",
    "Cemig — 2026–2030 investment plan (~R$44bn)",
    "Brazil",
    "12 Dec 2025 Cemig Fato Relevante: Board on 11 Dec 2025 approved Strategic Plan / Multi-Year Plan for Cycle 2026/2030 with estimated investment of R$ 44 billion; 2026 alone ~R$6.725bn (distribution R$5.269bn; transmission R$632m; generation R$197m; DG R$375m; gas R$227m; other R$25m). CapEx: enter R$44bn face. Distinct from Copel 2026 plan and Neoenergia/Energisa concession CapEx rows.",
    "44000000000", "2025-12-12", "2025", "-19.92", "-43.94",
    "Cemig Minas Gerais footprint (Belo Horizonte HQ pin).",
    "cemig_fr_44bn_20251212",
    "o Conselho de Administração, em 11/12/2025, aprovou a atualização do seu Planejamento Estratégico e Plano Plurianual para o Ciclo 2026/2030, com o plano de investimentos no montante estimado de R$ 44 bilhões.",
    "https://ri.cemig.com.br/docs/Fato-Relevante-Cemig-2025-12-12-9T8zwtDm.pdf",
    "Actor: Cemig (Minas Gerais state-controlled utility) — other. NEW row: company Portuguese Fato Relevante R$44bn 2026–2030. Shuffle power_plants_grid.",
    "hunt_cycle249", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(44000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais – Cemig. “Fato Relevante: CEMIG divulga plano de investimentos de R$ 44 bilhões para 2026/2030.” December 12, 2025. https://ri.cemig.com.br/docs/Fato-Relevante-Cemig-2025-12-12-9T8zwtDm.pdf.',
    annotation="Cemig NEW R$44bn ~USD 8474.41m via Fed H.10. Supports cemig_capex_plan_44bn_brl_2026_2030.",
    evid_note="Opened Cemig Fato Relevante PDF; R$44bn cycle / R$6.725bn 2026 breakdown confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Energisa four-state ~R$18bn
row_doc(
    "energisa_4states_18bn_brl_2026_2030",
    "energy", "power_plants_grid", "other",
    "Energisa — MT/MS/PB/SE distribution CapEx ~R$18bn (2026–2030)",
    "Brazil",
    "8 May 2026 Energisa company: signed 30-year concession renewals with MME for Mato Grosso, Mato Grosso do Sul, Paraíba and Sergipe; announced investment forecast of about R$ 18 billion over the next five years across the four states (5.7 million customers). Nested breakouts: MT R$9.3bn; MS R$4.4bn; PB R$2.8bn; SE R$1.69bn. CapEx: enter R$18bn soft floor. Distinct from Neoenergia/Cemig/Copel group plans.",
    "18000000000", "2026-05-08", "2026", "-15.60", "-56.10",
    "Energisa four-state distribution concessions (Cuiabá / MT pin).",
    "energisa_4states_18bn_20260508",
    "A Companhia também anunciou previsão de investimentos de cerca de R$ 18 bilhões para os próximos cinco anos nos quatro estados, que, se somados, atendem 5,7 milhões de clientes.",
    "https://www.energisa.com.br/noticias/energia-que-transforma/grupo-energisa-renova-concessoes-em-mt-ms-pb-e-se",
    "Actor: Grupo Energisa (Brazilian private utility) — other. NEW row: company Portuguese ~R$18bn four-state 2026–2030. Shuffle power_plants_grid.",
    "hunt_cycle249", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(18000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Grupo Energisa. “Grupo Energisa renova concessões em MT, MS, PB e SE.” May 8, 2026. https://www.energisa.com.br/noticias/energia-que-transforma/grupo-energisa-renova-concessoes-em-mt-ms-pb-e-se.',
    annotation="Energisa NEW ~R$18bn floor ~USD 3466.81m via Fed H.10. Supports energisa_4states_18bn_brl_2026_2030.",
    evid_note="Opened Energisa Portuguese; ~R$18bn / four states / MT 9.3 / MS 4.4 / PB 2.8 / SE 1.69 confirmed. CapEx enter R$18bn soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle249 added {len(added)}: {added}")
    print(f"cycle249 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
