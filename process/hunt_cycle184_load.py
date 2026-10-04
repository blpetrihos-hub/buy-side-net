#!/usr/bin/env python3
"""Cycle 184 hunt: shuffle_seed=20261184; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261184)):
lithium, fission_smr, port_ownership, other_renewables, niobium, bridges_roads,
water, engineering_epc, building_materials, solar, wind, nickel, power_plants_grid,
balsa, port_cranes, rail, copper, graphite.

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


# 1. other_renewables / allied — ENGIE Chile BESS Arica COD CapEx
row_doc(
    "engie_bess_arica_cod_51m_2026",
    "energy",
    "other_renewables",
    "allied",
    "ENGIE Chile — BESS Arica 25 MW / 150 MWh COD (stand-alone)",
    "Chile",
    "10 Jul 2026 ENGIE Chile: commercial operation of stand-alone BESS Arica (CEN authorization 25 Jun 2026) connected to Subestación Arica — COD page cites ~USD 50m and 25 MW / 150 MWh (36 Li-ion containers; 9 MVS); Dec 2025 construction release stated USD 51 million CapEx and design 34 MW / 170 MWh pre-COD. CapEx = USD 51m from construction primary (COD corroborates ~USD 50m). Distinct from engie_bess_libelula_cod_219m_2026 / engie_bess_los_loros_cod_64m_2026 / engie_bess_tocopilla_cod_170m_2026.",
    "51000000",
    "2025-12-02",
    "2026",
    "-18.48",
    "-70.32",
    "Subestación Arica / Región de Arica y Parinacota, Chile (ENGIE stand-alone BESS; approximate).",
    "engie_bess_arica_construccion_20251202",
    "Con una inversión de US$51 millones, BESS Arica forma parte de la hoja de ruta de transformación que ENGIE Chile está impulsando a nivel nacional",
    "https://www.engie.cl/avanzamos-en-la-construccion-del-proyecto-de-almacenamiento-bess-arica/",
    "Actor: ENGIE Chile (French ENGIE) — allied. Company Spanish construction primary for CapEx USD 51m; COD page 10 Jul 2026 corroborates commercial operation (~USD 50m / 25 MW/150 MWh). Shuffle other_renewables.",
    "hunt_cycle184",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='ENGIE Chile. “Avanzamos en la construcción del proyecto de almacenamiento BESS Arica.” December 2, 2025. https://www.engie.cl/avanzamos-en-la-construccion-del-proyecto-de-almacenamiento-bess-arica/.',
    annotation="ENGIE Chile: BESS Arica CapEx USD 51m. Supports engie_bess_arica_cod_51m_2026.",
    evid_note="Opened ENGIE Chile Spanish construction page 2026-10-04; cross-checked COD page https://www.engie.cl/mas-energia-renovable-para-chile-bess-arica-entra-en-operacion-comercial/ (10 Jul 2026).",
)

# 2. other_renewables / allied — ENGIE Chile BESS Kallpa CapEx
row_doc(
    "engie_bess_kallpa_69m_2026",
    "energy",
    "other_renewables",
    "allied",
    "ENGIE Chile — BESS Kallpa 57 MW / 285 MWh co-located at PE Kallpa (Taltal)",
    "Chile",
    "29 Jan 2026 ENGIE Chile: BESS Kallpa under construction (44% progress) co-located at Parque Eólico Kallpa (Taltal, Antofagasta) — 57 MW / 285 MWh; 70 battery containers; five-hour autonomy; CapEx USD 69 million; COD targeted 2H 2026; connects via wind-farm substation. First ENGIE Chile BESS integrated to a wind park. Distinct from engie_bess_arica_cod_51m_2026 / Los Loros / Libélula / Tocopilla.",
    "69000000",
    "2026-01-29",
    "2026",
    "-25.40",
    "-70.48",
    "Parque Eólico Kallpa / Taltal, Región de Antofagasta, Chile (company geography; approximate).",
    "engie_bess_kallpa_construccion_20260129",
    "BESS Kallpa considera una inversión de US$ 69 millones y tendrá una capacidad de 57 MW/285 MWh, mediante la instalación de 70 contenedores de baterías",
    "https://www.engie.cl/avanzamos-en-la-construccion-de-nuestro-primer-sistema-de-almacenamiento-integrado-a-un-parque-eolico-en-chile/",
    "Actor: ENGIE Chile (French ENGIE) — allied. Company Spanish primary. CapEx USD 69m. Shuffle other_renewables overflow.",
    "hunt_cycle184",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='ENGIE Chile. “Avanzamos en la construcción de nuestro primer sistema de almacenamiento integrado a un parque eólico en Chile.” January 29, 2026. https://www.engie.cl/avanzamos-en-la-construccion-de-nuestro-primer-sistema-de-almacenamiento-integrado-a-un-parque-eolico-en-chile/.',
    annotation="ENGIE Chile: BESS Kallpa CapEx USD 69m. Supports engie_bess_kallpa_69m_2026.",
    evid_note="Opened ENGIE Chile Spanish construction page 2026-10-04.",
)

# 3. other_renewables / allied — ENGIE Chile BESS Lile CapEx
row_doc(
    "engie_bess_lile_174m_2026",
    "energy",
    "other_renewables",
    "allied",
    "ENGIE Chile — BESS Lile 140 MW / 802 MWh at Complejo Térmico Mejillones",
    "Chile",
    "2 Oct 2025 ENGIE Chile announces BESS Lile stand-alone storage at Complejo Térmico de Mejillones (Antofagasta) — 140 MW / 802 MWh; 160 battery containers + 40 support units; COD targeted 2H 2026; reuses coal-complex transmission/substation. CapEx = USD 174 million from ENGIE Chile investor presentation (FY2025/H1 2026 decks) and contemporaneous La Tercera / pv magazine LatAm citing company. Distinct from Tocopilla / Arica / Kallpa / Los Loros / Libélula BESS rows.",
    "174000000",
    "2025-10-02",
    "2026",
    "-23.10",
    "-70.45",
    "Complejo Térmico de Mejillones, Región de Antofagasta, Chile (company geography; approximate).",
    "engie_chile_12m2025_presentation_bess_lile",
    "140MW BESS Lile US$174 million CAPEX",
    "https://www.engie.cl/wp-content/uploads/2024/10/12M2025-Presentation-ENGIE-CHILE-VF.pdf",
    "Actor: ENGIE Chile (French ENGIE) — allied. Company investor-deck primary for CapEx USD 174m; announcement page confirms scope/COD without USD. Shuffle other_renewables overflow.",
    "hunt_cycle184",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='ENGIE Chile. “12M 2025 Presentation ENGIE Chile.” Investor presentation PDF. https://www.engie.cl/wp-content/uploads/2024/10/12M2025-Presentation-ENGIE-CHILE-VF.pdf.',
    annotation="ENGIE Chile deck: BESS Lile CapEx USD 174m. Supports engie_bess_lile_174m_2026.",
    evid_note="Opened ENGIE Chile 12M2025 investor PDF 2026-10-04; cross-checked announcement https://www.engie.cl/anunciamos-proyecto-de-reconversion-en-el-complejo-termico-de-mejillones/ (2 Oct 2025) for scope/COD.",
)

# 4. solar / allied — Grenergy / Solar Antofagasta Parque Fotovoltaico Antofagasta 1 DIA
row_doc(
    "grenergy_antofagasta1_seia_520m_2026",
    "energy",
    "solar",
    "allied",
    "Grenergy / Solar Antofagasta — Parque Fotovoltaico Antofagasta 1 DIA (María Elena)",
    "Chile",
    "28 Aug 2026: Solar Antofagasta SpA (Grenergy Renovables) submits SEIA DIA for Parque Fotovoltaico Antofagasta 1 in María Elena (Tocopilla/Antofagasta) — 516.92 MWp / 430 MWn PV + 430 MW / ~3,010 MWh BESS (~7h); new Salitre 33/220 kV substation + 20.7 km line to Kimal; DIA executive summary CapEx ~USD 250m PV/Tx + USD 270m BESS = ~USD 520m (press later cites USD 593m admissibility figure — not used). Construction targeted May 2028; COD Feb 2030. CapEx = USD 520m from DIA breakdown. Distinct from Oasis de Atacama / Central Oasis / Gabriela rows.",
    "520000000",
    "2026-08-28",
    "2026",
    "-22.35",
    "-69.66",
    "María Elena commune, Provincia de Tocopilla, Región de Antofagasta, Chile (DIA geography; approximate).",
    "pv_magazine_grenergy_antofagasta1_20260828",
    "La DIA estima una inversión de aproximadamente 250 millones de dólares para el parque fotovoltaico, incluida la línea de transmisión y la subestación, y otros 270 millones de dólares para el sistema BESS, lo que sitúa la inversión descrita en el resumen ejecutivo en unos 520 millones de dólares.",
    "https://www.pv-magazine-latam.com/2026/08/28/grenergy-proyecta-en-chile-un-parque-solar-de-5169-mwp-con-un-bess-de-430-mw-3-010-mwh/",
    "Actor: Grenergy Renovables (Spain) via Solar Antofagasta SpA — allied. UNVERIFIED proxy: pv magazine LatAm citing SEIA DIA executive-summary CapEx split; SEIA HTML ficha returned 500 this cycle. Note USD 593m press figure after SEA admissibility not entered. Shuffle solar.",
    "hunt_cycle184",
    investment_type="permitting",
    evidence="proxy",
    bib_type="press",
    chicago='Ini, Luis. “Grenergy proyecta en Chile un parque solar de 516,9 MWp con un BESS de 430 MW / 3.010 MWh.” pv magazine Latinoamérica, August 28, 2026. https://www.pv-magazine-latam.com/2026/08/28/grenergy-proyecta-en-chile-un-parque-solar-de-5169-mwp-con-un-bess-de-430-mw-3-010-mwh/.',
    annotation="pv magazine LatAm: Antofagasta 1 DIA CapEx ~USD 520m. Supports grenergy_antofagasta1_seia_520m_2026.",
    evid_note="Opened pv magazine LatAm Spanish page 2026-10-04 citing DIA CapEx split; SEIA expediente URL returned HTTP 500 this cycle.",
)

# 5. power_plants_grid / prc — Nari Technology CGE Transmisión OA awards
row_doc(
    "nari_cge_parronal_casas_viejas_19p2m_2026",
    "energy",
    "power_plants_grid",
    "prc",
    "Nari Technology — CGE Transmisión OA awards (Parronal + Casas Viejas)",
    "Chile",
    "16 Jun 2026 CGE Transmisión Acta de Adjudicación (proceso CGET_OA_1_2025): Nari Technology Co. Ltd. Agencia en Chile awarded (i) Ampliación S/E Parronal (NTR ATMT) + seccionamiento Línea 1×66 kV Los Maquis–Hualañé — VI USD 9,856,103; (ii) Ampliación S/E Casas Viejas (NTR ATMT) — VI USD 9,373,503. CapEx/award face = combined VI USD 19,229,606. Distinct from CWE Pitrufquén OA and prior Hitachi/Siemens/GE Chile grid rows.",
    "19229606",
    "2026-06-16",
    "2026",
    "",
    "",
    "CGE Transmisión OA works — S/E Parronal / Los Maquis–Hualañé and S/E Casas Viejas (multi-site; lat/lon blank).",
    "cge_oa_acta_adjudicacion_20260616",
    "21_185_OA_16 Ampliación en S/E Parronal (NTR ATMT) y Seccionamiento Línea 1x66 kV Los Maquis - Hualañé Nari Technology Co. LTD. Agencia en Chile 9.856.103 … Ampliación en S/E Casas Viejas (NTR ATMT) Nari Technology Co. LTD. Agencia en Chile 9.373.503",
    "https://www.coordinador.cl/wp-content/uploads/2026/06/CGET_OA_1_2025_Acta-de-Adjudicacion-Rev.0.pdf",
    "Actor: Nari Technology (PRC) Agencia en Chile — prc. Official CGE Transmisión award acta published via Coordinador Eléctrico Nacional. Combined VI for two Nari awards. Shuffle power_plants_grid.",
    "hunt_cycle184",
    investment_type="epc",
    evidence="documented",
    bib_type="government",
    chicago='CGE Transmisión. “Acta de Adjudicación — Licitación Pública Internacional Obras de Ampliación CGE Transmisión (CGET_OA_1_2025).” June 16, 2026. https://www.coordinador.cl/wp-content/uploads/2026/06/CGET_OA_1_2025_Acta-de-Adjudicacion-Rev.0.pdf.',
    annotation="CGE OA acta: Nari Parronal+Casas Viejas VI USD 19.23m. Supports nari_cge_parronal_casas_viejas_19p2m_2026.",
    evid_note="Opened Coordinador-hosted CGE Transmisión Acta PDF 2026-10-04.",
)

# 6. engineering_epc / us — DFC proposed commitment to Patria PI Fund V
row_doc(
    "dfc_patria_pi_fund_v_75m_proposed",
    "infrastructure",
    "engineering_epc",
    "us",
    "DFC — proposed up to USD 75m investment in Patria PI Fund V (LatAm infrastructure)",
    "Regional",
    "DFC Policy Review (proposed): up to USD 75 million Loan/Guaranty/Equity Investment in PI Fund V (Ontario), L.P. managed by PI General Partner V Ltd. (Patria); target fund size USD 2.5 billion; primary focus Brazil, Colombia, Peru, Mexico (Chile excused-investor treatment); greenfield contracted infrastructure across power/energy, transportation/logistics, digital, and environmental services. Not a closed commitment — proposed disclosure. CapEx/commitment face = USD 75m ceiling. Distinct from dfc_serra_verde_pela_ema_565m_2025 (archived REE) and project-level DFC rows.",
    "75000000",
    "2024-04-29",
    "2024",
    "",
    "",
    "LatAm multi-country infrastructure fund — intentionally off-map (no single named worksite).",
    "dfc_patria_pi_fund_v_policy_review",
    "Up to $75 million … The Fund is targeting investments in infrastructure sectors in Latin America that align with DFC’s and the U.S. Government’s priorities … primary focus on Brazil (UMIC), Colombia [1] (UMIC), Peru (UMIC), and Mexico (UMIC)",
    "https://www.dfc.gov/sites/default/files/media/documents/PI%20Fund%20V%20%28Ontario%29%2C%20L.P..pdf",
    "Actor: U.S. International Development Finance Corporation — us; fund manager Patria. Official DFC proposed Policy Review PDF. Framework/FI commitment ceiling — not a named project loan. ≥1/3 U.S. hunt budget for cycle 184. Shuffle engineering_epc.",
    "hunt_cycle184",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='U.S. International Development Finance Corporation. “Proposed DFC Loan/Guaranty/Equity Investment — PI Fund V (Ontario), L.P.” Policy Review PDF. https://www.dfc.gov/sites/default/files/media/documents/PI%20Fund%20V%20%28Ontario%29%2C%20L.P..pdf.',
    annotation="DFC: proposed up to USD 75m for Patria PI Fund V. Supports dfc_patria_pi_fund_v_75m_proposed.",
    evid_note="Opened DFC Policy Review PDF 2026-10-04 (undated board packet; footnote cites Apr 2024 EPA access).",
)

# Thin top-up + remaining shuffle slots dry: lithium, fission_smr, port_ownership, niobium,
# bridges_roads, water, building_materials, wind, nickel, balsa, port_cranes, rail, copper,
# graphite (catalog dense; ≥1/3 U.S. hunt budget — AES Andes hub / ARRAY Lupi / EXIM Argentina
# / Chilean Cobalt LOI / Progress Rail VLI / Wabtec MRS / Albemarle TED already logged;
# holdovers unsigned).


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
    print(f"cycle184 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
