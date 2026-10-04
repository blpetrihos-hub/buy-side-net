#!/usr/bin/env python3
"""Cycle 181 hunt: shuffle_seed=20261181; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261181)):
power_plants_grid, building_materials, bridges_roads, nickel, other_renewables,
port_ownership, rail, port_cranes, lithium, copper, balsa, wind, fission_smr,
water, niobium, graphite, engineering_epc, solar.

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


# 1. power_plants_grid / allied — Redeia Redinter LatAm transmission plan
row_doc(
    "redeia_redinter_latam_150m_eur_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Redeia / Redinter — LatAm transmission investment plan (~€150m through 2029)",
    "Brazil",
    "26 Feb 2026 Redeia English: as part of Strategic Plan to 2029, group will roll out an investment plan worth around €150 million focused on strengthening and expanding transmission grids in Brazil, Chile and Peru through subsidiary Redinter. CapEx = EUR 150m plan ceiling (multi-country; no single named build site on opened page). Distinct from isa_nueva_lagunas_kimal_194p46m_2023.",
    "150000000",
    "2026-02-26",
    "2026",
    "",
    "",
    "Redinter LatAm transmission footprint Brazil/Chile/Peru — lat/lon blank (multi-country plan; Brazil tagged as largest Redinter circuit km).",
    "redeia_strategic_plan_latam_20260226",
    "As part of its strategic path until 2029, the group will consolidate its activity in electricity transmission in Latin America and in the field of telecommunications. In the first case, it will roll out an investment plan worth around €150 million, focused on strengthening and expanding the transmission grids in Brazil, Chile and Peru through its subsidiary Redinter.",
    "https://www.redeia.com/en/press-office/news/press-release/2026/02/redeia-increases-its-average-annual-investment-red-electrica-70-implement-next-plan",
    "Actor: Redeia (Spain) via Redinter — allied. Opened Redeia English press 26 Feb 2026. EUR stored without FX (Fed/ECB date-specific pull unreliable). Shuffle lead power_plants_grid.",
    "hunt_cycle181",
    investment_type="greenfield",
    evidence="documented",
    currency="EUR",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Redeia. “Redeia increases its average annual investment in Red Eléctrica by 70% to implement the next Plan.” February 26, 2026. https://www.redeia.com/en/press-office/news/press-release/2026/02/redeia-increases-its-average-annual-investment-red-electrica-70-implement-next-plan.',
    annotation="Redeia: ~€150m Redinter LatAm grid plan BR/CL/PE. Supports redeia_redinter_latam_150m_eur_2026.",
    evid_note="Opened Redeia English press release 2026-10-04.",
)

# 2. power_plants_grid / other — WEG Brazil transformer capacity
row_doc(
    "weg_brazil_xfmr_543m_brl_2024",
    "energy",
    "power_plants_grid",
    "other",
    "WEG — Brazil transformer capacity expansion (Betim + Gravataí; ~R$543m)",
    "Brazil",
    "25 Sep 2024 WEG English: investment plan of approximately R$ 543 million over two years to increase transformer production capacity in Brazil — ~R$370m expanding Betim (MG) power-transformer plant by nearly 24,000 m² (completion 2H 2026; total built area to 75,000 m²) and ~R$128m expanding Gravataí (RS) for transformers up to 230 kV (+7,300 m²; completion Q4 2026) to serve Brazilian and neighboring-country utilities. CapEx = BRL 543m. Distinct from weg_statkraft_seabra_7mw_2025 turbine row and Hitachi LatAm transformer package.",
    "543000000",
    "2024-09-25",
    "2024",
    "-19.968",
    "-44.198",
    "WEG Betim power-transformer plant, Minas Gerais (primary CapEx site; Gravataí RS also in package).",
    "weg_brazil_xfmr_20240925",
    "WEG announces an investment plan of approximately R$ 543 million to increase transformer production capacity in Brazil. The investments will be made over the next two years in manufacturing units located in Minas Gerais and Rio Grande do Sul. In Minas Gerais, the Company will invest approximately R$ 370 million, expanding its power transformer factory in the city of Betim by nearly 24,000 m²… In Rio Grande do Sul, the factory located in the city of Gravataí will receive an investment of approximately R$ 128 million…",
    "https://www.weg.net/institutional/GE/en/news/result-and-investiments/weg-announces-investments-to-expand-transformer-production-capacity-in-brazil",
    "Actor: WEG (Brazilian OEM) — other. Opened WEG English primary 25 Sep 2024. BRL stored without FX.",
    "hunt_cycle181",
    investment_type="manufacturing_presence",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='WEG. “WEG announces investments to expand transformer production capacity in Brazil.” September 25, 2024. https://www.weg.net/institutional/GE/en/news/result-and-investiments/weg-announces-investments-to-expand-transformer-production-capacity-in-brazil.',
    annotation="WEG: R$543m Betim+Gravataí transformer CapEx. Supports weg_brazil_xfmr_543m_brl_2024.",
    evid_note="Opened WEG English institutional news 2026-10-04.",
)

# 3. power_plants_grid / allied — BCIE SIEPAC second circuit
row_doc(
    "bcie_siepac_segundo_circuito_37p2m_2025",
    "energy",
    "power_plants_grid",
    "allied",
    "BCIE / CABEI — SIEPAC Second Circuit financing (USD 37.2m of USD 46.4m)",
    "Honduras",
    "28 Apr 2025 BCIE Spanish: Bank will finance USD 37.2 million of the USD 46.4 million Segundo Circuito SIEPAC project (EPR co-finance >USD 9.2m) — 301.8 km of 230 kV lines plus expansion of Agua Caliente (Honduras), Sandino and La Virgen (Nicaragua), and Fortuna (Costa Rica) substations; +≥300 MW operational exchange capacity on Honduras–Nicaragua and Nicaragua–Costa Rica interconnects. CapEx financing face = USD 37.2m BCIE tranche. Distinct from IDB HO-L1186 national transmission rows.",
    "37200000",
    "2025-04-28",
    "2025",
    "",
    "",
    "SIEPAC second-circuit corridor (Agua Caliente HN / Sandino+La Virgen NI / Fortuna CR) — lat/lon blank (multi-country package; Honduras tagged for Agua Caliente).",
    "bcie_siepac_segundo_20250428",
    "El costo total del proyecto asciende los US$46.4 millones, de los cuales US$37.2 millones serán financiados por el BCIE y más de US$9.2 millones por la Empresa Propietaria de la Red (EPR)… El proyecto contempla la construcción de 301.8 km de líneas de transmisión en 230 kV y la ampliación de cuatro subestaciones estratégicas: “Agua Caliente” (Honduras), “Sandino” (Nicaragua), “La Virgen” (Nicaragua) y “Fortuna” (Costa Rica).",
    "https://www.bcie.org/noticias/en-beneficio-de-50-millones-de-centroamericanos-bcie-fortalece-la-integracion-energetica-regional-con-el-financiamiento-del-segundo-circuito-siepac",
    "Actor: BCIE/CABEI (Central American multilateral) — allied. Opened BCIE Spanish primary 28 Apr 2025.",
    "hunt_cycle181",
    investment_type="financing",
    evidence="documented",
    bib_type="official",
    chicago='Banco Centroamericano de Integración Económica (BCIE). “En beneficio de 50 millones de centroamericanos, BCIE fortalece la integración energética regional con el financiamiento del Segundo Circuito SIEPAC.” April 28, 2025. https://www.bcie.org/noticias/en-beneficio-de-50-millones-de-centroamericanos-bcie-fortalece-la-integracion-energetica-regional-con-el-financiamiento-del-segundo-circuito-siepac.',
    annotation="BCIE: USD 37.2m of SIEPAC second-circuit USD 46.4m. Supports bcie_siepac_segundo_circuito_37p2m_2025.",
    evid_note="Opened BCIE Spanish news page 2026-10-04.",
)

# 4. rail / prc — BOC+ICBC Bogotá Metro Line 1 credit
row_doc(
    "boc_icbc_bogota_metro_230m_2024",
    "infrastructure",
    "rail",
    "prc",
    "Bank of China + ICBC — Metro Línea 1 Bogotá revolving credit (USD 230m)",
    "Colombia",
    "3 Feb 2025 Cuatrecasas (adviser; facility closed Nov 2024 per LatinFinance award write-up): Metro Línea 1 S.A.S. (CHEC 85% / Xi’an Rail 15%) secures USD 230 million revolving credit jointly from Bank of China Limited Panama Branch and Industrial and Commercial Bank of China Panama Branch for construction of Bogotá’s first metro line (23.9 km / 16 stations). Separate COP 1.2 billones local tranche (FDN/BBVA/Banco de Bogotá) not dual-tagged here. CapEx financing face = USD 230m PRC bank tranche.",
    "230000000",
    "2024-11-01",
    "2024",
    "4.65",
    "-74.09",
    "Bogotá Metro Line 1 elevated corridor / Portal Américas–Calle 72 (Cuatrecasas geography; approximate city pin).",
    "cuatrecasas_metro_linea1_20250203",
    "The first line of credit of USD 230 million was provided jointly by the Bank of China (Panama Branch) and the Industrial and Commercial Bank of China (Panama Branch). The second line of COP 1.2 billion was provided by the National Development Finance (FDN), BBVA Colombia and Banco de Bogotá… Congratulations to our clients, China Harbour Engineering Company and Metro Línea 1…",
    "https://www.cuatrecasas.com/en/latam/art/metro-linea-1-secures-financing-build-first-metro-line-bogota",
    "Actor: Bank of China + ICBC (PRC state banks) financing CHEC/Xi’an Metro Línea 1 concessionaire — prc. Opened Cuatrecasas English primary 3 Feb 2025. USD 230m tranche only (local COP facility not entered). Shuffle rail slot.",
    "hunt_cycle181",
    investment_type="financing",
    evidence="documented",
    bib_type="press",
    chicago='Cuatrecasas. “Metro Línea 1 secures financing to build first metro line in Bogotá.” February 3, 2025. https://www.cuatrecasas.com/en/latam/art/metro-linea-1-secures-financing-build-first-metro-line-bogota.',
    annotation="Cuatrecasas: BOC+ICBC USD 230m revolving credit for Bogotá Metro Line 1. Supports boc_icbc_bogota_metro_230m_2024.",
    evid_note="Opened Cuatrecasas English LatAm article 2026-10-04; COP figure on English page appears mistranslated vs Spanish billones — USD 230m tranche used only.",
)

# 5. copper / allied — Sandvik Alumbrera DR413i ×3
row_doc(
    "sandvik_alumbrera_dr413i_3_2026",
    "resources",
    "copper",
    "allied",
    "Sandvik — three DR413i rotary blasthole drills for Glencore Alumbrera restart",
    "Argentina",
    "24 Apr 2026 Sandvik Mining: order from Glencore for three DR413i rotary blasthole drill rigs for Bajo de la Alumbrera copper restart (Argentina); booked Q1 2026; first unit April 2026, remaining two Q4 2026; plus rebuilds for three D75KS and three DP1500 and fleet maintenance labor/parts. Ops restart expected 2027 / first production 2028; ~73 kt Cu through Jun 2031 initial four-year life. CapEx USD not disclosed — blank. Distinct from caterpillar_finning_alumbrera_250m_2026 Cat fleet row.",
    "",
    "",
    "2026",
    "",
    "",
    "Bajo de la Alumbrera copper mine, Catamarca (Sandvik geography) — lat/lon blank pending verified pit pin.",
    "sandvik_alumbrera_dr413i_20260424",
    "Sandvik has secured an order from Glencore to supply three DR413i rotary blasthole drill rigs for the restart of the Bajo de la Alumbrera copper mine in Argentina. The order was booked in Q1 2026. The first DR413i is scheduled to arrive in Argentina in April with the remaining two following in Q4 2026. Additionally, Sandvik will provide rebuild services to Glencore for three D75KS rotary blasthole drill rigs and three DP1500 crawled-based surface drill rigs, as well as labor and parts for maintenance of the whole fleet.",
    "https://www.mining.sandvik/en/news-and-media/news-archive/2026/04/sandvik-to-supply-three-dr413i-rotary-drill-rigs-to-glencore-for-alumbrera-restart/",
    "Actor: Sandvik (Sweden) — allied; Glencore host. Opened Sandvik Mining English primary 24 Apr 2026. CapEx blank.",
    "hunt_cycle181",
    investment_type="equipment_supply",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Sandvik Mining. “Sandvik to supply three DR413i rotary drill rigs to Glencore for Alumbrera restart.” April 24, 2026. https://www.mining.sandvik/en/news-and-media/news-archive/2026/04/sandvik-to-supply-three-dr413i-rotary-drill-rigs-to-glencore-for-alumbrera-restart/.',
    annotation="Sandvik: 3× DR413i for Alumbrera restart (CapEx blank). Supports sandvik_alumbrera_dr413i_3_2026.",
    evid_note="Opened Sandvik Mining English news 2026-10-04.",
)

# 6. copper / allied — Epiroc Peru Pit Viper order
row_doc(
    "epiroc_peru_pit_viper_sek210m_2026",
    "resources",
    "copper",
    "allied",
    "Epiroc — Pit Viper 351 fleet order for major Peru copper mine (~SEK 210m)",
    "Peru",
    "15 Jul 2026 Epiroc: large order for Pit Viper 351 surface blasthole drill rigs plus tools/spares/on-site services/training for a major Peru copper mine operated by a consortium of leading Chinese investment companies and an Australia-headquartered mining company (operator); order valued around SEK 210 million, booked Q2 2026; deliveries end-2026 through 1H 2027. CapEx = SEK 210m. Mine unnamed on page — lat/lon blank. Distinct from caterpillar_las_bambas_fleet_2026.",
    "210000000",
    "2026-07-15",
    "2026",
    "",
    "",
    "Unnamed major Peru copper mine (Epiroc: Chinese investors + Australian operator consortium) — lat/lon blank (site not named).",
    "epiroc_peru_pit_viper_20260715",
    "Epiroc AB… has won a large order for mining equipment for a major copper mine in Peru. The Peruvian mine is operated by a consortium comprising leading Chinese investment companies and a globally recognized mining company headquartered in Australia, which also serves as the mine operator. The customer ordered a fleet of Pit Viper 351 surface blasthole drill rigs that will support the mine’s expansion… The equipment order is valued at around SEK 210 million and was booked in the second quarter 2026.",
    "https://www.epirocgroup.com/en/media/corporate-press-releases/2026/20260715-epiroc-wins-large-order-for-mining-equipment-in-peru",
    "Actor: Epiroc (Sweden) — allied. Opened Epiroc English primary 15 Jul 2026. SEK stored without FX. Description matches MMG Las Bambas ownership pattern but mine not named on page — no pin.",
    "hunt_cycle181",
    investment_type="equipment_supply",
    evidence="documented",
    currency="SEK",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Epiroc AB. “Epiroc wins large order for mining equipment in Peru.” July 15, 2026. https://www.epirocgroup.com/en/media/corporate-press-releases/2026/20260715-epiroc-wins-large-order-for-mining-equipment-in-peru.',
    annotation="Epiroc: ~SEK 210m Pit Viper 351 Peru copper order. Supports epiroc_peru_pit_viper_sek210m_2026.",
    evid_note="Opened Epiroc corporate press release 2026-10-04.",
)

# 7. copper / allied — Sandvik CoMinVi Mexico underground fleet
row_doc(
    "sandvik_cominvi_mexico_sek340m_2026",
    "resources",
    "copper",
    "allied",
    "Sandvik — CoMinVi Mexico underground fleet order (~SEK 340m; 46 units)",
    "Mexico",
    "3 Jul 2026 Sandvik AB: large underground equipment order from Constructora Minera Villagómez (CoMinVi) for several Mexico contract sites; valued around SEK 340 million, booked Q2 2026; trucks/loaders/drill rigs; deliveries 2026–2028. Mining Sandvik detail page: 46 units (12 Toro TH430, 11 DS311 bolters, 10 Toro LH410, 7 TH545i, 4 LH514, 2 TH320) within 73-unit 2025–26 CoMinVi Sandvik total; parts/rebuilds four years. CapEx = SEK 340m. Multi-site Mexico — lat/lon blank. Coded copper as underground hard-rock mining equipment (catalog convention for Sandvik/Epiroc mine fleets).",
    "340000000",
    "2026-07-03",
    "2026",
    "",
    "",
    "CoMinVi underground mining contracts across Mexico — lat/lon blank (multi-site; no single named mine on opened Sandvik pages).",
    "sandvik_cominvi_mexico_20260703",
    "Sandvik has received a large underground equipment order from the Mexico-based mining contractor Constructora Minera Villagómez S.A. de C.V. (CoMinVi), for use at several of its contract sites across Mexico. The order is valued at around SEK 340 million and was booked in the second quarter. The order includes trucks, loaders and drill rigs, with deliveries expected to begin during 2026 and continue through 2028.",
    "https://www.home.sandvik/en/news-and-media/news/2026/07/sandvik-wins-large-underground-equipment-order-in-mexico-from-mining-contractor-cominvi/",
    "Actor: Sandvik (Sweden) — allied; CoMinVi (Mexico contractor) buyer. Opened Sandvik Group English primary 3 Jul 2026. SEK stored without FX.",
    "hunt_cycle181",
    investment_type="equipment_supply",
    evidence="documented",
    currency="SEK",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Sandvik AB. “Sandvik wins large underground equipment order in Mexico from mining contractor CoMinVi.” July 3, 2026. https://www.home.sandvik/en/news-and-media/news/2026/07/sandvik-wins-large-underground-equipment-order-in-mexico-from-mining-contractor-cominvi/.',
    annotation="Sandvik: ~SEK 340m CoMinVi Mexico 46-unit underground fleet. Supports sandvik_cominvi_mexico_sek340m_2026.",
    evid_note="Opened Sandvik Group English press 2026-10-04; unit breakdown cross-checked on mining.sandvik CoMinVi feature.",
)

# 8. water / us — NADBank Nuevo Laredo BEIF grant
row_doc(
    "nadbank_nuevo_laredo_beif_8m_2025",
    "resources",
    "water",
    "us",
    "NADBank / EPA BEIF — Nuevo Laredo Colector Ribereño + Donato Guerra sewer mains (USD 8m)",
    "Mexico",
    "3 Oct 2025 NADBank: groundbreaking for rehabilitation of Colector Ribereño and Colector Donato Guerra sewer mains within Nuevo Laredo Comprehensive Wastewater Collection and Treatment Project (COMAPA); NADBank providing USD 8 million BEIF grants funded by U.S. EPA. Total project ~MXN 1,398.4m (~USD 81.2m) with BEIF + commercial loan up to MXN 120m (~USD 6m) + Mexican public funds MXN 904.4m (~USD 53.2m). CapEx financing face = USD 8m BEIF grant. Distinct from nadbank_cespt_tijuana_sewer_4p2m_2026 / Sonora MXN 650m.",
    "8000000",
    "2025-10-03",
    "2025",
    "27.486",
    "-99.507",
    "Nuevo Laredo wastewater collectors / COMAPA system, Tamaulipas (NADBank geography; approximate municipal pin).",
    "nadbank_nuevo_laredo_beif_20251003",
    "These specific works will rehabilitate the Colector Ribereño and the Colector Donato Guerra. NADBank is providing $8 million dollars in grants from the Bank's Border Environment Infrastructure Fund (BEIF), funded by the U.S. Environmental Protection Agency (EPA)… The total project cost amounts to MX$1,398.4 million (~US$81.2 million)…",
    "https://nadbank.org/news/press-release/groundbreaking-ceremony-for-the-rehabilitation-of-two-wastewater-sewer-mains-in-nuevo-laredo-tamaulipas",
    "Actor: NADBank administering EPA BEIF (U.S.–Mexico binational; catalogued us) — us. Opened NADBank English release 3 Oct 2025. U.S. side-balance water.",
    "hunt_cycle181",
    investment_type="grant",
    evidence="documented",
    bib_type="official",
    chicago='North American Development Bank. “Groundbreaking ceremony for the rehabilitation of two wastewater sewer mains in Nuevo Laredo, Tamaulipas.” October 3, 2025. https://nadbank.org/news/press-release/groundbreaking-ceremony-for-the-rehabilitation-of-two-wastewater-sewer-mains-in-nuevo-laredo-tamaulipas.',
    annotation="NADBank/EPA BEIF: USD 8m Nuevo Laredo sewer mains. Supports nadbank_nuevo_laredo_beif_8m_2025.",
    evid_note="Opened NADBank English press release 2026-10-04.",
)

# Thin top-up + remaining shuffle slots dry: building_materials, bridges_roads, nickel,
# other_renewables, port_ownership, port_cranes, lithium, balsa, wind, fission_smr,
# niobium, graphite, engineering_epc, solar (catalog dense; holdovers unsigned).


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
    print(f"cycle181 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
