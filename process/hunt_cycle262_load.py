#!/usr/bin/env python3
"""Cycle 262 hunt: shuffle_seed=20261262; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261262).shuffle):
bridges_roads, rail, other_renewables, engineering_epc, nickel, power_plants_grid,
port_ownership, fission_smr, water, lithium, solar, building_materials, niobium, wind,
graphite, balsa, copper, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent residual (Equinix/Ascenty/Cirion/Wabtec Contagem dense;
  Progress Rail VLI R$430m / Equinix SP USD109m without openable dual primary).
PRC equal-budget: honest residual.
Other: NEW Ecorodovias 2T26 CapEx R$1,547.2m; NEW Ecorodovias 1S26 CapEx R$2,520.9m;
  NEW Aegea ecosystem 2T26 CapEx R$1,828m; NEW Aegea ecosystem 6M26 CapEx R$3,407m
  (distinct from prior Águas-scope R$832m row); NEW Cemig 2T26 CapEx R$1,805.3m.
Skipped: thin dry; holdovers unsigned; EPR Litoral 1S26 without dual company URL check.
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


# 1. bridges_roads / other — NEW Ecorodovias 2T26 CapEx R$1,547.2m
row_doc(
    "ecorodovias_2t26_capex_1547p2m_brl",
    "infrastructure", "bridges_roads", "other",
    "Ecorodovias — 2T26 CapEx R$1,547.2m",
    "Brazil",
    "EcoRodovias Infraestrutura e Logística S.A. Release de Resultados 2T26 (company RI PDF via republication): Capex R$1,547.2 million in 2T26 (+32.0% vs 2T25); mainly capacity expansion / improvements / pavement on Ecovias Rio Minas, Araguaia, Noroeste Paulista and Capixaba. CapEx: enter R$1,547.2m 2T26 face. Nested vs 1S26 envelope / Rota das Gerais plan (not additive).",
    "1547200000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Ecorodovias Brazil highway concession portfolio (São Paulo HQ pin).",
    "ecorodovias_2t26_release_2026",
    "Foco na entrega das obras de ampliação da capacidade e melhorias das concessões rodoviárias: capex de R$1.547,2 milhões no 2T26 (+32,0%) e R$2.520,9 milhões no 1S26 (+19,2%). … Capex6 1.547,2 1.171,9 32,0% 2.520,9 2.115,4 19,2%.",
    "https://investidor10.com.br/acoes/link_comunicado/ECOR3/46416/",
    "Actor: EcoRodovias (Brazilian highway concessionaire) — other. NEW nested 2T26 CapEx R$1,547.2m. Shuffle bridges_roads.",
    "hunt_cycle262", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1547200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='EcoRodovias Infraestrutura e Logística S.A. “Release de Resultados 2T26.” 2026. https://investidor10.com.br/acoes/link_comunicado/ECOR3/46416/.',
    annotation="Ecorodovias 2T26/1S26 CapEx via Fed H.10. Supports ecorodovias_2t26_capex_1547p2m_brl; ecorodovias_1s26_capex_2520p9m_brl.",
    evid_note="Opened Ecorodovias company 2T26 results PDF (RI republication); Capex R$1,547.2m / 1S26 R$2,520.9m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. bridges_roads / other — NEW Ecorodovias 1S26 CapEx R$2,520.9m
row_doc(
    "ecorodovias_1s26_capex_2520p9m_brl",
    "infrastructure", "bridges_roads", "other",
    "Ecorodovias — 1S26 CapEx R$2,520.9m",
    "Brazil",
    "EcoRodovias Release de Resultados 2T26: Capex R$2,520.9 million in 1S26 (+19.2% vs 1S25). CapEx: enter R$2,520.9m 1S26 face. Nested vs ecorodovias_2t26_capex_1547p2m_brl (not additive).",
    "2520900000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Ecorodovias Brazil highway concession portfolio (São Paulo HQ pin).",
    "ecorodovias_2t26_release_2026",
    "capex de R$1.547,2 milhões no 2T26 (+32,0%) e R$2.520,9 milhões no 1S26 (+19,2%). … Capex6 1.547,2 1.171,9 32,0% 2.520,9 2.115,4 19,2%.",
    "https://investidor10.com.br/acoes/link_comunicado/ECOR3/46416/",
    "Actor: EcoRodovias — other. NEW nested 1S26 CapEx R$2,520.9m. Shuffle bridges_roads.",
    "hunt_cycle262", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2520900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='EcoRodovias Infraestrutura e Logística S.A. “Release de Resultados 2T26.” 2026. https://investidor10.com.br/acoes/link_comunicado/ECOR3/46416/.',
    annotation="Ecorodovias 2T26/1S26 CapEx via Fed H.10. Supports ecorodovias_2t26_capex_1547p2m_brl; ecorodovias_1s26_capex_2520p9m_brl.",
    evid_note="Opened Ecorodovias 2T26 company PDF; 1S26 Capex R$2,520.9m (+19.2%) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. water / other — NEW Aegea ecosystem 2T26 CapEx R$1,828m
row_doc(
    "aegea_2t26_ecosystem_capex_1828m_brl",
    "resources", "water", "other",
    "Aegea — 2T26 ecosystem CapEx R$1,828m",
    "Brazil",
    "5 Aug 2026 Aegea 2T26 & 6M26 earnings release (company MZ IQ PDF): Capex R$1,828 million in 2T26 (+21.1% vs 2T25 R$1,509m); investments R$1,901m including outorgas. CapEx: enter R$1,828m 2T26 ecosystem face. Distinct from aegea_6m26_capex_832m_brl (narrower Capex table R$832m 6M26 perimeter).",
    "1828000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Aegea sanitation ecosystem Brazil footprint (Rio de Janeiro metro pin).",
    "aegea_2t26_6m26_release_mziq",
    "No primeiro semestre, investimos R$ 3,8 bilhões, sendo R$ 402 milhões em pagamento de outorgas e R$ 3,4 bilhões em Capex … Capex 1.828 1.509 21,1% 3.407 2.818 20,9% … Investimentos5 1.901 1.626 16,9% 3.809 2.987 27,5%.",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW ecosystem 2T26 CapEx R$1,828m. Shuffle water.",
    "hunt_cycle262", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1828000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento e Participações S.A. “Aegea 2T26 & 6M26.” August 5, 2026. https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea ecosystem 2T26/6M26 CapEx via Fed H.10. Supports aegea_2t26_ecosystem_capex_1828m_brl; aegea_6m26_ecosystem_capex_3407m_brl.",
    evid_note="Opened Aegea company 2T26/6M26 MZ IQ PDF; Capex table R$1,828m / R$3,407m confirmed (distinct from R$832m narrower Capex table). CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. water / other — NEW Aegea ecosystem 6M26 CapEx R$3,407m
row_doc(
    "aegea_6m26_ecosystem_capex_3407m_brl",
    "resources", "water", "other",
    "Aegea — 6M26 ecosystem CapEx R$3,407m",
    "Brazil",
    "5 Aug 2026 Aegea 2T26 & 6M26 earnings release: Capex R$3,407 million in 6M26 (+20.9% vs 6M25 R$2,818m); narrative also states R$3.4bn Capex within R$3.8bn total investments (incl. R$402m outorgas). CapEx: enter R$3,407m 6M26 ecosystem face. Distinct from aegea_6m26_capex_832m_brl; nested vs 2T26 R$1,828m (not additive).",
    "3407000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Aegea sanitation ecosystem Brazil footprint (Rio de Janeiro metro pin).",
    "aegea_2t26_6m26_release_mziq",
    "investimos R$ 3,8 bilhões, sendo R$ 402 milhões em pagamento de outorgas e R$ 3,4 bilhões em Capex … Capex 1.828 1.509 21,1% 3.407 2.818 20,9%.",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW ecosystem 6M26 CapEx R$3,407m. Shuffle water.",
    "hunt_cycle262", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3407000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento e Participações S.A. “Aegea 2T26 & 6M26.” August 5, 2026. https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea ecosystem 2T26/6M26 CapEx via Fed H.10. Supports aegea_2t26_ecosystem_capex_1828m_brl; aegea_6m26_ecosystem_capex_3407m_brl.",
    evid_note="Opened Aegea company MZ IQ PDF; 6M26 Capex R$3,407m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / other — NEW Cemig 2T26 CapEx R$1,805.3m
row_doc(
    "cemig_2t26_capex_1805p3m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — 2T26 CapEx R$1,805.3m",
    "Brazil",
    "Cemig 1S26/2T26 results presentation (company RI PDF): Investimentos R$1,805.3 million in 2T26 (+16.9% vs 2T25 R$1,544.0m); part of Capex realizado R$3.28bn in 1S26. CapEx: enter R$1,805.3m 2T26 face. Nested vs cemig_1s26_capex_3p28bn_brl / R$44bn plan (not additive).",
    "1805300000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig Minas Gerais footprint (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "Capex realizado de R$3,28 bilhões no 1S26 (aumento de 19,2% x 1S25) … Investimentos 1.805,3 1.544,0 16,9% 1.476,7 22,3%.",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig — other. NEW nested 2T26 CapEx R$1,805.3m under 1S26 envelope. Shuffle power_plants_grid.",
    "hunt_cycle262", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1805300000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais — Cemig. “Resultados 1S26 / 2T26” presentation. 2026. https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig 1S26/2T26 CapEx via Fed H.10. Supports cemig_1s26_capex_3p28bn_brl; cemig_2t26_capex_1805p3m_brl.",
    evid_note="Opened Cemig company RI PDF; Investimentos 2T26 R$1,805.3m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    # extend cemig bib supports
    if "cemig_1s26_results_presentation_20260630" in bib_by:
        e = bib[bib_by["cemig_1s26_results_presentation_20260630"]]
        e["supports"] = list(dict.fromkeys((e.get("supports") or []) + [
            "cemig_1s26_capex_3p28bn_brl", "cemig_2t26_capex_1805p3m_brl", "hunt_cycle262"
        ]))
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle262 added {len(added)}: {added}")
    print(f"cycle262 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
