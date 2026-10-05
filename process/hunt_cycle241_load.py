#!/usr/bin/env python3
"""Cycle 241 hunt: shuffle_seed=20261241; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261241).shuffle):
wind, balsa, water, other_renewables, copper, lithium, solar, engineering_epc,
power_plants_grid, fission_smr, niobium, graphite, bridges_roads, nickel,
port_ownership, port_cranes, building_materials, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes Solar Oriente USD 990m SEA submission;
  NEW Seven Seas Antigua WaaS BOOT SSWG USD 23m investment; honest residual.
PRC equal-budget: NEW CTG Brasil Ilha Solteira+Jupiá modernization R$1.5bn spent
  (within >R$3bn program to 2039).
Allied CapEx-fill: Acciona La Gina multipurpose hydro USD 108m dual (DOP award).
Skipped: Goldwind Sento Sé CapEx undisclosed; RAP/Huaxin–CSN/Xinhai MoU/Aldesa EUR;
  COP/CLP/PEN; holdovers unsigned; thin balsa/nickel/fission dry.
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


# 1. other_renewables / us — NEW AES Andes Solar Oriente USD 990m (PV+BESS SEA)
row_doc(
    "aes_andes_solar_oriente_990m_2024",
    "energy", "other_renewables", "us",
    "AES Andes — Solar Oriente PV + BESS (Pozo Almonte / Tarapacá)",
    "Chile",
    "8 Sep 2024 AES Andes: submits Solar Oriente to SEA — investment of US$990 million for 581 MW photovoltaic + 809 MW battery storage in Pozo Almonte, Tarapacá; part of three-project SEA package totaling US$3 billion (>1,700 MW PV + 2,400 MW BESS with Altos del Sol and Llanos del Sol). CapEx: enter USD 990m Solar Oriente face. Coded other_renewables for co-located storage-backed solar (same convention as Andes Solar III / Pampas+Cristales).",
    "990000000", "2024-09-08", "2024", "-20.26", "-69.79",
    "Pozo Almonte commune, Tarapacá Region (company geography; municipal pin).",
    "aes_andes_solar_oriente_sea_20240908",
    "The company reached this milestone yesterday with the submission to the Environmental Evaluation Service (SEA) of its Solar Oriente project, which involves an investment of US$990 million for an installed capacity of 581 MW photovoltaic and 809 MW of storage in the commune of Pozo Almonte, Tarapacá Region.",
    "https://www.aesandes.com/en/press-release/aes-andes-submits-new-renewable-project-sea-and-reaches-us3-billion-photovoltaic",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW row: company English SEA submission CapEx USD 990m. Distinct from aes_andes_pampas_cristales_2025 / Andes Solar III hub. Shuffle other_renewables / U.S. ≥1/3 budget.",
    "hunt_cycle241", investment_type="greenfield_storage", evidence="documented", currency="USD",
    value_usd="990000000", fx_usd="1",
    chicago='AES Andes. “AES Andes submits a new renewable project to SEA and reaches US$3 billion in photovoltaic parks with battery storage.” September 8, 2024. https://www.aesandes.com/en/press-release/aes-andes-submits-new-renewable-project-sea-and-reaches-us3-billion-photovoltaic.',
    annotation="AES Solar Oriente NEW USD 990m. Supports aes_andes_solar_oriente_990m_2024.",
    evid_note="Opened AES Andes English; US$990m / 581 MW PV + 809 MW BESS / Pozo Almonte SEA confirmed.",
)

# 2. water / us — NEW Seven Seas Antigua WaaS BOOT SSWG USD 23m investment
row_doc(
    "seven_seas_antigua_waas_23m_2024",
    "resources", "water", "us",
    "Seven Seas Water Group — Antigua dual SWRO WaaS BOOT (Ffryes + Barnacle Point)",
    "Antigua and Barbuda",
    "12 Mar 2024 Antigua News: APUA signs agreement with Seven Seas Water Group (SSWG) for two new SWRO plants (Ffryes Beach + Ivan Rodrigues/Barnacle Point) adding ~3 million gallons/day; overall project ~USD 80 million with SSWG investing approximately US$23 million and APUA EC$15 million civil works. CapEx: enter SSWG USD 23m investment face. Envelope for seven_seas_ffryes / barnacle_point plant COD rows (nested; CapEx blank on company COD pages).",
    "23000000", "2024-03-12", "2024", "17.045", "-61.886",
    "Ffryes Beach / Barnacle Point dual-plant Antigua WaaS package (Ffryes pin).",
    "antigua_news_seven_seas_waas_20240312",
    "The overall project cost is estimated to be around $80 million, with SSWG investing approximately US$23 million (EC$62.1 million) and APUA investing an additional EC$15 million for the civil works associated with the project.",
    "https://antigua.news/2024/03/12/multi-million-dollar-water-agreement-signed-between-apua-and-seven-seas/",
    "Actor: Seven Seas Water Group (Tampa/Houston, U.S.) — us. NEW package CapEx USD 23m SSWG investment (press citing parties). Distinct from plant-level COD rows without CapEx. Shuffle water / U.S. ≥1/3 budget.",
    "hunt_cycle241", investment_type="concession", evidence="press", currency="USD",
    value_usd="23000000", fx_usd="1", bib_type="press",
    chicago='Antigua News. “Multi-million dollar water agreement signed between APUA and Seven Seas.” March 12, 2024. https://antigua.news/2024/03/12/multi-million-dollar-water-agreement-signed-between-apua-and-seven-seas/.',
    annotation="Seven Seas Antigua WaaS NEW USD 23m SSWG investment (press). Supports seven_seas_antigua_waas_23m_2024.",
    evid_note="Opened Antigua News English; ~USD 80m overall / SSWG US$23m / dual plants confirmed. CapEx enter USD 23m SSWG face.",
)

# 3. power_plants_grid / prc — NEW CTG Ilha Solteira+Jupiá modernization R$1.5bn spent
row_doc(
    "ctg_ilha_jupia_mod_1p5bn_spent_2026",
    "energy", "power_plants_grid", "prc",
    "CTG Brasil — Ilha Solteira + Jupiá modernization CapEx already spent",
    "Brazil",
    "1–3 Jul 2026 CTG Brasil 10-year concession anniversary press: Ilha Solteira + Jupiá form Brazil’s largest hydro modernization program — 34 generating units by 2039 with investment exceeding R$3 billion; of which R$1.5 billion already applied and 12 units delivered. CapEx: enter R$1.5bn spent face; Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~288.90m. Distinct from ctg_ilha_solteira_ug1_2026 unit COD milestone (CapEx blank).",
    "1500000000", BRL_FX_DATE, "2026", "-20.38", "-51.36",
    "UHE Ilha Solteira (SP–MS) / program also covers UHE Jupiá (Ilha Solteira pin).",
    "ilha_news_ctg_ilha_solteira_1p5bn_20260703",
    "Ilha Solteira e Jupiá concentram o maior programa de modernização de usinas hidrelétricas em andamento no Brasil. Até 2039, serão modernizadas 34 unidades geradoras, com investimento superior a R$ 3 bilhões. Deste total, R$ 1,5 bilhão já foi aplicado e 12 unidades foram entregues.",
    "https://ilha.news/ctg-brasil-celebra-10-anos-de-concessao-da-uhe-ilha-solteira/",
    "Actor: CTG Brasil / China Three Gorges — prc. NEW CapEx spent face R$1.5bn (UNVERIFIED proxy local press citing CTG anniversary). Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle241", investment_type="modernization", evidence="proxy", currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Mariano, Rodrigo. “CTG Brasil celebra 10 anos de concessão da UHE Ilha Solteira.” Ilha News, July 3, 2026. https://ilha.news/ctg-brasil-celebra-10-anos-de-concessao-da-uhe-ilha-solteira/.',
    annotation="CTG Ilha+Jupiá mod NEW R$1.5bn spent ~USD 288.90m via Fed H.10 (proxy). Supports ctg_ilha_jupia_mod_1p5bn_spent_2026.",
    evid_note="Opened Ilha News Portuguese; R$1.5bn already applied / >R$3bn to 2039 / 12 units delivered confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. other_renewables / allied — CapEx-fill Acciona La Gina USD 108m dual
row_doc(
    "acciona_la_gina_dr_2026",
    "energy", "other_renewables", "allied",
    "Consorcio A&H Presa La Gina (Acciona Construcción / Acciona Infraestructuras México / Hage) — La Gina multipurpose hydro",
    "Dominican Republic",
    "19 May 2026 Compras Dominicana award DO1.AWD.1951818: Consorcio A&H Presa La Gina (Acciona Construcción / Acciona Infraestructuras México / Hage) — 45-month construction of Aprovechamiento Múltiple Cuenca Alta Río Baní / Presa La Gina (Peravia); award value DOP 6,362,123,311.24. CapEx-fill: enter BNamericas dual US$108 million for that DOP award face (UNVERIFIED press FX dual). Irrigation/drinking water + hydro generation.",
    "108000000", "2026-05-19", "2026", "18.45", "-70.45",
    "Upper Baní River basin, Peravia province (EGEHID / Compras Dominicana tender).",
    "bnamericas_acciona_la_gina_108m_20260529",
    "The winner of the 45-month contract, with a score of 99.02 points, is Consorcio A&H La Gina (Acciona Construcción- Acciona Infraestructuras México-Hage Constructora), which submitted an offer of 6.36bn pesos (US$108mn).",
    "https://www.bnamericas.com/en/news/acciona-lands-dominican-hydro-project-with-us108mn-bid",
    "Actor: Consorcio A&H — Acciona (Spain) + Hage — allied. CapEx-fill: enter USD 108m dual for stored DOP award (retain DOP face in note; USD from BNamericas paraphrase). Runner-up included PowerChina. Shuffle other_renewables.",
    "hunt_cycle241", investment_type="epc", evidence="proxy", currency="USD",
    value_usd="108000000", fx_usd="1", bib_type="press",
    chicago='BNamericas. “Acciona lands Dominican hydro project with US$108mn bid.” May 29, 2026. https://www.bnamericas.com/en/news/acciona-lands-dominican-hydro-project-with-us108mn-bid.',
    annotation="Acciona La Gina CapEx-fill USD 108m dual (proxy). Supports acciona_la_gina_dr_2026.",
    evid_note="Opened BNamericas English; DOP 6.36bn / US$108mn dual / Acciona consortium / 45-month confirmed. CapEx-fill enter USD 108m; DOP award retained on Compras Dominicana prior source.",
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
    print(f"cycle241 added {len(added)}: {added}")
    print(f"cycle241 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
