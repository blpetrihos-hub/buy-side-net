#!/usr/bin/env python3
"""Cycle 196 hunt: shuffle_seed=20261196; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261196).shuffle):
water, bridges_roads, wind, copper, engineering_epc, other_renewables, rail,
fission_smr, power_plants_grid, port_ownership, niobium, port_cranes, balsa,
lithium, nickel, building_materials, solar, graphite.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Google DR Digital Port, ODATA/Aligned green financing,
SEC/EXIM/AES/Freeport sweeps — 2 new U.S. rows.
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


# 1. engineering_epc / us — Google DR Digital Port phase-1 >USD 500m
row_doc(
    "google_dr_digital_port_500m_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Google — first LatAm Digital Exchange Port + submarine cable ring (Dominican Republic)",
    "Dominican Republic",
    "19 Feb 2026 Ministerio de la Presidencia (minpre): President Abinader signs Decree 113-26 declaring digital exchange ports and submarine-cable systems national priority; Google announces Digital Exchange Port (eighth worldwide; first in LatAm under construction) plus international submarine-cable ring connecting DR to continental U.S. / dual Google Cloud AI regions. First-phase investment exceeds USD 500 million. CapEx floor = USD 500m. Distinct from AES Andes Google Quilicura PPA and AWS Chile Region rows.",
    "500000000",
    "2026-02-19",
    "2026",
    "",
    "",
    "Google Digital Exchange Port / submarine-cable ring package, Dominican Republic (company national; worksite not named precisely — lat/lon blank).",
    "minpre_google_digital_port_20260219",
    "La primera fase de la inversión supera los 500 millones de dólares y colocará a la República Dominicana en el centro del intercambio de información entre América del Norte, Centroamérica y Sudamérica. … El director de Infraestructura Global de Google, Cristian Ramos, informó que este es el octavo puerto en el mundo de Google y el primero en Latinoamérica que se encuentra en construcción.",
    "https://minpre.gob.do/comunicacion/notas-de-prensa/google-construira-un-puerto-internacional-de-intercambio-digital-en-rd/",
    "Actor: Google (Alphabet Inc., U.S.) — us. Dominican Presidency/minpre Spanish primary. CapEx floor >USD 500m (stored as 5e8 floor). Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle196",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="500000000",
    fx_usd="1",
    bib_type="government",
    chicago='Ministerio de la Presidencia de la República Dominicana. “Google construirá un puerto internacional de intercambio digital en RD.” February 19, 2026. https://minpre.gob.do/comunicacion/notas-de-prensa/google-construira-un-puerto-internacional-de-intercambio-digital-en-rd/.',
    annotation="Minpre: Google DR Digital Port phase-1 >USD 500m. Supports google_dr_digital_port_500m_2026.",
    evid_note="Opened minpre Spanish release 2026-10-04; phase-1 >USD 500m confirmed.",
)

# 2. engineering_epc / us — ODATA (Aligned Data Centers) USD 1.02bn green financing
row_doc(
    "odata_aligned_green_financing_1p02bn_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "ODATA (Aligned Data Centers) — LatAm green financing for sustainable data centers",
    "Brazil",
    "4 Sep 2025 Aligned Data Centers / ODATA: announces US$1.02 billion green financing focused on sustainable data-center infrastructure investments across Brazil, Mexico, Chile, and Colombia; largest of its kind for LatAm data centers; brings ODATA total financing to US$2.25 billion. CapEx/financing = USD 1.02bn. Distinct from Equinix Bogotá DC2 and Ascenty AI campus rows.",
    "1020000000",
    "2025-09-04",
    "2025",
    "",
    "",
    "ODATA LatAm data-center growth package (Brazil/Mexico/Chile/Colombia; multi-site — lat/lon blank).",
    "aligned_odata_green_financing_20250904",
    "ODATA, an Aligned Data Centers Company (“ODATA” or the “Company”), a leader in the construction and operation of data centers in Latin America, today announced a US $1.02 billion green financing focused on sustainable data center infrastructure investments. … It will support the Company’s growth across key regional markets — Brazil, Mexico, Chile, and Colombia.",
    "https://aligneddc.com/press-release/odata-secures-landmark-green-financing/",
    "Actor: ODATA / Aligned Data Centers (U.S. parent) — us. Company English primary. Financing = USD 1.02bn for LatAm DC CapEx. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle196",
    investment_type="financing",
    evidence="documented",
    currency="USD",
    value_usd="1020000000",
    fx_usd="1",
    bib_type="company",
    chicago='Aligned Data Centers. “ODATA Secures Landmark Green Financing, Setting New Standard for Latin American Data Centers.” September 4, 2025. https://aligneddc.com/press-release/odata-secures-landmark-green-financing/.',
    annotation="Aligned/ODATA: USD 1.02bn green financing LatAm DCs. Supports odata_aligned_green_financing_1p02bn_2025.",
    evid_note="Opened Aligned Data Centers English press release 2026-10-04.",
)

# 3. rail / allied — VLI FCA 2026 CapEx ~R$1.2bn
row_doc(
    "vli_fca_capex_1p2bn_brl_2026",
    "infrastructure",
    "rail",
    "allied",
    "VLI (Brookfield largest shareholder) — Ferrovia Centro-Atlântica 2026 CapEx",
    "Brazil",
    "5 Feb 2026 VLI: prepares investment of about R$ 1.2 billion in the Ferrovia Centro-Atlântica (FCA) for permanent-way and rolling-stock maintenance and other operational/safety improvements; fourth consecutive year above R$1bn; cumulative 2023–2026 ~R$4.8bn; concession renewal still pending. CapEx = ~R$1.2bn. Distinct from progress_rail_vli_sd70_200m_brl_2024 (locomotive OEM CapEx) and progress_rail_vli_msa_norte_500m_brl_2025 (MSA).",
    "1200000000",
    "2026-02-05",
    "2026",
    "",
    "",
    "Ferrovia Centro-Atlântica (FCA) multi-state network (MG/ES/GO/BA/SP) — lat/lon blank (network CapEx).",
    "vli_fca_1p2bn_20260205",
    "Em um ano que pode marcar o início de mais um ciclo da concessão da Ferrovia Centro-Atlântica, a VLI – companhia de soluções logísticas que opera ferrovias, portos e terminais – prepara investimento de cerca de R$ 1,2 bilhão nesta malha ferroviária. Os recursos serão utilizados para manutenção da via permanente e material rodante, entre outras melhorias, com foco na excelência e na segurança das operações.",
    "https://www.vli-logistica.com.br/vli-mantem-investimento-na-fca-acima-de-r-1-bilhao-pelo-quarto-ano-consecutivo/",
    "Actor: VLI S.A. — Brookfield largest shareholder (36.5%; Canada) with Vale/Mitsui/FI-FGTS/BNDESPar — allied. Company Portuguese primary. CapEx ≈ R$1.2bn (BRL stored without FX). Shuffle rail.",
    "hunt_cycle196",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='VLI Logística. “VLI mantém investimento na FCA acima de R$ 1 bilhão pelo quarto ano consecutivo.” February 5, 2026. https://www.vli-logistica.com.br/vli-mantem-investimento-na-fca-acima-de-r-1-bilhao-pelo-quarto-ano-consecutivo/.',
    annotation="VLI: FCA 2026 CapEx ~R$1.2bn. Supports vli_fca_capex_1p2bn_brl_2026.",
    evid_note="Opened VLI Portuguese release 2026-10-04; ~R$1.2bn CapEx confirmed.",
)

# 4. power_plants_grid / prc — CPFL Energia FY2025 CapEx R$6.1bn
row_doc(
    "cpfl_fy2025_capex_6p1bn_brl",
    "energy",
    "power_plants_grid",
    "prc",
    "CPFL Energia (State Grid–controlled) — FY2025 record CapEx",
    "Brazil",
    "6 Mar 2026 CPFL Energia: executed R$ 6.1 billion CapEx in 2025 (+5.5% YoY), described as the company’s largest investment cycle; distribution quality (DEC/FEC) cited among national leaders; transmission reinforcement/improvement investments >R$800m within the year. CapEx = R$6.1bn. Distinct from sgbh_gate_uhv_18bn_brl_2025 and state_grid_mantiqueira_tx_2025.",
    "6100000000",
    "2026-03-06",
    "2025",
    "",
    "",
    "CPFL Energia Brazil distribution/transmission CapEx (national multi-concession footprint — lat/lon blank).",
    "cpfl_fy2025_results_20260306",
    "Em 2025, a CPFL executou R$ 6,1 bilhões em CAPEX, avanço de 5,5% frente ao ano anterior. O Conselho de Administração aprovou ainda o novo plano de investimentos para o período de 2026 a 2030, que totaliza R$ 31,1 bilhões, sendo R$ 25,3 bilhões para o segmento de Distribuição e R$ 4,5 bilhões para a Transmissão.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61",
    "Actor: CPFL Energia — controlled by State Grid Corporation of China — prc. Company Portuguese primary. CapEx = R$6.1bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle196",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra EBITDA de R$ 13,5 bilhões em 2025 e investimento recorde de R$ 6,1 bilhões.” March 6, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61.',
    annotation="CPFL: FY2025 CapEx R$6.1bn. Supports cpfl_fy2025_capex_6p1bn_brl.",
    evid_note="Opened CPFL Portuguese results release 2026-10-04.",
)

# 5. power_plants_grid / prc — CPFL 2026–2030 CapEx plan R$31.1bn
row_doc(
    "cpfl_capex_plan_31p1bn_2026_2030",
    "energy",
    "power_plants_grid",
    "prc",
    "CPFL Energia (State Grid–controlled) — 2026–2030 CapEx plan",
    "Brazil",
    "6 Mar 2026 CPFL Energia: Board approves new investment plan for 2026–2030 totaling R$ 31.1 billion — R$ 25.3 billion for Distribution and R$ 4.5 billion for Transmission (remainder other segments). CapEx plan = R$31.1bn envelope. Distinct from cpfl_fy2025_capex_6p1bn_brl (executed 2025 spend) and SGBH GATE UHV row.",
    "31100000000",
    "2026-03-06",
    "2026",
    "",
    "",
    "CPFL Energia 2026–2030 Brazil CapEx plan (national multi-concession — lat/lon blank).",
    "cpfl_fy2025_results_20260306",
    "O Conselho de Administração aprovou ainda o novo plano de investimentos para o período de 2026 a 2030, que totaliza R$ 31,1 bilhões, sendo R$ 25,3 bilhões para o segmento de Distribuição e R$ 4,5 bilhões para a Transmissão.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61",
    "Actor: CPFL Energia — State Grid–controlled — prc. Company Portuguese primary. CapEx plan = R$31.1bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle196",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra EBITDA de R$ 13,5 bilhões em 2025 e investimento recorde de R$ 6,1 bilhões.” March 6, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61.',
    annotation="CPFL: 2026–2030 CapEx plan R$31.1bn. Supports cpfl_capex_plan_31p1bn_2026_2030.",
    evid_note="Opened CPFL Portuguese results release 2026-10-04; plan R$31.1bn confirmed.",
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
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle196 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
