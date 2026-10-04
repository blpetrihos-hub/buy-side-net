#!/usr/bin/env python3
"""Cycle 205 hunt: shuffle_seed=20261205; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261205).shuffle):
bridges_roads, solar, building_materials, balsa, power_plants_grid, water,
engineering_epc, copper, port_cranes, rail, nickel, lithium, niobium, graphite,
wind, other_renewables, fission_smr, port_ownership.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES/Freeport/EXIM/DFC/Fluence/Bechtel/Progress
Rail/Wabtec/Albemarle/EnergyX/USTDA/GE Vernova/SSA/Nextracker sweeps (catalog
dense; 0 new U.S. rows). PRC equal-budget: CAMC Bluefields/PowerChina Vicuña/
ZPMC/CRBC Arequipa/CRIG TAM-TSB already logged — miss.
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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


# 1. port_cranes / allied — Liebherr FCC 280 electric for Puerto Seguro Fluvial (Paraguay)
row_doc(
    "liebherr_psf_paraguay_fcc280_2026",
    "infrastructure",
    "port_cranes",
    "allied",
    "Liebherr — electric FCC 280 fixed cargo crane for Puerto Seguro Fluvial (Villeta)",
    "Paraguay",
    "26 May 2026 Liebherr-Rostock: second electric-powered FCC 280 (11 m pedestal; 80 t at 18 m outreach) for Puerto Seguro Fluvial S.A. on the Río Paraguay at Villeta — Paraguay’s largest multipurpose terminal; joins existing FCC 230 + prior FCC 280; pier extension for container ops; delivery scheduled Q3 2026. CapEx / contract USD not disclosed. Distinct from liebherr_compas_cartagena_lhm600_2026 / liebherr_cice_veracruz_gpr_2026 / liebherr_antigua_lhm420_2025.",
    "",
    "",
    "2026",
    "-25.548",
    "-57.552",
    "Puerto Seguro Fluvial, Villeta / Río Paraguay (company geography; approximate terminal pin).",
    "liebherr_psf_fcc280_20260526",
    "Featuring an 11‑metre pedestal and reinforced hydraulic systems, the latest unit offers an exceptional lifting capacity of 80 tonnes at an 18‑metre outreach. The crane operates with an electro-hydraulic drive that produces no emissions at the port… Delivery is scheduled for Q3 2026, timed to support the terminal’s expansion programme.",
    "https://www.liebherr.com/en-gb/n/liebherr-delivers-electric-powered-fcc-280-to-paraguay%e2%80%99s-leading-terminal-260928-4715716",
    "Actor: Liebherr-Rostock GmbH (Germany) — allied; buyer Puerto Seguro Fluvial S.A. Company English primary. CapEx blank. Shuffle port_cranes.",
    "hunt_cycle205",
    investment_type="equipment_supply",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Liebherr. “Liebherr delivers electric-powered FCC 280 to Paraguay’s leading terminal.” May 26, 2026. https://www.liebherr.com/en-gb/n/liebherr-delivers-electric-powered-fcc-280-to-paraguay%e2%80%99s-leading-terminal-260928-4715716.',
    annotation="Liebherr FCC 280 electric for Puerto Seguro Fluvial; CapEx blank. Supports liebherr_psf_paraguay_fcc280_2026.",
    evid_note="Opened Liebherr English company primary 2026-10-04; 80 t/18 m / Q3 2026 delivery / electro-hydraulic confirmed; CapEx undisclosed.",
)

# 2. solar / allied — Aldesa Abangares 86.3 MWp EPC (~EUR 80m)
row_doc(
    "aldesa_abangares_solar_80m_eur_2026",
    "energy",
    "solar",
    "allied",
    "Aldesa / Ozul — Abangares 86.3 MWp PV EPC (ICE / CoopeGuanacaste)",
    "Costa Rica",
    "24 Sep 2026 Aldesa: awarded EPC (consortium with Ozul) for Abangares photovoltaic park in Guanacaste — ~EUR 80 million; 86.3 MWp with 119,028 bifacial modules; output split 50% CoopeGuanacaste / 50% ICE; COD targeted August 2028. Distinct from aldesa_mexico_solar_hybrid_2026.",
    "80000000",
    "2026-09-24",
    "2026",
    "10.249",
    "-85.027",
    "Abangares canton, Guanacaste, Costa Rica (company geography; canton pin).",
    "aldesa_abangares_20260924",
    "Aldesa… has been awarded the EPC contract for the Abangares photovoltaic park, in consortium with Ozul. Valued at approximately €80 million, the facility will become the largest solar power generation infrastructure built in Costa Rica to date… 119,028 state-of-the-art bifacial photovoltaic modules, reaching a total installed capacity of 86.3 MWp.",
    "https://aldesa.com/en/aldesa-se-adjudica-el-mayor-parque-solar-de-costa-rica-por-80-millones-de-euros/",
    "Actor: Aldesa (Spain; CRCC-linked group) — allied. Company English primary. Face = EUR 80m; Fed H.10 24 Sep 2026 EURUSD 1.1373 → USD 90,984,000. Shuffle solar.",
    "hunt_cycle205",
    investment_type="epc",
    evidence="documented",
    currency="EUR",
    value_usd="90984000",
    fx_usd="1.1373",
    bib_type="company",
    chicago='Aldesa. “Aldesa awarded Costa Rica’s largest solar park in an €80 million project.” September 24, 2026. https://aldesa.com/en/aldesa-se-adjudica-el-mayor-parque-solar-de-costa-rica-por-80-millones-de-euros/.',
    annotation="Aldesa Abangares solar EPC: EUR 80m / 86.3 MWp. Supports aldesa_abangares_solar_80m_eur_2026.",
    evid_note="Opened Aldesa English company primary 2026-10-04; EUR 80m / 86.3 MWp / Aug 2028 COD confirmed. FX Fed H.10 2026-09-24 EURUSD 1.1373.",
)

# 3. copper / allied — KGHM–South32 Sierra Gorda fourth grinding line USD 725m
row_doc(
    "kghm_sierra_gorda_4th_line_725m_2026",
    "resources",
    "copper",
    "allied",
    "KGHM (55%) / South32 (45%) — Sierra Gorda fourth grinding line expansion",
    "Chile",
    "2 Oct 2026 KGHM: foundation stone for Sierra Gorda fourth grinding line (jaw crusher + HPGR + ball mill + flotation) — raises ore processing from ~48 Mtpa to ~60 Mtpa (~+20% copper); investment ~USD 725 million; completion end-2029 / full capacity 2H 2030; financed from operating cash flow and available debt. JV KGHM 55% / South32 45%. Distinct from fcx_el_abra_mill_chile_2026.",
    "725000000",
    "2026-10-02",
    "2026",
    "-22.89",
    "-69.32",
    "Sierra Gorda SCM, Antofagasta Region (~60 km SW of Calama; company geography; approximate mine pin).",
    "kghm_sierra_gorda_725m_20261002",
    "The project now underway will increase the plant’s processing capacity from around 48 million to around 60 million tonnes of ore per year, and boost copper production by around 20 per cent. The value of the investment being carried out by KGHM Polska Miedź S.A. in partnership with South32 Ltd. is approximately USD 725 million.",
    "https://media.kghm.com/en/news-and-press-releases/kghm-polska-miedz-s-a-is-launching-an-expansion-of-the-sierra-gorda-mine-worth-usd-725-million",
    "Actor: KGHM Polska Miedź (Poland, 55%) with South32 (Australia, 45%) — allied. Company English primary. CapEx face = USD 725m. Shuffle copper.",
    "hunt_cycle205",
    investment_type="capex_expansion",
    evidence="documented",
    currency="USD",
    value_usd="725000000",
    fx_usd="1",
    bib_type="company",
    chicago='KGHM Polska Miedź S.A. “KGHM Polska Miedź S.A. is launching an expansion of the Sierra Gorda mine worth USD 725 million.” October 2, 2026. https://media.kghm.com/en/news-and-press-releases/kghm-polska-miedz-s-a-is-launching-an-expansion-of-the-sierra-gorda-mine-worth-usd-725-million.',
    annotation="KGHM/South32 Sierra Gorda 4th grinding line: USD 725m. Supports kghm_sierra_gorda_4th_line_725m_2026.",
    evid_note="Opened KGHM English company primary 2026-10-04; USD 725m / ~48→60 Mtpa / end-2029 completion confirmed.",
)

# 4. wind / allied — Statkraft Gran Sul 280 MW FID (CapEx blank)
row_doc(
    "statkraft_gran_sul_280mw_2026",
    "energy",
    "wind",
    "allied",
    "Statkraft — Gran Sul 280 MW onshore wind FID (Santa Vitória do Palmar, RS)",
    "Brazil",
    "8 Jul 2026 Statkraft: investment decision for Gran Sul 280 MW onshore wind in Santa Vitória do Palmar, Rio Grande do Sul; moves to execution with construction scheduled to begin January 2027. CapEx / contract USD not disclosed on company page. Distinct from statkraft_emma_peru_72mw_2026.",
    "",
    "",
    "2026",
    "-33.519",
    "-53.368",
    "Santa Vitória do Palmar municipality, Rio Grande do Sul (company geography; municipal pin).",
    "statkraft_gran_sul_20260708",
    "Statkraft has decided to invest in Gran Sul, a 280 MW onshore wind project in the state of Rio Grande do Sul, Brazil… With the investment decision, Gran Sul now moves into the execution phase, construction scheduled to begin in January 2027.",
    "https://www.globenewswire.com/news-release/2026/07/08/3323837/0/en/Statkraft-to-invest-in-280-MW-wind-project-in-Brazil.html",
    "Actor: Statkraft AS (Norway) — allied. Company English primary via GlobeNewswire. CapEx blank (FID without disclosed USD). Shuffle wind.",
    "hunt_cycle205",
    investment_type="fid",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Statkraft AS. “Statkraft to invest in 280 MW wind project in Brazil.” July 8, 2026. https://www.globenewswire.com/news-release/2026/07/08/3323837/0/en/Statkraft-to-invest-in-280-MW-wind-project-in-Brazil.html.',
    annotation="Statkraft Gran Sul 280 MW FID; CapEx blank. Supports statkraft_gran_sul_280mw_2026.",
    evid_note="Opened Statkraft English GlobeNewswire primary 2026-10-04; 280 MW / Jan 2027 construction start confirmed; CapEx undisclosed.",
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
            rows[by_id[rid]].update(full)
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
    print(f"cycle205 added {len(added)}: {added}")
    print(f"cycle205 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
