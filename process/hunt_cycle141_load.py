#!/usr/bin/env python3
"""Cycle 141 hunt: shuffle_seed=20261141; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: graphite, niobium, balsa, bridges_roads, other_renewables,
water, solar, port_ownership, port_cranes, wind, power_plants_grid, lithium,
building_materials, rail, nickel, fission_smr, engineering_epc, copper.

PRC ahead by 6 after 140 — keep equal US/PRC budget without padding.
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


# 1. other_renewables / us — Invenergy La Toba hybrid solar+BESS (BCS)
row_doc(
    "invenergy_la_toba_70m_2022",
    "energy",
    "other_renewables",
    "us",
    "Invenergy — La Toba Energy Center 35 MW solar + 20 MW / 4-hour BESS (Comondú)",
    "Mexico",
    "Invenergy case study (opened 2026): La Toba Energy Center in Baja California Sur COD October 2022 — co-located 35 MW solar + 20 MW four-hour BESS (55 MW total); USD 70 million investment; company estimates ~30,000 homes and 3% of BCS summer peak demand; CO₂ offset ~130,000 t/y. Distinct from invenergy_patria_600mw_br_2024.",
    "70000000",
    "2022-10-01",
    "2022",
    "25.1967",
    "-111.7509",
    "La Toba / Los Algarrobos, Municipio de Comondú, Baja California Sur (site pin ~25.1967, -111.7509).",
    "invenergy_la_toba_case",
    "The center began commercial operation in October 2022, co-locating a 35-megawatt solar plant with a 20-megawatt, four-hour storage facility. … La Toba represents a $70 million investment. … Energy output from La Toba is estimated to be enough to power 30,000 homes and 3% of peak energy demand in the summer.",
    "https://www.invenergy.com/projects/case-studies/la-toba-energy-center",
    "Actor: Invenergy LLC (Chicago, IL HQ) — us. Company English case study. CapEx USD 70m documented. Hybrid solar+BESS coded other_renewables.",
    "hunt_energy_other_renewables",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago='Invenergy. “La Toba Energy Center.” Case study. https://www.invenergy.com/projects/case-studies/la-toba-energy-center.',
    annotation="Invenergy primary: La Toba 35 MW solar + 20 MW BESS; USD 70m; COD Oct 2022. Supports invenergy_la_toba_70m_2022.",
    evid_note="Opened Invenergy La Toba case study (35 MW + 20 MW BESS; USD 70m; COD Oct 2022).",
)

# 2. other_renewables / prc — Sungrow PowerTitan for Atlas BESS del Desierto
row_doc(
    "sungrow_atlas_bess_del_desierto_2025",
    "energy",
    "other_renewables",
    "prc",
    "Sungrow — PowerTitan ESS for Atlas BESS del Desierto 200 MW / 800 MWh (Chile)",
    "Chile",
    "Sungrow case page: PowerTitan ESS supply for Atlas Renewable Energy BESS del Desierto — plant 200 MW / 800 MWh standalone storage; COD 24 Apr 2025; 15-year PPA with Copec-EMOAC; ~280 GWh/y; C5 anti-corrosion / IP54 / liquid cooling. CapEx blank on OEM page. Distinct from atlas_bess_del_desierto_chile_2025 (U.S. Atlas ownership) and sungrow_zelestra_aurora_1gwh_chile_2025.",
    "",
    "",
    "2025",
    "-22.35",
    "-69.66",
    "María Elena / Antofagasta Region (Atlas BESS del Desierto geography; same pin as ownership row).",
    "sungrow_bess_del_desierto_case",
    "Project Name: BESS del Desierto Client Atlas Renewable Energy … COD Time: 2025. 04. 24 … Capacity (Plant Perspective): 200 MW/800 MWh … To combat the harsh desert environment, Sungrow deployed its PowerTitan ESS. … The project will feed approximately 280 GWh of clean electricity into the grid each year. Additionally, under a 15-year PPA with Copec-EMOAC",
    "https://www.sungrowpower.com/us/en/case/utility-scale/largest-standalone-storage-project-200mw-800mwh-in-atlas",
    "Actor: Sungrow (PRC HQ) — prc; plant owner Atlas (U.S./GIP) logged separately. Company English case. CapEx blank.",
    "hunt_energy_other_renewables",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Sungrow. “Sungrow Helps Atlas Energy Deliver Its Largest Standalone Energy Storage Plant.” Case study (BESS del Desierto 200 MW/800 MWh; COD 24 Apr 2025). https://www.sungrowpower.com/us/en/case/utility-scale/largest-standalone-storage-project-200mw-800mwh-in-atlas.',
    annotation="Sungrow primary: PowerTitan for Atlas BESS del Desierto 200 MW/800 MWh COD Apr 2025. Supports sungrow_atlas_bess_del_desierto_2025.",
    evid_note="Opened Sungrow English case (BESS del Desierto PowerTitan; COD 2025-04-24).",
)

# 3. solar / prc — CTG LatAm Baranoa Phase II+III full-capacity COD
row_doc(
    "ctg_baranoa_ii_iii_58p3mw_2025",
    "energy",
    "solar",
    "prc",
    "CTG LatAm — Baranoa Solar Phase II+III full-capacity COD 58.3 MW (Atlántico)",
    "Colombia",
    "4 Dec 2025 CTG (English): on 30 Nov 2025 Baranoa Phase II and Phase III entered operation — full-capacity grid connection of CTG LatAm three-phase Baranoa Solar PV Project totaling 58.3 MW (~110 GWh/y; ~45,000 households; ~98,700 t CO₂/y avoided); 31 days ahead of schedule; described as China’s first greenfield solar project in Colombia. CapEx blank. Distinct from powerchina_baranoa_phase1_2025 (POWERCHINA EPC Phase 1) and ctg_nisperos_solar_colombia_2026 (separate Nísperos COD at same municipality).",
    "",
    "",
    "2025",
    "10.79",
    "-74.92",
    "Baranoa, Atlántico Department, Colombia (CTG LatAm Baranoa site municipality).",
    "ctg_baranoa_ii_iii_20251204",
    "On Nov 30, China's first greenfield solar project in Colombia — the Baranoa Solar PV Project — achieved full-capacity grid connection as Phase II and Phase III entered operation. Invested and built by CTG LatAm, the three-phase project has a total installed capacity of 58.3 MW, generating 110 million kWh of clean power annually, enough for 45,000 households and reducing 98,700 tonnes of CO₂ each year",
    "https://www.ctg.com.cn/ctgenglish/news_media/news37/2025122215512388368/index.html",
    "Actor: CTG LatAm / China Three Gorges — prc. Company English primary. CapEx blank. Distinct from POWERCHINA Baranoa Phase 1 and CTG Nísperos.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago='China Three Gorges Corporation. “The Baranoa Phase II and III Solar PV Projects in Colombia successfully connected to the grid.” December 4, 2025. https://www.ctg.com.cn/ctgenglish/news_media/news37/2025122215512388368/index.html.',
    annotation="CTG primary: Baranoa Phase II+III COD Nov 30 2025; three-phase total 58.3 MW. Supports ctg_baranoa_ii_iii_58p3mw_2025.",
    evid_note="Opened CTG English release 4 Dec 2025 (Baranoa II+III full-capacity COD; 58.3 MW).",
)

# 4. wind / prc — SPIC Brasil Pedra de Amolar + Paraíso Farol (Touros RN)
# BRL 755m → USD via ECB 2025-06-30: BRL/EUR 6.4384; USD/EUR 1.172 → USD/BRL = 1.172/6.4384 ≈ 0.18203
row_doc(
    "spic_pedra_paraiso_touros_755m_brl_2025",
    "energy",
    "wind",
    "prc",
    "SPIC Brasil — Pedra de Amolar + Paraíso Farol wind clusters 105.4 MW (Touros RN)",
    "Brazil",
    "SPIC Brasil Sustainability Report 2025 (EN): construction of Pedra de Amolar and Paraíso Farol wind clusters in Touros, Rio Grande do Norte — 100% SPIC Brasil-managed; total CapEx BRL 755 million; expected COD 2026; Paraíso Farol 7 WTGs / 43.4 MW; Pedra de Amolar 10 WTGs / 62 MW; combined 105.4 MW. Distinct from goldwind_spic_touros_br_2025 (Goldwind turbine supply for same ~105.4 MW RN farms) and spic_recurrent_marangatu_br_2024 (solar).",
    "755000000",
    "2025-06-30",
    "2025",
    "-5.20",
    "-35.55",
    "Touros municipality, Rio Grande do Norte, Brazil (SPIC RS geography; approximate municipal pin).",
    "spic_brasil_rs_2025_pedra_paraiso",
    "in 2025 we made progress on the construction of the Paraíso Farol and Pedra de Amolar wind clusters (projects managed entirely by SPIC Brasil) in Rio Grande do Norte. … representing a total investment of BRL 755 million. … expected to begin operations in 2026. The Paraíso Farol cluster will have seven wind turbines, with a total installed capacity of 43.4 MW, while Pedra de Amolar will have ten wind turbines, with a total capacity of 62 MW. Together, they will have an installed capacity of 105.4 MW",
    "https://www.spicbrasil.com.br/en/wp-content/uploads/sites/5/2026/05/RS_2025_SPIC-Brasil_EN_D4f.pdf",
    "Actor: SPIC Brasil (State Power Investment Corp. / PRC) — prc. Company English RS 2025 PDF. BRL 755m → USD 137,433,828 via ECB 2025-06-30 (USD/EUR 1.172; BRL/EUR 6.4384 → USD/BRL = 1.172/6.4384). Distinct from Goldwind turbine-supply row for same capacity.",
    "hunt_energy_wind",
    investment_type="greenfield_generation",
    currency="BRL",
    value_usd="137433828",
    fx_usd="0.18203",
    bib_type="company",
    chicago='SPIC Brasil. Sustainability Report 2025 (English). Pedra de Amolar and Paraíso Farol wind clusters, Touros RN — 105.4 MW; BRL 755 million; COD 2026. https://www.spicbrasil.com.br/en/wp-content/uploads/sites/5/2026/05/RS_2025_SPIC-Brasil_EN_D4f.pdf.',
    annotation="SPIC Brasil RS 2025: Pedra/Paraíso 105.4 MW; BRL 755m CapEx; Touros RN. Supports spic_pedra_paraiso_touros_755m_brl_2025.",
    evid_note="Opened SPIC Brasil RS 2025 EN PDF (Pedra de Amolar + Paraíso Farol; BRL 755m; 105.4 MW). ECB EXR D.USD.EUR and D.BRL.EUR 2025-06-30.",
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
    print(f"Cycle 141 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
