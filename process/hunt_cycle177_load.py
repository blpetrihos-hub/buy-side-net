#!/usr/bin/env python3
"""Cycle 177 hunt: shuffle_seed=20261177; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261177)): building_materials, niobium,
rail, port_ownership, lithium, port_cranes, solar, graphite, power_plants_grid,
copper, bridges_roads, balsa, nickel, water, engineering_epc, other_renewables,
wind, fission_smr.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (AIMA/WITS Ecuador balsa, Centaurus/BRN/MMG/Atlantic nickel,
and Meitner/Colombia/Peru FIRST fission already logged). Holdovers unsigned:
CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail past MoU.
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


# 1. building_materials / other — Cementos Argos Colombia 2026 CapEx package
# Company argos.co URL returns 403 to automated clients; Forbes Colombia mirrors board CapEx.
row_doc(
    "cementos_argos_colombia_50m_2026",
    "infrastructure",
    "building_materials",
    "other",
    "Cementos Argos — Colombia 2026 CapEx modernization package (>USD 50m)",
    "Colombia",
    "24 Feb 2026 (Forbes Colombia citing company/board): Junta Directiva approves CapEx package of more than USD 50 million (~COP 200bn) for 2026 to strengthen/modernize cement, ready-mix, and aggregates operations in Colombia, including generative-AI process tools under “De la mina al mercado.” CapEx = USD 50m floor. Distinct from holcim_cemex_colombia_2026 acquisition.",
    "50000000",
    "2026-02-24",
    "2026",
    "",
    "",
    "Cementos Argos Colombia national cement/ready-mix/aggregates footprint — lat/lon blank (multi-site package).",
    "forbes_argos_colombia_capex_20260224",
    "La Junta Directiva de Cementos Argos aprobó un paquete de inversiones de capital por más de US$ 50 millones para 2026, con el objetivo de robustecer y modernizar sus operaciones en Colombia… los recursos -equivalentes a cerca de $200.000 millones- estarán destinados a fortalecer los negocios de cemento, concretos y agregados… Un componente central será la implementación de soluciones de inteligencia artificial de última generación…",
    "https://forbes.co/2026/02/24/actualidad/cementos-argos-invertira-mas-de-us-50-millones-en-colombia-para-modernizar-su-operacion/",
    "Actor: Cementos Argos (Grupo Argos; Colombian) — other. Opened Forbes Colombia 24 Feb 2026 citing board/company. CapEx attributed to stated >USD 50m floor.",
    "hunt_cycle177",
    investment_type="brownfield_expansion",
    evidence="documented",
    bib_type="trade_press",
    chicago='Forbes Colombia Staff. “Cementos Argos invertirá más de US$ 50 millones en Colombia para modernizar su operación.” Forbes Colombia, February 24, 2026. https://forbes.co/2026/02/24/actualidad/cementos-argos-invertira-mas-de-us-50-millones-en-colombia-para-modernizar-su-operacion/.',
    annotation="Forbes Colombia: Argos Colombia 2026 CapEx >USD 50m. Supports cementos_argos_colombia_50m_2026.",
    evid_note="Opened Forbes Colombia page 2026-10-02 (argos.co blocked 403 to fetch client).",
)

# 1b. building_materials / allied — Holcim México Grupo COMOSA ready-mix integration
row_doc(
    "holcim_comosa_mexico_2025",
    "infrastructure",
    "building_materials",
    "allied",
    "Holcim México — Grupo COMOSA ready-mix integration (+7 plants / ~300k m³/y)",
    "Mexico",
    "28 Oct 2025 (Holcim México): strategic investment integrating Grupo COMOSA ready-mix network — seven plants in Polotitlán, Atlacomulco, Cuautla, Cuernavaca, Xochitepec, Toluca, and El Marqués (Querétaro); adds ~300,000 m³/year installed concrete capacity; NextGen Growth 2030 frame. Transaction USD not disclosed on company page — CapEx blank. Distinct from holcim_cemex_colombia_2026 / holcim_macuspana_grind_55m_2024.",
    "",
    "",
    "2025",
    "",
    "",
    "COMOSA ready-mix footprint (Estado de México / Morelos / Querétaro) — lat/lon blank (seven-site network).",
    "holcim_mx_comosa_20251028",
    "Esta inversión, contempla la integración de Grupo COMOSA, empresa concretera con más de 56 años de trayectoria en México… Se suman siete nuevas ubicaciones estratégicas en Polotitlán, Atlacomulco, Cuautla, Cuernavaca, Xochitepec, Toluca y El Marqués (Querétaro), y con ello, la compañía incrementa su capacidad instalada en cerca de 300 mil m3 de concreto anuales…",
    "https://www.holcim.com.mx/holcim-mexico-refuerza-su-presencia-en-el-centro-del-pais-con-una-inversion-estrategica-en",
    "Actor: Holcim México (Swiss Holcim) — allied. Opened company Spanish release 28 Oct 2025. CapEx blank (amount not disclosed).",
    "hunt_cycle177",
    investment_type="ownership_equity",
    evidence="documented",
    bib_type="company",
    chicago='Holcim México. “Holcim México refuerza su presencia en el centro del país con una inversión estratégica en expansión y sostenibilidad.” October 28, 2025. https://www.holcim.com.mx/holcim-mexico-refuerza-su-presencia-en-el-centro-del-pais-con-una-inversion-estrategica-en.',
    annotation="Holcim México: COMOSA seven-plant ready-mix integration. Supports holcim_comosa_mexico_2025.",
    evid_note="Opened Holcim México company page 2026-10-02.",
)

# 2–3. niobium / rail / miss (dense)

# 4. port_ownership / allied — DP World Callao Adenda 4 CapEx package
row_doc(
    "dpworld_callao_adenda4_1470m_2026",
    "infrastructure",
    "port_ownership",
    "allied",
    "DP World Callao — Adenda N.° 4 Muelle Sur expansion package (~USD 1,470m incl. IGV)",
    "Peru",
    "17 Sep 2026 (MTC): Adenda N.° 4 proposal by DP World Callao for Container Terminal – South Pier contemplates investments of approximately USD 1,470 million including IGV to expand infrastructure/equipment, implement Antepuerto del Callao, and improve access roads; under joint evaluation (APN/DGISTR/Provías/Callao municipality). CapEx = USD 1,470m package face (proposal; not yet closed). Distinct from dpworld_callao_bicentennial_2024.",
    "1470000000",
    "2026-09-17",
    "2026",
    "-12.048",
    "-77.146",
    "Terminal de Contenedores Muelle Sur, Callao (MTC geography; approximate pin).",
    "mtc_dpworld_callao_adenda4_20260917",
    "Uno de los principales temas abordados fue la propuesta de Adenda N.° 4, presentada por DP World Callao, que contempla inversiones por aproximadamente USD 1,470 millones, incluido IGV, destinadas a ampliar la infraestructura y el equipamiento del terminal, implementar el Antepuerto del Callao y mejorar sus vías de acceso.",
    "https://www.gob.pe/institucion/mtc/noticias/1445564-mtc-y-dp-world-callao-impulsan-nuevas-inversiones-para-ampliar-capacidad-del-muelle-sur",
    "Actor: DP World Callao (DP World Dubai affiliate) — allied. Opened MTC Spanish notice 17 Sep 2026. Proposal-stage CapEx face.",
    "hunt_cycle177",
    investment_type="concession",
    evidence="documented",
    bib_type="government",
    chicago='Ministerio de Transportes y Comunicaciones (Perú). “MTC y DP World Callao impulsan nuevas inversiones para ampliar capacidad del Muelle Sur.” September 17, 2026. https://www.gob.pe/institucion/mtc/noticias/1445564-mtc-y-dp-world-callao-impulsan-nuevas-inversiones-para-ampliar-capacidad-del-muelle-sur.',
    annotation="MTC: DP World Callao Adenda 4 ~USD 1,470m. Supports dpworld_callao_adenda4_1470m_2026.",
    evid_note="Opened MTC gob.pe notice 2026-10-02.",
)

# 5–6. lithium / port_cranes / miss (dense)

# 7. solar / prc — Sungrow Tonachihua I Tlaxcala
# ECB 2026-09-15: USD/EUR=1.1539; MXN/EUR=19.7972 → USD/MXN=0.05828602024528721
row_doc(
    "sungrow_tonachihua_tlaxcala_2164mdp_2026",
    "energy",
    "solar",
    "prc",
    "Sungrow / Tonachihua Energía — Tonachihua I 120 MW PV + BESS (Tlaxcala/Hidalgo)",
    "Mexico",
    "15 Sep 2026 (Poder México citing Tonachihua Energía): Tonachihua I — 120 MW nominal PV with BESS sized at 30% of capacity / 3-hour autonomy; investment MXN 2,164 million; interconnection to SEN for Valle de México industry; sites Calpulalpan (Tlaxcala) and Emiliano Zapata (Hidalgo); Sungrow Renewable Energy Investment / Sungrow Investment & Holding Singapore vehicles. USD 126,130,947.81 via ECB 2026-09-15 cross. Distinct from sungrow_zelestra_* / sungrow_engie_tocopilla rows.",
    "2164000000",
    "2026-09-15",
    "2026",
    "",
    "",
    "Tonachihua I / Calpulalpan (Tlaxcala)–Emiliano Zapata (Hidalgo) — lat/lon blank pending verified array pin.",
    "poder_mexico_tonachihua_20260915",
    "Hoy está en el ojo de Tonachihua Energía, una empresa filial de la empresa china Sungrow, quien invertirá 2 mil 164 millones de pesos en la construcción de una granja solar y un sistema de almacenamiento… “El proyecto Tonachihua I consiste en la construcción, operación y mantenimiento de una central fotovoltaica con una potencia nominal de 120 MW con sistema de almacenamiento por baterías (BESS) equivalente al 30 por ciento de su capacidad y 3 horas de autonomía”…",
    "https://www.podermexico.mx/?p=11003",
    "Actor: Sungrow Power Supply via Tonachihua Energía (PRC) — prc. Opened Poder México 15 Sep 2026 quoting company project description. FX: ECB EXR D.USD.EUR and D.MXN.EUR 2026-09-15.",
    "hunt_cycle177",
    investment_type="greenfield",
    evidence="documented",
    currency="MXN",
    value_usd="126130947.81",
    fx_usd="0.0582860202",
    bib_type="trade_press",
    chicago='Jiménez, Enrique. “Tlaxcala sí existe para una eléctrica china que invertirá 2 mil 164 mdp en una granja solar.” Poder México, September 15, 2026. https://www.podermexico.mx/?p=11003.',
    annotation="Poder México/Tonachihua: Sungrow Tonachihua I MXN 2,164m. Supports sungrow_tonachihua_tlaxcala_2164mdp_2026.",
    evid_note="Opened Poder México page 2026-10-02; ECB FX cross 2026-09-15.",
)

# 8–9. graphite / power_plants_grid / miss

# 10. copper / us — Cerro Verde USD 350m revolving credit facility
# (fcx_cerro_verde_stake_107m_2026 already active — skip stake re-add)
row_doc(
    "fcx_cerro_verde_rcf_350m_2026",
    "resources",
    "copper",
    "us",
    "Cerro Verde — new USD 350m five-year senior unsecured revolving credit facility",
    "Peru",
    "May 2026 (FCX 2Q2026 exhibit): Cerro Verde entered a new USD 350 million five-year senior unsecured revolving credit facility maturing May 2031, replacing its prior facility; at 30 Jun 2026 no borrowings outstanding. Financing face = USD 350m. Distinct from fcx_cerro_verde_stake_107m_2026 ownership add.",
    "350000000",
    "2026-05-31",
    "2026",
    "-16.53",
    "-71.60",
    "Cerro Verde mine, Arequipa Region (company geography; approximate pin).",
    "fcx_2q2026_exhibit991",
    "In May 2026, FCX entered into a new $3.0 billion, five-year senior unsecured revolving credit facility that matures in May 2031, which replaced its prior revolving credit facility, and Cerro Verde entered into a new $350 million, five-year, senior unsecured revolving credit facility that matures in May 2031, which replaced its prior revolving credit facility.",
    "https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm",
    "Actor: Freeport-controlled Cerro Verde (U.S. majority) — us. Opened same SEC Exhibit 99.1. U.S. side-balance financing for copper.",
    "hunt_cycle177",
    investment_type="financing",
    evidence="documented",
    bib_type="company",
    chicago='Freeport-McMoRan Inc. “FCX Reports Second-Quarter and Six-Month 2026 Results.” Exhibit 99.1 to Form 8-K, June 30, 2026 reporting period. https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm.',
    annotation="FCX SEC: Cerro Verde USD 350m RCF. Supports fcx_cerro_verde_rcf_350m_2026.",
    evid_note="Opened FCX SEC Exhibit 99.1 2026-10-02 (shared URL with stake purchase).",
)

# 10c. copper / allied — Antamina MEIA life-extension CapEx envelope
row_doc(
    "antamina_meia_2bn_2024",
    "resources",
    "copper",
    "allied",
    "Antamina — SENACE MEIA life-extension CapEx envelope (~USD 2bn to 2036)",
    "Peru",
    "15 Feb 2024 (Antamina): SENACE approves Modificación del Estudio de Impacto Ambiental (MEIA) enabling approximately USD 2 billion of staged investment to extend operations from 2028 to 2036 in Áncash — pit footprint, waste dumps, and tailings dam optimization within existing area. Shareholders BHP, Glencore, Teck, Mitsubishi. CapEx = USD 2bn envelope. Distinct from caterpillar_antamina_798_45_2026 fleet row and later ITS ~USD 300m tranche.",
    "2000000000",
    "2024-02-15",
    "2024",
    "-9.53",
    "-77.05",
    "Antamina mine, Áncash Region (company geography; approximate pin).",
    "antamina_meia_20240215",
    "Esta aprobación permite habilitar una inversión aproximada de US$ 2 mil millones a lo largo de los próximos años, siguiendo el proceso de gobernanza interna de Antamina, lo que permitirá a la empresa extender sus operaciones desde 2028 hasta el año 2036 en la región Áncash… Antamina es una de las empresas productoras de cobre líderes en el Perú… sus accionistas son BHP, Glencore, Teck y Mitsubishi.",
    "https://www.antamina.com/noticias/gobierno-peruano-aprueba-modificacion-estudio-de-impacto-ambiental-meia-antamina/",
    "Actor: Compañía Minera Antamina (BHP/Glencore/Teck/Mitsubishi JV) — allied. Opened company Spanish release 15 Feb 2024.",
    "hunt_cycle177",
    investment_type="brownfield_expansion",
    evidence="documented",
    bib_type="company",
    chicago='Compañía Minera Antamina. “Gobierno peruano aprueba Modificación del Estudio de Impacto Ambiental (MEIA) de Antamina.” February 15, 2024. https://www.antamina.com/noticias/gobierno-peruano-aprueba-modificacion-estudio-de-impacto-ambiental-meia-antamina/.',
    annotation="Antamina: SENACE MEIA CapEx envelope USD 2bn. Supports antamina_meia_2bn_2024.",
    evid_note="Opened Antamina company page 2026-10-02.",
)

# 10d. copper / us — Caterpillar CAT 798AC fleet for Codelco Andina Mina Rajo
row_doc(
    "caterpillar_andina_798ac_18_2026",
    "resources",
    "copper",
    "us",
    "Caterpillar — Codelco Andina Mina Rajo 18× CAT 798AC haul trucks (to 57-unit fleet)",
    "Chile",
    "30 Apr 2026 (Portal Minero): Codelco Andina completes arrival of last high-tonnage haul truck at Plataforma 3700 / Mina Rajo — 18 new CAT 798AC CAEX units (400 t payload) bring operating fleet to 57 trucks; kits shipped from the United States via San Antonio and Coquimbo ports then assembled on site; +80 t payload per cycle vs prior generation. CapEx USD not disclosed — blank. Distinct from caterpillar_antamina_798_45_2026 Peru fleet row.",
    "",
    "",
    "2026",
    "-32.95",
    "-70.28",
    "Codelco Andina Mina Rajo / Plataforma 3700, Valparaíso Region (press geography; approximate pin).",
    "portal_minero_andina_798ac_20260430",
    "Un importante hito para la continuidad operacional concretó Codelco Andina con el arribo del último camión de extracción de alto tonelaje a la Plataforma 3700, ubicada en la Mina Rajo, llegando así una flota de 18 equipos de última generación que desde ahora completan un total de 57 camiones en funcionamiento. La nueva flota está compuesta por equipos CAEX modelo CAT 798AC… Los camiones, con una capacidad de carga de 400 toneladas, fueron trasladados por partes desde Estados Unidos hasta Chile, ingresando por los puertos de San Antonio y Coquimbo.",
    "https://www.portalminero.com/wp/con-18-nuevos-camiones-de-extraccion-codelco-andina-completa-moderna-flota-de-equipos-en-su-mina-rajo/",
    "Actor: Caterpillar (U.S.) equipment for Codelco Andina — us. Opened Portal Minero 30 Apr 2026. CapEx blank (amount not disclosed).",
    "hunt_cycle177",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="trade_press",
    chicago='Portal Minero. “Con 18 nuevos camiones de extracción Codelco Andina completa moderna flota de equipos en su Mina Rajo.” April 30, 2026. https://www.portalminero.com/wp/con-18-nuevos-camiones-de-extraccion-codelco-andina-completa-moderna-flota-de-equipos-en-su-mina-rajo/.',
    annotation="Portal Minero: Codelco Andina 18× CAT 798AC. Supports caterpillar_andina_798ac_18_2026.",
    evid_note="Opened Portal Minero page 2026-10-02.",
)

# 11–15. bridges_roads / balsa / nickel / water / engineering_epc / miss (thin dry)

# 16. other_renewables / miss (byd_brazil_bess_factory_500m_2026 already active)

# 17. wind / other — Ecopetrol 49% JK1/JK2 stake from AES Colombia
row_doc(
    "ecopetrol_jk1_jk2_49pct_25p5m_2026",
    "energy",
    "wind",
    "other",
    "Ecopetrol — 49% interest in AES Colombia JK1/JK2 wind projects (~USD 25.5m)",
    "Colombia",
    "20 May 2026 (Ecopetrol / PR Newswire): conditions precedent fulfilled for acquisition of 49% interest in JK1 and JK2 (two of six Jemeiwaa Ka’I cluster projects in La Guajira) under Investment Framework Agreement with AES Colombia dated 14 Apr 2025; aggregate acquisition value ~USD 25.5 million; 259 MW assigned capacity + 35 km transmission to collector substation; remaining four projects’ conditions still pending. CapEx/investment = USD 25.5m acquisition face. Distinct from aes_jk1_jk2_idb_invest_150m_2025 and aes_colombia_guajira_549mw_1bn_2026 CapEx.",
    "25500000",
    "2026-05-20",
    "2026",
    "",
    "",
    "JK1/JK2 / Jemeiwaa Ka’I cluster, Uribia, La Guajira — lat/lon blank (multi-turbine cluster).",
    "ecopetrol_jk1_jk2_20260520",
    "Ecopetrol S.A… announces that, pursuant to the Investment Framework Agreement entered into with AES Colombia… the conditions precedent and legal requirements for the acquisition of a 49% interest in two of the six projects comprising the wind cluster have been fulfilled. The JK1 and JK2 projects… have an aggregate acquisition value of approximately USD 25.5 million. The projects have an assigned capacity of 259 MW and include a 35-kilometer transmission line…",
    "https://www.prnewswire.com/news-releases/ecopetrol-advances-acquisition-of-the-jemeiwaa-kai-wind-cluster-in-la-guajira-with-the-purchase-of-a-49-interest-in-the-jk1-and-jk2-wind-projects-302777666.html",
    "Actor: Ecopetrol (Colombian majority state-owned) — other; seller/partner AES Colombia (U.S.). Opened Ecopetrol PR Newswire 20 May 2026.",
    "hunt_cycle177",
    investment_type="ownership_equity",
    evidence="documented",
    bib_type="company",
    chicago='Ecopetrol S.A. “Ecopetrol advances acquisition of the Jemeiwaa Ka’I wind cluster in La Guajira with the purchase of a 49% interest in the JK1 and JK2 wind projects.” PR Newswire, May 20, 2026. https://www.prnewswire.com/news-releases/ecopetrol-advances-acquisition-of-the-jemeiwaa-kai-wind-cluster-in-la-guajira-with-the-purchase-of-a-49-interest-in-the-jk1-and-jk2-wind-projects-302777666.html.',
    annotation="Ecopetrol: JK1/JK2 49% ~USD 25.5m. Supports ecopetrol_jk1_jk2_49pct_25p5m_2026.",
    evid_note="Opened Ecopetrol PR Newswire page 2026-10-02.",
)

# 18. fission_smr / miss (thin)


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
    print(f"Cycle 177 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
