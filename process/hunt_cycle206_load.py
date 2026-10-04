#!/usr/bin/env python3
"""Cycle 206 hunt: shuffle_seed=20261206; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261206).shuffle):
port_cranes, balsa, solar, other_renewables, fission_smr, wind, nickel,
building_materials, lithium, port_ownership, bridges_roads, niobium,
engineering_epc, water, power_plants_grid, graphite, copper, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES/Freeport/EXIM/DFC/Fluence/Bechtel/Progress
Rail/Wabtec/Albemarle/EnergyX/USTDA/GE Vernova/SSA/Nextracker/Pumpco sweeps
(catalog dense; 0 new U.S. rows). PRC equal-budget: Goldwind Sento Sé/Sungrow
Observatorio/Envision 630/CAMC Bluefields/CRBC Arequipa already logged — miss.
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


# 1. power_plants_grid / allied — Konecranes AXIA Energia hydro crane modernizations
row_doc(
    "konecranes_axia_manso_mascarenhas_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Konecranes — crane modernizations at AXIA Energia Manso + Mascarenhas de Moraes hydros",
    "Brazil",
    "15 Jul 2026 Konecranes: two crane-modernization contracts signed May 2026 with AXIA Energia — five cranes total (electrical/mechanical drives, VFDs, braking, radio remote, cabins). Mascarenhas de Moraes (MG): one gantry 200 t / 25 t (Feb 2027). Manso (MT): two overhead 65/15/5 t + two gantries 20 t and 15 t (end-2027). CapEx USD not disclosed. Distinct from konecranes_portonave_rtg_2025 / konecranes_cartagena_rtg_2025.",
    "",
    "",
    "2026",
    "-14.87",
    "-55.78",
    "UHE Manso, Mato Grosso (primary of two sites; Mascarenhas de Moraes in Minas Gerais also in scope).",
    "konecranes_axia_hydro_20260715",
    "Konecranes has won two crane modernization projects from AXIA Energia… The contracts were signed in May 2026, with the modernization scheduled for 2027… The scope of supply includes the electrical and mechanical modernization of five cranes at the two power plants: two overhead cranes and three gantry cranes.",
    "https://investors.konecranes.com/press/konecranes-modernize-cranes-two-axia-energia-hydropower-plants-brazil-2469123",
    "Actor: Konecranes (Finland) — allied; counterpart AXIA Energia (Brazil renewables/transmission). Company English primary. CapEx blank. Shuffle power_plants_grid.",
    "hunt_cycle206",
    investment_type="equipment_modernization",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Konecranes. “Konecranes to modernize cranes at two AXIA Energia hydropower plants in Brazil.” July 15, 2026. https://investors.konecranes.com/press/konecranes-modernize-cranes-two-axia-energia-hydropower-plants-brazil-2469123.',
    annotation="Konecranes AXIA Manso/Mascarenhas hydro crane mods; CapEx blank. Supports konecranes_axia_manso_mascarenhas_2026.",
    evid_note="Opened Konecranes English company primary 2026-10-04; five-crane May 2026 awards / 2027 schedule confirmed; CapEx undisclosed.",
)

# 2. port_ownership / allied — DEME/FTS Paranaguá access-channel concession CapEx R$1.22bn
row_doc(
    "deme_paranagua_channel_1p22bn_brl_2025",
    "infrastructure",
    "port_ownership",
    "allied",
    "Consórcio Canal Galheta Dragagem (DEME / FTS) — Paranaguá access-channel concession",
    "Brazil",
    "22 Oct 2025 Agência Brasil (ANTAQ/B3 auction): Consórcio Canal Galheta Dragagem (FTS Participações + DEME Concessions / DEME Dredging, Belgium) wins 25-year access-channel concession for Port of Paranaguá — first Brazilian port access-channel lease; outorga R$276 million; obligated CapEx R$1.22 billion in first five years to deepen draft 13.5→15.5 m plus dredging/signaling/bathymetry. Distinct from jan_de_nul_via_navegable_troncal_2026 (Argentina Hidrovía).",
    "1220000000",
    "2025-10-22",
    "2025",
    "-25.516",
    "-48.508",
    "Canal da Galheta / Port of Paranaguá access channel, Paraná (port-authority geography; approximate pin).",
    "agencia_brasil_paranagua_channel_20251022",
    "O vencedor do leilão do Porto de Paranaguá terá que investir R$ 1,22 bilhão nos cinco primeiros anos de concessão, pagando uma outorga fixa anual de R$ 86 milhões ao longo de 25 anos. Uma das obrigações é ampliar a profundidade do canal e garantir que o porto passe dos atuais 13,5 para 15,5 metros de calado.",
    "https://agenciabrasil.ebc.com.br/economia/noticia/2025-10/porto-de-paranagua-e-concedido-ao-consorcio-canal-galheta-dragagem",
    "Actor: DEME (Belgium) with FTS Participações — allied (defeated CHEC Dredging in viva-voz). Agência Brasil Portuguese primary. CapEx face = BRL 1.22bn; Fed H.10 22 Oct 2025 BRL per USD 5.3919 → USD 226,265,324. Shuffle port_ownership.",
    "hunt_cycle206",
    investment_type="concession",
    evidence="documented",
    currency="BRL",
    value_usd="226265324",
    fx_usd="5.3919",
    bib_type="government",
    chicago='Agência Brasil. “Porto de Paranaguá é concedido ao Consórcio Canal Galheta Dragagem.” October 22, 2025. https://agenciabrasil.ebc.com.br/economia/noticia/2025-10/porto-de-paranagua-e-concedido-ao-consorcio-canal-galheta-dragagem.',
    annotation="DEME/FTS Paranaguá channel concession CapEx R$1.22bn / 5yr. Supports deme_paranagua_channel_1p22bn_brl_2025.",
    evid_note="Opened Agência Brasil Portuguese primary 2026-10-04; R$1.22bn / R$276m outorga / 13.5→15.5 m / DEME-FTS vs CHEC confirmed. FX Fed H.10 2025-10-22 BRL per USD 5.3919.",
)

# 3. lithium / allied — Codelco–Rio Tinto Maricunga CEOL amendment (CapEx blank; JV pending)
row_doc(
    "rio_tinto_codelco_maricunga_ceol_2026",
    "resources",
    "lithium",
    "allied",
    "Rio Tinto / Codelco — Salar de Maricunga CEOL amendment enabling JV",
    "Chile",
    "12 Feb 2026 Codelco: Ministry of Mining signs CEOL amendment with Salar de Maricunga SpA expanding area (pre-1979 Codelco + Minera Salar Blanco/LPI holdings), extending exploration/prospecting four years, and setting community contributions. Codelco selected Rio Tinto (May 2025) as strategic partner committing up to USD 900 million; CEOL is a condition precedent — foreign antitrust approvals still pending for JV close (projected 2026). CapEx / FID face not yet disbursed. Distinct from rio_tinto_rincon_expansion_2024 / rio_altoandinos_enami_2025.",
    "",
    "",
    "2026",
    "-26.92",
    "-69.05",
    "Salar de Maricunga, Atacama Region, Chile (company geography; approximate salar pin).",
    "codelco_maricunga_ceol_20260212",
    "It should be remembered that in May 2025 the Corporation selected Rio Tinto as a strategic partner for the lithium project in Maricunga, committing a capital contribution of up to US$900 million to develop this initiative… The modification of this CEOL is one of those conditions; others remain, such as obtaining free competition approvals in some foreign countries, which is projected to be achieved during 2026.",
    "https://www.codelco.com/en/codelco-obtiene-el-ceol-definitivo-para-el-desarrollo-del-litio-en-el",
    "Actor: Rio Tinto (UK/Australia) proposed 49.99% partner with Codelco majority — allied. Codelco English primary. CapEx blank (CEOL enables JV; USD 900m commitment not yet closed FID). Shuffle lithium.",
    "hunt_cycle206",
    investment_type="framework_agreement",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Codelco. “Codelco obtains the definitive CEOL for lithium development in the Maricunga Salt Flat.” February 12, 2026. https://www.codelco.com/en/codelco-obtiene-el-ceol-definitivo-para-el-desarrollo-del-litio-en-el.',
    annotation="Codelco–Rio Tinto Maricunga CEOL amendment; CapEx blank pending JV. Supports rio_tinto_codelco_maricunga_ceol_2026.",
    evid_note="Opened Codelco English primary 2026-10-04; CEOL amendment / Rio USD 900m commitment / JV conditions precedent confirmed; CapEx not disbursed.",
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
    print(f"cycle206 added {len(added)}: {added}")
    print(f"cycle206 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
