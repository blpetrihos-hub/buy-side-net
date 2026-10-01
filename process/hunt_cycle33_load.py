#!/usr/bin/env python3
"""Cycle 33 hunt: shuffle_seed=20261033; equal budget across 18 subcategories."""
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


# seed 20261033 order:
# balsa, water, port_ownership, bridges_roads, solar, rail, nickel, engineering_epc,
# fission_smr, power_plants_grid, niobium, wind, other_renewables, port_cranes,
# lithium, building_materials, copper, graphite

# 1 resources/balsa — miss (WITS/AIMA pairs already)
# 2 resources/water — miss (Almar Centinela / Acciona Yanacocha already)
# 3 infrastructure/port_ownership — miss (DP World San Antonio/Callao extensions still proposals)

# 4 infrastructure/bridges_roads — ERG El Estanquillo–Popayán + CRBC Arequipa evidence upgrade
A(
    {
        "id": "erg_estanquillo_popayan_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "ERG Vías Ciudad Blanca (ERG 90% / MIA 10%) — El Estanquillo–Popayán APP",
        "country": "Colombia",
        "asset": "5 Mar 2026 ANI award of public-initiative APP for El Estanquillo–Popayán corridor to Estructura Plural ERG Vías Ciudad Blanca (ERG Compañía de Infraestructura y Desarrollo SAS — British capital — 90%; MIA Grupo Empresarial SAS 10%): finance, final designs, environmental/land/social management, construction/rehab/improvement, O&M. Economic offer COP 6.56 trillion (present value) as ANI contributions; MinTransporte cites estimated total investment COP 8.8 trillion. 25-year APP incl. preconstruction (~24 months) + ~4.5 years construction",
        "investment_type": "ppp_concession",
        "value": "6560000000000",
        "currency": "COP",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "2.3",
        "lon": "-76.7",
        "geo_note": "El Estanquillo–Popayán corridor, Cauca / SW Colombia (ANI award geography; approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "ani_estanquillo_popayan_20260305",
        "note": "Actor: ERG (British capital) majority — allied. Official ANI Spanish award page 5 Mar 2026. Value stored as COP 6.56tn ANI-aporte offer (MinTransporte COP 8.8tn total investment narrative not used as row value). Distinct from ohla_panama_panamericana_este_2025 and crbc_arequipa_la_joya_2026.",
    },
    {
        "id": "erg_estanquillo_popayan_2026",
        "retrieved": "2026-10-01",
        "source_id": "ani_estanquillo_popayan_20260305",
        "url": "https://www.ani.gov.co/gobierno-del-cambio-le-cumple-al-suroccidente-colombiano-ani-adjudico-la-estructura-plural-erg-vias",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "La Estructura Plural ERG Vías Ciudad Blanca, conformada por la empresa de capital británico ERG Compañía de Infraestructura y Desarrollo SAS con el 90% de participación y la colombiana MIA Grupo Empresarial SAS con el 10%, presentó una oferta económica por $6.56 billones que correspondería a los aportes ANI.",
        "note": "Opened ANI Colombia Spanish award notice 5 Mar 2026.",
    },
    {
        "id": "ani_estanquillo_popayan_20260305",
        "type": "government",
        "chicago": "Agencia Nacional de Infraestructura (Colombia). “Gobierno del Cambio le cumple al suroccidente colombiano: ANI adjudicó a la Estructura Plural ERG Vías Ciudad Blanca la concesión del proyecto El Estanquillo-Popayán.” 5 March 2026.",
        "url": "https://www.ani.gov.co/gobierno-del-cambio-le-cumple-al-suroccidente-colombiano-ani-adjudico-la-estructura-plural-erg-vias",
        "annotation": "Official ANI award of El Estanquillo–Popayán APP to ERG/MIA at COP 6.56tn ANI aportes. Supports erg_estanquillo_popayan_2026.",
        "supports": ["erg_estanquillo_popayan_2026", "hunt_infra_bridges_roads"],
    },
)

A(
    {
        "id": "crbc_arequipa_la_joya_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Consorcio Ejecutor Joya (CRBC Perú + Integral Consultores) — Arequipa–La Joya Componente III",
        "country": "Peru",
        "asset": "MTC/Provías Descentralizado OxI award for Vía Regional Arequipa–La Joya componente 3: ~20.5 km dual carriageway from puente Virgen de Chapi exit to La Joya district; Consorcio Ejecutor Joya (China Road and Bridge Corporation Sucursal del Perú + Integral Consultores); investment >S/ 408.7 million; 570 calendar days after technical dossier update; completion targeted Q1 2028. Official gob.pe MTC notice 24 Jul 2026 (buena pro 30 Jun 2026)",
        "investment_type": "public_works",
        "value": "408700000",
        "currency": "PEN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-16.5",
        "lon": "-71.8",
        "geo_note": "Arequipa–La Joya regional corridor (MTC notice; approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "mtc_arequipa_la_joya_20260724",
        "note": "Actor: CRBC (PRC) — prc. Cycle 33 upgrades prior UNVERIFIED proxy press cite to official MTC Spanish notice stating >S/408.7m and Consorcio Ejecutor Joya. PEN stored without FX.",
    },
    {
        "id": "crbc_arequipa_la_joya_2026",
        "retrieved": "2026-10-01",
        "source_id": "mtc_arequipa_la_joya_20260724",
        "url": "https://www.gob.pe/institucion/mtc/noticias/1423124-mtc-anuncia-ejecucion-de-nuevo-tramo-de-la-via-arequipa-la-joya-por-s-408-7-millones-mediante-obras-por-impuestos",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Provías Descentralizado (PVD), anunció la ejecución del componente 3 de la vía regional Arequipa–La Joya, que permitirá construir un nuevo tramo de 20.5 kilómetros con una inversión superior a S/408.7 millones … La obra, a cargo del Consorcio Ejecutor Joya",
        "note": "Opened official Peruvian State Platform MTC Spanish notice 24 Jul 2026.",
    },
    {
        "id": "mtc_arequipa_la_joya_20260724",
        "type": "government",
        "chicago": "Ministerio de Transportes y Comunicaciones (Perú). “MTC anuncia ejecución de nuevo tramo de la vía Arequipa–La Joya por S/ 408.7 millones mediante Obras por Impuestos.” 24 July 2026.",
        "url": "https://www.gob.pe/institucion/mtc/noticias/1423124-mtc-anuncia-ejecucion-de-nuevo-tramo-de-la-via-arequipa-la-joya-por-s-408-7-millones-mediante-obras-por-impuestos",
        "annotation": "Official MTC OxI announcement for Arequipa–La Joya componente 3 at >S/408.7m to Consorcio Ejecutor Joya. Supports crbc_arequipa_la_joya_2026.",
        "supports": ["crbc_arequipa_la_joya_2026", "hunt_infra_bridges_roads"],
    },
)

# 5 energy/solar — Aldesa (CRCC) Mexico hybrid solar EPC
A(
    {
        "id": "aldesa_mexico_solar_hybrid_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Aldesa (CRCC) — Mexico hybrid solar EPC (420 MWp + 150 MW BESS)",
        "country": "Mexico",
        "asset": "17 Jul 2026: Aldesa (Spanish infra group owned by China Railway Construction Corporation) awarded turnkey EPC for undisclosed-site hybrid solar in Mexico: 420 MWp PV + 150 MW BESS + new 400 kV interconnection with >24 km transmission between new substations; budget >EUR 160 million (press paraphrase of company; Aldesa own page confirms scope without EUR). Site/client/COD undisclosed",
        "investment_type": "epc",
        "value": "160000000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "23.0",
        "lon": "-102.0",
        "geo_note": "Mexico hybrid solar EPC — site undisclosed (Aldesa release); approximate national centroid pin.",
        "evidence": "proxy",
        "source_id": "aldesa_mexico_solar_20260717",
        "note": "Actor: Aldesa (CRCC-owned) — prc. Company Spanish page documents scope; EUR >160m from Europa Press / El Economista paraphrases of Aldesa comunicado — UNVERIFIED proxy for exact EUR. Distinct from trina_pillanco_biobio_2026.",
    },
    {
        "id": "aldesa_mexico_solar_hybrid_2026",
        "retrieved": "2026-10-01",
        "source_id": "aldesa_mexico_solar_20260717",
        "url": "https://aldesa.com/aldesa-se-adjudica-un-parque-solar-en-mexico/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El proyecto abarca desde la ingeniería de detalle hasta la puesta en marcha, incluyendo una planta fotovoltaica de 420 MWp, un sistema de almacenamiento de energía (BESS) de 150 MW y la interconexión en alta tensión (400 kV) con más de 24 km de líneas de transmisión entre subestaciones, también de nueva construcción.",
        "note": "Opened Aldesa Spanish company page 17 Jul 2026 (scope). EUR value from paired press paraphrases — marked proxy.",
    },
    {
        "id": "aldesa_mexico_solar_20260717",
        "type": "company",
        "chicago": "Aldesa. “Aldesa se adjudica un parque solar en México.” 17 July 2026.",
        "url": "https://aldesa.com/aldesa-se-adjudica-un-parque-solar-en-mexico/",
        "annotation": "Company primary on Mexico 420 MWp + 150 MW BESS turnkey EPC (site undisclosed). Supports aldesa_mexico_solar_hybrid_2026.",
        "supports": ["aldesa_mexico_solar_hybrid_2026", "hunt_energy_solar"],
    },
)

# 6 infrastructure/rail — miss (OHLA L9 / Siemens–Sonda already)

# 7 resources/nickel — Jervois SMP CAPEX fill (proxy)
A(
    {
        "id": "jervois_smp_restart_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "Jervois — São Miguel Paulista nickel-cobalt refinery restart (São Paulo)",
        "country": "Brazil",
        "asset": "25 Nov 2025 FID/investment approval to restart Latin America’s only electrolytic Class 1 Ni-Co refinery; process MHP + Co hydroxide; forecast 12,000 mt/yr Ni + 2,000 mt/yr Co cathode; construction ~12 months from Jan 2026 mobilisation; ramp-up across 2027. Company primary PDF does not state CAPEX; Brasil Mineral (26 Nov 2025) citing the company reports planned investment USD 130 million (~USD 80m equity) — UNVERIFIED proxy for USD figure",
        "investment_type": "brownfield_restart",
        "value": "130000000",
        "currency": "USD",
        "value_usd": "130000000",
        "fx_usd": "1",
        "fx_date": "2025-11-25",
        "year": "2025",
        "status": "active",
        "lat": "-23.5",
        "lon": "-46.45",
        "geo_note": "São Miguel Paulista refinery, São Paulo city limits (Jervois release).",
        "evidence": "proxy",
        "source_id": "brasilmineral_jervois_smp_20251126",
        "note": "Actor: Jervois (U.S.-controlled private group) — us. Cycle 33 adds UNVERIFIED proxy USD 130m from Brasil Mineral citing company; FID timing/scope remain from company PDF. Complements ausenco_jervois_smp_epcm_2026.",
    },
    {
        "id": "jervois_smp_restart_2025",
        "retrieved": "2026-10-01",
        "source_id": "brasilmineral_jervois_smp_20251126",
        "url": "https://brasilmineral.com.br/noticias/grupo-jervois-anuncia-projeto-de-retomada-da-refinaria-de-sao-miguel-paulista",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "O investimento previsto para o empreendimento é de US$ 130 milhões, sendo cerca de US$ 80 milhões de capital próprio.",
        "note": "Opened Brasil Mineral Portuguese trade press 26 Nov 2025 citing company USD 130m. Paired with Jervois 25 Nov 2025 PDF for FID/scope.",
    },
    {
        "id": "brasilmineral_jervois_smp_20251126",
        "type": "press",
        "chicago": "Brasil Mineral. “Grupo Jervois anuncia projeto de retomada da refinaria de São Miguel Paulista.” 26 November 2025.",
        "url": "https://brasilmineral.com.br/noticias/grupo-jervois-anuncia-projeto-de-retomada-da-refinaria-de-sao-miguel-paulista",
        "annotation": "Trade press citing Jervois USD 130m SMP restart CAPEX. Supports jervois_smp_restart_2025 (proxy value).",
        "supports": ["jervois_smp_restart_2025", "hunt_res_nickel"],
    },
)

# 8 infrastructure/engineering_epc — miss (Ausenco SMP / PowerChina UFN-III already)
# 9 energy/fission_smr — miss (Rosatom Brazil SMR still ministerial talk / no contract)
# 10 energy/power_plants_grid — miss (avoid over-invest)
# 11 resources/niobium — miss (CBMM already)
# 12 energy/wind — miss
# 13 energy/other_renewables — miss

# 14 infrastructure/port_cranes — Portonave electric yard fleet
A(
    {
        "id": "portonave_electric_fleet_61m_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Portonave (TIL) — electric terminal tractors + Kalmar e-reach stackers",
        "country": "Brazil",
        "asset": "3 Aug 2026 Portonave (TIL-owned Navegantes terminal) acquires 30 Terberg electric terminal tractors + 5 Kalmar electric reach stackers for ~BRL 61 million under REPORTO incentives; phased delivery with all units operational by Jan 2027; part of BRL 2bn plan also covering quay works, 2 STS and 14 e-RTGs (STS/e-RTG packages logged separately where sourced). Expected GHG cuts ~30% (e-TT fleet) / ~80% (e-RS fleet)",
        "investment_type": "equipment_supply",
        "value": "61000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-26.9",
        "lon": "-48.65",
        "geo_note": "Portonave terminal, Navegantes, Santa Catarina (company release).",
        "evidence": "documented",
        "source_id": "portonave_electric_fleet_20260803",
        "note": "Actor: Portonave under TIL (MSC/Swiss) — allied; equipment Kalmar (Finland) + Terberg (Netherlands). Company English release 3 Aug 2026. Distinct from kalmar_portonave_ers_2026 (order-level) and zpmc_portonave_sts_2025. BRL stored without FX.",
    },
    {
        "id": "portonave_electric_fleet_61m_2026",
        "retrieved": "2026-10-01",
        "source_id": "portonave_electric_fleet_20260803",
        "url": "https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-rusd61-million-in-new-electrically-powered-equipment",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Portonave … has acquired 30 electric terminal tractors (e-TTs) manufactured by Terberg in Malaysia and five electric reach stackers (e-RSs) manufactured by Kalmar in China. The investment totals approximately BRL 61 million",
        "note": "Opened Portonave English company news 3 Aug 2026.",
    },
    {
        "id": "portonave_electric_fleet_20260803",
        "type": "company",
        "chicago": "Portonave. “Portonave Invests R$61 Million in New Electrically Powered Equipment.” 3 August 2026.",
        "url": "https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-rusd61-million-in-new-electrically-powered-equipment",
        "annotation": "Company primary on BRL 61m electric yard equipment package at Navegantes. Supports portonave_electric_fleet_61m_2026.",
        "supports": ["portonave_electric_fleet_61m_2026", "hunt_infra_port_cranes"],
    },
)

# 15 resources/lithium — miss
# 16 infrastructure/building_materials — miss (CALCEM logged C32)
# 17 resources/copper — miss (Centinela / El Abra / Escondida already)

# 18 resources/graphite — Atlas Malacacheta maiden MRE / exploration program
A(
    {
        "id": "atlas_malacacheta_graphite_mre_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "us",
        "counterpart": "Atlas Critical Minerals — Malacacheta Graphite Project maiden MRE (Minas Gerais)",
        "country": "Brazil",
        "asset": "29 Sep 2026: Atlas Critical Minerals (NASDAQ: ATCX) announces maiden Mineral Resource Estimate for 100%-owned Malacacheta Graphite Project (Minas Gerais): 17.2 Mt Indicated @ 5.73% Cg + 7.0 Mt Inferred @ 5.40% Cg (~1.36 Mt contained graphite) from one of three contiguous tenements; PEA targeted Q2 2027. Prior SGS SK-1300 TRS (31 Jul 2025) recommended exploration program totaling USD 2.145 million (incl. 5,000 m drilling). Pre-FID resource milestone — not mine CAPEX",
        "investment_type": "exploration",
        "value": "2145000",
        "currency": "USD",
        "value_usd": "2145000",
        "fx_usd": "1",
        "fx_date": "2025-07-31",
        "year": "2026",
        "status": "active",
        "lat": "-17.8",
        "lon": "-42.1",
        "geo_note": "Malacacheta municipality, Minas Gerais (Atlas/SGS TRS geography; approximate pin).",
        "evidence": "documented",
        "source_id": "atlas_malacacheta_mre_20260929",
        "note": "Actor: Atlas Critical Minerals (U.S.-listed OTCQB/NASDAQ explorer) — us. Value is SGS-recommended exploration program USD 2.145m (not construction CAPEX). Distinct from graphcoa_jordania_mg and south_star_santa_cruz_graphite_2024.",
    },
    {
        "id": "atlas_malacacheta_graphite_mre_2026",
        "retrieved": "2026-10-01",
        "source_id": "atlas_malacacheta_mre_20260929",
        "url": "https://en.acnnewswire.com/press-release/english/110465/atlas-critical-minerals-defines-south-america's-largest,-highest-grade-reported-graphite-resource-24.2-million-tonnes,-including-17.2-million-tonnes-",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "17.2 Mt Indicated at 5.73% Cg and 7.0 Mt Inferred at 5.40% Cg, for approximately 1.36 million tonnes of contained in-situ graphite … Preliminary Economic Assessment (\"PEA\") targeted for Q2 2027.",
        "note": "Opened Atlas newswire release 29 Sep 2026. Exploration budget from SGS SK-1300 TRS 31 Jul 2025 on company site.",
    },
    {
        "id": "atlas_malacacheta_mre_20260929",
        "type": "company",
        "chicago": "Atlas Critical Minerals Corporation. “Atlas Critical Minerals Defines South America’s Largest, Highest Grade Reported Graphite Resource …” 29 September 2026.",
        "url": "https://en.acnnewswire.com/press-release/english/110465/atlas-critical-minerals-defines-south-america's-largest,-highest-grade-reported-graphite-resource-24.2-million-tonnes,-including-17.2-million-tonnes-",
        "annotation": "Company newswire on Malacacheta maiden MRE and PEA path. Supports atlas_malacacheta_graphite_mre_2026.",
        "supports": ["atlas_malacacheta_graphite_mre_2026", "hunt_res_graphite"],
    },
)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    updated = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
            updated.append(rid)
        else:
            rows.append({k: row.get(k, "") for k in FIELDS})
            by_id[rid] = len(rows) - 1
            added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
            if bib_entry.get("supports"):
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(bib_entry["supports"])
                )
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    # Keep Jervois company PDF as corroborating bib
    jervois_pdf = {
        "id": "jervois_smp_fid_20251125",
        "type": "company",
        "chicago": "Jervois. “São Miguel Paulista Restart Project Investment Approval.” 25 November 2025.",
        "url": "https://jervoisglobal.com/wp-content/uploads/2025/12/SMP-investment-decision-External-vf_.pdf",
        "annotation": "Company FID PDF for SMP restart scope/timing (no CAPEX USD). Corroborates jervois_smp_restart_2025.",
        "supports": ["jervois_smp_restart_2025", "hunt_res_nickel"],
    }
    if jervois_pdf["id"] not in bib_by:
        bib.append(jervois_pdf)
    else:
        existing = bib[bib_by[jervois_pdf["id"]]]
        existing["supports"] = sorted(
            set(existing.get("supports") or []) | set(jervois_pdf["supports"])
        )

    hunt_updates = {
        "hunt_res_balsa": "Cycle 33: equal budget; WITS/AIMA already (miss).",
        "hunt_res_water": "Cycle 33: equal budget; Almar Centinela / Acciona Yanacocha already (miss).",
        "hunt_infra_port_ownership": "Cycle 33: equal budget; DP World San Antonio/Callao still proposals (miss).",
        "hunt_infra_bridges_roads": "Cycle 33: logged erg_estanquillo_popayan_2026; upgraded crbc_arequipa_la_joya_2026 to MTC primary.",
        "hunt_energy_solar": "Cycle 33: logged aldesa_mexico_solar_hybrid_2026 (proxy EUR).",
        "hunt_latam_rail_telecom": "Cycle 33: equal budget; OHLA L9 / Siemens–Sonda already (miss).",
        "hunt_res_nickel": "Cycle 33: refreshed jervois_smp_restart_2025 with UNVERIFIED proxy USD 130m.",
        "hunt_infra_engineering_epc": "Cycle 33: equal budget; Ausenco SMP / PowerChina already (miss).",
        "hunt_energy_fission_smr": "Cycle 33: equal budget; Rosatom Brazil SMR still talk-only (miss).",
        "hunt_br_power_equip": "Cycle 33: equal budget; avoid over-invest (miss).",
        "hunt_fenb_araxa": "Cycle 33: equal budget; CBMM already (miss).",
        "hunt_energy_wind": "Cycle 33: equal budget; prior Goldwind/Envision/IFC already (miss).",
        "hunt_energy_other_renewables": "Cycle 33: equal budget; Lindsayca/Ormat already (miss).",
        "hunt_infra_port_cranes": "Cycle 33: logged portonave_electric_fleet_61m_2026.",
        "hunt_res_lithium": "Cycle 33: equal budget; Fénix 1B / Albemarle already (miss).",
        "hunt_infra_building_materials": "Cycle 33: equal budget; CALCEM logged C32 (miss).",
        "hunt_res_copper": "Cycle 33: equal budget; Centinela / El Abra / Escondida already (miss).",
        "hunt_res_graphite": "Cycle 33: logged atlas_malacacheta_graphite_mre_2026.",
    }
    for hid, note in hunt_updates.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 33 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 33 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
