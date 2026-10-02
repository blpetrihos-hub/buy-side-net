#!/usr/bin/env python3
"""Cycle 133 hunt: shuffle_seed=20261133; equal budget; U.S./PRC split; thin after.

Order: copper, niobium, engineering_epc, port_cranes, wind, bridges_roads,
fission_smr, building_materials, other_renewables, water, balsa, lithium,
power_plants_grid, solar, port_ownership, graphite, rail, nickel.

PRC push (still slightly behind US post-audit). Thin top-up: balsa/graphite/nickel.
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


# 1. copper / allied — Metso SX-EW for Southern Peru Copper Tía María
row_doc(
    "metso_tia_maria_sxew_eur100m_2026",
    "resources",
    "copper",
    "allied",
    "Metso Corporation — VSF SX-EW plant supply (Southern Peru Copper / Tía María)",
    "Peru",
    "30 Mar 2026 Metso press release: signed major agreement with Southern Peru Copper Corporation for copper solvent extraction and electrowinning (SX-EW) technology at the Tía María project in Cocachacra, Islay, Arequipa; plant designed for 120,000 t/y LME Grade A cathodes; order value EUR 100 million booked in Minerals Q1 2026 intake; scope includes VSF SX-EW plants, Dual Media Filters, robotic cathode stripping, acid mist capture, site advisory, commissioning and start-up spares; basic engineering already completed. Distinct from Southern Copper CapEx / notes rows.",
    "100000000",
    "2026-03-30",
    "2026",
    "-17.09",
    "-71.77",
    "Tía María / Cocachacra, Islay Province, Arequipa, Peru (Metso geography; approximate pin).",
    "metso_tia_maria_sxew_20260330",
    "Metso has signed a major agreement with Southern Peru Copper Corporation… for the supply of copper Solvent Extraction and Electrowinning (SX-EW) technology to the company’s Tia Maria project in Cocachacra, Province of Islay, Arequipa, Peru. The new plant will produce 120,000 tons of high-purity (LME grade A) copper cathodes per year. The order value of EUR 100 million has been booked in the Minerals segment’s 2026 first-quarter order intake.",
    "https://www.metso.com/corporate/media/news/2026/3/metso-wins-major-greenfield-contract-to-supply-copper-refining-technology-to-southern-peru-copper-corporation/",
    "Actor: Metso Corporation (Espoo, Finland HQ) — allied; buyer Southern Peru Copper / Group México. Company English primary. EUR 100m; USD via ECB reference rate 1.1484 on 2026-03-30.",
    "hunt_res_copper",
    investment_type="equipment_supply",
    currency="EUR",
    value_usd="114840000",
    fx_usd="1.1484",
    bib_type="company",
    chicago="Metso Corporation. “Metso wins major greenfield contract to supply copper refining technology to Southern Peru Copper Corporation.” Press release, 30 March 2026. https://www.metso.com/corporate/media/news/2026/3/metso-wins-major-greenfield-contract-to-supply-copper-refining-technology-to-southern-peru-copper-corporation/.",
    annotation="Metso primary: Tía María SX-EW EUR 100m. Supports metso_tia_maria_sxew_eur100m_2026.",
    evid_note="Opened Metso corporate press release; EUR 100m / 120 ktpa named. ECB EXR D.USD.EUR 2026-03-30 = 1.1484.",
)

# 2. niobium / allied — St George CIT-SENAI pilot plant study (thin-adjacent)
row_doc(
    "st_george_cit_senai_pilot_2026",
    "resources",
    "niobium",
    "allied",
    "St George Mining — CIT-SENAI pilot-plant niobium flotation study (Araxá)",
    "Brazil",
    "2 Sep 2026 St George ASX release: pilot plant beneficiation study commenced at CIT-SENAI (Belo Horizonte) on ~9 tonnes near-surface Araxá saprolite; locked-cycle flotation with recycle streams; niobium concentrate destined for ferroniobium downstream tests; rare-earth-enriched flotation tailings for MREC/oxalate hydromet tests; results expected Q4 2026. Distinct from CEFET-MG Araxá campus pilot-plant construction row (st_george_cefet_pilot_plant_2026). CapEx blank (testwork).",
    "",
    "",
    "2026",
    "-19.92",
    "-43.94",
    "CIT-SENAI pilot facility, Belo Horizonte, Minas Gerais (ASX geography; approximate pin).",
    "st_george_cit_senai_asx_20260902",
    "Pilot plant study commenced at CIT-SENAI to build on the strong results from initial flotation beneficiation test work that produced a high-grade niobium concentrate and a rare earth enriched tailings stream… About 9 tonnes of near-surface saprolite material from the Araxá Project is being used in the study, which will continue for four to six weeks… Results from the beneficiation test work are expected in Q4 2026.",
    "https://www.stgm.com.au/pdf/c83fbdbe-842d-47e2-9b84-835b63973c17/Platform/ListPage/Pilot-Plant-Test-Work-at-Araxa-Project.pdf",
    "Actor: St George Mining Limited (ASX:SGQ; Australia HQ) — allied. Company ASX PDF opened. CapEx blank. Distinct from CEFET pilot construction.",
    "hunt_res_niobium",
    investment_type="other",
    bib_type="company",
    chicago="St George Mining Limited. “Pilot Plant Beneficiation Test Work at Araxá Project, Brazil.” ASX release, 2 September 2026. https://www.stgm.com.au/pdf/c83fbdbe-842d-47e2-9b84-835b63973c17/Platform/ListPage/Pilot-Plant-Test-Work-at-Araxa-Project.pdf.",
    annotation="St George ASX primary: CIT-SENAI 9t pilot study. Supports st_george_cit_senai_pilot_2026.",
    evid_note="Opened St George ASX PDF 2 Sep 2026; CIT-SENAI pilot named; CapEx blank.",
)

# 3. bridges_roads / prc — CREC China Railway No.10 Saramiriza road (Peru)
row_doc(
    "crec_saramiriza_road_peru_2025",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Railway No.10 Engineering Group (CREC) — Saramiriza Road (Borja)",
    "Peru",
    "16 Apr 2025 CREC English release: Saramiriza Road Project constructed by China Railway No.10 Engineering Group under CREC in Peru’s tropical rainforest region passed preliminary inspection on 26 Mar local time; newly built road spans 16.22 km in the Borja region; inspection team approved preliminary acceptance. CapEx USD not disclosed on opened page. Distinct from CCECC Cajamarca / Huancavelica road rows.",
    "",
    "",
    "2025",
    "-4.47",
    "-77.55",
    "Saramiriza / Borja region, Loreto, Peru (CREC geography; approximate pin).",
    "crec_saramiriza_20250416",
    "On March 26 local time, the Saramiriza Road Project constructed by China Railway No.10 Engineering Group under CREC in Peru’s tropical rainforest region passed its preliminary inspection. The newly built Saramiriza road spans 16.22 kilometers and is located in the Borja region.",
    "https://www.crecg.com/zgztywz/cs11/10210606/2025040717024884356/index.html",
    "Actor: China Railway No.10 / CREC (PRC SOE) — prc. Company English primary. CapEx blank.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="company",
    chicago="China Railway Engineering Corporation (CREC). “Peru’s Saramiriza Road Project Passed Preliminary Inspection.” 16 April 2025. https://www.crecg.com/zgztywz/cs11/10210606/2025040717024884356/index.html.",
    annotation="CREC primary: Saramiriza 16.22 km preliminary acceptance. Supports crec_saramiriza_road_peru_2025.",
    evid_note="Opened CREC English page; 16.22 km Borja named; CapEx blank.",
)

# 4. bridges_roads / prc — CCECC Huancavelica highland road handover
row_doc(
    "ccecc_huancavelica_road_207km_2026",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Civil Engineering Construction Corporation (CCECC) — Huancavelica Road (207.8 km)",
    "Peru",
    "1 Apr 2026 CCECC (中国土木) company bulletin via Goalfore: Peru Huancavelica Road Project constructed by CCECC passed handover/acceptance after five years; 207.8 km high-altitude Andean artery spanning Huancavelica and Ayacucho regions (elevations ~1,500–4,960 m; average ~3,800 m); full-cycle rebuild + maintenance + traffic assurance; commute cited as cut from ~16 h to ~6 h. CapEx USD not disclosed on opened page. Distinct from CCECC Cajamarca and CREC Saramiriza rows.",
    "",
    "",
    "2026",
    "-12.79",
    "-74.97",
    "Huancavelica–Ayacucho highland corridor, Peru (CCECC geography; approximate mid-route pin).",
    "ccecc_huancavelica_20260401",
    "近日，由中国土木承建的秘鲁万卡维利卡公路项目顺利通过交工验收，历经五年匠心履约，这条横贯安第斯山脉腹地的207.8公里高原交通干线正式落成……区域间通勤时间从原本的16小时大幅缩减至6小时。",
    "https://news.goalfore.cn/latest/detail/100386.html",
    "Actor: CCECC / China Civil Engineering (PRC SOE; CCCC affiliate) — prc. Company bulletin (中国土木) opened via Goalfore republish. CapEx blank.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="company",
    chicago="China Civil Engineering Construction Corporation (中国土木). “秘鲁万卡维利卡公路项目圆满交验.” Company bulletin, 1 April 2026. https://news.goalfore.cn/latest/detail/100386.html.",
    annotation="CCECC company bulletin: Huancavelica 207.8 km handover. Supports ccecc_huancavelica_road_207km_2026.",
    evid_note="Opened CCECC/中国土木 bulletin via Goalfore; 207.8 km / 5-year handover named; CapEx blank.",
)

# 5. power_plants_grid / us — NFE CELBA 2 first fire (Barcarena)
row_doc(
    "nfe_celba2_first_fire_624mw_2025",
    "energy",
    "power_plants_grid",
    "us",
    "New Fortress Energy — CELBA 2 624 MW gas power plant first fire (Barcarena)",
    "Brazil",
    "6 Oct 2025 NFE IR press release: achieved first fire at 624 MW CELBA 2 Power Plant in northern Brazil (Barcarena), marking start of hot commissioning; COD expected later in 2025. Barcarena terminal cited with 2.2 GW under development including CELBA 2 and 1.6 GW PortoCem (PortoCem already logged separately). CapEx for CELBA 2 not disclosed on opened page.",
    "",
    "",
    "2025",
    "-1.55",
    "-48.75",
    "CELBA 2 / Barcarena, Pará, Brazil (NFE geography; approximate pin).",
    "nfe_celba2_first_fire_20251006",
    "New Fortress Energy Inc. (NASDAQ: NFE)… today announced that it has achieved first fire at its 624 MW CELBA 2 Power Plant in northern Brazil, marking a major operational milestone toward commercial operations. The first fire signifies the successful initial ignition of the plant’s gas turbines and the start of the hot commissioning process.",
    "https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-achieves-first-fire-celba-2-power-plant",
    "Actor: New Fortress Energy Inc. (NASDAQ:NFE; U.S. HQ) — us. Company IR primary. CapEx blank. Distinct from nfe_portocem_1p6gw_epc_2024.",
    "hunt_energy_power_plants_grid",
    investment_type="ownership_equity",
    bib_type="company",
    chicago="New Fortress Energy Inc. “New Fortress Energy Achieves First Fire at CELBA 2 Power Plant.” IR news release, 6 October 2025. https://ir.newfortressenergy.com/news-releases/news-release-details/new-fortress-energy-achieves-first-fire-celba-2-power-plant.",
    annotation="NFE IR primary: CELBA 2 624 MW first fire. Supports nfe_celba2_first_fire_624mw_2025.",
    evid_note="Opened NFE IR release; 624 MW Barcarena first fire named; CapEx blank.",
)

# 6. rail / prc — CHEC/CCCC Bogotá Metro Line 1 franchise (first-train milestone 2025)
row_doc(
    "chec_bogota_metro_l1_5p016bn",
    "infrastructure",
    "rail",
    "prc",
    "China Harbour Engineering / CCCC — Bogotá Metro Line 1 DBFOM franchise (30 trains)",
    "Colombia",
    "Opened CHEC project page: Bogotá Subway Line 1 franchise awarded Nov 2019; 23.86 km / 16 stations / purchase of 30 trainsets; total contract USD 5.016 billion (EPC ~USD 3.240bn; O&M USD 1.776bn); franchise ~28 years. Cross-checked 2 Jul 2025 CCCC English release: first six-car GOA4 driverless train (“Gaby”) dispatched from Changchun for Line 1, contracted by CHEC — first-train milestone sets observation year 2025 within mandate window. Distinct from CRRC Salvador / SP metro rolling-stock rows.",
    "5016000000",
    "2025-07-02",
    "2025",
    "4.61",
    "-74.08",
    "Bogotá Metro Line 1 corridor, Bogotá, Colombia (CHEC/CCCC geography; approximate city pin).",
    "chec_bogota_metro_l1_project",
    "The total contract amount of the project is worth 5.016 billion U.S. dollars, wherein EPC is about 3.240 billion U.S. dollars, and the operation and maintenance is 1.776 billion U.S. dollars… With a total length of 23.86km, the project includes the construction of 16 stations and the purchase of 30, 7-group train wagons.",
    "https://www.chec.bj.cn/pub/chec_pc/en/ssbl/tzyys/gd/202208/t20220803_8320.html",
    "Actor: CHEC / CCCC (PRC SOE) consortium lead — prc; CRRC Changchun trains. CapEx from opened CHEC project page. First-train milestone cross-checked on opened CCCC English release (https://en.ccccltd.cn/xwzx/ywfb/202507/t20250707_221164.html).",
    "hunt_infra_rail",
    investment_type="concession",
    bib_type="company",
    chicago="China Harbour Engineering Company Ltd. “Bogota Subway Line 1 Project- Columbia.” Project page. https://www.chec.bj.cn/pub/chec_pc/en/ssbl/tzyys/gd/202208/t20220803_8320.html.",
    annotation="CHEC primary CapEx USD 5.016bn; CCCC first-train cross-check. Supports chec_bogota_metro_l1_5p016bn.",
    evid_note="Opened CHEC project page (USD 5.016bn) and CCCC English release (first train Gaby Jul 2025).",
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
    print(f"Cycle 133 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
