#!/usr/bin/env python3
"""Cycle 183 hunt: shuffle_seed=20261183; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261183)):
power_plants_grid, niobium, rail, nickel, balsa, port_ownership, solar,
fission_smr, copper, building_materials, port_cranes, water, other_renewables,
lithium, graphite, engineering_epc, wind, bridges_roads.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (Plantabal/AIMA/WITS Ecuador balsa; Centaurus/BRN/Atlantic/
Fenix nickel; Meitner/Colombia/Peru FIRST fission already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. power_plants_grid / allied — ISA ENERGIA BRASIL IE Madeira 49% buyout
row_doc(
    "isa_energia_ie_madeira_49pct_1167m_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "ISA ENERGIA BRASIL — acquires remaining 49% of IE Madeira (net torna R$1.167bn)",
    "Brazil",
    "31 Jul 2026 AXIA Energia / AXIA Nordeste material fact: complete unwinding of cross-holdings with ISA Energia Brasil — sale of 49% equity in Interligação Elétrica do Madeira S.A. (IE Madeira) to ISA; AXIA Nordeste acquires ISA’s 51% in IE Garanhuns; AXIA receives net proceeds R$1.167 billion. ISA consolidates 100% of IE Madeira (2,385 km HVDC Porto Velho–Araraquara) from Aug 2026. CapEx / transaction face = R$1.167bn net balancing payment. Distinct from hitachi_rio_madeira_service_2025 and isa_energia_serra_dourada_3p2bn_2025.",
    "1167000000",
    "2026-07-31",
    "2026",
    "-8.76",
    "-63.90",
    "IE Madeira HVDC — Porto Velho (RO) rectifier reference pin (ISA geography; Araraquara inverter co-mentioned).",
    "axia_ie_madeira_unwind_20260731",
    "further to the material fact disclosed on March 19, 2026, and following the satisfaction of the applicable conditions precedent, they have completed, on this date, the unwinding of cross-holdings with ISA Energia Brasil S.A. (\"ISA Energia\") in the special purpose entities (SPEs) Interligação Elétrica do Madeira S.A. (\"IE Madeira\") and Interligação Elétrica Garanhuns S.A. (\"IE Garanhuns\"), through: i. The sale of the 49% equity interests held by AXIA Energia and AXIA Nordeste in IE Madeira to ISA Energia; ii. the acquisition by AXIA Nordeste of the 51% equity interest held by ISA Energia Brasil in IE Garanhuns; and iii. the receipt of net proceeds in the amount of R$1.167 billion.",
    "https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Material%20Fact%20-%20Unwinding%20of%20cross-holdings%20in%20transmission%20assets.pdf",
    "Actor: ISA ENERGIA BRASIL (Colombian ISA control) buyer — allied; AXIA Energia (Brazil) seller of 49%. Opened AXIA Latibex English material fact 31 Jul 2026. BRL stored without FX. Cross-checked ISA ENERGIA BRASIL Portuguese news (rounded R$1.2bn torna). Shuffle lead power_plants_grid.",
    "hunt_cycle183",
    investment_type="m_and_a",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='AXIA Energia S.A. / AXIA Energia Nordeste S.A. “Material Fact — Unwinding of cross-holdings in transmission assets.” July 31, 2026. https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Material%20Fact%20-%20Unwinding%20of%20cross-holdings%20in%20transmission%20assets.pdf.',
    annotation="AXIA: ISA acquires remaining 49% IE Madeira for net R$1.167bn. Supports isa_energia_ie_madeira_49pct_1167m_2026.",
    evid_note="Opened AXIA Latibex English material-fact PDF 2026-10-04; cross-checked ISA ENERGIA BRASIL Portuguese newsroom 31 Jul 2026.",
)

# 2. rail / allied — CAF La Dorada–Chiriguaná structured loan (proxy reprint of CAF press)
row_doc(
    "caf_dorada_chiriguana_200m_2026",
    "infrastructure",
    "rail",
    "allied",
    "CAF — structured loan up to USD 200m for La Dorada–Chiriguaná rail PPP",
    "Colombia",
    "1 Oct 2026 BNamericas reprint of CAF press: CAF Board approves structured loan equivalent in Colombian pesos of up to US$200 million to partially finance Central Railway Line Concession–La Dorada–Chiriguaná Railway Corridor PPP; funds for rehabilitation/construction, O&M, machinery/equipment, and repayment of CAF bridge loans approved April 2026. Promoters: Ortiz Construcciones y Proyectos; Transferport; CI Colombian Natural Resources. CapEx/financing face = USD 200m ceiling. Distinct from caf_medellin_santiago_metro_2024 rolling-stock row.",
    "200000000",
    "2026-10-01",
    "2026",
    "5.45",
    "-74.73",
    "La Dorada (Caldas) start of 526 km corridor toward Chiriguaná (Cesar) — approximate municipal pin.",
    "bnamericas_caf_dorada_chiriguana_20261001",
    "The Board of Directors of CAF —the development bank of Latin America and the Caribbean— approved a structured loan for the equivalent in Colombian pesos of up to US$200 million to partially finance the Central Railway Line Concession–La Dorada–Chiriguaná Railway Corridor project in Colombia. The funds will be used for rehabilitation and construction work, as well as for the operation and maintenance of the railway infrastructure.",
    "https://www.bnamericas.com/en/news/caf-approves-us200mn-for-the-colombian-railway-corridor-la-doradachiriguana",
    "Actor: CAF (LatAm multilateral development bank) — allied. UNVERIFIED proxy: BNamericas English reprint of CAF press (CAF.com primary for this corridor loan not retrieved). Shuffle rail slot.",
    "hunt_cycle183",
    investment_type="financing",
    evidence="proxy",
    bib_type="press",
    chicago='BNamericas. “CAF approves US$200mn for the Colombian railway corridor La Dorada–Chiriguaná.” October 1, 2026 (reprint of CAF press release). https://www.bnamericas.com/en/news/caf-approves-us200mn-for-the-colombian-railway-corridor-la-doradachiriguana.',
    annotation="BNamericas/CAF press reprint: up to USD 200m Dorada–Chiriguaná rail loan. Supports caf_dorada_chiriguana_200m_2026.",
    evid_note="Opened BNamericas English page labeled Press release CAF 2026-10-04; CAF.com primary for this tranche not located.",
)

# 3. bridges_roads / allied — Anillo Vial Periférico Lima land-acquisition financing
row_doc(
    "anillo_vial_periferico_190m_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "BBVA Perú / COFIDE / MUFG — USD 190m land-acquisition financing for Anillo Vial Periférico (Lima)",
    "Peru",
    "31 Aug 2026 Cuatrecasas: advises BBVA Perú, COFIDE, and MUFG Bank on USD 190 million financing to Sociedad Concesionaria Anillo Vial S.A.C. for Proyecto Anillo Vial Periférico PPP land acquisition/clearance (Sections 1 and 3), secured by cash-flow trust. Milbank: sponsors Acciona, Cintra and Sacyr. COFIDE Spanish press: COFIDE contributes US$63.3 million (~one-third of first close up to US$190m). CapEx/financing face = USD 190m first close. Distinct from sacyr_ruta_pie_de_monte_355m_2026.",
    "190000000",
    "2026-08-31",
    "2026",
    "-12.05",
    "-77.04",
    "Anillo Vial Periférico / Lima–Callao beltway (ProInversión geography; approximate metro pin).",
    "cuatrecasas_anillo_vial_190m_20260831",
    "Cuatrecasas has advised BBVA Perú, COFIDE, and MUFG Bank (Japón) on a USD 190 million financing made available to Sociedad Concesionaria Anillo Vial S.A.C. for a primary beltway project (“Proyecto Anillo Vial Periférico”), which is being developed under a public-private partnership structure. The financing proceeds will be used to fund the land acquisition and clearance phase of the project and are secured through a cash flow trust arrangement.",
    "https://www.cuatrecasas.com/en/global/art/bbva-peru-cofide-mufg-bank-close-usd-190-million-financing-deal-primary-beltway",
    "Actor: Acciona / Cintra / Sacyr concessionaire (Spain) with BBVA (Spain) / COFIDE (Peru) / MUFG (Japan) lenders — allied. Opened Cuatrecasas English primary 31 Aug 2026; cross-checked COFIDE PDF and Milbank sponsor note. Shuffle bridges_roads slot.",
    "hunt_cycle183",
    investment_type="financing",
    evidence="documented",
    bib_type="company",
    chicago='Cuatrecasas. “BBVA Perú, COFIDE, and MUFG Bank close USD 190 million financing deal for primary beltway.” August 31, 2026. https://www.cuatrecasas.com/en/global/art/bbva-peru-cofide-mufg-bank-close-usd-190-million-financing-deal-primary-beltway.',
    annotation="Cuatrecasas: USD 190m Anillo Vial Periférico land-acquisition financing. Supports anillo_vial_periferico_190m_2026.",
    evid_note="Opened Cuatrecasas English page 2026-10-04; cross-checked COFIDE Spanish PDF and Milbank sponsor advisory.",
)

# 4. bridges_roads / allied — Mota-Engil / Neo Invest Rota dos Sertões CapEx
row_doc(
    "mota_engil_rota_dos_sertoes_43bn_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "Mota-Engil / Neo Invest / Galápagos — Rota dos Sertões highway concession CapEx (~R$4.3bn)",
    "Brazil",
    "29 Sep 2026: ANTT signs 30-year concession contract with Concessionária 116 Sertões S.A. (Consórcio 116 Sertões: Neo Invest/Novonor, Portuguese Mota-Engil, Galápagos) for Rota dos Sertões — ~502 km BR-116/BA/PE + BR-324/BA (Feira de Santana–Salgueiro). Estradas report of ANTT project page: approximately R$4.3 billion infrastructure CapEx and R$4.4 billion O&M over the concession; auction won 28 May 2026 with 19.6% toll discount. CapEx = R$4.3bn infrastructure tranche (not full R$8.5bn incl. Opex). Distinct from mota_engil_santos_guaruja_6p8bn_2026.",
    "4300000000",
    "2026-09-29",
    "2026",
    "-12.27",
    "-38.97",
    "Rota dos Sertões / Feira de Santana (BA) corridor start toward Salgueiro (PE) — approximate pin.",
    "estradas_rota_dos_sertoes_antt_20260929",
    "A Agência Nacional de Transportes Terrestres (ANTT) assinou em 29 de setembro de 2026 o contrato de concessão da Rota dos Sertões, sistema rodoviário formado por trechos das BR-116 na Bahia e em Pernambuco e da BR-324 na Bahia. A concessão terá duração de 30 anos, contados a partir da assunção das rodovias pela nova operadora, a Concessionária 116 Sertões S.A.. O sistema concedido possui cerca de 502 quilômetros de extensão. … A página atual do projeto na ANTT indica aproximadamente R$ 4,3 bilhões em investimentos em infraestrutura (Capex) e R$ 4,4 bilhões em custos de operação e manutenção (Opex) ao longo da concessão.",
    "https://estradas.com.br/antt-assina-concessao-da-rota-dos-sertoes-por-30-anos-entre-bahia-e-pernambuco/",
    "Actor: Mota-Engil (Portugal) + Neo Invest/Novonor (Brazil) + Galápagos — allied (Mota-Engil coding consistent with Santos–Guarujá / QI rows). UNVERIFIED proxy: Estradas report of ANTT 29 Sep 2026 signing and ANTT CapEx figures. BRL stored without FX. Overflow bridges_roads after Anillo Vial.",
    "hunt_cycle183",
    investment_type="concession",
    evidence="proxy",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='Estradas. “ANTT assina concessão da Rota dos Sertões por 30 anos entre Bahia e Pernambuco.” September 30, 2026. https://estradas.com.br/antt-assina-concessao-da-rota-dos-sertoes-por-30-anos-entre-bahia-e-pernambuco/.',
    annotation="Estradas/ANTT: Rota dos Sertões ~R$4.3bn CapEx concession signing. Supports mota_engil_rota_dos_sertoes_43bn_2026.",
    evid_note="Opened Estradas Portuguese page 2026-10-04 citing ANTT 29 Sep 2026 contract signing and ANTT CapEx/Opex split; ANTT HTML primary partially retrieved.",
)

# Thin top-up + remaining shuffle slots dry: niobium, nickel, balsa, port_ownership,
# solar, fission_smr, copper, building_materials, port_cranes, water, other_renewables,
# lithium, graphite, engineering_epc, wind (catalog dense; ≥1/3 U.S. hunt budget spent —
# EXIM Guyana GTE / DFC Serra Verde / Fluor ICA / AES Andes / Nextracker Casa dos Ventos /
# Freeport El Abra / USTDA Ecuador CNEL-ARCONEL already logged; holdovers unsigned).


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
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle183 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
