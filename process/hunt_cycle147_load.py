#!/usr/bin/env python3
"""Cycle 147 hunt: shuffle_seed=20261147; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: power_plants_grid, solar, fission_smr, port_cranes, rail,
bridges_roads, engineering_epc, graphite, copper, building_materials, lithium,
port_ownership, niobium, other_renewables, wind, balsa, water, nickel.

PRC ahead by 8 after 146 — keep equal US/PRC budget without padding.
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


# 1. solar / us — AES Colombia San Fernando 61 MWp COD; ~USD 40m (Ecopetrol)
row_doc(
    "aes_san_fernando_61mw_colombia_2021",
    "energy",
    "solar",
    "us",
    "AES Colombia — Parque Solar San Fernando COD (Castilla La Nueva, Meta)",
    "Colombia",
    "22 Oct 2021 Ecopetrol: Grupo Ecopetrol / Cenit / AES Colombia put San Fernando solar park into operation — 61 MWp; 57 ha / >114k bifacial tracker panels; AES Colombia built under 15-year energy-supply + O&M contract for Cenit; investment ~USD 40 million. Distinct from aes_colombia_solar3_anla_100mw_2025 and aes_castilla_21mw_colombia_2019.",
    "40000000",
    "2021-10-22",
    "2021",
    "3.950",
    "-73.680",
    "Castilla La Nueva, Meta Department, Colombia (Ecopetrol/AES project geography).",
    "ecopetrol_aes_san_fernando_20211022",
    "Esta mega estructura solar fue construida por AES Colombia por solicitud de Cenit bajo un contrato de suministro de energía por 15 años, que incluye su operación y mantenimiento. La inversión fue cercana a los US$40 millones… El ecoparque San Fernando tiene una potencia instalada de 61 megavatios (MWp).",
    "https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/Noticias+2021/grupo-ecopetrol-ceni-aes-inauguraron-parque-solar-san-fernando",
    "Actor: AES Colombia / AES Corporation (U.S.) — us. Ecopetrol official primary for COD + CapEx. Self-generation for Cenit/Ecopetrol offtake.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago='Ecopetrol S.A. “Grupo Ecopetrol, Cenit y AES pusieron en operación el Parque Solar San Fernando en el Meta.” October 22, 2021. https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/Noticias+2021/grupo-ecopetrol-ceni-aes-inauguraron-parque-solar-san-fernando.',
    annotation="Ecopetrol primary: AES San Fernando 61 MWp COD / ~USD 40m. Supports aes_san_fernando_61mw_colombia_2021.",
    evid_note="Opened Ecopetrol San Fernando COD release 22 Oct 2021 (61 MWp; ~USD 40m).",
)

# 2. solar / us — AES Colombia Castilla 21 MWp COD; ~USD 20m (Ecopetrol)
row_doc(
    "aes_castilla_21mw_colombia_2019",
    "energy",
    "solar",
    "us",
    "AES Colombia — Parque Solar Castilla COD (Castilla La Nueva, Meta)",
    "Colombia",
    "18 Oct 2019 Ecopetrol: Ecopetrol and AES Colombia put Castilla solar park into operation — 21 MWp; AES Colombia built under 15-year supply + O&M contract; investment ~USD 20 million; >54,500 panels on 18 ha; supplies Castilla oil field. Distinct from aes_san_fernando_61mw_colombia_2021.",
    "20000000",
    "2019-10-18",
    "2019",
    "3.940",
    "-73.690",
    "Castilla La Nueva, Meta Department, Colombia (Ecopetrol Castilla field / park geography).",
    "ecopetrol_aes_castilla_20191018",
    "Este parque solar fue construido por AES Colombia por solicitud de Ecopetrol bajo un contrato de suministro de energía por 15 años, que incluye su operación y mantenimiento. La inversión fue cercana a los US$20 millones. El parque tiene una potencia instalada de 21 megavatios (MWp).",
    "https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/Noticias+2019/Noticias+Octubre/Noticia+12+Octubre+2019",
    "Actor: AES Colombia / AES Corporation (U.S.) — us. Ecopetrol official primary for COD + CapEx.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago='Ecopetrol S.A. “Ecopetrol y AES pusieron en operación Parque Solar Castilla en el Meta.” October 18, 2019. https://www.ecopetrol.com.co/wps/portal/Home/es/noticias/detalle/Noticias+2019/Noticias+Octubre/Noticia+12+Octubre+2019.',
    annotation="Ecopetrol primary: AES Castilla 21 MWp COD / ~USD 20m. Supports aes_castilla_21mw_colombia_2019.",
    evid_note="Opened Ecopetrol Castilla COD release 18 Oct 2019 (21 MWp; ~USD 20m).",
)

# 3. copper / prc — MMG Las Bambas H1 2026 CapEx USD 272.4m
row_doc(
    "mmg_las_bambas_h1_2026_capex_272m",
    "resources",
    "copper",
    "prc",
    "MMG — Las Bambas H1 2026 capital expenditure (Peru)",
    "Peru",
    "11 Aug 2026 MMG Interim Results (HKEX): capital expenditure totalled US$553.8 million in H1 2026, including US$272.4 million at Las Bambas. Distinct from mmg_las_bambas_2025_capex_494m (full-year 2025 actual) and mmg_las_bambas_2026_capex (full-year 2026 guidance USD 800–850m).",
    "272400000",
    "2026-06-30",
    "2026",
    "-14.080",
    "-72.300",
    "Las Bambas mine, Apurímac Region, Peru (company asset geography).",
    "mmg_interim_results_20260811",
    "Capital expenditure totalled US$553.8 million in the first half of 2026, including US$272.4 million at Las Bambas, US$138.6 million at Khoemacau (of which US$91.1 million related to the expansion project) and US$45.8 million at Kinsevere.",
    "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0811/2026081100891.pdf",
    "Actor: MMG Ltd (China Minmetals-controlled) — prc. HKEX interim results primary. H1 actual spend vs full-year guidance/prior-year rows.",
    "hunt_res_copper",
    investment_type="capex",
    chicago='MMG Limited. “Announcement of Interim Results for the Six Months Ended 30 June 2026.” August 11, 2026. https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0811/2026081100891.pdf.',
    annotation="MMG H1 2026 interim: Las Bambas CapEx USD 272.4m. Supports mmg_las_bambas_h1_2026_capex_272m.",
    evid_note="Opened MMG HKEX interim results 11 Aug 2026 (Las Bambas H1 CapEx USD 272.4m).",
)

# 4. wind / prc — POWERCHINA EPC for Goldwind Loma Blanca I–III/VI + Miramar (355 MW)
row_doc(
    "powerchina_loma_blanca_miramar_355mw_epc",
    "energy",
    "wind",
    "prc",
    "POWERCHINA — Loma Blanca I–III/VI + Miramar wind EPC (Goldwind Argentina)",
    "Argentina",
    "POWERCHINA Argentina branch: Goldwind contracted POWERCHINA under EPC for Loma Blanca I, II, III (52 MW each), Loma Blanca VI (103 MW) and Miramar (96 MW) — combined 355 MW installed wind capacity; Loma Blanca parks in Chubut between Rawson and Trelew; Miramar in southern Buenos Aires Province. CapEx blank on branch page. Distinct from goldwind_lomas_taltal_342mw_install_2024 (Chile OEM install).",
    "",
    "",
    "2019",
    "-43.300",
    "-65.100",
    "Loma Blanca corridor between Rawson and Trelew, Chubut Province, Argentina (company geography; Miramar is separate BA Province site).",
    "powerchina_ar_loma_blanca_miramar_epc",
    "La empresa Goldwind, propietaria de los Parques Eólicos Loma Blanca I, II, III (de 52 Mw cada uno de potencia instalada), Loma Blanca VI (de 103 Mw) y Parque Eólico Miramar (de 96 Mw), ha contratado bajo la modalidad EPC a POWERCHINA para la ejecución de la totalidad de estos Parques, totalizando una potencia instalada eólica de 355 Mw.",
    "https://powerchina.com.ar/loma-blanca-miramar.html",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; owner Goldwind (PRC) — same-side. Company Argentina branch primary. CapEx blank. Works targeted completion 2019 on page.",
    "hunt_energy_wind",
    investment_type="epc",
    chicago='POWERCHINA Ltd. Sucursal Argentina. “Loma Blanca I, II, III, VI / Parque Eólico Miramar.” Accessed 2026. https://powerchina.com.ar/loma-blanca-miramar.html.',
    annotation="POWERCHINA Argentina: Goldwind Loma Blanca+Miramar 355 MW wind EPC. Supports powerchina_loma_blanca_miramar_355mw_epc.",
    evid_note="Opened POWERCHINA Argentina Loma Blanca/Miramar EPC page (355 MW).",
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
    print(f"Cycle 147 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
