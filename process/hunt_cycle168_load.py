#!/usr/bin/env python3
"""Cycle 168 hunt: shuffle_seed=20261168; equal budget; U.S./PRC split; thin after.

Canonical shuffle: copper, niobium, solar, balsa, graphite, rail, water, port_cranes,
other_renewables, nickel, power_plants_grid, bridges_roads, engineering_epc, fission_smr,
lithium, wind, building_materials, port_ownership.

Thin top-up: balsa / fission_smr / niobium (fission filled with Mexico–U.S. 123;
balsa/niobium dry once). Holdovers unsigned: Corentyne, CSCEC 290 km package,
CCECC rail MoU, POWERCHINA Nickerie hydro (drainage logged instead).
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


# 1. copper / allied — Hudbay Constancia mill to 34 Mtpa (SENACE)
row_doc(
    "hudbay_constancia_34mtpa_senace_2026",
    "resources",
    "copper",
    "allied",
    "Hudbay Minerals — Constancia mill throughput permit to 34 Mtpa (SENACE)",
    "Peru",
    "2 Jul 2026 Hudbay: SENACE approved fifth environmental permit amendment at Constancia (Cusco), raising mill processing capacity to 34 million tonnes of ore per annum from 31 Mtpa (March 2026 amendment had raised from 29.9 to 31 Mtpa). Also approves mine-plan optimization, life extension, and additional tailings-transport/water-management infrastructure. CapEx blank (permit/optimization, not a disclosed CapEx package). Fills distinct Constancia throughput cell.",
    "",
    "",
    "2026",
    "-14.270",
    "-71.470",
    "Constancia mine, Cusco region, Peru.",
    "hudbay_constancia_34mtpa_20260702",
    "Hudbay Minerals Inc. (“Hudbay” or the “Company”) (TSX, NYSE: HBM) announced it has received approval from the National Environmental Certification Service for Sustainable Investments in Perú (“SENACE”) to amend its environmental permit and further increase annual mill processing capacity at Constancia. … The amended permit increases the processing capacity of the Constancia mill to 34 million tonnes of ore per annum from the previously permitted 31 million tonnes per annum.",
    "https://www.hudbayminerals.com/investors/press-releases/press-release-details/2026/Hudbay-Receives-Regulatory-Approval-to-Further-Increase-Mill-Throughput-at-its-Constancia-Mine-in-Peru/default.aspx",
    "Actor: Hudbay Minerals Inc. (Canada HQ; TSX/NYSE) — allied. Company English primary. CapEx blank. First Constancia throughput row.",
    "hunt_res_copper",
    investment_type="other",
    bib_type="company",
    chicago='Hudbay Minerals Inc. “Hudbay Receives Regulatory Approval to Further Increase Mill Throughput at its Constancia Mine in Peru.” July 2, 2026. https://www.hudbayminerals.com/investors/press-releases/press-release-details/2026/Hudbay-Receives-Regulatory-Approval-to-Further-Increase-Mill-Throughput-at-its-Constancia-Mine-in-Peru/default.aspx.',
    annotation="Hudbay primary: Constancia SENACE permit to 34 Mtpa. Supports hudbay_constancia_34mtpa_senace_2026.",
    evid_note="Opened Hudbay 2 Jul 2026 Constancia SENACE mill-throughput release.",
)

# 2. copper / prc — Chinalco Toromocho 2026 equipment CapEx >USD 400m
row_doc(
    "chinalco_toromocho_equip_400m_2026",
    "resources",
    "copper",
    "prc",
    "Minera Chinalco Perú — Toromocho 2026 mine/plant equipment renewal (>USD 400m)",
    "Peru",
    "4 Feb 2026 Gestión: Minera Chinalco Perú began 2026 investments focused on renewing mine and process-plant equipment at Toromocho (Junín), with a progressive program contemplating disbursement superior to USD 400 million during 2026; first milestone was transport of CAT 7495 shovel replacement bucket via Carretera Central. Distinct annual sustaining/equipment tranche from ITS-3 expansion package already logged (chinalco_toromocho_its3_700m_2026). CapEx = USD 400m floor UNVERIFIED press proxy.",
    "400000000",
    "2026-02-04",
    "2026",
    "-11.670",
    "-76.140",
    "Unidad Minera Toromocho, Junín, Peru.",
    "gestion_chinalco_toromocho_400m_20260204",
    "La Minera Chinalco Perú inició el proceso de inversiones contemplado para este 2026, enfocado en la renovación de equipos de mina y planta de procesos en la Unidad Minera Toromocho … un programa progresivo de inversiones que contempla un desembolso superior a US$400 millones en Toromocho durante el 2026.",
    "https://gestion.pe/economia/empresas/minera-chinalco-inicia-un-plan-de-inversiones-para-el-2026-en-la-unidad-minera-toromocho-noticia/",
    "Actor: Minera Chinalco Perú (Aluminum Corp of China / Chinalco) — prc. Spanish business press — evidence=proxy for CapEx figure (UNVERIFIED press) though actor/site/year named; value stored as proxy floor.",
    "hunt_res_copper",
    investment_type="equipment_supply",
    evidence="proxy",
    bib_type="news",
    chicago='Gestión. “Chinalco inicia inversiones por más de US$400 millones en mina Toromocho en 2026.” February 4, 2026. https://gestion.pe/economia/empresas/minera-chinalco-inicia-un-plan-de-inversiones-para-el-2026-en-la-unidad-minera-toromocho-noticia/.',
    annotation="Gestión: Chinalco Toromocho 2026 equipment CapEx >USD 400m (proxy). Supports chinalco_toromocho_equip_400m_2026.",
    evid_note="Opened Gestión 4 Feb 2026 Chinalco Toromocho 2026 equipment investment article.",
)

# 3. solar / prc — Grain Full El Vigía 52.8 MW Venezuela
row_doc(
    "grain_full_el_vigia_solar_52p8mw_venezuela",
    "energy",
    "solar",
    "prc",
    "Grain Full (China) — El Vigía photovoltaic farm 52.8 MW (Mérida)",
    "Venezuela",
    "31 Oct 2025 Ciudad Valencia (Radio Miraflores): El Vigía PV farm (Alberto Adriani, Mérida) installing 94,000 panels for 52.8 MW; works began April; framed under Venezuela–PRC energy cooperation; Grain Full work team on inspection with Corpoelec; >250 Venezuelan and Chinese workers. CapEx blank. Fills Venezuela×solar empty cell.",
    "",
    "",
    "2025",
    "8.610",
    "-71.650",
    "El Vigía / Alberto Adriani municipality, Mérida, Venezuela.",
    "ciudadvalencia_el_vigia_solar_20251031",
    "La granja fotovoltaica más grande de Venezuela, proyecta su inauguración para este mes noviembre, ubicada en El Vigía, estado Mérida, este proyecto cuenta con una instalación de 94 mil paneles solares que generarán 52,8 megavatios. … esta iniciativa se enmarca dentro del convenio de cooperación energética entre Venezuela y la República Popular China … Durante este recorrido participó el equipo de trabajo de la empresa Grain Full",
    "https://www.ciudadvalencia.com.ve/granja-fotovoltaica-noviembre/",
    "Actor: Grain Full / Green Full (Chinese contractor under Venezuela–PRC energy cooperation) — prc. Spanish regional press quoting governor inspection — CapEx blank; contractor named on site. First Venezuela solar row.",
    "hunt_energy_solar",
    investment_type="epc",
    evidence="proxy",
    bib_type="news",
    chicago='Ciudad Valencia (Radio Miraflores). “Mérida: Inaugurarán granja fotovoltaica más grande de Venezuela en noviembre.” October 31, 2025. https://www.ciudadvalencia.com.ve/granja-fotovoltaica-noviembre/.',
    annotation="Ciudad Valencia: Grain Full El Vigía 52.8 MW under Venezuela–China energy coop. Supports grain_full_el_vigia_solar_52p8mw_venezuela.",
    evid_note="Opened Ciudad Valencia 31 Oct 2025 El Vigía PV farm article (Grain Full / China coop).",
)

# 4. solar / allied — Ssangyong Caracol 13.4 MW Haiti (IDB USD 57m)
row_doc(
    "ssangyong_caracol_solar_13p4mw_haiti_57m",
    "energy",
    "solar",
    "allied",
    "Ssangyong E&C — Caracol Industrial Park solar plant 13.4 MW (IDB USD 57m)",
    "Haiti",
    "29 Jan 2026 HaitiLibre: Caracol PIC photovoltaic plant is Haiti’s largest solar project and first directly integrated into the national grid — 13.4 MW PV plus BESS; USD 57 million financed by Inter-American Development Bank; built by Ssangyong Engineering & Construction under ANARSE supervision. CapEx/investment = USD 57m face. Fills Haiti×solar empty cell.",
    "57000000",
    "2026-01-29",
    "2026",
    "19.740",
    "-72.020",
    "Caracol Industrial Park, Nord-Est, Haiti.",
    "haitilibre_caracol_solar_20260129",
    "With an installed capacity of 13.4 MW, it is the largest solar project ever undertaken in Haiti and the first to be directly integrated into the national grid. This $57 million project, financed by the Inter-American Development Bank (IDB) … The Caracol solar power plant, built by Ssangyong Engineering & Construction under the supervision of the National Energy Regulatory Authority (ANARSE)",
    "https://www.haitilibre.com/en/news-46735-haiti-caracol-the-country-s-largest-photovoltaic-solar-power-plant.html",
    "Actor: Ssangyong Engineering & Construction (Republic of Korea) — allied; IDB finance. HaitiLibre English primary. USD 57m face. First Haiti solar row.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="news",
    chicago='HaitiLibre. “Haiti - Caracol : The country’s largest photovoltaic solar power plant.” January 29, 2026. https://www.haitilibre.com/en/news-46735-haiti-caracol-the-country-s-largest-photovoltaic-solar-power-plant.html.',
    annotation="HaitiLibre: Ssangyong Caracol 13.4 MW; IDB USD 57m. Supports ssangyong_caracol_solar_13p4mw_haiti_57m.",
    evid_note="Opened HaitiLibre 29 Jan 2026 Caracol solar plant article.",
)

# 5. water / prc — POWERCHINA Nickerie Paradise drainage
row_doc(
    "powerchina_nickerie_paradise_drainage_2025",
    "resources",
    "water",
    "prc",
    "POWERCHINA — Nickerie Longmay/Paradise drainage upgrade (Politieweg culvert)",
    "Suriname",
    "11 Oct 2025 Dagblad Suriname: Districtscommissaris Mohamed Bakas inspected works by contractor PowerChina in Longmay and Paradise neighborhoods (Nickerie); key component replaces overflow under Politieweg with two 100 cm pipes and concrete retaining walls to improve stormwater drainage and reduce flooding around Paradise. CapEx blank. Distinct from Suriname solar microgrid rows; fills Suriname×water empty cell (holdover Nickerie hydro URL still unstable).",
    "",
    "",
    "2025",
    "5.930",
    "-56.990",
    "Paradise / Longmay, Nickerie District, Suriname.",
    "dbsuriname_nickerie_powerchina_20251011",
    "Tijdens dit bezoek werd op verschillende locaties de voortgang van werkzaamheden van aannemer PowerChina nauwlettend gevolgd. … Een van de belangrijkste onderdelen van het project betreft de vervanging van de bestaande overloop onder de Politieweg. Deze zal worden vernieuwd met twee buizen van 100 centimeter diameter, verstevigd met betonnen keermuren aan beide zijden.",
    "https://www.dbsuriname.com/2025/10/11/districtscommissariaat-nickerie-inspecteert-duurzame-infrastructuurprojecten/",
    "Actor: POWERCHINA (PRC SOE) — prc. Dutch-language Suriname press naming contractor on site — CapEx blank. First Suriname water row.",
    "hunt_res_water",
    investment_type="epc",
    evidence="proxy",
    bib_type="news",
    chicago='Dagblad Suriname. “Districtscommissariaat Nickerie inspecteert duurzame infrastructuurprojecten.” October 11, 2025. https://www.dbsuriname.com/2025/10/11/districtscommissariaat-nickerie-inspecteert-duurzame-infrastructuurprojecten/.',
    annotation="Dagblad Suriname: POWERCHINA Nickerie Paradise drainage works. Supports powerchina_nickerie_paradise_drainage_2025.",
    evid_note="Opened Dagblad Suriname 11 Oct 2025 Nickerie PowerChina drainage inspection article.",
)

# 6. power_plants_grid / us — USTDA ICE monitoring/diagnostics TA
row_doc(
    "ustda_ice_costa_rica_mdi_2022",
    "energy",
    "power_plants_grid",
    "us",
    "USTDA / EPRI — ICE integrated monitoring and diagnostics technical assistance",
    "Costa Rica",
    "22 Aug 2022 USTDA: awarded technical assistance grant to Costa Rican Electricity Institute (ICE) for a monitoring and diagnostic system roadmap covering generation, transmission and distribution assets; ICE selected California-based Electric Power Research Institute (EPRI) to carry out the assistance. CapEx/grant amount blank on opened page. Fills Costa Rica×power_plants_grid empty cell.",
    "",
    "",
    "2022",
    "9.930",
    "-84.090",
    "ICE institutional pin, San José, Costa Rica (national grid TA).",
    "ustda_ice_costa_rica_20220822",
    "Today, the U.S. Trade and Development Agency awarded a technical assistance grant to the Costa Rican Electricity Institute (ICE) to help strengthen the stability and reliability of the country’s power sector. Specifically, USTDA’s assistance will support the development of a monitoring and diagnostic system to enhance the utility’s management of its power generation, transmission, and distribution assets. ICE selected California-based Electric Power Research Institute to carry out the assistance.",
    "https://ustda.gov/ustda-supports-costa-ricas-power-sector-modernization/",
    "Actor: USTDA (U.S. government) / EPRI (U.S.) implementer — us. USTDA English primary. CapEx blank. First Costa Rica grid row.",
    "hunt_br_power_equip",
    investment_type="financing",
    bib_type="government",
    chicago='U.S. Trade and Development Agency. “USTDA Supports Costa Rica’s Power Sector Modernization.” August 22, 2022. https://ustda.gov/ustda-supports-costa-ricas-power-sector-modernization/.',
    annotation="USTDA primary: ICE monitoring/diagnostics TA with EPRI. Supports ustda_ice_costa_rica_mdi_2022.",
    evid_note="Opened USTDA 22 Aug 2022 Costa Rica ICE power-sector modernization release.",
)

# 7. bridges_roads / us — Freeport Cerro Verde OxI Uchumayo road
row_doc(
    "fcx_cerro_verde_oxi_uchumayo_2026",
    "infrastructure",
    "bridges_roads",
    "us",
    "Freeport / Cerro Verde — Works for Taxes Uchumayo road package (Arequipa)",
    "Peru",
    "24 Jul 2026 Freeport-McMoRan: Cerro Verde completed first two Peru Works for Taxes (Obras por Impuestos) projects investing more than USD 14 million — including a major road infrastructure project in Uchumayo district (resurfacing, drainage, signage, sidewalks, green spaces) plus a National University of San Agustín campus in El Pedregal, Majes. CapEx blank for road alone (USD 14m+ covers both projects without disclosed split). Fills distinct Cerro Verde OxI road cell.",
    "",
    "",
    "2026",
    "-16.430",
    "-71.680",
    "Uchumayo district road corridor, Arequipa, Peru.",
    "fcx_cerro_verde_oxi_20260724",
    "Cerro Verde has completed its first two projects through Peru’s Works for Taxes (Obras por Impuestos, OxI) program, investing more than $14 million … Cerro Verde also completed a major road infrastructure project in the district of Uchumayo. The work included roadway resurfacing, drainage improvements, signage upgrades, new sidewalks and green spaces.",
    "https://fcx.com/freeport-features/07242026",
    "Actor: Freeport-McMoRan / Sociedad Minera Cerro Verde (U.S. majority) — us. Company English primary. CapEx blank for road-only share of >USD 14m package.",
    "hunt_infra_bridges_roads",
    investment_type="other",
    bib_type="company",
    chicago='Freeport-McMoRan. “Cerro Verde Completes First Works for Taxes Projects in Arequipa.” July 24, 2026. https://fcx.com/freeport-features/07242026.',
    annotation="Freeport primary: Cerro Verde OxI Uchumayo road within >USD 14m package. Supports fcx_cerro_verde_oxi_uchumayo_2026.",
    evid_note="Opened Freeport 24 Jul 2026 Cerro Verde Works for Taxes feature.",
)

# 8. fission_smr / us — Mexico–U.S. 123 agreement in force
row_doc(
    "mexico_us_123_agreement_2022",
    "energy",
    "fission_smr",
    "us",
    "United States–Mexico Agreement for Peaceful Nuclear Cooperation (123) in force",
    "Mexico",
    "World Nuclear Association (updated 8 Jul 2026): bilateral U.S.–Mexico peaceful nuclear cooperation agreement (Atomic Energy Act §123) signed May 2018 and entered into force November 2022, permitting transfers of material, equipment (including reactors), components and information for nuclear research and power under safeguards. CapEx blank (legal framework, not a reactor award). Fills Mexico×fission_smr empty cell. Distinct from Laguna Verde GE BWR units (historical build).",
    "",
    "",
    "2022",
    "",
    "",
    "National civil-nuclear cooperation framework (no single plant pin).",
    "wna_mexico_nuclear_20260708",
    "A bilateral agreement for peaceful nuclear cooperation between Mexico and the USA (a ‘123 agreement’) was signed in May 2018 and entered into force in November 2022.",
    "https://world-nuclear.org/information-library/country-profiles/countries-g-n/mexico",
    "Actor: United States (DOE/State 123 framework with Mexico) — us. World Nuclear Association country profile. CapEx blank. First Mexico fission_smr row.",
    "hunt_energy_fission_smr",
    investment_type="other",
    bib_type="ngo",
    chicago='World Nuclear Association. “Nuclear Power in Mexico.” Updated July 8, 2026. https://world-nuclear.org/information-library/country-profiles/countries-g-n/mexico.',
    annotation="WNA: U.S.–Mexico 123 agreement in force Nov 2022. Supports mexico_us_123_agreement_2022.",
    evid_note="Opened World Nuclear Association Mexico profile (123 agreement in-force note).",
)

# 9. port_ownership / prc — CHINAICTC Corinto Julia Herrera credit USD 126.6m
row_doc(
    "chinaitc_corinto_julia_herrera_126p6m_2025",
    "infrastructure",
    "port_ownership",
    "prc",
    "CHINAICTC — Corinto Centro Logístico Julia Herrera credit (USD 126.6m)",
    "Nicaragua",
    "10–12 Jul 2025 Canal 4: Asamblea Nacional approved credit agreement for expansion/modernization of Centro Logístico Julia Herrera de Pomares (San Isidro, El Realejo) supporting Puerto Corinto; total financing ~USD 149m of which USD 126.6m is Chinese credit from Iconic Technology Company Limited (CHINAICTC) and USD 22.4m state counterpart; agreement signed 20 Jun 2025 MHCP–CHINAICTC; EPN executes. CapEx/investment = USD 126.6m Chinese credit face. Fills Nicaragua×port_ownership empty cell.",
    "126600000",
    "2025-07-10",
    "2025",
    "12.540",
    "-87.140",
    "Centro Logístico Julia Herrera de Pomares, San Isidro / El Realejo, Chinandega (Puerto Corinto logistics hub), Nicaragua.",
    "canal4_corinto_chinaitc_20250710",
    "La Asamblea Nacional de Nicaragua aprobó un acuerdo de crédito que permitirá la ampliación y modernización del Centro Logístico Julia Herrera de Pomares, ubicado en San Isidro, El Realejo. El financiamiento asciende a 149 millones de dólares, de los cuales 126.6 millones provienen de un crédito con China y 22.4 millones corresponden a una contrapartida estatal. El convenio fue suscrito el pasado 20 de junio de 2025 entre el Ministerio de Hacienda y Crédito Público y la empresa Iconic Technology Company Limited (CHINAICTC).",
    "https://www.canal4.com.ni/asamblea-aprueba-credito-para-fortalecer-infraestructura-portuaria-en-nicaragua/",
    "Actor: Iconic Technology Company Limited / CHINAICTC (PRC lender) — prc; EPN host. Officialist TV press quoting Asamblea approval — value treated as documented credit face from named decree coverage. First Nicaragua port_ownership row.",
    "hunt_infra_port_ownership",
    investment_type="financing",
    evidence="proxy",
    bib_type="news",
    chicago='Canal 4. “Asamblea aprueba crédito para fortalecer infraestructura portuaria en Nicaragua.” July 10, 2025. https://www.canal4.com.ni/asamblea-aprueba-credito-para-fortalecer-infraestructura-portuaria-en-nicaragua/.',
    annotation="Canal 4: CHINAICTC USD 126.6m Corinto Julia Herrera logistics credit. Supports chinaitc_corinto_julia_herrera_126p6m_2025.",
    evid_note="Opened Canal 4 10 Jul 2025 Asamblea Corinto CHINAICTC credit article.",
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
    print(f"Cycle 168 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
