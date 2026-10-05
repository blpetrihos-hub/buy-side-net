#!/usr/bin/env python3
"""Cycle 236 hunt: shuffle_seed=20261236; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261236).shuffle):
graphite, lithium, nickel, bridges_roads, other_renewables, niobium, balsa, port_cranes,
port_ownership, building_materials, water, copper, wind, power_plants_grid, fission_smr,
solar, rail, engineering_epc.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: honest residual Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/
Nextracker/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted after cycle 235 fills).
PRC equal-budget: Danasun Choloma CapEx-fill (proxy).
NEW: Colas Rail Santiago L9 electrical/SCADA EUR 104m; Colas/VINCI Alameda–Melipilla
S2 EUR 100m.
Skipped: RAP-as-CapEx; Huaxin–CSN; Xinhai MoU; Aldesa EUR; Goldwind Sento Sé (no
contract USD); COP/CLP/PEN (no Fed H.10).
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

EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"
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


# 1. NEW rail / allied — Colas Rail Santiago Metro Line 9 electrical/SCADA ~EUR 104m
row_doc(
    "colas_santiago_l9_electrical_scada_104m_eur_2026",
    "infrastructure", "rail", "allied",
    "Colas Rail — Santiago Metro Line 9 electrical systems + SCADA",
    "Chile",
    "24 Jun 2026 Colas: awarded approximately EUR 104 million for design, supply, installation and commissioning of electrical systems and associated SCADA for future Santiago Metro Line 9; includes distribution center, eight rectifier substations, thirty-nine lighting/power units, SCADA for power/traction, and 20-year maintenance. CapEx: Fed H.10 Sep 25 2026 EUR 1.1400 → USD 118.56m. Distinct from ohla_metro_santiago_l9_2026 civil works.",
    "104000000", EUR_FX_DATE, "2026", "-33.45", "-70.65",
    "Santiago Metro Line 9 corridor (company geography; Santiago pin).",
    "colas_santiago_l9_electrical_20260624",
    "Colas Rail (Colas) has been awarded the contract worth approximately 104 million euros* for the design, supply, installation and commissioning of the electrical systems and the associated SCADA (Supervisory Control and Data Acquisition) system.",
    "https://www.colas.com/en/press-releases/colas-has-secured-new-railway-contract-chile",
    "Actor: Colas Rail (France / Colas) — allied. NEW row: company English ~EUR 104m Line 9 electrical/SCADA. CapEx USD via Fed H.10 Sep 25 2026 1.1400. Shuffle rail.",
    "hunt_cycle236", investment_type="epc", evidence="documented", currency="EUR",
    value_usd=str(round(104000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='Colas. “Colas has secured a new railway contract in Chile.” June 24, 2026. https://www.colas.com/en/press-releases/colas-has-secured-new-railway-contract-chile.',
    annotation="Colas Santiago L9 electrical NEW ~USD 118.56m via Fed H.10. Supports colas_santiago_l9_electrical_scada_104m_eur_2026.",
    evid_note="Opened Colas English; ~EUR 104m / Line 9 electrical+SCADA / 20-year maintenance confirmed. CapEx USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 2. NEW rail / allied — Colas Rail / VINCI ETF Alameda–Melipilla S2 EUR 100m
row_doc(
    "colas_vinci_alameda_melipilla_s2_100m_eur_2025",
    "infrastructure", "rail", "allied",
    "Colas Rail / VINCI ETF — Alameda–Melipilla railway section 2",
    "Chile",
    "2 Jul 2025 Colas/VINCI: ETF (VINCI Construction lead) and Colas Rail selected by Dragados-Besalco to subcontract construction of the second stretch of Alameda–Melipilla railway for EFE; contract worth EUR 100 million split equally; 21.5 km; three new tracks with overhead lines; works from end-Aug 2025 for three years. CapEx: Fed H.10 Sep 25 2026 EUR 1.1400 → USD 114.00m. Distinct from crec7_alameda_melipilla_depot_90m_2025 (PRC depot).",
    "100000000", EUR_FX_DATE, "2025", "-33.55", "-70.90",
    "Alameda–Melipilla section 2 corridor (company geography).",
    "colas_vinci_alameda_melipilla_20250702",
    "The contract, which is worth €100 million, split equally between ETF and Colas Rail, involves three years of works, including in particular dismantling the existing track, providing the materials (track, sleepers, ballast and overhead lines, etc.), as well as the construction and commissioning of a new suburban railway line.",
    "https://www.colas.com/en/press-releases/consortium-vinci-construction-and-colas-wins-new-railway-contract-chile",
    "Actor: Colas Rail (France) + VINCI ETF (France) — allied. NEW row: company English EUR 100m Alameda–Melipilla S2. CapEx USD via Fed H.10 Sep 25 2026 1.1400. Shuffle rail.",
    "hunt_cycle236", investment_type="epc", evidence="documented", currency="EUR",
    value_usd=str(round(100000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='Colas. “A consortium of VINCI Construction and Colas wins a new railway contract in Chile.” July 2, 2025. https://www.colas.com/en/press-releases/consortium-vinci-construction-and-colas-wins-new-railway-contract-chile.',
    annotation="Colas/VINCI Alameda–Melipilla S2 NEW USD 114.00m via Fed H.10. Supports colas_vinci_alameda_melipilla_s2_100m_eur_2025.",
    evid_note="Opened Colas English; EUR 100m / 21.5 km S2 / 50-50 ETF–Colas confirmed. CapEx USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 3. building_materials / allied — CapEx-fill Holcim Pacasmayo ~USD 1.5bn EV
row_doc(
    "holcim_pacasmayo_complete_2026",
    "infrastructure", "building_materials", "allied",
    "Holcim — Cementos Pacasmayo majority-stake acquisition",
    "Peru",
    "Holcim completes majority-stake acquisition of Cementos Pacasmayo; company announces transaction value of approximately USD 1.5 billion on a 100% basis (8.8x 2025 consensus EBITDA / 7.1x after ~USD 40m year-three synergies). CapEx-fill: enter company USD 1.5bn EV face. Distinct from holcim_pacasmayo_aspi_1850370k_pen_2026 (Inversiones ASPI share cash in PEN).",
    "1500000000", "2025-12-16", "2026", "-7.4", "-79.55",
    "Cementos Pacasmayo Peru footprint (company geography).",
    "holcim_pacasmayo_acquire_20251216",
    "The transaction value of approximately USD 1.5 billion on a 100% basis implies an 8.8x multiple on 2025 market consensus EBITDA, or 7.1x after expected run-rate synergies of around USD 40 million realized in year three.",
    "https://www.holcim.com/media/media-releases/holcim-to-acquire-majority-stake-cementos-pacasmayo",
    "Actor: Holcim (Switzerland) — allied. CapEx-fill: enter company USD 1.5bn 100% EV. Shuffle building_materials.",
    "hunt_cycle236", investment_type="acquisition", evidence="documented", currency="USD",
    value_usd="1500000000", fx_usd="1",
    chicago='Holcim. “Holcim to acquire majority stake in Cementos Pacasmayo.” December 16, 2025. https://www.holcim.com/media/media-releases/holcim-to-acquire-majority-stake-cementos-pacasmayo.',
    annotation="Holcim Pacasmayo CapEx-fill USD 1.5bn EV. Supports holcim_pacasmayo_complete_2026.",
    evid_note="Opened Holcim English announce; ~USD 1.5bn 100% EV confirmed. CapEx-fill enter USD 1.5bn.",
)

# 4. solar / prc — CapEx-fill Danasun Choloma ~USD 400m
row_doc(
    "danasun_choloma_solar_honduras_2024",
    "energy", "solar", "prc",
    "Danasun / Texhong — Choloma solar+BESS megaproject (~USD 400m)",
    "Honduras",
    "2024 MoU with ENEE / continuing through 2025–26: Danasun Energy Honduras (Texhong / Danasun Energy Hong Kong) develops Choloma (Cortés) solar park described as ~300 MW PV with 60 MW battery storage; authorities cite ~USD 400 million Chinese-backed solar megaproject. CapEx-fill: enter stated ~USD 400m proxy face.",
    "400000000", "2024-01-01", "2024", "15.61", "-87.95",
    "Choloma, Cortés (press geography).",
    "expediente_danasun_choloma_2024",
    "The project is being developed by Danasun Energy Honduras S.A. de C.V., a subsidiary of the Chinese textile conglomerate Texhong International Group Ltd. … promoting a US$400 million Chinese-backed solar megaproject … plant’s projected capacity—300 MW with 60 MW of battery storage",
    "https://www.expedientepublico.org/asfura-government-withholds-key-details-of-chinese-solar-megaproject-amid-transparency-concerns/",
    "Actor: Danasun/Texhong (PRC/HK) — prc. CapEx-fill: enter ~USD 400m. UNVERIFIED proxy (contract texts not released). Shuffle solar / PRC equal-budget.",
    "hunt_cycle236", investment_type="greenfield", evidence="proxy", currency="USD",
    value_usd="400000000", fx_usd="1", bib_type="press",
    chicago='Expediente Público. “Asfura government withholds key details of Chinese solar megaproject amid transparency concerns.” 2024. https://www.expedientepublico.org/asfura-government-withholds-key-details-of-chinese-solar-megaproject-amid-transparency-concerns/.',
    annotation="Danasun Choloma CapEx-fill USD 400m (proxy). Supports danasun_choloma_solar_honduras_2024.",
    evid_note="Opened Expediente Público English; ~USD 400m / 300 MW+60 MW BESS Choloma cited. CapEx-fill enter USD 400m proxy.",
)

# 5. power_plants_grid / allied — CapEx-fill ISA IE Madeira 49% R$1.167bn
row_doc(
    "isa_energia_ie_madeira_49pct_1167m_2026",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — IE Madeira 49% equity acquisition (R$1.167bn)",
    "Brazil",
    "31 Jul 2026 AXIA Energia material fact: unwinding of cross-holdings with ISA Energia Brasil — sale of 49% equity in Interligação Elétrica do Madeira S.A. to ISA; AXIA receives net proceeds R$1.167 billion; ISA consolidates 100% of IE Madeira (2,385 km HVDC Porto Velho–Araraquara). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~224.76m.",
    "1167000000", BRL_FX_DATE, "2026", "-8.76", "-63.90",
    "IE Madeira HVDC Porto Velho–Araraquara (Porto Velho pin).",
    "axia_ie_madeira_unwind_20260731",
    "further to the material fact disclosed on March 19, 2026, and following the satisfaction of the applicable conditions precedent, they have completed, on this date, the unwinding of cross-holdings with ISA Energia Brasil S.A. (\"ISA Energia\") in the special purpose entities (SPEs) Interligação Elétrica do Madeira S.A. (\"IE Madeira\") and Interligação Elétrica Garanhuns S.A. (\"IE Garanhuns\"), through: i. The sale of the 49% equity interests held by AXIA Energia and AXIA Nordeste in IE Madeira to ISA Energia; ii. the acquisition by AXIA Nordeste of the 51% equity interest held by ISA Energia Brasil in IE Garanhuns; and iii. the receipt of net proceeds in the amount of R$1.167 billion.",
    "https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Material%20Fact%20-%20Unwinding%20of%20cross-holdings%20in%20transmission%20assets.pdf",
    "Actor: ISA Energia Brasil (Colombian ISA) — allied. CapEx-fill: retain R$1.167bn net proceeds face; add Fed H.10 Sep 25 2026 FX to USD ~224.76m. Shuffle power_plants_grid.",
    "hunt_cycle236", investment_type="acquisition", evidence="documented", currency="BRL",
    value_usd=str(round(1167000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='AXIA Energia. “Material Fact — Unwinding of cross-holdings in transmission assets.” July 31, 2026. https://www.latibex.com/docs/Documentos/esp/hechosrelev/2026/Material%20Fact%20-%20Unwinding%20of%20cross-holdings%20in%20transmission%20assets.pdf.',
    annotation="ISA IE Madeira CapEx-fill ~USD 224.76m via Fed H.10. Supports isa_energia_ie_madeira_49pct_1167m_2026.",
    evid_note="Opened AXIA Latibex English; R$1.167bn / 49% IE Madeira to ISA confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. graphite / allied — CapEx-fill South Star Santa Cruz Phase 1 CapEx presence (company dual if in asset)
# Skip - no verified CapEx figure on opened company primary this pass.

# 6. bridges_roads — thin top-up miss; holdovers unsigned.


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
    print(f"cycle236 added {len(added)}: {added}")
    print(f"cycle236 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
