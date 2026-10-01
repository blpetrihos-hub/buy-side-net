#!/usr/bin/env python3
"""Cycle 57 thin_topup: 3 thinnest after equal pass.

Post-equal thinnest (active+hunt, evidence documented|proxy|hunt):
niobium ~21, balsa ~21, graphite ~22.
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


# ---------------------------------------------------------------------------
# thin 1 resources/niobium — St George Araxá MRE upgrade Nb inventory (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "st_george_araxa_mre_upgrade_nb_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "St George Mining — Araxá MRE upgrade (Nb₂O₅ inventory)",
        "country": "Brazil",
        "asset": "11 Aug 2026 ASX: St George Mining announces upgraded JORC MRE for 100%-owned Araxá Nb–REE project (Minas Gerais) to 111.2 Mt @ 3.57% TREO and 0.57% Nb₂O₅ (contained ~630,000 t Nb₂O₅); Measured & Indicated 75.2 Mt @ 0.58% Nb₂O₅ (+155% vs prior). Company frames as largest undeveloped niobium Measured resource globally, adjacent CBMM district. Distinct from st_george_araxa_nb_2025 (acquisition), st_george_araxa_permitting_2026, and st_george_araxa_capex_brl3bn_2026.",
        "investment_type": "exploration_development",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá, Minas Gerais (Barreiro carbonatite district pin; approximate).",
        "evidence": "documented",
        "source_id": "stgeorge_araxa_mre_20260811",
        "note": "Actor: St George Mining (Australia) — allied. Resource upgrade observation; no CapEx on this ASX page.",
    },
    {
        "id": "st_george_araxa_mre_upgrade_nb_2026",
        "retrieved": "2026-10-01",
        "source_id": "stgeorge_araxa_mre_20260811",
        "url": "https://announcements.asx.com.au/asxpdf/20260811/pdf/072mjx9qmb4527.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The updated MRE has increased to 111.2Mt @ 3.57% TREO, 0.70% MREO, 0.68% NdPr and 0.57% Nb₂O₅ … The MRE now contains an estimated 3.98Mt of TREO – including 760,000t of NdPr oxides – as well as 630,000t of Nb₂O₅",
        "note": "Opened St George ASX PDF 11 Aug 2026 MRE upgrade.",
    },
    {
        "id": "stgeorge_araxa_mre_20260811",
        "type": "company",
        "chicago": "St George Mining Limited. “155% Increase in Measured & Indicated Araxá Resource.” ASX announcement, 11 August 2026.",
        "url": "https://announcements.asx.com.au/asxpdf/20260811/pdf/072mjx9qmb4527.pdf",
        "annotation": "ASX primary on Araxá MRE upgrade including 630 kt Nb₂O₅. Supports st_george_araxa_mre_upgrade_nb_2026.",
        "supports": ["st_george_araxa_mre_upgrade_nb_2026", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# thin 2 resources/balsa — DIAB Ecuador ProBalsa processing facility (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "diab_ecuador_probalsa_facility",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "DIAB — Ecuador ProBalsa end-grain processing facility",
        "country": "Ecuador",
        "asset": "DIAB Group product literature (ProBalsa brochure / company balsa pages): processing of raw balsa for ProBalsa end-grain core is carried out in DIAB’s own modern facility in Ecuador; DIAB Ecuador qualifies suppliers and administers harvesting/replanting ecology for wind-blade and marine core supply. Processor/plant-presence angle — distinct from Plantabal/3A, Gurit Balsaflex Quevedo, and CoreLite Balsasud. CapEx USD and exact municipal address not disclosed on opened pages.",
        "investment_type": "ownership_presence",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.45",
        "geo_note": "Ecuador balsa processing (coastal lowlands / Quevedo region pin; facility municipality not named on brochure — approximate).",
        "evidence": "documented",
        "source_id": "diab_probalsa_brochure",
        "note": "Actor: DIAB (Sweden) — allied. Company product brochure confirming owned Ecuador processing facility; CapEx not disclosed.",
    },
    {
        "id": "diab_ecuador_probalsa_facility",
        "retrieved": "2026-10-01",
        "source_id": "diab_probalsa_brochure",
        "url": "http://www.duroplastic.com/pdf/ProBalsa_Brochure.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Processing raw balsa wood is carried out in DIAB’s own modern facility in Ecuador. DIAB Ecuador also qualifies raw material suppliers and carries out the ecological administration of the balsa program. This includes working closely with suppliers regarding correct harvesting and subsequent re-planting programs to ensure the future availability of balsa.",
        "note": "Opened DIAB ProBalsa brochure PDF mirrored via Duroplastic distributor host.",
    },
    {
        "id": "diab_probalsa_brochure",
        "type": "company",
        "chicago": "DIAB Group. “ProBalsa — Technical Brochure.” Product literature (accessed 2026).",
        "url": "http://www.duroplastic.com/pdf/ProBalsa_Brochure.pdf",
        "annotation": "DIAB ProBalsa brochure stating owned Ecuador processing facility and supplier ecology program. Supports diab_ecuador_probalsa_facility.",
        "supports": ["diab_ecuador_probalsa_facility", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# thin 3 resources/graphite — South Star Santa Cruz June 2026 ramp (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "south_star_santa_cruz_june_ramp_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "South Star — Santa Cruz plant June 2026 ROM ramp / commercial flake production",
        "country": "Brazil",
        "asset": "22 Jul 2026 GlobeNewswire / company ops update: Santa Cruz (Bahia) plant ROM feed rose April→June 2026 (1,337.5 → 3,798.5 → 4,920.1 t); May→June ROM +~30% with concentrate output doubling; 100% of June concentrate met commercial specs at ~95% C flake; targeting 5,000 tpa concentrate ramp. Distinct from south_star_santa_cruz_restart_202604 (re-start) and south_star_santa_cruz_po_36t_2026 (36 t PO).",
        "investment_type": "brownfield_restart",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-16.58",
        "lon": "-39.58",
        "geo_note": "Santa Cruz Graphite Mine, southern Bahia (Itabela/Itagimirim district pin; approximate).",
        "evidence": "documented",
        "source_id": "southstar_santa_cruz_ops_20260722",
        "note": "Actor: South Star Battery Metals (Canada) — allied. Company ops update; CapEx not restated.",
    },
    {
        "id": "south_star_santa_cruz_june_ramp_2026",
        "retrieved": "2026-10-01",
        "source_id": "southstar_santa_cruz_ops_20260722",
        "url": "https://www.bnnbloomberg.ca/press-releases/2026/07/22/south-star-announces-santa-cruz-operational-update-first-shipment-of-graphite-shipped/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ROM feed increased substantially once again: April 2026: 1,337.5 tonnes May 2026: 3,798.5 tonnes June 2026: 4,920.1 tonnes … From May to June, ROM feed to the plant increased by approximately 30%, while graphite concentrate production doubled … The plant is being monitored regularly and consistently in order to attain a production capacity of 5,000 tpa of graphite concentrate.",
        "note": "Opened BNN Bloomberg mirror of South Star GlobeNewswire ops update 22 Jul 2026.",
    },
    {
        "id": "southstar_santa_cruz_ops_20260722",
        "type": "company",
        "chicago": "South Star Battery Metals Corp. “South Star Announces Santa Cruz Operational Update; First Shipment of Graphite Shipped.” GlobeNewswire / BNN Bloomberg, 22 July 2026.",
        "url": "https://www.bnnbloomberg.ca/press-releases/2026/07/22/south-star-announces-santa-cruz-operational-update-first-shipment-of-graphite-shipped/",
        "annotation": "Company ops update on Santa Cruz June 2026 ROM/concentrate ramp toward 5,000 tpa. Supports south_star_santa_cruz_june_ramp_2026.",
        "supports": ["south_star_santa_cruz_june_ramp_2026", "hunt_res_graphite"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
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

    hunt_updates = {
        "hunt_fenb_araxa": "Cycle 57 thin_topup: logged st_george_araxa_mre_upgrade_nb_2026 (allied).",
        "hunt_res_balsa": "Cycle 57 thin_topup: logged diab_ecuador_probalsa_facility (allied).",
        "hunt_res_graphite": "Cycle 57 thin_topup: logged south_star_santa_cruz_june_ramp_2026 (allied).",
    }
    for hid, note in hunt_updates.items():
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
    print("Cycle 57 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
