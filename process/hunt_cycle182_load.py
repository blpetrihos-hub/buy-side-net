#!/usr/bin/env python3
"""Cycle 182 hunt: shuffle_seed=20261182; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261182)):
solar, other_renewables, fission_smr, niobium, nickel, port_cranes,
power_plants_grid, engineering_epc, rail, water, lithium, port_ownership,
balsa, wind, copper, graphite, bridges_roads, building_materials.

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


# 1. other_renewables / allied — Grenergy Gabriela Phase 4 sale to CVC DIF
row_doc(
    "grenergy_gabriela_cvc_dif_475m_2026",
    "energy",
    "other_renewables",
    "allied",
    "Grenergy → CVC DIF — Gabriela / Oasis de Atacama Phase 4 hybrid sale (EV USD 475m)",
    "Chile",
    "2 Sep 2026 Grenergy English: completes sale of Gabriela (fourth phase of Oasis de Atacama) to CVC DIF after COD; 272 MW solar + 1,100 MWh BESS; Enterprise Value US$475 million; 15-year hybrid PPA; construction financed by US$324m green loan (BNP Paribas, Natixis, SG, Scotiabank, SMBC, BofA, BBVA, JPMorgan, KfW IPEX, Rabobank, ICO); Grenergy retains 5-year O&M. Combined with ContourGlobal (KKR) first-phase sale ~25% of Oasis platform / ~US$1.5bn EV. CapEx = USD 475m EV. Distinct from contourglobal_oasis_atacama_ev_2024 and byd_grenergy_* BESS supply rows.",
    "475000000",
    "2026-09-02",
    "2026",
    "",
    "",
    "Gabriela / Oasis de Atacama Phase 4, northern Chile (Grenergy geography) — lat/lon blank (commune not named on opened page).",
    "grenergy_gabriela_cvc_dif_20260902",
    "Grenergy has completed the sale of Gabriela, the fourth phase of Oasis de Atacama, its flagship energy storage project in Chile, to CVC DIF. Gabriela has 272 MW of installed solar capacity and 1,100 MWh of energy storage. The project is now operational, marking the completion of the transaction, which was announced in September 2025. The transaction’s Enterprise Value (EV) amounted to US$475 million.",
    "https://grenergy.eu/grenergy-completes-the-sale-of-the-fourth-phase-of-oasis-de-atacama-for-us475-million/",
    "Actor: Grenergy (Spain seller) / CVC DIF (infrastructure buyer) — allied. Opened Grenergy English press 2 Sep 2026. Coded other_renewables for hybrid solar-plus-storage asset rotation (same convention as ContourGlobal Oasis EV). Shuffle lead other_renewables.",
    "hunt_cycle182",
    investment_type="m_and_a",
    evidence="documented",
    bib_type="company",
    chicago='Grenergy. “Grenergy completes the sale of the fourth phase of Oasis de Atacama for $475 million.” September 2, 2026. https://grenergy.eu/grenergy-completes-the-sale-of-the-fourth-phase-of-oasis-de-atacama-for-us475-million/.',
    annotation="Grenergy: Gabriela Phase 4 sale to CVC DIF at USD 475m EV. Supports grenergy_gabriela_cvc_dif_475m_2026.",
    evid_note="Opened Grenergy English press release 2026-10-04.",
)

# 2. engineering_epc / us — Fluor ICA-Fluor Daniel Mexico JV divestiture
row_doc(
    "fluor_ica_fluor_daniel_divest_175m_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Fluor — divestiture of equity stake in ICA-Fluor Daniel Mexico JV (USD 175m)",
    "Mexico",
    "16 Jul 2026 Fluor: divests equity stake in ICA-Fluor Daniel to existing JV partner ICA for USD 175 million. JV formed 1993; completed numerous Mexico oil and gas, power, mining and manufacturing projects. Fluor retains ability to support ICA on a project-by-project basis. CapEx / transaction face = USD 175m. Distinct from fluor_salares_norte_chile_2024 / fluor_toromocho_expansion_peru / fluor_quellaveco_epcm_peru project rows.",
    "175000000",
    "2026-07-16",
    "2026",
    "",
    "",
    "ICA-Fluor Daniel Mexico JV footprint (nationwide EPC presence) — lat/lon blank (corporate equity exit; no single named site).",
    "fluor_ica_fluor_daniel_20260716",
    "Fluor Corporation (NYSE: FLR) announced today that it has divested its equity stake in ICA-Fluor Daniel to its existing JV Partner, ICA for $175 million. “Since the joint venture was formed in 1993, Fluor and ICA have successfully completed numerous projects in support of Mexico’s oil and gas, power, mining and manufacturing markets,” said Jim Breuer, Fluor’s Chief Executive Officer.",
    "https://newsroom.fluor.com/news-releases/news-details/2026/Fluor-Divests-Equity-Stake-in-Mexico-JV/default.aspx",
    "Actor: Fluor Corporation (U.S.) — us. Opened Fluor newsroom English primary 16 Jul 2026. U.S. side-balance engineering_epc (Mexico JV equity exit).",
    "hunt_cycle182",
    investment_type="m_and_a",
    evidence="documented",
    bib_type="company",
    chicago='Fluor Corporation. “Fluor Divests Equity Stake in Mexico JV.” July 16, 2026. https://newsroom.fluor.com/news-releases/news-details/2026/Fluor-Divests-Equity-Stake-in-Mexico-JV/default.aspx.',
    annotation="Fluor: USD 175m ICA-Fluor Daniel Mexico JV equity divestiture. Supports fluor_ica_fluor_daniel_divest_175m_2026.",
    evid_note="Opened Fluor English newsroom release 2026-10-04.",
)

# 3. bridges_roads / allied — Sacyr Ruta Pie de Monte Chile concession
row_doc(
    "sacyr_ruta_pie_de_monte_355m_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "Sacyr Concesiones Chile — Concesión Vial Ruta Pie de Monte (USD 355m / UF 9.145m)",
    "Chile",
    "24 Jun 2026 MOP / DGC: Diario Oficial publishes Decreto Supremo adjudicating Concesión Vial Ruta Pie de Monte (Biobío) to Sacyr Concesiones Chile SpA; estimated investment US$355 million (UF 9.145.000); ~20 km dual-carriageway alternative to Ruta 160 between San Pedro de la Paz and Coronel; construction targeted 2030 / operation 2034; free-flow electronic tolling; tsunami evacuation routes. CapEx = USD 355m official investment estimate. Distinct from other Sacyr Chile road concessions.",
    "355000000",
    "2026-06-24",
    "2026",
    "-36.95",
    "-73.08",
    "Ruta Pie de Monte corridor San Pedro de la Paz–Coronel, Biobío Region (MOP geography; approximate mid-corridor pin).",
    "mop_ruta_pie_de_monte_20260624",
    "Este miércoles 24 de junio fue publicado en el Diario Oficial el Decreto Supremo que adjudica el proyecto Concesión Vial Ruta Pie de Monte, en la región del Biobío, a la empresa Sacyr Concesiones Chile SPA. La obra considera una inversión estimada de US$355 millones (UF 9.145.000) y permitirá mejorar la conectividad y seguridad vial en la Región del Biobío a través de una nueva autopista de 20 kilómetros en doble calzada.",
    "https://concesiones.mop.gob.cl/mop-adjudica-nueva-concesion-ruta-pie-de-monte-en-biobio-por-una-inversion-de-355-millones-de-dolares/",
    "Actor: Sacyr Concesiones Chile SpA (Spain) — allied. Opened MOP DGC Spanish primary 24 Jun 2026. Shuffle bridges_roads slot.",
    "hunt_cycle182",
    investment_type="concession",
    evidence="documented",
    bib_type="official",
    chicago='Ministerio de Obras Públicas / Dirección General de Concesiones (Chile). “MOP adjudica nueva concesión ‘Ruta Pie de Monte’ en Biobío por una inversión de 355 millones de dólares.” June 24, 2026. https://concesiones.mop.gob.cl/mop-adjudica-nueva-concesion-ruta-pie-de-monte-en-biobio-por-una-inversion-de-355-millones-de-dolares/.',
    annotation="MOP DGC: Sacyr Ruta Pie de Monte USD 355m (UF 9.145m). Supports sacyr_ruta_pie_de_monte_355m_2026.",
    evid_note="Opened MOP DGC Spanish press page 2026-10-04; cross-checked Sacyr company formalization page.",
)

# 4. copper / allied — Sandvik Marmato underground fleet (hard-rock UG equipment convention)
row_doc(
    "sandvik_marmato_ug_sek250m_2026",
    "resources",
    "copper",
    "allied",
    "Sandvik — underground mining equipment for Aris Mining Marmato (~SEK 250m)",
    "Colombia",
    "1 Apr 2026 Sandvik AB: major underground mining equipment order from Canadian miner Aris Mining for Marmato gold mine (Colombia); valued around SEK 250 million, booked Q1 2026; underground trucks, loaders and drill rigs; deliveries Q2 2026 through Q2 2027 plus maintenance/repair services. CapEx = SEK 250m. Coded copper as underground hard-rock mining equipment (catalog convention for Sandvik/Epiroc mine fleets; Marmato is gold). Distinct from sandvik_cominvi_mexico_sek340m_2026 / sandvik_alumbrera_dr413i_3_2026.",
    "250000000",
    "2026-04-01",
    "2026",
    "5.475",
    "-75.601",
    "Marmato underground gold mine, Caldas Department (Sandvik / Aris Mining geography; approximate municipal pin).",
    "sandvik_marmato_aris_20260401",
    "Sandvik has received a major order for underground mining equipment from the Canadian mining company Aris Mining, to be used at the Marmato gold mine in Colombia. The order is valued at around SEK 250 million and was booked in the first quarter of 2026. The order consists of underground trucks, loaders and drill rigs, with deliveries expected to begin in the second quarter of 2026 and continue through the second quarter of 2027.",
    "https://www.home.sandvik/en/news-and-media/news/2026/04/sandvik-wins-large-underground-mining-equipment-order-in-colombia/",
    "Actor: Sandvik (Sweden) — allied; Aris Mining (Canada) host. Opened Sandvik Group English primary 1 Apr 2026. SEK stored without FX. Shuffle copper slot.",
    "hunt_cycle182",
    investment_type="equipment_supply",
    evidence="documented",
    currency="SEK",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Sandvik AB. “Sandvik wins large underground mining equipment order in Colombia.” April 1, 2026. https://www.home.sandvik/en/news-and-media/news/2026/04/sandvik-wins-large-underground-mining-equipment-order-in-colombia/.',
    annotation="Sandvik: ~SEK 250m Marmato underground fleet for Aris Mining. Supports sandvik_marmato_ug_sek250m_2026.",
    evid_note="Opened Sandvik Group English press 2026-10-04.",
)

# Thin top-up + remaining shuffle slots dry: solar, fission_smr, niobium, nickel,
# port_cranes, power_plants_grid, rail, water, lithium, port_ownership, balsa, wind,
# graphite, building_materials (catalog dense; holdovers unsigned; Sungrow Observatorio /
# CATL La Alegría / EXIM Guyana GTE / DFC Serra Verde / AES Pampas already logged).


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
    print(f"cycle182 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
