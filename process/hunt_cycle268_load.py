#!/usr/bin/env python3
"""Cycle 268 hunt: shuffle_seed=20261268; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261268).shuffle):
rail, bridges_roads, solar, port_ownership, power_plants_grid, port_cranes, copper,
engineering_epc, niobium, fission_smr, graphite, balsa, lithium, building_materials,
wind, water, nickel, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW ODATA SP04 Osasco campus >R$2.6bn (company Portuguese).
PRC equal-budget: NEW CPFL Transmissão 2026 CapEx R$856m + 2027 R$1.221bn +
  2026–2030 plan R$4.540bn (Formulário de Referência company PDF).
Other: NEW Portonave R$2bn modernization envelope + R$439m equipment tranche.
Skipped: thin dry; holdovers unsigned; Equinix/Ascenty/Neoenergia/Equatorial/
  Copel/Portonave quay R$1.5bn already nested.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
    status="active",
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": status,
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


# 1. engineering_epc / us — NEW ODATA SP04 >R$2.6bn campus
row_doc(
    "odata_sp04_2p6bn_brl_2025",
    "infrastructure", "engineering_epc", "us",
    "ODATA (Aligned Data Centers) — DC SP04 Osasco campus CapEx >R$2.6bn",
    "Brazil",
    "17 Mar 2025 ODATA company Portuguese: announces DC SP04 in Osasco, Greater São Paulo — investment of more than R$ 2.6 billion when completed; 48 MW IT capacity; first Brazil deployment of Aligned Delta³ cooling; operations targeted Apr 2025. CapEx: enter R$2.6bn soft floor. Distinct from odata_deltaflow_630m_2026 (SP04+QR03 liquid-cooling first-phase USD 630m) and Colombia BG02/BG03 rows.",
    "2600000000", "2025-03-17", "2025", "-23.53", "-46.79",
    "ODATA DC SP04, Osasco, Greater São Paulo (company geography).",
    "odata_sp04_announce_20250317",
    "Com um investimento de mais de R$2,6 bilhões quando concluído, o campus tem capacidade de TI de 48MW",
    "https://odatadc.com/imprensa/odata-anuncia-novo-data-center-em-sao-paulo/",
    "Actor: ODATA / Aligned Data Centers (U.S. parent) — us. NEW SP04 campus CapEx >R$2.6bn. Shuffle engineering_epc; ≥1/3 U.S. hunt. Holdover company CapEx primary resolved.",
    "hunt_cycle268", investment_type="greenfield_plant", evidence="documented", currency="BRL",
    value_usd=str(round(2600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ODATA. “ODATA anuncia novo data center em São Paulo.” March 17, 2025. https://odatadc.com/imprensa/odata-anuncia-novo-data-center-em-sao-paulo/.',
    annotation="ODATA SP04 >R$2.6bn via Fed H.10. Supports odata_sp04_2p6bn_brl_2025.",
    evid_note="Opened ODATA company Portuguese; SP04 >R$2.6bn / 48 MW Osasco confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. port_ownership / other — NEW Portonave R$2bn modernization envelope
row_doc(
    "portonave_2bn_program_brl_2025",
    "infrastructure", "port_ownership", "other",
    "Portonave — quay + equipment modernization package R$2bn",
    "Brazil",
    "28 Nov 2025 Portonave company: quay modernization phase-2 (~R$1.5bn) plus ~R$439m new handling/inspection equipment together total an investment of R$ 2 billion; capacity 1.5→2.0m TEU by end-2026; Navegantes, SC. CapEx: enter R$2bn combined program face. Envelope containing nested portonave_cais_1p5bn_brl_2026 quay tranche and equipment R$439m (not additive).",
    "2000000000", "2025-11-28", "2025", "-26.89", "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina (company geography).",
    "portonave_cais_2bn_program_2026",
    "Juntos, totalizam um investimento de R$ 2 bilhões.",
    "https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes",
    "Actor: Portonave S.A. — other. NEW combined R$2bn program envelope. Shuffle port_ownership.",
    "hunt_cycle268", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(2000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Portonave. “Investimentos da Portonave na modernização do cais e em novos equipamentos chegam a R$ 2 bilhões.” November 28, 2025. https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes.',
    annotation="Portonave R$2bn program + R$439m equipment via Fed H.10. Supports portonave_2bn_program_brl_2025; portonave_equip_439m_brl_2025.",
    evid_note="Opened Portonave company Portuguese; combined R$2bn modernization package confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. port_cranes / other — NEW Portonave R$439m equipment tranche
row_doc(
    "portonave_equip_439m_brl_2025",
    "infrastructure", "port_cranes", "other",
    "Portonave — new container handling/inspection equipment CapEx R$439m",
    "Brazil",
    "28 Nov 2025 Portonave company: alongside ~R$1.5bn quay works, R$ 439 million in new equipment for container handling and inspection — two STS, 14 RTG, reach stacker, two scanners (all 100% electric cited). CapEx: enter R$439m equipment tranche face. Nested within portonave_2bn_program_brl_2025; distinct from portonave_ertg_210m / electric_fleet_61m / >R$500m electric package rows (overlapping equipment generations — treat as program tranche, not additive to those).",
    "439000000", "2025-11-28", "2025", "-26.89", "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina (company geography).",
    "portonave_cais_2bn_program_2026",
    "com investimentos que totalizam aproximadamente R$ 1,5 bilhão e R$ 439 milhões em novos equipamentos para movimentação e inspeção de contêineres.",
    "https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes",
    "Actor: Portonave S.A. — other. NEW equipment CapEx tranche R$439m. Shuffle port_cranes.",
    "hunt_cycle268", investment_type="equipment_supply", evidence="documented", currency="BRL",
    value_usd=str(round(439000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Portonave. “Investimentos da Portonave na modernização do cais e em novos equipamentos chegam a R$ 2 bilhões.” November 28, 2025. https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes.',
    annotation="Portonave R$2bn program + R$439m equipment via Fed H.10. Supports portonave_2bn_program_brl_2025; portonave_equip_439m_brl_2025.",
    evid_note="Opened Portonave company Portuguese; R$439m equipment tranche confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / prc — NEW CPFL Transmissão 2026 CapEx R$856m
row_doc(
    "cpfl_tx_2026_capex_856m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — 2026 CapEx plan R$856m",
    "Brazil",
    "28 May 2026 CPFL Transmissão Formulário de Referência (company RI PDF): planned capital investments approximately R$ 856 million in 2026 (and R$ 1.221 billion in 2027); table shows CPFL-T projected CapEx 2026=856. CapEx: enter R$856m 2026 face. Nested vs cpfl_capex_plan_31p1bn_2026_2030 group plan and cpfl_tx_lote3_1p1bn row (not additive).",
    "856000000", "2026-05-28", "2026", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_tx_fr_2026_20260528",
    "Planejamos investir R$ 4.540 milhões em nossas atividades durante o período de 2026 a 2030. Pretendemos realizar investimentos no valor total de R$ 856 milhões em 2026, R$ 1.221 milhões em 2027",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D",
    "Actor: CPFL Transmissão (State Grid–controlled CPFL Energia) — prc. NEW 2026 TX CapEx plan R$856m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle268", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(856000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Transmissão. “Formulário de Referência 2026” (FR_CPFL Transmissão 2026). May 28, 2026. https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D.',
    annotation="CPFL Transmissão 2026 R$856m / 2027 R$1.221bn / 2026–2030 R$4.540bn via Fed H.10. Supports cpfl_tx_2026_capex_856m_brl; cpfl_tx_2027_capex_1221m_brl; cpfl_tx_2026_2030_4540m_brl.",
    evid_note="Opened CPFL Transmissão Formulário de Referência 2026 PDF; 2026 CapEx R$856m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / prc — NEW CPFL Transmissão 2027 CapEx R$1.221bn
row_doc(
    "cpfl_tx_2027_capex_1221m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — 2027 CapEx plan R$1.221bn",
    "Brazil",
    "28 May 2026 CPFL Transmissão Formulário de Referência: planned investments R$ 1.221 billion in 2027 (table CPFL-T 2027*=1.221). CapEx: enter R$1.221bn 2027 face. Nested within 2026–2030 R$4.540bn TX plan (not additive to 2026 R$856m).",
    "1221000000", "2026-05-28", "2027", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_tx_fr_2026_20260528",
    "Pretendemos realizar investimentos no valor total de R$ 856 milhões em 2026, R$ 1.221 milhões em 2027, R$ 1.059 milhões em 2028, R$ 799 milhões em 2029 e R$ 605 milhões em 2030.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW nested 2027 TX CapEx plan R$1.221bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle268", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(1221000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Transmissão. “Formulário de Referência 2026” (FR_CPFL Transmissão 2026). May 28, 2026. https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D.',
    annotation="CPFL Transmissão 2026 R$856m / 2027 R$1.221bn / 2026–2030 R$4.540bn via Fed H.10. Supports cpfl_tx_2026_capex_856m_brl; cpfl_tx_2027_capex_1221m_brl; cpfl_tx_2026_2030_4540m_brl.",
    evid_note="Opened CPFL Transmissão FR 2026 PDF; 2027 CapEx R$1.221bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. power_plants_grid / prc — NEW CPFL Transmissão 2026–2030 plan R$4.540bn
row_doc(
    "cpfl_tx_2026_2030_4540m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — 2026–2030 CapEx plan R$4.540bn",
    "Brazil",
    "28 May 2026 CPFL Transmissão Formulário de Referência: plans to invest R$ 4.540 billion in transmission activities over 2026–2030 (856+1,221+1,059+799+605). CapEx: enter R$4.540bn multi-year face. Distinct from group cpfl_capex_plan_31p1bn_2026_2030 (R$4.5bn transmission cited at group level — this is CPFL-T subsidiary face from FR).",
    "4540000000", "2026-05-28", "2026", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_tx_fr_2026_20260528",
    "Planejamos investir R$ 4.540 milhões em nossas atividades durante o período de 2026 a 2030.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW 2026–2030 TX CapEx plan R$4.540bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle268", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(4540000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Transmissão. “Formulário de Referência 2026” (FR_CPFL Transmissão 2026). May 28, 2026. https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D.',
    annotation="CPFL Transmissão 2026 R$856m / 2027 R$1.221bn / 2026–2030 R$4.540bn via Fed H.10. Supports cpfl_tx_2026_capex_856m_brl; cpfl_tx_2027_capex_1221m_brl; cpfl_tx_2026_2030_4540m_brl.",
    evid_note="Opened CPFL Transmissão FR 2026 PDF; 2026–2030 CapEx plan R$4.540bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)


def upsert_bib(bib, bib_by, bib_e):
    sid = bib_e["id"]
    entry = {
        "id": sid,
        "type": bib_e.get("type", "company"),
        "chicago": bib_e["chicago"],
        "url": bib_e["url"],
        "annotation": bib_e.get("annotation", ""),
        "supports": bib_e.get("supports", []),
    }
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        old = existing.get("supports") or []
        new = entry["supports"] or []
        merged = list(dict.fromkeys(list(old) + list(new)))
        existing.update({k: v for k, v in entry.items() if k != "supports"})
        existing["supports"] = merged
    else:
        bib.append(entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("entries") or bib.get("sources") or []
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
    print(f"cycle268 added {len(added)}: {added}")
    print(f"cycle268 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
