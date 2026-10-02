#!/usr/bin/env python3
"""Cycle 131 hunt: shuffle_seed=20261131; equal budget; U.S./PRC split; thin after.

Order: engineering_epc, building_materials, port_cranes, balsa, port_ownership,
nickel, power_plants_grid, graphite, lithium, water, solar, bridges_roads, rail,
other_renewables, copper, niobium, wind, fission_smr.

PRC push (undersampled post-territory audit). Thin top-up: balsa/graphite/nickel.
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
        fx_usd = "1" if value_usd else ""
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


# 1. port_ownership / prc — CMPort 70% Vast Infraestrutura (Port of Açu)
row_doc(
    "cmport_vast_acu_70pct_spa_2025",
    "infrastructure",
    "port_ownership",
    "prc",
    "China Merchants Port Holdings — 70% Vast Infraestrutura (Port of Açu crude terminal)",
    "Brazil",
    "28 Feb 2025 HKEX discloseable-transaction announcement: CMPort (via Cyber Chic) enters SPA to acquire 70% of Vast Infraestrutura S.A. from Prumo Logística / Açu Petróleo Investimentos; closing purchase price equal to USD 448 million in BRL (adjustable; cap USD 714 million) plus USD 56 million milestone payments and EBITDA earn-outs; Vast operates the onshore crude-oil transfer terminal at Port of Açu (Rio de Janeiro) — Brazil’s only privately operated non-Petrobras VLCC-capable oil terminal (~30% of Brazil crude exports; permitted capacity 1.2 mb/d). Closing subject to CADE/ANTAQ/SASAC and other conditions. Distinct from CMPort TCP Paranaguá 2017.",
    "448000000",
    "2025-02-28",
    "2025",
    "-21.85",
    "-40.98",
    "Port of Açu crude-oil terminal, São João da Barra, Rio de Janeiro (CMPort/Vast geography).",
    "cmport_vast_acu_hkex_20250228",
    "買方於交割時應付的購買價應為等於4.48億美元（相當於約34.94億港元）的巴西雷亞爾金額",
    "https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0228/2025022801382_c.pdf",
    "Actor: China Merchants Port Holdings (PRC SOE-linked HK-listed) — prc; sellers Prumo/API. Official HKEX Chinese primary opened; value stored as USD 448m closing purchase price (ex-milestones/earn-outs). CapEx blank beyond equity consideration.",
    "hunt_infra_port_ownership",
    investment_type="ownership_equity",
    bib_type="filing",
    chicago="China Merchants Port Holdings Company Limited. “Discloseable Transaction — Acquisition of Vast in Brazil.” Hong Kong Stock Exchange announcement (Chinese), 28 February 2025. https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0228/2025022801382_c.pdf.",
    annotation="HKEX primary SPA. Supports cmport_vast_acu_70pct_spa_2025.",
    evid_note="Opened HKEX Chinese SPA PDF; USD 448m purchase price; 70% Vast at Port of Açu.",
)

# 2. power_plants_grid / prc — POWERCHINA Chile Decree 4 G15/G04 substations
row_doc(
    "powerchina_chile_decree4_g15_g04_2025",
    "energy",
    "power_plants_grid",
    "prc",
    "POWERCHINA — Chile 2024 Decree No. 4 G15 (Parinas 500 kV) + G04 (San Juan/Algarrobal 220 kV) EPC",
    "Chile",
    "16 Jun 2025: POWERCHINA signs EPC contracts with Transelec, CGE, and Engie for two key substation expansions under Chile’s 2024 Decree No. 4 — G15 segment (500 kV Parinas substation OC01/OC02, Antofagasta Region) and G04 segment (220 kV San Juan and Algarrobal upgrades, central-northern grid). CapEx USD not disclosed on opened company English page. Distinct from cen_parinas_elecnor_powerchina_2024 CNE award package.",
    "",
    "",
    "2025",
    "-24.05",
    "-69.55",
    "Parinas 500 kV substation area, Antofagasta Region (POWERCHINA G15 geography; approximate).",
    "powerchina_chile_g15_g04_20250619",
    "On June 16, POWERCHINA signed EPC contracts with Chilean companies Transelec and CGE, as well as the French company Engie, for the expansion of two key substations under Chile's 2024 Decree No 4.",
    "https://en.powerchina.cn/2025-06/19/c_828966.htm",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; counterparties Transelec/CGE/Engie under CEN Decree 4. Company English primary. CapEx blank.",
    "hunt_energy_power_plants_grid",
    investment_type="epc",
    bib_type="company",
    chicago="POWERCHINA. “POWERCHINA secures transmission expansion projects in Chile.” Company English release, 19 June 2025. https://en.powerchina.cn/2025-06/19/c_828966.htm.",
    annotation="POWERCHINA English primary. Supports powerchina_chile_decree4_g15_g04_2025.",
    evid_note="Opened POWERCHINA English page; G15/G04 EPC signed 16 Jun 2025; CapEx blank.",
)

# 3. solar / prc — POWERCHINA/HDEC Dune Plus PV+storage EPC Chile
row_doc(
    "powerchina_dune_plus_epc_chile_2025",
    "energy",
    "solar",
    "prc",
    "POWERCHINA International / HDEC — Dune Plus PV + storage EPC (María Elena)",
    "Chile",
    "27 Jun 2025 (HDEC 28 Jun): PowerChina International Group Limited–Chile Branch, HDEC, and GM Developments SpA sign EPC general contract for Dune Plus Photovoltaic Storage Project at María Elena, Antofagasta (~1,300 km from Santiago, adjacent to delivered CEME1 PV). Scope: (1) new 1,334 MWh BESS within CEME1 site; (2) new 186 MWp PV + 702 MWh BESS south of CEME1; (3) CEME1 substation renovation support. Claimed largest single-unit storage EPC turnkey by HDEC/POWERCHINA in the Americas. CapEx USD not on opened HDEC page. Distinct from POWERCHINA CEME1 delivery and Sungrow Observatorio BESS rows.",
    "",
    "",
    "2025",
    "-22.35",
    "-69.67",
    "María Elena, Antofagasta Region — Dune Plus / CEME1 vicinity (HDEC release).",
    "hdec_dune_plus_epc_20250628",
    "On the afternoon of June 27, 2025, local time in Chile, PowerChina International Group Limited-Chile Branch, HDEC, and GM Developments SpA formally signed the EPC general contract for the Dune Plus Photovoltaic Storage Project in Chile.",
    "https://www.hdec.com/en/news/show-668.html",
    "Actor: POWERCHINA International / HDEC (PRC SOE group) — prc; client GM Developments SpA. HDEC English primary. CapEx blank. Later press naming Sungrow as EPC not used (secondary).",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago="PowerChina HuaDong Engineering Corporation Limited (HDEC). “The Dune Plus Photovoltaic Storage Project in Chile Signed.” Company English news, 28 June 2025. https://www.hdec.com/en/news/show-668.html.",
    annotation="HDEC English primary. Supports powerchina_dune_plus_epc_chile_2025.",
    evid_note="Opened HDEC English page; EPC signed 27 Jun 2025; 186 MWp + multi-GWh storage scope; CapEx blank.",
)

# 4. lithium / prc — Ganfeng USD 180m convertible + definitive PPG JV
row_doc(
    "ganfeng_lar_180m_convertible_ppg_2026",
    "resources",
    "lithium",
    "prc",
    "Ganfeng Lithium — USD 180m convertible note into Lithium Argentina + definitive PPG JV (67/33)",
    "Argentina",
    "24 Aug 2026 Lithium Argentina SEC Exhibit 99.1: definitive agreements finalize PPG JV consolidating Ganfeng Pozuelos–Pastos Grandes with Lithium Argentina Pastos Grandes and Sal de la Puna (Salta) under Millennial Lithium B.V. owned 67% Ganfeng / 33% Lithium Argentina; integrated development targeting 150,000 tpa LCE across three phases; combined historical investment cited USD 1.8bn. Concurrently Ganfeng invests USD 180 million via six-year 4.0% unsecured convertible note (conversion USD 12.50/share; close targeted Sep 2026). Distinct from ganfeng_ppg_jv_framework_2025 and ganfeng_pozuelos_dev_200m_2025.",
    "180000000",
    "2026-08-24",
    "2026",
    "-24.55",
    "-66.75",
    "Pozuelos–Pastos Grandes basin, Salta Province (PPG JV geography; approximate).",
    "lithium_argentina_ganfeng_ppg_180m_20260824",
    "Concurrently, Ganfeng has agreed to invest $180 million in Lithium Argentina through a six-year unsecured convertible note with a 4.0% coupon",
    "https://www.sec.gov/Archives/edgar/data/1440972/000106299326004563/exhibit99-1.htm",
    "Actor: Ganfeng Lithium Group (PRC) — prc; counterpart Lithium Argentina AG. Official SEC Exhibit 99.1. Value = USD 180m convertible (PPG JV CapEx blank pending project financing).",
    "hunt_res_lithium",
    investment_type="financing",
    bib_type="filing",
    chicago="Lithium Argentina AG and Ganfeng Lithium Group Co., Ltd. “Lithium Argentina Finalizes PPG Joint Venture; Announces $180M Strategic Investment from Ganfeng.” SEC Exhibit 99.1, 24 August 2026. https://www.sec.gov/Archives/edgar/data/1440972/000106299326004563/exhibit99-1.htm.",
    annotation="SEC Exhibit 99.1 primary. Supports ganfeng_lar_180m_convertible_ppg_2026.",
    evid_note="Opened SEC Exhibit 99.1; USD 180m Ganfeng convertible + 67% PPG JV terms.",
)

# 5. power_plants_grid / us — NFE Portocem 1.6 GW EPC NTP
row_doc(
    "nfe_portocem_1p6gw_epc_2024",
    "energy",
    "power_plants_grid",
    "us",
    "New Fortress Energy — 1.6 GW Portocem thermal EPC NTP (Barcarena)",
    "Brazil",
    "17 Apr 2024 NFE release: executes fixed-price date-certain EPC with Mitsubishi Power Americas / Andrade Gutierrez consortium for 1.6 GW power plant adjacent to Barcarena LNG terminal; full Notice to Proceed issued; COD projected no later than August 2026 under 15-year Capacity Reserve Contract with CCEE (acquired from Denham/CEIBA Mar 2024). March 2026 NFE BrazilCo separation release still lists 1.6 GW PortoCem in Barcarena cluster under development. CapEx USD not on opened EPC page. Distinct from excelerate_jamaica_nfe sale row.",
    "",
    "",
    "2024",
    "-1.52",
    "-48.75",
    "Barcarena LNG / Portocem site, Pará (NFE release).",
    "nfe_portocem_epc_20240417",
    "New Fortress Energy Inc. (NASDAQ: NFE) (“NFE” or the “Company”) today announced that it has finalized and executed an engineering, procurement and construction contract (the “EPC Contract”) with a consortium formed by Mitsubishi Power Americas and Andrade Gutierrez (the “MHI/AG Consortium”) for a 1.6 GW power plant to be built adjacent to the Barcarena LNG terminal.",
    "https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-signs-epc-contract-and-begins-construction",
    "Actor: New Fortress Energy Inc. (NYSE:NFE; U.S. HQ) — us; EPC consortium Mitsubishi Power Americas / Andrade Gutierrez. Company IR primary. CapEx blank.",
    "hunt_energy_power_plants_grid",
    investment_type="epc",
    bib_type="company",
    chicago="New Fortress Energy Inc. “New Fortress Energy Signs EPC Contract and Begins Construction of 1.6 GW Power Plant to Serve 15-Year Agreement in Brazil.” Company IR release, 17 April 2024. https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-signs-epc-contract-and-begins-construction.",
    annotation="NFE IR primary. Supports nfe_portocem_1p6gw_epc_2024.",
    evid_note="Opened NFE IR HTML; 1.6 GW Portocem EPC NTP; COD ≤ Aug 2026; CapEx blank.",
)

# 6. power_plants_grid / us — Seaboard Estrella del Mar IV floating CCGT
row_doc(
    "seaboard_estrella_del_mar_iv_2025",
    "energy",
    "power_plants_grid",
    "us",
    "Seaboard / Transcontinental Capital — Estrella del Mar IV 145 MW floating CCGT barge (Santo Domingo)",
    "Dominican Republic",
    "17 Oct 2025 ST Engineering Marine + Siemens Energy awarded second contract by Transcontinental Capital Corporation (Bermuda) Ltd., a Seaboard Corporation subsidiary, to deliver Estrella del Mar IV barge-mounted power plant to Santo Domingo; Siemens Energy supplies 145 MW combined-cycle package (2× SGT-800 + SST-600) with lithium-ion storage under SeaFloat concept; delivery expected 2028 alongside Estrella del Mar III (commissioned 2022). CapEx USD not on opened ST Engineering page. Distinct from prior Seaboard Estrella II/III presence.",
    "",
    "",
    "2025",
    "18.47",
    "-69.88",
    "Río Ozama / Santo Domingo floating power barge site (ST Engineering / Seaboard geography).",
    "steng_seaboard_estrella_iv_20251017",
    "ST Engineering’s Marine business and Siemens Energy have been awarded a second contract by Transcontinental Capital Corporation (Bermuda) Ltd., a subsidiary of Seaboard Corporation, to deliver Estrella del Mar IV",
    "https://www.stengg.com/en/newsroom/news-releases/st-engineering-and-siemens-energy-awarded-contract-for-2nd-floating-power-plant",
    "Actor: Seaboard Corporation (U.S. HQ) via Transcontinental Capital — us; OEMs ST Engineering (Singapore/allied) and Siemens Energy (allied) not dual-tagged. ST Engineering English primary. CapEx blank.",
    "hunt_energy_power_plants_grid",
    investment_type="epc",
    bib_type="company",
    chicago="ST Engineering. “ST Engineering and Siemens Energy Awarded Contract for 2nd Floating Power Plant in Dominican Republic.” Company English release, 17 October 2025. https://www.stengg.com/en/newsroom/news-releases/st-engineering-and-siemens-energy-awarded-contract-for-2nd-floating-power-plant.",
    annotation="ST Engineering primary naming Seaboard subsidiary. Supports seaboard_estrella_del_mar_iv_2025.",
    evid_note="Opened ST Engineering English page; Seaboard TCC award; 145 MW Siemens SeaFloat; delivery 2028; CapEx blank.",
)

# 7. copper / allied — Fortescue completes Alta Copper / Cañariaco
row_doc(
    "fortescue_canariaco_alta_copper_2026",
    "resources",
    "copper",
    "allied",
    "Fortescue — 100% Cañariaco Copper Project via Alta Copper acquisition (Northern Peru)",
    "Peru",
    "10 Mar 2026 Fortescue ASX: Nascent Exploration Pty Ltd completes Plan of Arrangement acquiring all Alta Copper Corp. shares not already owned; cash C$1.40/share implying total equity value ~C$139 million; Fortescue now 100% owner of Cañariaco Copper Project (91 km² porphyry corridor, Northern Peru). Immediate focus technical reviews, community engagement, and studies — no FID CapEx on page. Distinct from MMG Las Bambas / Zijin La Arena copper rows.",
    "139000000",
    "2026-03-10",
    "2026",
    "-6.05",
    "-79.25",
    "Cañariaco project area, Northern Peru (Fortescue ASX geography; approximate).",
    "fortescue_alta_copper_asx_20260310",
    "Alta Copper shareholders received cash consideration of C$1.40 per share, implying a total equity value of approximately C$139 million.",
    "https://content.fortescue.com/fortescue17114-fortescueeb60-productionbbdb-8be5/media/project/fortescueportal/shared/documents/regulatory/asx-announcements/automated/03066248-fortescue-completes-acquisition-of-alta-copper.pdf",
    "Actor: Fortescue Ltd (ASX:FMG; Australia HQ) — allied. Official ASX PDF. Value stored as CAD 139m equity consideration (company-stated; no FX applied — UNVERIFIED USD conversion omitted). Distinct from prior PRC Peru copper set.",
    "hunt_res_copper",
    investment_type="ownership_equity",
    currency="CAD",
    value_usd="",
    fx_usd="",
    evidence="documented",
    bib_type="filing",
    chicago="Fortescue Ltd. “Fortescue Completes Acquisition of Alta Copper.” ASX announcement PDF, 10 March 2026. https://content.fortescue.com/fortescue17114-fortescueeb60-productionbbdb-8be5/media/project/fortescueportal/shared/documents/regulatory/asx-announcements/automated/03066248-fortescue-completes-acquisition-of-alta-copper.pdf.",
    annotation="Fortescue ASX primary. Supports fortescue_canariaco_alta_copper_2026.",
    evid_note="Opened Fortescue ASX PDF; C$139m equity value; 100% Cañariaco; CAD stored without USD FX.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
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

    # Archive residual gold-primary Cangrejos (out_of_scope)
    if "cmoc_cangrejos_ecuador_1p7bn_2026" in by_id:
        r = rows[by_id["cmoc_cangrejos_ecuador_1p7bn_2026"]]
        if r["status"] == "active":
            r["status"] = "archived"
            marker = "Archived: out_of_scope — gold_silver (gold-primary deposit)."
            if marker not in (r.get("note") or ""):
                r["note"] = ((r.get("note") or "") + " " + marker).strip()

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
    print(f"Cycle 131 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
