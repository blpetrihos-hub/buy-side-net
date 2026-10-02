#!/usr/bin/env python3
"""Cycle 171 hunt: shuffle_seed=20261171; equal budget; U.S./PRC split; thin after.

Canonical shuffle (codebook order + Random(20261171)): other_renewables,
port_cranes, graphite, balsa, niobium, power_plants_grid, copper, bridges_roads,
lithium, solar, port_ownership, wind, fission_smr, nickel, engineering_epc,
building_materials, water, rail.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
balsa filled (Balsa de Colombia presence); nickel/fission dry this pass.
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC rail past MoU.
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


# 1. graphite / prc — Data México 2024 China→Mexico natural graphite imports
row_doc(
    "data_mexico_graphite_china_imp_2024",
    "resources",
    "graphite",
    "prc",
    "China — Mexico HS 2504 natural graphite imports (Data México)",
    "Mexico",
    "2024: Data México (SE Economía) reports Mexico natural-graphite imports from China at USD 437k (HS 2504). Trade-flow presence; not a mine CapEx. Paired same-year U.S. origin (data_mexico_graphite_us_imp_2024). Updates 2023 WITS Mexico×graphite China cell.",
    "437000",
    "2024-12-31",
    "2024",
    "19.430",
    "-99.130",
    "Mexico import gateway proxy (national pin; not a single mill).",
    "data_mexico_graphite_2504_2024",
    "Los países con más Exportaciones a México en 2024 fueron Estados Unidos (US$4.72M), Brasil (US$649k), Canadá (US$528k), China (US$437k) y Mozambique (US$168k).",
    "https://www.economia.gob.mx/datamexico/es/profile/product/natural-graphite",
    "Actor: China export origin into Mexico — prc. Opened Data México official product page (SE). Paired U.S. 2024 row. Thin graphite.",
    "hunt_cycle171",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='México, Secretaría de Economía. “Grafito Natural — Intercambio comercial” (Data México, HS 2504). 2024. https://www.economia.gob.mx/datamexico/es/profile/product/natural-graphite.',
    annotation="Data México: 2024 Mexico natural-graphite imports by origin. Supports data_mexico_graphite_china_imp_2024 / data_mexico_graphite_us_imp_2024.",
    evid_note="Opened Data México HS 2504 product page 2026-10-02.",
    pair_id="data_mexico_graphite_2024_us_cn",
    counterpart_side="us",
    counterpart_actor="United States",
    counterpart_value="4720000",
    counterpart_currency="USD",
    counterpart_value_usd="4720000",
    gap="",
)

# 2. graphite / us — Data México 2024 US→Mexico natural graphite imports
row_doc(
    "data_mexico_graphite_us_imp_2024",
    "resources",
    "graphite",
    "us",
    "United States — Mexico HS 2504 natural graphite imports (Data México)",
    "Mexico",
    "2024: Data México (SE Economía) reports Mexico natural-graphite imports from the United States at USD 4.72M (HS 2504). Trade-flow presence; not a mine CapEx. Paired same-year China origin (data_mexico_graphite_china_imp_2024).",
    "4720000",
    "2024-12-31",
    "2024",
    "19.430",
    "-99.130",
    "Mexico import gateway proxy (national pin; not a single mill).",
    "data_mexico_graphite_2504_2024",
    "Los países con más Exportaciones a México en 2024 fueron Estados Unidos (US$4.72M), Brasil (US$649k), Canadá (US$528k), China (US$437k) y Mozambique (US$168k).",
    "https://www.economia.gob.mx/datamexico/es/profile/product/natural-graphite",
    "Actor: United States export origin into Mexico — us. Opened Data México official product page (SE). Paired China 2024 row. Thin graphite + U.S. side-balance.",
    "hunt_cycle171",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='México, Secretaría de Economía. “Grafito Natural — Intercambio comercial” (Data México, HS 2504). 2024. https://www.economia.gob.mx/datamexico/es/profile/product/natural-graphite.',
    annotation="Data México: 2024 Mexico natural-graphite imports by origin. Supports data_mexico_graphite_us_imp_2024 / data_mexico_graphite_china_imp_2024.",
    evid_note="Opened Data México HS 2504 product page 2026-10-02.",
    pair_id="data_mexico_graphite_2024_us_cn",
    counterpart_side="prc",
    counterpart_actor="China",
    counterpart_value="437000",
    counterpart_currency="USD",
    counterpart_value_usd="437000",
    gap="",
)

# 3. balsa / other — Balsa de Colombia presence (Lebrija, Santander)
row_doc(
    "balsa_de_colombia_presence",
    "resources",
    "balsa",
    "other",
    "Balsa de Colombia — plantation processing/export (Lebrija, Santander)",
    "Colombia",
    "Company site: Balsa de Colombia (since 1994) states reforestation, processing and commercialization of balsa from Lebrija, Santander; exports to markets including the United States and China (also DR, EU, Korea, Japan). CapEx blank (presence/export claim; no named CapEx figure on opened page). Thin balsa top-up; Colombia×balsa under-covered cell.",
    "",
    "",
    "2026",
    "",
    "",
    "Lebrija, Santander (Calle 7 #15-33/35) — lat/lon blank pending verified worksite coords.",
    "balsa_de_colombia_site_2026",
    "Desde 1994 exportamos madera balsa de calidad premium a todo el mundo, con una sólida presencia en mercados líderes como Estados Unidos… Exportamos a todo el mundo, con presencia en mercados como Estados Unidos… China…",
    "https://balsadecolombia.com.co/",
    "Actor: Colombian private balsa processor/exporter — other. Opened company site 2026-10-02. CapEx blank. Distinct from Plantabal/Sinobalsa Ecuador rows.",
    "hunt_cycle171",
    investment_type="ownership_equity",
    evidence="documented",
    bib_type="company",
    chicago='Balsa de Colombia. “Reforestación, procesamiento y comercialización de la madera balsa.” Company website. Accessed October 2, 2026. https://balsadecolombia.com.co/.',
    annotation="Balsa de Colombia company site: export markets include U.S. and China. Supports balsa_de_colombia_presence.",
    evid_note="Opened balsadecolombia.com.co company site 2026-10-02.",
)

# 4. power_plants_grid / prc — PowerChina Coca Codo AOM fee USD 46m/yr
row_doc(
    "powerchina_coca_codo_aom_46m_yr_2026",
    "energy",
    "power_plants_grid",
    "prc",
    "PowerChina — Coca Codo Sinclair O&M annual fee (minister-stated agreement)",
    "Ecuador",
    "13 Apr 2026: Energy Minister Inés Manzano states technical tables settled on USD 46 million per year for PowerChina to operate/maintain Coca Codo Sinclair (1,500 MW) for 25 years (implies ~USD 1.15bn cumulative if signed); contract to be signed within ~30 days after definitive reception from Sinohydro. Distinct from powerchina_coca_codo_om_2026 (USD 400m arbitration settlement package). CapEx blank for unsigned AOM; value = stated annual fee.",
    "46000000",
    "2026-04-13",
    "2026",
    "",
    "",
    "Coca Codo Sinclair (Napo/Sucumbíos) — lat/lon blank (multi-component hydro; use existing plant pin only if single named worksite).",
    "primicias_powerchina_ccs_aom_20260413",
    "finalmente, el acuerdo al que se llegó es pagar anualmente USD 46 millones. Si el contrato se firma por 25 años, esto representaría USD 1.150 millones… PowerChina… se haga cargo de la operación y mantenimiento de la central por 25 años.",
    "https://www.primicias.ec/economia/coca-codo-power-china-sinohydro-contrato-mantenimiento-operacion-coca-fisuras-120339/",
    "Actor: PowerChina (PRC SOE) — prc. Opened Primicias 13 Apr 2026 quoting Minister Manzano. Annual fee documented; full AOM contract still pending signature. Distinct from CELEC USD 400m settlement row.",
    "hunt_cycle171",
    investment_type="other",
    evidence="documented",
    bib_type="press",
    chicago='Primicias. “PowerChina recibirá USD 46 millones al año por operar la hidroeléctrica Coca Codo, dice la Ministra de Energía.” April 13, 2026. https://www.primicias.ec/economia/coca-codo-power-china-sinohydro-contrato-mantenimiento-operacion-coca-fisuras-120339/.',
    annotation="Primicias: Minister states USD 46m/yr PowerChina CCS O&M agreement. Supports powerchina_coca_codo_aom_46m_yr_2026.",
    evid_note="Opened Primicias Spanish article 13 Apr 2026.",
)

# 5. lithium / us — Atlas Lithium Neves named in U.S.–Japan critical minerals fact sheet
row_doc(
    "atlas_lithium_us_japan_neves_2026",
    "resources",
    "lithium",
    "us",
    "Atlas Lithium (NASDAQ: ATLX) — Neves Project named for potential U.S./Japan financial support",
    "Brazil",
    "2 Apr 2026: Atlas Lithium announces Neves Project (Brazil Lithium Valley) is named in Japan–U.S. Critical Minerals Project Cooperation Joint Fact Sheet (METI/MOFA 20 Mar 2026); both governments considering financial support for Neves development. Only Brazil lithium project on the list. CapEx blank (support under consideration; not a closed loan). Distinct from atlas_lithium_neves_dfs / 71pct CapEx / Mitsui offtake rows.",
    "",
    "",
    "2026",
    "",
    "",
    "Neves Project, Jequitinhonha Valley, Minas Gerais — lat/lon blank pending single named pit/plant pin.",
    "atlas_lithium_us_japan_neves_20260402",
    "its 100%-owned Neves Project in Brazil’s Lithium Valley is named in the Joint Fact Sheet for Japan-U.S. Critical Minerals Project Cooperation … the Government of Japan and the Government of United States are considering financial support for the purpose of development of the Neves Project.",
    "https://www.atlas-lithium.com/news/u-s-and-japan-identify-atlas-lithiums-neves-project-for-potential-government-financial-support-in-landmark-critical-minerals-partnership/",
    "Actor: Atlas Lithium (U.S.-listed) + U.S./Japan gov support consideration — us. Opened Atlas Lithium Newsfile PR 2 Apr 2026. CapEx blank until financed.",
    "hunt_cycle171",
    investment_type="financing",
    evidence="documented",
    bib_type="company",
    chicago='Atlas Lithium Corporation. “U.S. and Japan Identify Atlas Lithium’s Neves Project for Potential Government Financial Support in Landmark Critical Minerals Partnership.” April 2, 2026. https://www.atlas-lithium.com/news/u-s-and-japan-identify-atlas-lithiums-neves-project-for-potential-government-financial-support-in-landmark-critical-minerals-partnership/.',
    annotation="Atlas Lithium: Neves named on U.S.–Japan critical minerals fact sheet. Supports atlas_lithium_us_japan_neves_2026.",
    evid_note="Opened Atlas Lithium company press release 2 Apr 2026.",
)

# 6. solar / other — ANDE Loma Plata 140 MWac tender (Paraguay)
row_doc(
    "ande_loma_plata_solar_140mw_2026",
    "energy",
    "solar",
    "other",
    "ANDE — Loma Plata (Boquerón) 140 MWac photovoltaic energy procurement tender",
    "Paraguay",
    "1 Jun 2026: ANDE holds public hearing on international tender pliego for acquisition of photovoltaic energy from a 140 MWac plant to be built at Loma Plata (Boquerón), connected via ~7 km 220 kV line to Subestación Loma Plata; World Bank technical support cited. CapEx blank (pre-award tender; no contractor/OEM named). Paraguay×solar under-covered cell.",
    "",
    "",
    "2026",
    "",
    "",
    "Loma Plata, Boquerón — lat/lon blank pending awarded plant site coords.",
    "lanacion_ande_loma_plata_20260601",
    "El proyecto contempla la adquisición de energía proveniente de una planta solar fotovoltaica con una potencia instalada de 140 MWac, que será construida en Loma Plata y conectada al Sistema Interconectado Nacional (SIN) mediante una línea de transmisión en 220 kV.",
    "https://www.lanacion.com.py/negocios/2026/06/01/ande-avanza-con-primera-licitacion-solar-y-atrae-interes-de-mas-de-380-actores-del-sector/",
    "Actor: ANDE (Paraguayan SOE procurer) — other until U.S./PRC OEM/contractor named. Opened La Nación Paraguay 1 Jun 2026. CapEx blank pre-award.",
    "hunt_cycle171",
    investment_type="other",
    evidence="documented",
    bib_type="press",
    chicago='La Nación (Paraguay). “ANDE avanza con primera licitación solar y atrae interés de más de 380 actores del sector.” June 1, 2026. https://www.lanacion.com.py/negocios/2026/06/01/ande-avanza-con-primera-licitacion-solar-y-atrae-interes-de-mas-de-380-actores-del-sector/.',
    annotation="La Nación: ANDE Loma Plata 140 MWac solar tender hearing. Supports ande_loma_plata_solar_140mw_2026.",
    evid_note="Opened La Nación Paraguay article 1 Jun 2026.",
)

# 7. wind / other — ICE Tejona repower USD 77.5m
row_doc(
    "ice_tejona_wind_77p5m_2024",
    "energy",
    "wind",
    "other",
    "Instituto Costarricense de Electricidad (ICE) — Planta Eólica Tejona repower",
    "Costa Rica",
    "5 Sep 2024: ICE and Banco de Costa Rica sign financing contract (₡37.4bn) for remodel/expansion of Planta Eólica Tejona (Tilarán, Guanacaste); total modernization investment USD 77.5m (ICE contributes remainder). 14 new turbines; capacity to 42 MW; return to SEN targeted 2H 2026. CapEx = USD 77.5m. OEM not named on opened ICE page — side other (Costa Rican SOE).",
    "77500000",
    "2024-09-05",
    "2024",
    "",
    "",
    "Planta Eólica Tejona, Tilarán, Guanacaste — lat/lon blank pending verified plant pin.",
    "ice_tejona_bcr_20240905",
    "firmaron el contrato de financiamiento para remodelar y ampliar la Planta Eólica Tejona (Tilarán, Guanacaste), por ₡37.400 millones. La inversión completa para modernizar la planta será de $77,5 millones… contará con 14 aerogeneradores… capacidad instalada de 42 megavatios.",
    "https://www.grupoice.com/wps/portal/ICE/quienessomos/comunicacion/sala-de-prensa/noticiasanteriores/ice+y+bcr+firman+contrato+de+financiamiento+para+modernizacion+de+planta+eolica+tejona/ice+y+bcr+firman+contrato+de+financiamiento+para+modernizacion+de+planta+eolica+tejona",
    "Actor: ICE (Costa Rican SOE) + BCR local finance — other. Opened ICE sala de prensa 5 Sep 2024. Costa Rica×wind under-covered. Distinct from POWERCHINA Chucas / private Las Pavas rows.",
    "hunt_cycle171",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='Instituto Costarricense de Electricidad. “ICE y BCR firman contrato de financiamiento para modernización de Planta Eólica Tejona.” September 5, 2024. https://www.grupoice.com/wps/portal/ICE/quienessomos/comunicacion/sala-de-prensa/noticiasanteriores/ice+y+bcr+firman+contrato+de+financiamiento+para+modernizacion+de+planta+eolica+tejona/ice+y+bcr+firman+contrato+de+financiamiento+para+modernizacion+de+planta+eolica+tejona.',
    annotation="ICE: Tejona wind repower financing USD 77.5m. Supports ice_tejona_wind_77p5m_2024.",
    evid_note="Opened ICE Grupo ICE press room page 5 Sep 2024.",
)

# 8. water / us — Xylem Vue Mexico City + Monterrey (with Amazon)
row_doc(
    "xylem_amazon_vue_mexico_2025",
    "resources",
    "water",
    "us",
    "Xylem (NYSE: XYL) — Xylem Vue smart-water deployments (Mexico City + Monterrey)",
    "Mexico",
    "11 Sep 2025: Xylem and Amazon announce Xylem Vue deployments with Mexico City (SEGIAGUA) and Monterrey (SADM) utilities to detect leaks, manage pressure, and cut losses — estimated savings >800 million liters/yr CDMX and 560 million liters/yr Monterrey (>1.3 billion liters combined). CapEx blank (software/platform partnership; no dollar CapEx on opened BusinessWire).",
    "",
    "",
    "2025",
    "",
    "",
    "Mexico City and Monterrey municipal systems — lat/lon blank (multi-district deployments).",
    "xylem_amazon_vue_mexico_20250911",
    "The two cities are working in partnership with global water technology company Xylem (NYSE: XYL) and Amazon (NASDAQ: AMZN) to deploy Xylem Vue… estimated to save upwards of 800 million liters of water a year in Mexico City and 560 million liters a year in Monterrey.",
    "https://www.businesswire.com/news/home/20250911628782/en/Xylem-and-Amazon-Partner-on-Smart-Water-Upgrades-to-Save-More-Than-1.3-Billion-Liters-Annually-in-Mexico",
    "Actor: Xylem (U.S. water tech) — us. Opened BusinessWire 11 Sep 2025. CapEx blank. Distinct from Fluence desal / Acciona Los Cabos rows.",
    "hunt_cycle171",
    investment_type="other",
    evidence="documented",
    bib_type="company",
    chicago='Xylem Inc. “Xylem and Amazon Partner on Smart Water Upgrades to Save More Than 1.3 Billion Liters Annually in Mexico.” Business Wire, September 11, 2025. https://www.businesswire.com/news/home/20250911628782/en/Xylem-and-Amazon-Partner-on-Smart-Water-Upgrades-to-Save-More-Than-1.3-Billion-Liters-Annually-in-Mexico.',
    annotation="Xylem/Amazon BusinessWire: Vue deployments CDMX + Monterrey. Supports xylem_amazon_vue_mexico_2025.",
    evid_note="Opened BusinessWire Xylem release 11 Sep 2025.",
)

# 9. water / allied — Holcim México water strategy MXN 356m (~USD 20m) to 2027
row_doc(
    "holcim_mexico_water_356mdp_2026",
    "resources",
    "water",
    "allied",
    "Holcim México — water-management infrastructure/technology investment to 2027",
    "Mexico",
    "24 Mar 2026: Holcim México announces ~MXN 356 million (~USD 20m per company/press) through 2027 for water infrastructure, technology, and resilience projects; cites 58% freshwater-withdrawal cut vs 2020 and 71% of plants using recycled/non-conventional water. Value = USD 20m (stated USD equivalent of 356 MDP). Allied (Swiss Holcim).",
    "20000000",
    "2026-03-24",
    "2026",
    "",
    "",
    "Nationwide Holcim México cement/concrete plants — lat/lon blank (multi-site program).",
    "holcim_mexico_hidrica_20260324",
    "Holcim México fortalecerá su estrategia integral de gestión hídrica en el país, con una inversión de 356 MDP hacia 2027 para ampliar su infraestructura y tecnología para el cuidado del agua.",
    "https://www.holcim.com.mx/holcim-mexico-acelera-su-estrategia-hidrica-con-innovacion-e-inversion-en-nuevas-tecnologias",
    "Actor: Holcim México (Swiss Holcim) — allied. Opened Holcim México press page 24 Mar 2026. USD 20m = stated MXN 356m equivalent. Distinct from Holcim Geocycle/grind CapEx rows.",
    "hunt_cycle171",
    investment_type="other",
    evidence="documented",
    bib_type="company",
    chicago='Holcim México. “Holcim México acelera su estrategia hídrica con innovación e inversión en nuevas tecnologías.” March 24, 2026. https://www.holcim.com.mx/holcim-mexico-acelera-su-estrategia-hidrica-con-innovacion-e-inversion-en-nuevas-tecnologias.',
    annotation="Holcim México: MXN 356m water strategy to 2027. Supports holcim_mexico_water_356mdp_2026.",
    evid_note="Opened Holcim México Spanish press page 24 Mar 2026.",
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
    print(f"Cycle 171 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
