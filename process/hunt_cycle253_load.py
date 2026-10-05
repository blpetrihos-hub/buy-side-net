#!/usr/bin/env python3
"""Cycle 253 hunt: shuffle_seed=20261253; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261253).shuffle):
port_ownership, building_materials, niobium, copper, balsa, water, graphite,
engineering_epc, lithium, port_cranes, rail, solar, power_plants_grid,
bridges_roads, wind, other_renewables, nickel, fission_smr.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Cirion (Stonepeak) >USD 300m LatAm 2024 CapEx.
PRC equal-budget: honest residual (CPFL/State Grid/BYD/Goldwind/SPIC/CTG CapEx dense).
Allied: NEW Neoenergia 1T26 CapEx R$1.8bn.
Other: NEW Gerdau FY2025 CapEx R$6.1bn + 2026 plan R$4.7bn; NEW Copel 2T26 CapEx
  R$957.2m; NEW Aegea 6M26 CapEx R$832m (water).
Skipped: thin balsa/nickel/fission dry; holdovers unsigned; catalog dense elsewhere.
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


# 1. engineering_epc / us — NEW Cirion >USD 300m LatAm 2024
row_doc(
    "cirion_latam_300m_2024",
    "infrastructure", "engineering_epc", "us",
    "Cirion Technologies (Stonepeak) — LatAm digital infrastructure CapEx >USD 300m (2024)",
    "Brazil",
    "1 Aug 2024 Cirion Technologies English company blog (second anniversary as Cirion under Stonepeak): digital/tech infrastructure investments increased annually; 2023 invested over US$235MM, expected to increase ~30% in 2024 hitting over US$300MM; footprint >90,500 km fiber across >20 LatAm countries. CapEx: enter >USD 300m soft floor for 2024 LatAm envelope. Distinct from Ascenty/Equinix/Scala/ODATA/Tecto DC CapEx rows.",
    "300000000", "2024-08-01", "2024", "", "",
    "Cirion LatAm multi-country fiber/DC footprint (Santiago/Lima/Rio expansions cited in trade coverage; multi-site — lat/lon blank).",
    "cirion_anniversary_300m_20240801",
    "In 2023, we invested over US$235MM figure that is expected to increase by 30% this year, hitting over US$300MM.",
    "https://blog.ciriontechnologies.com/en/new-anniversary-investments-expansions-strategic-alliances",
    "Actor: Cirion Technologies (Stonepeak U.S.-backed; ex-Lumen LatAm) — us. NEW row: company English >USD 300m 2024 LatAm CapEx soft floor. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle253", investment_type="corporate_capex", evidence="documented", currency="USD",
    chicago='Cirion Technologies. “anniversary with investments, expansions and strategic alliances.” August 1, 2024. https://blog.ciriontechnologies.com/en/new-anniversary-investments-expansions-strategic-alliances.',
    annotation="Cirion NEW >USD 300m 2024 LatAm CapEx soft floor. Supports cirion_latam_300m_2024.",
    evid_note="Opened Cirion English anniversary blog (published 2024-08-01); >US$300MM 2024 / >US$235MM 2023 / Stonepeak backing / >90,500 km fiber confirmed.",
)

# 2. building_materials / other — NEW Gerdau FY2025 CapEx R$6.1bn
row_doc(
    "gerdau_fy2025_capex_6p1bn_brl",
    "infrastructure", "building_materials", "other",
    "Gerdau — FY2025 CapEx R$6.1bn",
    "Brazil",
    "Latibex Notice to the Market / Gerdau 4Q25 earnings presentation: 2025 CAPEX R$6.1 b; CAPEX guidance for 2026 of R$4.7 b (−24% vs 2025 realized); maintenance / coking+blast furnaces / competitiveness split. CapEx: enter R$6.1bn FY2025 face. Consolidated group CapEx (Brazil + North America + South America); company materials emphasize Brazil operations including Ouro Branco hot-strip and Miguel Burnier mining. Distinct from 2026 plan row.",
    "6100000000", "2025-12-31", "2025", "-20.02", "-44.05",
    "Gerdau Brazil steel footprint (Ouro Branco / MG industrial pin).",
    "gerdau_4q25_latibex_presentation_2026",
    "2025 CAPEX: R$6.1 b CAPEX guidance for 2026 of R$4.7 b, down 24% vs. realized in 2025",
    "https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Notice%20to%20the%20Market%20-%20Presentation%20of%20the%204Q25%20earnings%20conference%20call.pdf",
    "Actor: Gerdau S.A. (Brazilian steel) — other. NEW row: company Latibex 4Q25 presentation R$6.1bn FY2025 CapEx. Shuffle building_materials.",
    "hunt_cycle253", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(6100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Gerdau S.A. “Notice to the Market — Presentation of the 4Q25 earnings conference call.” Latibex hechos relevantes, 2026. https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Notice%20to%20the%20Market%20-%20Presentation%20of%20the%204Q25%20earnings%20conference%20call.pdf.',
    annotation="Gerdau FY2025 NEW R$6.1bn ~USD 1174.86m via Fed H.10. Supports gerdau_fy2025_capex_6p1bn_brl.",
    evid_note="Opened Gerdau Latibex 4Q25 English presentation PDF; R$6.1bn 2025 CAPEX / R$4.7bn 2026 guidance confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. building_materials / other — NEW Gerdau 2026 CapEx plan R$4.7bn
row_doc(
    "gerdau_2026_capex_plan_4p7bn_brl",
    "infrastructure", "building_materials", "other",
    "Gerdau — 2026 CapEx plan R$4.7bn",
    "Brazil",
    "Latibex Notice to the Market / Gerdau 4Q25 earnings presentation: CAPEX guidance for 2026 of R$4.7 b, down 24% vs realized 2025; Board-approved plan focused on Maintenance and Competitiveness (excludes jointly-controlled entities/associates). CapEx: enter R$4.7bn 2026 plan face. Nested vs FY2025 R$6.1bn realized row (not additive across years).",
    "4700000000", "2025-10-01", "2026", "-20.02", "-44.05",
    "Gerdau Brazil steel footprint (Ouro Branco / MG industrial pin).",
    "gerdau_4q25_latibex_presentation_2026",
    "2025 CAPEX: R$6.1 b CAPEX guidance for 2026 of R$4.7 b, down 24% vs. realized in 2025",
    "https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Notice%20to%20the%20Market%20-%20Presentation%20of%20the%204Q25%20earnings%20conference%20call.pdf",
    "Actor: Gerdau S.A. (Brazilian steel) — other. NEW nested 2026 CapEx plan R$4.7bn. Shuffle building_materials.",
    "hunt_cycle253", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(4700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Gerdau S.A. “Notice to the Market — Presentation of the 4Q25 earnings conference call.” Latibex hechos relevantes, 2026. https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Notice%20to%20the%20Market%20-%20Presentation%20of%20the%204Q25%20earnings%20conference%20call.pdf.',
    annotation="Gerdau 2026 plan NEW R$4.7bn ~USD 905.22m via Fed H.10. Supports gerdau_2026_capex_plan_4p7bn_brl.",
    evid_note="Opened Gerdau Latibex 4Q25 English presentation PDF; R$4.7bn 2026 CAPEX guidance confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW Neoenergia 1T26 CapEx R$1.8bn
row_doc(
    "neoenergia_1t26_capex_1p8bn_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — 1T26 CapEx R$1.8bn",
    "Brazil",
    "28 Apr 2026 Neoenergia company Portuguese: 1T26 CapEx reached R$ 1.8 billion, of which R$ 1.7 billion allocated to distribution, contributing to Regulatory Asset Base (BRR) of R$ 45.6 billion. CapEx: enter R$1.8bn 1T26 face. Nested vs FY2025 R$10.1bn / R$50bn 2026–2030 distribution cycle envelopes (not additive).",
    "1800000000", "2026-03-31", "2026", "", "",
    "Neoenergia Brazil distribution/transmission CapEx (national footprint; no single-site pin).",
    "neoenergia_1t26_results_20260428",
    "Empenhada na estratégia de crescimento sustentável, a Neoenergia registrou Capex de R$ 1,8 bilhão no 1T26. Desse montante, R$ 1,7 bilhão foi alocado no segmento de distribuição, o que contribuiu para uma Base de Remuneração Regulatória (BRR) de R$ 45,6 bilhões.",
    "https://www.neoenergia.com/w/lucro-bilhao-alta-primeiro-trimestre-2026",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested 1T26 CapEx R$1.8bn. Shuffle power_plants_grid.",
    "hunt_cycle253", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia. “Neoenergia registra lucro de R$ 1,2 bilhão no 1T26, alta de 28% em relação ao 1T25.” April 28, 2026. https://www.neoenergia.com/w/lucro-bilhao-alta-primeiro-trimestre-2026.',
    annotation="Neoenergia 1T26 NEW R$1.8bn ~USD 346.68m via Fed H.10. Supports neoenergia_1t26_capex_1p8bn_brl.",
    evid_note="Opened Neoenergia Portuguese 1T26 results page; Capex R$1.8bn / distribuição R$1.7bn / BRR R$45.6bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / other — NEW Copel 2T26 CapEx R$957.2m
row_doc(
    "copel_2t26_capex_957p2m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — 2T26 CapEx R$957.2m",
    "Brazil",
    "CVM IPE protocol 1553068 / Copel 2T26 results presentation: Capex no 2T26 R$ 957,2 mi; includes LRCAP investments ~R$318m for Foz do Areia / Segredo capacity expansion. CapEx: enter R$957.2m 2T26 face. Nested vs copel_capex_2026_plan_3021m_brl envelope and ANDRITZ Foz/Segredo EPC row (not additive).",
    "957200000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel Paraná footprint (Curitiba HQ pin).",
    "copel_2t26_cvm_1553068",
    "Capex no 2T26 R$ 957,2 mi alavancagem de 2,9x dívida líquida/Ebitda em 30.06.2026",
    "https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1553068",
    "Actor: Copel (Paraná utility) — other. NEW nested 2T26 CapEx R$957.2m. Shuffle power_plants_grid.",
    "hunt_cycle253", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(957200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel. “2T26 Resultados” presentation (CVM IPE protocol 1553068). 2026. https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1553068.',
    annotation="Copel 2T26 NEW R$957.2m ~USD 184.36m via Fed H.10. Supports copel_2t26_capex_957p2m_brl.",
    evid_note="Opened Copel 2T26 CVM presentation PDF; Capex R$957.2m / LRCAP ~R$318m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. water / other — NEW Aegea 6M26 CapEx R$832m
row_doc(
    "aegea_6m26_capex_832m_brl",
    "resources", "water", "other",
    "Aegea Saneamento — 6M26 CapEx R$832m",
    "Brazil",
    "6 Aug 2026 Aegea 2T26/6M26 results presentation (CVM IPE protocol 1553072): Capex 6M26 x 6M25 R$ 832 milhões (−9.0%); investments in water-system improvements, Coletor Tempo Seco sewage system, ETE Queimados inauguration, and sewer-coverage network expansion. CapEx: enter R$832m 6M26 face. Distinct from prior utility CapEx rows (no prior Aegea water CapEx in catalog).",
    "832000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Aegea Águas do Rio / Corsan footprint (Rio de Janeiro metro pin).",
    "aegea_2t26_6m26_cvm_1553072",
    "Capex 6M26 x 6M25 R$ 832 milhões -9,0%",
    "https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1553072",
    "Actor: Aegea Saneamento (Brazilian private water/sanitation) — other. NEW row: company CVM 6M26 CapEx R$832m. Shuffle water / thin-adjacent.",
    "hunt_cycle253", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(832000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados Aegea 2T26 e 6M26” presentation (CVM IPE protocol 1553072). August 6, 2026. https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1553072.',
    annotation="Aegea 6M26 NEW R$832m ~USD 160.24m via Fed H.10. Supports aegea_6m26_capex_832m_brl.",
    evid_note="Opened Aegea 2T26/6M26 CVM presentation PDF; Capex 6M26 R$832m (−9.0% vs 6M25) / water+sewer investment scope confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle253 added {len(added)}: {added}")
    print(f"cycle253 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
