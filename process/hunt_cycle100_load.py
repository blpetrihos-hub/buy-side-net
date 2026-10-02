#!/usr/bin/env python3
"""Cycle 100 hunt: shuffle_seed=20261100; equal budget; U.S./PRC split; thin after.

Order: niobium, wind, solar, port_ownership, fission_smr, other_renewables,
engineering_epc, rail, port_cranes, power_plants_grid, building_materials,
bridges_roads, water, balsa, nickel, copper, lithium, graphite.
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
# resources/niobium — CBMM Araxá CapEx R$630m 2024 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cbmm_araxa_capex_630m_2024",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM — Araxá niobium complex CapEx 2024",
        "country": "Brazil",
        "asset": "24 Apr 2025 CBMM results release: 2024 CapEx of R$ 630 million at the Araxá (MG) niobium industrial complex alongside net revenue R$ 13 billion, net income R$ 5 billion, and >95 kt FeNb-equivalent sales (+4% YoY); company also cites R$ 270 million R&D and inauguration of Echion XNO® battery-anode plant. Distinct from Folha/Reuters R$10bn five-year plan proxy and Diário do Comércio R$13bn 2026–2031 proxy rows — this is company-documented 2024 executed CapEx.",
        "investment_type": "other",
        "value": "630000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-19.5902",
        "lon": "-46.9406",
        "geo_note": "CBMM Industrial Complex, Araxá, Minas Gerais (company geography).",
        "evidence": "documented",
        "source_id": "cbmm_results_2024_release_20250424",
        "note": "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. Official CBMM results PDF. Value stored as BRL (no FX). Thin top-up niobium.",
    },
    {
        "id": "cbmm_araxa_capex_630m_2024",
        "retrieved": "2026-10-02",
        "source_id": "cbmm_results_2024_release_20250424",
        "url": "https://cbmm.com/-/media/CBMM/MEDIA-CENTER/Noticias-Internas/resultado-final-2024/CBMM_Release-de-Resultados-2025---Final---22042025.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Os investimentos contínuos da companhia em pesquisa e desenvolvimento, além de sua sólida capacidade logística possibilitaram um resultado financeiro e operacional positivo com receita líquida de R$ 13 bilhões; lucro líquido de R$ 5 bilhões; e Capex de R$ 630 milhões.",
        "note": "Opened CBMM 24 Apr 2025 results PDF: CapEx R$630m in 2024; FeNb-eq sales >95 kt.",
    },
    {
        "id": "cbmm_results_2024_release_20250424",
        "type": "company",
        "chicago": "Companhia Brasileira de Metalurgia e Mineração (CBMM). “CBMM mantém estratégia de desenvolvimento de tecnologia para aplicações de Nióbio” (Release de Resultados 2024). 24 April 2025. https://cbmm.com/-/media/CBMM/MEDIA-CENTER/Noticias-Internas/resultado-final-2024/CBMM_Release-de-Resultados-2025---Final---22042025.pdf.",
        "url": "https://cbmm.com/-/media/CBMM/MEDIA-CENTER/Noticias-Internas/resultado-final-2024/CBMM_Release-de-Resultados-2025---Final---22042025.pdf",
        "annotation": "CBMM primary: 2024 CapEx R$630m at Araxá. Supports cbmm_araxa_capex_630m_2024.",
        "supports": ["cbmm_araxa_capex_630m_2024", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Nieves Lares 2024 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_nieves_lares_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Nieves & Nieves Engineers & Contractors Inc — FHWA Emergency Relief PR-128 / HWY-133–137 (Lares)",
        "country": "Puerto Rico",
        "asset": "24 Jul 2024: FHWA awards firm-fixed-price contract 693C7324C000015 to Nieves & Nieves Engineers & Contractors Inc for Project PR ER DOT PRMNT RPR(21) — repairing landslide and washout damages on PR-128 HWY-133 (km 51.3), HWY-134 (km 51.63), HWY-135 (km 51.71), HWY-136 (km 51.77), HWY-137 (km 51.83), and related sites; obligated USD 3,831,400; place of performance Lares. Distinct from Nieves Ángeles 2022 award.",
        "investment_type": "epc",
        "value": "3831400",
        "currency": "USD",
        "value_usd": "3831400",
        "fx_usd": "1",
        "fx_date": "2024-07-24",
        "year": "2024",
        "status": "active",
        "lat": "18.295",
        "lon": "-66.878",
        "geo_note": "Lares Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_nieves_lares_20240724",
        "note": "Actor: Nieves & Nieves (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_nieves_lares_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_nieves_lares_20240724",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000015_6925_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "PROJECT PR ER DOT PRMNT RPR(21) THE PROJECT CONSISTS OF REPAIRING LANDSLIDE AND WASHOUT DAMAGES CAUSED BY HURRICANES IRMA AND MARIA ON PR-128 HWY-133 (KM. 51.3), HWY-134 (KM. 51.63), HWY-135 (KM. 51.71), HWY-136 (KM. 51.77), HWY-137 (KM. 51.83), AND",
        "note": "Opened USASpending Award API: Nieves & Nieves; USD 3,831,400; date_signed 2024-07-24; PoP Lares, PR.",
    },
    {
        "id": "usaspending_nieves_lares_20240724",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7324C000015_6925_-NONE-_-NONE- (Nieves & Nieves Engineers & Contractors Inc; FHWA Emergency Relief Lares PR-128). Signed 24 July 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000015_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7324C000015_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 3.83m FHWA award to Nieves for Lares PR-128 landslide repairs. Supports fhwa_nieves_lares_2024.",
        "supports": ["fhwa_nieves_lares_2024", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Caribbean Sign PR-1/2/3 2021 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_caribbean_sign_pr123_2021",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Caribbean Sign Supplies Manufacturers, Inc. — FHWA Emergency Relief signs/guardrails PR-1/2/3",
        "country": "Puerto Rico",
        "asset": "16 Feb 2021: FHWA awards firm-fixed-price contract 693C7321C000009 to Caribbean Sign Supplies Manufacturers, Inc. for Project PR ST ER PRMNT RPR(6) — repairing signs and guardrails on PR-1, PR-2, and PR-3; obligated USD 17,192,295.66; place of performance San Juan. Distinct from Caribbean Sign Metro/North/South 2026 award.",
        "investment_type": "epc",
        "value": "17192295.66",
        "currency": "USD",
        "value_usd": "17192295.66",
        "fx_usd": "1",
        "fx_date": "2021-02-16",
        "year": "2021",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "San Juan Municipality, Puerto Rico (USASpending place of performance; PR-1/2/3 corridor scope).",
        "evidence": "documented",
        "source_id": "usaspending_caribbean_sign_20210216",
        "note": "Actor: Caribbean Sign Supplies Manufacturers, Inc. (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_caribbean_sign_pr123_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caribbean_sign_20210216",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000009_6925_-NONE-_-NONE-/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "PROJECT PR ST ER PRMNT RPR (6) THE PROJECT CONSISTS OF REPAIRING SIGNS AND GUARDRAILS DAMAGED BY HURRICANES IRMA AND MARIA ON PR-1, PR-2 AND PR-3 AND OTHER MISCELLANEOUS WORK.",
        "note": "Opened USASpending Award API: Caribbean Sign; USD 17,192,295.66; date_signed 2021-02-16; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_caribbean_sign_20210216",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7321C000009_6925_-NONE-_-NONE- (Caribbean Sign Supplies Manufacturers, Inc.; FHWA Emergency Relief PR-1/2/3 signs). Signed 16 February 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000009_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000009_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 17.19m FHWA award to Caribbean Sign for PR-1/2/3 signs/guardrails. Supports fhwa_caribbean_sign_pr123_2021.",
        "supports": ["fhwa_caribbean_sign_pr123_2021", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA JC Associates East Region 2022 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_jc_associates_east_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "JC & Associates Property Management Group Inc — FHWA Emergency Relief signs/guardrails (East Region)",
        "country": "Puerto Rico",
        "asset": "2 Sep 2022: FHWA awards firm-fixed-price contract 693C7322C000019 to JC & Associates Property Management Group Inc for Project PR ER PRMNT RPR(11) — repairing signs and guardrails in the East Region; obligated USD 14,520,510; place of performance San Juan. Distinct from JC Associates West Region 2026 award.",
        "investment_type": "epc",
        "value": "14520510",
        "currency": "USD",
        "value_usd": "14520510",
        "fx_usd": "1",
        "fx_date": "2022-09-02",
        "year": "2022",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "San Juan Municipality, Puerto Rico (USASpending place of performance; East Region scope).",
        "evidence": "documented",
        "source_id": "usaspending_jc_associates_east_20220902",
        "note": "Actor: JC & Associates (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_jc_associates_east_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jc_associates_east_20220902",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000019_6925_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "PROJECT PR ER PRMNT RPR(11) THE PROJECT CONSISTS OF REPAIRING SIGNS AND GUARDRAILS DAMAGED BY HURRICANES IRMA AND MARIA ON EAST REGION AND OTHER MISCELLANEOUS WORK.",
        "note": "Opened USASpending Award API: JC & Associates; USD 14,520,510; date_signed 2022-09-02; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_jc_associates_east_20220902",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7322C000019_6925_-NONE-_-NONE- (JC & Associates; FHWA Emergency Relief East Region signs). Signed 2 September 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000019_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7322C000019_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 14.52m FHWA award to JC & Associates for East Region signs/guardrails. Supports fhwa_jc_associates_east_2022.",
        "supports": ["fhwa_jc_associates_east_2022", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Master Pavement PR-52/53 2021 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_master_pavement_pr52_2021",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Master Pavement Line Corp. — FHWA Emergency Relief signs/guardrails PR-52/53",
        "country": "Puerto Rico",
        "asset": "3 Feb 2021: FHWA awards firm-fixed-price contract 693C7321C000010 to Master Pavement Line Corp. for Project PR ST ER PRMNT RPR(5) — repairing signs and guardrails on PR-52 and PR-53; obligated USD 8,880,038.04; place of performance Mayagüez. Distinct from Caribbean Sign / JC Associates sign awards.",
        "investment_type": "epc",
        "value": "8880038.04",
        "currency": "USD",
        "value_usd": "8880038.04",
        "fx_usd": "1",
        "fx_date": "2021-02-03",
        "year": "2021",
        "status": "active",
        "lat": "18.201",
        "lon": "-67.140",
        "geo_note": "Mayagüez Municipality, Puerto Rico (USASpending place of performance; PR-52/53 corridor).",
        "evidence": "documented",
        "source_id": "usaspending_master_pavement_20210203",
        "note": "Actor: Master Pavement Line Corp. (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_master_pavement_pr52_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_master_pavement_20210203",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000010_6925_-NONE-_-NONE-/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "PROJECT PR ST ER PRMNT RPR(5) THE PROJECT CONSISTS OF REPAIRING SIGNS AND GUARDRAILS DAMAGED BY HURRICANES IRMA AND MARIA ON PR-52 AND PR-53 AND OTHER MISCELLANEOUS WORK.",
        "note": "Opened USASpending Award API: Master Pavement Line Corp.; USD 8,880,038.04; date_signed 2021-02-03; PoP Mayagüez, PR.",
    },
    {
        "id": "usaspending_master_pavement_20210203",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7321C000010_6925_-NONE-_-NONE- (Master Pavement Line Corp.; FHWA Emergency Relief PR-52/53 signs). Signed 3 February 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000010_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000010_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 8.88m FHWA award to Master Pavement for PR-52/53 signs/guardrails. Supports fhwa_master_pavement_pr52_2021.",
        "supports": ["fhwa_master_pavement_pr52_2021", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA JPI Maunabo 2023 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_jpi_maunabo_2023",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "JPI Construction LLC — FHWA Emergency Relief embankment/retaining-wall repairs (Maunabo)",
        "country": "Puerto Rico",
        "asset": "21 Jul 2023: FHWA awards firm-fixed-price contract 693C7323C000014 to JPI Construction LLC for hurricane road repairs including embankment reconstruction, gabion walls, drainage, soldier-pile retaining wall with concrete lagging, milling/overlay, pavement reconstruction, and guardrail replacement; obligated USD 6,146,323.41; place of performance Maunabo. Distinct from JPI Añasco 2023 award.",
        "investment_type": "epc",
        "value": "6146323.41",
        "currency": "USD",
        "value_usd": "6146323.41",
        "fx_usd": "1",
        "fx_date": "2023-07-21",
        "year": "2023",
        "status": "active",
        "lat": "18.007",
        "lon": "-65.899",
        "geo_note": "Maunabo Municipality, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_jpi_maunabo_20230721",
        "note": "Actor: JPI Construction LLC (Puerto Rico / U.S.) + FHWA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_jpi_maunabo_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jpi_maunabo_20230721",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000014_6925_-NONE-_-NONE-/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "THE WORK INCLUDES EMBANKMENT RECONSTRUCTION, GABION WALLS, DRAINAGE SYSTEMS INSTALLATION, AND SOLDIER PILE RETAINING WALL WITH CONCRETE LAGGING, MILLING AND OVERLAY, PAVEMENT RECONSTRUCTION, PAVEMENT MARKINGS, REMOVAL AND REPLACEMENT OF GUARDRAILS,",
        "note": "Opened USASpending Award API: JPI Construction LLC; USD 6,146,323.41; date_signed 2023-07-21; PoP Maunabo, PR.",
    },
    {
        "id": "usaspending_jpi_maunabo_20230721",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7323C000014_6925_-NONE-_-NONE- (JPI Construction LLC; FHWA Emergency Relief Maunabo). Signed 21 July 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000014_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7323C000014_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 6.15m FHWA award to JPI for Maunabo embankment/retaining-wall repairs. Supports fhwa_jpi_maunabo_2023.",
        "supports": ["fhwa_jpi_maunabo_2023", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — FHWA Novel El Yunque FS-27 2021 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fhwa_novel_yunque_fs27_2021",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Novel Construction LLC — FHWA/FAA Emergency Relief FS Route 27 landslides (El Yunque)",
        "country": "Puerto Rico",
        "asset": "30 Aug 2021: FHWA awards firm-fixed-price contract 693C7321C000023 to Novel Construction LLC for repairing two landslides at mile post 1.1 of FS Route 27 within El Yunque National Forest for the Federal Aviation Administration (anchored soldier-pile wall, gabion wall, rock buttress); obligated USD 6,861,239.89; place of performance Palmer. Distinct from Novel Ciales 2023 / Morovis 2024 and Caribe Tecno El Yunque forest-road awards.",
        "investment_type": "epc",
        "value": "6861239.89",
        "currency": "USD",
        "value_usd": "6861239.89",
        "fx_usd": "1",
        "fx_date": "2021-08-30",
        "year": "2021",
        "status": "active",
        "lat": "18.374",
        "lon": "-65.764",
        "geo_note": "Palmer / El Yunque National Forest, Puerto Rico (USASpending place of performance).",
        "evidence": "documented",
        "source_id": "usaspending_novel_yunque_20210830",
        "note": "Actor: Novel Construction LLC (Puerto Rico / U.S.) + FHWA/FAA — us. Official USASpending Award API.",
    },
    {
        "id": "fhwa_novel_yunque_fs27_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_novel_yunque_20210830",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000023_6925_-NONE-_-NONE-/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "THE PROJECT CONSISTS OF REPAIRING TWO LANDSLIDES AT MILE POST 1.1 OF FS ROUTE 27 (FS-27) WITHIN EL YUNQUE NATIONAL FOREST FOR THE FEDERAL AVIATION ADMINISTRATION.  THE WORK INCLUDES CONSTRUCTING AN ANCHORED SOLDIER PILE WALL, GABION WALL, ROCK BUTTRE",
        "note": "Opened USASpending Award API: Novel Construction LLC; USD 6,861,239.89; date_signed 2021-08-30; PoP Palmer, PR.",
    },
    {
        "id": "usaspending_novel_yunque_20210830",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_693C7321C000023_6925_-NONE-_-NONE- (Novel Construction LLC; FHWA/FAA El Yunque FS-27 landslide repairs). Signed 30 August 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000023_6925_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7321C000023_6925_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 6.86m FHWA/FAA award to Novel for El Yunque FS-27 landslide repairs. Supports fhwa_novel_yunque_fs27_2021.",
        "supports": ["fhwa_novel_yunque_fs27_2021", "hunt_infra_bridges_roads"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
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

    hunt_updates = {
        "hunt_fenb_araxa": "Cycle 100: logged cbmm_araxa_capex_630m_2024 (allied CBMM CapEx R$630m documented). PRC Catalão CapEx not separately disclosed on opened CMOC pages (miss).",
        "hunt_energy_wind": "Cycle 100: equal budget; Envision Casa / Goldwind / Vestas dense (miss).",
        "hunt_energy_solar": "Cycle 100: equal budget; EXIM Olanchito / CCCC ENESOLAR / First Solar dense (miss).",
        "hunt_infra_port_ownership": "Cycle 100: equal budget; APM Lazaro/Suape / Hutchison ICAVE / DP World dense (miss).",
        "hunt_energy_fission_smr": "Cycle 100: equal budget; CAREM / CNNC / CONUAR dense (miss).",
        "hunt_energy_other_renewables": "Cycle 100: equal budget; Sungrow / Trina dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 100: equal budget; Halliburton / Bechtel / Fluor dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 100: equal budget; USTDA Honduras / PowerChina Chancay dense (miss).",
        "hunt_infra_port_cranes": "Cycle 100: equal budget; ZPMC Chancay / Santos / ICAVE dense (miss).",
        "hunt_br_power_equip": "Cycle 100: equal budget; GE Vernova / ENGIE / EXIM GTE dense (miss).",
        "hunt_infra_building_materials": "Cycle 100: equal budget; Sinoma dense (miss). Thin spare dry.",
        "hunt_infra_bridges_roads": "Cycle 100: logged fhwa_nieves_lares_2024 + fhwa_caribbean_sign_pr123_2021 + fhwa_jc_associates_east_2022 + fhwa_master_pavement_pr52_2021 + fhwa_jpi_maunabo_2023 + fhwa_novel_yunque_fs27_2021 (U.S. FHWA).",
        "hunt_res_water": "Cycle 100: equal budget; CCCC El Curval / Acciona dense (miss).",
        "hunt_res_balsa": "Cycle 100: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_res_nickel": "Cycle 100: equal budget; MMG / BRN dense (miss). Thin dry — shift.",
        "hunt_res_copper": "Cycle 100: equal budget; CMOC / Chinalco dense (miss).",
        "hunt_res_lithium": "Cycle 100: equal budget; Ganfeng / Yahua dense (miss).",
        "hunt_res_graphite": "Cycle 100: equal budget; Graphcoa / Atlas dense (miss). Thin dry — shift.",
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
    print("Cycle 100 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
