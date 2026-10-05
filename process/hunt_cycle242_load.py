#!/usr/bin/env python3
"""Cycle 242 hunt: shuffle_seed=20261242; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261242).shuffle):
building_materials, niobium, solar, port_ownership, graphite, lithium,
power_plants_grid, engineering_epc, nickel, rail, other_renewables, water,
balsa, port_cranes, wind, copper, fission_smr, bridges_roads.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes Altos del Sol USD 1.375bn SEA CapEx;
  NEW AES Andes Llanos del Sol USD 635m SEA CapEx; honest residual.
PRC equal-budget: NEW Sungrow–Grupo Roca C&I BESS R$500m / 400 MWh.
Allied: NEW ISA Energia Brasil authorized R&M carteira ~R$7.2bn.
Skipped: Microsoft Chile USD 3.3bn IDC ecosystem (not company CapEx face);
  BYD Camaçari auto plant out of taxonomy / archived precedent; GATE R$18bn
  company vs R$23bn press (retain company); Dune Plus USD 629m Latham (allied
  owner CapEx — hold for next if needed); Goldwind Sento Sé CapEx undisclosed;
  COP/CLP/PEN; holdovers unsigned; thin balsa/nickel/fission dry.
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

BRL_USD = "5.1921"
BRL_FX_DATE = "2026-09-25"


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


# 1. other_renewables / us — NEW AES Andes Altos del Sol USD 1.375bn (PV+BESS SEA)
row_doc(
    "aes_andes_altos_del_sol_1375m_2024",
    "energy", "other_renewables", "us",
    "AES Andes — Parque Fotovoltaico Altos del Sol (Antofagasta PV + BESS)",
    "Chile",
    "Jul 2024 SEA DIA / Apr 2025 COEVA RCA (Electrominería citing AES Andes): Parque Fotovoltaico Altos del Sol — ~763.6 MW PV + ~1,063.4 MW / 5h BESS in Antofagasta commune (~177 km SE of Antofagasta city); estimated investment US$1.375 billion; LAT 2×220 kV to S/E Monte Mina. CapEx: enter USD 1.375bn face. Complements Solar Oriente (USD 990m) and Llanos del Sol within company US$3bn SEA package.",
    "1375000000", "2024-07-19", "2024", "-24.45", "-69.55",
    "Antofagasta commune, Antofagasta Region (~177 km SE of Antofagasta city; municipal pin).",
    "electromineria_aes_altos_del_sol_1375m_2025",
    "AES Andes obtuvo la aprobación ambiental del proyecto «Parque Fotovoltaico Altos del Sol», el cual considera una potencia instalada de 763,6 MW, con una capacidad de almacenamiento eléctrico en baterías BESS, de aproximadamente 1.063,4 MWh por 5 horas, bajo una inversión estimada de US$1.375 millones.",
    "https://electromineria.cl/aes-andes-obtiene-aprobacion-ambiental-de-mega-proyecto-solar-por-us1-375-millones-en-antofagasta/",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW row: Electrominería CapEx US$1.375bn (UNVERIFIED press citing SEA/COEVA; company AES Andes English confirms Altos del Sol in US$3bn three-project SEA package with Solar Oriente / Llanos del Sol). Distinct from aes_andes_solar_oriente_990m_2024. Shuffle other_renewables / U.S. ≥1/3 budget.",
    "hunt_cycle242", investment_type="greenfield_storage", evidence="press", currency="USD",
    value_usd="1375000000", fx_usd="1", bib_type="press",
    chicago='Electrominería. “AES Andes obtiene aprobación ambiental de mega proyecto solar por US$1.375 millones en Antofagasta.” 2025. https://electromineria.cl/aes-andes-obtiene-aprobacion-ambiental-de-mega-proyecto-solar-por-us1-375-millones-en-antofagasta/.',
    annotation="AES Altos del Sol NEW USD 1.375bn (press). Supports aes_andes_altos_del_sol_1375m_2024.",
    evid_note="Opened Electrominería Spanish; US$1.375bn / 763.6 MW PV / ~1,063.4 MW 5h BESS / Monte Mina LAT / Antofagasta RCA confirmed.",
)

# 2. other_renewables / us — NEW AES Andes Llanos del Sol USD 635m (PV+BESS SEA)
row_doc(
    "aes_andes_llanos_del_sol_635m_2024",
    "energy", "other_renewables", "us",
    "AES Andes — Parque Fotovoltaico Llanos del Sol (Pozo Almonte PV + BESS)",
    "Chile",
    "8 Jul 2024 Electrominería (citing AES Andes SEIA DIA): Parque Fotovoltaico Llanos del Sol — 381.8 MW PV + 531.5 MW / 5h BESS (2.66 GWh) on ~610 ha in Pozo Almonte, Tarapacá; investment US$635 million; 220 kV LAT ~12.2 km to existing S/E San Simón. CapEx: enter USD 635m face. Complements Solar Oriente / Altos del Sol in company US$3bn SEA package.",
    "635000000", "2024-07-08", "2024", "-20.26", "-69.79",
    "Pozo Almonte commune, Tarapacá Region (company geography; municipal pin).",
    "electromineria_aes_llanos_del_sol_635m_20240708",
    "AES Andes ingresó al Sistema de Evluación de Impacto Ambiental (SEIA) el proyecto “Parque Fotovoltaico Llanos del Sol”, el cual también contempla el uso de almacenamiento de energía, mediante baterías BESS, buscando emplazarse en una superficie aproximada de 610 hectáreas, en la comuna de Pozo Almonte, en la región de Tarapacá, considerando una inversión de US$635 millones.",
    "https://electromineria.cl/tarapaca-aes-andes-ingreso-proyecto-solar-con-almacenamiento-por-us635-millones/",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW row: Electrominería CapEx US$635m (UNVERIFIED press citing SEIA DIA; company AES Andes English confirms Llanos del Sol in US$3bn package). Distinct from Solar Oriente / Altos del Sol. Shuffle other_renewables / U.S. ≥1/3 budget.",
    "hunt_cycle242", investment_type="greenfield_storage", evidence="press", currency="USD",
    value_usd="635000000", fx_usd="1", bib_type="press",
    chicago='Electrominería. “Tarapacá: AES Andes ingresó proyecto solar con almacenamiento por US$635 millones.” July 8, 2024. https://electromineria.cl/tarapaca-aes-andes-ingreso-proyecto-solar-con-almacenamiento-por-us635-millones/.',
    annotation="AES Llanos del Sol NEW USD 635m (press). Supports aes_andes_llanos_del_sol_635m_2024.",
    evid_note="Opened Electrominería Spanish; US$635m / 381.8 MW PV / 531.5 MW 5h BESS / Pozo Almonte / San Simón LAT confirmed.",
)

# 3. other_renewables / prc — NEW Sungrow–Grupo Roca C&I BESS R$500m / 400 MWh
row_doc(
    "sungrow_roca_bess_400mwh_500m_brl_2025",
    "energy", "other_renewables", "prc",
    "Sungrow — Grupo Roca / MOBS / TCCOM C&I BESS supply (400 MWh / 3 years)",
    "Brazil",
    "11 Aug 2025 pv magazine Brasil: Sungrow signs BESS supply agreement with MOBS Armazenagem de Energia e Mobilidade and TCCOM Comercializadora de Energia (Grupo Roca) for 400 MWh of C&I storage over three years; expected investment R$ 500 million. CapEx: enter R$500m envelope (UNVERIFIED press; Brazil-wide C&I deployment — leave lat/lon empty).",
    "500000000", "2025-08-11", "2025", "", "",
    "Brazil-wide C&I BESS deployment (no single named site in source; lat/lon blank).",
    "pv_magazine_br_sungrow_roca_bess_20250811",
    "A chinesa Sungrow firmou um acordo de fornecimento de sistemas BESS (Battery Energy Storage System) com a MOBS Armazenagem de Energia e Mobilidade e a TCCOM Comercializadora de Energia, ambas pertencentes ao Grupo Roca para a implantação de 400 MWh em armazenamento de energia nos próximos três anos, voltados exclusivamente para o mercado comercial e industrial (C&I). A expectativa de investimento é de R$ 500 milhões",
    "https://www.pv-magazine-brasil.com/2025/08/11/sungrow-fornecera-400-mwh-em-solucoes-de-armazenamento-para-o-grupo-roca/",
    "Actor: Sungrow (PRC) — prc. NEW row: pv magazine Brasil CapEx R$500m / 400 MWh C&I BESS with Grupo Roca (UNVERIFIED press). Distinct from byd_brazil_bess_factory_500m_2026. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle242", investment_type="equipment_supply", evidence="press", currency="BRL",
    value_usd=str(round(500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Neris, Alessandra. “Sungrow fornecerá 400 MWh em soluções de armazenamento para o Grupo Roca.” pv magazine Brasil, August 11, 2025. https://www.pv-magazine-brasil.com/2025/08/11/sungrow-fornecera-400-mwh-em-solucoes-de-armazenamento-para-o-grupo-roca/.',
    annotation="Sungrow–Roca BESS NEW R$500m ~USD 96.30m via Fed H.10 (press). Supports sungrow_roca_bess_400mwh_500m_brl_2025.",
    evid_note="Opened pv magazine Brasil Portuguese; R$500m / 400 MWh / 3-year C&I / MOBS+TCCOM Grupo Roca confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW ISA Energia R&M authorized carteira ~R$7.2bn
row_doc(
    "isa_energia_rm_carteira_7p2bn_2026",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — authorized Reinforcements & Improvements (R&M) carteira",
    "Brazil",
    "3 Sep 2026 ISA Energia Brasil company: invested R$815.4 million in R&M in 1H2026 (+19% YoY); authorized R&M project carteira at end of 2Q totaled approximately R$7.2 billion to be executed in coming years (São Paulo concession-focused modernization). CapEx: enter R$7.2bn authorized carteira face. Distinct from isa_energia_rm_370m_brl_1t26 (Q1 spent) and isa_energia_fy2025_capex_5p1bn_brl (FY2025 executed).",
    "7200000000", "2026-09-03", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil São Paulo concession / multi-state transmission portfolio (São Paulo pin).",
    "isa_energia_rm_815m_carteira_7p2bn_20260903",
    "A carteira de projetos de Reforços e Melhorias autorizada ao fim do segundo trimestre totalizava aproximadamente R$ 7,2 bilhões que serão executados pela Companhia nos próximos anos.",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-8154-milhoes-na-modernizacao-da-rede-de-transmissao-no-1-semestre/",
    "Actor: ISA Energia Brasil (controlled by Colombian ISA / Interconexión Eléctrica) — allied. NEW row: company Portuguese authorized R&M carteira ~R$7.2bn. Nested vs Q1 R$370m spent / FY2025 R$5.1bn executed. Shuffle power_plants_grid.",
    "hunt_cycle242", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(7200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “ISA ENERGIA BRASIL investe R$ 815,4 milhões na modernização da rede de transmissão no 1º semestre.” September 3, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-8154-milhoes-na-modernizacao-da-rede-de-transmissao-no-1-semestre/.',
    annotation="ISA R&M carteira NEW R$7.2bn ~USD 1386.72m via Fed H.10. Supports isa_energia_rm_carteira_7p2bn_2026.",
    evid_note="Opened ISA Energia Brasil Portuguese; ~R$7.2bn authorized R&M carteira / R$815.4m 1H2026 / 2Q R$445.4m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle242 added {len(added)}: {added}")
    print(f"cycle242 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
