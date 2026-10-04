#!/usr/bin/env python3
"""Cycle 216 hunt: shuffle_seed=20261216; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261216).shuffle):
engineering_epc, port_cranes, power_plants_grid, bridges_roads, wind, balsa,
port_ownership, building_materials, other_renewables, niobium, copper, graphite,
fission_smr, nickel, water, lithium, solar, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
nickel CapEx-fill (Atlantic UG USD); balsa/fission_smr dry.
≥1/3 U.S. hunt budget spent on GE Vernova São Simão CapEx-fill + Freeport El Abra/
EnergyX/EXIM/Bechtel EIMISA/Fluor Quellaveco/Wabtec/Nextracker/Array Lupi/
USTDA/Equinix/SSA Marine sweeps (1 US CapEx-fill; catalog dense otherwise).
PRC equal-budget: Goldwind Sento Sé / PowerChina Conchagua / CAMCE Bluefields /
ZPMC / CCCC El Barro already logged; holdovers unsigned.
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


# 1. engineering_epc / allied — Siemens Energy × Seatrium P-84/P-85 electric compression R$2bn
row_doc(
    "siemens_energy_seatrium_p84_p85_2bn_2025",
    "infrastructure",
    "engineering_epc",
    "allied",
    "Siemens Energy — electric compression packages for Petrobras FPSO P-84 / P-85 (Seatrium)",
    "Brazil",
    "7 Jul 2025 Folha/Reuters (Siemens Energy to Reuters) + Valor International: Siemens Energy signs ~R$ 2 billion contract with Seatrium to supply electric motor-driven compression systems for Petrobras FPSOs P-84 (Atapu) and P-85 (Sépia), Santos Basin pre-salt; 12 electric compression systems per FPSO (main gas / export / injection / CO₂); compressors built in Germany with Santa Bárbara d’Oeste (SP) piping/spools/auxiliaries; deliveries 2026 (P-84) and 2027 (P-85); platforms targeted COD 2029–2030. Distinct from siemens_energy_petrobras_fpso_p81_p87_2026 (SBM SEAP, no USD/BRL disclosed).",
    "2000000000",
    BRL_FX_DATE,
    "2025",
    "-23.96",
    "-42.50",
    "Atapu / Sépia FPSO topside packages for Santos Basin pre-salt, offshore Brazil (project geography; basin pin).",
    "folha_siemens_seatrium_p84_p85_20250707",
    "A Siemens Energy assinou um contrato para fornecer uma solução de eficiência energética para dois novos navios-plataforma (FPSO) que serão construídos pela Seatrium para a Petrobras, afirmou a empresa alemã à Reuters. O acordo é avaliado em cerca de R$ 2 bilhões e envolve o fornecimento de sistemas de compressão acionados por motor elétrico para as plataformas P-84 e P-85.",
    "https://www1.folha.uol.com.br/mercado/2025/07/siemens-energy-e-seatrium-fecham-acordo-de-r-2-bi-para-plataformas-para-a-petrobras.shtml",
    "Actor: Siemens Energy (Germany) — allied; EPC buyer Seatrium (Singapore) for Petrobras-owned FPSOs. UNVERIFIED proxy: Folha/Reuters citing Siemens Energy on ~R$2bn package value (company English P-81/P-87 release has no USD/BRL). Value stored as BRL; Fed H.10 Sep 25 2026 (5.1921) → USD ~385.2m. Shuffle engineering_epc.",
    "hunt_cycle216",
    investment_type="equipment_supply",
    evidence="proxy",
    currency="BRL",
    value_usd=str(round(2000000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="press",
    chicago='Folha de S.Paulo / Reuters. “Siemens Energy e Seatrium fecham acordo de R$ 2 bi para plataformas para a Petrobras.” July 7, 2025. https://www1.folha.uol.com.br/mercado/2025/07/siemens-energy-e-seatrium-fecham-acordo-de-r-2-bi-para-plataformas-para-a-petrobras.shtml.',
    annotation="Siemens Energy Seatrium P-84/P-85 ~R$2bn electric compression. Supports siemens_energy_seatrium_p84_p85_2bn_2025.",
    evid_note="Opened Folha 2026-10-04; ~R$2bn / P-84 Atapu / P-85 Sépia / Seatrium / electric compression / Santa Bárbara d’Oeste confirmed. UNVERIFIED proxy value (Siemens to Reuters). FX Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. nickel / allied — CapEx-fill Atlantic Nickel Santa Rita UG USD from BNamericas
row_doc(
    "atlantic_nickel_ug_capex_2026",
    "resources",
    "nickel",
    "allied",
    "Atlantic Nickel / Appian — Santa Rita underground expansion CapEx (Bahia)",
    "Brazil",
    "Appian/Atlantic Nickel Santa Rita open-pit→underground conversion; Exame 25 Aug 2026 cites ~R$3.3bn UG CapEx. CapEx-fill: BNamericas 27 Mar 2026 reports construction start with ~R$3.3 billion (US$630 million). Distinct from atlantic_nickel_santa_rita_br presence and IFC/Appian fund rows.",
    "3300000000",
    "2026-03-27",
    "2026",
    "-14.28",
    "-39.85",
    "Santa Rita nickel mine, Itagibá, Bahia, Brazil (mine geography).",
    "bnamericas_atlantic_nickel_ug_20260327",
    "A Atlantic Nickel iniciou o processo de construção da maior mina subterrânea de níquel da América Latina, que deve exigir investimentos de cerca de R$3,3 bilhões (US$630 milhões).",
    "https://www.bnamericas.com/pt/noticias/atlantic-nickel-inicia-construcao-de-mina-subterranea-de-r33bi-na-bahia",
    "Actor: Atlantic Nickel / Appian Capital Brazil (UK PE) — allied. CapEx-fill upgrade: retain R$3.3bn face; add contemporaneous BNamericas US$630m as value_usd (UNVERIFIED proxy press FX). Thin nickel top-up / shuffle nickel.",
    "hunt_cycle216",
    investment_type="capex",
    evidence="proxy",
    currency="BRL",
    value_usd="630000000",
    fx_usd="",
    bib_type="press",
    chicago='BNamericas. “Atlantic Nickel inicia construção de mina subterrânea de R$3,3bi na Bahia.” March 27, 2026. https://www.bnamericas.com/pt/noticias/atlantic-nickel-inicia-construcao-de-mina-subterranea-de-r33bi-na-bahia.',
    annotation="Atlantic Nickel Santa Rita UG CapEx-fill USD 630m. Supports atlantic_nickel_ug_capex_2026.",
    evid_note="Opened BNamericas PT 2026-10-04; R$3.3bn (US$630m) / construction start / Santa Rita UG / Appian confirmed. CapEx-fill USD 630m UNVERIFIED proxy alongside stored BRL 3.3bn.",
)

# 3. bridges_roads / allied — CapEx-fill Sacyr Ruta 57 best offer UF 23.153m
row_doc(
    "sacyr_ruta57_best_offer_2026",
    "infrastructure",
    "bridges_roads",
    "allied",
    "Sacyr Concesiones Chile — Segunda Concesión Ruta 57 Santiago–Colina–Los Andes (best offer)",
    "Chile",
    "4 Sep 2026 MOP: Sacyr Concesiones Chile SPA presents best economic offer for Segunda Concesión Ruta 57 Santiago–Colina–Los Andes (~110.4 km incl. Ruta 57 / G-71 / new links; parallel Túnel Chacabuco). CapEx-fill: MOP states estimated investment UF 23.153.000 (value stored as UF; USD blank — no official FX on page). Preferred/best-offer milestone pending award decree. Distinct from other Sacyr Chile road rows.",
    "23153000",
    "",
    "2026",
    "-33.20",
    "-70.68",
    "Ruta 57 Santiago–Colina–Los Andes corridor, Región Metropolitana / Valparaíso, Chile (corridor geography).",
    "mop_ruta57_sacyr_best_20260904",
    "En un proceso marcado por una alta participación, este viernes 4 de septiembre se realizó el Acto de Apertura de Ofertas Económicas del proyecto Segunda Concesión Ruta 57 Santiago-Colina-Los Andes, iniciativa que contempla una inversión estimada de UF 23.153.000. Sacyr Concesiones Chile SPA presentó la mejor oferta.",
    "https://www.mop.gob.cl/sacyr-concesiones-chile-spa-presento-la-mejor-oferta-para-el-desarrollo-del-proyecto-segunda-concesion-ruta-57-santiago-colina-los-andes/",
    "Actor: Sacyr Concesiones Chile (Spanish Sacyr) — allied. Official MOP Spanish notice. CapEx-fill: UF 23.153.000 estimated investment stored (currency UF); USD not entered (no official FX on page). Shuffle bridges_roads.",
    "hunt_cycle216",
    investment_type="concession",
    evidence="documented",
    currency="UF",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Ministerio de Obras Públicas (Chile). “Sacyr Concesiones Chile SPA presentó la mejor oferta para el desarrollo del proyecto ‘Segunda Concesión Ruta 57 Santiago–Colina–Los Andes’.” September 4, 2026. https://www.mop.gob.cl/sacyr-concesiones-chile-spa-presento-la-mejor-oferta-para-el-desarrollo-del-proyecto-segunda-concesion-ruta-57-santiago-colina-los-andes/.',
    annotation="Sacyr Ruta 57 best offer CapEx-fill UF 23.153m. Supports sacyr_ruta57_best_offer_2026.",
    evid_note="Opened MOP primary 2026-10-04; UF 23.153.000 / Sacyr best offer / Ruta 57 Segunda Concesión confirmed. Value stored as UF; USD blank.",
)

# 4. port_ownership / allied — DP World Callao Shore Power USD 3.69m
row_doc(
    "dpworld_callao_shore_power_3p69m_2026",
    "infrastructure",
    "port_ownership",
    "allied",
    "DP World Callao — Shore Power (OPS) Muelles 2 y 3",
    "Peru",
    "17 Sep 2026 MTC: during viceministerial visit to DP World Callao Muelle Sur, verifies Sistema de Conexión Shore Power on Muelles 2 y 3 with investment USD 3.69 million, 95% physical progress, completion targeted Oct 2026. Distinct from dpworld_callao_bicentennial_2024 (USD 400m pier expansion) and dpworld_callao_adenda4_1470m_2026 (Adenda N.° 4 proposal).",
    "3690000",
    "2026-09-17",
    "2026",
    "-12.05",
    "-77.14",
    "DP World Callao Muelle Sur / Muelles 2–3, Callao, Peru (terminal geography).",
    "mtc_dpworld_callao_shore_power_20260917",
    "Asimismo, durante la visita se revisó la implementación del Corredor Humanitario Marítimo Callao–Paita … y se verificó la obra Sistema de Conexión Shore Power en los Muelles 2 y 3, la que posee una inversión de USD 3.69 millones, y que registra un 95 % de avance físico y culminación prevista para octubre de 2026.",
    "https://www.gob.pe/institucion/mtc/noticias/1445564-mtc-y-dp-world-callao-impulsan-nuevas-inversiones-para-ampliar-capacidad-del-muelle-sur",
    "Actor: DP World Callao (UAE DP World) — allied. Official MTC Spanish notice. CapEx face = USD 3.69m Shore Power package. Shuffle port_ownership.",
    "hunt_cycle216",
    investment_type="equipment_supply",
    evidence="documented",
    currency="USD",
    value_usd="3690000",
    fx_usd="1",
    bib_type="government",
    chicago='Ministerio de Transportes y Comunicaciones (Peru). “MTC y DP World Callao impulsan nuevas inversiones para ampliar capacidad del Muelle Sur.” September 17, 2026. https://www.gob.pe/institucion/mtc/noticias/1445564-mtc-y-dp-world-callao-impulsan-nuevas-inversiones-para-ampliar-capacidad-del-muelle-sur.',
    annotation="DP World Callao Shore Power USD 3.69m. Supports dpworld_callao_shore_power_3p69m_2026.",
    evid_note="Opened MTC gob.pe 2026-10-04; USD 3.69m / Muelles 2–3 Shore Power / 95% progress / Oct 2026 completion target confirmed.",
)

# 5. power_plants_grid / us — CapEx-fill GE Vernova São Simão modernization USD via Fed H.10
row_doc(
    "ge_vernova_sao_simao_ug3_2026",
    "energy",
    "power_plants_grid",
    "us",
    "GE Vernova — São Simão hydro modernization program (SPIC Brasil; UG3 milestone)",
    "Brazil",
    "14 Sep 2026 GE Vernova / SPIC Brasil: UG3 modernization complete in 10.3 months (third of six units at 1,710 MW São Simão); consortium led by GE Vernova with Powerchina hydromechanical/BOP scope; program CapEx >R$ 1.2 billion over ~10 years, completion targeted 2029. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~231.12m for stored R$1.2bn face. Distinct from other GE Vernova Brazil grid rows.",
    "1200000000",
    BRL_FX_DATE,
    "2026",
    "-18.99",
    "-50.51",
    "UHE São Simão, Goiás–Minas Gerais border, Brazil (plant geography).",
    "ge_vernova_sao_simao_ug3_20260914",
    "O robusto programa de modernização é impulsionado por um investimento superior a R$ 1,2 bilhão distribuído ao longo de dez anos. … A modernização da usina de 1.710 MW … está sendo executada por um consórcio liderado pela GE Vernova.",
    "https://www.gevernova.com/news/press-releases/spic-brasil-e-ge-vernova-aceleram-modernizacao-da-usina-hidreletrica-de-sao-simao",
    "Actor: GE Vernova (U.S.-listed) consortium lead — us; plant operator SPIC Brasil (PRC parent) with Powerchina package — counterpart not paired here. CapEx-fill: retain R$1.2bn; add Fed H.10 Sep 25 2026 FX to USD ~231.12m. ≥1/3 U.S. hunt budget / shuffle power_plants_grid.",
    "hunt_cycle216",
    investment_type="epc",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(1200000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    bib_type="company",
    chicago='GE Vernova. “SPIC Brasil e GE Vernova aceleram a modernização da Usina Hidrelétrica de São Simão, atingindo importantes marcos de desempenho.” September 14, 2026. https://www.gevernova.com/news/press-releases/spic-brasil-e-ge-vernova-aceleram-modernizacao-da-usina-hidreletrica-de-sao-simao.',
    annotation="GE Vernova São Simão CapEx-fill ~USD 231.12m via Fed H.10. Supports ge_vernova_sao_simao_ug3_2026.",
    evid_note="Opened GE Vernova PT release 2026-10-04; >R$1.2bn / UG3 10.3 months / GE Vernova lead + Powerchina / 1,710 MW confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
            # CapEx-fill / upgrade: merge non-empty fields onto existing
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
    print(f"cycle216 added {len(added)}: {added}")
    print(f"cycle216 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
