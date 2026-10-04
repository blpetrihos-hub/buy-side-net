#!/usr/bin/env python3
"""Cycle 191 hunt: shuffle_seed=20261191; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md codebook order + Random(20261191)):
copper, building_materials, port_cranes, solar, power_plants_grid, port_ownership,
bridges_roads, water, fission_smr, lithium, nickel, wind, rail, other_renewables,
niobium, balsa, graphite, engineering_epc.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
    1 fission_smr row (Finep/Diamante MRN R$50m); balsa/nickel dry.
≥1/3 U.S. hunt budget spent on Freeport/EXIM/DFC/USTDA/NADBank/AES/Atlas/
Fluor/Bechtel/Progress/Wabtec — 1 new U.S. row (El Abra Sulfolix USD 741m).
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


# 1. copper / us — Freeport El Abra Sulfolix leach-pad modification USD 741m
row_doc(
    "fcx_el_abra_sulfolix_741m_2025",
    "resources",
    "copper",
    "us",
    "Freeport-McMoRan / Minera El Abra — Sulfolix heap-leach pad modification",
    "Chile",
    "23 Sep 2025 La Tercera: COEVA Antofagasta approves (10–0) Minera El Abra (Freeport 51% / Codelco 49%) DIA Sulfolix — modify leach-pad design to optimize copper recovery; investment face = USD 741 million; construction ~2.5 years; peak workforce 632; does not change extraction/production/life parameters vs 2008 permit; Calama commune. Distinct from fcx_el_abra_mill_chile_2026 (USD 7.5bn Continuidad/mill submission).",
    "741000000",
    "2025-09-23",
    "2025",
    "-21.90",
    "-68.80",
    "Minera El Abra, Calama / El Loa, Antofagasta Region, Chile (COEVA / La Tercera geography; approximate El Abra pin).",
    "latercera_el_abra_sulfolix_20250923",
    "La mañana de este martes la Comisión de Evaluación Ambiental (Coeva) de la Región de Antofagasta aprobó por 10 votos a favor el proyecto Sulfolix de US$741 millones de Minera El Abra, cuyo objetivo principal es optimizar el ciclo de lixiviación de cobre.",
    "https://www.latercera.com/pulso/noticia/freeport-mcmoran-obtiene-luz-verde-para-proyecto-de-lixiviacion-en-el-abra-de-us741-millones/",
    "Actor: Freeport-McMoRan (U.S.) via Minera El Abra — us; Codelco 49% partner. La Tercera Spanish press quoting Freeport Chile. CapEx = USD 741m. Shuffle copper; ≥1/3 U.S. hunt.",
    "hunt_cycle191",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="741000000",
    fx_usd="1",
    bib_type="company",
    chicago='Vera, Matías. “Freeport-McMoRan obtiene luz verde para proyecto de lixiviación en El Abra de US$741 millones.” La Tercera, September 23, 2025. https://www.latercera.com/pulso/noticia/freeport-mcmoran-obtiene-luz-verde-para-proyecto-de-lixiviacion-en-el-abra-de-us741-millones/.',
    annotation="La Tercera/COEVA: El Abra Sulfolix USD 741m. Supports fcx_el_abra_sulfolix_741m_2025.",
    evid_note="Opened La Tercera Spanish Pulso article 2026-10-04 quoting Freeport Chile country manager and Minera El Abra president.",
)

# 2. building_materials / allied — Holcim México ECOPact silos MXN 56m
row_doc(
    "holcim_mexico_ecopact_silos_56mdp_2025",
    "infrastructure",
    "building_materials",
    "allied",
    "Holcim México — ECOPact low-carbon concrete silo network (27 silos)",
    "Mexico",
    "25 Jun 2025 Holcim México: strategic investment of MXN 56 million to expand ECOPact low-carbon concrete production/distribution — install 27 silos totaling 2,600 tonnes sustainable cement storage capacity across national ready-mix plants. CapEx face = MXN 56,000,000 (MXN stored without FX). Distinct from holcim_comosa_mexico_2025 acquisition.",
    "56000000",
    "2025-06-25",
    "2025",
    "",
    "",
    "Holcim México national ready-mix plant network (company release; multi-site — lat/lon blank).",
    "holcim_mexico_ecopact_56mdp_20250625",
    "Holcim México … anunció una inversión estratégica de 56 millones de pesos para expandir significativamente su capacidad de producción y distribución de ECOPact … instalación de 27 silos, con una capacidad para almacenar 2,600 toneladas",
    "https://www.holcim.com.mx/holcim-mexico-impulsa-la-construccion-sostenible-con-inversion-de-56-millones-en-infraestructura",
    "Actor: Holcim México (Switzerland Holcim) — allied. Company Spanish press. CapEx = MXN 56m. Shuffle building_materials.",
    "hunt_cycle191",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="MXN",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Holcim México. “Holcim México impulsa la construcción sostenible con inversión de 56 millones en infraestructura para su concreto bajo en carbono.” June 25, 2025. https://www.holcim.com.mx/holcim-mexico-impulsa-la-construccion-sostenible-con-inversion-de-56-millones-en-infraestructura.',
    annotation="Holcim México: ECOPact silos MXN 56m. Supports holcim_mexico_ecopact_silos_56mdp_2025.",
    evid_note="Opened Holcim México Spanish company press 2026-10-04.",
)

# 3. port_cranes / allied — Hutchison Ports TIMSA e-RTG Manzanillo MXN 70m+
row_doc(
    "timsa_ertg_manzanillo_70m_mxn_2026",
    "infrastructure",
    "port_cranes",
    "allied",
    "Hutchison Ports TIMSA — two e-RTG electric yard cranes (Manzanillo)",
    "Mexico",
    "1 Jul 2026 T21 / Hutchison Ports TIMSA: investment exceeding MXN 70 million for two new electric Rubber Tyred Gantry (e-RTG) cranes for yard operations at Manzanillo terminal; units arrived 29 Jun 2026 aboard Xiang He Kou from China; 45-tonne lift each; 100% electric. CapEx face = MXN 70,000,000 floor (MXN stored without FX).",
    "70000000",
    "2026-07-01",
    "2026",
    "19.06",
    "-104.32",
    "Hutchison Ports TIMSA terminal, Puerto de Manzanillo, Colima, Mexico (ASIPONA Manzanillo geography; approximate port pin).",
    "t21_timsa_ertg_manzanillo_20260701",
    "Hutchison Ports TIMSA anunció una inversión superior a 70 millones de pesos para incorporar dos nuevas grúas eléctricas tipo Rubber Tyred Gantry Crane (e-RTG) … arribaron al puerto el pasado 29 de junio a bordo del buque Xiang He Kou, procedente de China",
    "https://t21.com.mx/hutchison-ports-timsa-suma-dos-nuevas-gruas-electricas-en-manzanillo/",
    "Actor: Hutchison Ports TIMSA (CK Hutchison / HK) — allied. Spanish trade press quoting TIMSA GM. CapEx = MXN 70m+. Shuffle port_cranes.",
    "hunt_cycle191",
    investment_type="equipment_procurement",
    evidence="documented",
    currency="MXN",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='T21. “Hutchison Ports TIMSA suma dos nuevas grúas eléctricas en Manzanillo.” July 1, 2026. https://t21.com.mx/hutchison-ports-timsa-suma-dos-nuevas-gruas-electricas-en-manzanillo/.',
    annotation="TIMSA: Manzanillo e-RTG MXN 70m+. Supports timsa_ertg_manzanillo_70m_mxn_2026.",
    evid_note="Opened T21 Spanish trade page quoting Hutchison Ports TIMSA GM 2026-10-04; Heraldo/DataPortuaria corroborate.",
)

# 4. power_plants_grid / allied — ENGIE Brasil Jaguara expansion R$1.2bn
row_doc(
    "engie_jaguara_expansion_1p2bn_brl_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "ENGIE Brasil Energia — UHE Jaguara capacity expansion (+232 MW)",
    "Brazil",
    "27 Jul 2026 Valor (WEG CVM-linked award): WEG contracted by ENGIE Brasil Energia to supply two generating units for Jaguara HPP expansion on Rio Grande (Rifaina SP / Sacramento MG) — total project investment R$ 1.2 billion to add 232 MW via two 116 MW units in existing shafts; new turbines targeted COD 2030. CapEx = R$1,200,000,000 (BRL stored without FX). Distinct from R$500m modernization program noted in ENGIE LRCAP release.",
    "1200000000",
    "2026-07-27",
    "2026",
    "-20.02",
    "-47.28",
    "UHE Jaguara, Rifaina (SP) / Sacramento (MG) on Rio Grande, Brazil (Valor/ENGIE geography; approximate dam pin).",
    "valor_weg_jaguara_20260727",
    "O projeto prevê um investimento total de R$ 1,2 bilhão, que permitirá ampliar a capacidade instalada da usina em 232 megawatts (MW), por meio da instalação de duas novas unidades geradoras em poços já existentes, cada uma com 116 MW de potência.",
    "https://valor.globo.com/empresas/noticia/2026/07/27/weg-assina-contrato-de-r-12-bi-com-a-engie-brasil-para-expanso-na-usina-de-jaguara.ghtml",
    "Actor: ENGIE Brasil Energia (France ENGIE) — allied; WEG equipment supplier (other). Valor Portuguese. CapEx = R$1.2bn. Shuffle power_plants_grid.",
    "hunt_cycle191",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Laurence, Felipe. “WEG assina contrato de R$ 1,2 bi com a Engie Brasil para expansão na usina de Jaguara.” Valor Econômico, July 27, 2026. https://valor.globo.com/empresas/noticia/2026/07/27/weg-assina-contrato-de-r-12-bi-com-a-engie-brasil-para-expanso-na-usina-de-jaguara.ghtml.',
    annotation="Valor/WEG: Jaguara expansion R$1.2bn. Supports engie_jaguara_expansion_1p2bn_brl_2026.",
    evid_note="Opened Valor Econômico Portuguese article 2026-10-04; ENGIE LRCAP English press corroborates auction/CapEx.",
)

# 5. power_plants_grid / allied — ENGIE Brasil Jaguara modernization R$500m
row_doc(
    "engie_jaguara_modernization_500m_brl_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "ENGIE Brasil Energia — UHE Jaguara modernization (4 units / 424 MW)",
    "Brazil",
    "18 Mar 2026 ENGIE Brasil LRCAP release: Jaguara modernization began Jul 2023 with investment of R$ 500 million, of which R$ 130 million already expended — maintain capacity of four generating units totaling 424 MW; first-unit modernization due 2Q26; completion targeted 2029. CapEx face = R$500,000,000 (BRL stored without FX). Distinct from R$1.2bn +232 MW expansion.",
    "500000000",
    "2026-03-18",
    "2026",
    "-20.02",
    "-47.28",
    "UHE Jaguara, Rifaina (SP) / Sacramento (MG) on Rio Grande, Brazil (ENGIE geography; approximate dam pin).",
    "engie_brasil_jaguara_lrcap_20260318",
    "Work on the modernization of the hydropower plant began in July 2023 and involves an investment of R$ 500 million, of which R$ 130 million has already been expended.",
    "https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-vence-leilao-de-reserva-de-capacidade-e-vai-ampliar-potencia-da-usina-hidreletrica-jaguara/",
    "Actor: ENGIE Brasil Energia (France ENGIE) — allied. Company English press. CapEx = R$500m modernization. Shuffle power_plants_grid.",
    "hunt_cycle191",
    investment_type="brownfield_modernization",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil wins the Capacity Reserve Auction and will increase the power output of the Jaguara Hydropower Plant.” March 18, 2026. https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-vence-leilao-de-reserva-de-capacidade-e-vai-ampliar-potencia-da-usina-hidreletrica-jaguara/.',
    annotation="ENGIE: Jaguara modernization R$500m. Supports engie_jaguara_modernization_500m_brl_2026.",
    evid_note="Opened ENGIE Brasil English press via browser fetch 2026-10-04 (modernization paragraph); curl bots may 403.",
)

# 6. fission_smr / other — Finep/Diamante Brazilian microreactor tech R$50m (thin top-up)
row_doc(
    "finep_diamante_mrn_50m_brl_2025",
    "energy",
    "fission_smr",
    "other",
    "Finep / Diamante Geração / INB / Terminus — Brazilian microreactor technology project",
    "Brazil",
    "17 Jun 2025 MCTI/Finep: sign contract-project for development and testing of critical technologies for Brazilian Nuclear Microreactors (MRN) — total investment R$ 50 million (Finep economic grant R$ 30m from FNDCT + R$ 20m company counterpart); led by Diamante Geração de Energia with co-executors INB and Terminus; nine ICTs including AMAZUL/IPEN/IEN. CapEx/program face = R$50,000,000 (BRL stored without FX). Distinct from diamante_jorge_lacerda_smr_loi_2026 (C2N LOI).",
    "50000000",
    "2025-06-17",
    "2025",
    "",
    "",
    "Brazilian MRN R&D consortium (MCTI/Finep; multi-institution — lat/lon blank).",
    "mcti_finep_mrn_20250617",
    "O projeto representa um investimento total de R$ 50 milhões, sendo R$ 30 milhões em subvenção econômica e R$ 20 milhões de contrapartida das empresas participantes.",
    "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2025/06/mcti-e-finep-investem-r-30-milhoes-para-projeto-de-microrreator-nuclear",
    "Actor: Diamante/INB/Terminus (Brazilian) with Finep/MCTI — other. Official MCTI Portuguese release. CapEx = R$50m program. Thin fission_smr top-up.",
    "hunt_cycle191",
    investment_type="rd_pilot",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Ministério da Ciência, Tecnologia e Inovação (MCTI). “MCTI e FINEP investem R$ 30 milhões para projeto de microrreator nuclear.” June 17, 2025. https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2025/06/mcti-e-finep-investem-r-30-milhoes-para-projeto-de-microrreator-nuclear.',
    annotation="MCTI/Finep: MRN R$50m. Supports finep_diamante_mrn_50m_brl_2025.",
    evid_note="Opened MCTI Portuguese government release 2026-10-04; Finep/CNEN corroborate.",
)

# 7. wind / allied — ENGIE Chile Pemuco/Chequenes 165 MW USD 228m
row_doc(
    "engie_pemuco_chequenes_228m_2025",
    "energy",
    "wind",
    "allied",
    "ENGIE Chile — Parque Eólico Pemuco / Chequenes (165 MW, Ñuble)",
    "Chile",
    "26 Feb 2025 ENGIE Chile: groundbreaking for Parque Eólico Pemuco (later Chequenes) in Pemuco commune, Ñuble — 22 × 7.5 MW turbines; 165 MW installed; investment USD 228 million; connect to Transelec Entre Ríos substation; COD targeted ~1H 2027. CapEx = USD 228m. Distinct from goldwind_pemuco_chile (turbine OEM supply, CapEx blank) and goldwind_kallpa_chile_342mw_2026.",
    "228000000",
    "2025-02-26",
    "2025",
    "-36.98",
    "-72.00",
    "Parque Eólico Pemuco/Chequenes, Pemuco commune (~47 km south of Chillán), Ñuble Region, Chile (ENGIE geography; approximate pin).",
    "engie_chile_pemuco_20250226",
    "el proyecto -que contempla una inversión de US$ 228 millones- contará con 22 aerogeneradores de 7,5 MW de potencia nominal, lo que se traduce en una capacidad instalada de 165 MW",
    "https://www.engie.cl/comenzamos-la-construccion-del-primer-parque-eolico-de-la-region-de-nuble/",
    "Actor: ENGIE Chile (France ENGIE) — allied. Company Spanish groundbreaking. CapEx = USD 228m. Shuffle wind.",
    "hunt_cycle191",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="228000000",
    fx_usd="1",
    bib_type="company",
    chicago='ENGIE Chile. “Comenzamos la construcción del primer parque eólico de la región de Ñuble.” February 26, 2025. https://www.engie.cl/comenzamos-la-construccion-del-primer-parque-eolico-de-la-region-de-nuble/.',
    annotation="ENGIE Chile: Pemuco/Chequenes USD 228m. Supports engie_pemuco_chequenes_228m_2025.",
    evid_note="Opened ENGIE Chile Spanish groundbreaking 2026-10-04; Energía Ministry later cites same USD 228m under Chequenes name.",
)

# 8. wind / allied — ENGIE Chile Pampa Fidelia 306 MW USD 461m
row_doc(
    "engie_pampa_fidelia_461m_2025",
    "energy",
    "wind",
    "allied",
    "ENGIE Chile — Parque Eólico Pampa Fidelia (306 MW, Taltal)",
    "Chile",
    "23 Jul 2025 ENGIE Chile announces construction start of Parque Eólico Pampa Fidelia in Taltal wind reserve, Antofagasta — 51 turbines; 306 MW to SEN; COD targeted 1H 2027. CapEx = USD 461 million per ENGIE Chile investor presentation (306 MW Wind Pampa Fidelia US$461 million CAPEX). Distinct from engie_pemuco_chequenes_228m_2025 and engie BESS rows.",
    "461000000",
    "2025-07-23",
    "2025",
    "-25.40",
    "-70.48",
    "Parque Eólico Pampa Fidelia, Reserva Eólica de Taltal, Antofagasta Region, Chile (ENGIE geography; approximate Taltal pin).",
    "engie_chile_ir_pampa_fidelia_capex",
    "306MW Wind Pampa Fidelia US$461 million CAPEX",
    "https://www.engie.cl/wp-content/uploads/2024/10/9M2025-Presentation-ENGIE-CHILE-NEW-vF.pdf",
    "Actor: ENGIE Chile (France ENGIE) — allied. Company IR deck CapEx; construction start announced 23 Jul 2025 Spanish press (no $ on that page). CapEx = USD 461m. Shuffle wind.",
    "hunt_cycle191",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="461000000",
    fx_usd="1",
    bib_type="company",
    chicago='ENGIE Chile. “9M 2025 Results Presentation” (investor deck). 2025. https://www.engie.cl/wp-content/uploads/2024/10/9M2025-Presentation-ENGIE-CHILE-NEW-vF.pdf.',
    annotation="ENGIE IR: Pampa Fidelia USD 461m CapEx. Supports engie_pampa_fidelia_461m_2025.",
    evid_note="Opened ENGIE Chile 9M2025 IR PDF CapEx line 2026-10-04; construction-start Spanish press cross-checked for 51 turbines / 306 MW / COD 1H27.",
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
    added = []

    for row, evid, bib_e in ITEMS:
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
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle191 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
