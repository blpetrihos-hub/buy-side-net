#!/usr/bin/env python3
"""Cycle 286 hunt: shuffle_seed=20261286; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261286).shuffle):
water, port_ownership, other_renewables, balsa, rail, lithium, port_cranes, niobium,
copper, building_materials, fission_smr, graphite, power_plants_grid, solar, nickel,
engineering_epc, bridges_roads, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Brasil 2024E Cajuína / Tucano Expansion nested faces +
  Capitalized Interest 2024E/2025E/2026E from Material Fact; Arenales CapEx blank;
  Equinix/Ascenty CapEx blanks; EXIM/USTDA probes.
PRC equal-budget: CPFL 2T26 news reopened (R$1.5bn/R$2.8bn already nested; debentures
  R$2bn financing not CapEx); Goldwind Jacobina 05 CNY guarantee ≠ CapEx; State Grid /
  Sungrow / BYD company pages 403/dense — miss this cycle after equal-budget probes.
Other: NEW Motiva 2026 highways CapEx plan R$7.2bn (company primary; distinct from
  OE proxy R$7.167bn municipal breakout).
Skipped: thin dry; water/port_ownership/other_renewables/lithium/etc. dense; Motiva
  FY2025 airports R$780m taxonomy-out; holdovers unsigned.
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


# 1. power_plants_grid / us — NEW AES Brasil 2024E Cajuína Wind Complex R$373.8m
row_doc(
    "aes_brasil_2024e_cajuina_373p8m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Cajuína Wind Complex CapEx R$373.8m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2024E Cajuína Wind Complex R$373.8 million within Expansion R$388.2m / Total Investments R$712.7m. CapEx: enter R$373.8m Cajuína face. Nested vs aes_brasil_2024e_expansion_388p2m_brl / Total 2024E (not additive).",
    "373800000", "2024-02-26", "2024", "-5.20", "-35.55",
    "Cajuína Wind Complex / Rio Grande do Norte (AES Brasil geography; approximate RN pin).",
    "aes_brasil_mf_capex_20240226",
    "Cajuína Wind Complex 373.8 0.0 0.0 0.0 0.0 373.8",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil (AES Corp U.S.–controlled) — us. NEW nested 2024E Cajuína CapEx R$373.8m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle286", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(373800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E Cajuína CapEx R$373.8m via Fed H.10. Supports aes_brasil_2024e_cajuina_373p8m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Cajuína Wind Complex R$373.8m confirmed.",
)

# 2. power_plants_grid / us — NEW AES Brasil 2024E Tucano Wind Complex R$14.4m
row_doc(
    "aes_brasil_2024e_tucano_14p4m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Tucano Wind Complex CapEx R$14.4m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2024E Tucano Wind Complex R$14.4 million within Expansion R$388.2m. CapEx: enter R$14.4m Tucano face. Nested vs aes_brasil_2024e_expansion_388p2m_brl / Cajuína R$373.8m (not additive).",
    "14400000", "2024-02-26", "2024", "-10.50", "-38.50",
    "Tucano Wind Complex / Bahia (AES Brasil geography; approximate Tucano pin).",
    "aes_brasil_mf_capex_20240226",
    "Tucano Wind Complex 14.4 0.0 0.0 0.0 0.0 14.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW nested 2024E Tucano CapEx R$14.4m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle286", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(14400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E Tucano CapEx R$14.4m via Fed H.10. Supports aes_brasil_2024e_tucano_14p4m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Tucano Wind Complex R$14.4m confirmed.",
)

# 3. power_plants_grid / us — NEW AES Brasil 2024E Capitalized Interest and Labor R$93.8m
row_doc(
    "aes_brasil_2024e_cap_interest_93p8m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Capitalized Interest and Labor R$93.8m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Capitalized Interest and Labor (footnote 2 — debt capitalization interest on projects under construction) 2024E R$93.8 million (separate from Total Investments R$712.7m). CapEx: enter R$93.8m capitalized-interest face. Distinct from Total Investments year faces (not additive).",
    "93800000", "2024-02-26", "2024", "-23.55", "-46.63",
    "AES Brasil generation portfolio under construction (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Capitalized Interest and Labor² 93.8 101.1 49.9 2.9 3.5 251.2",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW 2024E Capitalized Interest and Labor R$93.8m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle286", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(93800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E Capitalized Interest R$93.8m via Fed H.10. Supports aes_brasil_2024e_cap_interest_93p8m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Capitalized Interest and Labor R$93.8m confirmed.",
)

# 4. power_plants_grid / us — NEW AES Brasil 2025E Capitalized Interest R$101.1m
row_doc(
    "aes_brasil_2025e_cap_interest_101p1m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2025E Capitalized Interest and Labor R$101.1m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Capitalized Interest and Labor 2025E R$101.1 million (separate from Total Investments R$214.2m). CapEx: enter R$101.1m face. Distinct from Total Investments / 2024E capitalized-interest faces (not additive).",
    "101100000", "2024-02-26", "2025", "-23.55", "-46.63",
    "AES Brasil generation portfolio under construction (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Capitalized Interest and Labor² 93.8 101.1 49.9 2.9 3.5 251.2",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW 2025E Capitalized Interest and Labor R$101.1m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle286", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(101100000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2025E Capitalized Interest R$101.1m via Fed H.10. Supports aes_brasil_2025e_cap_interest_101p1m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2025E Capitalized Interest and Labor R$101.1m confirmed.",
)

# 5. power_plants_grid / us — NEW AES Brasil 2026E Capitalized Interest R$49.9m
row_doc(
    "aes_brasil_2026e_cap_interest_49p9m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2026E Capitalized Interest and Labor R$49.9m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Capitalized Interest and Labor 2026E R$49.9 million (separate from Total Investments R$136.7m). CapEx: enter R$49.9m face. Distinct from Total Investments / prior capitalized-interest faces (not additive).",
    "49900000", "2024-02-26", "2026", "-23.55", "-46.63",
    "AES Brasil generation portfolio under construction (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Capitalized Interest and Labor² 93.8 101.1 49.9 2.9 3.5 251.2",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW 2026E Capitalized Interest and Labor R$49.9m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle286", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(49900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2026E Capitalized Interest R$49.9m via Fed H.10. Supports aes_brasil_2026e_cap_interest_49p9m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2026E Capitalized Interest and Labor R$49.9m confirmed.",
)

# 6. bridges_roads / other — NEW Motiva 2026 highways CapEx plan R$7.2bn (company primary)
row_doc(
    "motiva_2026_highways_plan_72bn_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 2026 highways CapEx plan R$7.2bn (company primary)",
    "Brazil",
    "Motiva company FY2025 results news: for 2026 forecasts investing R$ 8.3 billion excluding Airports, of which R$ 7.2 billion in highways (Rodovias). CapEx: enter R$7.2bn highways plan face. Distinct from motiva_2026_highways_plan_7167m_brl (prior OE proxy with municipal breakout totaling R$7.167bn) and motiva_2026_capex_plan_8p3bn_brl total envelope (not additive).",
    "7200000000", "2026-02-10", "2026", "-23.55", "-46.63",
    "Motiva Brazil highway portfolio (São Paulo HQ pin).",
    "motiva_fy2025_results_8p3bn_2026",
    "investir R$ 8,3 bilhões – já sem contabilizar a plataforma de Aeroportos – , sendo R$ 7, 2 bilhões em R odovias",
    "https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/",
    "Actor: Motiva S.A. — other. NEW company-primary 2026 highways CapEx plan R$7.2bn. Shuffle bridges_roads.",
    "hunt_cycle286", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(7200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva encerra 2025 com lucro líquido de R$ 3,27 bilhões….” 2026. https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/.',
    annotation="Motiva 2026 highways CapEx plan R$7.2bn via Fed H.10. Supports motiva_2026_highways_plan_72bn_brl.",
    evid_note="Opened Motiva FY2025 company news; 2026 highways CapEx plan R$7.2bn confirmed.",
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
    print(f"cycle286 added {len(added)}: {added}")
    print(f"cycle286 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
