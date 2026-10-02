#!/usr/bin/env python3
"""Cycle 176 hunt: shuffle_seed=20261176; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261176)): balsa, wind, nickel,
building_materials, power_plants_grid, niobium, port_ownership, engineering_epc,
copper, solar, water, rail, port_cranes, lithium, fission_smr, other_renewables,
graphite, bridges_roads.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (AIMA/WITS Ecuador balsa, Centaurus/BRN/MMG nickel, and
Meitner/Colombia/Peru FIRST fission already logged). Holdovers unsigned: CRBC
Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail past MoU.
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
            "retrieved": "2026-10-02",
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


# 1. balsa / miss (thin; AIMA/WITS/Plantabal dense)

# 2. wind / us — AES Colombia La Guajira cluster CapEx
row_doc(
    "aes_colombia_guajira_549mw_1bn_2026",
    "energy",
    "wind",
    "us",
    "AES Colombia — La Guajira wind cluster first stage 549 MW CapEx (~USD 1bn)",
    "Colombia",
    "21 Aug 2026 (La República interview with AES Colombia GM Federico Echavarría): La Guajira wind cluster first stage 549 MW (transmission-limited pending GEB Colectora) with investment near USD 1 billion; financial close targeted early 2027 then construction; cluster >1 GW overall; first build tranche ~255 MW near USD 500m. CapEx = USD 1bn for stated 549 MW stage. Distinct from aes_jk1_jk2_idb_invest_150m_2025 (proposed IDB Invest loan).",
    "1000000000",
    "2026-08-21",
    "2026",
    "",
    "",
    "La Guajira wind cluster / Uribia area (transmission via Colectora) — lat/lon blank (multi-site cluster).",
    "larepublica_aes_guajira_1bn_20260821",
    "Este es el mayor clúster eólico que hay en el país: son más de 1.000 megavatios del clúster. Pero en La Guajira el tema es transmisión. Con transmisión garantizada son 549 megavatios, que lo vamos a obtener cuando complete la construcción el Grupo Energía Bogotá con la línea Colectora. La primera etapa son 549 megavatios y es una inversión cercana a US$1.000 millones. Lo vamos a ver en dos etapas: la primera que le estoy comentando, es de alrededor de 255 megavatios, cercano a US$500 millones.",
    "https://www.larepublica.co/empresas/aes-alista-una-inversion-de-us-1-000-millones-para-proyecto-en-la-guajira-4463385",
    "Actor: AES Colombia (AES Corporation U.S. affiliate) — us. Opened La República interview 21 Aug 2026. U.S. side-balance for wind. CapEx attributed to stated USD 1bn for 549 MW stage (not closed financing).",
    "hunt_cycle176",
    investment_type="greenfield",
    evidence="documented",
    bib_type="trade_press",
    chicago='Murcia, Juan Diego. “AES alista una inversión de US$1.000 millones para proyecto en La Guajira.” La República, August 21, 2026. https://www.larepublica.co/empresas/aes-alista-una-inversion-de-us-1-000-millones-para-proyecto-en-la-guajira-4463385.',
    annotation="La República/AES Colombia: Guajira 549 MW stage ~USD 1bn. Supports aes_colombia_guajira_549mw_1bn_2026.",
    evid_note="Opened La República interview page 2026-10-02.",
)

# 3. nickel / miss (thin; Centaurus/BRN/MMG dense)

# 4. building_materials / miss

# 5. power_plants_grid / miss

# 6. niobium / miss

# 7. port_ownership / miss

# 8. engineering_epc / miss

# 9. copper / miss

# 10. solar / us — AES Colombia additional solar CapEx ~USD 100m
row_doc(
    "aes_colombia_solar_expand_100m_2026",
    "energy",
    "solar",
    "us",
    "AES Colombia — additional solar parks CapEx (~USD 100m; Huila/Meta base)",
    "Colombia",
    "21 Aug 2026 (same La República AES Colombia interview): company states existing ~128 MW solar in Huila and Meta and plans more solar parks with investment around USD 100 million. CapEx = USD 100m (CEO figure; sites not individually named on opened page). Distinct from aes_colombia_solar3_anla_100mw_2025.",
    "100000000",
    "2026-08-21",
    "2026",
    "",
    "",
    "Huila / Meta solar footprint (AES Colombia) — lat/lon blank (multi-site / unnamed new parks).",
    "larepublica_aes_guajira_1bn_20260821",
    "En hidroeléctricas tenemos 1.020 megavatios, y alrededor de 128 megavatios solares en el Huila y en el Meta.\n¿Tienen planeado poner más parques solares?\n…\n¿Y la inversión para ese de cuánto es?\nEs alrededor de US$100 millones.",
    "https://www.larepublica.co/empresas/aes-alista-una-inversion-de-us-1-000-millones-para-proyecto-en-la-guajira-4463385",
    "Actor: AES Colombia (U.S. affiliate) — us. Opened same La República interview 21 Aug 2026. U.S. side-balance for solar. CapEx = stated ~USD 100m for additional solar parks.",
    "hunt_cycle176",
    investment_type="greenfield",
    evidence="documented",
    bib_type="trade_press",
    chicago='Murcia, Juan Diego. “AES alista una inversión de US$1.000 millones para proyecto en La Guajira.” La República, August 21, 2026. https://www.larepublica.co/empresas/aes-alista-una-inversion-de-us-1-000-millones-para-proyecto-en-la-guajira-4463385.',
    annotation="La República/AES Colombia: additional solar ~USD 100m. Supports aes_colombia_solar_expand_100m_2026.",
    evid_note="Opened La República interview page 2026-10-02 (shared URL with Guajira CapEx).",
)

# 11. water / allied — NGE/Saceem OSE Metropolitan Water Infrastructure
row_doc(
    "saceem_ose_agua_metropolitana_212m_2026",
    "resources",
    "water",
    "allied",
    "NGE / Saceem consortium — OSE Metropolitan Water Infrastructure (Montevideo)",
    "Uruguay",
    "9 Mar 2026 (NGE): Saceem-led consortium with Berkes and Ciemsa signs Metropolitan Water Infrastructure Project for OSE — design/build/finance/maintain; CapEx approx USD 212 million; 20-year contract; Santa Lucía River intake; 200,000 m³/day plant at Aguas Corrientes; 2.5 km raw + 56 km drinking pipelines; ~USD 45m equity + ~USD 255m senior debt structuring. Distinct from invenergy_tealov_cardal_tx_uruguay_2024.",
    "212000000",
    "2026-03-09",
    "2026",
    "",
    "",
    "Aguas Corrientes / Santa Lucía River / Montevideo metro water system — lat/lon blank (corridor + plant).",
    "nge_saceem_ose_agua_20260309",
    "The NGE Group announces, through its subsidiary Saceem—leader of a consortium alongside Berkes and Ciemsa—the signing of the Metropolitan Water Infrastructure Project in Uruguay for Obras Sanitarias del Estado (OSE)… With an investment of approximately $212 million (CAPEX) and a 20-year contractual duration… the construction of a new water intake on the Santa Lucía River; a drinking water production plant with a capacity of 200,000 m³ per day, located in Aguas Corrientes; 2.5 km of raw water pipelines and 56 km of drinking water pipelines…",
    "https://www.nge.fr/app/uploads/2026/03/PR-NGE-Saceem-2026_Agua-Metropolitana-DEF.pdf",
    "Actor: NGE Group / Saceem (French) — allied; Berkes/Ciemsa local partners. Opened NGE English PDF press release 9 Mar 2026.",
    "hunt_cycle176",
    investment_type="epc",
    evidence="documented",
    bib_type="company",
    chicago='NGE Group. “Uruguay – Montevideo: NGE, through its subsidiary Saceem, wins a major drinking water infrastructure investment project ($212 million).” March 9, 2026. https://www.nge.fr/app/uploads/2026/03/PR-NGE-Saceem-2026_Agua-Metropolitana-DEF.pdf.',
    annotation="NGE/Saceem: OSE Metropolitan Water CapEx USD 212m. Supports saceem_ose_agua_metropolitana_212m_2026.",
    evid_note="Opened NGE PDF press release 2026-10-02.",
)

# 12. rail / miss

# 13. port_cranes / prc — ZPMC Tecon Santos STS+RTG package
row_doc(
    "zpmc_tecon_santos_sts_rtg_57m_2026",
    "infrastructure",
    "port_cranes",
    "prc",
    "ZPMC — 2× STS + 8× electric RTG for Tecon Santos (Santos Brasil)",
    "Brazil",
    "15 Jan 2026 (PortalPortuario): Tecon Santos receives two new ship-to-shore (STS) cranes and eight electric RTGs manufactured by Shanghai Zhenhua (ZPMC), delivered assembled on Zhen Hua 28; package investment on order of USD 57 million; remote operation phased after tests; part of Tecon Santos expansion/modernization (~USD 570m through 2031). CapEx = USD 57m equipment package. Distinct from zpmc_tecon_rio_grande_2026 and zpmc_icave_veracruz_sts_rtg_2026.",
    "57000000",
    "2026-01-15",
    "2026",
    "",
    "",
    "Tecon Santos, left bank of Port of Santos — lat/lon blank pending verified berth pin.",
    "portalportuario_zpmc_tecon_santos_20260115",
    "Tecon Santos recibió dos nuevas grúas ship-to-shore (STS) y ocho grúas pórtico sobre neumáticos (RTG) eléctricas, las que fueron fabricadas Shanghai Zhenhua Heavy Industries Company Limited (ZPMC) en China y adquiridas por Santos Brasil… Los diez equipos representan inversiones del orden de USD 57 millones.",
    "https://portalportuario.cl/brasil-zpmc-entrega-dos-nuevas-gruas-sts-y-ocho-rtg-a-tecon-santos/",
    "Actor: ZPMC (PRC SOE crane OEM) — prc; Santos Brasil host. Opened PortalPortuario Spanish report 15 Jan 2026.",
    "hunt_cycle176",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="trade_press",
    chicago='PortalPortuario. “Brasil: ZPMC entrega dos nuevas grúas STS y ocho RTG a Tecon Santos.” January 15, 2026. https://portalportuario.cl/brasil-zpmc-entrega-dos-nuevas-gruas-sts-y-ocho-rtg-a-tecon-santos/.',
    annotation="PortalPortuario: ZPMC 2 STS + 8 RTG Tecon Santos ~USD 57m. Supports zpmc_tecon_santos_sts_rtg_57m_2026.",
    evid_note="Opened PortalPortuario page 2026-10-02.",
)

# 14. lithium / miss; 15. fission_smr / miss (thin); 16. other_renewables / miss; 17. graphite / miss

# 18. wind / other — Colbún Cuatro Vientos RCA CapEx (second wind fill; Chilean host)
row_doc(
    "colbun_cuatro_vientos_540m_2026",
    "energy",
    "wind",
    "other",
    "Colbún — Parque Eólico Cuatro Vientos 345.6 MW RCA (Llanquihue)",
    "Chile",
    "1–2 Sep 2026: Los Lagos Coeva unanimously approves RCA for Colbún Parque Eólico Cuatro Vientos in Llanquihue — projected investment USD 540 million; 48× 7.2 MW turbines (345.6 MW); ~800 GWh/year; 15 km double-circuit line to Subestación Tineo; FID still contingent on customer/SEN needs; ops targeted 1H 2028 if built. CapEx = USD 540m. Distinct from aes/goldwind Chile wind catalog.",
    "540000000",
    "2026-09-02",
    "2026",
    "",
    "",
    "Parque Eólico Cuatro Vientos, Llanquihue (Loncotoro/Colegual) — lat/lon blank pending verified turbine-field pin.",
    "radiosago_colbun_cuatro_vientos_20260902",
    "La Comisión de Evaluación Ambiental (Coeva) de la Región de Los Lagos aprobó por unanimidad la Resolución de Calificación Ambiental del Parque Eólico Cuatro Vientos, propiedad de la empresa Colbún. Con una inversión proyectada de US$540 millones, la iniciativa ubicada en Llanquihue se convierte en el proyecto de mayor inversión calificado ambientalmente en la historia de la región… La central proyecta una capacidad instalada de 345,6 megavatios (MW) mediante la instalación de 48 aerogeneradores de 7,2 MW de potencia nominal cada uno.",
    "https://www.radiosago.cl/aprobado-el-mayor-parque-eolico-de-los-lagos-por-us540-millones-en-llanquihue/",
    "Actor: Colbún (Chilean; Grupo Matte) — other. Opened RadioSago 2 Sep 2026 summarizing Coeva RCA; CapEx matches Revista Electricidad / La Tercera synthesis.",
    "hunt_cycle176",
    investment_type="greenfield",
    evidence="documented",
    bib_type="trade_press",
    chicago='Márquez, Luis. “Aprobado el mayor parque eólico de Los Lagos por US$540 millones en Llanquihue.” RadioSago, September 2, 2026. https://www.radiosago.cl/aprobado-el-mayor-parque-eolico-de-los-lagos-por-us540-millones-en-llanquihue/.',
    annotation="RadioSago/Coeva: Colbún Cuatro Vientos RCA CapEx USD 540m. Supports colbun_cuatro_vientos_540m_2026.",
    evid_note="Opened RadioSago page 2026-10-02.",
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
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 176 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
