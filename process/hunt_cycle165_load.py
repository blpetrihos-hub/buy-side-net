#!/usr/bin/env python3
"""Cycle 165 hunt: shuffle_seed=20261165; equal budget; U.S./PRC split; thin after.

Canonical shuffle: water, building_materials, port_cranes, power_plants_grid, niobium,
lithium, fission_smr, nickel, port_ownership, bridges_roads, graphite, rail,
other_renewables, solar, wind, copper, engineering_epc, balsa.

Thin: balsa/fission/niobium once (dry); nickel/graphite already used this session.
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


# 1. water / prc — POWERCHINA Wiesner Bogotá waterworks upgrade EPC
row_doc(
    "powerchina_wiesner_bogota_water_2023",
    "resources",
    "water",
    "prc",
    "POWERCHINA — Wiesner waterworks upgrade EPC (Bogotá)",
    "Colombia",
    "2 Feb 2023 POWERCHINA English: signed contract 26 Jan 2023 to upgrade/renovate Bogotá waterworks plant (second Colombia water project after Tibitó); on completion treatment capacity rises from 14 m³/s to 21 m³/s, serving ~10 million people (~70% of capital domestic water supply). CapEx blank on opened page. Distinct from powerchina Tibitó upgrade and El Curval rows.",
    "",
    "",
    "2023",
    "4.710",
    "-74.210",
    "Wiesner / Bogotá water treatment complex, Colombia (company geography; approximate).",
    "powerchina_colombia_2projects_20230202",
    "One was signed the contract to upgrade and renovate a waterworks plant on Jan 26; the other was the Tepuy Photovoltaic (PV) Power Station on Jan 31. The waterworks plant is located in Bogota, capital of Colombia. It is the second water project undertaken by POWERCHINA in the Colombian market. On completion, the treatment capacity of the water plant will increase from 14 cubic meters per second to 21 cu m per second, providing high-quality domestic water for about 10 million people in Bogota",
    "https://en.powerchina.cn/2023-02/02/c_828236.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary. CapEx blank. Bogotá Wiesner capacity 14→21 m³/s.",
    "hunt_res_water",
    investment_type="epc",
    bib_type="company",
    chicago='Power Construction Corporation of China. “POWERCHINA Signs 2 Projects in Colombia.” February 2, 2023. https://en.powerchina.cn/2023-02/02/c_828236.htm.',
    annotation="POWERCHINA primary: Bogotá Wiesner waterworks upgrade EPC (14→21 m³/s). Supports powerchina_wiesner_bogota_water_2023.",
    evid_note="Opened POWERCHINA English 2 Feb 2023 (Wiesner waterworks + Tepuy PV signing).",
)

# 2. water / prc — POWERCHINA Tibitó Bogotá upgrade (first Colombia water; nano system COD 2026)
row_doc(
    "powerchina_tibitoc_bogota_water_upgrade",
    "resources",
    "water",
    "prc",
    "POWERCHINA — Tibitó water treatment plant upgrade (Bogotá metropolitan)",
    "Colombia",
    "POWERCHINA 11th Bureau feature: consortium led by POWERCHINA won Tibitó upgrade Dec 2019 (first Colombia market win); construction start 17 Feb 2021; design capacity ~907,000 m³/day normal / ~1,037,000 m³/day peak; nano pre-oxidation system entered normal operation Mar 2026 after multi-year optimization. CapEx blank (relative 15–20% of new-build cost noted — not stored as absolute CapEx). Distinct from Wiesner upgrade.",
    "",
    "",
    "2026",
    "4.980",
    "-73.960",
    "Tibitó WTP ~40 km from Bogotá, Cundinamarca, Colombia.",
    "powerchina_tibitoc_feature_2026",
    "2019年12月，由中国电建牵头的联营体成功中标缇比托克水厂升级改造工程，这也是中国电建在哥伦比亚市场中标的首个项目。… 直到2021年2月17日才正式开工。… 2026年3月，相关技术和商务事项最终落定，纳米预氧化系统投入正常运行。… 按设计能力计算，缇比托克水厂正常日处理能力90.7万立方米，峰值可达103.7万立方米。",
    "http://11j.powerchina.cn/col/col11645/art/2026/art_dc2241e1e3704a3d973d19e1f5bc01ca.html",
    "Actor: POWERCHINA-led consortium — prc. Company Chinese primary. CapEx blank. First Colombia water win; nano COD Mar 2026.",
    "hunt_res_water",
    investment_type="epc",
    bib_type="company",
    chicago='Power Construction Corporation of China (11th Bureau). “【特稿】“功勋水厂”焕新记——哥伦比亚缇比托克水厂升级改造工程施工管理侧记.” 2026. http://11j.powerchina.cn/col/col11645/art/2026/art_dc2241e1e3704a3d973d19e1f5bc01ca.html.',
    annotation="POWERCHINA primary: Tibitó Bogotá WTP upgrade; nano pre-ox COD Mar 2026. Supports powerchina_tibitoc_bogota_water_upgrade.",
    evid_note="Opened POWERCHINA 11th Bureau Tibitó feature (award 2019 / COD nano 2026).",
)

# 3. building_materials / allied — Holcim acquires Cemex Guatemala ops
row_doc(
    "holcim_cemex_guatemala_ops_2024",
    "infrastructure",
    "building_materials",
    "allied",
    "Holcim — acquisition of Cemex Guatemala cement/ready-mix operations (USD 212m)",
    "Guatemala",
    "10 Sep 2024 Cemex 4Q24 report: sold Guatemala ops to Holcim Group for total consideration USD 212 million; divested assets mainly one grinding mill (~0.6 Mtpa), three ready-mix plants, five distribution centers. CapEx/investment = USD 212m consideration face. Fills Guatemala×building_materials empty cell. Distinct from holcim_cemex_colombia_2026.",
    "212000000",
    "2024-09-10",
    "2024",
    "13.930",
    "-90.780",
    "Cement grinding plant / Guatemala Cemex footprint (Puerto Quetzal area; approximate).",
    "cemex_4q24_guatemala_sale",
    "On September 10, 2024, Cemex sold its operations in Guatemala to Holcim Group, for a total consideration of US$212 million. The divested assets mainly consist of one grinding mill with an installed capacity of around 0.6 million metric tons per year, three ready-mix plants and five distribution centers.",
    "https://www.cemex.com/documents/d/cemex/4q24_report_english",
    "Actor: Holcim Group buyer (Zug HQ) — allied; seller Cemex. Cemex 4Q24 English primary. USD 212m. First Guatemala building_materials row.",
    "hunt_infra_building_materials",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Cemex, S.A.B. de C.V. “Fourth Quarter Results 2024.” https://www.cemex.com/documents/d/cemex/4q24_report_english.',
    annotation="Cemex 4Q24: Guatemala ops sold to Holcim for USD 212m. Supports holcim_cemex_guatemala_ops_2024.",
    evid_note="Opened Cemex 4Q24 English report (Guatemala sale USD 212m).",
)

# 4. building_materials / other — Cemex Carib Cement Rockfort USD 42m
row_doc(
    "cemex_carib_rockfort_42m_jamaica",
    "infrastructure",
    "building_materials",
    "other",
    "Cemex / Caribbean Cement — Rockfort Debottleneck Project (USD 42m)",
    "Jamaica",
    "26 Jun (Carib Cement company page): Caribbean Cement Company Limited (Cemex subsidiary) commissioned USD 42 million Debottleneck Project at Rockfort facility, East Kingston; scope includes new main baghouse, solid fuel dosing system with storage silo, CO₂ fire suppression/inerting, upgraded process ducts, compressed air system, kiln chimney; aims to raise cement production up to ~30%. CapEx = USD 42m face. Actor HQ Monterrey (Mexico) — other (not US/PRC/allied Western).",
    "42000000",
    "2025-06-26",
    "2025",
    "17.970",
    "-76.760",
    "Rockfort cement works, East Kingston, Jamaica.",
    "caribcement_rockfort_42m_2025",
    "Caribbean Cement Company Limited (CCCL), a subsidiary of global building materials leader, Cemex, commissioned its US$42 million Debottleneck Project at its Rockfort facility in East Kingston earlier today. … The scope of work for the project included the installation of a new main baghouse, a solid fuel dosing system with storage silo, CO₂ fire suppression and inerting systems, upgraded process ducts, a new compressed air system, and a kiln chimney.",
    "https://caribcement.com/cemex-carib-cements-us42-million-expansion-project-is-ready-to-boost-cement-production-in-jamaica/",
    "Actor: Cemex S.A.B. de C.V. via CCCL (Mexico HQ) — other. Company English primary. USD 42m Rockfort debottleneck.",
    "hunt_infra_building_materials",
    investment_type="epc",
    bib_type="company",
    chicago='Caribbean Cement Company Limited. “Cemex Carib Cement’s US$42 Million Expansion Project Is Ready to Boost Cement Production in Jamaica.” June 26, 2025. https://caribcement.com/cemex-carib-cements-us42-million-expansion-project-is-ready-to-boost-cement-production-in-jamaica/.',
    annotation="Carib Cement/Cemex primary: Rockfort Debottleneck USD 42m commissioned. Supports cemex_carib_rockfort_42m_jamaica.",
    evid_note="Opened Carib Cement Rockfort USD 42m commissioning release.",
)

# 5. port_cranes / allied — Konecranes 3 reach stackers Chiquita Puerto Barrios
row_doc(
    "konecranes_chiquita_puerto_barrios_3rs_2024",
    "infrastructure",
    "port_cranes",
    "allied",
    "Konecranes — 3 reach stackers (Chiquita Terminal Ferroviaria, Puerto Barrios)",
    "Guatemala",
    "6 Feb 2024 Konecranes Lift Trucks: Chiquita Guatemala received first two of three Konecranes reach stackers in Q3 2023 for Terminal Ferroviaria at Puerto Barrios; third (Liftace 4532 TCE5) scheduled 2024 delivery; models SMV 4632 TC5, SMV 4632 TC6H, Liftace 4532 TCE5 with TRUCONNECT monitoring. CapEx blank. Fills Guatemala×port_cranes empty cell.",
    "",
    "",
    "2024",
    "15.730",
    "-88.600",
    "Puerto Barrios / Terminal Ferroviaria, Izabal, Guatemala.",
    "konecranes_chiquita_barrios_20240206",
    "In Q3 2023, Chiquita Guatemala S.A. (Chiquita) received the first two of three Konecranes reach stackers for their Terminal Ferroviaria in Puerto Barrios. With one more scheduled for delivery in 2024, all three will help raise Chiquita’s banana business to the next level. … The first two reach stackers, a Konecranes SMV 4632 TC5 and a Konecranes SMV 4632 TC6H are already on-site. The third one, currently on its way, is a Konecranes Liftace 4532 TCE5.",
    "https://www.kclifttrucks.com/press-releases/konecranes-to-deliver-3-reach-stackers-to-boost-chiquita-exports-in-guatemala",
    "Actor: Konecranes (Finland HQ) — allied. Company English primary. CapEx blank. First Guatemala port_cranes row.",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Konecranes Lift Trucks. “Konecranes to Deliver 3 Reach Stackers to Boost Chiquita Exports in Guatemala.” February 6, 2024. https://www.kclifttrucks.com/press-releases/konecranes-to-deliver-3-reach-stackers-to-boost-chiquita-exports-in-guatemala.',
    annotation="Konecranes primary: 3 reach stackers for Chiquita Puerto Barrios. Supports konecranes_chiquita_puerto_barrios_3rs_2024.",
    evid_note="Opened Konecranes 6 Feb 2024 Chiquita Puerto Barrios reach-stacker release.",
)

# 6. lithium / allied — American Lithium Falchani PEA Phase 1 CapEx USD 681m
row_doc(
    "american_lithium_falchani_pea_681m_peru",
    "resources",
    "lithium",
    "allied",
    "American Lithium — Falchani lithium project updated PEA Phase 1 CapEx (Puno)",
    "Peru",
    "10 Jan 2024 American Lithium: updated PEA for Falchani (Puno) by DRA Global — initial CapEx estimated USD 681 million; LOM CapEx USD 2,565 million; sustaining CapEx USD 236 million; after-tax NPV8% USD 5.11 billion at USD 22,500/t LCE. CapEx/investment = USD 681m Phase 1 PEA face (study estimate, not FID). Fills Peru×lithium empty cell.",
    "681000000",
    "2024-01-10",
    "2024",
    "-14.080",
    "-70.430",
    "Falchani project, Macusani Plateau, Puno, Peru (company geography; approximate).",
    "american_lithium_falchani_pea_20240110",
    "Initial Capital Costs (“Capex”) estimated at $681 million … Total Capex LOM estimated at $2,565 million; Sustaining Capital estimated at $236 million … After-tax NPV 8% $5.11 billion at $22,500/t LCE",
    "https://americanlithiumcorp.com/updated-pea-for-falchani-highlights-robust-economics-after-tax-npv8-triples-to-us5-11-billion-irr-32-0-and-low-opex-5093-t-lce/",
    "Actor: American Lithium Corp. (Vancouver HQ) — allied. Company English primary. USD 681m Phase 1 PEA CapEx. First Peru lithium row.",
    "hunt_res_lithium",
    investment_type="other",
    bib_type="company",
    chicago='American Lithium Corp. “Updated PEA for Falchani Highlights Robust Economics After-Tax NPV8% Triples to US$5.11 Billion, IRR 32.0% and Low Opex $5,093/t LCE.” January 10, 2024. https://americanlithiumcorp.com/updated-pea-for-falchani-highlights-robust-economics-after-tax-npv8-triples-to-us5-11-billion-irr-32-0-and-low-opex-5093-t-lce/.',
    annotation="American Lithium primary: Falchani PEA Phase 1 CapEx USD 681m. Supports american_lithium_falchani_pea_681m_peru.",
    evid_note="Opened American Lithium 10 Jan 2024 Falchani updated PEA release.",
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
    print(f"Cycle 165 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
