#!/usr/bin/env python3
"""Cycle 300 hunt: shuffle_seed=20261300; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261300).shuffle):
copper, wind, water, port_ownership, balsa, engineering_epc, niobium, nickel,
graphite, bridges_roads, solar, building_materials, port_cranes,
power_plants_grid, lithium, fission_smr, other_renewables, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa fifth / nickel eighth / fission_smr sixteenth in shuffle).
≥1/3 U.S. hunt budget: AES Arenales CapEx blank (URL 404→home); SSA Guaymas
  404; Wabtec Vale CapEx blank; Progress Rail R$430m not on VLI page (R$200m /
  R$600m / MSA R$500m already logged); Fluor/FCX/Caterpillar CapEx-fill blanks;
  Bechtel 403.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Alupar CapEx Previsto USD (TES/TEL/SED/TEP/TSA/TER/Geral) + NEW
  Alupar TAP/TPC/TCN period cash CapEx 1T26/2T26 (quarterly visão caixa nested
  under CapEx Realizado cumulative).
OTHER: NEW Energisa Transmissão CapEx 2T26/6M26 + NEW Energisa (re)energisa
  CapEx 2T26/6M26 (GD / energy-services LoB → other_renewables).
Skipped: thin dry; Motiva/Aegea/ISA largely mined; gas Dist taxonomy-out;
  Alupar TECP CapEx figure still not separately disclosed beyond RAP/debt;
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
ALUPAR_URL = "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip"
ALUPAR_CHICAGO = (
    'Alupar Investimento S.A. “Release de Resultados 2T26” (RI ZIP). August 6, 2026. '
    + ALUPAR_URL + "."
)
ENERGISA_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/60f49a2d-bd8c-4fd9-95ab-bdf833097a83/"
    "c4a851a2-10c3-3c55-3d68-fcf7f6306b96?origin=2"
)
ENERGISA_CHICAGO = (
    'Energisa S.A. “Release de Resultados 2T26.” August 6, 2026. ' + ENERGISA_URL + "."
)


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


# --- Alupar CapEx Previsto USD (TES TEL SED TEP TSA TER Geral) ---
# País: PER CHL COL CHL PER PER PER
for rid, name, country, val_m, chars, geo, quote in [
    ("alupar_tes_capex_previsto_38p9m_usd", "TES", "Peru", 38.9,
     "1 SE + LT 9 km", "Alupar TES transmission (Peru; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 38,9"),
    ("alupar_tel_capex_previsto_40m_usd", "TEL", "Chile", 40.0,
     "2 SEs + LT 15.7 km", "Alupar TEL transmission (Chile; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 40,0"),
    ("alupar_sed_capex_previsto_45p2m_usd", "SED", "Colombia", 45.2,
     "3 SEs + LT 100 km", "Alupar SED transmission (Colombia; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 45,2"),
    ("alupar_tep_capex_previsto_145p9m_usd", "TEP", "Chile", 145.9,
     "2 SEs + synchronous compensators", "Alupar TEP transmission (Chile; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 145,9"),
    ("alupar_tsa_capex_previsto_19p6m_usd", "TSA", "Peru", 19.6,
     "LT 9.5 km + 3 SEs", "Alupar TSA transmission (Peru; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 19,6"),
    ("alupar_ter_capex_previsto_400p2m_usd", "TER", "Peru", 400.2,
     "LT 176.5 km + 6 SEs", "Alupar TER transmission (Peru; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 400,2"),
    ("alupar_geral_capex_previsto_42p8m_usd", "Geral", "Peru", 42.8,
     "LT 76.0 km + 2 SEs", "Alupar Geral transmission (Peru; site coords not named — left blank).",
     "CAPEX Previsto (MM) … US$ 42,8"),
]:
    val = int(round(val_m * 1_000_000))
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"Alupar — {name} CapEx Previsto USD{val_m}m (2T26 table)",
        country,
        f"6 Aug 2026 Alupar Investimento 2T26 earnings release: Projetos de Transmissão em Implantação — {name} ({country}; {chars}) CAPEX Previsto US${val_m} million. CapEx: enter planned envelope. Distinct from CapEx Realizado USD face already logged for same project; parallel to Brazil TAP/TPC/TCN CapEx Previsto BRL faces.",
        str(val), "2026-08-06", "2026", "", "", geo,
        "alupar_2t26_release_20260806", quote, ALUPAR_URL,
        f"Actor: Alupar Investimento — allied. NEW {name} CapEx Previsto USD. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle300", investment_type="corporate_capex", evidence="documented", currency="USD",
        value_usd=str(val), fx_usd="1", bib_type="company",
        chicago=ALUPAR_CHICAGO,
        annotation=f"Alupar {name} CapEx Previsto USD. Supports {rid}.",
        evid_note=f"Opened Alupar 2T26 RI ZIP PDF; {name} CapEx Previsto US${val_m}m confirmed.",
    )


# --- Alupar TAP/TPC/TCN period cash CapEx (visão caixa quarterly) nested under Realizado ---
for rid, name, period, val_m, quote in [
    ("alupar_tap_capex_1t26_45p59m_brl", "TAP", "1T26", 45.59, "R$ 45,59 … 1T26"),
    ("alupar_tap_capex_2t26_41p55m_brl", "TAP", "2T26", 41.55, "R$ 41,55 … 2T26"),
    ("alupar_tpc_capex_1t26_50p79m_brl", "TPC", "1T26", 50.79, "R$ 50,79 … 1T26"),
    ("alupar_tpc_capex_2t26_113p01m_brl", "TPC", "2T26", 113.01, "R$ 113,01 … 2T26"),
    ("alupar_tcn_capex_1t26_9p17m_brl", "TCN", "1T26", 9.17, "R$ 9,17 … 1T26"),
    ("alupar_tcn_capex_2t26_9p61m_brl", "TCN", "2T26", 9.61, "R$ 9,61 … 2T26"),
]:
    val = int(round(val_m * 1_000_000))
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"Alupar — {name} CapEx {period} R${val_m}m (visão caixa)",
        "Brazil",
        f"6 Aug 2026 Alupar Investimento 2T26 earnings release: Investimentos nos Projetos em Andamento (visão caixa, consonant with CAPEX Realizado) — {name} {period} R${val_m} million. CapEx: enter period cash face. Nested under {name} CapEx Realizado cumulative; distinct from CapEx Previsto envelope.",
        str(val), "2026-08-06", "2026", "-15.78", "-47.93",
        f"Alupar {name} transmission project Brazil (Brasília HQ pin).",
        "alupar_2t26_release_20260806", quote, ALUPAR_URL,
        f"Actor: Alupar Investimento — allied. NEW {name} {period} cash CapEx. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle300", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=ALUPAR_CHICAGO,
        annotation=f"Alupar {name} {period} CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Alupar 2T26 RI ZIP PDF; {name} {period} cash CapEx R${val_m}m confirmed.",
    )


# --- Energisa Transmissão CapEx (other) ---
ENERGISA_URL_NOTE = ENERGISA_URL
for rid, period, val_m, quote in [
    ("energisa_tx_2t26_63m_brl", "2T26", 63, "Transmissão de energia elétrica 63 … 2T26"),
    ("energisa_tx_6m26_100m_brl", "6M26", 100, "Transmissão de energia elétrica … 100 … 6M26"),
]:
    val = int(val_m * 1_000_000)
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"Energisa — Transmissão CapEx {period} R${val_m}m",
        "Brazil",
        f"6 Aug 2026 Energisa S.A. Release de Resultados 2T26: Investimentos por Linha de Negócio — Transmissão de energia elétrica {period} R${val_m} million. CapEx: enter TX LoB face. Nested under consolidated CapEx R$1.713bn 2T26 / R$3.267bn 6M26; distinct from Dist R$1.568bn / R$3.022bn already logged. Natural-gas Dist taxonomy-out (not entered).",
        str(val), "2026-08-06", "2026", "-21.39", "-42.70",
        "Energisa Group HQ Cataguases, MG pin.",
        "energisa_2t26_release_20260806", quote, ENERGISA_URL,
        f"Actor: Energisa — other. NEW TX CapEx {period}. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle300", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=ENERGISA_CHICAGO,
        annotation=f"Energisa TX {period} CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Energisa 2T26 MZ IQ PDF; TX CapEx {period} R${val_m}m confirmed.",
    )


# --- Energisa (re)energisa CapEx (other_renewables — GD / energy-services LoB) ---
for rid, period, val_m, quote in [
    ("energisa_reenergisa_2t26_36m_brl", "2T26", 36, "(re)energisa 36 … 2T26"),
    ("energisa_reenergisa_6m26_72m_brl", "6M26", 72, "(re)energisa … 72 … 6M26"),
]:
    val = int(val_m * 1_000_000)
    row_doc(
        rid, "energy", "other_renewables", "other",
        f"Energisa — (re)energisa CapEx {period} R${val_m}m",
        "Brazil",
        f"6 Aug 2026 Energisa S.A. Release de Resultados 2T26: Investimentos por Linha de Negócio — (re)energisa {period} R${val_m} million. CapEx: enter energy-services / distributed-generation LoB face (release highlights Geração Distribuída growth within (re)energisa). Nested under consolidated CapEx; distinct from Dist and TX LoB faces. Holdings/outros and gas Dist not entered.",
        str(val), "2026-08-06", "2026", "-21.39", "-42.70",
        "Energisa Group HQ Cataguases, MG pin.",
        "energisa_2t26_release_20260806", quote, ENERGISA_URL,
        f"Actor: Energisa — other. NEW (re)energisa CapEx {period}. Shuffle other_renewables; other equal-budget.",
        "hunt_cycle300", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=ENERGISA_CHICAGO,
        annotation=f"Energisa (re)energisa {period} CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Energisa 2T26 MZ IQ PDF; (re)energisa CapEx {period} R${val_m}m confirmed.",
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
    print(f"cycle300 added {len(added)}: {added}")
    print(f"cycle300 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
