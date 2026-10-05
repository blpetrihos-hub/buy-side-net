#!/usr/bin/env python3
"""Cycle 290 hunt: shuffle_seed=20261290; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261290).shuffle):
engineering_epc, port_cranes, wind, water, rail, building_materials, balsa,
graphite, fission_smr, port_ownership, niobium, nickel, copper, lithium,
power_plants_grid, solar, bridges_roads, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: AES Andes Arenales CapEx-fill still blank; SSA Guaymas STS
  CapEx blank; FCX El Abra/Cerro Verde company pages CapEx-blank; USTDA CNEL grant
  $ blank; Equinix/Progress Rail holdovers — no new US CapEx face.
PRC equal-budget: Goldwind/Sungrow/BYD/CTG CapEx-blank COD faces.
ALLIED: NEW Neoenergia 6M26 CapEx by distributor (Coelba/PE/Cosern/Elektro/Brasília);
  NEW ISA Energia 2T26 R&M energized R$290.8m.
OTHER: NEW Equatorial PI/AL/RS/AP 2T26 Totals; NEW Cemig 2026 plan R$6.725bn nested
  (Dist/Gen/Tx/GD; gás taxonomy-out).
Skipped: thin dry; engineering_epc/port_cranes/wind/water/rail/building_materials/
  balsa/graphite/fission_smr/port_ownership/niobium/nickel/copper/lithium/solar/
  bridges_roads dense or CapEx-blank; Cemig Gasmig plan R$227m taxonomy-out;
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
NEO_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/"
    "145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2"
)
ISA_URL = (
    "https://ri.isaenergiabrasil.com.br/pt/documentos/"
    "6758-Earnings-Release-2T26-vfinal.pdf"
)
EQ_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/"
    "b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2"
)
CEMIG_URL = "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf"


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


# Neoenergia 6M26 CapEx by distributor (allied) — order Coelba, PE, Cosern, Elektro, Brasília
for rid, name, val, lat, lon, geo, quote_frag in [
    ("neoenergia_coelba_capex_6m26_1919m_brl", "Neoenergia Coelba", 1919000000, "-12.97", "-38.51", "Neoenergia Coelba (Salvador pin).", "CAPEX … 1.919"),
    ("neoenergia_pe_capex_6m26_746m_brl", "Neoenergia Pernambuco", 746000000, "-8.05", "-34.88", "Neoenergia Pernambuco (Recife pin).", "CAPEX … 746"),
    ("neoenergia_cosern_capex_6m26_240m_brl", "Neoenergia Cosern", 240000000, "-5.79", "-35.21", "Neoenergia Cosern (Natal pin).", "CAPEX … 240"),
    ("neoenergia_elektro_capex_6m26_564m_brl", "Neoenergia Elektro", 564000000, "-23.55", "-46.63", "Neoenergia Elektro (São Paulo pin).", "CAPEX … 564"),
    ("neoenergia_brasilia_capex_6m26_228m_brl", "Neoenergia Brasília", 228000000, "-15.78", "-47.93", "Neoenergia Brasília (Brasília pin).", "CAPEX … 228"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"{name} — CapEx 6M26 R${val/1e6:.0f}m",
        "Brazil",
        f"21 Jul 2026 Neoenergia 2T26/6M26 release: Distribuição CapEx by distributor — {name} CAPEX 6M26 R${val/1e6:,.0f} million (columns Coelba/PE/Cosern/Elektro/Brasília; consolidado R$3,696m). CapEx: enter face. Nested under Dist CapEx R$3.696bn (not additive).",
        str(val), "2026-07-21", "2026", lat, lon, geo,
        "neoenergia_2q26_release_mziq", quote_frag, NEO_URL,
        f"Actor: {name} (Iberdrola) — allied. NEW 6M26 CapEx. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + ".",
        annotation=f"{name} 6M26 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Neoenergia 2T26/6M26 PDF; {name} CAPEX 6M26 R${val/1e6:,.0f}m confirmed.",
    )

# ISA R&M energized 2T26 (allied)
row_doc(
    "isa_energia_2t26_rm_energized_290p8m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — R&M projects energized 2T26 R$290.8m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: replaced 312 equipment units and energized 16 R&M projects (13 small / 3 large) in 2T26 with total investment R$290.8 million. CapEx: enter R$290.8m energized face. Nested under 2T26 R&M R$445.4m (not additive).",
    "290800000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil R&M energized projects (São Paulo HQ pin).",
    "isa_energia_2t26_earnings_release",
    "com investimento total de R$ 290,8 milhões",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW 2T26 R&M energized R$290.8m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle290", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(290800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA 2T26 R&M energized R$290.8m via Fed H.10. Supports isa_energia_2t26_rm_energized_290p8m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; R&M energized 2T26 R$290.8m confirmed.",
)

# Equatorial remaining distributors (other)
for rid, name, val, lat, lon, geo in [
    ("equatorial_pi_2t26_239m_brl", "Equatorial Piauí", 239000000, "-5.09", "-42.80", "Equatorial Piauí (Teresina pin)."),
    ("equatorial_al_2t26_188m_brl", "Equatorial Alagoas", 188000000, "-9.67", "-35.74", "Equatorial Alagoas (Maceió pin)."),
    ("equatorial_rs_2t26_282m_brl", "Equatorial CEEE-D (RS)", 282000000, "-30.03", "-51.23", "Equatorial CEEE-D Rio Grande do Sul (Porto Alegre pin)."),
    ("equatorial_ap_2t26_97m_brl", "Equatorial Amapá (CEA)", 97000000, "0.03", "-51.07", "Equatorial Amapá / CEA (Macapá pin)."),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"{name} — Distribuição CapEx Total 2T26 R${val/1e6:.0f}m",
        "Brazil",
        f"12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras Total 2T26 R${val/1e6:,.0f} million for {name}. CapEx: enter face. Nested under Dist Total R$2.527bn (not additive).",
        str(val), "2026-08-12", "2026", lat, lon, geo,
        "equatorial_2t26_release_20260812", f"Total … {val//1000000}", EQ_URL,
        f"Actor: {name} — other. NEW 2T26 Total CapEx. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
        annotation=f"{name} 2T26 Total via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Equatorial 2T26 PDF; {name} Total 2T26 R${val/1e6:,.0f}m confirmed.",
    )

# Cemig 2026 plan nested (other) — company release chart Planejamento 2026 R$6,725m
row_doc(
    "cemig_2026_capex_plan_6725m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — 2026 investment plan R$6.725bn",
    "Brazil",
    "14 Aug 2026 Cemig 2T26 results materials: between 2026 and 2030 planned investments R$43.70bn, of which R$6.725 billion in 2026 (chart Planejamento 2026). CapEx: enter R$6.725bn face. Nested vs multi-year R$43.7/44bn plan (not additive).",
    "6725000000", "2026-08-14", "2026", "-19.92", "-43.94",
    "Cemig Minas Gerais portfolio (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "Planejamento 2026: Investimento de R$6.725 milhões",
    CEMIG_URL,
    "Actor: Cemig — other. NEW 2026 plan R$6.725bn. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(6725000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais — CEMIG. “Resultados 2T26” materials. August 2026. ' + CEMIG_URL + ".",
    annotation="Cemig 2026 plan R$6.725bn via Fed H.10. Supports cemig_2026_capex_plan_6725m_brl.",
    evid_note="Opened Cemig 2T26 results PDF; Planejamento 2026 R$6.725m confirmed.",
)

row_doc(
    "cemig_2026_dist_plan_5269m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — 2026 Distribuição CapEx plan R$5.269bn",
    "Brazil",
    "14 Aug 2026 Cemig 2T26 results materials: Planejamento 2026 chart — Distribuição R$5,269 million of R$6,725m total. CapEx: enter R$5.269bn face. Nested under 2026 plan (not additive). Gás slice taxonomy-out.",
    "5269000000", "2026-08-14", "2026", "-19.92", "-43.94",
    "Cemig Distribuição Minas Gerais (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "5.269 … Planejamento 2026 … Distribuição",
    CEMIG_URL,
    "Actor: Cemig D — other. NEW 2026 Dist plan R$5.269bn. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(5269000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais — CEMIG. “Resultados 2T26” materials. August 2026. ' + CEMIG_URL + ".",
    annotation="Cemig 2026 Dist plan R$5.269bn via Fed H.10. Supports cemig_2026_dist_plan_5269m_brl.",
    evid_note="Opened Cemig 2T26 results PDF; Distribuição Planejamento 2026 R$5,269m confirmed.",
)

row_doc(
    "cemig_2026_tx_plan_632m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — 2026 Transmissão CapEx plan R$632m",
    "Brazil",
    "14 Aug 2026 Cemig 2T26 results materials: Planejamento 2026 chart — Transmissão R$632 million of R$6,725m total. CapEx: enter R$632m face. Nested under 2026 plan (not additive).",
    "632000000", "2026-08-14", "2026", "-19.92", "-43.94",
    "Cemig Geração e Transmissão (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "632 … Planejamento 2026 … Transmissão",
    CEMIG_URL,
    "Actor: Cemig GT — other. NEW 2026 Tx plan R$632m. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(632000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais — CEMIG. “Resultados 2T26” materials. August 2026. ' + CEMIG_URL + ".",
    annotation="Cemig 2026 Tx plan R$632m via Fed H.10. Supports cemig_2026_tx_plan_632m_brl.",
    evid_note="Opened Cemig 2T26 results PDF; Transmissão Planejamento 2026 R$632m confirmed.",
)

row_doc(
    "cemig_2026_gen_plan_197m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — 2026 Geração CapEx plan R$197m",
    "Brazil",
    "14 Aug 2026 Cemig 2T26 results materials: Planejamento 2026 chart — Geração R$197 million of R$6,725m total. CapEx: enter R$197m face. Nested under 2026 plan (not additive).",
    "197000000", "2026-08-14", "2026", "-19.92", "-43.94",
    "Cemig generation portfolio (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "197 … Planejamento 2026 … Geração",
    CEMIG_URL,
    "Actor: Cemig GT — other. NEW 2026 Gen plan R$197m. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(197000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais — CEMIG. “Resultados 2T26” materials. August 2026. ' + CEMIG_URL + ".",
    annotation="Cemig 2026 Gen plan R$197m via Fed H.10. Supports cemig_2026_gen_plan_197m_brl.",
    evid_note="Opened Cemig 2T26 results PDF; Geração Planejamento 2026 R$197m confirmed.",
)

row_doc(
    "cemig_2026_gd_plan_375m_brl",
    "energy", "other_renewables", "other",
    "Cemig — 2026 Geração Distribuída CapEx plan R$375m",
    "Brazil",
    "14 Aug 2026 Cemig 2T26 results materials: Planejamento 2026 chart — Geração Distribuída R$375 million of R$6,725m total (Cemig Sim / distributed solar). CapEx: enter R$375m face. Nested under 2026 plan; distinct from Cemig Sim 2T26 UFV acquisition R$155m (not additive).",
    "375000000", "2026-08-14", "2026", "-19.92", "-43.94",
    "Cemig Sim distributed generation (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "375 … Planejamento 2026 … Geração Distribuída",
    CEMIG_URL,
    "Actor: Cemig Sim — other. NEW 2026 GD plan R$375m. Shuffle other_renewables; other equal-budget.",
    "hunt_cycle290", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(375000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Energética de Minas Gerais — CEMIG. “Resultados 2T26” materials. August 2026. ' + CEMIG_URL + ".",
    annotation="Cemig 2026 GD plan R$375m via Fed H.10. Supports cemig_2026_gd_plan_375m_brl.",
    evid_note="Opened Cemig 2T26 results PDF; Geração Distribuída Planejamento 2026 R$375m confirmed.",
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
    print(f"cycle290 added {len(added)}: {added}")
    print(f"cycle290 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
