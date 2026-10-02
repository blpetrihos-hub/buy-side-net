#!/usr/bin/env python3
"""Cycle 135 hunt: shuffle_seed=20261135; equal budget; U.S./PRC split; thin after.

Order: wind, copper, other_renewables, port_cranes, fission_smr, engineering_epc,
bridges_roads, lithium, port_ownership, nickel, power_plants_grid, graphite,
building_materials, rail, balsa, solar, niobium, water.

PRC push continues (sides nearly even after 134). Thin top-up: balsa/graphite/nickel.
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


# 1. wind / allied — Solaer Calbuco 47 MW + 80 MWh; USD 65m construction financing
row_doc(
    "solaer_calbuco_chile_65m_2026",
    "energy",
    "wind",
    "allied",
    "Solaer Renewable Energies — Calbuco wind farm (47 MW) + ~80 MWh storage",
    "Chile",
    "22 Sep 2026 Ctech (Calcalist): Israeli Solaer secures USD 65 million construction financing for first Chile wind project — 47 MW farm in Calbuco area south of Puerto Montt with ~80 MWh storage; Solaer holds 47% stake; construction began 2025; 11-year PPA; grid connection expected 2027; additional USD 6.3m facility for guarantees/VAT. CapEx blank beyond disclosed financing. Distinct from ENAPAC desal row.",
    "65000000",
    "2026-09-22",
    "2026",
    "-41.77",
    "-73.13",
    "Calbuco area, Los Lagos Region, Chile (south of Puerto Montt; approximate municipal pin).",
    "ctech_solaer_calbuco_2026",
    "The project involves the construction of a 47-megawatt wind farm in the Calbuco area of southern Chile, south of Puerto Montt. It will also include approximately 80 megawatt-hours of energy storage. Solaer holds a 47% stake in the project. … securing $65 million in financing for construction.",
    "https://www.calcalistech.com/ctechnews/article/dimbwlbc0",
    "Actor: Solaer (Israel HQ; TASE-listed) — allied. Press primary opened (Ctech). Value is construction financing USD 65m (not full CapEx). CapEx blank beyond financing figure.",
    "hunt_energy_wind",
    investment_type="financing",
    bib_type="press",
    chicago='Prager, Amir. “Solaer secures $65 million for first wind project in Chile.” Ctech / Calcalist, September 22, 2026. https://www.calcalistech.com/ctechnews/article/dimbwlbc0.',
    annotation="Solaer Calbuco 47 MW / 80 MWh; USD 65m financing. Supports solaer_calbuco_chile_65m_2026.",
    evid_note="Opened Ctech article naming Calbuco 47 MW, 80 MWh storage, USD 65m financing, 47% stake.",
)

# 2. copper / us — FCX open-market Cerro Verde stake increase USD 107m
row_doc(
    "fcx_cerro_verde_stake_107m_2026",
    "resources",
    "copper",
    "us",
    "Freeport-McMoRan — Cerro Verde open-market share purchase (55.08% → 55.66%)",
    "Peru",
    "FCX Q2 2026 earnings exhibit 99.1 (SEC): during 2Q 2026 purchased 2.0 million Cerro Verde common shares in the open market for USD 107 million, increasing ownership from 55.08% to 55.66%. Distinct from Cerro Verde MEIA / Enlozada / renewable-PPA rows.",
    "107000000",
    "2026-05-31",
    "2026",
    "-16.53",
    "-71.57",
    "Cerro Verde mine, Arequipa Region, Peru (approximate UP pin).",
    "fcx_2q2026_exhibit991_cerro_verde",
    "During second-quarter 2026, FCX purchased 2.0 million shares of Cerro Verde common stock in the open market for $107 million, increasing its ownership interest in Cerro Verde from 55.08% to 55.66%.",
    "https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm",
    "Actor: Freeport-McMoRan Inc. (Phoenix, U.S. HQ) — us. SEC exhibit primary. Ownership_equity purchase USD 107m (May 2026).",
    "hunt_res_copper",
    investment_type="ownership_equity",
    bib_type="sec",
    chicago='Freeport-McMoRan Inc. “Freeport-McMoRan Reports Second-Quarter and Six-Month 2026 Results.” Exhibit 99.1 to Form 8-K, 2026. https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm.',
    annotation="SEC exhibit: Cerro Verde open-market buy USD 107m to 55.66%. Supports fcx_cerro_verde_stake_107m_2026.",
    evid_note="Opened FCX SEC exhibit 99.1 Q2 2026; Cerro Verde share purchase paragraph.",
)

# 3. other_renewables / prc — Jinko ESS Chile 340 MW / 1.6 GWh (METLEN)
row_doc(
    "jinko_ess_chile_340mw_1600mwh_2025",
    "energy",
    "other_renewables",
    "prc",
    "Jinko ESS — Chile utility-scale BESS supply (340 MW / 1.6 GWh; METLEN)",
    "Chile",
    "Jinko ESS reference-project page lists Chile Utility-Scale Energy Storage Project 340 MW / 1.6 GWh (Sep 2025). Cross-checked 24 Jun 2025 JinkoSolar news: Jinko ESS–METLEN frame agreement for >3 GWh across Chile and Europe, built around the 1.6 GWh Chile project with G2 Utility systems; full delivery scheduled Q4 2025. Distinct from jinko_aloe_bess (SEA pertinencia / different MW-MWh) and jinko_bess_amanecer. CapEx blank.",
    "",
    "",
    "2025",
    "",
    "",
    "Chile (utility-scale BESS; company listing does not name a single municipality — lat/lon blank).",
    "jinkoess_chile_reference_340mw_2025",
    "The collaboration centers on a 1.6 GWh project currently under development in Chile, for which Jinko ESS will supply its advanced G2 Utility Series energy storage systems, with full delivery scheduled for Q4 2025. … Chile Utility-Scale Energy Storage Project … 340MW/1.6GWh Capacity … Sep 2025",
    "https://www.jinkoess.com/en/site/reference-project",
    "Actor: Jinko ESS / JinkoSolar (PRC) — prc; METLEN offtake/developer partner (Greece). Company English primary opened; CapEx blank. Cross-check jinkosolar.com/en/site/newsdetail/2641.",
    "hunt_energy_other_renewables",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Jinko ESS. “Energy Storage Projects / Project Cases.” Chile Utility-Scale Energy Storage Project 340 MW / 1.6 GWh (Sep 2025). https://www.jinkoess.com/en/site/reference-project.',
    annotation="Jinko ESS Chile 340 MW/1.6 GWh; CapEx blank. Supports jinko_ess_chile_340mw_1600mwh_2025.",
    evid_note="Opened Jinko ESS reference-project page and JinkoSolar METLEN frame-agreement news (1.6 GWh Chile).",
)

# 4. other_renewables / prc — Xinyuan/SPIC Atacama Chile BESS RMB 381.8m
row_doc(
    "xinyuan_spic_atacama_bess_chile_rmb381m_2024",
    "energy",
    "other_renewables",
    "prc",
    "Xinyuan Smart Storage (China Power / SPIC) — Tierra Amarilla Atacama BESS 110 MW / 220 MWh",
    "Chile",
    "15 Apr 2024 China Power International Development HKEX announcement: Xinyuan Smart Storage sells BESS equipment/services to Shandong Ludian for Atacama Project — 110 MW / 220 MWh energy storage at Tierra Amarilla, Copiapó Province, Atacama Region, Chile; consideration RMB 381,807,090 (inclusive of taxes). Distinct from CIP Patache / AES Atacama BESS rows.",
    "381807090",
    "2024-04-15",
    "2024",
    "-27.48",
    "-70.27",
    "Tierra Amarilla, Copiapó Province, Atacama Region, Chile (company-named site; approximate municipal pin).",
    "chinapower_xinyuan_atacama_bess_20240415",
    "Xinyuan Smart Storage… entered into a BESS S&P Contract with Shandong Ludian on 15 April 2024 in relation to the provision of equipment and components for an energy storage system and its related services for an overseas energy storage project located in Tierra Amarilla, Province of Copiapo, Atacama Region, Chile. … The consideration under the BESS S&P Contract payable to Xinyuan Smart Storage is RMB 381,807,090 (inclusive of all taxes). … “Atacama Project” A 110MW/220MWh energy storage project",
    "https://doc.irasia.com/listco/hk/chinapower/announcement/a240415.pdf",
    "Actor: Xinyuan Smart Storage (China Power International / SPIC group; PRC) — prc. HKEX primary. RMB 381,807,090 → USD 52,746,342 via ECB 2024-04-15 (USD/EUR 1.0656; CNY/EUR 7.7134 → USD/CNY = 1.0656/7.7134).",
    "hunt_energy_other_renewables",
    investment_type="equipment_supply",
    currency="CNY",
    value_usd="52746342",
    fx_usd="0.13815",
    bib_type="company",
    chicago='China Power International Development Limited. “Connected Transaction — Energy Storage System Equipment Sale and Purchase Contract.” HKEX announcement, 15 April 2024. https://doc.irasia.com/listco/hk/chinapower/announcement/a240415.pdf.',
    annotation="HKEX primary: Atacama Chile 110 MW/220 MWh; RMB 381.8m. Supports xinyuan_spic_atacama_bess_chile_rmb381m_2024.",
    evid_note="Opened China Power HKEX PDF a240415; RMB consideration and Tierra Amarilla 110 MW/220 MWh named. ECB EXR D.USD.EUR and D.CNY.EUR 2024-04-15.",
)

# 5. other_renewables / other — Promigas acquires Zelestra LatAm ~USD 1.1bn EV
row_doc(
    "promigas_zelestra_latam_1p1bn_2026",
    "energy",
    "other_renewables",
    "other",
    "Promigas — acquisition of Zelestra Latin America platform (~3,500 MW solar/storage)",
    "Colombia",
    "28 May 2026 Zelestra English release: completes sale of Latin America platform to Promigas (Colombia multi-energy holding) for c. USD 1.1 billion enterprise value including project-finance debt; ~3,500 MW renewables in operation, under construction and development across Chile, Peru and Colombia (solar + storage). Promigas special page cross-check: 1,273 MW operating/construction + ~2,250 MW development; Chile market entry. Distinct from Sungrow–Zelestra equipment rows (seller-side OEM). CapEx = disclosed EV.",
    "1100000000",
    "2026-05-28",
    "2026",
    "",
    "",
    "Multi-country LatAm portfolio (Chile, Peru, Colombia); no single-site pin — lat/lon blank. Country coded Colombia (buyer HQ / controlling operator).",
    "zelestra_latam_sale_promigas_2026",
    "Zelestra… confirms the completion of the sale of its Latin America platform to Promigas, a leading multi-energy holding company based in Colombia. The transaction, valued at c. USD 1.1 billion (including project finance debt), includes approximately 3,500 MW of renewable energy projects in operation, under construction and in development across Chile, Peru and Colombia.",
    "https://zelestra.energy/en/news/latam-sale",
    "Actor: Promigas S.A. E.S.P. (Barranquilla, Colombia HQ) — other (not U.S./PRC HQ). Seller Zelestra (Spain) exits LatAm ownership. Company English primary opened.",
    "hunt_energy_other_renewables",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Zelestra. “Zelestra completes the sale of its Latin America Business Unit to Promigas for $1.1B Enterprise Value.” May 28, 2026. https://zelestra.energy/en/news/latam-sale.',
    annotation="Zelestra→Promigas LatAm EV ~USD 1.1bn / ~3,500 MW. Supports promigas_zelestra_latam_1p1bn_2026.",
    evid_note="Opened Zelestra LatAm sale page; Promigas special page cross-check for MW split.",
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
    print(f"Cycle 135 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
