#!/usr/bin/env python3
"""Cycle 287 hunt: shuffle_seed=20261287; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261287).shuffle):
nickel, solar, port_ownership, copper, power_plants_grid, graphite, rail,
building_materials, other_renewables, fission_smr, engineering_epc, wind, lithium,
niobium, balsa, port_cranes, water, bridges_roads.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (nickel first in shuffle; thin top-up still dry).
≥1/3 U.S. hunt budget: NEW AES Brasil Capitalized Interest 2027E R$2.9m + 2028E
  R$3.5m (Material Fact residual faces); Equinix/Ascenty CapEx blanks; EXIM probes.
PRC equal-budget: NEW CPFL CEEE-T acquisition R$2.67bn (Jul 2021) + post-acquisition
  improvements CapEx ~R$1.6bn (Jornal do Comércio UNVERIFIED press quoting company);
  SGBH RS 2025 reopened (R$516m supplier opex / social R$3.9m not CapEx).
Skipped: thin dry; nickel/solar/graphite/etc. dense; Motiva airports taxonomy-out;
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


# 1. power_plants_grid / us — NEW AES Brasil 2027E Capitalized Interest R$2.9m
row_doc(
    "aes_brasil_2027e_cap_interest_2p9m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2027E Capitalized Interest and Labor R$2.9m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Capitalized Interest and Labor 2027E R$2.9 million (separate from Total Investments R$125.5m). CapEx: enter R$2.9m face. Distinct from Total Investments / prior capitalized-interest faces (not additive).",
    "2900000", "2024-02-26", "2027", "-23.55", "-46.63",
    "AES Brasil generation portfolio under construction (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Capitalized Interest and Labor² 93.8 101.1 49.9 2.9 3.5 251.2",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW 2027E Capitalized Interest and Labor R$2.9m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle287", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2027E Capitalized Interest R$2.9m via Fed H.10. Supports aes_brasil_2027e_cap_interest_2p9m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2027E Capitalized Interest and Labor R$2.9m confirmed.",
)

# 2. power_plants_grid / us — NEW AES Brasil 2028E Capitalized Interest R$3.5m
row_doc(
    "aes_brasil_2028e_cap_interest_3p5m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2028E Capitalized Interest and Labor R$3.5m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Capitalized Interest and Labor 2028E R$3.5 million (separate from Total Investments R$159.5m). CapEx: enter R$3.5m face. Distinct from Total Investments / prior capitalized-interest faces (not additive).",
    "3500000", "2024-02-26", "2028", "-23.55", "-46.63",
    "AES Brasil generation portfolio under construction (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Capitalized Interest and Labor² 93.8 101.1 49.9 2.9 3.5 251.2",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW 2028E Capitalized Interest and Labor R$3.5m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle287", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2028E Capitalized Interest R$3.5m via Fed H.10. Supports aes_brasil_2028e_cap_interest_3p5m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2028E Capitalized Interest and Labor R$3.5m confirmed.",
)

# 3. power_plants_grid / prc — NEW CPFL CEEE-T acquisition R$2.67bn
row_doc(
    "cpfl_ceee_t_acquisition_267bn_brl_2021",
    "energy", "power_plants_grid", "prc",
    "CPFL — CEEE-T transmission privatization acquisition R$2.67bn",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio: CPFL arrematou a área de transmissão da antiga CEEE-T por R$ 2,67 bilhões in July 2021 (privatization). CapEx/M&A: enter R$2.67bn acquisition face. Distinct from cpfl_tx_rs_3p9bn_2025_2029 forward cycle and post-acquisition improvements ~R$1.6bn. UNVERIFIED press proxy quoting company.",
    "2670000000", "2021-07-01", "2021", "-30.03", "-51.23",
    "Former CEEE-T Rio Grande do Sul transmission system (Porto Alegre / Canoas pin).",
    "jornal_comercio_cpfl_tx_rs_20250424",
    "Desde a privatização da área de transmissão da antiga CEEE-T, que foi arrematada por R$ 2,67 bilhões pela CPFL em julho de 2021",
    "https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html",
    "Actor: CPFL (State Grid–controlled) — prc. NEW CEEE-T acquisition R$2.67bn (UNVERIFIED press). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle287", investment_type="mna_acquisition", evidence="proxy", currency="BRL",
    value_usd=str(round(2670000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html.',
    annotation="CPFL CEEE-T acquisition R$2.67bn via Fed H.10 (UNVERIFIED press). Supports cpfl_ceee_t_acquisition_267bn_brl_2021.",
    evid_note="Opened Jornal do Comércio 24 Apr 2025; CEEE-T acquisition R$2.67bn Jul 2021 confirmed.",
)

# 4. power_plants_grid / prc — NEW CPFL CEEE-T post-acquisition improvements ~R$1.6bn
row_doc(
    "cpfl_ceee_t_improvements_16bn_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — CEEE-T post-acquisition improvements CapEx ~R$1.6bn",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio: since CEEE-T privatization acquisition, CPFL already invested around R$ 1.6 billion in improvements of the acquired assets (through Apr 2025 coverage date), before the 2025–2029 ~R$3.9bn cycle. CapEx: enter R$1.6bn cumulative improvements face. Nested vs acquisition R$2.67bn / forward RS cycle R$3.9bn (not additive). UNVERIFIED press proxy quoting company.",
    "1600000000", "2025-04-24", "2025", "-30.03", "-51.23",
    "Former CEEE-T Rio Grande do Sul transmission assets (Porto Alegre / Canoas pin).",
    "jornal_comercio_cpfl_tx_rs_20250424",
    "o grupo privado já investiu em torno de R$ 1,6 bilhão em melhorias dos ativos adquiridos",
    "https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW ~R$1.6bn post-acquisition improvements (UNVERIFIED press). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle287", investment_type="brownfield_expansion", evidence="proxy", currency="BRL",
    value_usd=str(round(1600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html.',
    annotation="CPFL CEEE-T improvements ~R$1.6bn via Fed H.10 (UNVERIFIED press). Supports cpfl_ceee_t_improvements_16bn_brl.",
    evid_note="Opened Jornal do Comércio 24 Apr 2025; post-acquisition improvements ~R$1.6bn confirmed.",
)


def upsert_bib(bib, bib_by, entry):
    sid = entry["id"]
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
    print(f"cycle287 added {len(added)}: {added}")
    print(f"cycle287 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
