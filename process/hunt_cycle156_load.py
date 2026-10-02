#!/usr/bin/env python3
"""Cycle 156 hunt: shuffle_seed=20261156; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: port_cranes, power_plants_grid, copper, rail, niobium,
bridges_roads, wind, port_ownership, engineering_epc, building_materials,
other_renewables, fission_smr, lithium, balsa, water, graphite, nickel, solar.

Weight under-covered Caribbean (SVG, Trinidad, Bahamas, Cuba, Suriname, Panama).
PRC ahead by 11 — keep equal US/PRC budget without padding.
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


# 1. port_cranes / allied — Konecranes ESP.7 Port of Kingstown (first SVG row)
row_doc(
    "konecranes_kingstown_esp7_svg_2024",
    "infrastructure",
    "port_cranes",
    "allied",
    "Konecranes — Gottwald ESP.7 MHC for St. Vincent and the Grenadines Port Authority (Kingstown)",
    "Saint Vincent and the Grenadines",
    "14 Aug 2024 Konecranes: in Q2 2024 SVGPA ordered a Gottwald ESP.7 Generation 6 mobile harbor crane for Port of Kingstown new terminal (opening Q1 2025); up to 51 m radius / 125 t; mains-electric capable; relocates existing Gen 5 crane. CapEx USD not disclosed. First Saint Vincent and the Grenadines observation.",
    "",
    "",
    "2024",
    "13.156",
    "-61.225",
    "Port of Kingstown, Saint Vincent (new terminal MHC).",
    "konecranes_kingstown_esp7_20240814",
    "In Q2 2024, the St. Vincent and the Grenadines Port Authority (SVGPA) ordered a Konecranes Gottwald ESP.7 Mobile Harbor Crane to boost container and general cargo handling capacity in the Port of Kingstown. This new Generation 6 machine will join their existing Konecranes Gottwald mobile harbor crane in a new terminal, opening in Q1 2025 … The Konecranes Gottwald ESP.7 Mobile Harbor Crane has a working radius of up to 51 m and a maximum capacity of 125 t",
    "https://www.konecranes.com/press-releases/caribbean-port-extends-capacity-with-konecranes-gottwald-generation-6-mobile-harbor-crane",
    "Actor: Konecranes (Nasdaq Helsinki / Finland HQ) — allied. Company English primary. CapEx blank. Undersampled SVG (prior n=0).",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Konecranes. “Caribbean port extends capacity with Konecranes Gottwald Generation 6 Mobile Harbor Crane.” August 14, 2024. https://www.konecranes.com/press-releases/caribbean-port-extends-capacity-with-konecranes-gottwald-generation-6-mobile-harbor-crane.',
    annotation="Konecranes primary: SVGPA ESP.7 order for Port of Kingstown. Supports konecranes_kingstown_esp7_svg_2024.",
    evid_note="Opened Konecranes English release 14 Aug 2024 (Kingstown ESP.7 Q2 2024 order).",
)

# 2. port_ownership / us — EXIM Liwathon BOS South Riding Point Bahamas
row_doc(
    "exim_liwathon_bos_bahamas_71p3m_2023",
    "infrastructure",
    "port_ownership",
    "us",
    "U.S. EXIM — Liwathon B.O.S. South Riding Point energy terminal loan guarantee (>USD 71.3m)",
    "Bahamas",
    "16 Oct 2023 Liwathon / EXIM: Board of Directors approved final-commitment loan guarantee exceeding USD 71.3 million to support relaunch of the 1.1 million m³ South Riding Point energy terminal (Grand Bahama) operated by Liwathon B.O.S. LLC; among largest EXIM CARICOM commitments. Face value = guarantee floor stated on company page.",
    "71300000",
    "2023-10-16",
    "2023",
    "26.616",
    "-78.233",
    "South Riding Point / Grand Bahama, Bahamas (1.1 million m³ energy terminal).",
    "liwathon_exim_bos_bahamas_20231016",
    "Liwathon Group … announce that the Board of Directors of the Export-Import Bank of the United States (EXIM) has approved a final commitment loan guarantee exceeding $71.3 million. This significant financial backing will support the relaunch of the 1.1 million m3 South Riding Point energy terminal in the Bahamas later this year, operated by Liwathon B.O.S. LLC. The loan guarantee marks one of the largest financial commitments by EXIM for a project in The Caribbean Community (CARICOM).",
    "https://www.liwathon.com/post/liwathon-receives-loan-guarantee-from-exim-for-the-relaunch-of-liwathon-b-o-s-terminal-in-bahamas",
    "Actor: U.S. EXIM financing (guarantee) for Liwathon BOS Bahamas terminal — us. Company English primary citing EXIM Board approval. Distinct from exim_focol_bahamas_99p6m_2025 / exim_bahamas_lng_99m_2025.",
    "hunt_infra_port_ownership",
    investment_type="financing",
    bib_type="company",
    chicago='Liwathon Group. “Liwathon Receives Loan Guarantee from EXIM for the Relaunch of Liwathon B.O.S. Terminal in Bahamas.” October 16, 2023. https://www.liwathon.com/post/liwathon-receives-loan-guarantee-from-exim-for-the-relaunch-of-liwathon-b-o-s-terminal-in-bahamas.',
    annotation="Liwathon primary: EXIM >USD 71.3m guarantee for South Riding Point terminal. Supports exim_liwathon_bos_bahamas_71p3m_2023.",
    evid_note="Opened Liwathon English release 16 Oct 2023 (EXIM >USD 71.3m South Riding Point).",
)

# 3. water / us — EXIM Trinidad and Tobago USD 500m MOU
row_doc(
    "exim_trinidad_mou_500m_2024",
    "resources",
    "water",
    "us",
    "U.S. EXIM — Trinidad and Tobago MOU (USD 500m; renewable energy / water sanitation)",
    "Trinidad and Tobago",
    "20 Jun 2024 EXIM: Chair Lewis signs USD 500 million MOU with Trinidad and Tobago (Minister of Finance Colm Imbert) covering maritime domain awareness, cybersecurity, renewable energy, and water sanitation; also USD 150m LOI for maritime vessels/aircraft (not dual-entered). Face value = MOU ceiling.",
    "500000000",
    "2024-06-18",
    "2024",
    "10.650",
    "-61.520",
    "Port of Spain, Trinidad (MOU signing).",
    "exim_trinidad_mou_20240620",
    "Export-Import Bank of the United States (EXIM) President and Chair Reta Jo Lewis … signed a US$500 million Memorandum of Understanding (MOU) for the Republic of Trinidad and Tobago with Minister of Finance and the Economy Colm Imbert. The MOU will develop opportunities and support financing in the maritime domain awareness, cybersecurity, renewable energy, and water sanitation sectors.",
    "https://www.exim.gov/news/export-import-bank-chair-lewis-signs-500-million-memorandum-understanding-republic-trinidad",
    "Actor: U.S. EXIM — us. Official EXIM English primary. Value = MOU ceiling (facility). Distinct from powerchina_malabar_wwtp_trinidad_2019 / powerchina_piarco_trinidad_2024.",
    "hunt_res_water",
    investment_type="financing",
    bib_type="official",
    chicago='Export-Import Bank of the United States. “Export-Import Bank of the U.S. Chair Lewis Signs $500 Million Memorandum of Understanding with the Republic of Trinidad & Tobago.” June 20, 2024. https://www.exim.gov/news/export-import-bank-chair-lewis-signs-500-million-memorandum-understanding-republic-trinidad.',
    annotation="EXIM primary: Trinidad and Tobago MOU USD 500m (incl. water sanitation). Supports exim_trinidad_mou_500m_2024.",
    evid_note="Opened EXIM English release 20 Jun 2024 (Trinidad MOU USD 500m).",
)

# 4. solar / us — AES Panama Los Santos 8 MW
row_doc(
    "aes_panama_los_santos_8mw_2025",
    "energy",
    "solar",
    "us",
    "AES Panamá — Los Santos Solar (8 MW; 49% AES ownership)",
    "Panama",
    "7 Aug 2026 AES Corporation Q2 2026 Fact Sheet lists Los Santos Panama Solar at 8 MW nameplate with 49% AES ownership, commercial-operation year 2025, and offtakers ENSA/Edemet/Edechi (through 2030). CapEx USD not on fact sheet. Distinct from aes_panama_corotu_10mw_2025 and prior AES Pesé/Mayorca/Cedro/Caoba rows.",
    "",
    "",
    "2025",
    "7.750",
    "-80.250",
    "Los Santos Province, Panama (Los Santos Solar site; approximate).",
    "aes_q2_2026_fact_sheet",
    "Los Santos Panama Solar 8 49% 2025 2030 ENSA, Edemet, Edechi, Other",
    "https://www.aes.com/sites/vault/files/2026-08/08-07-26%20Q2%202026%20Fact%20Sheet_FINAL.pdf",
    "Actor: AES Corporation / AES Panamá (U.S. HQ) — us. Company English fact sheet primary for 8 MW / COD year 2025. CapEx blank. Pairs with Corotú logged C155.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Corporation. “Q2 2026 Fact Sheet.” August 7, 2026. https://www.aes.com/sites/vault/files/2026-08/08-07-26%20Q2%202026%20Fact%20Sheet_FINAL.pdf.',
    annotation="AES Q2 2026 fact sheet: Los Santos Panama 8 MW COD year 2025. Supports aes_panama_los_santos_8mw_2025; aes_panama_corotu_10mw_2025.",
    evid_note="Opened AES Q2 2026 Fact Sheet PDF (Los Santos 8 MW / 49% / COD year 2025).",
)

# 5. solar / prc — PRC donation Mártires de Barbados II 5 MW Cuba
row_doc(
    "china_cuba_martires_barbados_ii_5mw_2025",
    "energy",
    "solar",
    "prc",
    "PRC government donation — PSFV Mártires de Barbados II (5 MW; Guanajay, Artemisa)",
    "Cuba",
    "12 Nov 2025 Radio Rebelde / Presidencia: President Díaz-Canel inaugurates Mártires de Barbados II solar park in Guanajay, Artemisa — seventh and closing park of first stage of PRC 120 MW donation (35 MW first stage / seven × ~5 MW); Chinese and Cuban firms recognized; phase 2 85 MW advancing. CapEx blank (donation). Distinct from shanghai_electric_castillo_agramonte_cuba_5mw_2026 (phase 2 with BESS).",
    "",
    "",
    "2025",
    "22.928",
    "-82.688",
    "Guanajay municipality, Artemisa, Cuba (Mártires de Barbados II PV site).",
    "radiorebelde_martires_barbados_ii_20251112",
    "Miguel Díaz-Canel Bermúdez, inauguró … el parque solar «Mártires de Barbados II», ubicado en el municipio Guanajuay, de la provincia de Artemisa, con el que concluye la primera etapa de instalación del donativo de la República Popular China equivalente, en sus dos partes, a 120 megawatts. … Con la conexión … ya generan siete instalaciones de esta primera fase del donativo … En el acto se reconocieron a las empresas chinas y cubanas que en menos de cuatro meses instalaron y conectaron el séptimo parque solar del donativo chino en su primera etapa de 35 megawatts.",
    "https://www.radiorebelde.cu/diaz-canel-inaugura-parque-solar-fruto-de-la-comunidad-de-futuro-compartido-con-china-12112025/",
    "Actor: PRC government donation / Chinese firms — prc. Official Cuban Radio Rebelde primary. CapEx blank (donation). Undersampled Cuba solar.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="official",
    chicago='Radio Rebelde. “Díaz-Canel inaugura parque solar, fruto de la Comunidad de Futuro Compartido con China.” November 12, 2025. https://www.radiorebelde.cu/diaz-canel-inaugura-parque-solar-fruto-de-la-comunidad-de-futuro-compartido-con-china-12112025/.',
    annotation="Radio Rebelde: Mártires de Barbados II closes PRC 35 MW first-stage donation. Supports china_cuba_martires_barbados_ii_5mw_2025.",
    evid_note="Opened Radio Rebelde Spanish 12 Nov 2025 (Mártires de Barbados II / PRC donation phase 1 close).",
)

# 6. solar / prc — POWERCHINA Kajana + Guyaba Suriname Phase II sites
row_doc(
    "powerchina_kajana_guyaba_suriname_2026",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Kajana (Site 3) and Guyaba (Site 9) micro-grid solar COD (Suriname Phase II)",
    "Suriname",
    "18 May 2026 POWERCHINA: President Jennifer Geerlings-Simons attends 3 May completion/unveiling/lighting of Sites 3 (Kajana) and 9 (Guyaba) of Suriname Villages Micro-grid Solar Project Phase II; with these CODs seven of nine Phase II sites handed over; portfolio 5.349 MW solar + 18.6 MWh storage + 2.813 MVA diesel. CapEx blank. Distinct from powerchina_djoemoe_suriname_2026 (Site/fourth station) and powerchina_suriname_microgrid_p2_2026 portfolio row.",
    "",
    "",
    "2026",
    "4.150",
    "-55.530",
    "Kajana / Guyaba corridor along Suriname River, Saramacca, Suriname (Phase II Sites 3 and 9; approximate river-corridor pin).",
    "powerchina_kajana_guyaba_20260518",
    "Jennifer Geerlings-Simons, president of Suriname, delivered a speech at the completion, unveiling, and lighting ceremonies for Sites 3 (Kajana) and 9 (Guyaba) of the Suriname Villages Micro-grid Solar Project Phase II, constructed by POWERCHINA, on May 3 … With the commissioning of Sites 3 and 9, a total of seven sites have been completed and handed over. The project … has a total installed capacity of 5.349 MW, with 18.6 MWh of energy storage and a diesel power generation capacity of 2.813 MVA.",
    "https://en.powerchina.cn/2026-05/18/c_829069.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary for named Kajana/Guyaba COD. CapEx blank. Named-site presence distinct from Djoemoe station row.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “Suriname\'s president attends micro-grid solar project commissioning ceremony.” May 18, 2026. https://en.powerchina.cn/2026-05/18/c_829069.htm.',
    annotation="POWERCHINA primary: Kajana (Site 3) and Guyaba (Site 9) Phase II COD. Supports powerchina_kajana_guyaba_suriname_2026.",
    evid_note="Opened POWERCHINA English 18 May 2026 (Kajana/Guyaba Sites 3 and 9 COD).",
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
    print(f"Cycle 156 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
