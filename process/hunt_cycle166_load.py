#!/usr/bin/env python3
"""Cycle 166 hunt: shuffle_seed=20261166; equal budget; U.S./PRC split; thin after.

Canonical shuffle: power_plants_grid, other_renewables, graphite, lithium, port_cranes,
building_materials, engineering_epc, copper, rail, fission_smr, solar, niobium, water,
nickel, bridges_roads, wind, balsa, port_ownership.

Thin: balsa/fission/niobium once (dry); nickel+graphite already used this session.
Prioritize US fills after cycle-165 US dry.
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


# 1. power_plants_grid / allied — Abengoa Chile ANDE Chaco Lote 2
row_doc(
    "abengoa_ande_chaco_lote2_29p7m_paraguay",
    "energy",
    "power_plants_grid",
    "allied",
    "Abengoa Chile / LT S.A. (Consorcio Eléctrico Chaqueño) — ANDE Chaco 220 kV Lote 2",
    "Paraguay",
    "30 May 2025 Agencia IP / ANDE: Lote 2 of Villa Hayes–Villa Real 220 kV transmission (217 km) awarded to Consorcio Eléctrico Chaqueño (LT S.A. – Abengoa Chile S.A.) for USD 29.7 million; 18-month execution. Part of USD 96m Chaco package (KfW/FONPLATA/ANDE). Fills Paraguay×power_plants_grid empty cell.",
    "29700000",
    "2025-05-30",
    "2025",
    "-25.090",
    "-57.560",
    "Subestación Villa Hayes start of Lote 2 corridor, Presidente Hayes, Paraguay.",
    "ip_ande_chaco_220kv_20250530",
    "Lote 2: Construcción de la línea de transmisión en 220 kV entre Villa Hayes y Villa Real (217 km), adjudicada al Consorcio Eléctrico Chaqueño (LT S.A. – Abengoa Chile S.A.) por un monto de USD 29.700.000, con un plazo de 18 meses.",
    "https://www.ip.gov.py/ip/2025/05/30/ande-firma-contrato-para-construir-linea-de-220-kv-e-impulsar-el-desarrollo-socioeconomico-en-el-chaco/",
    "Actor: Abengoa Chile S.A. (Spanish Abengoa group) via Consorcio Eléctrico Chaqueño — allied. Agencia IP primary quoting ANDE lot awards. USD 29.7m Lote 2 face. Distinct from Lote 3 row.",
    "hunt_br_power_equip",
    investment_type="epc",
    bib_type="government",
    chicago='Agencia de Información Pública (Paraguay). “ANDE firma contrato para construir línea de 220 KV e impulsar el desarrollo en el Chaco.” May 30, 2025. https://www.ip.gov.py/ip/2025/05/30/ande-firma-contrato-para-construir-linea-de-220-kv-e-impulsar-el-desarrollo-socioeconomico-en-el-chaco/.',
    annotation="Agencia IP/ANDE: Chaco 220 kV Lote 2 Abengoa Chile USD 29.7m. Supports abengoa_ande_chaco_lote2_29p7m_paraguay.",
    evid_note="Opened Agencia IP 30 May 2025 ANDE Chaco 220 kV contract signing page.",
)

# 2. power_plants_grid / allied — Abengoa Chile ANDE Chaco Lote 3
row_doc(
    "abengoa_ande_chaco_lote3_35p7m_paraguay",
    "energy",
    "power_plants_grid",
    "allied",
    "Abengoa Chile / LT S.A. (Consorcio Eléctrico Chaqueño) — ANDE Chaco 220 kV Lote 3",
    "Paraguay",
    "30 May 2025 Agencia IP / ANDE: Lote 3 Villa Real–Pozo Colorado–Loma Plata 220 kV (339 km) awarded to same Consorcio Eléctrico Chaqueño (LT S.A. – Abengoa Chile S.A.) for USD 35.7 million; 20-month execution. New Pozo Colorado 50 MVA substation in package. Distinct from Lote 2.",
    "35700000",
    "2025-05-30",
    "2025",
    "-23.500",
    "-58.800",
    "Pozo Colorado area on Villa Real–Loma Plata 220 kV corridor, Presidente Hayes, Paraguay (approximate).",
    "ip_ande_chaco_220kv_20250530",
    "Lote 3: Construcción de la línea de transmisión en 220 kV entre Villa Real – Pozo Colorado – Loma Plata (339 km), adjudicada al mismo consorcio, por USD 35.700.000 y un plazo de ejecución de 20 meses.",
    "https://www.ip.gov.py/ip/2025/05/30/ande-firma-contrato-para-construir-linea-de-220-kv-e-impulsar-el-desarrollo-socioeconomico-en-el-chaco/",
    "Actor: Abengoa Chile S.A. (Spanish Abengoa group) — allied. Same Agencia IP/ANDE primary. USD 35.7m Lote 3 face.",
    "hunt_br_power_equip",
    investment_type="epc",
    bib_type="government",
    chicago='Agencia de Información Pública (Paraguay). “ANDE firma contrato para construir línea de 220 KV e impulsar el desarrollo en el Chaco.” May 30, 2025. https://www.ip.gov.py/ip/2025/05/30/ande-firma-contrato-para-construir-linea-de-220-kv-e-impulsar-el-desarrollo-socioeconomico-en-el-chaco/.',
    annotation="Agencia IP/ANDE: Chaco 220 kV Lote 3 Abengoa Chile USD 35.7m. Supports abengoa_ande_chaco_lote3_35p7m_paraguay.",
    evid_note="Opened Agencia IP 30 May 2025 ANDE Chaco 220 kV contract signing page (Lote 3).",
)

# 3. port_cranes / prc — Jiangsu Rainbow 4 RTGs Puerto Corinto
row_doc(
    "jiangsu_rainbow_corinto_4rtg_nicaragua_2026",
    "infrastructure",
    "port_cranes",
    "prc",
    "Jiangsu Rainbow — 4 RTG quay/yard cranes (Puerto Corinto)",
    "Nicaragua",
    "SPIEX (Nicaragua government) + TN8: Puerto Corinto commissioned four Chinese RTG cranes (up to 41 t; stack 6 rows / 5 levels; 20–25 moves/hour) supplied by Jiangsu Rainbow, with reach stackers (SANY) and Yantai Jiajia weighbridges; CAMCE named for later phases to 150,000 DWT vessels. CapEx blank. Fills Nicaragua×port_cranes empty cell.",
    "",
    "",
    "2026",
    "12.480",
    "-87.170",
    "Puerto Corinto, Chinandega, Nicaragua.",
    "spiex_corinto_rtg_2026",
    "supervisaron la entrada en funcionamiento de cuatro grúas RTG con capacidad de hasta 41 toneladas… Pueden apilar hasta seis filas y elevar carga a cinco niveles, realizando entre 20 y 25 movimientos por hora… Estos equipos han sido suministrados por empresas como Jiangsu Rainbow, Yantai Jiajia y SANY",
    "https://spiex.gob.ni/es/noticias/puerto-corinto-sigue-modernizandose-con-cuatro-nuevas-gruas-rtg-y-apiladoras/",
    "Actor: Jiangsu Rainbow (PRC) RTG supply — prc. SPIEX government primary. CapEx blank. First Nicaragua port_cranes row.",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    bib_type="government",
    chicago='Secretaría de Políticas e Inversiones Extranjeras (SPIEX), Nicaragua. “Puerto Corinto sigue modernizándose con cuatro nuevas grúas RTG y apiladoras.” 2026. https://spiex.gob.ni/es/noticias/puerto-corinto-sigue-modernizandose-con-cuatro-nuevas-gruas-rtg-y-apiladoras/.',
    annotation="SPIEX primary: Jiangsu Rainbow 4 RTGs at Puerto Corinto. Supports jiangsu_rainbow_corinto_4rtg_nicaragua_2026.",
    evid_note="Opened SPIEX Corinto RTG modernization notice (Jiangsu Rainbow / SANY / Yantai).",
)

# 4. engineering_epc / us — Trigon Cap-Haïtien port CM
row_doc(
    "trigon_cap_haitien_port_cm_43m",
    "infrastructure",
    "engineering_epc",
    "us",
    "Trigon Associates — Cap-Haïtien Port Improvement construction management (USAID)",
    "Haiti",
    "Trigon Associates (New Orleans) portfolio: prime contractor under USAID A-E IDIQ providing full-service construction management / contract administration for Cap-Haïtien Port Improvement Project; stated Cost USD 43 million. CapEx/investment = USD 43m project face on company page. Fills Haiti×port CM / engineering presence beyond Fluor NEC.",
    "43000000",
    "2017-09-29",
    "2017",
    "19.760",
    "-72.200",
    "Cap-Haïtien Port, Nord, Haiti.",
    "trigon_cap_haitien_port_cm",
    "As the Prime contractor under our USAID A-E IDIQ contract, Trigon Associates provided full-service construction management consulting and contract administration support for the Cap-Haïtien Port Improvement Project in Haiti. … Cost$43M",
    "https://trigonassociates.com/portfolio/construction-management-consulting-services-at-cap-haitien-port/",
    "Actor: Trigon Associates (U.S.) for USAID/Haiti — us. Company English primary. USD 43m stated project cost. Year from USAID CHP CM window context; company page undated — evidence=documented cost face.",
    "hunt_infra_engineering_epc",
    investment_type="epc",
    bib_type="company",
    chicago='Trigon Associates. “Construction Management Consulting Services at Cap-Haïtien Port.” https://trigonassociates.com/portfolio/construction-management-consulting-services-at-cap-haitien-port/.',
    annotation="Trigon primary: Cap-Haïtien Port Improvement CM; Cost USD 43m. Supports trigon_cap_haitien_port_cm_43m.",
    evid_note="Opened Trigon Cap-Haïtien Port CM portfolio page (Cost USD 43m).",
)

# 5. copper / us — Freeport Sierra Azul earn-in 2025 program
row_doc(
    "fcx_max_sierra_azul_4p8m_colombia_2025",
    "resources",
    "copper",
    "us",
    "Freeport-McMoRan Exploration — Sierra Azul (Cesar) copper-silver earn-in 2025 program",
    "Colombia",
    "25 Feb 2025 Max Resource: Freeport-McMoRan Exploration Corporation fully funds approved USD 4.8 million 2025 exploration budget at Sierra Azul (formerly Cesar) copper-silver project, NE Colombia; earn-in option up to 80% via C$50m cumulative expenditures + C$1.55m cash (May 2024 EIA). CapEx/investment = USD 4.8m 2025 program face. Fills Colombia copper US side (prior PRC Alacrán/JCHX).",
    "4800000",
    "2025-02-25",
    "2025",
    "10.480",
    "-73.250",
    "Sierra Azul / Cesar Basin AM district, Cesar department, Colombia (approximate).",
    "max_resource_sierra_azul_20250225",
    "The US $4.8 million budget for 2025, fully funded by Freeport, is an increase of 14% compared with 2024 … Freeport can earn an 80% interest in the Sierra Azul Copper-Silver Project in two stages by spending an aggregate amount of $50 million and paying a total of $1.55 million in cash to Max.",
    "https://www.maxresource.com/20250225-max-resource-reports-1.6-copper-over-55-metres-at-sierra-azul",
    "Actor: Freeport-McMoRan Exploration (U.S., NYSE: FCX affiliate) — us. Max Resource English primary. USD 4.8m 2025 program; earn-in to 80%.",
    "hunt_res_copper",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Max Resource Corp. “Max Resource Reports 1.6% Copper Over 55 Metres at Sierra Azul.” February 25, 2025. https://www.maxresource.com/20250225-max-resource-reports-1.6-copper-over-55-metres-at-sierra-azul.',
    annotation="Max Resource primary: Freeport-funded USD 4.8m 2025 Sierra Azul program. Supports fcx_max_sierra_azul_4p8m_colombia_2025.",
    evid_note="Opened Max Resource 25 Feb 2025 Sierra Azul assay / Freeport budget release.",
)

# 6. solar / allied — JPS Marubeni/EWP USD 300m solar+BESS
row_doc(
    "jps_marubeni_300m_solar_bess_jamaica_2025",
    "energy",
    "solar",
    "allied",
    "JPS (Marubeni / Korea East-West Power) — 133 MW solar + 171.5 MW BESS program",
    "Jamaica",
    "JPS Annual Report 2024: Government approved JPS plan to replace existing generation with 133 MW solar and 171.5 MW battery storage; invest approximately USD 300 million between 2025 and 2028. JPS majority privately owned by Marubeni (Japan, 40%) and Korea East-West Power (40%). CapEx = USD 300m face. Fills Jamaica×solar empty cell. BESS portion overlaps other_renewables taxonomy but program framed as solar+storage replacement.",
    "300000000",
    "2025-04-30",
    "2025",
    "17.970",
    "-76.790",
    "Hunts Bay / Kingston generation complex context, Jamaica (program multi-site; pin approximate).",
    "jps_ar_2024_solar_bess_300m",
    "Our future projects include the development of new renewable generating facilities and the integration of battery energy storage systems … the Government has approved our plans to replace existing generation with 133 MW of solar energy and 171.5 MW of Battery Storage. We will invest approximately US$300 million in these projects between 2025 and 2028.",
    "https://www.jpsco.com/wp-content/uploads/2025/04/JPS-AR-2024-MM-FINAL-300425-SPREADS.pdf",
    "Actor: JPS under Marubeni (Japan HQ) / EWP ownership — allied (Japan lead). JPS AR 2024 primary PDF. USD 300m 2025–28 program face.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='Jamaica Public Service Company Limited. “Annual Report 2024.” April 2025. https://www.jpsco.com/wp-content/uploads/2025/04/JPS-AR-2024-MM-FINAL-300425-SPREADS.pdf.',
    annotation="JPS AR 2024: USD 300m for 133 MW solar + 171.5 MW BESS (2025–28). Supports jps_marubeni_300m_solar_bess_jamaica_2025.",
    evid_note="Opened JPS Annual Report 2024 PDF (USD 300m solar+BESS approval).",
)

# 7. wind / allied — Vestas Costa Rica 22 MW order
row_doc(
    "vestas_costa_rica_22mw_order_2025",
    "energy",
    "wind",
    "allied",
    "Vestas — 22 MW Costa Rica wind order (5× V117-4.3 MW)",
    "Costa Rica",
    "29 Sep 2025 Vestas Q3 order intake: Costa Rica Americas order 22 MW — 5× V117-4.3 MW turbines with 8-year AOM 4000 service; delivery and commissioning planned 2026; customer/project undisclosed. CapEx blank (equipment order). Fills Costa Rica×wind empty cell.",
    "",
    "",
    "2025",
    "10.470",
    "-84.970",
    "Guanacaste wind corridor (Tilarán/Bagaces area typical for ICE private wind block; approximate — site undisclosed).",
    "vestas_q3_orders_20250929",
    "Costa Rica | Americas | Undisclosed | Undisclosed | 22 | 5 x V117-4.3 MW | 8-year AOM 4000 Service Agreement | Delivery and commissioning are planned for 2026",
    "https://www.vestas.com/en/media/company-news/2025/vestas-announces-four-new-orders-for-a-total-of-132-mw-c4241543",
    "Actor: Vestas Wind Systems A/S (Denmark HQ) — allied. Company English primary. CapEx blank. First Costa Rica wind row.",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Vestas Wind Systems A/S. “Vestas Announces Four New Orders for a Total of 132 MW.” September 29, 2025. https://www.vestas.com/en/media/company-news/2025/vestas-announces-four-new-orders-for-a-total-of-132-mw-c4241543.',
    annotation="Vestas primary: 22 MW Costa Rica order (5× V117-4.3). Supports vestas_costa_rica_22mw_order_2025.",
    evid_note="Opened Vestas 29 Sep 2025 Q3 order intake release.",
)

# 8. port_ownership / allied — KFTL/CMA Westlands USD 80m
row_doc(
    "kftl_cma_westlands_80m_jamaica_2025",
    "infrastructure",
    "port_ownership",
    "allied",
    "Kingston Freeport Terminal / CMA Terminals — Westlands Expansion (USD 80m)",
    "Jamaica",
    "11 Jul 2025 Jamaica Observer: PAJ / KFTL / CMA Terminals Holding launch Westlands Expansion Project — USD 80 million for 15 ha of new storage, security upgrades, automated domestic gate; ~25% storage capacity increase. KFTL is CMA CGM subsidiary under 30-year Kingston Container Terminal concession (from 2016). CapEx = USD 80m face. Fills Jamaica×port_ownership empty cell.",
    "80000000",
    "2025-07-11",
    "2025",
    "17.980",
    "-76.820",
    "Kingston Freeport Terminal / Westlands, Kingston Harbour, Jamaica.",
    "jamaica_observer_kftl_westlands_20250711",
    "Operations at Kingston Freeport Terminal (KFTL) are set to expand across 15 more hectares under the newly launched Westlands Expansion Project, a US$80-million investment aimed at easing congestion, boosting cargo capacity… The initiative — a joint effort between the Port Authority of Jamaica (PAJ), KFTL, and CMA Terminals Holding",
    "https://www.jamaicaobserver.com/2025/07/11/us80-m-port-expansion/",
    "Actor: KFTL / CMA Terminals Holding (CMA CGM, France HQ) — allied. Press with PM/PAJ groundbreaking quotes — evidence=proxy for CapEx figure (UNVERIFIED press) though actors/site named; value stored as proxy.",
    "hunt_infra_port_ownership",
    investment_type="concession",
    evidence="proxy",
    bib_type="news",
    chicago='Williams, Jerome. “US$80-m Port Expansion.” Jamaica Observer, July 11, 2025. https://www.jamaicaobserver.com/2025/07/11/us80-m-port-expansion/.',
    annotation="Jamaica Observer: KFTL/CMA Westlands USD 80m expansion (proxy CapEx). Supports kftl_cma_westlands_80m_jamaica_2025.",
    evid_note="Opened Jamaica Observer 11 Jul 2025 Westlands groundbreaking article.",
)

# 9. wind / us — USTDA Jamaica offshore wind feasibility
row_doc(
    "ustda_jamaica_offshore_wind_875k",
    "energy",
    "wind",
    "us",
    "USTDA / Keystone Engineering — Jamaica offshore wind feasibility study grant",
    "Jamaica",
    "Keystone Engineering project page: 2017 Petroleum Corporation of Jamaica awarded ~USD 875,000 USTDA grant for technical/economic feasibility and implementation plan for utility-scale offshore wind off Jamaica’s south coast; Keystone prime contractor (resource assessment, foundations, logistics, U.S. supplier register). CapEx/investment = USD 875k grant face. Fills Jamaica×wind empty US cell (study, not construction).",
    "875000",
    "2017-01-01",
    "2017",
    "17.850",
    "-77.200",
    "South coast offshore wind study area, Jamaica (approximate coastal pin).",
    "keystone_jamaica_offshore_wind_ustda",
    "In 2017, the Petroleum Corporation of Jamaica was awarded an approximately $875,000 grant from the US Trade and Development Agency (USTDA) to develop a technical and economic feasibility study and implementation plan for a utility-scale offshore wind farm off the coast of Jamaica. … Keystone served as the prime contractor for the effort.",
    "https://www.keystoneengr.com/projects/jamaica-offshore-wind-farm-study",
    "Actor: USTDA (U.S. government) / Keystone Engineering (U.S.) — us. Company English primary. USD 875k grant. Study-only — not FID construction.",
    "hunt_energy_wind",
    investment_type="financing",
    bib_type="company",
    chicago='Keystone Engineering Inc. “Jamaica Offshore Wind Farm Study.” https://www.keystoneengr.com/projects/jamaica-offshore-wind-farm-study.',
    annotation="Keystone primary: USTDA ~USD 875k Jamaica offshore wind feasibility. Supports ustda_jamaica_offshore_wind_875k.",
    evid_note="Opened Keystone Jamaica offshore wind USTDA study page.",
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
    print(f"Cycle 166 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
