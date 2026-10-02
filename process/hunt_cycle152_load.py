#!/usr/bin/env python3
"""Cycle 152 hunt: shuffle_seed=20261152; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: balsa, power_plants_grid, other_renewables, rail,
building_materials, bridges_roads, nickel, solar, niobium, graphite,
port_ownership, wind, port_cranes, water, fission_smr, lithium,
engineering_epc, copper.

PRC ahead by 13 after 151 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr/nickel (dry → niobium).
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


# 1. other_renewables / us — AES Gener–Teck Carmen de Andacollo 550 GWh/y
row_doc(
    "aes_andes_teck_cda_550gwh_2020",
    "energy",
    "other_renewables",
    "us",
    "AES Gener / AES Andes — Teck Carmen de Andacollo renewable PPA (550 GWh/y)",
    "Chile",
    "17 Sep 2020 AES Andes: Chilean affiliates of Teck and AES enter long-term PPA for 100% renewable power at Carmen de Andacollo copper mine (Coquimbo); CdA sources 72 MW (550 GWh/year) from AES Gener renewable portfolio (wind, solar, hydro); effective 1 Sep 2020 through end-2031. CapEx blank (offtake/PPA). Distinct from aes_andes_teck_qb2_1069gwh_2022.",
    "",
    "",
    "2020",
    "-30.250",
    "-71.070",
    "Carmen de Andacollo mine, Coquimbo Region, Chile (AES–Teck offtake naming).",
    "aes_andes_teck_cda_ppa_20200917",
    "Under the agreement, CdA will source 72 Megawatts (MW) (550 GWh/year) from AES Gener’s growing renewable portfolio of wind, solar and hydroelectric energy… The Carmen de Andacollo renewable power arrangement is in effect as of September 1, 2020 and will run through to the end of 2031.",
    "https://www.aesandes.com/en/press-release/teck-carmen-de-andacollo-switches-renewable-power",
    "Actor: AES Gener / AES Andes / AES Corporation (U.S.) — us. Company English primary for offtake volume. CapEx blank (PPA).",
    "hunt_energy_other_renewables",
    investment_type="offtake",
    chicago='AES Andes. “Teck Carmen de Andacollo Switches to Renewable Power.” September 17, 2020. https://www.aesandes.com/en/press-release/teck-carmen-de-andacollo-switches-renewable-power.',
    annotation="AES Andes: Teck CdA 550 GWh/y renewable PPA through 2031. Supports aes_andes_teck_cda_550gwh_2020.",
    evid_note="Opened AES Andes–Teck Carmen de Andacollo PPA primary (550 GWh/y; CapEx blank).",
)

# 2. power_plants_grid / us — AES Andes Alto Maipo 531 MW COD
row_doc(
    "aes_andes_alto_maipo_531mw_cod_2022",
    "energy",
    "power_plants_grid",
    "us",
    "AES Andes — Alto Maipo run-of-river hydro COD (531 MW)",
    "Chile",
    "4 Nov 2022 AES Andes: Alto Maipo, a 531 MW renewable project essential for Chile’s decarbonization, is already a reality and delivering 100% renewable energy to the National Electric System (run-of-river hydro complex Alfalfal II / Las Lajas). Company history lists commercial operations commencement in 2022. CapEx blank on COD/operating release (prior restructuring/deconsolidation narrative separate). Distinct from aes_andes_campo_lindo_cod_2023 and Virtual Reservoir rows.",
    "",
    "",
    "2022",
    "-33.600",
    "-70.200",
    "Alto Maipo / San José de Maipo, Metropolitan Region, Chile (company geography; approximate pin).",
    "aes_andes_greentegra_20221104",
    "In addition, Alto Maipo, a 531 MW renewable project, essential for Chile's decarbonization process, is already a reality and is delivering 100% renewable energy to the National Electric System.",
    "https://www.aesandes.com/en/press-release/aes-andes-consolidates-greentegra-strategy-new-projects-and-100-renewable-plants",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary confirming 531 MW delivering to SEN. CapEx blank.",
    "hunt_energy_power_plants_grid",
    investment_type="greenfield",
    chicago='AES Andes. “AES Andes consolidates Greentegra strategy with new projects and 100% renewable plants.” November 4, 2022. https://www.aesandes.com/en/press-release/aes-andes-consolidates-greentegra-strategy-new-projects-and-100-renewable-plants.',
    annotation="AES Andes: Alto Maipo 531 MW delivering to SEN. Supports aes_andes_alto_maipo_531mw_cod_2022.",
    evid_note="Opened AES Andes Greentegra release confirming Alto Maipo 531 MW operational (CapEx blank).",
)

# 3. solar / prc — POWERCHINA Cura Brochero + Villa María del Río Seco 65 MW
row_doc(
    "powerchina_cura_brochero_villa_maria_65mw_2020",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Cura Brochero (30 MWp) + Villa de María del Río Seco (35 MWp) solar",
    "Argentina",
    "POWERCHINA Argentina Sucursal: solar parks Cura Brochero and Villa de María del Río Seco in Córdoba Province totaling 65 MW; POWERCHINA won the tender in March 2020; Cura Brochero 30 MWp and Villa de María del Río Seco 35 MWp. CapEx blank on opened page. Distinct from powerchina_san_carlos_18p3mw_salta_2024 and powerchina_cafayate_argentina_97p6mw_epc.",
    "",
    "",
    "2020",
    "-31.390",
    "-65.000",
    "Cura Brochero / Villa de María del Río Seco, Córdoba Province, Argentina (POWERCHINA Sucursal naming; approximate mid-province pin).",
    "powerchina_ar_cura_brochero",
    "Los proyectos solares Cura Brochero y Villa de María del Río Seco están ubicados en la provincia de Córdoba en Argentina y tiene una capacidad total de 65 MW. POWERCHINA ganó la licitación en marzo de 2020… El Parque Solar Cura Brochero cuenta con una capacidad de 30 MWp y Villa de María del Río Seco es una planta fotovoltaica con una potencia instalada de 35 MWp.",
    "https://www.powerchina.com.ar/cura-brochero.html",
    "Actor: POWERCHINA (PRC SOE) — prc. Company Argentina primary for award + 65 MW split. CapEx blank.",
    "hunt_energy_solar",
    investment_type="epc",
    chicago='POWERCHINA Ltd. Sucursal Argentina. “Parques Solares Cura Brochero y Villa de María del Río Seco.” https://www.powerchina.com.ar/cura-brochero.html.',
    annotation="POWERCHINA Argentina: Cura Brochero + Villa María 65 MW. Supports powerchina_cura_brochero_villa_maria_65mw_2020.",
    evid_note="Opened POWERCHINA Argentina Cura Brochero/Villa María primary (65 MW; CapEx blank).",
)

# 4. solar / prc — POWERCHINA Andina de las Marianas 120 MWp + 72 MW/288 MWh BESS EPC
row_doc(
    "powerchina_andina_marianas_120mwp_2021",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Andina de las Marianas off-grid PV+BESS EPC (120 MWp + 72 MW/288 MWh)",
    "Argentina",
    "POWERCHINA Argentina Sucursal: Andina de las Marianas PV+storage project in Salta Province at 3,770 m altitude — 120 MWp photovoltaic plus 72 MW / 288 MWh storage; described as LatAm’s largest off-grid solar+storage park; owner Litio Minera Argentina S.A. (Ganfeng Mariana lithium complex offtake); POWERCHINA signed contract November 2021; 100% of electricity for lithium plant at Tolar Grande. CapEx blank on EPC page (distinct from ganfeng_mariana_solar_190m_2025 ownership CapEx proxy).",
    "",
    "",
    "2021",
    "-24.590",
    "-67.450",
    "Andina de las Marianas / Tolar Grande, Salta Province, Argentina (POWERCHINA Sucursal geography; approximate pin).",
    "powerchina_ar_andina_marianas",
    "El proyecto incluye una central fotovoltáica de 120 MWp más un almacenamiento de energía de 72 MW / 288 MWh. Es el parque solar offgrid y de storage más grande de América Latina. El propietario es Litio Minera Argentina S.A.. POWERCHINA firmó el contrato en noviembre de 2021… el cien por ciento de su electricidad será utilizada en la planta de litio… en el municipio de Tolar Grande.",
    "https://www.powerchina.com.ar/andina.html",
    "Actor: POWERCHINA (PRC SOE) — prc (EPC). Owner Litio Minera Argentina / Ganfeng — separate ownership CapEx row. CapEx blank on EPC primary.",
    "hunt_energy_solar",
    investment_type="epc",
    chicago='POWERCHINA Ltd. Sucursal Argentina. “Parque Solar Andina de las Marianas.” https://www.powerchina.com.ar/andina.html.',
    annotation="POWERCHINA Argentina: Andina Marianas 120 MWp + 72 MW/288 MWh off-grid EPC. Supports powerchina_andina_marianas_120mwp_2021.",
    evid_note="Opened POWERCHINA Argentina Andina Marianas EPC primary (120 MWp + BESS; CapEx blank).",
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
    print(f"Cycle 152 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
