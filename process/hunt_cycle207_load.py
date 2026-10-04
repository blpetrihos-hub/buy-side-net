#!/usr/bin/env python3
"""Cycle 207 hunt: shuffle_seed=20261207; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261207).shuffle):
power_plants_grid, copper, water, lithium, solar, niobium, fission_smr, nickel,
port_ownership, port_cranes, balsa, wind, engineering_epc, graphite, rail,
other_renewables, bridges_roads, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Glenfarne/AES/EXIM/DFC/Fluence/Bechtel/Progress
Rail/Wabtec/Albemarle/EnergyX/USTDA/GE Vernova/SSA/Nextracker/Array/Pumpco sweeps
(+1 new U.S. row: Glenfarne Chile METLEN). PRC equal-budget: TIC Trens CRRC
concession hit; Goldwind/Sungrow/Envision/CAMC/CRBC Arequipa already logged.
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


# 1. solar / us — Glenfarne acquires METLEN Chile solar+BESS portfolio USD 865m
row_doc(
    "glenfarne_metlen_chile_solar_865m_2025",
    "energy",
    "solar",
    "us",
    "Glenfarne Group — acquisition of four METLEN Chile solar+BESS projects (909 MW)",
    "Chile",
    "23 Dec 2025 Glenfarne: subsidiary completes acquisition from METLEN of four northern-Chile energy projects — combined 909 MW installed (588 MW solar + associated BESS 1.61 GWh / 321 MW-equivalent). Transaction valued at USD 865 million including assumed debt; concurrent >USD 1bn finance package (Scotiabank / BNP Paribas / Société Générale). BESS completion by METLEN 1H 2026. Distinct from jinko_ess_chile_340mw_1600mwh_2025 (METLEN/Jinko ESS supply, different MW-MWh).",
    "865000000",
    "2025-12-23",
    "2025",
    "",
    "",
    "Northern Chile provinces / SEN interconnection nodes (company release does not name a single municipality — lat/lon blank).",
    "glenfarne_metlen_chile_20251223",
    "A subsidiary of Glenfarne Group , LLC (“Glenfarne”) today announced the completion of a previously announced acquisition of four energy projects in Chile with a combined 909 Megawatts (“MW”) of installed capacity comprised of 588 MW of solar and associated battery energy storage system (“BESS”) facilities with a capacity of 1.61 Gigawatt-hours (“GWh”) (321 MW equivalent). Glenfarne acquired the assets from Metlen Energy & Metals (“METLEN”). … The transaction is valued at $865 million including the assumption of debt",
    "https://glenfarnegroup.com/glenfarne-completes-acquisition-of-integrated-utility-scale-solar-and-battery-assets-in-chile-from-metlen/",
    "Actor: Glenfarne Group (U.S., New York) — us; seller METLEN (Greece). Company English primary. Face = USD 865m including assumed debt. Shuffle solar.",
    "hunt_cycle207",
    investment_type="ownership_equity",
    evidence="documented",
    currency="USD",
    value_usd="865000000",
    fx_usd="1",
    bib_type="company",
    chicago='Glenfarne Group. “Glenfarne Completes Acquisition of Integrated Utility-Scale Solar and Battery Assets in Chile From Metlen.” December 23, 2025. https://glenfarnegroup.com/glenfarne-completes-acquisition-of-integrated-utility-scale-solar-and-battery-assets-in-chile-from-metlen/.',
    annotation="Glenfarne–METLEN Chile 909 MW solar+BESS acquisition USD 865m. Supports glenfarne_metlen_chile_solar_865m_2025.",
    evid_note="Opened Glenfarne company primary 2026-10-04; USD 865m / 588 MW solar / 1.61 GWh BESS / northern Chile confirmed.",
)

# 2. rail / prc — TIC Trens (CRRC 40% / Comporte 60%) São Paulo–Campinas concession CapEx R$13.48bn
row_doc(
    "crrc_tic_trens_eixo_norte_13p48bn_2024",
    "infrastructure",
    "rail",
    "prc",
    "TIC Trens (CRRC Hong Kong 40% / Grupo Comporte 60%) — TIC Eixo Norte + TIM + Linha 7-Rubi concession",
    "Brazil",
    "ARTESP concession page: TIC Trens (Grupo Comporte + CRRC) — contract signed 3 Jun 2024; concession start Dec 2025; 30-year term; estimated investment R$13.48 billion; outorga R$268 million. Scope: TIC Eixo Norte express São Paulo–Campinas 101 km (via Jundiaí), TIM Jundiaí–Campinas 44 km, and Linha 7-Rubi modernization 60.5 km; fleets include 15 new TIC + 7 new TIM trains. Distinct from crrc_araraquara_factory_2026 (manufacturing plant) and crrc_sp_metro_frota_r_44_2025 (metro rolling stock).",
    "13480000000",
    "2024-06-03",
    "2024",
    "-23.5505",
    "-46.6333",
    "TIC Eixo Norte corridor São Paulo (Barra Funda)–Jundiaí–Campinas (ARTESP geography; approximate São Paulo pin for named corridor).",
    "artesp_tic_trens_concession",
    "Empresa(s) Controladora(s): Grupo Comporte e CRRC Data da Assinatura do Contrato: 03/06/2024 Início da Concessão: 12/2025 Prazo da Concessão: 30 anos Investimento estimado: R$ 13,48 bilhões Contraprestação / Outorga: R$ 268 milhões … Trem Intercidades (TIC) Eixo Norte vai ligar a Capital a Campinas … Extensões - TIC (Serviço Expresso): 101 km - TIM (Serviço Parador): 44 km - Linha 7 (Serviço Parador): 60,5 km",
    "https://www.artesp.sp.gov.br/artesp/setor-regulado/metroferroviario/tic-trens",
    "Actor: CRRC (PRC SOE) 40% with Grupo Comporte 60% in TIC Trens — prc. ARTESP Portuguese regulator primary. CapEx face = BRL 13.48bn; Fed H.10 3 Jun 2024 BRL per USD 5.2345 → USD 2,575,222,084. Shuffle rail.",
    "hunt_cycle207",
    investment_type="concession",
    evidence="documented",
    currency="BRL",
    value_usd="2575222084",
    fx_usd="5.2345",
    bib_type="government",
    chicago='ARTESP (Agência de Transporte do Estado de São Paulo). “TIC Trens.” Concession registry page. https://www.artesp.sp.gov.br/artesp/setor-regulado/metroferroviario/tic-trens.',
    annotation="TIC Trens CRRC/Comporte SP–Campinas concession CapEx R$13.48bn. Supports crrc_tic_trens_eixo_norte_13p48bn_2024.",
    evid_note="Opened ARTESP Portuguese primary 2026-10-04; R$13.48bn / CRRC+Comporte / 101 km TIC / 3 Jun 2024 signature confirmed. FX Fed H.10 2024-06-03 BRL per USD 5.2345.",
)

# 3. engineering_epc / allied — Siemens Energy Petrobras/SBM FPSO P-81/P-87 power+compression skids
row_doc(
    "siemens_energy_petrobras_fpso_p81_p87_2026",
    "infrastructure",
    "engineering_epc",
    "allied",
    "Siemens Energy — power generation + gas compression skids for Petrobras FPSOs P-81 / P-87 (SEAP)",
    "Brazil",
    "10 Aug 2026 Siemens Energy: supply of 16 main modular systems (skids) — eight per platform — for Petrobras FPSOs P-81 and P-87 in the Sergipe-Alagoas Deepwater basin (SEAP I/II), via partnership with SBM Offshore. Per FPSO: four gas-turbine generators, three gas-turbine-driven compressor trains, one electrically driven injection compressor. Majority assembly at Santa Bárbara d’Oeste (SP); first package to SBM by end-2027, final deliveries through 2028. CapEx USD not disclosed. Distinct from siemens_axia_chesf_retrofit_2025 / siemens_manzanillo_power_land_414mw_2026.",
    "",
    "",
    "2026",
    "-11.00",
    "-36.50",
    "Sergipe-Alagoas Deepwater basin / FPSOs P-81 and P-87 (company geography; approximate offshore basin pin).",
    "siemens_energy_fpso_p81_p87_20260810",
    "In total, Siemens Energy will supply 16 main modular systems (skids), eight for each platform, which combine the necessary equipment for power generation and gas compression solutions. For each FPSO, this package includes four gas turbine generators to supply electricity, three gas turbine-driven compressor trains for gas processing and export, and one electrically driven compressor for gas injection into the reservoir. … The first solution package will be delivered to SBM Offshore by the end of 2027, with final deliveries scheduled throughout 2028.",
    "https://www.siemens-energy.com/global/en/home/press-releases/siemens-energy-advances-offshore-expansion-in-brazil-with-supply.html",
    "Actor: Siemens Energy (Germany) — allied; counterpart Petrobras/SBM Offshore. Company English primary. CapEx blank. Shuffle engineering_epc.",
    "hunt_cycle207",
    investment_type="equipment_supply",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Siemens Energy. “Siemens Energy advances offshore expansion in Brazil with supply for Petrobras platforms.” August 10, 2026. https://www.siemens-energy.com/global/en/home/press-releases/siemens-energy-advances-offshore-expansion-in-brazil-with-supply.html.',
    annotation="Siemens Energy Petrobras FPSO P-81/P-87 skids; CapEx blank. Supports siemens_energy_petrobras_fpso_p81_p87_2026.",
    evid_note="Opened Siemens Energy English primary 2026-10-04; 16 skids / P-81+P-87 / SEAP / SBM delivery 2027–28 confirmed; CapEx undisclosed.",
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
            rows[by_id[rid]].update(full)
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
    print(f"cycle207 added {len(added)}: {added}")
    print(f"cycle207 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
