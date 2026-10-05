#!/usr/bin/env python3
"""Cycle 261 hunt: shuffle_seed=20261261; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261261).shuffle):
rail, nickel, building_materials, graphite, lithium, engineering_epc, niobium,
port_ownership, other_renewables, power_plants_grid, water, balsa, port_cranes,
wind, fission_smr, copper, solar, bridges_roads.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent residual (Equinix/Ascenty/Cirion/Scala/USTDA/EXIM dense;
  Progress Rail VLI R$430m / Equinix SP USD109m without openable dual primary).
PRC equal-budget: honest residual (CPFL 2T26 already logged C255/C256; BYD BESS ≤R$500m
  without company CapEx primary).
Other: NEW Gerdau 2Q26 Brazil CapEx R$800m (80% of R$1.0bn group); NEW Alupar TAP CapEx
  previsto R$498.52m; NEW Alupar TPC CapEx previsto R$2,597.23m; NEW Alupar TCN CapEx
  previsto R$1,390.64m (company 2T26 ZIP PDF).
Skipped: thin dry; holdovers unsigned; Alupar TECP R$2.0518bn still not company face;
  rail dense after Rumo C260; ISA/CPFL CapEx already logged.
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


# 1. building_materials / other — NEW Gerdau 2Q26 Brazil CapEx R$800m (80% of R$1.0bn)
row_doc(
    "gerdau_2q26_brazil_capex_800m_brl",
    "infrastructure", "building_materials", "other",
    "Gerdau — 2Q26 Brazil CapEx R$800m (80% of R$1.0bn)",
    "Brazil",
    "Gerdau S.A. SEC Form 6-K Exhibit 99.1 Quarterly Results 2Q26: CAPEX totaled R$1.0 billion in 2Q26; in 2Q26, 80% of the CAPEX were allocated to operations in Brazil (Miguel Burnier mining platform / Pindamonhangaba scrap processing cited); remainder includes Midlothian TX (U.S.) expansion — excluded from LatAm face. CapEx: enter Brazil allocation R$800m (=0.80×R$1.0bn). Nested vs gerdau_2026_capex_plan_4p7bn_brl (not additive).",
    "800000000", "2026-06-30", "2026", "-20.02", "-44.05",
    "Gerdau Brazil steel footprint (Ouro Branco / MG industrial pin; Miguel Burnier / Pindamonhangaba cited).",
    "gerdau_2q26_sec_6k_2026",
    "CAPEX totaled R$1.0 billion in 2Q26, and in 6M26 reached 45% of the total planned for the year. Of the amount invested in the quarter, 44% was allocated to Maintenance and 56% to Competitiveness … In 2Q26, 80% of the CAPEX were allocated to operations in Brazil. We continue to make progress toward completing the integrated testing phase of the Miguel Burnier sustainable mining platform … scrap processing project in Pindamonhangaba.",
    "https://www.sec.gov/Archives/edgar/data/1073404/000110465926090494/tm2621830d2_ex99-1.htm",
    "Actor: Gerdau S.A. (Brazilian steel) — other. NEW nested Brazil 80% of 2Q26 CapEx R$1.0bn → R$800m LatAm face. Shuffle building_materials.",
    "hunt_cycle261", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Gerdau S.A. “Form 6-K Exhibit 99.1 — Quarterly Results 2Q26.” 2026. https://www.sec.gov/Archives/edgar/data/1073404/000110465926090494/tm2621830d2_ex99-1.htm.',
    annotation="Gerdau 2Q26 Brazil CapEx R$800m (80% of R$1.0bn) via Fed H.10. Supports gerdau_2q26_brazil_capex_800m_brl.",
    evid_note="Opened Gerdau SEC 6-K 2Q26 Exhibit 99.1; CapEx R$1.0bn with 80% Brazil allocation confirmed. Enter R$800m LatAm face. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / other — NEW Alupar TAP CapEx previsto R$498.52m
row_doc(
    "alupar_tap_capex_previsto_498p52m_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — TAP CapEx previsto R$498.52m",
    "Brazil",
    "6 Aug 2026 Alupar Investimento 2T26 earnings release (company RI ZIP PDF): transmission projects table lists TAP (Brazil; 1 SE) CAPEX Previsto R$498.52 mm / CAPEX Realizado R$226.1 mm; related TECP(TAP) note cites LI for 500 kV Silvânia–Nova Ponte 3–Ribeirão Preto C1/C2 issued 10 Jul 2026. CapEx: enter R$498.52m planned face. Distinct from alupar_lote7_tesp_1089m_brl_2026 / growth-cycle envelope.",
    "498520000", "2026-06-30", "2026", "-16.66", "-48.61",
    "Alupar TAP / TECP corridor Silvânia–Nova Ponte–Ribeirão Preto (Silvânia GO pin).",
    "alupar_2t26_release_20260806",
    "TECP (TAP) | EMISSÃO DA LICENÇA DE INSTALAÇÃO … Linha de Transmissão de 500 kV Silvânia – Nova Ponte 3 – Ribeirão Preto, Circuitos 1 e 2 … PROJETO TAP TPC TCN … País BRA BRA BRA … CAPEX Previsto (MM) R$ 498,52 R$ 2.597,23 R$ 1.390,64 … CAPEX Realizado (MM) R$ 226,1 R$ 305,8 R$ 35,1.",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento — other. NEW TAP CapEx previsto R$498.52m from company 2T26 PDF. Shuffle power_plants_grid.",
    "hunt_cycle261", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(498520000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26.” August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar 2T26 TAP/TPC/TCN CapEx previsto via Fed H.10. Supports alupar_tap_capex_previsto_498p52m_brl; alupar_tpc_capex_previsto_2597p23m_brl; alupar_tcn_capex_previsto_1390p64m_brl.",
    evid_note="Opened Alupar 2T26 RI ZIP PDF; TAP CapEx Previsto R$498.52 mm confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / other — NEW Alupar TPC CapEx previsto R$2,597.23m
row_doc(
    "alupar_tpc_capex_previsto_2597p23m_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — TPC CapEx previsto R$2,597.23m",
    "Brazil",
    "6 Aug 2026 Alupar Investimento 2T26 earnings release: TPC (Brazil; LT 551 km) CAPEX Previsto R$2,597.23 mm / CAPEX Realizado R$305.8 mm; regulator COD 2029 / managerial 2027. CapEx: enter R$2,597.23m planned face. Distinct from Lot 7 TESP / TAP / growth-cycle rows.",
    "2597230000", "2026-06-30", "2026", "", "",
    "Alupar TPC Brazil 551 km transmission project (multi-site LT — lat/lon blank).",
    "alupar_2t26_release_20260806",
    "PROJETO TAP TPC TCN … País BRA BRA BRA … Características 1 SE LT: 551 km LT: 509 km … CAPEX Previsto (MM) R$ 498,52 R$ 2.597,23 R$ 1.390,64 … CAPEX Realizado (MM) R$ 226,1 R$ 305,8 R$ 35,1 … Entrada em Operação (Regulador) 2028 2029 2029.",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento — other. NEW TPC CapEx previsto R$2,597.23m. Shuffle power_plants_grid.",
    "hunt_cycle261", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(2597230000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26.” August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar 2T26 TAP/TPC/TCN CapEx previsto via Fed H.10. Supports alupar_tap_capex_previsto_498p52m_brl; alupar_tpc_capex_previsto_2597p23m_brl; alupar_tcn_capex_previsto_1390p64m_brl.",
    evid_note="Opened Alupar 2T26 RI ZIP PDF; TPC CapEx Previsto R$2,597.23 mm / LT 551 km confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Alupar TCN CapEx previsto R$1,390.64m
row_doc(
    "alupar_tcn_capex_previsto_1390p64m_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — TCN CapEx previsto R$1,390.64m",
    "Brazil",
    "6 Aug 2026 Alupar Investimento 2T26 earnings release: TCN (Brazil; LT 509 km) CAPEX Previsto R$1,390.64 mm / CAPEX Realizado R$35.1 mm; regulator and managerial COD 2029. CapEx: enter R$1,390.64m planned face. Distinct from TAP/TPC/Lot 7 rows.",
    "1390640000", "2026-06-30", "2026", "", "",
    "Alupar TCN Brazil 509 km transmission project (multi-site LT — lat/lon blank).",
    "alupar_2t26_release_20260806",
    "PROJETO TAP TPC TCN … País BRA BRA BRA … Características 1 SE LT: 551 km LT: 509 km … CAPEX Previsto (MM) R$ 498,52 R$ 2.597,23 R$ 1.390,64 … CAPEX Realizado (MM) R$ 226,1 R$ 305,8 R$ 35,1 … Entrada em Operação (Regulador) 2028 2029 2029.",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento — other. NEW TCN CapEx previsto R$1,390.64m. Shuffle power_plants_grid.",
    "hunt_cycle261", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(1390640000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26.” August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar 2T26 TAP/TPC/TCN CapEx previsto via Fed H.10. Supports alupar_tap_capex_previsto_498p52m_brl; alupar_tpc_capex_previsto_2597p23m_brl; alupar_tcn_capex_previsto_1390p64m_brl.",
    evid_note="Opened Alupar 2T26 RI ZIP PDF; TCN CapEx Previsto R$1,390.64 mm / LT 509 km confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    # merge Alupar bib supports from C260 Lot 7
    if "alupar_2t26_release_20260806" in bib_by:
        e = bib[bib_by["alupar_2t26_release_20260806"]]
        e["supports"] = list(dict.fromkeys((e.get("supports") or []) + [
            "alupar_lote7_tesp_1089m_brl_2026",
            "alupar_tap_capex_previsto_498p52m_brl",
            "alupar_tpc_capex_previsto_2597p23m_brl",
            "alupar_tcn_capex_previsto_1390p64m_brl",
            "hunt_cycle260", "hunt_cycle261",
        ]))
        e["annotation"] = (
            "Alupar 2T26 company release (ZIP): Lot 7 TESP R$1,089m; TAP/TPC/TCN CapEx "
            "previsto R$498.52m / R$2,597.23m / R$1,390.64m via Fed H.10."
        )
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle261 added {len(added)}: {added}")
    print(f"cycle261 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
