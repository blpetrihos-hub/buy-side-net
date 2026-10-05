#!/usr/bin/env python3
"""Cycle 283 hunt: shuffle_seed=20261283; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261283).shuffle):
wind, power_plants_grid, bridges_roads, graphite, building_materials, port_ownership,
niobium, solar, fission_smr, balsa, water, engineering_epc, nickel, rail, copper,
lithium, port_cranes, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Brasil 2026E CapEx R$136.7m (company Material Fact
  nested within 2024–2028 plan); Ormat/Wabtec/Progress/Equinix/SSA/Seven Seas CapEx
  blanks; EXIM/USTDA/Bechtel probes.
PRC equal-budget: NEW CPFL Transmissão RS 2025 planned R$638m + Nova Prata 2 ~R$78m
  (Jornal do Comércio proxy nested within RS ~R$3.9bn cycle).
Other: NEW Southern Copper 2Q26 CapEx USD422.8m; Rumo Contêiner Expansão 6M26 R$32m;
  Aegea Corsan outorga 6M26 R$41m.
Skipped: thin dry; ENGIE Colibri 403; Ascenty 403; Alupar TECP CapEx absent;
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


# 1. power_plants_grid / us — NEW AES Brasil 2026E CapEx R$136.7m
row_doc(
    "aes_brasil_2026e_capex_136p7m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2026E Total Investments CapEx R$136.7m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact (English): investment projections 2024–2028 table shows 2026E Total Investments R$136.7 million (Modernization and Maintenance R$136.7m; pipeline/expansion zero in 2026E). CapEx: enter R$136.7m 2026E face. Nested vs aes_brasil_capex_plan_1348m_brl_2024_2028 multi-year envelope (not additive).",
    "136700000", "2024-02-26", "2026", "-23.55", "-46.63",
    "AES Brasil generation portfolio (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Total Investments 712.7 214.2 136.7 125.5 159.5 1,348.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil (AES Corp U.S.–controlled) — us. NEW nested 2026E CapEx R$136.7m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle283", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(136700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2026E CapEx R$136.7m via Fed H.10. Supports aes_brasil_2026e_capex_136p7m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2026E Total Investments R$136.7m confirmed.",
)

# 2. power_plants_grid / prc — NEW CPFL TX RS 2025 planned R$638m
row_doc(
    "cpfl_tx_rs_2025_638m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — Rio Grande do Sul 2025 planned CapEx R$638m",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio: within CPFL Transmissão RS 2025–2029 ~R$3.9bn cycle, 2025 planned disbursement R$638 million. CapEx: enter R$638m 2025 face. Nested vs cpfl_tx_rs_3p9bn_2025_2029 cycle (not additive). UNVERIFIED press proxy quoting company.",
    "638000000", "2025-04-24", "2025", "-30.03", "-51.23",
    "CPFL Transmissão Rio Grande do Sul system (Porto Alegre / Canoas pin).",
    "jornal_comercio_cpfl_tx_rs_20250424",
    "Para 2025, está previsto um desembolso de R$ 638 milhões",
    "https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW nested RS 2025 CapEx R$638m (UNVERIFIED press). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle283", investment_type="corporate_capex", evidence="proxy", currency="BRL",
    value_usd=str(round(638000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html.',
    annotation="CPFL TX RS 2025 CapEx R$638m via Fed H.10 (UNVERIFIED press). Supports cpfl_tx_rs_2025_638m_brl.",
    evid_note="Opened Jornal do Comércio 24 Apr 2025; RS 2025 planned CapEx R$638m confirmed.",
)

# 3. power_plants_grid / prc — NEW CPFL Nova Prata 2 ~R$78m
row_doc(
    "cpfl_nova_prata_2_78m_brl_2025",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — Nova Prata 2 substation modernization ~R$78m",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio: CPFL Transmissão to finalize in H1 2025 modernization and expansion of Nova Prata 2 substation — investment of approximately R$78 million. CapEx: enter R$78m Nova Prata 2 face. Nested vs cpfl_tx_rs_3p9bn_2025_2029 / cpfl_tx_rs_2025_638m_brl (not additive). UNVERIFIED press proxy quoting company.",
    "78000000", "2025-04-24", "2025", "-28.68", "-51.61",
    "Nova Prata 2 substation / Rio Grande do Sul (Nova Prata pin).",
    "jornal_comercio_cpfl_tx_rs_20250424",
    "modernização e ampliação da subestação de Nova Prata 2, resultado de um investimento de aproximadamente R$ 78 milhões",
    "https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html",
    "Actor: CPFL Transmissão — prc. NEW Nova Prata 2 CapEx ~R$78m (UNVERIFIED press). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle283", investment_type="brownfield_expansion", evidence="proxy", currency="BRL",
    value_usd=str(round(78000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html.',
    annotation="CPFL Nova Prata 2 ~R$78m via Fed H.10 (UNVERIFIED press). Supports cpfl_nova_prata_2_78m_brl_2025.",
    evid_note="Opened Jornal do Comércio 24 Apr 2025; Nova Prata 2 ~R$78m CapEx quote confirmed.",
)

# 4. copper / other — NEW Southern Copper 2Q26 CapEx USD422.8m
row_doc(
    "southern_copper_2q26_capex_422p8m_usd",
    "resources", "copper", "other",
    "Southern Copper — 2Q26 capital investments USD422.8m",
    "Peru",
    "21 Jul 2026 Southern Copper Corp. 2Q26 earnings release (SEC exhibit): capital investments USD 422.8 million in 2Q26 (within 6M26 USD864.7m already nested). CapEx: enter USD422.8m 2Q26 face. Nested vs southern_copper_6m26_capex_864p7m_usd (not additive).",
    "422800000", "2026-06-30", "2026", "-16.62", "-71.87",
    "Southern Copper LatAm ops (Peru Toquepala/Cuajone pin; Mexico also in scope).",
    "scco_2q26_ex99_20260721",
    "In 2Q26, we spent $422.8 million on capital investments",
    "https://www.sec.gov/Archives/edgar/data/1001838/000110465926085515/scco-20260721xex99d1.htm",
    "Actor: Southern Copper (Grupo Mexico majority) — other. NEW nested 2Q26 CapEx USD422.8m. Shuffle copper.",
    "hunt_cycle283", investment_type="corporate_capex", evidence="documented", currency="USD",
    value_usd="422800000", fx_usd="1", bib_type="company",
    chicago='Southern Copper Corporation. “Southern Copper Corporation Reports 2Q26 Results” (SEC Exhibit 99.1). July 21, 2026. https://www.sec.gov/Archives/edgar/data/1001838/000110465926085515/scco-20260721xex99d1.htm.',
    annotation="Southern Copper 2Q26 CapEx USD422.8m SEC. Supports southern_copper_2q26_capex_422p8m_usd.",
    evid_note="Opened SCCO 2Q26 SEC Exhibit 99.1; 2Q26 capital investments $422.8m confirmed.",
)

# 5. rail / other — NEW Rumo Contêiner Expansão 6M26 R$32m
row_doc(
    "rumo_conteiner_expansao_6m26_32m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Contêiner Expansão CapEx 6M26 R$32m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Contêiner Expansão R$32 million in 6M26 (2T26 R$19m). CapEx: enter R$32m Contêiner Expansão 6M26 face. Nested vs rumo_conteiner_6m26_40m_brl total Contêiner (not additive).",
    "32000000", "2026-06-30", "2026", "-23.95", "-46.30",
    "Rumo/Brado container expansion (Santos corridor pin).",
    "rumo_2t26_release_20260812",
    "19 11 81,5 % Expansão 32 13 >100%",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Contêiner Expansão 6M26 CapEx R$32m. Shuffle rail.",
    "hunt_cycle283", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(32000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Contêiner Expansão 6M26 CapEx R$32m via Fed H.10. Supports rumo_conteiner_expansao_6m26_32m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Contêiner Expansão Capex 6M26 R$32m confirmed.",
)

# 6. water / other — NEW Aegea Corsan outorga 6M26 R$41m
row_doc(
    "aegea_corsan_outorga_6m26_41m_brl",
    "resources", "water", "other",
    "Aegea — Corsan outorga 6M26 R$41m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas table Corsan R$41 million in 6M26 (2T26 R$20m already nested). CapEx: enter R$41m Corsan outorga 6M26 face. Nested vs aegea_corsan_outorga_2t26_20m_brl / aegea_corsan_6m26_845m_brl Capex (not additive).",
    "41000000", "2026-06-30", "2026", "-30.03", "-51.23",
    "Corsan / Rio Grande do Sul concession outorga (Porto Alegre pin).",
    "aegea_2t26_6m26_release_mziq",
    "Corsan 20 30 -31,9% 41 82 -49,8%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Corsan outorga 6M26 R$41m. Shuffle water.",
    "hunt_cycle283", investment_type="concession_payment", evidence="documented", currency="BRL",
    value_usd=str(round(41000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Corsan outorga 6M26 R$41m via Fed H.10. Supports aegea_corsan_outorga_6m26_41m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Corsan outorga 6M26 R$41m confirmed.",
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
    print(f"cycle283 added {len(added)}: {added}")
    print(f"cycle283 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
