#!/usr/bin/env python3
"""Cycle 255 hunt: shuffle_seed=20261255; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261255).shuffle):
balsa, fission_smr, lithium, other_renewables, niobium, bridges_roads, rail,
engineering_epc, port_ownership, graphite, port_cranes, water, building_materials,
copper, wind, solar, power_plants_grid, nickel.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent (Wabtec Contagem R$20m/R$150m already logged; Progress Rail
  VLI R$430m holdover vs R$200m conflict; EXIM Argentina 7bn already logged; DFC V.tal
  archived telecom scope) — honest residual.
PRC equal-budget: honest residual (CPFL 2T26 nested C254; CRRC/TIC/State Grid dense).
Other: NEW TAESA 6M26 CapEx R$445.3m; NEW Eneva 2T26 CapEx R$1.59bn.
Allied: ISA ~R$4.6bn remaining CapEx only on investidor10 mirror — skip without company PDF.
Skipped: thin dry; holdovers unsigned; catalog dense elsewhere.
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


# 1. power_plants_grid / other — NEW TAESA 6M26 CapEx R$445.3m
row_doc(
    "taesa_6m26_capex_445p3m_brl",
    "energy", "power_plants_grid", "other",
    "TAESA — 6M26 CapEx R$445.3m",
    "Brazil",
    "11 Aug 2026 TAESA 2T26 earnings release (company RI PDF): in 6M26 the Company, subsidiaries, joint ventures and associates invested total R$ 445.3 MM vs R$ 747.8 MM in 6M25 (−40.5%) on projects under construction (Tangará/Saíra partial energizations; Ananaí/Juruá/ATE reinforcements). CapEx: enter R$445.3m 6M26 face. Nested vs taesa_greenfield_4p3bn_brl_aneel / taesa_fy2025_capex_1p783bn_brl envelopes (not additive).",
    "445300000", "2026-06-30", "2026", "-22.91", "-43.17",
    "TAESA Brazil transmission footprint (Rio de Janeiro HQ pin).",
    "taesa_2t26_release_20260811",
    "No 6M26, a Companhia, suas controladas, investidas em conjunto e coligadas investiram o total de R$ 445,3 MM contra R$ 747,8 MM investidos no 6M25, referentes aos empreendimentos em implantação.",
    "https://ri.taesa.com.br/wp-content/uploads/2018/11/TAESA_Release-2T26.pdf",
    "Actor: TAESA (Brazilian transmission) — other. NEW nested 6M26 CapEx R$445.3m. Shuffle power_plants_grid.",
    "hunt_cycle255", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(445300000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Transmissora Aliança de Energia Elétrica S.A. (TAESA). “Divulgação de Resultados 2T26.” August 11, 2026. https://ri.taesa.com.br/wp-content/uploads/2018/11/TAESA_Release-2T26.pdf.',
    annotation="TAESA 6M26 NEW R$445.3m ~USD 85.76m via Fed H.10. Supports taesa_6m26_capex_445p3m_brl.",
    evid_note="Opened TAESA 2T26 company RI PDF; CAPEX 6M26 R$445.3m (−40.5%) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / other — NEW Eneva 2T26 CapEx R$1.59bn
row_doc(
    "eneva_2t26_capex_1p59bn_brl",
    "energy", "power_plants_grid", "other",
    "Eneva — 2T26 CapEx Total R$1.59bn",
    "Brazil",
    "CVM IPE protocol 1556832 / Eneva 2T26 results presentation: CAPEX Total (economic/competence view) R$1,590 million in 2T26; 87% of CapEx directed to capital projects in development; principal investments include LRCAP 2026 R$616m, Azulão 950 R$415m (+R$77m support), Upstream R$147m (+R$57m Gavião fields), Sustaining Parnaíba II/Jaguatirica. CapEx: enter R$1.59bn 2T26 face. Distinct from Fluence/GE Vernova Azulão equipment rows.",
    "1590000000", "2026-06-30", "2026", "-2.53", "-44.30",
    "Eneva Parnaíba / Azulão thermal-gas footprint (São Luís / Maranhão corridor pin).",
    "eneva_2t26_cvm_1556832",
    "CAPEX Total¹ (R$ Milhões) … 2T26 … 1.590 … 87% do Capex destinado aos projetos de capital em desenvolvimento",
    "https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1556832",
    "Actor: Eneva S.A. (Brazilian thermal/gas IPP) — other. NEW row: company CVM 2T26 CapEx Total R$1.59bn. Shuffle power_plants_grid.",
    "hunt_cycle255", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1590000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Eneva S.A. “Resultados 2T26” presentation (CVM IPE protocol 1556832). August 2026. https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1556832.',
    annotation="Eneva 2T26 NEW R$1.59bn ~USD 306.23m via Fed H.10. Supports eneva_2t26_capex_1p59bn_brl.",
    evid_note="Opened Eneva 2T26 CVM presentation PDF; CAPEX Total 2T26 R$1,590m / 87% development projects / LRCAP+Azulão+Upstream breakouts confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle255 added {len(added)}: {added}")
    print(f"cycle255 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
