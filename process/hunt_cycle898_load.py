#!/usr/bin/env python3
"""Cycle 898 hunt: shuffle_seed=20261898; Haiti PIP FY2025–26 CapEx faces.

Shuffle: lithium, solar, water, bridges_roads, balsa, port_ownership, copper,
building_materials, engineering_epc, rail, fission_smr, niobium, other_renewables,
power_plants_grid, graphite, wind, port_cranes, nickel.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry (Bechtel QB2 /
AES Arenales CapEx still blank; USACE/DFC/EXIM dense).
OTHER/ALLIED: NEW Haiti PIP FY2025–26 faces (HTG; USD blank — no Fed H.10 HTG).
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

PIP_URL = "https://docs.haitidocs.org/mpce-pip-2025-2026-adopte-cdm.pdf"
PIP_SID = "haiti_mpce_pip_fy2025_2026"
PIP_CHICAGO = (
    "République d'Haïti, Ministère de la Planification et de la Coopération Externe. "
    "“Programmes d'Investissements Publics — Exercice 2025-2026.” Budget Général de la "
    f"République d'Haïti. Retrieved October 5, 2026. {PIP_URL}."
)


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
            "pair_id": "",
            "counterpart_side": "",
            "counterpart_actor": "",
            "counterpart_value": "",
            "counterpart_currency": "",
            "counterpart_value_usd": "",
            "gap": "",
        },
        {
            "id": rid,
            "retrieved": "2026-10-05",
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
            "accessed": "2026-10-05",
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. bridges_roads / other — FINALISATION DU MAILLAGE ROUTIER NATIONAL
row_doc(
    "haiti_pip_maillage_routier_9625m_htg_fy2526",
    "infrastructure",
    "bridges_roads",
    "other",
    "MTPTC — Finalisation du maillage routier national (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line FINALISATION DU MAILLAGE ROUTIER NATIONAL under MTPTC "
    "Programme de mise en place du réseau de transport national: Trésor 633,740,000 HTG "
    "+ multilatéral 8,991,040,000 HTG = TOTAL PIP 9,624,780,000 HTG for FY2025–26. "
    "CapEx: enter FY PIP face (HTG; USD blank — no Fed H.10 HTG). Distinct from "
    "wb_haiti_resilient_corridors_80m_2025 / idb_haiti_les_cayes_rn2_69m_2026.",
    "9624780000",
    "",
    "2025",
    "",
    "",
    "Haiti national road-network completion program (PIP geography multi-corridor) — lat/lon blank.",
    PIP_SID,
    "FINALISATION DU MAILLAGE ROUTIER NATIONAL               633,740,000                                -              633,740,000                              -                  8,991,040,000        8,991,040,000          9,624,780,000",
    PIP_URL,
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF (haitidocs mirror). "
    "FY face HTG; USD blank (no Fed H.10 HTG). Shuffle bridges_roads; Haiti under-covered; "
    "≥1/3 US hunt CapEx dry.",
    "hunt_cycle898",
    investment_type="capex",
    evidence="documented",
    currency="HTG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: Maillage routier TOTAL PIP 9,624,780,000 HTG. Supports haiti_pip_maillage_routier_9625m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; Maillage routier TOTAL PIP column G.",
)

# 2. port_ownership / other — CONSTRUCTION D'UN DEBARCADERE A FORT-LIBERTE
row_doc(
    "haiti_pip_debarcadere_fort_liberte_160m_htg_fy2526",
    "infrastructure",
    "port_ownership",
    "other",
    "MTPTC — Construction d'un débarcadère à Fort-Liberté (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 11141-1-25-32-11 CONSTRUCTION D'UN DEBARCADERE A FORT-LIBERTE "
    "(Nord-Est): Trésor / ressources nationales 160,000,000 HTG = TOTAL PIP 160,000,000 HTG. "
    "CapEx: enter FY PIP face (HTG; USD blank — no Fed H.10 HTG). Distinct from "
    "pc_terminals_port_royal_haiti_60m_2025 / Chinourette envelope (private PPP, nearby Nord-Est).",
    "160000000",
    "",
    "2025",
    "19.668",
    "-71.838",
    "Fort-Liberté, Nord-Est Department, Haiti (PIP localisation; approximate municipal pin).",
    PIP_SID,
    "11141-1-25-32-11- CONSTRUCTION D'UN DEBARCADERE A FORT-LIBERTE NORD-EST               160,000,000                                -              160,000,000                              -                                      -                               -               160,000,000",
    PIP_URL,
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; "
    "USD blank. Shuffle port_ownership; Haiti under-covered; ≥1/3 US hunt CapEx dry.",
    "hunt_cycle898",
    investment_type="greenfield",
    evidence="documented",
    currency="HTG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: Debarcadère Fort-Liberté 160,000,000 HTG. Supports haiti_pip_debarcadere_fort_liberte_160m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; Fort-Liberté débarcadère TOTAL PIP.",
)

# 3. water / allied — PROJET EAU POTABLE ET ASSAINISSEMENT III (HA-L1103)
row_doc(
    "haiti_pip_dinepa_hal1103_1608m_htg_fy2526",
    "resources",
    "water",
    "allied",
    "IDB / DINEPA — Eau potable et assainissement III HA-L1103 (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 1114-2-22-50-56 PROJET EAU POTABLE ET ASSAINISSEMENT III (HA-L1103): "
    "multilatéral BID DON 1,608,000,000 HTG = TOTAL PIP 1,608,000,000 HTG for FY2025–26 under "
    "DINEPA. CapEx/financing FY face (HTG; USD blank — no Fed H.10 HTG). Distinct from "
    "usaid_haiti_wash_41p8m_2017 and nested under DINEPA programme envelope (not loaded as parent).",
    "1608000000",
    "",
    "2025",
    "",
    "",
    "Haiti national DINEPA HA-L1103 WASH program — lat/lon blank (national package).",
    PIP_SID,
    "1114-2-22-50-56- PROJET EAU POTABLE ET ASSAINISSEMENT III (HA-L1103) NATIONAL                                -                                  -                                -                                -                  1,608,000,000  BID  DON        1,608,000,000          1,608,000,000",
    PIP_URL,
    "Actor: IDB (BID) grant via DINEPA — allied multilateral. Official MPCE PIP PDF. "
    "FY face HTG; USD blank. Shuffle water; Haiti under-covered; ≥1/3 US hunt CapEx dry.",
    "hunt_cycle898",
    investment_type="financing",
    evidence="documented",
    currency="HTG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: HA-L1103 BID 1,608,000,000 HTG. Supports haiti_pip_dinepa_hal1103_1608m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; HA-L1103 TOTAL PIP / BID DON.",
)

# 4. solar / allied — RENFORCEMENT CENTRALE SOLAIRE CARACOL (HA-G1060)
row_doc(
    "haiti_pip_caracol_solar_hag1060_171m_htg_fy2526",
    "energy",
    "solar",
    "allied",
    "IDB — Renforcement centrale solaire photovoltaïque Caracol HA-G1060 (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 1112-1-12-56-13 RENFORCEMENT DE LA CAPACITE DE LA CENTRALE SOLAIRE "
    "PHOTOVOLTAIQUE AU PARC INDUSTRIEL DE CARACOL (HA-G1060): multilatéral BID DON "
    "170,601,805 HTG = TOTAL PIP 170,601,805 HTG for FY2025–26. CapEx/financing FY face "
    "(HTG; USD blank — no Fed H.10 HTG). Distinct from ssangyong_caracol_solar_13p4mw_haiti_57m "
    "(project CapEx USD 57m) — this row is the FY PIP reinforcement appropriation face.",
    "170601805",
    "",
    "2025",
    "19.740",
    "-72.020",
    "Caracol Industrial Park solar plant, Nord-Est, Haiti (prior Caracol solar pin).",
    PIP_SID,
    "1112-1-12-56-13- RENFORCEMENT DE LA CAPACITE DE LA CENTRALE SOLAIRE PHOTOVOLTAIQUE AU PARC INDUSTRIEL DE CARACOL (HA-G1060) NATIONAL                                -                                  -                                -                                -                     170,601,805  BID  DON           170,601,805             170,601,805",
    PIP_URL,
    "Actor: IDB (BID) grant — allied multilateral. Official MPCE PIP PDF. FY reinforcement "
    "face HTG; USD blank. Shuffle solar; Haiti under-covered; ≥1/3 US hunt CapEx dry.",
    "hunt_cycle898",
    investment_type="financing",
    evidence="documented",
    currency="HTG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: HA-G1060 Caracol solar 170,601,805 HTG. Supports haiti_pip_caracol_solar_hag1060_171m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; HA-G1060 TOTAL PIP / BID DON.",
)

# 5. power_plants_grid / allied — EXPLOITATION DURABLE CENTRALE PELIGRE (HA-L1140)
row_doc(
    "haiti_pip_peligre_hal1140_1388m_htg_fy2526",
    "energy",
    "power_plants_grid",
    "allied",
    "IDB — Exploitation durable centrale électrique de Péligre HA-L1140 (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 1114-1-12-55-13 EXPLOITATION DURABLE DE LA CENTRALE ÉLECTRIQUE DE "
    "PELIGRE (HA-L1140): multilatéral BID DON 1,388,451,301 HTG = TOTAL PIP 1,388,451,301 HTG "
    "for FY2025–26 under MTPTC Programme d'accroissement de l'électricité. CapEx/financing "
    "FY face (HTG; USD blank — no Fed H.10 HTG). Distinct from route-de-déviation Péligre "
    "road line (bridges_roads treasury face, not loaded this cycle).",
    "1388451301",
    "",
    "2025",
    "18.900",
    "-72.000",
    "Centrale hydroélectrique de Péligre, Centre Department, Haiti (PIP localisation; approximate).",
    PIP_SID,
    "1114-1-12-55-13- EXPLOITATION DURABLE DE LA CENTRALE ÉLECTRIQUE DE PELIGRE (HA-L1140) CENTRE                                -                                  -                                -                                -                  1,388,451,301  BID  DON        1,388,451,301          1,388,451,301",
    PIP_URL,
    "Actor: IDB (BID) grant — allied multilateral. Official MPCE PIP PDF. FY face HTG; "
    "USD blank. Shuffle power_plants_grid; Haiti under-covered; ≥1/3 US hunt CapEx dry.",
    "hunt_cycle898",
    investment_type="financing",
    evidence="documented",
    currency="HTG",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: HA-L1140 Péligre 1,388,451,301 HTG. Supports haiti_pip_peligre_hal1140_1388m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; HA-L1140 TOTAL PIP / BID DON.",
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
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle898 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
