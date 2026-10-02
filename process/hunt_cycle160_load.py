#!/usr/bin/env python3
"""Cycle 160 hunt: shuffle_seed=20261160; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: solar, fission_smr, building_materials, balsa, water,
niobium, rail, wind, power_plants_grid, lithium, other_renewables, port_ownership,
graphite, engineering_epc, bridges_roads, port_cranes, copper, nickel.

Weight under-covered: Costa Rica, Suriname, Trinidad, Bolivia, El Salvador, Panama.
PRC ahead by 10 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr (once each this session; dry → nickel/niobium).
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


# 1. solar / us — DFC GoSolar Costa Rica USD 15m (distributed + 5 MW ICE plant)
row_doc(
    "dfc_gosolar_costa_rica_15m_2021",
    "energy",
    "solar",
    "us",
    "DFC / Luz Verde Costa Rica LLC — GoSolar Energy Efficiency S.R.L. (distributed solar + 5 MW ICE plant)",
    "Costa Rica",
    "DFC Public Information Summary (project 9000093595; 2021 energy approvals): USD 15m debt and equity to Luz Verde Costa Rica LLC (owned by U.S. WRB Serra Fund 1) for GoSolar Energy Efficiency S.R.L. — portfolio of small-scale residential/commercial solar plus development and operation of a 5 MW solar plant for ICE (Instituto Costarricense de Electricidad). Proposed political-risk insurance USD 13.5m. Total project costs USD 15m.",
    "15000000",
    "2021-12-31",
    "2021",
    "9.920",
    "-84.140",
    "Costa Rica distributed solar portfolio + ICE 5 MW plant (national pin; plant site not named on PIS).",
    "dfc_gosolar_costa_rica_pis_9000093595",
    "Host Country Costa Rica … Project Description Portfolio of small scale residential and commercial solar energy projects, and the development and operation of a 5MW solar plant for the Costa Rican Institute of Energy. Investment Amount $15,000,000 Investment Type Debt and Equity Proposed Insurance Amount $13,500,000 Total Project Costs $15,000,000 U.S. Involvement Luz Verde Costa Rica LLC is owned by WRB Serra Fund 1, a U.S. entity and managed by U.S. Persons. Foreign Enterprise GoSolar Energy Efficiency S.R.L.",
    "https://www.dfc.gov/sites/default/files/media/documents/9000093595.pdf",
    "Actor: DFC financing to U.S.-owned Luz Verde / GoSolar — us. DFC PIS primary (opened). USD 15m documented. Undersampled Costa Rica solar (first U.S. solar row).",
    "hunt_energy_solar",
    investment_type="financing",
    bib_type="government",
    chicago='U.S. International Development Finance Corporation. “Public Information Summary: GoSolar Energy Efficiency S.R.L.” Project 9000093595. https://www.dfc.gov/sites/default/files/media/documents/9000093595.pdf.',
    annotation="DFC PIS: USD 15m debt/equity GoSolar Costa Rica + 5 MW ICE plant. Supports dfc_gosolar_costa_rica_15m_2021.",
    evid_note="Opened DFC PIS 9000093595 (GoSolar CR USD 15m / 5 MW ICE).",
)

# 2. solar / us — AES Pesé Solar 10 MW Panama
row_doc(
    "aes_panama_pese_10mw_2021",
    "energy",
    "solar",
    "us",
    "AES Panamá — Pesé Solar (10 MW; Herrera)",
    "Panama",
    "14 Feb 2020 AES Panamá: awards Elecnor EPC for four 10 MW nominal solar parks totaling 40 MW / >USD 50m investment — Pesé Solar (Pesé district, Herrera), Mayorca Solar (Pocrí, Los Santos), Cedro and Caoba Solar (Boquerón, Chiriquí). AES Q2 2026 Fact Sheet lists Pesé Solar Panama 10 MW at 49% AES ownership, COD 2021, contracts through 2030. CapEx blank at plant level (portfolio >USD 50m UNVERIFIED allocation). Distinct from aes_panama_corotu_10mw_2025 / aes_panama_los_santos_8mw_2025.",
    "",
    "",
    "2021",
    "7.908",
    "-80.612",
    "Pesé district, Herrera province, Panama (Pesé Solar).",
    "aes_panama_solar40mw_20200214",
    "AES continues to contribute towards the diversification and strengthening of the energy sector in Panama, this time through the announcement of a solar project that contemplates four smaller projects of 10MW each that are distributed through three provinces in the country, with an investment of more than USD $50 million. … Pesé Solar (District of Pesé, Herrera Province), Mayorca Solar (District of Pocrí, Los Santos Province), and Cedro & Caoba Solar (both in the district of Boquerón, Chiriquí Province).",
    "https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables",
    "Actor: AES Panamá (U.S. HQ parent) — us. Company English/Spanish primary + AES Fact Sheet COD 2021 confirmation. CapEx blank at plant level. Undersampled named Panama solar sites.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Panamá. “AES Panamá aumenta su apuesta a las energías renovables.” February 14, 2020. https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables.',
    annotation="AES Panamá primary: Pesé/Mayorca/Cedro/Caoba 4×10 MW solar (>USD 50m portfolio). Supports aes_panama_pese_10mw_2021; aes_panama_mayorca_10mw_2021.",
    evid_note="Opened AES Panamá 14 Feb 2020 release (Pesé Solar 10 MW / >USD 50m four-park portfolio).",
)

# 3. solar / us — AES Mayorca Solar 10 MW Panama
row_doc(
    "aes_panama_mayorca_10mw_2021",
    "energy",
    "solar",
    "us",
    "AES Panamá — Mayorca Solar (10 MW; Pocrí, Los Santos)",
    "Panama",
    "14 Feb 2020 AES Panamá: Mayorca Solar among four 10 MW parks (Pesé, Mayorca, Cedro, Caoba); construction kick-off with Pesé noted on same page. AES Q2 2026 Fact Sheet lists Mayorca Solar Panama 10 MW at 49% AES ownership, COD 2021. CapEx blank at plant level. Distinct from aes_panama_pese_10mw_2021 / aes_panama_los_santos_8mw_2025.",
    "",
    "",
    "2021",
    "7.663",
    "-80.116",
    "Pocrí district, Los Santos province, Panama (Mayorca Solar).",
    "aes_panama_solar40mw_20200214",
    "This week we held the construction kick-off for the solar projects of Pesé and Mayorca Solar in Panama, with the beginning of land movements. These two (2) projects are part of a total of four (4) solar projects of 10MW each: Pesé Solar (District of Pesé, Herrera Province), Mayorca Solar (District of Pocrí, Los Santos Province), and Cedro & Caoba Solar (both in the district of Boquerón, Chiriquí Province).",
    "https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables",
    "Actor: AES Panamá (U.S. HQ parent) — us. Same company primary as Pesé. CapEx blank. Distinct named site in Los Santos.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Panamá. “AES Panamá aumenta su apuesta a las energías renovables.” February 14, 2020. https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables.',
    annotation="AES Panamá primary: Mayorca Solar 10 MW COD 2021. Supports aes_panama_mayorca_10mw_2021; aes_panama_pese_10mw_2021.",
    evid_note="Opened AES Panamá 14 Feb 2020 release (Mayorca Solar 10 MW kick-off).",
)

# 4. solar / prc — POWERCHINA Goejaba & Pikin Slee Suriname Phase I microgrid
row_doc(
    "powerchina_goejaba_pikinslee_suriname_2020",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Goejaba and Pikin Slee Photovoltaic Microgrid (Suriname)",
    "Suriname",
    "20 May 2025 POWERCHINA Solar portfolio page: Goejaba and Pikin Slee Photovoltaic Microgrid Project in Suriname — total PV 673.2 kW and energy storage 2.6 MWh; put into operation May 2020; precedent for Chinese firms providing power in unelectrified overseas areas. CapEx blank. Distinct from Phase II Botopasi/Djoemoe/Kajana/Guyaba rows.",
    "",
    "",
    "2020",
    "4.100",
    "-55.480",
    "Goejaba and Pikin Slee villages, Suriname River corridor (approximate village-cluster pin).",
    "powerchina_solar_portfolio_20250520",
    "9. Goejaba and Pikin Slee Photovoltaic Microgrid Project in Suriname The project is constructed in the two villages of Goejaba and Pikin Slee, with a total installed photovoltaic capacity of 673.2 kW and a total energy storage capacity of 2.6 MWh. It was put into operation in May 2020. The successful implementation of the project sets a precedent for Chinese enterprises to provide high-quality power services in vast areas overseas without electricity.",
    "https://en.powerchina.cn/2025-05/20/c_816883.htm",
    "Actor: POWERCHINA — prc. Company English primary. CapEx blank. Phase I Suriname microgrid not previously logged (Phase II sites already covered).",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “Solar.” Updated May 20, 2025. https://en.powerchina.cn/2025-05/20/c_816883.htm.',
    annotation="POWERCHINA Solar portfolio: Goejaba/Pikin Slee 673.2 kW PV + 2.6 MWh storage COD May 2020. Supports powerchina_goejaba_pikinslee_suriname_2020.",
    evid_note="Opened POWERCHINA English Solar page 20 May 2025 (Goejaba/Pikin Slee 673.2 kW).",
)

# 5. water / prc — CREC/CTCE Cañas–Bebedero potable plant Costa Rica (PRC grant)
row_doc(
    "crec_canas_bebedero_water_costa_rica_2022",
    "resources",
    "water",
    "prc",
    "China Railway / CTCE (中铁四局) — Cañas–Bebedero potable water plant (AyA; Guanacaste)",
    "Costa Rica",
    "24 Mar 2022 Costa Rica Presidency: Cañas–Bebedero aqueduct/potabilization plant delivered — PRC grant ₡9,815 million; AyA equips and operates; serves ~37,000 people in Cañas, Palmira, San Miguel, Bebedero, Porozal; rapid-filtration CEPIS plant 126 L/s; 13.5 km conveyance piping. CREC newspaper / People Daily: China Tiesiju Civil Engineering Group (CTCE / 中铁四局) EPC; construction from Apr 2019; handover Mar 2022. CapEx blank in USD (CRC grant figure on Presidency page; FX not applied). Distinct from CHEC Ruta 32 rows.",
    "",
    "",
    "2022",
    "10.430",
    "-85.100",
    "Sandillal de Cañas, Guanacaste, Costa Rica (Cañas–Bebedero potabilization plant).",
    "cr_presidencia_canas_bebedero_20220324",
    "El proyecto Cañas-Bebedero tuvo un costo de ₡9.815 millones donados por la República Popular China, y el Instituto Costarricense de Acueductos y Alcantarillados (AyA) equipó la planta y aportó el personal que la opera para brindar agua potable a unas 37.000 personas de las comunidades de Cañas, Palmira, San Miguel, Bebedero y Porozal. … Las obras incluyeron la construcción de una planta potabilizadora de filtración rápida tipo CEPIS con tecnología de punta capaz de procesar 126 litros por segundo. Además, se instalaron 13.5 kilómetros de tuberías de conducción",
    "https://presidencia.gobiernocarlosalvarado.cr/comunicados/2022/03/canas-recibe-planta-potabilizadora-mas-moderna-del-pais-por-parte-de-aya-y-la-republica-popular-china/",
    "Actor: China Tiesiju Civil Engineering Group (CTCE / CREC 4th Bureau) under PRC grant — prc. Costa Rica Presidency primary for grant/handover; People Daily Spanish names CTCE as builder. CapEx blank USD (₡9,815m grant cited; no FX). First Costa Rica water row.",
    "hunt_resources_water",
    investment_type="epc",
    bib_type="government",
    chicago='Presidencia de la República de Costa Rica. “Cañas recibe planta potabilizadora más moderna del país por parte de AyA y la República Popular China.” March 24, 2022. https://presidencia.gobiernocarlosalvarado.cr/comunicados/2022/03/canas-recibe-planta-potabilizadora-mas-moderna-del-pais-por-parte-de-aya-y-la-republica-popular-china/.',
    annotation="CR Presidency: Cañas–Bebedero plant PRC grant ₡9,815m / 126 L/s / ~37k people. Supports crec_canas_bebedero_water_costa_rica_2022.",
    evid_note="Opened CR Presidency 24 Mar 2022 (Cañas–Bebedero handover / PRC grant); People Daily Spanish 28 Feb 2022 names CTCE builder.",
)

# 6. bridges_roads / prc — CREC Oruro–Challapata Tramo I Bolivia
row_doc(
    "crec_oruro_challapata_tramo1_bolivia_2024",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Railway (CREC International / CREC 7th Bureau) — Oruro–Challapata Tramo I dual carriageway (19.79 km)",
    "Bolivia",
    "14 May 2024 EqualOcean (opened): groundbreaking 13 May 2024 for Oruro–Challapata Section 1 bidirectional highway — 19.79 km four-lane rigid pavement on Bolivian Route 01; consortium China Railway International + China Railway 7th Bureau Group; President Arce attended. CREC South America branch 28 Sep 2025 confirms ongoing Oruro highway labor-competition / construction targets. CAF project page: Tramo I 19.79 km; project cost USD 73m (CAF loan USD 58.4m + local USD 14.6m) — financing of ABC sovereign project, not disclosed CREC contract price; CapEx blank for contractor row. Distinct from crec_espino_highway_bolivia_2023 / powerchina_el_sillar_bolivia_2023.",
    "",
    "",
    "2024",
    "-17.970",
    "-67.110",
    "Oruro–Cruce Vinto–Cruce Huanuni corridor, Oruro department, Bolivia (Tramo I start near Oruro).",
    "equalocean_crec_oruro_challapata_20240514",
    "May 13th, local time in Bolivia, the groundbreaking ceremony for the Oruro-Challapata Section 1 bidirectional highway project … undertaken by China Railway(中国中铁), was held in Oruro. … The Oruro Highway Project is a project to renovate and expand the Bolivian national road network's Route 01. It mainly involves the construction of a 19.79-kilometer-long, bidirectional four-lane rigid pavement highway. The project is undertaken by a consortium formed by China Railway International and China Railway 7th Bureau Group.",
    "https://equalocean.com/news/2024051420904",
    "Actor: CREC International / CREC 7th Bureau — prc. EqualOcean English primary (opened, non-paywalled) + CREC confirmation of active Oruro highway works. CapEx blank (CAF USD 73m is sovereign project cost, not CREC award). Holdover CREC Oruro–Challapata filled.",
    "hunt_infrastructure_bridges_roads",
    investment_type="epc",
    evidence="proxy",
    bib_type="news",
    chicago='EqualOcean. “China Railway Commences Construction of Oruro Highway Project in Bolivia.” May 14, 2024. https://equalocean.com/news/2024051420904.',
    annotation="EqualOcean: CREC consortium groundbreaking Oruro–Challapata Tramo I 19.79 km. Supports crec_oruro_challapata_tramo1_bolivia_2024. Press primary — evidence=proxy.",
    evid_note="Opened EqualOcean 14 May 2024 (CREC Oruro–Challapata 19.79 km groundbreaking).",
)

# 7. power_plants_grid / us — Invenergy Energía del Pacífico 380 MW El Salvador
row_doc(
    "invenergy_edp_acajutla_380mw_1bn_2022",
    "energy",
    "power_plants_grid",
    "us",
    "Invenergy — Energía del Pacífico LNG-to-power (380 MW; Acajutla)",
    "El Salvador",
    "20 Oct 2022 Invenergy: Energía del Pacífico (EDP) at Port of Acajutla reaches commercial operations — 380 MW natural gas-fired plant, permanently moored FSRU, 1.8 km subsea pipeline, two 230 kV transmission lines (one to SIEPAC); >USD 1 billion project financed by DFC, IFC, IDB Invest, Finnish Export Credit, KfW IPEX-Bank; up to 30% of national demand; largest-ever private FDI in El Salvador. Lead developer Invenergy with local partners. Distinct from aes_elsalvador rows and nfe_puerto_sandino Nicaragua.",
    "1000000000",
    "2022-10-20",
    "2022",
    "13.592",
    "-89.827",
    "Port of Acajutla, Sonsonate department, El Salvador (EDP LNG-to-power complex).",
    "invenergy_edp_cod_20221020",
    "Invenergy … has reached commercial operations at the Energía del Pacífico (EDP) LNG-to-power project, located at the Port of Acajutla in El Salvador. … The project is comprised of a 380-megawatt (MW) natural gas-fired power plant, a permanently moored floating storage regasification unit (FSRU), a 1.8-km subsea pipeline that connects the power plant to the FSRU, and two 230-kV electric transmission lines … The more than $1 billion transformative infrastructure project, the largest-ever private investment in El Salvador, was financed by leading global financial institutions U.S. International Development Finance Corporation, International Finance Corporation, IDB Invest, Finnish Export Credit Ltd and KfW IPEX-Bank.",
    "https://invenergy.com/news/transformative-lng-to-power-project-lights-up-el-salvador-accelerates-region-s-energy-transition",
    "Actor: Invenergy (Chicago HQ) lead developer/owner — us. Company English primary. USD 1bn+ floor documented. Undersampled El Salvador thermal/LNG generation.",
    "hunt_energy_power_plants_grid",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Invenergy LLC. “Transformative LNG-to-Power Project Lights Up El Salvador, Accelerates Region’s Energy Transition.” October 20, 2022. https://invenergy.com/news/transformative-lng-to-power-project-lights-up-el-salvador-accelerates-region-s-energy-transition.',
    annotation="Invenergy primary: EDP Acajutla 380 MW COD / >USD 1bn. Supports invenergy_edp_acajutla_380mw_1bn_2022.",
    evid_note="Opened Invenergy 20 Oct 2022 release (EDP 380 MW / >USD 1bn COD).",
)

# 8. port_ownership / allied — APM Terminals Moín Costa Rica (ongoing modernization documents presence)
row_doc(
    "apm_moin_costa_rica_modernization_2025",
    "infrastructure",
    "port_ownership",
    "allied",
    "APM Terminals — Moín Container Terminal (TCM) modernization / ongoing concession (Limón)",
    "Costa Rica",
    "18 Aug 2025 APM Terminals: Moín Container Terminal modernization 2024–2025 — crane electrification, STS OCR, access controls, electric work-fleet target by end-2025; Managing Director José Rueda describes multi-year modernization of Costa Rica’s main Caribbean container port. CapEx blank (modernization amounts not disclosed on opened page). Distinct from apm_hgt_caldera_costa_rica_2026 (Pacific Caldera).",
    "",
    "",
    "2025",
    "10.023",
    "-83.075",
    "Moín Container Terminal, Limón province, Caribbean coast, Costa Rica.",
    "apm_moin_modernization_20250818",
    "During 2024 and this year, 2025, APM Terminals Moin is making significant investments in various operational and security areas of the MCT. … Another of our important projects is the electrification of cranes, which will contribute to the decarbonization of operations. … by the end of 2025, it is expected that the fleet of work vehicles will be electric",
    "https://www.apmterminals.com/en/moin/practical-information/news/2025/250818-APM-Terminals-Moin-invests-in-modernizing-TCM",
    "Actor: APM Terminals (A.P. Moller–Maersk, Copenhagen HQ) — allied. Company English primary. CapEx blank. Undersampled Costa Rica Caribbean port ownership (Caldera already logged).",
    "hunt_infrastructure_port_ownership",
    investment_type="concession",
    bib_type="company",
    chicago='APM Terminals. “APM Terminals Moín invests in modernizing TCM, ensuring competitiveness and efficiency.” August 18, 2025. https://www.apmterminals.com/en/moin/practical-information/news/2025/250818-APM-Terminals-Moin-invests-in-modernizing-TCM.',
    annotation="APM Terminals primary: Moín TCM 2024–25 modernization / ongoing operator presence. Supports apm_moin_costa_rica_modernization_2025.",
    evid_note="Opened APM Terminals Moín 18 Aug 2025 modernization release.",
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
    print(f"Cycle 160 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
