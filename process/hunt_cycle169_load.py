#!/usr/bin/env python3
"""Cycle 169 hunt: shuffle_seed=20261169; equal budget; U.S./PRC split; thin after.

Canonical shuffle: lithium, solar, balsa, nickel, building_materials, power_plants_grid,
fission_smr, engineering_epc, rail, other_renewables, port_cranes, copper, wind,
port_ownership, graphite, niobium, water, bridges_roads.

Thin top-up (recomputed after equal pass): balsa / nickel / fission_smr (tied graphite) —
balsa/nickel/fission dry this pass (prior MoUs/COD already logged; no new signed CapEx).
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


# 1. lithium / us — Colombia–U.S. Critical Minerals Framework (Barranquilla)
row_doc(
    "colombia_us_critical_minerals_framework_2026",
    "resources",
    "lithium",
    "us",
    "U.S. Department of State — Critical Minerals Framework with Colombia (Barranquilla)",
    "Colombia",
    "8 Sep 2026: Secretary Rubio and Colombian Foreign Minister Omar Bula sign a U.S.–Colombia Critical Minerals Framework to secure resilient supply chains for critical minerals and rare earths, committing both governments to mobilize guarantees, loans, equity, offtake, insurance, or regulatory facilitation to jointly identify and finance mining and processing projects within six months. CapEx blank (non-binding framework; no named mine CapEx). Lithium subcategory proxy for critical-minerals diplomacy cell (Colombia×lithium/critical minerals under-covered).",
    "",
    "",
    "2026",
    "",
    "",
    "Framework signing in Barranquilla; no single named mine site — lat/lon blank.",
    "state_colombia_critical_minerals_20260908",
    "Establishes a U.S.-Colombia framework to secure resilient, diversified, and fair supply chains for critical minerals and rare earths, committing both governments to mobilize government and private sector support—via guarantees, loans, equity, offtake arrangements, insurance, or regulatory facilitation—to jointly identify and finance mining and processing projects within six months of signing.",
    "https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation",
    "Actor: U.S. Department of State (us). Opened State.gov Spokesperson release 8 Sep 2026. Distinct from colombia_us_civil_nuclear_mou_2026 (nuclear MoU same day). CapEx blank.",
    "hunt_cycle169",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='U.S. Department of State. “Secretary Rubio and Colombian Foreign Minister Bula Sign Arrangements on Critical Minerals and Civil Nuclear Cooperation.” September 8, 2026. https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation.',
    annotation="State.gov: U.S.–Colombia Critical Minerals Framework. Supports colombia_us_critical_minerals_framework_2026.",
    evid_note="Opened State.gov 8 Sep 2026 Barranquilla critical minerals framework release.",
)

# 2. lithium / us — Peru–U.S. critical minerals MoU (Washington ministerial)
row_doc(
    "peru_us_critical_minerals_mou_2026",
    "resources",
    "lithium",
    "us",
    "U.S. Department of State / Peru Cancillería — Critical Minerals and Rare Earths MoU",
    "Peru",
    "4 Feb 2026: Peruvian Foreign Minister Hugo de Zela signs a non-binding Memorandum of Understanding on critical minerals and rare earths with the United States at the State Department Critical Minerals Ministerial in Washington. Facilitates joint identification of priority projects and access to financial and technological instruments; Peru lists lithium among ten U.S.-identified critical minerals present in-country. CapEx blank (MoU; no named CapEx package). Fills Peru×lithium diplomacy cell.",
    "",
    "",
    "2026",
    "",
    "",
    "Ministerial MoU signed in Washington; no single named mine site — lat/lon blank.",
    "gobpe_peru_critical_minerals_mou_20260204",
    "El canciller Hugo de Zela suscribió en Washington D.C. un Memorándum de Entendimiento (MdE) sobre cooperación en minerales críticos y tierras raras con los Estados Unidos. El acuerdo facilita la identificación conjunta de proyectos prioritarios y el acceso a instrumentos financieros y tecnológicos… El Perú cuenta actualmente con diez minerales críticos… litio…",
    "https://www.gob.pe/institucion/rree/noticias/1347576-canciller-hugo-de-zela-suscribio-memorandum-de-entendimiento-sobre-minerales-criticos-en-washington-d-c",
    "Actor: U.S. MoU partner (us); Peru Cancillería primary Spanish text. Opened gob.pe RREE Nota 27-26. Distinct from dfc_cerro_pasco_quiulacocha_5m_2026 (project funding). CapEx blank.",
    "hunt_cycle169",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='Perú, Ministerio de Relaciones Exteriores. “Canciller Hugo de Zela suscribió Memorándum de Entendimiento sobre minerales críticos en Washington D.C.” February 4, 2026. https://www.gob.pe/institucion/rree/noticias/1347576-canciller-hugo-de-zela-suscribio-memorandum-de-entendimiento-sobre-minerales-criticos-en-washington-d-c.',
    annotation="gob.pe RREE: Peru–U.S. critical minerals MoU. Supports peru_us_critical_minerals_mou_2026.",
    evid_note="Opened gob.pe Cancillería Spanish MoU release 4 Feb 2026.",
)

# 3. lithium / us — Paraguay–U.S. critical minerals MoU
row_doc(
    "paraguay_us_critical_minerals_mou_2026",
    "resources",
    "lithium",
    "us",
    "U.S. Department of State / Paraguay MRE — Critical Minerals MoU",
    "Paraguay",
    "4 Feb 2026: Paraguayan Foreign Minister Rubén Ramírez Lezcano signs a Memorandum of Understanding on critical-minerals cooperation with the United States at the Critical Minerals Ministerial in Washington. Commits both sides to intensify cooperation to accelerate secure supplies of critical minerals for advanced technology and defense, using U.S. industrial demand/storage and Paraguay’s strategic reserves. CapEx blank (MoU). Fills Paraguay×critical-minerals/lithium diplomacy cell (under-covered).",
    "",
    "",
    "2026",
    "",
    "",
    "Ministerial MoU; no named mine site — lat/lon blank.",
    "mre_paraguay_critical_minerals_mou_20260204",
    "Mediante el Memorándum de Entendimiento, Paraguay y los Estados Unidos se comprometen a intensificar los esfuerzos de cooperación para acelerar el suministro seguro de minerales críticos necesarios para apoyar la fabricación de tecnologías avanzadas y de defensa… El acuerdo incluye… la demanda industrial y la infraestructura de almacenamiento de los Estados Unidos, así como las reservas estratégicas de Paraguay.",
    "https://www.mre.gov.py/paraguay-refuerza-alianza-con-ee-uu-y-se-suma-a-iniciativa-sobre-minerales-criticos/",
    "Actor: U.S. MoU partner (us); Paraguay MRE primary Spanish text. Opened mre.gov.py 4 Feb 2026. CapEx blank.",
    "hunt_cycle169",
    investment_type="other",
    evidence="documented",
    bib_type="government",
    chicago='Paraguay, Ministerio de Relaciones Exteriores. “Paraguay refuerza alianza con EE.UU. y se suma a iniciativa sobre minerales críticos.” February 4, 2026. https://www.mre.gov.py/paraguay-refuerza-alianza-con-ee-uu-y-se-suma-a-iniciativa-sobre-minerales-criticos/.',
    annotation="Paraguay MRE: U.S.–Paraguay critical minerals MoU. Supports paraguay_us_critical_minerals_mou_2026.",
    evid_note="Opened Paraguay MRE Spanish MoU release 4 Feb 2026.",
)

# 4. lithium / us — Ecuador–U.S. critical minerals framework
row_doc(
    "ecuador_us_critical_minerals_framework_2026",
    "resources",
    "lithium",
    "us",
    "U.S. Department of State / Ecuador Cancillería — Critical Minerals and Rare Earths Supply Framework",
    "Ecuador",
    "4 Feb 2026: Ecuadorian Foreign Minister Gabriela Sommerfeld signs the Framework between Ecuador and the United States for Securing Supply in the Mining and Processing of Critical Minerals and Rare Earths at the State Department Critical Minerals Ministerial. Non-binding cooperation to foster investment, mobilize capital, coordinate mining-project support, and promote technology transfer; transparency/traceability measures against illegal mining. CapEx blank. Fills Ecuador×critical-minerals diplomacy cell.",
    "",
    "",
    "2026",
    "",
    "",
    "Ministerial framework; no named mine site — lat/lon blank.",
    "eltelegrafo_ecuador_critical_minerals_20260204",
    "Como parte de la agenda, Ecuador suscribió el “Marco entre el Ecuador y los Estados Unidos para el Aseguramiento del Suministro en la Minería y el Procesamiento de Minerales Críticos y Tierras Raras”… El documento plantea fortalecer y diversificar las cadenas de suministro mediante cooperación orientada a fomentar inversiones, movilizar capitales, coordinar apoyo a proyectos mineros y promover transferencia de tecnologías, indicó la Cancillería.",
    "https://www.eltelegrafo.com.ec/noticias/nacionales/210/ecuador-participo-conferencia-ministerial-minerales-criticos",
    "Actor: U.S. framework partner (us). Opened El Telégrafo 4 Feb 2026 quoting Cancillería. Corroborated by State.gov ministerial fact sheet listing Ecuador among eleven new MoUs. CapEx blank.",
    "hunt_cycle169",
    investment_type="other",
    evidence="documented",
    bib_type="news",
    chicago='El Telégrafo. “Ecuador participó en conferencia ministerial sobre minerales críticos en Washington D. C.” February 4, 2026. https://www.eltelegrafo.com.ec/noticias/nacionales/210/ecuador-participo-conferencia-ministerial-minerales-criticos.',
    annotation="El Telégrafo / Cancillería: Ecuador–U.S. critical minerals framework. Supports ecuador_us_critical_minerals_framework_2026.",
    evid_note="Opened El Telégrafo 4 Feb 2026 Cancillería-sourced framework article.",
)

# 5. engineering_epc / allied — Casale USD 465m EPC Villeta green fertilizer (ATOME)
row_doc(
    "casale_atome_villeta_epc_465m_2025",
    "infrastructure",
    "engineering_epc",
    "allied",
    "Casale S.A. (Switzerland) — EPC for ATOME Villeta green fertilizer plant",
    "Paraguay",
    "7 Apr 2025: Swiss Casale announces definitive USD 465 million fixed-price lump-sum EPC contract with ATOME PLC for the Villeta green fertilizer plant (260,000 t/y zero-carbon fertiliser using 100% renewable baseload power; site in tax-free zone with 145 MW renewable PPA). Production targeted within 38 months of FID. CapEx = USD 465m EPC contract value (project total cited USD 625m on page; row uses EPC figure). Fills Paraguay×engineering_epc cell.",
    "465000000",
    "2025-04-07",
    "2025",
    "-25.51",
    "-57.56",
    "Villeta, Departamento Central, Paraguay (ATOME/Casale named site on Paraguay River corridor).",
    "casale_villeta_epc_20250407",
    "Casale… proudly announces the signing of a definitive $465 million Engineering, Procurement, and Construction (EPC) contract with ATOME PLC… world’s first green fertilizer plant in Villeta, Paraguay… produce 260,000 tonnes of zero-carbon fertiliser per year using 100% renewable baseload power… The Villeta site benefits from a 145MW renewable power purchase agreement and is situated in a tax-free zone… total estimated cost of US$625 million",
    "https://casale.ch/casale-signs-definitive-465-million-epc-contract-for-worlds-first-large-scale-green-fertilizer-plant-in-villeta-paraguay/",
    "Actor: Casale S.A. (Switzerland) — allied. Opened Casale company release 7 Apr 2025. Value = USD 465m EPC (not full project USD 625m). FID later made unconditional May 2026 (not double-counted here).",
    "hunt_cycle169",
    investment_type="epc",
    evidence="documented",
    bib_type="company",
    chicago='Casale S.A. “Casale Signs Definitive $465 Million EPC Contract for World’s First Large-Scale Green Fertilizer Plant in Villeta, Paraguay.” April 7, 2025. https://casale.ch/casale-signs-definitive-465-million-epc-contract-for-worlds-first-large-scale-green-fertilizer-plant-in-villeta-paraguay/.',
    annotation="Casale: USD 465m Villeta EPC. Supports casale_atome_villeta_epc_465m_2025.",
    evid_note="Opened Casale company EPC announcement 7 Apr 2025.",
)

# 6. building_materials / allied — Holcim Ecuador ECOPact for Mundo Ambiensa
row_doc(
    "holcim_ambiensa_ecopact_mundo_guayaquil",
    "infrastructure",
    "building_materials",
    "allied",
    "Holcim Ecuador — ECOPact low-carbon concrete supply to Mundo Ambiensa (Guayaquil)",
    "Ecuador",
    "Holcim partners with developer Ambiensa on Mundo Ambiensa in west Guayaquil — Latin America’s largest social-housing project built with ECOPact (≥30% embodied-carbon reduction without offsets): >45 projects, 35,000 homes for ~180,000 people, due finished 2030. Holcim Ecuador supplied >75,000 m³ ECOPact (page figure). CapEx blank (materials supply volume disclosed, not USD CapEx). Distinct from holcim_guayaquil_calcined_clay_2025 (calcined-clay cement plant).",
    "",
    "",
    "2025",
    "-2.17",
    "-79.95",
    "West Guayaquil / vía a la Costa corridor (Mundo Ambiensa cluster; approximate pin).",
    "holcim_ambiensa_ecopact_story",
    "Holcim has partnered with Ambiensa to build Latin America’s largest social housing project for around 180,000 people – using ECOPact… Ambiensa is now building more than 45 projects in the west of the city as part of Mundo Ambiensa, to provide 35,000 homes… exclusively using ECOPact concrete, to reduce the embodied carbon of the buildings by at least 30% without offsets… To date, Holcim Ecuador has supplied more than 75,000m³ of ECOPact.",
    "https://www.holcim.com/who-we-are/our-stories/social-housing-ecuador",
    "Actor: Holcim (Switzerland) — allied. Opened Holcim global story page (retrieved 2026-10-02; project active through 2030). CapEx blank.",
    "hunt_cycle169",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Holcim. “Providing affordable housing to 180,000 in Ecuador with ECOPact.” https://www.holcim.com/who-we-are/our-stories/social-housing-ecuador.',
    annotation="Holcim: Mundo Ambiensa ECOPact supply Guayaquil. Supports holcim_ambiensa_ecopact_mundo_guayaquil.",
    evid_note="Opened Holcim ECOPact Mundo Ambiensa story page.",
)

# 7. wind / prc — CCCC La Mesita wind credit USD 57.4m (Estelí)
row_doc(
    "cccc_la_mesita_wind_57p4m_esteli_2025",
    "energy",
    "wind",
    "prc",
    "China Communications Construction Company (CCCC) — La Mesita wind plant credit / EPC finance (Estelí)",
    "Nicaragua",
    "1 Oct 2025 Acuerdo Presidencial 156-2025 authorizes Treasury to sign a CCCC Credit Facility Agreement for RMB 407,540,000 (~USD 57,400,000) for design, supply, construction and commissioning of wind plant ‘La Mesita’ in Estelí department; ENATREL executing agency. Asamblea approval reported 21 Oct 2025; Canal 4 cites 55.2 MW installed / 157,416 MWh/year. CapEx = USD 57.4m credit equivalent. Distinct from cccc_el_barro_wind_nicaragua_2025.",
    "57400000",
    "2025-10-01",
    "2025",
    "12.95",
    "-86.30",
    "San Nicolás / La Trinidad corridor, Estelí department (Canal 4 / ENATREL named municipalities; approximate pin).",
    "asamblea_ni_la_mesita_ap_156_2025",
    "suscriba con la Empresa China Communications Construction Company Limited (CCCC)… Acuerdo de Facilidad de Crédito por un monto de RMB407,540,000.00… equivalente aproximadamente a US$57,400,000.00… Proyecto “Diseño, suministro, construcción y puesta en servicio de una Planta de Generación de Energía Eléctrica, Eólica ‘La Mesita’, en el departamento de Estelí”, siendo el Organismo Ejecutor la Empresa Nacional de Transmisión Eléctrica.",
    "http://legislacion.asamblea.gob.ni/Normaweb.nsf/4c9d05860ddef1c50625725e0051e506/f2f0aec78df8d21606258d17006e1d7c?OpenDocument=",
    "Actor: CCCC (PRC SOE) — prc. Opened Asamblea Nacional Acuerdo Presidencial 156-2025 text. MW corroboration from Canal 4 21 Oct 2025 (55.2 MW). Value = USD 57.4m credit floor.",
    "hunt_cycle169",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='Nicaragua, Presidencia de la República. “Acuerdo Presidencial N°. 156-2025” (CCCC credit facility for La Mesita wind plant). October 1, 2025. http://legislacion.asamblea.gob.ni/Normaweb.nsf/4c9d05860ddef1c50625725e0051e506/f2f0aec78df8d21606258d17006e1d7c?OpenDocument=.',
    annotation="Asamblea NI AP 156-2025: CCCC La Mesita wind credit ~USD 57.4m. Supports cccc_la_mesita_wind_57p4m_esteli_2025.",
    evid_note="Opened Asamblea Normaweb AP 156-2025 La Mesita CCCC credit text.",
)

# 8. port_ownership / other — PTP Paraguay USD 2m bond for Villeta terminal
row_doc(
    "ptp_villeta_bond_usd2m_202504",
    "infrastructure",
    "port_ownership",
    "other",
    "PTP Paraguay SAE (PTP Group) — USD 2m bond placement for Terminal Puerto de Villeta",
    "Paraguay",
    "10 Apr 2025: PTP Paraguay SAE places Series 3+4 bonds totaling USD 2,000,000 under Global Bond Program USD3 on the Asunción exchange (USD 1m @ 8.00% due Feb 2029; USD 1m @ 8.50% due Jun 2030). Issuer jointly administers Terminal Puerto de Villeta inside ANNP facilities (operational alliance with Argentine/Uruguayan PTP Group). Funds 60–80% investments / 0–20% liability restructuring / 0–20% working capital. CapEx proxy = USD 2m placement (not full terminal CapEx). Fills Paraguay×port_ownership cell.",
    "2000000",
    "2025-04-10",
    "2025",
    "-25.51",
    "-57.56",
    "Terminal Portuaria de Villeta, Departamento Central (ANNP named site; Km 353 Río Paraguay).",
    "revistaplus_ptp_villeta_bond_20250414",
    "PTP Paraguay SAE posee la administración conjunta del Terminal Puerto de Villeta… El jueves 10 de abril de 2025 se realizó la colocación de los títulos de la series 3 y 4… Monto de la serie: 1.000.000… Monto de la serie: 1.000.000… Los fondos obtenidos serán destinados entre 60% y 80% a inversiones",
    "https://revistaplus.com.py/2025/04/14/ptp-paraguay-emite-bonos-por-us-2-millones-en-la-bolsa-de-asuncion/",
    "Actor: PTP Group (Uruguay/Argentina holding) — other (neither US nor PRC nor Five Eyes/EU ally HQ for side coding). Opened Revista PLUS 14 Apr 2025. ANNP page corroborates PTP GROUP operational alliance. Value = USD 2m bond placement.",
    "hunt_cycle169",
    investment_type="financing",
    evidence="documented",
    bib_type="news",
    chicago='Revista PLUS. “PTP Paraguay emite bonos por US$ 2 millones en la bolsa de Asunción.” April 14, 2025. https://revistaplus.com.py/2025/04/14/ptp-paraguay-emite-bonos-por-us-2-millones-en-la-bolsa-de-asuncion/.',
    annotation="Revista PLUS: PTP Villeta USD 2m bond. Supports ptp_villeta_bond_usd2m_202504.",
    evid_note="Opened Revista PLUS 14 Apr 2025 PTP Series 3+4 bond placement article.",
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
    print(f"Cycle 169 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
