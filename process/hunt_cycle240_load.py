#!/usr/bin/env python3
"""Cycle 240 hunt: shuffle_seed=20261240; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261240).shuffle):
rail, solar, port_cranes, building_materials, graphite, niobium, other_renewables,
wind, port_ownership, lithium, engineering_epc, balsa, power_plants_grid,
bridges_roads, fission_smr, nickel, copper, water.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: CapEx-fill Atlas Lithium Neves 71% contracted face
  (~USD 34.31m = 71% of DFS USD 57.56m × 16% below); honest residual
  Equinix/Ascenty/Microsoft/Oceaneering/Wabtec sweeps.
PRC equal-budget: CapEx-upgrade SPIC São Simão UG7 from >R$1bn floor to R$1.4bn
  project CapEx (company announcement via Reuters/Brasil Energia).
NEW allied: Portonave TIL >R$500m 100% electric equipment package (Konecranes
  e-RTGs + ZPMC STS + RS/scanners/tractors envelope; nested STS/RTG/fleet rows).
Skipped: RAP-as-CapEx; Huaxin–CSN; Xinhai MoU; Aldesa EUR; Konecranes Arica CapEx
  undisclosed; COP/CLP/PEN; holdovers unsigned; thin balsa/nickel/fission dry.
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


# 1. lithium / us — CapEx-fill Atlas Neves 71% contracted (16% below DFS slice)
# DFS direct CapEx USD 57.56m (atlas_lithium_neves_dfs_57p6m_2025); contracted =
# 0.71 * 57560000 * 0.84 ≈ USD 34,308,864
NEVES_CONTRACTED = str(round(0.71 * 57560000 * 0.84, 2))
row_doc(
    "atlas_lithium_neves_71pct_capex_2026",
    "resources", "lithium", "us",
    "Atlas Lithium — Neves Project 71% direct CapEx contracted",
    "Brazil",
    "9 Sep 2026 Atlas Lithium: approximately 71% of Neves Project direct CapEx (per DFS USD 57.56m) now supported by executed contracts/firm agreements; contracted costs approximately 16% below corresponding DFS budget. CapEx-fill: enter USD ~34.31m contracted face (= 71% × USD 57.56m × 0.84). Distinct from atlas_lithium_neves_dfs_57p6m_2025 full DFS CapEx row.",
    NEVES_CONTRACTED, "2026-09-09", "2026", "-16.85", "-42.07",
    "Neves / Araçuaí Lithium Valley, Minas Gerais (company geography; approximate pin).",
    "inn_atlas_neves_71pct_20260909",
    "Atlas Lithium Corporation (NASDAQ: ATLX) (\"Atlas Lithium\" or the \"Company\") today announced that approximately 71% of the direct capital expenditures (\"CAPEX\") for its 100%-owned Neves Project (\"Project\"), as outlined in the Company's Definitive Feasibility Study (\"DFS\"), are now supported by executed contracts and firm agreements with selected execution partners. In aggregate, these contracted costs are approximately 16% below the corresponding DFS budget.",
    "https://investingnews.com/atlas-lithium-materially-de-risks-neves-project-with-71-of-direct-capital-budget-already-contracted/",
    "Actor: Atlas Lithium (U.S.-listed NASDAQ:ATLX) — us. CapEx-fill: enter ~USD 34.31m contracted face from 71% of DFS × 16% below. Nested within DFS USD 57.56m envelope (not additive to full DFS row). Shuffle lithium / U.S. ≥1/3 budget.",
    "hunt_cycle240", investment_type="epc_contract", evidence="documented", currency="USD",
    value_usd=NEVES_CONTRACTED, fx_usd="1",
    chicago='Atlas Lithium Corporation. “Atlas Lithium Materially De-Risks Neves Project with 71% of Direct Capital Budget Already Contracted.” Investing News Network (Newsfile), September 9, 2026. https://investingnews.com/atlas-lithium-materially-de-risks-neves-project-with-71-of-direct-capital-budget-already-contracted/.',
    annotation="Atlas Neves 71% CapEx-fill ~USD 34.31m contracted. Supports atlas_lithium_neves_71pct_capex_2026.",
    evid_note="Opened INN Newsfile republication; 71% of DFS direct CapEx contracted / 16% below DFS budget confirmed. CapEx-fill = 0.71×57.56m×0.84.",
)

# 2. power_plants_grid / prc — CapEx-upgrade SPIC São Simão UG7 to R$1.4bn
row_doc(
    "spic_sao_simao_ug7_lrcap_2026",
    "energy", "power_plants_grid", "prc",
    "SPIC Brasil — UHE São Simão UG7 expansion via LRCAP (R$1.4bn)",
    "Brazil",
    "10 Sep 2026: SPIC Brasil announces Dongfang Electric + CGGC consortium contract for UG7 Francis turbine/generator supply and on-site assembly; project CapEx R$1.4 billion to add 310 MW (commercial ops targeted 2030); LRCAP award March 2026 had cited >R$1bn floor (prior CapEx-fill). CapEx-upgrade: enter R$1.4bn company-announced project face; Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~269.64m. Complements dongfang_cggc_sao_simao_ug7_2026 equipment-supply row (contract USD blank).",
    "1400000000", BRL_FX_DATE, "2026", "-18.99", "-50.51",
    "UHE São Simão, Minas Gerais / Goiás border (company geography).",
    "brasilenergia_spic_sao_simao_1p4bn_20260910",
    "Companhia investirá R$ 1,4 bilhão para implantar uma nova unidade geradora e ampliar a capacidade instalada da hidrelétrica em 310 MW.",
    "https://brasilenergia.azurewebsites.net/energia/hidrica/spic-brasil-contrata-consorcio-para-a-expansao-da-uhe-sao-simao",
    "Actor: SPIC Brasil (State Power Investment Corp., PRC) — prc. CapEx-upgrade from >R$1bn floor to R$1.4bn project CapEx (company announcement via Brasil Energia / Reuters). Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle240", investment_type="expansion", evidence="documented", currency="BRL",
    value_usd=str(round(1400000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Melloni, Eugenio. “Spic Brasil contrata consórcio para expandir São Simão.” Brasil Energia, September 10, 2026. https://brasilenergia.azurewebsites.net/energia/hidrica/spic-brasil-contrata-consorcio-para-a-expansao-da-uhe-sao-simao.',
    annotation="SPIC São Simão CapEx-upgrade R$1.4bn ~USD 269.64m via Fed H.10. Supports spic_sao_simao_ug7_lrcap_2026.",
    evid_note="Opened Brasil Energia Portuguese; R$1.4bn / 310 MW / Dongfang+CGGC / COD 2030 confirmed (SPIC announcement). CapEx-upgrade USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. port_cranes / allied — NEW Portonave >R$500m 100% electric equipment package
row_doc(
    "portonave_electric_equip_500m_brl_2026",
    "infrastructure", "port_cranes", "allied",
    "Portonave (TIL) — >R$500m 100% electric equipment package (Navegantes)",
    "Brazil",
    "27 Jul 2026 Portonave: completes arrival of 14 Konecranes e-RTGs; package of more than R$500 million in 100% electric equipment also includes two ZPMC STS quay cranes, reach stackers, cargo scanners and terminal tractors. CapEx: enter R$500m floor; Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~96.30m. Envelope containing nested zpmc_portonave_sts_2025 / portonave_ertg_210m_brl_2026 / portonave_electric_fleet_61m_2026 (not additive).",
    "500000000", BRL_FX_DATE, "2026", "-26.89", "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina (company geography).",
    "portonave_ertg_complete_20260727",
    "A frota renovada de pátio integra um pacote de mais de R$ 500 milhões em equipamentos 100% elétricos, que contempla ainda dois guindastes Ship-to-Shore (STS), Reach Stackers e scanners de inspeção de cargas e Terminal Tractors.",
    "https://www.portonave.com.br/pt/todas-as-noticias/portonave-recebe-mais-sete-unidades-e-completa-a-chegada-dos-14-novos-guindastes-eletricos-de-patio",
    "Actor: Portonave under TIL (MSC/Swiss) — allied. NEW envelope row: company Portuguese >R$500m electric equipment package. Nested STS/RTG/fleet CapEx rows are components. Shuffle port_cranes.",
    "hunt_cycle240", investment_type="equipment_package", evidence="documented", currency="BRL",
    value_usd=str(round(500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Portonave. “Portonave recebe mais sete unidades e completa a chegada dos 14 novos guindastes elétricos de pátio.” July 27, 2026. https://www.portonave.com.br/pt/todas-as-noticias/portonave-recebe-mais-sete-unidades-e-completa-a-chegada-dos-14-novos-guindastes-eletricos-de-patio.',
    annotation="Portonave electric package NEW >R$500m ~USD 96.30m via Fed H.10. Supports portonave_electric_equip_500m_brl_2026.",
    evid_note="Opened Portonave Portuguese; >R$500m electric package / 14 Konecranes e-RTGs / ZPMC STS confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle240 added {len(added)}: {added}")
    print(f"cycle240 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
