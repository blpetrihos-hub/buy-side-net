#!/usr/bin/env python3
"""Cycle 137 hunt: shuffle_seed=20261137; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: solar, port_cranes, lithium, rail, wind, nickel, balsa,
power_plants_grid, graphite, building_materials, other_renewables, copper, water,
engineering_epc, niobium, fission_smr, port_ownership, bridges_roads.

PRC push with equal US/PRC budget (PRC ahead by 4 after 136 — no padding).
Thin top-up: balsa/graphite/nickel.
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


# 1. solar / prc — LONGi Hi-MO 9 modules for Yinson Sol de Verano 1 (Peru)
row_doc(
    "longi_sol_de_verano1_peru_53p2mw_2025",
    "energy",
    "solar",
    "prc",
    "LONGi — Hi-MO 9 module supply for Yinson Sol de Verano 1 (Peru)",
    "Peru",
    "16 May 2025 LONGi: partners with Yinson Renewables to supply 53.2 MW of Hi-MO 9 back-contact modules for Sol de Verano 1 near Majes, Peru — first phase of Yinson’s ground-mounted Peru plant; 82,836 modules; construction set to begin May 2025. Module CapEx USD not disclosed.",
    "",
    "",
    "2025",
    "-16.40",
    "-72.20",
    "Near Majes, Arequipa Region, Peru (Sol de Verano 1 site; approximate).",
    "longi_yinson_sol_verano_20250516",
    "16 May 2025 – LONGi … has partnered with global energy leader Yinson Renewables to supply 53.2MW of Hi-MO 9 modules for the Sol de Verano 1 Solar Project, near Majes in Peru. … The Sol de Verano 1 project … will deploy 82,836 Hi-MO 9 high efficiency modules … Construction is set to begin in May 2025",
    "https://www.longi.com/en/news/partnership-with-yinson-renewables/",
    "Actor: LONGi Green Energy (PRC OEM) — prc. Company English primary. CapEx blank (module supply). Distinct from Array Lupi / Sungrow San Martín Peru rows.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='LONGi Green Energy Technology Co., Ltd. “LONGi Powers Peru’s Renewable Vision with BC Technology, Showcasing Global Synergy for Local Impact.” May 16, 2025. https://www.longi.com/en/news/partnership-with-yinson-renewables/.',
    annotation="LONGi primary: 53.2 MW Hi-MO 9 for Yinson Sol de Verano 1 near Majes. Supports longi_sol_de_verano1_peru_53p2mw_2025.",
    evid_note="Opened LONGi English release 16 May 2025 (Sol de Verano 1 / 53.2 MW Hi-MO 9).",
)

# 2. solar / prc — LONGi Hi-MO 7 modules at Pétalo del Norte I (Colombia)
row_doc(
    "longi_petalo_norte_colombia_19p9mw_2025",
    "energy",
    "solar",
    "prc",
    "LONGi — Hi-MO 7 modules for Pétalo del Norte I (Colombia)",
    "Colombia",
    "11 Dec 2025 LONGi: Pétalo del Norte I inaugurated at La Esperanza, Norte de Santander — 19.9 MW installed capacity equipped with LONGi Hi-MO 7 modules; >43 GWh/y; CFM principal investor with EU support; Erco Energía developer/contractor; Andina Solar project management; 15-year PPA. Module CapEx USD not disclosed.",
    "",
    "",
    "2025",
    "7.91",
    "-72.66",
    "La Esperanza, Norte de Santander, Colombia (Pétalo del Norte I site).",
    "longi_petalo_norte_colombia_20251211",
    "Colombia, December 11 - La Esperanza, Norte de Santander — Colombia recently celebrated the inauguration of Pétalo del Norte I … With an installed capacity of 19.9 MW and equipped with LONGi’s Hi-MO 7 photovoltaic modules … Located in La Esperanza, Norte de Santander, Pétalo del Norte I will produce more than 43 GWh of clean energy per year",
    "https://www.longi.com/en/news/colombia-first-solar-project/",
    "Actor: LONGi Green Energy (PRC OEM) — prc. Company English primary. CapEx blank (module supply; CFM/Erco are non-US finance/developer). Distinct from Trina Pillancó / PowerChina Colombia solar rows.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='LONGi Green Energy Technology Co., Ltd. “With LONGi Photovoltaic Modules, Colombia Inaugurates Its First Solar Project Aligned with International Standards.” December 11, 2025. https://www.longi.com/en/news/colombia-first-solar-project/.',
    annotation="LONGi primary: Pétalo del Norte I 19.9 MW Hi-MO 7 at La Esperanza. Supports longi_petalo_norte_colombia_19p9mw_2025.",
    evid_note="Opened LONGi English release 11 Dec 2025 (Pétalo del Norte I / 19.9 MW).",
)

# 3. other_renewables / us — AES Dominicana 138.1 MW BESS package USD 94m
row_doc(
    "aes_dr_bess_138mw_94m_2025",
    "energy",
    "other_renewables",
    "us",
    "AES Dominicana Renewable Energy — 138.1 MW co-located BESS package (DR)",
    "Dominican Republic",
    "AES Dominicana Q3 2025 investor presentation (updated Dec 2025): 138.1 MW BESS project signed in Q3 2025 with NTP December 2025; co-located at PV assets but grid-operated independently — Bayasol 20.2 MW, Santanasol 27 MW, Mirasol 40.5 MW, Peravia I 50.4 MW; Fluence named on BESS timeline; US$94 million investment (70/30 D/E); 12–15 year terms after COD; tolling capacity payment amending Disco solar PPAs. Distinct from aes_dr_peravia_140mw_cod_2025 (solar COD).",
    "94000000",
    "2025-12-01",
    "2025",
    "18.28",
    "-70.33",
    "Baní / Peravia cluster, Dominican Republic (Peravia I BESS pin; Bayasol/Santanasol/Mirasol sites not dual-pinned).",
    "aes_dr_investor_q3_2025",
    "BESS NTP Dec 2025 +138.1 MWn … Project Bayasol Santanasol Mirasol Peravia I … BESS (MW) 20.2 MW 27 MW 40.5 MW 50.4 MW … US$94 million investment (70/30 D/E) … 138.1MW BESS project signed in Q3",
    "https://www.aesdominicana.com/sites/aesvault.com/files/2026-01/AES%20DR%20-%20Investor%20Presentation%202025%20Q3.pdf",
    "Actor: AES Corporation via AES Dominicana Renewable Energy — us. Company investor deck. CapEx USD 94m. Distinct from Peravia 140 MW solar COD row.",
    "hunt_energy_other_renewables",
    investment_type="greenfield_storage",
    bib_type="company",
    chicago='AES Dominicana. “Investor Presentation — Q3 2025.” Updated December 2025. https://www.aesdominicana.com/sites/aesvault.com/files/2026-01/AES%20DR%20-%20Investor%20Presentation%202025%20Q3.pdf.',
    annotation="AES Dominicana deck: 138.1 MW BESS NTP Dec 2025; USD 94m. Supports aes_dr_bess_138mw_94m_2025.",
    evid_note="Opened AES Dominicana Q3 2025 investor PDF (BESS 138.1 MW / USD 94m / NTP Dec 2025).",
)

# 4. solar / prc — CTG Brasil Complexo Solar Arinos full commercial operation
row_doc(
    "ctg_arinos_solar_full_cod_2025",
    "energy",
    "solar",
    "prc",
    "CTG Brasil — Complexo Solar Fotovoltaico Arinos full COD (Minas Gerais)",
    "Brazil",
    "17 Jun 2026 CTG Brasil sustainability release covering 2025: full commercial operation of Complexo Solar Fotovoltaico Arinos (MG) plus completion of Serra da Palmeira wind construction added ~1 GW renewable capacity; Arinos named as the solar COD milestone (annual-report companion cites 336.83 MW). CapEx USD not restated on opened page. Distinct from huawei_ctg_arinos_inv_2022 inverter-supply row and ctg_serra_da_palmeira_2025 wind ownership row.",
    "",
    "",
    "2025",
    "-15.92",
    "-46.11",
    "Arinos, Minas Gerais, Brazil (Complexo Solar Arinos; municipal pin).",
    "ctg_brasil_sustentabilidade_2025_20260617",
    "Com a entrada em operação comercial plena do Complexo Solar Arinos (MG) e a finalização da construção do Complexo Eólico Serra da Palmeira (PB), a companhia adicionou 1 GW de capacidade instalada.",
    "https://www.ctgbr.com.br/ctg-brasil-se-prepara-para-novo-ciclo-de-crescimento-sustentavel/",
    "Actor: CTG Brasil / China Three Gorges — prc. Company Portuguese primary. CapEx blank (COD/presence). Distinct from Huawei Arinos inverter and Serra da Palmeira wind rows.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='CTG Brasil. “CTG Brasil se prepara para novo ciclo de crescimento sustentável.” June 17, 2026. https://www.ctgbr.com.br/ctg-brasil-se-prepara-para-novo-ciclo-de-crescimento-sustentavel/.',
    annotation="CTG Brasil primary: Arinos solar full COD in 2025 portfolio. Supports ctg_arinos_solar_full_cod_2025.",
    evid_note="Opened CTG Brasil 17 Jun 2026 sustainability release (Arinos full COD).",
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
    print(f"Cycle 137 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
