#!/usr/bin/env python3
"""Cycle 167 hunt: shuffle_seed=20261167; equal budget; U.S./PRC split; thin after.

Canonical shuffle: rail, balsa, graphite, water, power_plants_grid, copper, fission_smr,
wind, bridges_roads, other_renewables, building_materials, port_cranes, nickel, niobium,
engineering_epc, port_ownership, solar, lithium.

Thin: balsa/fission/niobium once (dry); nickel+graphite already used this session.
Prioritize PRC fills after cycle-166 PRC thin.
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


# 1. rail / allied — Sacyr Grupo Vía Central Ferrocarril Central Uruguay
row_doc(
    "sacyr_via_central_ferrocarril_uruguay_2025",
    "infrastructure",
    "rail",
    "allied",
    "Sacyr Concesiones / Grupo Vía Central — Ferrocarril Central PPP (Montevideo–Paso de los Toros)",
    "Uruguay",
    "Uruguay MEF Ferrocarril Central page: MTOP awarded definitive PPP 30 Apr 2019 to Grupo Vía Central (SACEEM, BERKES, Sacyr Concesiones 40%, NGE); contract signed 10 May 2019 for finance/design/build/rehab/maintain Puerto de Montevideo–Estación Paso de los Toros; Acta de Puesta en Servicio 8 Aug 2024; operational approval certificate 8 Aug 2025; 2025 PPP adenda. CapEx blank on opened MEF page (availability payments tracked separately). Fills Uruguay×rail empty cell. CMEC–SDHS bid lost.",
    "",
    "",
    "2025",
    "-34.880",
    "-56.180",
    "Puerto de Montevideo railhead / Ferrocarril Central corridor start, Uruguay.",
    "mef_uruguay_ferrocarril_central",
    "30 de abril de 2019: El Ministerio de Transporte y Obras Públicas adjudicó, en forma definitiva, la licitación del proyecto al oferente Grupo Vía Central integrado por SACEEM, BERKES, SACYR y NGE. … 10 de mayo de 2019: Se firmó el contrato … Puerto de Montevideo-Estación Paso de los Toros … 8 de agosto de 2025: La Dirección Nacional de Transporte Ferroviario, otorgó el Certificado de Aprobación Operacional de Proyecto. … SACYR CONCESIONES (40%)",
    "https://www.gub.uy/ministerio-economia-finanzas/politicas-y-gestion/proyecto-ferrocarril-central",
    "Actor: Sacyr Concesiones S.L. (Spain HQ, 40% lead) via Grupo Vía Central — allied. Uruguay MEF government primary. CapEx blank. First Uruguay rail row.",
    "hunt_latam_rail_telecom",
    investment_type="concession",
    bib_type="government",
    chicago='Ministerio de Economía y Finanzas (Uruguay). “Proyecto Ferrocarril Central.” https://www.gub.uy/ministerio-economia-finanzas/politicas-y-gestion/proyecto-ferrocarril-central.',
    annotation="Uruguay MEF: Sacyr/Grupo Vía Central Ferrocarril Central PPP; ops certificate Aug 2025. Supports sacyr_via_central_ferrocarril_uruguay_2025.",
    evid_note="Opened Uruguay MEF Ferrocarril Central project page (award, shareholding, 2025 ops certificate).",
)

# 2. water / prc — CCECC Matagalpa water/sewer/WWTP contract
row_doc(
    "ccecc_matagalpa_water_wwtp_nicaragua",
    "resources",
    "water",
    "prc",
    "CCECC — Matagalpa potable water, sewerage and wastewater treatment upgrade contract",
    "Nicaragua",
    "18 Apr 2024 TN8 interview with CCECC VP Guan Jiaxin: company signed a contract to improve and expand potable water systems, sewers and wastewater treatment in Matagalpa city (distinct from Managua–Masaya–Granada rail MoU still in prefeasibility). CapEx blank (amount undecided per same interview for rail; water CapEx not disclosed). Fills Nicaragua×water empty cell.",
    "",
    "",
    "2024",
    "12.930",
    "-85.920",
    "Matagalpa city, Matagalpa Department, Nicaragua.",
    "tn8_ccecc_matagalpa_water_20240418",
    "En Nicaragua firmamos un memorando con el ministro Mojica sobre el proyecto ferroviario que conectará Managua, Masaya y Granada. … En Nicaragua firmamos un contrato de mejoramiento y ampliación de los sistemas de agua potable, alcantarillado y tratamiento de aguas residuales en la ciudad de Matagalpa",
    "https://www.tn8.ni/nacionales/exclusiva-asi-avanza-el-proyecto-del-ferrocarril-que-construira-china-en-nicaragua/",
    "Actor: China Civil Engineering Construction Corporation (CCECC, PRC SOE) — prc. Press interview quoting CCECC VP — CapEx blank; contract existence attributed to named executive. First Nicaragua water row.",
    "hunt_res_water",
    investment_type="epc",
    evidence="proxy",
    bib_type="news",
    chicago='Morales, Oscar. “EXCLUSIVA: Así avanza el proyecto del ferrocarril que construirá China en Nicaragua.” TN8, April 18, 2024. https://www.tn8.ni/nacionales/exclusiva-asi-avanza-el-proyecto-del-ferrocarril-que-construira-china-en-nicaragua/.',
    annotation="TN8/CCECC VP: Matagalpa water/sewer/WWTP contract signed (CapEx blank). Supports ccecc_matagalpa_water_wwtp_nicaragua.",
    evid_note="Opened TN8 18 Apr 2024 CCECC VP interview (Matagalpa water contract quote).",
)

# 3. water / us — USAID Haiti Water and Sanitation USD 41.8m
row_doc(
    "usaid_haiti_wash_41p8m_2017",
    "resources",
    "water",
    "us",
    "USAID — Haiti Water and Sanitation project (DAI implementer)",
    "Haiti",
    "24 Dec 2017 VOA editorial (U.S. government): USAID Water and Sanitation project is a USD 41.8 million investment aligned with Haiti Ministry of Public Health and water/sanitation directorate; four-year project implemented by Development Alternatives, Inc. (DAI); focuses on cholera hotspot communes and Hurricane Matthew recovery communes. CapEx/investment = USD 41.8m face. Fills Haiti×water empty cell.",
    "41800000",
    "2017-12-24",
    "2017",
    "18.540",
    "-72.340",
    "National WASH program (Port-au-Prince institutional pin; approximate).",
    "voa_usaid_haiti_wash_20171224",
    "The USAID Water and Sanitation project represents a 41.8 million dollar investment aligned with the priorities of Haiti’s Ministry of Public Health and the water and sanitation directorate. … The four-year project will be implemented by Development Alternatives, Inc.",
    "https://editorials.voa.gov/a/safe-water-haiti/4175506.html",
    "Actor: USAID (U.S. government) / DAI implementer — us. VOA U.S. government editorial primary. USD 41.8m face. First Haiti water row.",
    "hunt_res_water",
    investment_type="financing",
    bib_type="government",
    chicago='Voice of America (U.S. government editorial). “Safe Water for Haiti.” December 24, 2017. https://editorials.voa.gov/a/safe-water-haiti/4175506.html.',
    annotation="VOA/USAID: Haiti Water and Sanitation project USD 41.8m (DAI). Supports usaid_haiti_wash_41p8m_2017.",
    evid_note="Opened VOA 24 Dec 2017 Safe Water for Haiti editorial (USD 41.8m USAID WASH).",
)

# 4. building_materials / prc — CSCEC Nuevas Victorias Phase 1
row_doc(
    "cscec_nuevas_victorias_fase1_920_nicaragua",
    "infrastructure",
    "building_materials",
    "prc",
    "CSCEC — Nuevas Victorias affordable housing Phase 1 (920 houses, Managua)",
    "Nicaragua",
    "25 Aug 2025 CSCEC English: first phase of Nicaragua affordable housing project completed and handed over — 920 single-story two-bedroom houses in Managua plus community roads/utilities; >1,000 local jobs during construction. CapEx blank on company page. Fills Nicaragua×building_materials empty cell.",
    "",
    "",
    "2025",
    "12.140",
    "-86.250",
    "Nuevas Victorias Phase 1 community, Managua, Nicaragua (approximate urban pin).",
    "cscec_nuevas_victorias_fase1_20250825",
    "Recently, CSCEC-built first phase of Nicaragua's affordable housing project, undertaken by CSCEC, has been successfully completed and handed over. The first phase of the project involved the construction of 920 single-story, two-bedroom houses in the city of Managua, along with supporting infrastructure such as roads and utility networks within the community.",
    "https://english.cscec.com/CompanyNews/CorporateNews/202508/3901201.html",
    "Actor: China State Construction Engineering Corporation (CSCEC, PRC SOE) — prc. Company English primary. CapEx blank. First Nicaragua building_materials row.",
    "hunt_infra_building_materials",
    investment_type="epc",
    bib_type="company",
    chicago='China State Construction Engineering Corporation. “CSCEC-Built First Phase of Nicaragua’s Affordable Housing Project Handed Over.” August 25, 2025. https://english.cscec.com/CompanyNews/CorporateNews/202508/3901201.html.',
    annotation="CSCEC primary: Nuevas Victorias Phase 1 920 houses Managua handed over. Supports cscec_nuevas_victorias_fase1_920_nicaragua.",
    evid_note="Opened CSCEC English 25 Aug 2025 Nuevas Victorias Phase 1 handover release.",
)

# 5. port_cranes / prc — ZPMC 3 RTGs Caucedo
row_doc(
    "zpmc_caucedo_3rtg_7p9m_dr_2025",
    "infrastructure",
    "port_cranes",
    "prc",
    "ZPMC — 3 RTG cranes (DP World Caucedo)",
    "Dominican Republic",
    "4 Jul 2025 WorldCargo News: DP World took delivery of three new ZPMC RTGs at Port of Caucedo; fleet to 35 RTGs / 11 STS; each 41 t / 21 m lift / 23.47 m span; CEO Manuel Martínez cites USD 7.9 million investment. CapEx = USD 7.9m UNVERIFIED press proxy. Fills Dominican Republic×port_cranes empty cell.",
    "7900000",
    "2025-07-04",
    "2025",
    "18.420",
    "-69.630",
    "DP World Caucedo terminal, Boca Chica, Dominican Republic.",
    "worldcargo_caucedo_zpmc_rtg_20250704",
    "DP World has added three new RTGs to its terminal in Caucedo, Dominican Republic, increasing the fleet to 35 units. … The new RTGs, supplied by ZPMC, represent a US$7.9m investment, according to Manuel Martínez, CEO of DP World Dominicana.",
    "https://www.worldcargonews.com/cargo-handling-equipment/2025/07/more-rtgs-for-caucedo/",
    "Actor: ZPMC (PRC SOE) — prc; terminal DP World (allied operator). Trade press quoting DP World CEO — evidence=proxy for CapEx. First DR port_cranes row.",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    evidence="proxy",
    bib_type="news",
    chicago='WorldCargo News. “More RTGs for Caucedo.” July 4, 2025. https://www.worldcargonews.com/cargo-handling-equipment/2025/07/more-rtgs-for-caucedo/.',
    annotation="WorldCargo News: ZPMC 3 RTGs Caucedo; USD 7.9m (proxy). Supports zpmc_caucedo_3rtg_7p9m_dr_2025.",
    evid_note="Opened WorldCargo News 4 Jul 2025 Caucedo ZPMC RTG delivery article.",
)

# 6. wind / allied — Acciona Chiripa EV USD 80m sale
row_doc(
    "acciona_chiripa_ev_80m_costa_rica_2025",
    "energy",
    "wind",
    "allied",
    "ACCIONA Energía — Chiripa wind farm 65% stake sale (EV USD 80m)",
    "Costa Rica",
    "17 Sep 2025 ACCIONA Energía: agrees to sell 65% stake in Chiripa wind farm (49.5 MW, Guanacaste, COD 2015, BOT to 2033) to Ecoenergía; enterprise value of asset USD 80 million (€71.4m); project financing USD 50 million. CapEx/investment = USD 80m EV face (ownership transfer, not new build). Distinct from vestas_costa_rica_22mw_order_2025 equipment order.",
    "80000000",
    "2025-09-17",
    "2025",
    "10.480",
    "-85.100",
    "Chiripa wind farm, Guanacaste, Costa Rica.",
    "acciona_chiripa_sale_20250917",
    "ACCIONA Energía has reached an agreement to sell its 65% stake in the Chiripa wind farm in Costa Rica to Ecoenergía … reflects an enterprise value (EV) of the asset of US$80 million (€71.4 million). With an installed capacity of 49.5MW, the Chiripa wind farm is located in the province of Guanacaste and has been in operation since 2015.",
    "https://www.acciona-energia.com/updates/news/acciona-energia-sells-stake-chiripa-wind-farm-costa-rica-to-ecoenergia",
    "Actor: ACCIONA Energía (Spain HQ) seller — allied. Company English primary. USD 80m EV. Ownership exit documentation.",
    "hunt_energy_wind",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='ACCIONA Energía. “ACCIONA Energía Sells Its Stake in the Chiripa Wind Farm in Costa Rica to Ecoenergía.” September 17, 2025. https://www.acciona-energia.com/updates/news/acciona-energia-sells-stake-chiripa-wind-farm-costa-rica-to-ecoenergia.',
    annotation="ACCIONA primary: Chiripa 65% sale EV USD 80m. Supports acciona_chiripa_ev_80m_costa_rica_2025.",
    evid_note="Opened ACCIONA Energía 17 Sep 2025 Chiripa stake-sale release.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
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
    print(f"Cycle 167 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
