#!/usr/bin/env python3
"""Cycle 248 hunt: shuffle_seed=20261248; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261248).shuffle):
other_renewables, port_ownership, lithium, wind, engineering_epc, copper,
bridges_roads, fission_smr, solar, graphite, power_plants_grid, nickel, niobium,
water, rail, building_materials, port_cranes, balsa.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: honest residual (Ascenty Vinhedo/Osasco USD breakouts on
  Valor only — company page holds USD 1.2bn envelope already logged; AES Andes
  Solar Hub / Greentegra already filled; Wabtec Contagem R$150m prior cycle).
PRC equal-budget: NEW CPFL Transmissão Aneel Lote 3 CapEx ~R$1.1bn (company).
Allied: NEW ENGIE Graúna transmission Aneel CapEx R$2,933.6m (English earnings);
  NEW Neoenergia Elektro R$8.2bn 2026–2030 (company).
Skipped: Ascenty site breakouts Valor-only; Progress Rail R$430m conflicts with
  logged R$200m eight-loco; holdovers unsigned; thin dry.
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


# 1. power_plants_grid / prc — NEW CPFL Transmissão Aneel Lote 3 ~R$1.1bn
row_doc(
    "cpfl_tx_lote3_1p1bn_brl_2025",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — Aneel Transmission Auction 4/2025 Lote 3 (RS/PR)",
    "Brazil",
    "31 Oct 2025 CPFL company: won Lote 3 (Rio Grande do Sul and Paraná) at Aneel Transmission Auction 4/2025 with 53.93% discount to max RAP; ~115 km of new 230 kV lines and ~1,100 MVA of 230/525 kV transformation; investment on the order of R$ 1.1 billion; ~48-month execution. CapEx: enter R$1.1bn face. Distinct from cpfl_fy2025_capex_6p1bn / RGE 9.3bn / smart meters 1.2bn.",
    "1100000000", "2025-10-31", "2025", "-30.03", "-51.23",
    "CPFL Transmissão Lote 3 RS/PR corridor (Porto Alegre pin).",
    "cpfl_tx_lote3_1p1bn_20251031",
    "Estão previstas a construção de aproximadamente 115 km de novas linhas de 230 kV, com cerca de 1.100 MVA de transformação em 230 kV / 525 kV, investimento da ordem de R$ 1,1 bilhão e prazo de execução estimado em 48 meses.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-arremata-lote-do-leilao-da-aneel-com-foco-na-estrategia-de-expansao-do-negocio",
    "Actor: CPFL Transmissão (State Grid–controlled CPFL Energia) — prc. NEW row: company Portuguese Lote 3 CapEx ~R$1.1bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle248", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(1100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia arremata lote do Leilão da ANEEL com foco na estratégia de expansão do negócio Transmissão.” October 31, 2025. https://www.grupocpfl.com.br/noticia/cpfl-energia-arremata-lote-do-leilao-da-aneel-com-foco-na-estrategia-de-expansao-do-negocio.',
    annotation="CPFL TX Lote 3 NEW ~R$1.1bn ~USD 211.86m via Fed H.10. Supports cpfl_tx_lote3_1p1bn_brl_2025.",
    evid_note="Opened CPFL Portuguese; ~R$1.1bn / 115 km / 1,100 MVA / RS+PR / 53.93% discount confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / allied — NEW ENGIE Graúna Aneel CapEx R$2,933.6m
row_doc(
    "engie_grauna_tx_2p93bn_brl_2024",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil — Graúna Transmissora (Aneel Auction 02/2024 Block 1)",
    "Brazil",
    "25 Feb 2026 ENGIE Brasil Energia English 4Q25 earnings release: Graúna (Auction 02/2024 Block 1) — ~732 km new lines + two new substations + brownfield 162 km / two substations across SC/PR/MG/SP/ES; contracted RAP R$268.3m; estimated Aneel Capex R$2,933.6m; concession signed 9 Dec 2024; brownfield ops from 18 Jul 2025 (~5% RAP). CapEx: enter R$2,933.6m face. Distinct from engie_asa_branca_tx_2p7bn_2025 / engie_fy2025_capex_6bn_brl.",
    "2933600000", "2024-12-09", "2024", "-19.92", "-43.94",
    "ENGIE Graúna multi-state transmission (MG/ES brownfield pin Belo Horizonte).",
    "engie_grauna_capex_2933m_4q25",
    "Contracted RAP (R$ million): 268.3. Estimated Aneel Capex (R$ million): 2,933.6. Total 268.3 / 2,933.6. Santa Catarina, Paraná, Minas Gerais, São Paulo and Espírito Santo.",
    "https://www.engie.com.br/wp-content/uploads/2026/02/260225-Earnings-Release-4Q25.pdf",
    "Actor: ENGIE Brasil Energia (France) — allied. NEW row: company English Aneel Capex R$2,933.6m Graúna. Shuffle power_plants_grid.",
    "hunt_cycle248", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(2933600000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ENGIE Brasil Energia. “Earnings Release 4Q25.” February 25, 2026. https://www.engie.com.br/wp-content/uploads/2026/02/260225-Earnings-Release-4Q25.pdf.',
    annotation="ENGIE Graúna NEW R$2.9336bn ~USD 565.01m via Fed H.10. Supports engie_grauna_tx_2p93bn_brl_2024.",
    evid_note="Opened ENGIE English 4Q25 earnings PDF; Aneel Capex R$2,933.6m / RAP R$268.3m / ~732+162 km / concession 9 Dec 2024 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW Neoenergia Elektro R$8.2bn
row_doc(
    "neoenergia_elektro_8p2bn_brl_2026_2030",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Elektro — SP/MS distribution CapEx >R$8.2bn (2026–2030)",
    "Brazil",
    "11 May 2026 Neoenergia Elektro company: will invest more than R$ 8.2 billion between 2026 and 2030 across 228 municipalities in São Paulo and Mato Grosso do Sul (+66% vs prior cycle) after early concession renewal to 2058. CapEx: enter R$8.2bn soft floor. Distinct from neoenergia_dist_50bn / Coelba 25bn / Pernambuco 9.7bn / Cosern 4.1bn / Ilhabela nested R$200m.",
    "8200000000", "2026-05-11", "2026", "-23.55", "-46.63",
    "Neoenergia Elektro SP/MS concession (São Paulo pin).",
    "neoenergia_elektro_8p2bn_20260511",
    "A Neoenergia Elektro irá investir, entre 2026 e 2030, mais de R$ 8,2 bilhões nos 228 municípios da sua área de concessão localizados nos estados de São Paulo e Mato Grosso do Sul.",
    "https://www.neoenergia.com/web/sp/w/renovacao-concessao-30-anos-bilhoes-investimentos-elektro",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW row: company Portuguese Elektro >R$8.2bn through 2030. Shuffle power_plants_grid.",
    "hunt_cycle248", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(8200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia Elektro. “Neoenergia Elektro tem concessão renovada por mais 30 anos e anuncia R$ 8,2 bilhões em investimentos.” May 11, 2026. https://www.neoenergia.com/web/sp/w/renovacao-concessao-30-anos-bilhoes-investimentos-elektro.',
    annotation="Neoenergia Elektro NEW >R$8.2bn floor ~USD 1579.32m via Fed H.10. Supports neoenergia_elektro_8p2bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Elektro Portuguese; >R$8.2bn 2026–2030 / +66% / 228 municipalities / to 2058 confirmed. CapEx enter R$8.2bn soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle248 added {len(added)}: {added}")
    print(f"cycle248 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
