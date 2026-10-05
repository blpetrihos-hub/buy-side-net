#!/usr/bin/env python3
"""Cycle 235 hunt: shuffle_seed=20261235; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261235).shuffle):
other_renewables, solar, bridges_roads, power_plants_grid, niobium, rail, nickel, water,
building_materials, engineering_epc, graphite, port_ownership, port_cranes, wind, lithium,
fission_smr, copper, balsa.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: CapEx-fills Oceaneering Petrobras umbilicals; Freeport El Abra
Continuidad; CB&I VMOS Punta Colorada (plus residual sweeps).
PRC equal-budget: ZPMC DP World Lirquén; Huawei/Aggreko Amazonas BESS.
NEW: OHLA Santiago Metro Line 7 Groups 5–6 stations EUR 71.8m (company monográfico).
Skipped: RAP-as-CapEx; Huaxin–CSN; Xinhai MoU; Aldesa EUR; ISA Madeira unwind;
Worley (Rio Tinto project total not Worley fee); NFE TGS EBITDA; Freeport OxI package;
COP/CLP/PEN (no Fed H.10).
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

EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"
SEK_USD = "9.9047"
SEK_FX_DATE = "2026-09-25"


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
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


# 1. NEW rail / allied — OHLA Santiago Metro Line 7 Groups 5–6 stations EUR 71.8m
row_doc(
    "ohla_santiago_l7_stations_g5g6_71p8m_eur_2026",
    "infrastructure", "rail", "allied",
    "OHLA — Santiago Metro Line 7 Groups 5–6 stations (6 stations)",
    "Chile",
    "OHLA Ferrocarriles 2026 monográfico: Línea 7 Grupo 5 y 6 — construction of 6 new stations within Line 7 expansion; investment EUR 71.8 million. Distinct from ohla_metro_santiago_l9_2026 (Line 9 shafts/tunnels) and prior Line 7 Tramo 4 shafts award. CapEx: Fed H.10 Sep 25 2026 EUR 1.1400 → USD 81.852m.",
    "71800000", EUR_FX_DATE, "2026", "-33.40", "-70.58",
    "Santiago Metro Line 7 Groups 5–6 stations corridor (Vitacura/Las Condes pin).",
    "ohla_ferrocarriles_monografico_202609",
    "Línea 7. Grupo 5 y 6 Construcción de 6 nuevas estaciones dentro del proyecto de expansión de la Línea 7. Inversión: 71,8 millones de euros",
    "https://www.ohla-group.com/wp-content/uploads/2026/09/monografico-ferrocarriles-2026-esp-1.pdf",
    "Actor: OHLA (Spain) — allied. NEW row: company monográfico EUR 71.8m Line 7 Groups 5–6 stations. CapEx USD via Fed H.10 Sep 25 2026 1.1400. Shuffle rail.",
    "hunt_cycle235", investment_type="epc", evidence="documented", currency="EUR",
    value_usd=str(round(71800000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='OHLA. “Infraestructuras Ferroviarias” (monográfico). September 2026. https://www.ohla-group.com/wp-content/uploads/2026/09/monografico-ferrocarriles-2026-esp-1.pdf.',
    annotation="OHLA Santiago L7 G5–6 stations NEW ~USD 81.85m via Fed H.10. Supports ohla_santiago_l7_stations_g5g6_71p8m_eur_2026.",
    evid_note="Opened OHLA Ferrocarriles monográfico PDF Spanish; EUR 71.8m / 6 stations Línea 7 Grupo 5 y 6 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 2. other_renewables / prc — CapEx-fill Huawei/Aggreko Amazonas ~USD 165m
row_doc(
    "huawei_aggreko_amazonas_bess_2026",
    "energy", "other_renewables", "prc",
    "Huawei Digital Power / Aggreko — Amazonas hybrid solar+BESS microgrids",
    "Brazil",
    "2–3 Mar 2026: Huawei supplies batteries to Aggreko for hybrid solar+BESS microgrids across 24 isolated Amazonas locations totaling ~110 MWp solar + 120 MWh storage; total investment estimated at USD 165 million (R$850 million). CapEx-fill: enter company/press dual USD 165m.",
    "165000000", "2026-03-03", "2026", "-3.35", "-64.71",
    "Amazonas isolated systems incl. Tefé (press geography).",
    "ess_news_huawei_aggreko_amazonas_20260303",
    "A consortium formed by Huawei Digital Power and British company Aggreko is set to deploy the largest integrated battery energy storage system (BESS) in Brazil in the Amazon … 110 MWp of photovoltaic plants and 120 MWh of battery capacity distributed across 24 locations, including mid-sized municipalities such as Tefé. Total investment is estimated at $165 million (Brazilian R$850 million)",
    "https://www.ess-news.com/2026/03/03/huawei-and-aggreko-win-brazils-largest-battery-storage-contract-will-replace-diesel-in-the-amazon/",
    "Actor: Huawei Digital Power (PRC) with Aggreko (UK) — prc (Huawei equipment). CapEx-fill: enter USD 165m dual. UNVERIFIED proxy press. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle235", investment_type="epc", evidence="proxy", currency="USD",
    value_usd="165000000", fx_usd="1", bib_type="press",
    chicago='ESS News. “Huawei and Aggreko win Brazil’s largest battery storage contract, will replace diesel in the Amazon.” March 3, 2026. https://www.ess-news.com/2026/03/03/huawei-and-aggreko-win-brazils-largest-battery-storage-contract-will-replace-diesel-in-the-amazon/.',
    annotation="Huawei/Aggreko Amazonas CapEx-fill USD 165m (proxy). Supports huawei_aggreko_amazonas_bess_2026.",
    evid_note="Opened ESS News English; USD 165m / R$850m dual / 110 MWp + 120 MWh / 24 sites confirmed. CapEx-fill enter USD 165m.",
)

# 3. water / us — CapEx-fill Freeport El Abra Continuidad ~USD 7.5bn
row_doc(
    "fcx_el_abra_desal_aqueduct_2026",
    "resources", "water", "us",
    "Freeport / Minera El Abra — Continuidad Operacional desal + aqueduct package",
    "Chile",
    "18 Mar 2026 Minera El Abra: Continuidad Operacional SEIA filing includes desalination plant and water pumping/conveyance alongside concentrator, thickened tailings, mine expansion, and leach continuity; preliminary total project investment approximately USD 7.5 billion. CapEx-fill: enter company USD 7.5bn preliminary total (water components embedded; no desal-only split disclosed).",
    "7500000000", "2026-03-18", "2026", "-22.19", "-68.85",
    "Minera El Abra, Antofagasta Region (company geography).",
    "elabra_continuidad_seia_20260318",
    "La inversión preliminar estimada del proyecto asciende aproximadamente a US$7.500 millones e incluye el desarrollo de una planta concentradora, una planta desalinizadora y un sistema de impulsión de agua, un depósito de relaves espesados, la expansión de la mina y la continuidad de las operaciones de lixiviación.",
    "https://www.elabra.cl/minera-el-abra-filial-de-freeport-mcmoran-ingresa-proyecto-de-continuidad-operacional-para-evaluacion-ambiental/",
    "Actor: Freeport-McMoRan / Minera El Abra — us. CapEx-fill: enter USD 7.5bn preliminary Continuidad total (desal+aqueduct embedded). Shuffle water / U.S. ≥1/3 budget.",
    "hunt_cycle235", investment_type="brownfield_expansion", evidence="documented", currency="USD",
    value_usd="7500000000", fx_usd="1",
    chicago='Minera El Abra. “Minera El Abra, filial de Freeport-McMoRan, ingresa proyecto de Continuidad Operacional para evaluación ambiental.” March 18, 2026. https://www.elabra.cl/minera-el-abra-filial-de-freeport-mcmoran-ingresa-proyecto-de-continuidad-operacional-para-evaluacion-ambiental/.',
    annotation="FCX El Abra Continuidad CapEx-fill USD 7.5bn. Supports fcx_el_abra_desal_aqueduct_2026.",
    evid_note="Opened El Abra Spanish; US$7.500 millones preliminary Continuidad package confirmed. CapEx-fill enter USD 7.5bn.",
)

# 4. engineering_epc / us — CapEx-fill Oceaneering Petrobras umbilicals USD 120m floor
row_doc(
    "oceaneering_petrobras_umbilicals_2024",
    "infrastructure", "engineering_epc", "us",
    "Oceaneering — Petrobras umbilicals + subsea distribution (up to 362 km)",
    "Brazil",
    "10 Jun 2024 Oceaneering: Manufactured Products wins two Petrobras contracts for up to 362 km steel-tube and thermoplastic electro-hydraulic umbilicals plus subsea distribution hardware; manufacture at Niterói; expected aggregate net revenue in the range of USD 120–183 million. CapEx-fill: enter USD 120m range floor.",
    "120000000", "2024-06-10", "2024", "-22.88", "-43.12",
    "Oceaneering Niterói manufacturing / Petrobras Campos–Santos umbilicals (company geography).",
    "oceaneering_petrobras_umbilicals_20240610",
    "The expected aggregate net revenue is in the range of $120 million to $183 million. Oceaneering is contracted to supply up to 362 kilometers … of steel tube and thermoplastic electro-hydraulic umbilicals and associated subsea distribution hardware",
    "https://investors.oceaneering.com/news/news-details/2024/Oceaneering-Announces-Manufactured-Products-Contracts-with-Petrobras/default.aspx",
    "Actor: Oceaneering (U.S.) — us. CapEx-fill: enter USD 120m floor of stated USD 120–183m aggregate net revenue range. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle235", investment_type="equipment_supply", evidence="documented", currency="USD",
    value_usd="120000000", fx_usd="1",
    chicago='Oceaneering International. “Oceaneering Announces Manufactured Products Contracts with Petrobras.” June 10, 2024. https://investors.oceaneering.com/news/news-details/2024/Oceaneering-Announces-Manufactured-Products-Contracts-with-Petrobras/default.aspx.',
    annotation="Oceaneering Petrobras umbilicals CapEx-fill USD 120m floor. Supports oceaneering_petrobras_umbilicals_2024.",
    evid_note="Opened Oceaneering IR English; USD 120–183m range / ≤362 km umbilicals confirmed. CapEx-fill enter USD 120m floor.",
)

# 5. engineering_epc / us — CapEx-fill CB&I VMOS Punta Colorada USD 100m floor
row_doc(
    "cbi_vmos_punta_colorada_storage_2025",
    "infrastructure", "engineering_epc", "us",
    "CB&I — VMOS Punta Colorada crude storage EPC (630,000 m³)",
    "Argentina",
    "16 Jan 2025 CB&I: significant EPC contract by VMOS for 630,000 m³ (4 million barrels) crude storage at Vaca Muerta Sur export facility, Punta Colorada; CB&I defines significant as between USD 100 million and USD 250 million. CapEx-fill: enter USD 100m range floor.",
    "100000000", "2025-01-16", "2025", "-41.70", "-65.02",
    "Punta Colorada, Río Negro (company geography).",
    "cbi_vmos_punta_colorada_20250116",
    "CB&I today announced that it has been awarded a significant* contract by VMOS, S.A., for the engineering, procurement, fabrication, and construction (EPC) of 630,000 cubic meters (4 million barrels) of total storage for the Vaca Muerta crude oil exportation facility, located in Punta Colorada, Rio Negro Province, Argentina. … *CB&I defines a significant contract as between USD $100 million and $250 million.",
    "https://www.cbi.com/wp-content/uploads/2025/01/CBI-Awarded-Crude-Oil-Exportation-Storage-Contract-for-Vaca-Muerta-Sur-Project-in-Argentina-FINAL.pdf",
    "Actor: CB&I (U.S./McDermott lineage) — us. CapEx-fill: enter USD 100m floor of company-defined significant range. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle235", investment_type="epc", evidence="documented", currency="USD",
    value_usd="100000000", fx_usd="1",
    chicago='CB&I. “CB&I Awarded Crude Oil Exportation Storage Contract for Vaca Muerta Sur Project in Argentina.” January 16, 2025. https://www.cbi.com/wp-content/uploads/2025/01/CBI-Awarded-Crude-Oil-Exportation-Storage-Contract-for-Vaca-Muerta-Sur-Project-in-Argentina-FINAL.pdf.',
    annotation="CB&I VMOS CapEx-fill USD 100m floor. Supports cbi_vmos_punta_colorada_storage_2025.",
    evid_note="Opened CB&I English PDF; 630,000 m³ / significant = USD 100–250m confirmed. CapEx-fill enter USD 100m floor.",
)

# 6. port_cranes / prc — CapEx-fill ZPMC DP World Lirquén ~USD 45m
row_doc(
    "zpmc_dpworld_lirquen_2022",
    "infrastructure", "port_cranes", "prc",
    "ZPMC — DP World Lirquén Super Post-Panamax quay cranes",
    "Chile",
    "DP World Lirquén receives first two ZPMC Super Post-Panamax quay cranes; a third similar crane to be added; port equipment forms part of a USD 45 million terminal investment. CapEx-fill: enter stated USD 45m package face.",
    "45000000", "2022-01-01", "2022", "-36.711", "-72.983",
    "DP World Lirquén, Biobío (press geography).",
    "seatrade_zpmc_lirquen_2022",
    "DP World Lirquen, in Chile, has received the first two Super Post Panamax cranes from Chinese manufacturer ZPMC. ... A third similar crane will be added and the port equipment form part of a $45m investment.",
    "https://www.seatrade-maritime.com/ports-logistics/dp-world-lirquen-receives-first-quay-cranes",
    "Actor: ZPMC (PRC OEM); buyer DP World Lirquén. CapEx-fill: enter USD 45m package. UNVERIFIED proxy press. Shuffle port_cranes / PRC equal-budget.",
    "hunt_cycle235", investment_type="equipment_supply", evidence="proxy", currency="USD",
    value_usd="45000000", fx_usd="1", bib_type="press",
    chicago='Seatrade Maritime. “DP World Lirquen receives first quay cranes.” 2022. https://www.seatrade-maritime.com/ports-logistics/dp-world-lirquen-receives-first-quay-cranes.',
    annotation="ZPMC Lirquén CapEx-fill USD 45m (proxy). Supports zpmc_dpworld_lirquen_2022.",
    evid_note="Opened Seatrade English; ZPMC cranes / $45m investment package confirmed. CapEx-fill enter USD 45m.",
)

# 7. lithium / allied — CapEx-fill Rio Tinto Maricunga up to USD 900m
row_doc(
    "rio_tinto_codelco_maricunga_ceol_2026",
    "resources", "lithium", "allied",
    "Rio Tinto / Codelco — Salar de Maricunga lithium partnership CapEx",
    "Chile",
    "12 Feb 2026 Codelco: Ministry of Mining signs CEOL amendment for Salar de Maricunga SpA; Codelco selected Rio Tinto as strategic partner in May 2025, committing a capital contribution of up to USD 900 million to develop the initiative. CapEx-fill: enter up-to USD 900m capital contribution face.",
    "900000000", "2026-02-12", "2026", "-26.92", "-69.05",
    "Salar de Maricunga, Atacama (official geography).",
    "codelco_maricunga_ceol_20260212",
    "It should be remembered that in May 2025 the Corporation selected Rio Tinto as a strategic partner for the lithium project in Maricunga, committing a capital contribution of up to US$900 million to develop this initiative",
    "https://www.codelco.com/en/codelco-obtiene-el-ceol-definitivo-para-el-desarrollo-del-litio-en-el",
    "Actor: Rio Tinto (UK/Australia) with Codelco — allied. CapEx-fill: enter up-to USD 900m contribution. Shuffle lithium.",
    "hunt_cycle235", investment_type="jv_equity", evidence="documented", currency="USD",
    value_usd="900000000", fx_usd="1",
    chicago='Codelco. “Codelco obtiene el CEOL definitivo para el desarrollo del litio en el Salar de Maricunga.” February 12, 2026. https://www.codelco.com/en/codelco-obtiene-el-ceol-definitivo-para-el-desarrollo-del-litio-en-el.',
    annotation="Rio Tinto Maricunga CapEx-fill up-to USD 900m. Supports rio_tinto_codelco_maricunga_ceol_2026.",
    evid_note="Opened Codelco English; up to US$900m Rio Tinto capital contribution / CEOL amendment confirmed. CapEx-fill enter USD 900m.",
)

# 8. copper / allied — CapEx-fill Sandvik Marmato ~SEK 250m
row_doc(
    "sandvik_marmato_ug_sek250m_2026",
    "resources", "copper", "allied",
    "Sandvik — Aris Mining Marmato underground fleet (~SEK 250m)",
    "Colombia",
    "1 Apr 2026 Sandvik AB: major underground mining equipment order from Aris Mining for Marmato gold mine (Colombia); valued around SEK 250 million, booked Q1 2026. CapEx-fill: Fed H.10 Sep 25 2026 Sweden krona 9.9047 → USD ~25.24m. Coded copper as underground hard-rock mining equipment (catalog convention).",
    "250000000", SEK_FX_DATE, "2026", "5.475", "-75.601",
    "Marmato mine, Caldas (company geography).",
    "sandvik_marmato_aris_20260401",
    "Sandvik has received a major order for underground mining equipment from the Canadian mining company Aris Mining, to be used at the Marmato gold mine in Colombia. The order is valued at around SEK 250 million and was booked in the first quarter of 2026.",
    "https://www.home.sandvik/en/news-and-media/news/2026/04/sandvik-wins-large-underground-mining-equipment-order-in-colombia/",
    "Actor: Sandvik (Sweden) — allied. CapEx-fill: retain ~SEK 250m; add Fed H.10 Sep 25 2026 FX to USD ~25.24m. Shuffle copper.",
    "hunt_cycle235", investment_type="equipment_supply", evidence="documented", currency="SEK",
    value_usd=str(round(250000000 / float(SEK_USD), 2)), fx_usd=SEK_USD,
    chicago='Sandvik. “Sandvik wins large underground mining equipment order in Colombia.” April 1, 2026. https://www.home.sandvik/en/news-and-media/news/2026/04/sandvik-wins-large-underground-mining-equipment-order-in-colombia/.',
    annotation="Sandvik Marmato CapEx-fill ~USD 25.24m via Fed H.10. Supports sandvik_marmato_ug_sek250m_2026.",
    evid_note="Opened Sandvik English; ~SEK 250m / Marmato / Aris Mining confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 9.9047 SEK/USD.",
)

# 9. solar / us — CapEx-fill AES Panama four-park package >USD 50m on Pesé row
row_doc(
    "aes_panama_pese_10mw_2021",
    "energy", "solar", "us",
    "AES Panamá — Pesé/Mayorca/Cedro/Caoba 4×10 MW solar package (>USD 50m)",
    "Panama",
    "14 Feb 2020 AES Panamá: awards Elecnor EPC for four 10 MW nominal solar parks totaling 40 MW with an investment of more than USD 50 million — Pesé, Mayorca, Cedro & Caoba. CapEx-fill: enter USD 50m floor for the four-park package face on this Pesé row (portfolio CapEx; sister park rows remain presence).",
    "50000000", "2020-02-14", "2020", "7.91", "-80.62",
    "Pesé district, Herrera (company geography; package also Mayorca/Cedro/Caoba).",
    "aes_panama_four_solar_20200214",
    "AES continues to contribute towards the diversification and strengthening of the energy sector in Panama, this time through the announcement of a solar project that contemplates four smaller projects of 10MW each that are distributed through three provinces in the country, with an investment of more than USD $50 million. … Pesé Solar (District of Pesé, Herrera Province), Mayorca Solar (District of Pocrí, Los Santos Province), and Cedro & Caoba Solar (both in the district of Boquerón, Chiriquí Province)",
    "https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables",
    "Actor: AES Panamá (U.S. AES) — us. CapEx-fill: enter >USD 50m floor for four-park package on Pesé row. Shuffle solar / U.S. ≥1/3 budget.",
    "hunt_cycle235", investment_type="greenfield", evidence="documented", currency="USD",
    value_usd="50000000", fx_usd="1",
    chicago='AES Panamá. “AES Panamá aumenta su apuesta a las energías renovables.” February 14, 2020. https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables.',
    annotation="AES Panama four-park CapEx-fill USD 50m floor. Supports aes_panama_pese_10mw_2021.",
    evid_note="Opened AES Panamá English; >USD 50m / 4×10 MW Pesé–Mayorca–Cedro–Caoba confirmed. CapEx-fill enter USD 50m floor.",
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
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
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
    print(f"cycle235 added {len(added)}: {added}")
    print(f"cycle235 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
