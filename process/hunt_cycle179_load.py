#!/usr/bin/env python3
"""Cycle 179 hunt: shuffle_seed=20261179; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261179)):
water, balsa, fission_smr, niobium, nickel, copper, other_renewables,
engineering_epc, building_materials, graphite, bridges_roads, power_plants_grid,
port_cranes, wind, solar, lithium, rail, port_ownership.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (Plantabal/AIMA/WITS Ecuador balsa; Centaurus/BRN/Atlantic/
Fenix nickel; Meitner/Colombia/Peru FIRST fission already logged).
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


# 1a. water / allied — ProInversión PTAR Puerto Maldonado (Mota-Engil consortium)
row_doc(
    "mota_engil_ptar_puerto_maldonado_150m_2025",
    "resources",
    "water",
    "allied",
    "Mota-Engil / BTD — PTAR Puerto Maldonado PPP concession (>USD 150m)",
    "Peru",
    "15 Dec 2025 (ProInversión): awards Consorcio Saneamiento Puerto Maldonado (Mota-Engil Perú S.A., Mota-Engil Capital S.A., BTD Capital 12 S.L.) the Puerto Maldonado wastewater treatment plant PPP — first jungle PTAR under APP; treat 100% of city wastewater; benefit >190,000 people; design/finance/build/O&M for 24-year concession; 192 km sewer networks; +20,000 household connections. Valued at more than USD 150 million. CapEx/concession face = USD 150m floor.",
    "150000000",
    "2025-12-15",
    "2025",
    "-12.59",
    "-69.19",
    "Puerto Maldonado / Tambopata, Madre de Dios (ProInversión geography; approximate city pin).",
    "proinversion_ptar_puerto_maldonado_20251215",
    "El proyecto, valorizado en más de US$ 150 millones, comprende el diseño, financiamiento, construcción, operación y mantenimiento del sistema por un periodo de concesión de 24 años. Incluye la instalación y rehabilitación de 192 kilómetros de redes primarias y secundarias de alcantarillado, la ampliación en 20 000 conexiones domiciliarias a la red de desagüe… adjudicado al Consorcio Saneamiento Puerto Maldonado…",
    "https://www.gob.pe/institucion/proinversion/noticias/1315940-gobierno-adjudica-ptar-puerto-maldonado-que-tratara-el-100-de-aguas-residuales-de-la-ciudad-en-beneficio-de-190-mil-personas",
    "Actor: Mota-Engil (Portugal) + BTD Capital (Spain) consortium — allied. Opened ProInversión Spanish release 15 Dec 2025. Floor face >USD 150m.",
    "hunt_cycle179",
    investment_type="ppp_concession",
    evidence="documented",
    bib_type="government",
    chicago='Agencia de Promoción de la Inversión Privada (PROINVERSIÓN). “Gobierno adjudica PTAR Puerto Maldonado que tratará el 100 % de aguas residuales de la ciudad en beneficio de 190 mil personas.” December 15, 2025. https://www.gob.pe/institucion/proinversion/noticias/1315940-gobierno-adjudica-ptar-puerto-maldonado-que-tratara-el-100-de-aguas-residuales-de-la-ciudad-en-beneficio-de-190-mil-personas.',
    annotation="ProInversión: PTAR Puerto Maldonado >USD 150m PPP. Supports mota_engil_ptar_puerto_maldonado_150m_2025.",
    evid_note="Opened gob.pe ProInversión page 2026-10-04.",
)

# 1b. water / us — NADBank/JMAS Ciudad Juárez wastewater collector
row_doc(
    "nadbank_jmas_juarez_ww_26p9m_2025",
    "resources",
    "water",
    "us",
    "NADBank / JMAS — Ciudad Juárez Norzagaray wastewater collector upgrades (USD 26.9m)",
    "Mexico",
    "29 May 2025 (NADBank): celebrates first-phase completion of JMAS Ciudad Juárez wastewater system upgrades — total investment USD 26.9 million financed via USD 11.5m BEIF grant (EPA-funded, NADBank-administered) + USD 4.5m NADBank loan + USD 10.9m Mexican local matching. CapEx face = USD 26.9m. Distinct from nadbank_sadm_monterrey_16p75m_2025 / nadbank_sonora_env_650m_mxn_2026.",
    "26900000",
    "2025-05-29",
    "2025",
    "31.69",
    "-106.42",
    "Ciudad Juárez / Norzagaray collector corridor, Chihuahua (NADBank geography; approximate city pin).",
    "nadbank_jmas_juarez_20250529",
    "With a total investment of US$26.9 million, the full project is being financed through a combination of sources: a US$11.5 million grant provided through NADBank's Border Environment Infrastructure Fund (BEIF)—funded by the U.S. Environmental Protection Agency (EPA) and administered by the Bank—, a US$4.5 million loan, which was used by JMAS to carry out the initial construction, and the remaining US$10.9 million will be covered by local matching funds from Mexican sources.",
    "https://nadbank.org/news/press-release/nadbank-and-the-local-water-utility-jmas-celebrate-completion-of-first-phase-of-wastewater-system-upgrades-in-ciudad-juarez",
    "Actor: NADBank (U.S.–Mexico binational) financing JMAS Juárez — us. Opened NADBank English release 29 May 2025. U.S. side-balance water.",
    "hunt_cycle179",
    investment_type="financing",
    evidence="documented",
    bib_type="official",
    chicago='North American Development Bank. “NADBank and the local water utility, JMAS Celebrate Completion of First Phase of Wastewater System Upgrades in Ciudad Juárez.” May 29, 2025. https://nadbank.org/news/press-release/nadbank-and-the-local-water-utility-jmas-celebrate-completion-of-first-phase-of-wastewater-system-upgrades-in-ciudad-juarez.',
    annotation="NADBank/JMAS: Juárez WW upgrades USD 26.9m. Supports nadbank_jmas_juarez_ww_26p9m_2025.",
    evid_note="Opened NADBank press release 2026-10-04.",
)

# 2–5 thin / miss notes covered in docstring (balsa, fission_smr, niobium, nickel)

# 6a. copper / allied — BHP Spence Operational Adequacy USD 1.7bn
row_doc(
    "bhp_spence_operational_adequacy_1p7bn_2024",
    "resources",
    "copper",
    "allied",
    "BHP — Spence Operational Adequacy leaching extension (USD 1.7bn)",
    "Chile",
    "30 Dec 2024 (InvestChile citing Coeva/SEA): Antofagasta Region Environmental Evaluation Commission approves EIA for Spence Operational Adequacy — upgrade current leaching operation to extend mine life to 2039 (Full SaL); update mine plan, deepen pit, optimize crushing/heaps/solution handling; investment USD 1.7 billion. CapEx = USD 1.7bn. Distinct from bhp_escondida_new_concentrator_2026 and June 2026 Spence concentrator/chalcopyrite sanctions.",
    "1700000000",
    "2024-12-30",
    "2024",
    "-22.82",
    "-69.30",
    "BHP Spence / Pampa Norte, Antofagasta Region (company geography; approximate pin).",
    "investchile_bhp_spence_1p7bn_20241230",
    "The Antofagasta Region’s Environmental Evaluation Commission (Coeva) approved the Environmental Impact Assessment (EIA) for the Spence Operational Adequacy project, an initiative by BHP’s Spence mine involving US$1.7 billion in investment… “The ‘Spence Operational Adequacy’ project involves upgrading the mine’s current leaching operation to extend its useful life until 2039,” the company’s EIA explained.",
    "https://blog.investchile.gob.cl/en/2026/bhp-spence",
    "Actor: BHP (Australia/UK) Spence — allied. Opened InvestChile English post 30 Dec 2024 summarizing Coeva EIA approval and USD 1.7bn.",
    "hunt_cycle179",
    investment_type="brownfield_expansion",
    evidence="documented",
    bib_type="government",
    chicago='InvestChile. “BHP gets the green light for a US$1.7 billion mining project.” December 30, 2024. https://blog.investchile.gob.cl/en/2026/bhp-spence.',
    annotation="InvestChile/Coeva: Spence Operational Adequacy USD 1.7bn. Supports bhp_spence_operational_adequacy_1p7bn_2024.",
    evid_note="Opened InvestChile page 2026-10-04.",
)

# 6b. copper / allied — BHP Spence concentrator + chalcopyrite sanctions (CapEx undisclosed)
row_doc(
    "bhp_spence_concentrator_chalcopyrite_2026",
    "resources",
    "copper",
    "allied",
    "BHP — Spence Concentrator Upgrade Recovery + Chalcopyrite Leaching sanctions",
    "Chile",
    "16 Jul 2026 (BHP Operational Review / ASX): Spence Concentrator Upgrade Recovery project (flotation residence-time upgrade) sanctioned June 2026 with first production expected FY28; Spence Chalcopyrite Leaching project (Simple Approach to Leaching 2 / SAL2) also sanctioned June 2026 with first production expected CY28. CapEx USD not disclosed — blank. Distinct from bhp_spence_operational_adequacy_1p7bn_2024 Full SaL EIA.",
    "",
    "",
    "2026",
    "-22.82",
    "-69.30",
    "BHP Spence / Pampa Norte, Antofagasta Region (company geography; approximate pin).",
    "bhp_op_review_fy26_20260716",
    "The Spence Concentrator Upgrade Recovery project, which upgrades the flotation circuit to increase residence time and improve recoveries, was sanctioned in June 2026, with first production expected during FY28… The Spence Chalcopyrite Leaching project was also sanctioned in June 2026, which includes the implementation of BHP’s sulphide leaching technology, Simple Approach to Leaching 2… with first production expected in CY28.",
    "https://announcements.asx.com.au/asxpdf/20260716/pdf/071rnjvs39bf7r.pdf",
    "Actor: BHP — allied. Opened BHP Operational Review PDF on ASX 16 Jul 2026. CapEx blank (not disclosed).",
    "hunt_cycle179",
    investment_type="brownfield_expansion",
    evidence="documented",
    bib_type="company",
    chicago='BHP Group Limited. “Operational review for the year ended 30 June 2026.” ASX announcement, July 16, 2026. https://announcements.asx.com.au/asxpdf/20260716/pdf/071rnjvs39bf7r.pdf.',
    annotation="BHP ASX: Spence concentrator + chalcopyrite sanctions. Supports bhp_spence_concentrator_chalcopyrite_2026.",
    evid_note="Opened ASX PDF 2026-10-04.",
)

# 7. other_renewables / miss (CIP Esperanza / CATL / Fluence dense)

# 8. engineering_epc / us — EXIM Hokchi Mexico USD 69.8m
row_doc(
    "exim_hokchi_mexico_69p8m_2021",
    "infrastructure",
    "engineering_epc",
    "us",
    "U.S. EXIM — Hokchi Energy Mexico O&G equipment direct loan (USD 69.8m)",
    "Mexico",
    "2021 (EXIM Board / FY2021 Annual Report): EXIM Board approves USD 69.8 million direct loan to Hokchi Energy S.A. de C.V. (Mexico) with Pan American Energy S.L. (Argentina) as guarantor — purchase of U.S. turbines, compressor units, and spare parts for shallow-water Gulf of Mexico oil and gas production/processing; estimated 200 U.S. jobs. CapEx/financing face = USD 69.8m. Distinct from exim_wabtec_gmxt_185m_2025 / exim_bahamas_lng_99m_2025.",
    "69800000",
    "2021-01-01",
    "2021",
    "",
    "",
    "Hokchi Energy shallow-water Gulf of Mexico block (EXIM geography) — lat/lon blank (offshore block not named with coordinates).",
    "exim_hokchi_mexico_69p8m",
    "The EXIM Board of Directors unanimously approved a transaction where the borrower and end-user of a $69.8 million direct loan is Hokchi Energy S.A. de C.V. of Mexico, with Pan American Energy S.L. of Argentina acting as guarantor. Hokchi Energy will use the direct loan for the purchase of U.S. goods and services including turbines, compressor units, and spare parts, for use in the production and processing of oil and gas resources located in an offshore block in the Gulf of Mexico.",
    "https://www.exim.gov/news/exim-board-unanimously-approves-698-million-loan-support-oil-and-gas-production-and-processing",
    "Actor: U.S. EXIM Bank financing U.S. equipment exports to Hokchi (Mexico) — us. Opened EXIM English release (FY2021 authorization). U.S. side-balance engineering_epc.",
    "hunt_cycle179",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='Export-Import Bank of the United States. “EXIM Board Unanimously Approves $69.8 Million Loan to Support U.S. Oil and Gas Production and Processing Equipment Exports to the Shallow Waters of Mexico and an Estimated 200 American Jobs.” https://www.exim.gov/news/exim-board-unanimously-approves-698-million-loan-support-oil-and-gas-production-and-processing.',
    annotation="EXIM: Hokchi Mexico USD 69.8m direct loan. Supports exim_hokchi_mexico_69p8m_2021.",
    evid_note="Opened EXIM.gov press page 2026-10-04; FY2021 Annual Report confirms authorization year.",
)

# 9–11 miss: building_materials, graphite, bridges_roads (catalog dense)

# 12. power_plants_grid / allied — Omexom Energisa LOT 12 EPCM
row_doc(
    "omexom_energisa_lot12_epcm_2025",
    "energy",
    "power_plants_grid",
    "allied",
    "Omexom (VINCI Energies) — Energisa LOT 12 transmission EPCM (2×500 kV / 391.8 km)",
    "Brazil",
    "Jul 2025 (Omexom): Omexom in Brazil awarded EPCM contract by Energisa Group for LOT 12 from ANEEL Transmission Auction June 2024 — construct two 500 kV transmission lines totaling 391.8 km; contract signed July 2025 after ~1 year negotiations; completion targeted Feb 2029 (43 months). CapEx USD not disclosed — blank. Distinct from engie_peru_grupo1_transmision_230m_2026.",
    "",
    "",
    "2025",
    "",
    "",
    "Energisa LOT 12 dual 500 kV corridors (Brazil multi-segment) — lat/lon blank (multi-line package).",
    "omexom_energisa_lot12_2025",
    "Omexom in Brazil has been awarded an Engineering, Procurement, and Construction Management (EPCM) contract by the Energisa Group for the execution of LOT 12, part of the ANEEL Transmission Auction held in June 2024. The project involves the construction of two 500 kV transmission lines, totaling 391.8 kilometers… The contract was officially signed by Omexom in Brazil in July 2025… expected to be completed by February 2029, after 43 months of intensive work.",
    "https://www.omexom.com/news/omexom-in-brazil-awarded-epcm-contract-for-lot-12-a-major-transmission-line-project/",
    "Actor: Omexom / VINCI Energies (France) — allied. Opened Omexom English release. CapEx blank.",
    "hunt_cycle179",
    investment_type="epc",
    evidence="documented",
    bib_type="company",
    chicago='Omexom. “Omexom in Brazil Awarded EPCM Contract for LOT 12, A Major Transmission Line Project.” 2025. https://www.omexom.com/news/omexom-in-brazil-awarded-epcm-contract-for-lot-12-a-major-transmission-line-project/.',
    annotation="Omexom: Energisa LOT 12 EPCM 391.8 km. Supports omexom_energisa_lot12_epcm_2025.",
    evid_note="Opened Omexom company page 2026-10-04.",
)

# 13–14 miss: port_cranes, wind (Vestas Dom Inocêncio already logged)

# 15. solar / allied — World Bank Haiti Jacmel AF
row_doc(
    "wb_haiti_jacmel_renewable_af_7p1m_2025",
    "energy",
    "solar",
    "allied",
    "World Bank / IDA — Haiti Renewable Energy for All additional financing (USD 7.1m)",
    "Haiti",
    "2025 (World Bank AF PAD P156719): Additional Financing USD 7.1 million (USD 3.6m grant + USD 3.5m concessional SCF-SREP loan) to complete parent Project activities including grid-connected 5.5 MWp / 4.61 MWac Jacmel solar PV, 2 MW / 6 MWh grid-forming BESS, MV/LV distribution lines and public lighting, plus TA. AF face = USD 7.1m. Distinct from ifc_idb_solengy_haiti_13p5m_2025 / wb_haiti_resilient_corridors_80m_2025.",
    "7100000",
    "2025-09-02",
    "2025",
    "18.23",
    "-72.53",
    "Jacmel grid-connected solar+BESS site, Sud-Est Department (PAD geography; approximate municipal pin).",
    "wb_haiti_re4all_af_pad_2025",
    "The AF in the amount of US$7.1 million (US$3.6 million grant and US$3.5 million concessional loan from SCF- SREP) will help (a) complete some activities of the parent Project and (b) finance costs associated with Project management and TA… Design, supply, installation and commissioning of a grid-connected photovoltaic power plant with a minimum capacity of 5.5 MWp / 4.61 MWac at Jacmel… BESS with a minimum capacity of 2 MW / 6MWh…",
    "https://documents1.worldbank.org/curated/en/099090325211017284/pdf/P156719-89cf5bdd-6cac-4c70-979c-5b776d673a5b.pdf",
    "Actor: World Bank / IDA (+SCF-SREP) — allied. Opened AF PAD PDF. Haiti under-covered solar cell.",
    "hunt_cycle179",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='World Bank. “Haiti: Renewable Energy for All (P156719) — Additional Financing Project Paper.” 2025. https://documents1.worldbank.org/curated/en/099090325211017284/pdf/P156719-89cf5bdd-6cac-4c70-979c-5b776d673a5b.pdf.',
    annotation="WB AF PAD: Haiti Jacmel solar+BESS USD 7.1m. Supports wb_haiti_jacmel_renewable_af_7p1m_2025.",
    evid_note="Opened World Bank AF PAD PDF 2026-10-04.",
)

# 16–18 miss: lithium, rail, port_ownership (catalog dense; Progress Rail VLI / PowerChina Chancay already logged)


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
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 179 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
