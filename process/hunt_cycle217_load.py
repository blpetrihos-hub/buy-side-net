#!/usr/bin/env python3
"""Cycle 217 hunt: shuffle_seed=20261217; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261217).shuffle):
copper, wind, port_cranes, bridges_roads, power_plants_grid, lithium, balsa,
nickel, engineering_epc, fission_smr, other_renewables, niobium,
building_materials, port_ownership, solar, water, graphite, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry this cycle; next-thinnest niobium CapEx-fill (Boston Metal R$1bn → USD).
≥1/3 U.S. hunt budget spent on Wabtec Vale PTC CapEx-fill + Boston Metal
niobium CapEx-fill + Freeport El Abra / EnergyX / EXIM / Bechtel EIMISA /
Fluor Quellaveco / Wabtec MRS / Nextracker / Array Lupi / USTDA / Equinix /
SSA Marine / Jervois SMP sweeps (2 US CapEx-fills; catalog dense otherwise).
PRC equal-budget: Sungrow×BHP Escondida/Spence solar+BESS (new); Goldwind /
PowerChina / CAMCE / ZPMC / CCCC holdovers already logged or unsigned.
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

# Fed H.10 weekly release 2026-09-28; Brazil Real Sep 25 = 5.1921 BRL/USD
BRL_USD = "5.1921"
BRL_FX_DATE = "2026-09-25"


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


# 1. solar / prc — Sungrow × BHP Escondida + Spence onsite solar + BESS (CapEx blank)
row_doc(
    "sungrow_bhp_escondida_spence_solar_bess_2026",
    "energy",
    "solar",
    "prc",
    "Sungrow — onsite solar + BESS for BHP Escondida and Spence (Chile)",
    "Chile",
    "1 Jun 2026 International Mining (BHP): long-term agreements with Sungrow to develop onsite renewable self-supply at Escondida and Spence — Escondida 110 MW solar + 110 MW/540 MWh BESS; Spence 85 MW solar + 85 MW/420 MWh BESS (combined 195 MW solar / 960 MWh storage); integrated at point of consumption; operational from FY2029; supports maintaining 100% renewable electricity as copper production demand grows. CapEx USD not disclosed. Distinct from sungrow_zelestra_aurora / Librillo / Observatorio Chile BESS rows and bhp_escondida_new_concentrator_2026.",
    "",
    "",
    "2026",
    "-24.27",
    "-69.07",
    "Escondida / Spence copper operations, Antofagasta Region, Chile (BHP geography; Escondida pin; Spence co-located in region).",
    "immining_bhp_sungrow_escondida_spence_20260601",
    "BHP has signed long-term agreements with Sungrow, a global renewable energy technology provider, to develop renewable energy projects at its Escondida and Spence operations in Chile. … Together, the projects aim to develop 110 MW of solar capacity and 110 MW/540 MWh of battery storage at Escondida, and 85 MW of solar capacity and 85 MW/420 MWh of storage at Spence.",
    "https://im-mining.com/2026/06/01/bhp-advances-renewable-power-supply-and-storage-at-escondida-spence/",
    "Actor: Sungrow (PRC) technology provider — prc; offtaker/host BHP (allied miner) at Escondida/Spence. Trade press paraphrasing BHP; Diario Minero Spanish corroborates same MW/MWh split. CapEx blank (undisclosed). Shuffle solar.",
    "hunt_cycle217",
    investment_type="equipment_supply",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='International Mining. “BHP advances renewable power supply and storage at Escondida & Spence.” June 1, 2026. https://im-mining.com/2026/06/01/bhp-advances-renewable-power-supply-and-storage-at-escondida-spence/.',
    annotation="BHP–Sungrow Escondida/Spence 195 MW solar + 960 MWh BESS. Supports sungrow_bhp_escondida_spence_solar_bess_2026.",
    evid_note="Opened IM-Mining 2026-10-04; 110 MW+540 MWh Escondida / 85 MW+420 MWh Spence / FY2029 / Sungrow LTA confirmed. CapEx undisclosed.",
)

# 2. port_cranes / other — Hutchison Ports TIMSA two ESP.10 MHC >MXN 300m (Manzanillo)
row_doc(
    "timsa_mhc_esp10_manzanillo_300m_mxn_2026",
    "infrastructure",
    "port_cranes",
    "other",
    "Hutchison Ports TIMSA — two Gottwald ESP.10 electric MHC (Manzanillo)",
    "Mexico",
    "28 Apr 2026 Cluster Industrial / Hutchison Ports TIMSA: investment exceeding MXN 300 million for two electric MHC ESP.10 units at Manzanillo terminal; arrived 15 Apr 2026 aboard BBC Aquamarine from Terneuzen, Netherlands; ~100 t lift / 22-row outreach for Super Post-Panamax up to ~15,500 TEU; brings TIMSA MHC fleet to eight units. CapEx floor = MXN 300,000,000 (MXN stored without FX). Distinct from timsa_ertg_manzanillo_70m_mxn_2026 (e-RTG yard cranes) and konecranes_arica_mhc_2026.",
    "300000000",
    "",
    "2026",
    "19.06",
    "-104.32",
    "Hutchison Ports TIMSA terminal, Puerto de Manzanillo, Colima, Mexico (ASIPONA Manzanillo geography; approximate port pin).",
    "cluster_timsa_mhc_esp10_20260428",
    "Hutchison Ports TIMSA fortaleció su infraestructura operativa con la incorporación de dos grúas eléctricas tipo MHC ESP.10 … La llegada de estas unidades representó una inversión superior a 300 millones de pesos y se concretó el 15 de abril de 2026 con el arribo del buque BBC Aquamarine, procedente de Terneuzen, Países Bajos.",
    "https://clusterindustrial.com.mx/hutchison-ports-timsa-invierte-300-mdp-en-gruas-electricas-para-elevar-capacidad-en-manzanillo/",
    "Actor: Hutchison Ports TIMSA (CK Hutchison / Hong Kong) — other. Spanish trade press quoting TIMSA GM. CapEx = MXN 300m+ floor. OEM Gottwald/Konecranes cited in corroborating WorldCargo News. Shuffle port_cranes.",
    "hunt_cycle217",
    investment_type="equipment_procurement",
    evidence="documented",
    currency="MXN",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='Cluster Industrial. “Hutchison Ports TIMSA invierte 300 MDP en grúas eléctricas para elevar capacidad en Manzanillo.” April 28, 2026. https://clusterindustrial.com.mx/hutchison-ports-timsa-invierte-300-mdp-en-gruas-electricas-para-elevar-capacidad-en-manzanillo/.',
    annotation="TIMSA Manzanillo ESP.10 MHC >MXN 300m. Supports timsa_mhc_esp10_manzanillo_300m_mxn_2026.",
    evid_note="Opened Cluster Industrial 2026-10-04; >MXN 300m / two MHC ESP.10 / 15 Apr 2026 BBC Aquamarine / 100 t / 22 rows / fleet to eight units confirmed.",
)

# 3. rail / us — CapEx-fill Wabtec Vale PTC R$1bn → USD via Fed H.10
row_doc(
    "wabtec_vale_ptc_brl1bn_2026",
    "infrastructure",
    "rail",
    "us",
    "Wabtec — I-ETMS Positive Train Control for Vale EFC + EFVM (Brazil)",
    "Brazil",
    "Wabtec company release: Vale agreement to implement Wabtec I-ETMS Positive Train Control on Carajás Railway (EFC) and Vitória a Minas Railway (EFVM); real-time monitoring with automatic intervention; project investment approximately BRL 1 billion, phased through 2031; integrates onboard systems with existing infrastructure. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~192.60m for stored R$1bn face. Distinct from wabtec_vale_50_locos_2026 locomotive purchase and prior EFC MSA rows.",
    "1000000000",
    BRL_FX_DATE,
    "2026",
    "-6.07",
    "-49.90",
    "Carajás Railway (EFC) / southeastern Pará corridor (company geography; approximate ops pin).",
    "wabtec_vale_ptc_2026",
    "The project, which represents an investment of approximately BRL 1 billion, will be implemented in phases through 2031 … The technology to be implemented is Wabtec’s I-ETMS (Interoperable Electronic Train Management System)",
    "https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-agreement-to-enhance-operational-safety-on-the-efc-and-efvm-railways-with-advanced-railway",
    "Actor: Wabtec Corporation (U.S./Pittsburgh) — us; operator Vale (Brazil). Company primary. CapEx-fill: retain R$1bn; add Fed H.10 Sep 25 2026 FX to USD ~192.60m. ≥1/3 U.S. hunt budget / shuffle rail.",
    "hunt_cycle217",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(1000000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="company",
    chicago='Wabtec Corporation. “Vale and Wabtec Sign Agreement to Enhance Operational Safety on the EFC and EFVM Railways with Advanced Railway Signaling Technology.” 2026. https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-agreement-to-enhance-operational-safety-on-the-efc-and-efvm-railways-with-advanced-railway.',
    annotation="Wabtec Vale PTC CapEx-fill ~USD 192.60m via Fed H.10. Supports wabtec_vale_ptc_brl1bn_2026.",
    evid_note="Opened Wabtec company press; ~BRL 1bn / I-ETMS / EFC+EFVM / through 2031 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. niobium / us — CapEx-fill Boston Metal Coronel Xavier R$1bn → USD (thin top-up next-thinnest)
row_doc(
    "boston_metal_coronel_xavier_plant_2025",
    "resources",
    "niobium",
    "us",
    "Boston Metal do Brasil — Coronel Xavier Chaves MOE critical-metals plant",
    "Brazil",
    "Apr 2025 (Diário do Comércio) / May 2026 (MIT Technology Review): Boston Metal (U.S.) subsidiary Boston Metal do Brasil advances first commercial molten-oxide electrolysis (MOE) plant at Coronel Xavier Chaves (near São João del-Rei, Minas Gerais) to produce niobium, tantalum and tin ferroalloys from mining/metallurgical residues; press cites R$ 1 billion investment through 2026 and ~12,000 tpy product capacity across five electrolytic cells; MIT TR confirms Brazil commercial facility and Sep 2026 restart target after Jan 2026 refractory leak. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~192.60m for stored R$1bn face (UNVERIFIED proxy CapEx retained). Distinct from St George–Boston Metal Araxá MOE trial MoU (feedstock MoU only).",
    "1000000000",
    BRL_FX_DATE,
    "2025",
    "-21.02",
    "-44.22",
    "Coronel Xavier Chaves, Minas Gerais (Diário do Comércio / Boston Metal geography).",
    "diario_comercio_boston_metal_20250406",
    "A Boston Metal do Brasil irá iniciar no próximo mês a produção em escala industrial na unidade em Coronel Xavier Chaves, município próximo de São João del-Rei, no Campo das Vertentes. Com investimentos de R$ 1 bilhão até 2026, o espaço vai abrigar o primeiro hub de metais estratégicos do mundo produzidos a partir da tecnologia de Eletrólise de Óxido Fundido (MOE).",
    "https://diariodocomercio.com.br/economia/boston-metal-inicia-producao-escala-industrial-minas-gerais/",
    "Actor: Boston Metal (U.S.) via Boston Metal do Brasil — us. UNVERIFIED proxy CapEx R$1bn retained; CapEx-fill adds Fed H.10 Sep 25 2026 FX to USD ~192.60m. Thin niobium top-up (balsa/nickel/fission_smr dry) / ≥1/3 U.S. hunt.",
    "hunt_cycle217",
    investment_type="greenfield_plant",
    evidence="proxy",
    currency="BRL",
    value_usd=str(round(1000000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="press",
    chicago='Diário do Comércio. “Boston Metal vai investir R$ 1 bilhão até 2026 na planta de Coronel Xavier Chaves.” April 6, 2025. https://diariodocomercio.com.br/economia/boston-metal-inicia-producao-escala-industrial-minas-gerais/.',
    annotation="Boston Metal Coronel Xavier CapEx-fill ~USD 192.60m via Fed H.10. Supports boston_metal_coronel_xavier_plant_2025.",
    evid_note="Opened Diário do Comércio; R$1bn through 2026 / Coronel Xavier Chaves / Nb-Ta-Sn MOE / 12 ktpy confirmed (UNVERIFIED proxy CapEx). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    updated = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k == "id":
                    continue
                if v != "" and v is not None:
                    existing[k] = v
            updated.append(rid)
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
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle217 added {len(added)}: {added}")
    print(f"cycle217 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
