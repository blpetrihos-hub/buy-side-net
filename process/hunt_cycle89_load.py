#!/usr/bin/env python3
"""Cycle 89 hunt: shuffle_seed=20261089; equal budget; U.S./PRC split; thin after.

Order: port_cranes, graphite, solar, niobium, lithium, power_plants_grid, water,
engineering_epc, building_materials, copper, other_renewables, nickel, balsa, wind,
rail, fission_smr, port_ownership, bridges_roads.
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
# 1 infrastructure/port_cranes — ZPMC Contecon Manzanillo STS #13–14 + 5 RTG (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "zpmc_contecon_manzanillo_sts_rtg_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — Contecon Manzanillo TEC II electric STS #13–14 + five RTGs",
        "country": "Mexico",
        "asset": "29 Sep 2026 T21: Contecon Manzanillo (ICTSI TEC II) receives two ZPMC fully electric STS quay cranes (#13 and #14) rated for vessels up to 24,000 TEU — each ~1,600 t, 60 m height, 74 m outreach — plus five RTG yard cranes delivered the prior week. CapEx for the crane tranche not isolated (CEO situates within broader >USD 500m 2022 extension investment). Distinct from zpmc_cmsa_manzanillo_rtg_2025 (three hybrid RTGs, Oct 2025) and ssa_manzanillo_sts_21m_2025 (SSA TEC I).",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "19.05",
        "lon": "-104.30",
        "geo_note": "TEC II / Contecon Manzanillo, Port of Manzanillo, Colima (T21 geography).",
        "evidence": "documented",
        "source_id": "t21_contecon_sts_20260929",
        "note": "Actor: ZPMC (PRC) OEM to Contecon/ICTSI — prc. Trade press names ZPMC; CapEx blank.",
    },
    {
        "id": "zpmc_contecon_manzanillo_sts_rtg_2026",
        "retrieved": "2026-10-02",
        "source_id": "t21_contecon_sts_20260929",
        "url": "https://t21.com.mx/contecon-suma-dos-gruas-de-muelle-en-manzanillo-suministro-electrico-pone-a-prueba-su-expansion/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Contecon Manzanillo … recibió dos grúas pórtico eléctricas STS de la china ZPMC capaces de atender buques de hasta 24 mil contenedores … Las nuevas grúas de muelle son las números 13 y 14 … La terminal también incorporó desde la semana pasada cinco grúas RTG",
        "note": "Opened T21 Spanish trade coverage of Contecon Manzanillo ZPMC STS/RTG delivery.",
    },
    {
        "id": "t21_contecon_sts_20260929",
        "type": "press",
        "chicago": "Duarte Rionda, Enrique. “Contecon suma dos grúas de muelle en Manzanillo; suministro eléctrico pone a prueba su expansión.” T21, 29 September 2026.",
        "url": "https://t21.com.mx/contecon-suma-dos-gruas-de-muelle-en-manzanillo-suministro-electrico-pone-a-prueba-su-expansion/",
        "annotation": "ZPMC electric STS #13–14 + five RTGs at Contecon Manzanillo TEC II. Supports zpmc_contecon_manzanillo_sts_rtg_2026.",
        "supports": ["zpmc_contecon_manzanillo_sts_rtg_2026", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# 3 energy/solar — AES Dominicana Peravia I & II 140 MW COD (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aes_dr_peravia_140mw_cod_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "AES Dominicana Renewable Energy — Peravia I & II solar COD (Baní)",
        "country": "Dominican Republic",
        "asset": "AES Dominicana Q3 2025 investor presentation (updated Dec 2025): Peravia I & II solar plants in Baní totaling 140 MWn achieved commercial operation September 2025 (Peravia II grid injection from 1 Jul; Peravia I end-Jul); Peravia I under 15-year PPA with EDE ESTE and Peravia II under 12-year PPA with AES Andrés DR. CapEx USD not isolated for the pair on the opened deck. Distinct from aes_andes Chile rows and Bayasol/Santanasol presence.",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "18.28",
        "lon": "-70.33",
        "geo_note": "Baní, Peravia province, Dominican Republic (AES DR investor geography).",
        "evidence": "documented",
        "source_id": "aes_dr_investor_q3_2025",
        "note": "Actor: AES Corporation via AES Dominicana Renewable Energy — us. Company investor deck. CapEx blank.",
    },
    {
        "id": "aes_dr_peravia_140mw_cod_2025",
        "retrieved": "2026-10-02",
        "source_id": "aes_dr_investor_q3_2025",
        "url": "https://www.aesdominicana.com/sites/aesvault.com/files/2026-01/AES%20DR%20-%20Investor%20Presentation%202025%20Q3.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "COD Sep 2025 Peravia I & II +140 MWn … Peravia I & II 140MWn located in Bani … both achieved COD Sep 2025.",
        "note": "Opened AES Dominicana Q3 2025 investor presentation PDF.",
    },
    {
        "id": "aes_dr_investor_q3_2025",
        "type": "company",
        "chicago": "AES Dominicana. “AES DR — Investor Presentation 2025 Q3.” January 2026 PDF (Q3 2025 results deck).",
        "url": "https://www.aesdominicana.com/sites/aesvault.com/files/2026-01/AES%20DR%20-%20Investor%20Presentation%202025%20Q3.pdf",
        "annotation": "Documents Peravia I & II 140 MW COD Sep 2025 and related DR renewables pipeline. Supports aes_dr_peravia_140mw_cod_2025.",
        "supports": ["aes_dr_peravia_140mw_cod_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 7 resources/water — NADBank San Quintín desalination loan proposal (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "nadbank_san_quintin_desal_665m_mxn_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "NADBank — proposed up to MXN 665m loan for San Quintín desalination (Desaladora Kenton)",
        "country": "Mexico",
        "asset": "12 May 2026 NADBank certification/financing proposal (Board draft): resubmits San Quintín Valley seawater RO desalination plant (250 lps / 5.7 mgd) after 2018 certification was not implemented; proposed NADBank loan up to MXN 665 million (≤25-year tenor) to Desaladora Kenton S.A. de C.V., now sponsored by consortium GL Desal Holdings and EBD Blukey LLC; plant expected to benefit ~109,200 residents. Proposed financing — not a closed commitment on the opened proposal.",
        "investment_type": "financing",
        "value": "665000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "30.56",
        "lon": "-115.94",
        "geo_note": "San Quintín Valley / former Ejido Chapala area, Baja California (NADBank proposal geography; approximate municipal pin).",
        "evidence": "documented",
        "source_id": "nadbank_san_quintin_proposal_20260512",
        "note": "Actor: North American Development Bank (U.S.–Mexico) — us. Official NADBank English proposal PDF. Value stored as MXN ceiling; USD conversion left blank (no cited FX on page). Distinct from nadbank_baja_rosarito_distrib_82m_2026.",
    },
    {
        "id": "nadbank_san_quintin_desal_665m_mxn_2026",
        "retrieved": "2026-10-02",
        "source_id": "nadbank_san_quintin_proposal_20260512",
        "url": "https://nadbank.org/hubfs/proposals-open-for-public-comment/Planta%20Desaladora%20en%20San%20Quintin%20(Eng)_published.pdf?hsLang=en",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "NADBank is requesting authorization to provide a loan for up to $665 million pesos to the Project Sponsor. … desalination plant with a capacity of 250 liters per second (lps) or 5.7 million gallons per day (mgd)",
        "note": "Opened NADBank English certification and financing proposal PDF for San Quintín desal.",
    },
    {
        "id": "nadbank_san_quintin_proposal_20260512",
        "type": "official",
        "chicago": "North American Development Bank. “Certification and Financing Proposal — Desalination Plant in San Quintín, Baja California.” Published 12 May 2026.",
        "url": "https://nadbank.org/hubfs/proposals-open-for-public-comment/Planta%20Desaladora%20en%20San%20Quintin%20(Eng)_published.pdf?hsLang=en",
        "annotation": "Proposed NADBank loan up to MXN 665m for 250 lps San Quintín desal (Desaladora Kenton). Supports nadbank_san_quintin_desal_665m_mxn_2026.",
        "supports": ["nadbank_san_quintin_desal_665m_mxn_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 7 resources/water — GS Inima Espírito Santo Lot A sanitation PPP (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "gs_inima_espirito_santo_lot_a_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "GS Inima Brasil / Forte Ambiental — Espírito Santo Sanitation Lot A concession",
        "country": "Brazil",
        "asset": "9 Oct 2025 GS Inima: consortium with Forte Ambiental signs 24-year concession contract with Espírito Santo state and CESAN for Sanitation Lot A — wastewater collection/treatment in 35 municipalities including Vitória; company cites investment exceeding EUR 150 million for 37 new WWTPs, expansion of five existing plants, 46 km discharge pipes, 75 pumping stations, and 62,000 sewer connections; new SPV Espírito Santo Saneamento S.A.; 180-day assisted-operation transition. Distinct from GS Inima Atacama/Ensenada desal rows.",
        "investment_type": "concession",
        "value": "150000000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-20.32",
        "lon": "-40.34",
        "geo_note": "Vitória / Espírito Santo Lot A municipalities (company geography; capital pin).",
        "evidence": "documented",
        "source_id": "gs_inima_espirito_santo_20251009",
        "note": "Actor: GS Inima (Spain HQ) — allied. Company English primary. Value at stated floor (>EUR 150m); USD conversion blank.",
    },
    {
        "id": "gs_inima_espirito_santo_lot_a_2025",
        "retrieved": "2026-10-02",
        "source_id": "gs_inima_espirito_santo_20251009",
        "url": "https://inima.com/en/gs-inima-signs-contract-the-integrated-sanitation-service-in-thestate-of-espirito-santo/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "GS Inima Brasil has been awarded a 24-year contract to manage wastewater collection and treatment services in 35 municipalities … With an investment exceeding 150 million euros, the project includes the construction of 37 new Wastewater Treatment Plants (WWTPs)",
        "note": "Opened GS Inima English company release on Espírito Santo Lot A contract signing.",
    },
    {
        "id": "gs_inima_espirito_santo_20251009",
        "type": "company",
        "chicago": "GS Inima. “GS Inima Has Signed the Contract for the Integrated Sanitation Service in the Brazilian State of Espírito Santo.” 9 October 2025.",
        "url": "https://inima.com/en/gs-inima-signs-contract-the-integrated-sanitation-service-in-thestate-of-espirito-santo/",
        "annotation": "GS Inima/Forte Ambiental Lot A 24-year sanitation concession (>EUR 150m; 35 municipalities). Supports gs_inima_espirito_santo_lot_a_2025.",
        "supports": ["gs_inima_espirito_santo_lot_a_2025", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 10 resources/copper — Southern Copper USD 1.25bn notes for Tía María (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "southern_copper_tia_maria_notes_1p25bn_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "other",
        "counterpart": "Southern Copper — USD 1.25bn 5.350% notes due 2036 (Tía María / SPCC CapEx)",
        "country": "Peru",
        "asset": "24–25 Jun 2026: Southern Copper Corporation completes SEC-registered offering of USD 1.25 billion aggregate principal 5.350% senior unsecured notes due 2036; net proceeds ~USD 1.241bn to be used by Southern Peru Copper Corporation Sucursal del Perú for Tía María project development, SPCC CapEx program, and/or general corporate purposes. Distinct financing row from southern_copper_tia_maria_2025 (ownership/CAPEX budget USD 1.80bn).",
        "investment_type": "financing",
        "value": "1250000000",
        "currency": "USD",
        "value_usd": "1250000000",
        "fx_usd": "1",
        "fx_date": "2026-06-24",
        "year": "2026",
        "status": "active",
        "lat": "-17.0",
        "lon": "-71.85",
        "geo_note": "Tía María / Islay province, Arequipa (same geography as southern_copper_tia_maria_2025).",
        "evidence": "documented",
        "source_id": "scco_notes_1p25bn_20260625",
        "note": "Actor: Southern Copper / Grupo México (Mexico-majority; Phoenix process) — other (consistent with southern_copper_tia_maria_2025). SEC/company primary. Value = face principal.",
    },
    {
        "id": "southern_copper_tia_maria_notes_1p25bn_2026",
        "retrieved": "2026-10-02",
        "source_id": "scco_notes_1p25bn_20260625",
        "url": "https://www.sec.gov/Archives/edgar/data/1001838/000114036126026337/ef20076661_ex99.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Southern Copper Corporation … has completed a public offering of US$1,250,000,000 million 5.350% Notes due 2036. … The net proceeds from this offering will be used by Southern Peru Copper Corporation, Sucursal del Perú … for the development of the Tia Maria project",
        "note": "Opened Southern Copper Exhibit 99 press release on SEC EDGAR for the USD 1.25bn notes.",
    },
    {
        "id": "scco_notes_1p25bn_20260625",
        "type": "filing",
        "chicago": "Southern Copper Corporation. “Southern Copper Corporation Issued $1,250,000,000 Unsecured Notes Due 2036.” Exhibit 99 to Form 8-K, 25 June 2026. SEC EDGAR.",
        "url": "https://www.sec.gov/Archives/edgar/data/1001838/000114036126026337/ef20076661_ex99.htm",
        "annotation": "USD 1.25bn SCCO notes with proceeds earmarked for Tía María / SPCC CapEx. Supports southern_copper_tia_maria_notes_1p25bn_2026.",
        "supports": ["southern_copper_tia_maria_notes_1p25bn_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 10 resources/copper — DFC Cerro de Pasco Quiulacocha project development (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "dfc_cerro_pasco_quiulacocha_5m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "us",
        "counterpart": "DFC — USD 5m project-development support for Cerro de Pasco Quiulacocha tailings",
        "country": "Peru",
        "asset": "2026 DFC investment story: committed USD 5 million in project-development support to Cerro de Pasco Resources Inc. for feasibility study and ESIA on the Quiulacocha Tailings Storage Facility (~70 Mt historic silver/zinc/copper/lead/gold tailings; potential gallium recovery and iron sulfide for sulfuric acid). Framed as potential precursor to later DFC debt/equity. Distinct from CRTG Cerro de Pasco–Tingo María road EPC.",
        "investment_type": "financing",
        "value": "5000000",
        "currency": "USD",
        "value_usd": "5000000",
        "fx_usd": "1",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-10.68",
        "lon": "-76.26",
        "geo_note": "Cerro de Pasco / Quiulacocha TSF, Pasco Region, Peru (DFC project geography; approximate municipal pin).",
        "evidence": "documented",
        "source_id": "dfc_cerro_pasco_2026",
        "note": "Actor: U.S. DFC project-development support — us. Official DFC investment-story page. Coded copper (Cu among named recoverable metals in scarce-minerals layer).",
    },
    {
        "id": "dfc_cerro_pasco_quiulacocha_5m_2026",
        "retrieved": "2026-10-02",
        "source_id": "dfc_cerro_pasco_2026",
        "url": "https://www.dfc.gov/investment-story/enhancing-mineral-processing-peru",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "DFC committed $5 million in project development support to help Cerro de Pasco Resources Inc. advance a tailings reprocessing project … for the Quiulacocha Tailings Storage Facility",
        "note": "Opened DFC English investment-story page on Cerro de Pasco / Quiulacocha support.",
    },
    {
        "id": "dfc_cerro_pasco_2026",
        "type": "official",
        "chicago": "U.S. International Development Finance Corporation. “Enhancing Mineral Processing in Peru.” Investment story, 2026.",
        "url": "https://www.dfc.gov/investment-story/enhancing-mineral-processing-peru",
        "annotation": "DFC USD 5m project-development support for Quiulacocha tailings reprocessing. Supports dfc_cerro_pasco_quiulacocha_5m_2026.",
        "supports": ["dfc_cerro_pasco_quiulacocha_5m_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 14 energy/wind — SANY Renewable Purranque 18 MW first LatAm wind (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sany_purranque_18mw_chile_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "SANY Renewable Energy — 18 MW Purranque wind supply/install (Los Lagos)",
        "country": "Chile",
        "asset": "17 Jun 2026 SANY Renewable Energy: ships core equipment from Tianjin for its first Latin America wind project — 18 MW PURRANQUE in Chile — providing integrated supply, transportation, and installation. BioBioChile 10 Aug 2026 corroborates turbine installation underway in Purranque (Los Lagos) with generation targeted ~October. Contract USD not disclosed. Distinct from Sany Suape port-crane row.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-40.92",
        "lon": "-73.17",
        "geo_note": "Purranque, Los Lagos Region, Chile (SANY / BioBioChile geography).",
        "evidence": "documented",
        "source_id": "sany_purranque_20260617",
        "note": "Actor: SANY Renewable Energy (PRC) — prc. Company PR Newswire English primary. CapEx blank.",
    },
    {
        "id": "sany_purranque_18mw_chile_2026",
        "retrieved": "2026-10-02",
        "source_id": "sany_purranque_20260617",
        "url": "https://www.prnewswire.com/news-releases/sany-ships-core-equipment-for-first-wind-project-in-latin-america-advancing-global-energy-transition-302803741.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "SANY Renewable Energy Co., Ltd. … recently shipped the core equipment for its first wind power project in Chile, the 18 MW PURRANQUE project, from the Port of Tianjin. The company is providing integrated supply, transportation, and installation services for the project.",
        "note": "Opened SANY Group PR Newswire English release on Purranque shipment.",
    },
    {
        "id": "sany_purranque_20260617",
        "type": "company",
        "chicago": "SANY Group. “SANY Ships Core Equipment for First Wind Project in Latin America, Advancing Global Energy Transition.” PR Newswire, 17 June 2026.",
        "url": "https://www.prnewswire.com/news-releases/sany-ships-core-equipment-for-first-wind-project-in-latin-america-advancing-global-energy-transition-302803741.html",
        "annotation": "SANY Renewable 18 MW Purranque Chile first LatAm wind supply/install. Supports sany_purranque_18mw_chile_2026.",
        "supports": ["sany_purranque_18mw_chile_2026", "hunt_energy_wind"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]] = entry
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8"))
    assert isinstance(bib, list)
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
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

    hunt_updates = {
        "hunt_infra_port_cranes": "Cycle 89: logged zpmc_contecon_manzanillo_sts_rtg_2026 (PRC); Tecon RG / TCP Montevideo already.",
        "hunt_res_graphite": "Cycle 89: equal budget; Graphcoa / Atlas Malacacheta dense (miss). Thin top-up dry — shift.",
        "hunt_energy_solar": "Cycle 89: logged aes_dr_peravia_140mw_cod_2025 (U.S.); Array Lupi / Atlas refi already.",
        "hunt_fenb_araxa": "Cycle 89: equal budget; CMOC / CBMM already (miss).",
        "hunt_res_lithium": "Cycle 89: equal budget; Zijin 3Q / EXIM Argentina already (miss).",
        "hunt_br_power_equip": "Cycle 89: equal budget; GE Vernova / PowerChina São Simão already (miss).",
        "hunt_res_water": "Cycle 89: logged nadbank_san_quintin_desal_665m_mxn_2026 (U.S.) + gs_inima_espirito_santo_lot_a_2025 (allied).",
        "hunt_infra_engineering_epc": "Cycle 89: equal budget; Halliburton / Baker Hughes dense (miss).",
        "hunt_infra_building_materials": "Cycle 89: equal budget; Holcim Colombia / Sinoma Cruz Azul already (miss).",
        "hunt_res_copper": "Cycle 89: logged southern_copper_tia_maria_notes_1p25bn_2026 (other) + dfc_cerro_pasco_quiulacocha_5m_2026 (U.S.).",
        "hunt_energy_other_renewables": "Cycle 89: equal budget; Sungrow / Ormat Dominica already (miss).",
        "hunt_res_nickel": "Cycle 89: equal budget; DFC Piauí already (miss). Next-thinnest after fission/balsa/graphite dry.",
        "hunt_res_balsa": "Cycle 89: equal budget; Plantabal / AIMA dense (miss). Thin top-up dry — shift.",
        "hunt_energy_wind": "Cycle 89: logged sany_purranque_18mw_chile_2026 (PRC); Goldwind Sento Sé already.",
        "hunt_latam_rail_telecom": "Cycle 89: equal budget; CRCC Batuco / CRI electrification already (miss).",
        "hunt_energy_fission_smr": "Cycle 89: equal budget; USTDA / CAREM / FIRST already (miss). Thin top-up dry — shift.",
        "hunt_infra_port_ownership": "Cycle 89: equal budget; COSCO Chancay / APM/DP World dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 89: equal budget; CRBC Corentyne Lot 2 / CHEC San Carlos already (miss).",
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
    print("Cycle 89 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
