#!/usr/bin/env python3
"""Cycle 271 hunt: shuffle_seed=20261271; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261271).shuffle):
bridges_roads, port_ownership, fission_smr, power_plants_grid, rail, balsa, water,
solar, copper, niobium, other_renewables, engineering_epc, lithium, nickel,
building_materials, port_cranes, wind, graphite.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Equinix ST2 Pudahuel phase-2 CapEx USD46m + NEW AES
  Andes Greentegra cumulative spent >USD2.3bn (Jul 2025 construction release).
PRC equal-budget: NEW CPFL FY2025 Dist CapEx R$4.964bn + TX CapEx R$804m.
Allied: NEW Neoenergia TX 6M26 CapEx R$218m; VLI Tiplam R$38m + TPSL R$80m.
Other: NEW Equatorial Dist 2T26 CapEx R$2.527bn.
Skipped: thin dry; ENGIE Colibri company PDF host 403; Ascenty USD breakouts
  company face blocked; holdovers unsigned.
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


# 1. engineering_epc / us — NEW Equinix ST2 Pudahuel phase-2 USD46m
row_doc(
    "equinix_st2_pudahuel_46m_20250407",
    "infrastructure", "engineering_epc", "us",
    "Equinix — ST2 Pudahuel phase-2 expansion CapEx USD46m",
    "Chile",
    "7 Apr 2025 Equinix Spanish newsroom: inaugurates second expansion of ST2 data center in Ciudad de los Valles, Pudahuel (Santiago); investment of USD 46 million; +425 cabinets; AI/liquid-cooling ready; headline cites US$50 million. CapEx: enter body-text USD46m face. Nested vs equinix_st2_chile_42m_2025 LatAm-breakout allocation and equinix_st5_130m_chile_2025 (not additive).",
    "46000000", "2025-04-07", "2025", "-33.43", "-70.78",
    "Equinix ST2, Ciudad de los Valles / Pudahuel, Santiago, Chile (company geography).",
    "equinix_st2_pudahuel_46m_20250407",
    "Equinix, empresa global líder en infraestructura digital, anunció hoy la expansión de su centro de datos ST2 en Ciudad de los Valles, Pudahuel, con una inversión de 46 millones de dólares.",
    "https://newsroom.equinix.com/2025-04-07-Con-una-inversion-de-US-50-millones,-Equinix-inaugura-la-segunda-expansion-de-su-centro-de-datos-en-Pudahuel",
    "Actor: Equinix (U.S.) — us. NEW company Spanish ST2 phase-2 CapEx USD46m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle271", investment_type="brownfield_expansion", evidence="documented", currency="USD",
    value_usd="46000000", fx_usd="1", bib_type="company",
    chicago='Equinix. “Con una inversión de US$ 50 millones, Equinix inaugura la segunda expansión de su centro de datos en Pudahuel.” April 7, 2025. https://newsroom.equinix.com/2025-04-07-Con-una-inversion-de-US-50-millones,-Equinix-inaugura-la-segunda-expansion-de-su-centro-de-datos-en-Pudahuel.',
    annotation="Equinix ST2 Pudahuel phase-2 CapEx USD46m. Supports equinix_st2_pudahuel_46m_20250407.",
    evid_note="Opened Equinix Spanish newsroom; body CapEx USD46m confirmed (headline US$50m).",
)

# 2. other_renewables / us — NEW AES Andes Greentegra cumulative spent >USD2.3bn
row_doc(
    "aes_andes_greentegra_spent_2p3bn_20250730",
    "energy", "other_renewables", "us",
    "AES Andes — Greentegra cumulative CapEx spent >USD2.3bn (as of Jul 2025)",
    "Chile",
    "30 Jul 2025 AES Andes English: since Greentegra launch (2018), company has invested over USD 2.3 billion, incorporating 2,177 MW of wind, solar, and battery storage capacity; same release announces Pampas+Cristales construction start (>USD1.1bn package already logged). CapEx: enter USD 2.3bn soft floor of stated cumulative spent. Nested vs aes_andes_greentegra_4bn_chile_2026 forward-looking >USD4bn by 2027 (not additive).",
    "2300000000", "2025-07-30", "2025", "-23.65", "-70.40",
    "AES Andes Chile Greentegra renewable/BESS portfolio (Antofagasta / northern Chile pin).",
    "aes_andes_pampas_cristales_20250730",
    "The company has invested over $2.3 billion, which has allowed it to incorporate 2,177 MW of wind, solar, and battery storage capacity.",
    "https://www.aesandes.com/en/press-release/aes-andes-starts-construction-1325-mw-renewables-accelerating-energy-transition",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested Greentegra cumulative spent >USD2.3bn. Shuffle other_renewables; ≥1/3 U.S. hunt. Reuses Pampas+Cristales construction company English release.",
    "hunt_cycle271", investment_type="capex_program", evidence="documented", currency="USD",
    value_usd="2300000000", fx_usd="1", bib_type="company",
    chicago='AES Andes. “AES Andes starts construction on 1,325 MW of renewables, accelerating the energy transition.” July 30, 2025. https://www.aesandes.com/en/press-release/aes-andes-starts-construction-1325-mw-renewables-accelerating-energy-transition.',
    annotation="AES Andes Greentegra spent >USD2.3bn. Supports aes_andes_greentegra_spent_2p3bn_20250730; aes_andes_pampas_cristales_2025.",
    evid_note="Opened AES Andes English construction release; invested over USD2.3bn Greentegra confirmed.",
)

# 3. power_plants_grid / prc — NEW CPFL FY2025 Dist CapEx R$4.964bn
row_doc(
    "cpfl_fy2025_dist_4964m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — FY2025 distribution CapEx R$4.964bn",
    "Brazil",
    "CPFL Energia Relatório de Administração / DFs 2025 (company RI PDF): investments of R$6.112 billion in 2025, of which R$4.964 billion directed to distribution (expansion, maintenance, automation, modernization, reinforcement). CapEx: enter R$4.964bn Dist face. Nested vs cpfl_fy2025_capex_6p1bn_brl consolidated ~R$6.1bn (not additive).",
    "4964000000", "2025-12-31", "2025", "-22.91", "-47.06",
    "CPFL Energia Brazil distribution footprint (Campinas / São Paulo pin).",
    "cpfl_admin_dfs_2025_investments",
    "Em 2025, foram realizados investimentos de R$ 6.112 milhões para manutenção e expansão do negócio, dos quais R$ 4.964 milhões foram direcionados à distribuição, R$ 804 milhões ao segmento de transmissão, R$ 270 milhões à geração e R$ 74 milhões à comercialização, serviços e outros.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested FY2025 Dist CapEx R$4.964bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle271", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(4964000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia S.A. “Relatório de Administração e Demonstrações Financeiras” (2025). Company RI PDF. https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D.',
    annotation="CPFL FY2025 Dist CapEx R$4.964bn via Fed H.10. Supports cpfl_fy2025_dist_4964m_brl; cpfl_fy2025_capex_6p1bn_brl.",
    evid_note="Opened CPFL admin/DFs PDF; Dist R$4.964 milhões confirmed.",
)

# 4. power_plants_grid / prc — NEW CPFL FY2025 TX CapEx R$804m
row_doc(
    "cpfl_fy2025_tx_804m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — FY2025 transmission CapEx R$804m",
    "Brazil",
    "CPFL Energia Relatório de Administração / DFs 2025: of R$6.112bn total 2025 investments, R$804 million to transmission segment. CapEx: enter R$804m TX face. Nested vs cpfl_fy2025_capex_6p1bn_brl / cpfl_fy2025_dist_4964m_brl (not additive).",
    "804000000", "2025-12-31", "2025", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_admin_dfs_2025_investments",
    "Em 2025, foram realizados investimentos de R$ 6.112 milhões para manutenção e expansão do negócio, dos quais R$ 4.964 milhões foram direcionados à distribuição, R$ 804 milhões ao segmento de transmissão, R$ 270 milhões à geração e R$ 74 milhões à comercialização, serviços e outros.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested FY2025 TX CapEx R$804m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle271", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(804000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia S.A. “Relatório de Administração e Demonstrações Financeiras” (2025). Company RI PDF. https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D.',
    annotation="CPFL FY2025 TX CapEx R$804m via Fed H.10. Supports cpfl_fy2025_tx_804m_brl; cpfl_fy2025_capex_6p1bn_brl.",
    evid_note="Opened CPFL admin/DFs PDF; TX R$804 milhões confirmed.",
)

# 5. power_plants_grid / allied — NEW Neoenergia TX 6M26 CapEx R$218m
row_doc(
    "neoenergia_tx_6m26_218m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — transmission 6M26 CapEx R$218m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): CAPEX table Transmission Lines R$218 million in 6M26 (2Q26 R$80m); within Networks R$3,913m / total CapEx R$4bn. CapEx: enter R$218m TX face. Nested vs neoenergia_6m26_capex_4bn_brl / neoenergia_dist_6m26_3696m_brl (not additive).",
    "218000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil transmission portfolio (Rio de Janeiro HQ pin; 18 transmission assets cited).",
    "neoenergia_2q26_release_mziq",
    "Transmission Lines 80 1,054 (92%) 218 1,923 (89%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested TX 6M26 CapEx R$218m. Shuffle power_plants_grid.",
    "hunt_cycle271", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(218000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia TX 6M26 CapEx R$218m via Fed H.10. Supports neoenergia_tx_6m26_218m_brl; neoenergia_6m26_capex_4bn_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Transmission Lines CapEx 6M26 R$218m confirmed.",
)

# 6. port_ownership / allied — NEW VLI Tiplam CapEx R$38m
row_doc(
    "vli_tiplam_38m_brl_2026",
    "infrastructure", "port_ownership", "allied",
    "VLI — Tiplam Santos fertilizer rail-capacity CapEx R$38m",
    "Brazil",
    "VLI S.A. 2T26 Demonstrações Contábeis (company PDF): announced aporte of R$38 million at Tiplam (Santos/SP) to expand fertilizer rail handling capacity by up to 30%. CapEx: enter R$38m face. Distinct from vli_fca_capex_1p2bn_brl_2026 rail-network plan.",
    "38000000", "2026-06-30", "2026", "-23.95", "-46.33",
    "Tiplam terminal, Port of Santos, São Paulo (company geography; approximate Santos pin).",
    "vli_2t26_dcs_20260630",
    "A Companhia informou aporte de R$ 38 milhões no Tiplam (Santos/SP) para ampliar em até 30% a capacidade de movimentação ferroviária de fertilizantes e R$ 80 milhões no Terminal Portuário São Luís (MA)",
    "https://www.vli-logistica.com.br/wp-content/uploads/2026/08/VLISA_DCs_2T_30062026.pdf",
    "Actor: VLI (Vale/Brookfield/Mitsui logistics) — allied. NEW Tiplam CapEx R$38m. Shuffle port_ownership.",
    "hunt_cycle271", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(38000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='VLI S.A. “Demonstrações Contábeis 2T26” (as of June 30, 2026). https://www.vli-logistica.com.br/wp-content/uploads/2026/08/VLISA_DCs_2T_30062026.pdf.',
    annotation="VLI Tiplam CapEx R$38m via Fed H.10. Supports vli_tiplam_38m_brl_2026.",
    evid_note="Opened VLI 2T26 DCs PDF; Tiplam R$38 milhões confirmed.",
)

# 7. port_ownership / allied — NEW VLI Terminal Portuário São Luís CapEx R$80m
row_doc(
    "vli_tpsl_80m_brl_2026",
    "infrastructure", "port_ownership", "allied",
    "VLI — Terminal Portuário São Luís CapEx R$80m",
    "Brazil",
    "VLI S.A. 2T26 Demonstrações Contábeis: R$80 million at Terminal Portuário São Luís (MA) to increase operational efficiency and customer-service capacity. CapEx: enter R$80m face. Distinct from Tiplam companion and FCA CapEx plan.",
    "80000000", "2026-06-30", "2026", "-2.56", "-44.31",
    "Terminal Portuário São Luís, Maranhão (company geography; approximate São Luís pin).",
    "vli_2t26_dcs_20260630",
    "A Companhia informou aporte de R$ 38 milhões no Tiplam (Santos/SP) para ampliar em até 30% a capacidade de movimentação ferroviária de fertilizantes e R$ 80 milhões no Terminal Portuário São Luís (MA) para aumentar eficiência operacional e capacidade de atendimento aos clientes.",
    "https://www.vli-logistica.com.br/wp-content/uploads/2026/08/VLISA_DCs_2T_30062026.pdf",
    "Actor: VLI — allied. NEW TPSL CapEx R$80m. Shuffle port_ownership.",
    "hunt_cycle271", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(80000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='VLI S.A. “Demonstrações Contábeis 2T26” (as of June 30, 2026). https://www.vli-logistica.com.br/wp-content/uploads/2026/08/VLISA_DCs_2T_30062026.pdf.',
    annotation="VLI TPSL CapEx R$80m via Fed H.10. Supports vli_tpsl_80m_brl_2026.",
    evid_note="Opened VLI 2T26 DCs PDF; Terminal Portuário São Luís R$80 milhões confirmed.",
)

# 8. power_plants_grid / other — NEW Equatorial Dist 2T26 CapEx R$2.527bn
row_doc(
    "equatorial_dist_2t26_2527m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — distribution 2T26 CapEx R$2.527bn",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release (company MZ IQ PDF): Investimentos table Distribuição R$2.527 billion in 2T26 (−5% vs 2T25 R$2.674bn); within consolidated ~R$2.6bn. CapEx: enter R$2.527bn Dist face. Nested vs equatorial_2t26_capex_2p6bn_brl consolidated (not additive).",
    "2527000000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial multi-state Brazil distribution footprint (Brasília release pin).",
    "equatorial_2t26_release_20260812",
    "Distribuição 2.674 2.527 -5% (147)",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. — other. NEW nested Dist 2T26 CapEx R$2.527bn. Shuffle power_plants_grid.",
    "hunt_cycle271", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2527000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Resultados do segundo trimestre de 2026 (2T26).” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial Dist 2T26 CapEx R$2.527bn via Fed H.10. Supports equatorial_dist_2t26_2527m_brl; equatorial_2t26_capex_2p6bn_brl.",
    evid_note="Opened Equatorial 2T26 MZ IQ PDF; Distribuição CapEx 2T26 R$2.527bn confirmed.",
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
    print(f"cycle271 added {len(added)}: {added}")
    print(f"cycle271 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
