#!/usr/bin/env python3
"""Cycle 155 hunt: shuffle_seed=20261155; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: building_materials, power_plants_grid, fission_smr, graphite,
other_renewables, port_ownership, nickel, engineering_epc, copper, lithium, water,
wind, solar, balsa, rail, port_cranes, bridges_roads, niobium.

Weight toward under-covered countries (Caribbean / Central America / Cuba / Dominica /
Saint Kitts). PRC ahead by 13 — keep equal US/PRC budget without padding.
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


# 1. water / us — Seven Seas Ffryes Beach SWRO Antigua (1 IMGD)
row_doc(
    "seven_seas_ffryes_antigua_1migd_2025",
    "resources",
    "water",
    "us",
    "Seven Seas Water Group — Ffryes Beach SWRO desalination plant (1 IMGD BOOT)",
    "Antigua and Barbuda",
    "25 Mar 2025 Seven Seas Water Group (Tampa HQ): with APUA opens Ffryes Beach seawater reverse osmosis plant — 1 million imperial gallons/day; first of two WaaS plants under March 2024 12-year BOOT; second plant at Ivan Rodriguez targeted for Q3 2025 toward combined 3 IMGD. CapEx USD not disclosed on opened page.",
    "",
    "",
    "2025",
    "17.045",
    "-61.886",
    "Ffryes Beach, Antigua (desalination plant adjacent to existing APUA facility).",
    "seven_seas_ffryes_antigua_20250325",
    "The Antigua Public Utilities Authority (APUA) and Seven Seas Water Group (SSWG) … have jointly announced the opening of the Ffryes Beach seawater reverse osmosis (SWRO) desalination plant. The plant has a capacity of 1 million imperial gallons per day (IMGD) … This is the first of two SWRO plants that APUA and SSWG announced as part of their WaaS® agreement in March 2024. … Headquartered in Tampa, with operations across the U.S., Caribbean, and Latin America",
    "https://sevenseaswater.com/ffryes-beach-desalination-plant-delivered/",
    "Actor: Seven Seas Water Group (Tampa, Florida HQ) — us. Company English primary. CapEx blank (BOOT / WaaS). Distinct from liebherr_antigua_lhm420_2025. Undersampled Antigua.",
    "hunt_res_water",
    investment_type="concession",
    bib_type="company",
    chicago='Seven Seas Water Group. “Seven Seas Water Group and APUA Deliver Ffryes Beach Desalination Plant in Record Time.” March 25, 2025. https://sevenseaswater.com/ffryes-beach-desalination-plant-delivered/.',
    annotation="Seven Seas primary: Ffryes Beach Antigua 1 IMGD SWRO opening. Supports seven_seas_ffryes_antigua_1migd_2025.",
    evid_note="Opened Seven Seas English release 25 Mar 2025 (Ffryes Beach 1 IMGD SWRO COD).",
)

# 2. other_renewables / us — EXIM Saint Kitts and Nevis up to USD 300m MOU
row_doc(
    "exim_saint_kitts_mou_300m_2024",
    "energy",
    "other_renewables",
    "us",
    "U.S. EXIM — Saint Kitts and Nevis MOU (up to USD 300m; renewable energy / critical minerals / infrastructure)",
    "Saint Kitts and Nevis",
    "25 Nov 2024 EXIM: Chair Reta Jo Lewis signs MOU with Prime Minister Terrance Michael Drew providing access to up to USD 300 million in potential financing; areas for cooperation include renewable energy, cybersecurity, critical minerals and infrastructure. Face value = MOU ceiling (financing facility, not a closed project loan).",
    "300000000",
    "2024-11-25",
    "2024",
    "17.302",
    "-62.717",
    "Basseterre, Saint Kitts (MOU signing venue via U.S. Embassy Bridgetown host; host-country pin).",
    "exim_barbados_skn_mou_20241125",
    "The MOU between Saint Kitts and Nevis, providing access to up to $300 million in financing was signed by Chair Lewis and Prime Minister Terrance Michael Drew at the U.S. Embassy in Bridgetown … Areas for cooperation and procurement included renewable energy, cybersecurity, critical minerals and infrastructure.",
    "https://www.exim.gov/news/export-import-bank-signs-800-million-memoranda-understanding-barbados-and-saint-kitts-and",
    "Actor: U.S. Export-Import Bank — us. Official EXIM English primary. Value = MOU ceiling (facility; not a disbursed project). First Saint Kitts and Nevis observation. Distinct from EXIM FOCOL Bahamas / GTE Guyana closed loans.",
    "hunt_energy_other_renewables",
    investment_type="financing",
    evidence="documented",
    bib_type="official",
    chicago='Export-Import Bank of the United States. “Export-Import Bank of the U.S. Signs $800 Million Memoranda of Understanding with Barbados and Saint Kitts and Nevis Governments to Support Strategic Investments.” November 25, 2024. https://www.exim.gov/news/export-import-bank-signs-800-million-memoranda-understanding-barbados-and-saint-kitts-and.',
    annotation="EXIM primary: SKN MOU up to USD 300m (renewable energy / critical minerals / infrastructure). Supports exim_saint_kitts_mou_300m_2024; exim_barbados_mou_500m_2024.",
    evid_note="Opened EXIM English release 25 Nov 2024 (SKN MOU up to USD 300m).",
)

# 3. water / us — EXIM Barbados up to USD 500m MOU (renewable energy / water)
row_doc(
    "exim_barbados_mou_500m_2024",
    "resources",
    "water",
    "us",
    "U.S. EXIM — Barbados MOU (up to USD 500m; renewable energy / water and sanitation)",
    "Barbados",
    "25 Nov 2024 EXIM: Chair Lewis and Prime Minister Mia Mottley sign MOU for up to USD 500 million in financing; areas include renewable energy, cybersecurity, water and sanitation and maritime domain awareness. Face value = MOU ceiling (financing facility). Distinct from powerchina_barbados_water_infra_2025 / crseg_barbados_south_coast_water_2026.",
    "500000000",
    "2024-11-25",
    "2024",
    "13.097",
    "-59.616",
    "Bridgetown, Barbados (Office of the Prime Minister MOU signing).",
    "exim_barbados_skn_mou_20241125",
    "The MOU between EXIM and the government of Barbados, in the amount of up to $500 million in financing, was signed by Chair Lewis and Prime Minister Mia Mottley in the Office of the Prime Minister … Areas for cooperation and procurement included renewable energy, cybersecurity, water and sanitation and maritime domain awareness.",
    "https://www.exim.gov/news/export-import-bank-signs-800-million-memoranda-understanding-barbados-and-saint-kitts-and",
    "Actor: U.S. Export-Import Bank — us. Official EXIM English primary. Value = MOU ceiling (facility). Undersampled Barbados; pairs with PRC Barbadian water rows on opposite side.",
    "hunt_res_water",
    investment_type="financing",
    bib_type="official",
    chicago='Export-Import Bank of the United States. “Export-Import Bank of the U.S. Signs $800 Million Memoranda of Understanding with Barbados and Saint Kitts and Nevis Governments to Support Strategic Investments.” November 25, 2024. https://www.exim.gov/news/export-import-bank-signs-800-million-memoranda-understanding-barbados-and-saint-kitts-and.',
    annotation="EXIM primary: Barbados MOU up to USD 500m (incl. water and sanitation). Supports exim_barbados_mou_500m_2024; exim_saint_kitts_mou_300m_2024.",
    evid_note="Opened EXIM English release 25 Nov 2024 (Barbados MOU up to USD 500m).",
)

# 4. solar / us — AES Panama Corotú 10 MW (COD year 2025 on AES fact sheet)
row_doc(
    "aes_panama_corotu_10mw_2025",
    "energy",
    "solar",
    "us",
    "AES Panamá — Corotú Solar (10 MW; 49% AES ownership)",
    "Panama",
    "7 Aug 2026 AES Corporation Q2 2026 Fact Sheet lists Corotú Panama Solar at 10 MW nameplate with 49% AES ownership, commercial-operation year 2025, and offtakers ENSA/Edemet/Edechi (through 2030). CapEx USD not on fact sheet (BNamericas EIS press ~USD 10.9m UNVERIFIED — not used as CapEx). Distinct from powerchina_sajalices_panama_530mw_2024 and prior AES Pesé/Mayorca/Cedro/Caoba rows.",
    "",
    "",
    "2025",
    "8.505",
    "-82.570",
    "Boquerón district, Chiriquí, Panama (Corotú Solar site).",
    "aes_q2_2026_fact_sheet",
    "Corotú Panama Solar 10 49% 2025 2030 ENSA, Edemet, Edechi, Other",
    "https://www.aes.com/sites/vault/files/2026-08/08-07-26%20Q2%202026%20Fact%20Sheet_FINAL.pdf",
    "Actor: AES Corporation / AES Panamá (U.S. HQ) — us. Company English fact sheet primary for 10 MW / COD year 2025. CapEx blank. Undersampled relative to Chile AES Andes density.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Corporation. “Q2 2026 Fact Sheet.” August 7, 2026. https://www.aes.com/sites/vault/files/2026-08/08-07-26%20Q2%202026%20Fact%20Sheet_FINAL.pdf.',
    annotation="AES Q2 2026 fact sheet: Corotú Panama 10 MW COD year 2025. Supports aes_panama_corotu_10mw_2025.",
    evid_note="Opened AES Q2 2026 Fact Sheet PDF (Corotú 10 MW / 49% / COD year 2025).",
)

# 5. engineering_epc / prc — China Railway No.5 Dominica International Airport (Wesley)
row_doc(
    "crec5_dominica_intl_airport_wesley_2024",
    "infrastructure",
    "engineering_epc",
    "prc",
    "China Railway No.5 Engineering Group — Dominica International Airport Project (Wesley)",
    "Dominica",
    "8 Aug 2024 PRC MFA / Chinese Embassy in Dominica: Ambassador Chu Maoming inspects Dominica International Airport Project constructed by China Railway No.5 Engineering Group Co., Ltd. in Wesley (project GM Ma Zongyao). 29 Dec 2025 CREC English corroborates PM Skerrit inspection of Aggregate Quarry No. 2 for the same CR5 airport project (quarry production targeted Jan 2026). CapEx USD not on opened MFA/CREC pages (press figures conflict — left blank). Distinct from ormat_dominica_geothermal rows.",
    "",
    "",
    "2024",
    "15.547",
    "-61.300",
    "Wesley, Dominica (International Airport Project construction site).",
    "mfa_crec5_dominica_airport_20240808",
    "On August 7, Ambassador Chu Maoming inspected the International Airport Project constructed by China Railway No.5 Engineering Group Co., Ltd. in Wesley, accompanied by General Manager of the project Ma Zongyao … Ambassador Chu said that the International Airport Project is a key project of China-Dominica pragmatic cooperation",
    "https://www.fmprc.gov.cn/mfa_eng/xw/zwbd/202408/t20240812_11471253.html",
    "Actor: China Railway No.5 Engineering Group (CREC subsidiary / PRC SOE) — prc. Official MFA English primary; CREC English quarry inspection corroborates ongoing works. CapEx blank. Undersampled Dominica.",
    "hunt_infra_engineering_epc",
    investment_type="epc",
    bib_type="official",
    chicago='Ministry of Foreign Affairs of the People’s Republic of China. “Chinese Ambassador to Dominica Chu Maoming Inspects International Airport Project.” August 8, 2024. https://www.fmprc.gov.cn/mfa_eng/xw/zwbd/202408/t20240812_11471253.html.',
    annotation="PRC MFA: CR5 constructs Dominica International Airport at Wesley. Supports crec5_dominica_intl_airport_wesley_2024.",
    evid_note="Opened MFA English 8 Aug 2024 (CR5 Dominica airport inspection); CREC English 29 Dec 2025 quarry corroboration.",
)

# 6. solar / prc — Shanghai Electric / China donation Castillo Agramonte 5 MW + 1 MW BESS Cuba
row_doc(
    "shanghai_electric_castillo_agramonte_cuba_5mw_2026",
    "energy",
    "solar",
    "prc",
    "Shanghai Electric / PRC donation — PSFV General Ángel del Castillo Agramonte (5 MW + 1 MW BESS)",
    "Cuba",
    "30 Apr 2026 ACN: inaugurates General Ángel del Castillo Agramonte PV park in Majagua, Ciego de Ávila — 5 MW with 1 MW battery storage; first synchronized project of second stage of PRC 120 MW donation (85 MW with storage); ~17 Shanghai Electric specialists with UNE technicians; synchronized 25 Mar 2026. CapEx blank (government donation). Distinct from prior Cuba engineering_epc rows.",
    "",
    "",
    "2026",
    "21.924",
    "-78.922",
    "Majagua municipality, Ciego de Ávila, Cuba (Castillo Agramonte PV + BESS site).",
    "acn_castillo_agramonte_cuba_20260430",
    "Con una potencia de cinco megawatts (MW) y un sistema de acumulación en baterías de un MW, quedó inaugurado hoy en este municipio avileño el parque solar fotovoltaico General Ángel del Castillo Agramonte … primer proyecto sincronizado de la segunda etapa del donativo de 120 MW otorgado por el gobierno de la República Popular China … También en esta obra intervinieron unos 17 especialistas chinos de la compañía Shanghai Electric, junto a técnicos de la Unión Eléctrica de Cuba.",
    "https://www.acn.cu/economia/inauguran-en-ciego-de-avila-primer-parque-solar-con-baterias",
    "Actor: Shanghai Electric (PRC) + PRC government donation — prc. Official Cuban ACN primary names Shanghai Electric specialists and PRC donation. CapEx blank (donation). Undersampled Cuba energy layer.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="official",
    chicago='Agencia Cubana de Noticias. “Inauguran en Ciego de Ávila primer parque solar con baterías.” April 30, 2026. https://www.acn.cu/economia/inauguran-en-ciego-de-avila-primer-parque-solar-con-baterias.',
    annotation="ACN: Castillo Agramonte 5 MW + 1 MW BESS; Shanghai Electric / PRC 120 MW donation phase 2. Supports shanghai_electric_castillo_agramonte_cuba_5mw_2026.",
    evid_note="Opened ACN Spanish 30 Apr 2026 (Castillo Agramonte 5 MW + 1 MW BESS; Shanghai Electric).",
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
    print(f"Cycle 155 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
