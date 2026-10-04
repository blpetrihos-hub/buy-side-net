#!/usr/bin/env python3
"""Cycle 210 hunt: shuffle_seed=20261210; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261210).shuffle):
fission_smr, port_ownership, engineering_epc, solar, copper, balsa, water,
port_cranes, power_plants_grid, building_materials, niobium, rail, graphite,
bridges_roads, lithium, wind, nickel, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Black Giant LOI/DFC Serra/
EnergyX/Nextracker/Array Lupi/Wabtec MRS/GE Vernova São Simão/Bechtel Chile/
Fluence/USTDA/Equinix/Freeport El Abra sweeps (0 new U.S. rows — catalog dense;
GE Vernova São Simão R$1.2bn / EnergyX CapEx / Array Lupi already logged).
PRC equal-budget: PowerChina Chile Decree 4 / Dune Plus / Palmira III /
Francisco Juana / State Grid NE UHV already logged (CapEx blank or prior);
holdovers unsigned.
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


# 1. lithium / allied — CleanTech Lithium Laguna Verde PFS CapEx USD 748m (Chile)
row_doc(
    "cleantech_laguna_verde_pfs_748m_2026",
    "resources",
    "lithium",
    "allied",
    "CleanTech Lithium PLC — Laguna Verde DLE project Pre-Feasibility Study CapEx (Atacama)",
    "Chile",
    "31 Mar 2026 CleanTech Lithium RNS: Laguna Verde PFS (Worley-led) Capex including 20.6% contingency = USD 748 million for 15,000 tpa battery-grade lithium carbonate over 25-year operating life; pre-tax NPV8 USD 1.37bn / IRR 24.2%; CEOL terms agreed Mar 2026 pending final ratification. Distinct from EnergyX Black Giant and Rio Tinto Rincón lithium rows.",
    "748000000",
    "2026-03-31",
    "2026",
    "-26.9",
    "-68.6",
    "Laguna Verde hypersaline system, Atacama Region, Chile (company geography; approximate pin).",
    "cleantech_laguna_verde_pfs_20260331",
    "Capex (including contingency of 20.6%) US$748 million … Pre-Tax NPV8 US$1.37bn and IRR of 24.2% … The PFS demonstrates production of 15,000 tonnes per annum (“tpa”) of battery grade lithium carbonate for an operating life of 25 years",
    "https://wp-ctlithium-rebuild-2022.s3.eu-west-2.amazonaws.com/media/2026/03/CTL-RNS-PFS-Completed-for-Laguna-Verde_Final-R5-300325.pdf",
    "Actor: CleanTech Lithium PLC (UK AIM-listed) — allied. Opened company RNS PDF 31 Mar 2026. CapEx face = USD 748m including contingency. Shuffle lithium.",
    "hunt_cycle210",
    investment_type="greenfield_mine",
    evidence="documented",
    currency="USD",
    value_usd="748000000",
    fx_usd="1",
    bib_type="company",
    chicago='CleanTech Lithium PLC. “Pre-Feasibility Study Completed for Laguna Verde.” RNS, March 31, 2026. https://wp-ctlithium-rebuild-2022.s3.eu-west-2.amazonaws.com/media/2026/03/CTL-RNS-PFS-Completed-for-Laguna-Verde_Final-R5-300325.pdf.',
    annotation="CleanTech Laguna Verde PFS CapEx USD 748m. Supports cleantech_laguna_verde_pfs_748m_2026.",
    evid_note="Opened CleanTech RNS PDF 2026-10-04; Capex US$748m incl. 20.6% contingency / 15,000 tpa / NPV8 US$1.37bn / IRR 24.2% confirmed.",
)

# 2. port_ownership / allied — CapEx fill: DP World Posorja expansion USD 190m
row_doc(
    "dpworld_posorja_expansion_2025",
    "infrastructure",
    "port_ownership",
    "allied",
    "DP World — Posorja deepwater terminal berth expansion (Guayas, Ecuador)",
    "Ecuador",
    "23 Apr 2026 DP World: inaugurates Posorja terminal expansion as part of a USD 190 million private investment; quay extended to 700 m (adding 232.5 m) enabling dual post-Panamax operations; berth to reach 800 m by end-2026 with capacity to 1.4 million TEU/year; two fully electric Super Post-Panamax quay cranes (68 m outreach) delivered Sep 2025 now operational. CapEx face filled/upgraded to USD 190m from prior USD 140m figure. Distinct from dpworld_callao and dpworld_caucedo rows.",
    "190000000",
    "2026-04-23",
    "2026",
    "-2.7",
    "-80.25",
    "DP World Posorja terminal, Guayas Province, Ecuador (company geography; approximate pin).",
    "dpworld_posorja_inauguration_20260423",
    "DP World has inaugurated a major expansion at its Posorja terminal, part of a USD $190 million private investment that strengthens Ecuador’s trade infrastructure … The project extends the terminal’s quay to 700 meters (an addition of 232.5 meters) enabling the simultaneous handling of two post-Panamax vessels at full capacity. By the end of 2026, the berth will reach 800 meters in length, increasing annual throughput capacity to 1.4 million twenty-foot equivalent units (TEUs).",
    "https://www.dpworld.com/en/news/dp-world-inaugurates-posorja-terminal-expansion-boosting-ecuadors-global-trade-capacity",
    "Actor: DP World (UAE/Dubai) — allied. CapEx-fill upgrade: company English primary 23 Apr 2026 cites USD 190m private investment (was USD 140m on prior row). Shuffle port_ownership.",
    "hunt_cycle210",
    investment_type="expansion",
    evidence="documented",
    currency="USD",
    value_usd="190000000",
    fx_usd="1",
    bib_type="company",
    chicago='DP World. “DP World Inaugurates Posorja Terminal Expansion, Boosting Ecuador’s Global Trade Capacity.” April 23, 2026. https://www.dpworld.com/en/news/dp-world-inaugurates-posorja-terminal-expansion-boosting-ecuadors-global-trade-capacity.',
    annotation="DP World Posorja CapEx fill USD 190m. Supports dpworld_posorja_expansion_2025.",
    evid_note="Opened DP World English primary 2026-10-04; USD 190m / 700 m quay (+232.5 m) / 1.4m TEU / dual post-Panamax / electric Super Post-Panamax cranes confirmed. CapEx-fill upgrade from prior USD 140m.",
)

# 3. port_ownership / other — Portonave quay modernization ~R$1.5bn (Navegantes)
row_doc(
    "portonave_cais_1p5bn_brl_2026",
    "infrastructure",
    "port_ownership",
    "other",
    "Portonave S.A. — Quay infrastructure modernization (Navegantes / Itajaí complex)",
    "Brazil",
    "Portonave company: quay modernization investments total approximately R$1.5 billion (plus R$439 million in new handling/inspection equipment; combined works+equipment program cited as reaching ~R$2 billion). Quay deepened to 17 m to receive vessels up to 400 m; Adequação do Cais begun Jan 2024 with completion targeted H2 2026. CapEx face = R$1.5bn quay works (equipment subsets logged separately as ZPMC STS / Konecranes e-RTG / Kalmar / electric fleet). Distinct from portonave_ertg_210m_brl_2026 and zpmc_portonave_sts_2025.",
    "1500000000",
    "",
    "2026",
    "-26.89",
    "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina (company geography).",
    "portonave_cais_2bn_program_2026",
    "Para manter a competitividade e a excelência na movimentação de contêineres … a Portonave realiza a … etapa da obra de adequação do cais, com investimentos que totalizam aproximadamente R$ 1,5 bilhão e R$ 439 milhões em novos equipamentos para movimentação e inspeção de contêineres. Com o cais mais robusto, com profundidade de 17 metros, navios de até 400 metros de comprimento poderão ser recebidos",
    "https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes",
    "Actor: Portonave S.A. (Brazilian private terminal) — other. Company Portuguese primary. CapEx face = R$1.5bn quay modernization (not full ~R$2bn works+equipment aggregate). USD blank (Fed H.10 unreachable). Shuffle port_ownership.",
    "hunt_cycle210",
    investment_type="expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Portonave. “Investimentos da Portonave na modernização do cais e em novos equipamentos chegam a R$ 2 bilhões.” https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes.',
    annotation="Portonave quay modernization R$1.5bn. Supports portonave_cais_1p5bn_brl_2026.",
    evid_note="Opened Portonave Portuguese primary 2026-10-04; R$1.5bn quay / R$439m equipment / 17 m depth / 400 m vessels / H2 2026 completion target confirmed.",
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
    print(f"cycle210 added {len(added)}: {added}")
    print(f"cycle210 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
