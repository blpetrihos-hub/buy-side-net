#!/usr/bin/env python3
"""Cycle 144 hunt: shuffle_seed=20261144; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: copper, niobium, port_ownership, bridges_roads, solar, water,
other_renewables, power_plants_grid, port_cranes, lithium, wind, rail,
building_materials, balsa, graphite, engineering_epc, fission_smr, nickel.

PRC ahead by 8 after 143 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr/nickel (dry → niobium).
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
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
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


# 1. copper / prc — MMG Las Bambas 2025 CapEx USD 494.2m
row_doc(
    "mmg_las_bambas_2025_capex_494m",
    "resources",
    "copper",
    "prc",
    "MMG — Las Bambas 2025 capital expenditure (Peru)",
    "Peru",
    "3 Mar 2026 MMG 2025 Annual Results: Las Bambas CapEx US$494.2 million in 2025 for tailings dam facility expansion, Ferrobamba pit infrastructure, and Chalcobamba execution (part of group CapEx US$1,081.4m). Distinct from mmg_las_bambas_2026_capex (2026 guidance US$800–850m) and mmg_chalcobamba_877m_senace_2025 (Senace MEIA investment plan).",
    "494200000",
    "2025-12-31",
    "2025",
    "-14.080",
    "-72.300",
    "Las Bambas mine, Apurímac Region, Peru (company asset geography).",
    "mmg_2025_annual_results_20260303",
    "2025 Capital Expenditure: Total capital expenditure for 2025 was US$1,081.4 million. Major expenditure included Las Bambas US$494.2 million for the tailings dam facility expansion, Ferrobamba pit infrastructure, and Chalcobamba execution…",
    "https://www.mmg.com/content/uploads/2026/03/e_2026-03-03_2025-Annual-Results.pdf",
    "Actor: MMG Ltd (China Minmetals-controlled) — prc. Company HKEX annual results primary. Actual 2025 spend vs 2026 guidance row.",
    "hunt_res_copper",
    investment_type="capex",
    chicago='MMG Limited. “Announcement on 2025 Annual Results.” March 3, 2026. https://www.mmg.com/content/uploads/2026/03/e_2026-03-03_2025-Annual-Results.pdf.',
    annotation="MMG 2025 annual results: Las Bambas CapEx USD 494.2m. Supports mmg_las_bambas_2025_capex_494m.",
    evid_note="Opened MMG 2025 Annual Results PDF (Las Bambas CapEx USD 494.2m).",
)

# 2. solar / prc — POWERCHINA Colombia Guayepo III + Escobales + Paranova III all COD (260 MW)
row_doc(
    "powerchina_colombia_3pv_260mw_cod_2025",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Guayepo III, Escobales, Paranova III Colombia PV triple full-capacity COD",
    "Colombia",
    "11 Dec 2025 POWERCHINA International: with Paranova III grid connection, POWERCHINA’s three 2025 Colombia large ground-mount PV EPCs — Guayepo III, Escobales, and Paranova III — all reached full-capacity commercial generation on schedule; combined 260 MW; ~520 GWh/year; ~350k households; ~420kt CO₂ avoided/year. CapEx blank on portfolio wrap (individual EPC CapEx not on this page). Distinct portfolio COD-completion milestone vs prior per-plant rows.",
    "",
    "",
    "2025",
    "10.800",
    "-74.900",
    "Colombia Atlantic/Cesar PV corridor (Guayepo III / Escobales / Paranova III cluster pin — company portfolio geography).",
    "powerchina_intl_colombia_3pv_20251211",
    "近日，中国电建承建的哥伦比亚帕拉诺瓦3期光伏电站成功并网。至此，公司2025年在哥承建的瓜业博3期、埃斯科巴勒斯及帕拉诺瓦3期三个大型地面光伏项目已全部如期实现全容量并网发电…3座光伏电站总装机容量达260兆瓦，年均发电量约5.2亿千瓦时…",
    "https://www.powerchina-intl.com/show/9/4553.html",
    "Actor: POWERCHINA International (PRC SOE) — prc. Company Chinese primary. CapEx blank. Portfolio wrap confirming three previously logged plants all COD.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA International. “中国电建在哥伦比亚承建的3个大型光伏项目全部并网发电.” December 11, 2025. https://www.powerchina-intl.com/show/9/4553.html.',
    annotation="POWERCHINA Intl: Guayepo III + Escobales + Paranova III combined 260 MW full COD. Supports powerchina_colombia_3pv_260mw_cod_2025.",
    evid_note="Opened POWERCHINA International release 11 Dec 2025 (Colombia 3 PV / 260 MW COD wrap).",
)

# 3. wind / us — AES Andes Campo Lindo COD 66 MW
row_doc(
    "aes_andes_campo_lindo_cod_2023",
    "energy",
    "wind",
    "us",
    "AES Andes — Campo Lindo Wind Farm COD (Los Ángeles, Biobío)",
    "Chile",
    "May 2023 AES Andes English: commercial operation (COD) of 66 MW Campo Lindo wind farm in Los Ángeles, Biobío Region — joins Mesamávida and Los Olmos in southern Chile renewable hub. CapEx blank on COD release.",
    "",
    "",
    "2023",
    "-37.470",
    "-72.350",
    "Los Ángeles, Biobío Region, Chile (company geography; same Biobío hub pin family as San Matías).",
    "aes_andes_campo_lindo_cod_202305",
    "In April the Company achieved the commercial operation (COD) of the 66 MW Campo Lindo wind farm, located in Los Angeles, Biobío Region, which joins AES Andes’ Mesamávida and Los Olmos wind farms in the South of Chile.",
    "https://www.aesandes.com/en/press-release/aes-andes-advances-its-transformation-process-new-wind-farm-operation-and-entry-new",
    "Actor: AES Andes / AES Corporation — us. Company English primary. CapEx blank. Distinct from aes_andes_san_matias_cod_2024 (78 MW).",
    "hunt_energy_wind",
    investment_type="greenfield_generation",
    chicago='AES Andes. “AES Andes advances in its transformation process with a new wind farm in operation and entry of new renewable projects.” May 4, 2023. https://www.aesandes.com/en/press-release/aes-andes-advances-its-transformation-process-new-wind-farm-operation-and-entry-new.',
    annotation="AES Andes primary: Campo Lindo 66 MW wind COD Apr/May 2023. Supports aes_andes_campo_lindo_cod_2023.",
    evid_note="Opened AES Andes English release (Campo Lindo 66 MW COD).",
)

# 4. rail / us — Progress Rail–VLI Northern Corridor MSA up to R$500m
# ECB 2025-10-10: BRL/EUR 6.2082; USD/EUR 1.1568 → USD/BRL = 1.1568/6.2082 ≈ 0.1863342
row_doc(
    "progress_rail_vli_msa_norte_500m_brl_2025",
    "infrastructure",
    "rail",
    "us",
    "Progress Rail (Caterpillar) — VLI Northern Corridor 10-year locomotive MSA",
    "Brazil",
    "10 Feb 2026 VLI: with Progress Rail locomotive delivery celebration, discloses Oct 2025 Maintenance Services Agreement (MSA) for VLI Northern Corridor (Tocantins–São Luís / Matopiba) — Progress Rail’s first long-term MSA in South America; 10 years; value up to R$500 million. CapEx = contract ceiling from VLI primary. Distinct from progress_rail_vli_sd70_2026 (locomotive delivery; CapEx blank on Progress Rail page).",
    "500000000",
    "2025-10-10",
    "2025",
    "-2.530",
    "-44.300",
    "VLI Northern Corridor / São Luís port system, Maranhão, Brazil (corridor southern pin at São Luís).",
    "vli_progress_rail_msa_celebration_20260210",
    "Em outubro, as companhias firmaram um contrato de prestação de serviços de manutenção (MSA), com foco nas operações ferroviárias da VLI no Corredor Norte… Este foi o primeiro acordo do gênero da Progress Rail na América do Sul, com duração de 10 anos e valor de até R$ 500 milhões.",
    "https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/",
    "Actor: Progress Rail (Caterpillar Inc., U.S.) — us. VLI company primary for MSA CapEx ceiling. ECB FX 2025-10-10 BRL/EUR 6.2082, USD/EUR 1.1568 → USD/BRL≈0.186334 → USD 93,167,102.",
    "hunt_infra_rail",
    investment_type="services_contract",
    currency="BRL",
    value_usd="93167102",
    fx_usd="0.1863342035",
    chicago='VLI Logística. “VLI e Progress Rail celebram recebimento de locomotivas para operação na Ferrovia Centro-Atlântica.” February 10, 2026. https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-locomotivas-para-operacao-na-ferrovia-centro-atlantica/.',
    annotation="VLI primary: Progress Rail Northern Corridor MSA up to R$500m. Supports progress_rail_vli_msa_norte_500m_brl_2025.",
    evid_note="Opened VLI release 10 Feb 2026 (MSA até R$500m; ECB FX 2025-10-10).",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 144 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
