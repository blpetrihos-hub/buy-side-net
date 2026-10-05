#!/usr/bin/env python3
"""Cycle 293 hunt: shuffle_seed=20261293; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261293).shuffle):
graphite, power_plants_grid, other_renewables, balsa, port_ownership, port_cranes,
niobium, fission_smr, lithium, copper, wind, building_materials, solar, rail,
nickel, bridges_roads, water, engineering_epc.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: graphite CapEx-fill (Atlas/Graphcoa blanks); Arenales
  project CapEx blank; SSA Guaymas STS dollar blank (MXN424.8m already on TUM);
  Bechtel QB2 desal blank; Progress Rail VLI R$430m unsigned; DFC Honduras
  $10m microfinance out of taxonomy; USTDA Atlántico TA already logged CapEx-blank;
  Atlas $11.0m equity offering = financing not CapEx.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER / ALLIED: NEW Equatorial 2T26 nested AL/AP Ativos elétricos + OE, GO OE,
  nonelectric + Projetos Estratégicos by distributor; ISA Serra Dourada /
  Itatiaia Total Realizado CapEx; Jacarandá total + 2T26 spend.
Skipped: thin dry; graphite CapEx-fill dry; US CapEx dry streak continues;
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
EQ_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/"
    "b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2"
)
ISA_URL = (
    "https://ri.isaenergiabrasil.com.br/pt/documentos/"
    "6758-Earnings-Release-2T26-vfinal.pdf"
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


# --- Equatorial 2T26 nested (other) ---
# Columns MA PA PI AL RS AP GO — 2T26:
# eletricos 279/362/179/169/262/71/611 (AL/AP NEW; others cycle 292)
# OE 30/329/49/10/-/23/20 (AL/AP/GO NEW; RS dash skip)
# nonelectric 21/25/11/10/20/3/44
# Projetos Estratégicos 7/8/3/3/6/1/18 (nested under nonelectric aggregate R$46m)
for rid, name, line, val, lat, lon, geo, quote in [
    ("equatorial_al_eletricos_2t26_169m_brl", "Equatorial Alagoas", "Ativos elétricos", 169000000, "-9.67", "-35.74", "Equatorial Alagoas (Maceió pin).", "Ativos elétricos … 169"),
    ("equatorial_al_oe_2t26_10m_brl", "Equatorial Alagoas", "Obrigações especiais", 10000000, "-9.67", "-35.74", "Equatorial Alagoas OE / PLPT (Maceió pin).", "Obrigações especiais … 10"),
    ("equatorial_ap_eletricos_2t26_71m_brl", "Equatorial Amapá (CEA)", "Ativos elétricos", 71000000, "0.03", "-51.07", "Equatorial Amapá / CEA (Macapá pin).", "Ativos elétricos … 71"),
    ("equatorial_ap_oe_2t26_23m_brl", "Equatorial Amapá (CEA)", "Obrigações especiais", 23000000, "0.03", "-51.07", "Equatorial Amapá OE / PLPT (Macapá pin).", "Obrigações especiais … 23"),
    ("equatorial_go_oe_2t26_20m_brl", "Equatorial Goiás", "Obrigações especiais", 20000000, "-16.69", "-49.25", "Equatorial Goiás OE / PLPT (Goiânia pin).", "Obrigações especiais … 20"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"{name} — {line} CapEx 2T26 R${val/1e6:.0f}m",
        "Brazil",
        f"12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras — {name} {line} 2T26 R${val/1e6:,.0f} million. CapEx: enter face. Nested under distributor Total / Dist Ativos elétricos R$1.933bn / OE R$460m (not additive).",
        str(val), "2026-08-12", "2026", lat, lon, geo,
        "equatorial_2t26_release_20260812", quote, EQ_URL,
        f"Actor: {name} — other. NEW 2T26 {line}. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
        annotation=f"{name} 2T26 {line} via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Equatorial 2T26 PDF; {name} {line} 2T26 R${val/1e6:,.0f}m confirmed.",
    )

for rid, name, line, val, lat, lon, geo, quote in [
    ("equatorial_ma_nonelectric_2t26_21m_brl", "Equatorial Maranhão", "Ativos não elétricos", 21000000, "-2.53", "-44.30", "Equatorial Maranhão (São Luís pin).", "Ativos não elétricos … 21"),
    ("equatorial_pa_nonelectric_2t26_25m_brl", "Equatorial Pará", "Ativos não elétricos", 25000000, "-1.46", "-48.50", "Equatorial Pará (Belém pin).", "Ativos não elétricos … 25"),
    ("equatorial_pi_nonelectric_2t26_11m_brl", "Equatorial Piauí", "Ativos não elétricos", 11000000, "-5.09", "-42.80", "Equatorial Piauí (Teresina pin).", "Ativos não elétricos … 11"),
    ("equatorial_al_nonelectric_2t26_10m_brl", "Equatorial Alagoas", "Ativos não elétricos", 10000000, "-9.67", "-35.74", "Equatorial Alagoas (Maceió pin).", "Ativos não elétricos … 10"),
    ("equatorial_rs_nonelectric_2t26_20m_brl", "Equatorial CEEE-D (RS)", "Ativos não elétricos", 20000000, "-30.03", "-51.23", "Equatorial CEEE-D (Porto Alegre pin).", "Ativos não elétricos … 20"),
    ("equatorial_ap_nonelectric_2t26_3m_brl", "Equatorial Amapá (CEA)", "Ativos não elétricos", 3000000, "0.03", "-51.07", "Equatorial Amapá / CEA (Macapá pin).", "Ativos não elétricos … 3"),
    ("equatorial_go_nonelectric_2t26_44m_brl", "Equatorial Goiás", "Ativos não elétricos", 44000000, "-16.69", "-49.25", "Equatorial Goiás (Goiânia pin).", "Ativos não elétricos … 44"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"{name} — {line} CapEx 2T26 R${val/1e6:.0f}m",
        "Brazil",
        f"12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras — {name} {line} 2T26 R${val/1e6:,.0f} million. CapEx: enter face. Nested under Dist Ativos não elétricos R$134m (not additive).",
        str(val), "2026-08-12", "2026", lat, lon, geo,
        "equatorial_2t26_release_20260812", quote, EQ_URL,
        f"Actor: {name} — other. NEW 2T26 {line}. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
        annotation=f"{name} 2T26 {line} via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Equatorial 2T26 PDF; {name} {line} 2T26 R${val/1e6:,.0f}m confirmed.",
    )

for rid, name, val, lat, lon, geo, quote in [
    ("equatorial_ma_projetos_2t26_7m_brl", "Equatorial Maranhão", 7000000, "-2.53", "-44.30", "Equatorial Maranhão (São Luís pin).", "Projetos Estratégicos … 7"),
    ("equatorial_pa_projetos_2t26_8m_brl", "Equatorial Pará", 8000000, "-1.46", "-48.50", "Equatorial Pará (Belém pin).", "Projetos Estratégicos … 8"),
    ("equatorial_pi_projetos_2t26_3m_brl", "Equatorial Piauí", 3000000, "-5.09", "-42.80", "Equatorial Piauí (Teresina pin).", "Projetos Estratégicos … 3"),
    ("equatorial_al_projetos_2t26_3m_brl", "Equatorial Alagoas", 3000000, "-9.67", "-35.74", "Equatorial Alagoas (Maceió pin).", "Projetos Estratégicos … 3"),
    ("equatorial_rs_projetos_2t26_6m_brl", "Equatorial CEEE-D (RS)", 6000000, "-30.03", "-51.23", "Equatorial CEEE-D (Porto Alegre pin).", "Projetos Estratégicos … 6"),
    ("equatorial_ap_projetos_2t26_1m_brl", "Equatorial Amapá (CEA)", 1000000, "0.03", "-51.07", "Equatorial Amapá / CEA (Macapá pin).", "Projetos Estratégicos … 1"),
    ("equatorial_go_projetos_2t26_18m_brl", "Equatorial Goiás", 18000000, "-16.69", "-49.25", "Equatorial Goiás (Goiânia pin).", "Projetos Estratégicos … 18"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"{name} — Projetos Estratégicos CapEx 2T26 R${val/1e6:.0f}m",
        "Brazil",
        f"12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras — {name} Projetos Estratégicos 2T26 R${val/1e6:,.0f} million. CapEx: enter face. Nested under Dist Projetos Estratégicos R$46m / Ativos não elétricos R$134m (not additive).",
        str(val), "2026-08-12", "2026", lat, lon, geo,
        "equatorial_2t26_release_20260812", quote, EQ_URL,
        f"Actor: {name} — other. NEW 2T26 Projetos Estratégicos. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
        annotation=f"{name} 2T26 Projetos Estratégicos via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Equatorial 2T26 PDF; {name} Projetos Estratégicos 2T26 R${val/1e6:,.0f}m confirmed.",
    )

row_doc(
    "equatorial_ativos_operacionais_2t26_48m_brl", "energy", "power_plants_grid", "other",
    "Equatorial — Ativos Operacionais CapEx 2T26 R$48m",
    "Brazil",
    "12 Aug 2026 Equatorial 2T26 release: Investimentos — Ativos Operacionais 2T26 R$48 million (vs R$21m 2T25). CapEx: enter face. Nested under Total Equatorial R$2.600bn (not additive to Dist).",
    "48000000", "2026-08-12", "2026", "-15.78", "-47.93",
    "Equatorial Group Brazil HQ pin (operational assets group-wide).",
    "equatorial_2t26_release_20260812", "Ativos Operacionais 21                    48", EQ_URL,
    "Actor: Equatorial S.A. — other. NEW 2T26 Ativos Operacionais. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(48000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
    annotation="Equatorial 2T26 Ativos Operacionais via Fed H.10. Supports equatorial_ativos_operacionais_2t26_48m_brl.",
    evid_note="Opened Equatorial 2T26 PDF; Ativos Operacionais 2T26 R$48m confirmed.",
)

# --- ISA Energia Brasil greenfield CapEx (allied) ---
ISA_CHICAGO = (
    'ISA Energia Brasil. “Earnings Release 2T26.” August 3, 2026. ' + ISA_URL + "."
)

row_doc(
    "isa_energia_serra_dourada_realized_1844p5m_brl", "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Serra Dourada Total Realizado CapEx R$1,844.5m (jun/26)",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil Earnings Release 2T26: CapEx Total do Projeto — Total Realizado ISA ENERGIA BRASIL for Serra Dourada (Lote 1, BA/MG) R$1,844.5 million (termos reais, data base jun/26); 49% avanço físico; Total ANEEL R$3,731.4m. CapEx: enter cumulative realized face. Distinct from 2T26 spend R$455.7m and prior ANEEL CapEx R$3.2bn news face.",
    "1844500000", "2026-08-03", "2026", "-11.09", "-43.14",
    "Serra Dourada transmission lot (BA/MG; prior Serra Dourada pin).",
    "isa_energia_2t26_earnings_release",
    "Serra Dourada (Lote 1) … Total Realizado ISA ENERGIA BRASIL … 1.844,5",
    ISA_URL,
    "Actor: ISA Energia Brasil (ISA/Colombia group) — allied. NEW cumulative realized CapEx. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1844500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=ISA_CHICAGO,
    annotation="ISA Serra Dourada Total Realizado via Fed H.10. Supports isa_energia_serra_dourada_realized_1844p5m_brl.",
    evid_note="Opened ISA 2T26 Earnings Release PDF; Serra Dourada Total Realizado R$1,844.5m confirmed.",
)

row_doc(
    "isa_energia_itatiaia_realized_549p7m_brl", "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Itatiaia Total Realizado CapEx R$549.7m (jun/26)",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil Earnings Release 2T26: CapEx Total do Projeto — Total Realizado ISA ENERGIA BRASIL for Itatiaia (Lote 7, RJ/MG) R$549.7 million (termos reais, data base jun/26); 33% avanço físico; Total ANEEL R$2,719.4m. CapEx: enter cumulative realized face. Distinct from 2T26 spend R$52.2m.",
    "549700000", "2026-08-03", "2026", "-22.50", "-44.56",
    "Itatiaia transmission lot RJ/MG (Itatiaia region pin).",
    "isa_energia_2t26_earnings_release",
    "Itatiaia (Lote 7) … Total Realizado ISA ENERGIA BRASIL … 549,7",
    ISA_URL,
    "Actor: ISA Energia Brasil (ISA/Colombia group) — allied. NEW cumulative realized CapEx. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(549700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=ISA_CHICAGO,
    annotation="ISA Itatiaia Total Realizado via Fed H.10. Supports isa_energia_itatiaia_realized_549p7m_brl.",
    evid_note="Opened ISA 2T26 Earnings Release PDF; Itatiaia Total Realizado R$549.7m confirmed.",
)

row_doc(
    "isa_energia_jacaranda_188p8m_brl", "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Jacarandá project CapEx ~R$188.8m",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil Earnings Release 2T26: Jacarandá (ANEEL Auction 01/2022 Lot 6; IE Jaguar 8; Subestação Água Azul expansion, SP) energized Apr 2026 — investimento total do projeto cerca de R$188.8 million (33% efficiency vs CapEx ANEEL updated 30 Mar 2026). CapEx: enter total project face. RAP ciclo 2026/2027 R$16.9m.",
    "188800000", "2026-08-03", "2026", "", "",
    "Jacarandá / Subestação Água Azul (SP; company UF SP; site coords not named — left blank).",
    "isa_energia_2t26_earnings_release",
    "O investimento total do projeto foi de cerca de R$ 188,8 milhões",
    ISA_URL,
    "Actor: ISA Energia Brasil (ISA/Colombia group) — allied. NEW Jacarandá total CapEx. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(188800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=ISA_CHICAGO,
    annotation="ISA Jacarandá total CapEx via Fed H.10. Supports isa_energia_jacaranda_188p8m_brl.",
    evid_note="Opened ISA 2T26 Earnings Release PDF; Jacarandá total ~R$188.8m confirmed.",
)

row_doc(
    "isa_energia_jacaranda_2t26_13p5m_brl", "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Jacarandá CapEx spend 2T26 R$13.5m",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil Earnings Release 2T26 Anexo II: Investimentos Greenfield 2T26 includes Jacarandá R$13.5 million (vs R$23.1m 2T25). CapEx: enter 2T26 spend face. Nested under licitados 2T26 R$608.1m / not additive to total project ~R$188.8m.",
    "13500000", "2026-08-03", "2026", "", "",
    "Jacarandá / Subestação Água Azul (SP; company UF SP; site coords not named — left blank).",
    "isa_energia_2t26_earnings_release",
    "Jacarandá 13,5 23,1 -41,5%",
    ISA_URL,
    "Actor: ISA Energia Brasil (ISA/Colombia group) — allied. NEW Jacarandá 2T26 spend. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle293", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(13500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=ISA_CHICAGO,
    annotation="ISA Jacarandá 2T26 spend via Fed H.10. Supports isa_energia_jacaranda_2t26_13p5m_brl.",
    evid_note="Opened ISA 2T26 Earnings Release PDF; Jacarandá 2T26 R$13.5m confirmed.",
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
    print(f"cycle293 added {len(added)}: {added}")
    print(f"cycle293 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
