#!/usr/bin/env python3
"""Cycle 44 thin_topup: balsa / nickel / water (fewest post-pass).

Hit: Aguas Pacífico desal CAPEX USD 1.2bn (Patria; distinct from Veolia O&M).
Miss: balsa (WITS 2022–2025 / AIMA / Plantabal already dense).
Miss: nickel (DFC PNP LOI / BNDES / Centaurus Jaguar / Atlantic UG already).
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


# resources/water — Aguas Pacífico multipurpose desal plant CAPEX USD 1.2bn
A(
    {
        "id": "aguas_pacifico_desal_capex_1p2bn_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "other",
        "counterpart": "Aguas Pacífico / Patria Investments — Valparaíso multipurpose desal CAPEX",
        "country": "Chile",
        "asset": "Oct 2025 (La Tercera quoting Aguas Pacífico): multipurpose seawater desalination plant + aqueduct for Valparaíso/Metropolitan Regions has total investment USD 1,200 million; plant ~86% complete; COD targeted 1H 2026; 1,000 L/s product water; 100% renewable power for operations cited. Distinct from veolia_aguas_pacifico_om_2025 (Veolia O&M award only). Patria (NASDAQ: PAX) developed via infrastructure funds; Fund III→V sale closed early 2025.",
        "investment_type": "greenfield",
        "value": "1200000000",
        "currency": "USD",
        "value_usd": "1200000000",
        "fx_usd": "1",
        "fx_date": "2025-10-21",
        "year": "2025",
        "status": "active",
        "lat": "-32.73",
        "lon": "-71.42",
        "geo_note": "Puchuncaví desal plant, Valparaíso Region (project geography; approximate pin).",
        "evidence": "documented",
        "source_id": "latercera_aguas_pacifico_20251021",
        "note": "Actor: Aguas Pacífico / Patria Investments (Brazil-origin alt manager, NASDAQ: PAX) — other. La Tercera 21 Oct 2025. Complements Veolia O&M row with plant-level CAPEX.",
    },
    {
        "id": "aguas_pacifico_desal_capex_1p2bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "latercera_aguas_pacifico_20251021",
        "url": "https://www.latercera.com/pulso/noticia/aguas-pacifico-otorga-la-licitacion-de-la-primera-planta-desalinizadora-para-la-region-valparaiso-y-metropolitana-a-veolia/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "La iniciativa considera una inversión total de US$ 1.200 millones, donde Veolia hará un aporte a la puesta en marcha del proyecto. El estado de avance de la planta es 86% y la entrada en operaciones está programada para el primer semestre de 2026. … producción de 1.000 l/s de agua desalinizada … La firma, ligada al Fondo de Inversiones Internacional Patria Investments.",
        "note": "Opened La Tercera Pulso 21 Oct 2025.",
    },
    {
        "id": "latercera_aguas_pacifico_20251021",
        "type": "press",
        "chicago": "Carrizo, Emiliano. “Aguas Pacífico otorga la licitación de la primera planta desalinizadora para la Región Valparaíso y Metropolitana a Veolia.” La Tercera (Pulso), 21 October 2025.",
        "url": "https://www.latercera.com/pulso/noticia/aguas-pacifico-otorga-la-licitacion-de-la-primera-planta-desalinizadora-para-la-region-valparaiso-y-metropolitana-a-veolia/",
        "annotation": "Chilean press on Aguas Pacífico USD 1.2bn desal CAPEX and Veolia O&M award. Supports aguas_pacifico_desal_capex_1p2bn_2025.",
        "supports": ["aguas_pacifico_desal_capex_1p2bn_2025", "hunt_res_water"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

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

    for hid, note in {
        "hunt_res_balsa": "Cycle 44 thin_topup: miss (WITS/AIMA/Plantabal already dense).",
        "hunt_res_nickel": "Cycle 44 thin_topup: miss (DFC PNP / BNDES / Centaurus / Atlantic UG already).",
        "hunt_res_water": "Cycle 44 thin_topup: logged aguas_pacifico_desal_capex_1p2bn_2025 (USD 1.2bn).",
    }.items():
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
    print("Cycle 44 thin_topup added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
