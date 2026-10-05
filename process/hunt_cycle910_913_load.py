#!/usr/bin/env python3
"""Cycles 910–913: USASpending Haiti US CapEx + residual PIP faces.

Seeds: 20261910–20261913. Thin top-up dry each pass (balsa/nickel/fission/niobium).
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
    bib_type="government",
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


def usa(rid, layer, sub, counterpart, asset, value, fx_date, year, lat, lon, geo, sid, quote, url, note, hunt, chicago, annotation, evid_note, investment_type="epc"):
    row_doc(
        rid, layer, sub, "us", counterpart, "Haiti", asset, value, fx_date, year, lat, lon, geo, sid, quote, url, note, hunt,
        investment_type=investment_type, chicago=chicago, annotation=annotation, evid_note=evid_note,
    )


def pip(rid, layer, sub, side, counterpart, asset, value, lat, lon, geo, quote, note, hunt, investment_type="rehabilitation"):
    row_doc(
        rid, layer, sub, side, counterpart, "Haiti", asset, value, "", "2025", lat, lon, geo, PIP_SID, quote, PIP_URL, note, hunt,
        investment_type=investment_type, currency="HTG", value_usd="", fx_usd="", chicago=PIP_CHICAGO,
        annotation=f"Haiti PIP FY2025–26 face supporting {rid}.",
        evid_note=f"Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; {rid}.",
    )


# === Cycle 910 ===
usa(
    "dfs_fort_liberte_prison_6p74m_2014",
    "infrastructure", "building_materials",
    "DFS Construction, LLC — Fort-Liberté prison compound construction",
    "11 Sep 2014: Department of State awards contract SAQMMA14C0188 to DFS Construction, LLC "
    "for construction of a prison compound in Fort-Liberté, Haiti; obligated USD 6,741,843.93. "
    "CapEx face = award obligation. Distinct from dfs_caracol_drainage_13p6m_2015.",
    "6741843.93", "2014-09-11", "2014", "19.668", "-71.838",
    "Prison compound, Fort-Liberté, Nord-Est, Haiti (USASpending PoP Haiti; Fort-Liberté pin).",
    "usaspending_dfs_fort_liberte_prison_20140911",
    "CONSTRUCTION OF A PRISON COMPOUND IN FORT LIBERTE, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0188_1900_-NONE-_-NONE-/",
    "Actor: DFS Construction, LLC (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle910",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0188_1900_-NONE-_-NONE- "
    "(DFS Construction, LLC; Fort-Liberté prison). Signed 11 September 2014. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0188_1900_-NONE-_-NONE-/.",
    "USASpending: DFS Fort-Liberté prison USD 6.742m. Supports dfs_fort_liberte_prison_6p74m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,741,843.93; date_signed 2014-09-11.",
)
usa(
    "spectrum_haiti_switchgear_7p02m_2021",
    "energy", "power_plants_grid",
    "Spectrum Electrical Services, Inc. — Haiti switchgear replacement",
    "24 Sep 2021: Department of State awards task order 19AQMM21F3866 to Spectrum Electrical "
    "Services, Inc. for Haiti switchgear replacement project; obligated USD 7,017,104.69. "
    "CapEx face = award obligation. Distinct from uep_chp_electrical_renewal_4p67m_2023 / "
    "cherokee_usembassy_pap_hvac_7p4m_2021.",
    "7017104.69", "2021-09-24", "2021", "18.540", "-72.340",
    "Haiti switchgear replacement (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_spectrum_haiti_switchgear_20210924",
    "HAITI SWITCHGEAR REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3866_1900_19AQMM18D0072_1900/",
    "Actor: Spectrum Electrical Services, Inc. (Fairfax VA, U.S.) under State — us. Official "
    "USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle910",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM21F3866_1900_19AQMM18D0072_1900 (Spectrum Electrical Services, Inc.; Haiti "
    "switchgear). Signed 24 September 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3866_1900_19AQMM18D0072_1900/.",
    "USASpending: Spectrum Haiti switchgear USD 7.017m. Supports spectrum_haiti_switchgear_7p02m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7,017,104.69; date_signed 2021-09-24.",
)
usa(
    "nathan_cap_haitien_customs_5p97m_2016",
    "infrastructure", "port_ownership",
    "Nathan Associates LLC — Cap-Haïtien customs operations (port rehab support)",
    "11 Jan 2016: USAID awards contract AID521C1600004 to Nathan Associates LLC to strengthen "
    "Cap-Haïtien customs operations to support increased trade volumes projected under the "
    "Cap-Haïtien Port rehabilitation project; obligated USD 5,973,482.79. CapEx/services face = "
    "award obligation. Distinct from nathan_cap_haitien_port_reg_3p07m_2015 / "
    "trigon_cap_haitien_cm_to_3p0m_2023.",
    "5973482.79", "2016-01-11", "2016", "19.759", "-72.201",
    "Cap-Haïtien Port customs operations, Nord, Haiti (USASpending PoP Haiti; Cap-Haïtien port pin).",
    "usaspending_nathan_cap_haitien_customs_20160111",
    "THE GOAL OF THE PROJECT IS TO ENSURE THAT CAP HAITIEN CUSTOMS OPERATIONS ARE SUFFICIENTLY "
    "EFECTIVE TO SUPPORT THE INCREASED VOLUMES OF TRADE PROJECTED IN THE CAP HAITIEN PORT "
    "REHABILITATION PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1600004_7200_-NONE-_-NONE-/",
    "Actor: Nathan Associates LLC (U.S.) under USAID — us. Official USASpending Award API. "
    "Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle910",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1600004_7200_-NONE-_-NONE- "
    "(Nathan Associates LLC; Cap-Haïtien customs). Signed 11 January 2016. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1600004_7200_-NONE-_-NONE-/.",
    "USASpending: Nathan Cap-Haïtien customs USD 5.973m. Supports nathan_cap_haitien_customs_5p97m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,973,482.79; date_signed 2016-01-11.",
    investment_type="services_contract",
)
pip(
    "haiti_pip_bm_municipal_resilience_322m_htg_fy2526",
    "infrastructure", "bridges_roads", "allied",
    "World Bank — Projet de développement municipal et de résilience urbaine (PIP FY2025–26)",
    "PIP FY2025–26 line 11141-1-25-31-10 PROJET DE DEVELOPPEMENT MUNICIPAL ET DE RESILIENCE "
    "URBAINE NATIONAL: BM DON 321,600,000 HTG = TOTAL PIP 321,600,000 HTG. CapEx/financing FY "
    "face (HTG; USD blank). Distinct from haiti_pip_cap_haitien_urbain_3762m_htg_fy2526.",
    "321600000", "", "",
    "Haiti national municipal development and urban resilience program — lat/lon blank.",
    "11141-1-25-31-10- PROJET DE DEVELOPPEMENT MUNICIPAL ET DE RESILIENCE URBAINE NATIONAL                                -                                  -                                -                                -                     321,600,000  BM  DON           321,600,000             321,600,000",
    "Actor: World Bank multilateral — allied. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle bridges_roads; Haiti under-covered.",
    "hunt_cycle910",
    investment_type="financing",
)
pip(
    "haiti_pip_drainage_pap_metro_100m_htg_fy2526",
    "resources", "water", "other",
    "MTPTC / DINEPA — Curage et entretien réseau de drainage aire métropolitaine PAP (PIP FY2025–26)",
    "PIP FY2025–26 line 1114-1-12-54-25 CURAGE ET ENTRETIEN DU RESEAU DE DRAINAGE DE L'AIRE "
    "METROPOLITAINE DE PORT-AU-PRINCE (Ouest): Trésor 100,000,000 HTG = TOTAL PIP 100,000,000 HTG. "
    "CapEx: FY PIP face (HTG; USD blank).",
    "100000000", "18.540", "-72.340",
    "Aire métropolitaine de Port-au-Prince drainage network, Ouest, Haiti (PIP localisation; approximate).",
    "1114-1-12-54-25- CURAGE ET ENTRETIEN DU RESEAU DE DRAINAGE DE L'AIRE METROPOLITAINE DE PORT-AU-PRINCE OUEST               100,000,000                                -              100,000,000                              -                                      -                               -               100,000,000",
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle water; Haiti under-covered.",
    "hunt_cycle910",
    investment_type="maintenance",
)

# === Cycle 911 ===
usa(
    "nathan_cap_haitien_port_reg_3p07m_2015",
    "infrastructure", "port_ownership",
    "Nathan Associates LLC — Cap-Haïtien Port regulatory strengthening",
    "21 Dec 2015: USAID awards contract AID521C1600003 to Nathan Associates LLC for Cap-Haïtien "
    "Port regulatory strengthening project; obligated USD 3,069,268.38. CapEx/services face = "
    "award obligation. Distinct from nathan_cap_haitien_customs_5p97m_2016.",
    "3069268.38", "2015-12-21", "2015", "19.759", "-72.201",
    "Cap-Haïtien Port regulatory strengthening, Nord, Haiti (USASpending PoP Haiti; Cap-Haïtien port pin).",
    "usaspending_nathan_cap_haitien_port_reg_20151221",
    "REQUEST OF REGULATORY STRENTHENING PROJECT CAP-HAITIEN PORT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1600003_7200_-NONE-_-NONE-/",
    "Actor: Nathan Associates LLC (U.S.) under USAID — us. Official USASpending Award API. "
    "Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle911",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1600003_7200_-NONE-_-NONE- "
    "(Nathan Associates LLC; Cap-Haïtien Port regulatory). Signed 21 December 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1600003_7200_-NONE-_-NONE-/.",
    "USASpending: Nathan Cap-Haïtien Port regulatory USD 3.069m. Supports nathan_cap_haitien_port_reg_3p07m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,069,268.38; date_signed 2015-12-21.",
    investment_type="services_contract",
)
usa(
    "cce_hnp_academy_repairs_4p97m_2011",
    "infrastructure", "building_materials",
    "Contracting Consulting Engineering LLC — HNP Academy repairs (INL)",
    "15 Feb 2011: Department of State awards order SAQMMA11F0195 to Contracting, Consulting, "
    "Engineering LLC for Haiti National Police (HNP) Academy repairs on behalf of INL/LP; "
    "obligated USD 4,966,334.47. CapEx face = award obligation. Distinct from "
    "cce_lapointe_caracol_infra_6p8m_2012 / cce_presidential_barracks_pap_9p3m_2012.",
    "4966334.47", "2011-02-15", "2011", "18.540", "-72.340",
    "Haiti National Police Academy, Haiti (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_cce_hnp_academy_20110215",
    "HAITI NATIONAL POLICE (HNP) ACADEMY REPAIRS ON BEHALF OF INL/LP.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0195_1900_SAQMMA08D0003_1900/",
    "Actor: Contracting, Consulting, Engineering LLC (U.S.) under State INL — us. Official "
    "USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle911",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA11F0195_1900_SAQMMA08D0003_1900 (CCE LLC; HNP Academy repairs). Signed 15 "
    "February 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0195_1900_SAQMMA08D0003_1900/.",
    "USASpending: CCE HNP Academy repairs USD 4.966m. Supports cce_hnp_academy_repairs_4p97m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,966,334.47; date_signed 2011-02-15.",
)
usa(
    "css_jacmel_eoc_drw_fs_2p13m_2011",
    "infrastructure", "building_materials",
    "CSS International Holdings, Inc. — Jacmel EOC / DRW / fire station",
    "12 Aug 2011: DoD awards contract N6945011C0066 to CSS International Holdings, Inc. for "
    "Emergency Operation Center, Disaster Relief Warehouse, and Fire Station in Jacmel, Haiti; "
    "obligated USD 2,128,916.43. CapEx face = award obligation. Distinct from "
    "gdg_cap_haitien_drw_1p27m_2010 / gdg_les_cayes_drw_1p19m_2010.",
    "2128916.43", "2011-08-12", "2011", "18.234", "-72.535",
    "EOC / DRW / fire station, Jacmel, Sud-Est, Haiti (USASpending PoP Haiti; Jacmel pin).",
    "usaspending_css_jacmel_eoc_20110812",
    "EMERGENCY OPERATION CENTER, DISASTER RELIEF WAREHOUSE AND FIRE STATION, JACMEL HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0066_9700_-NONE-_-NONE-/",
    "Actor: CSS International Holdings, Inc. (U.S.) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle911",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0066_9700_-NONE-_-NONE- "
    "(CSS International Holdings; Jacmel EOC/DRW/FS). Signed 12 August 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0066_9700_-NONE-_-NONE-/.",
    "USASpending: CSS Jacmel EOC/DRW/FS USD 2.129m. Supports css_jacmel_eoc_drw_fs_2p13m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,128,916.43; date_signed 2011-08-12.",
)
pip(
    "haiti_pip_dev_urbain_national_531m_htg_fy2526",
    "infrastructure", "bridges_roads", "allied",
    "UE — Développement urbain national (PIP FY2025–26)",
    "PIP FY2025–26 line 11141-1-25-31-35 DEVELOPPEMENT URBAIN NATIONAL: UE DON 531,300,000 HTG = "
    "TOTAL PIP 531,300,000 HTG. CapEx/financing FY face (HTG; USD blank). Distinct from "
    "haiti_pip_bm_municipal_resilience_322m_htg_fy2526.",
    "531300000", "", "",
    "Haiti national urban development program — lat/lon blank.",
    "11141-1-25-31-35- DEVELOPPEMENT URBAIN NATIONAL                                -                                  -                                -                                -                     531,300,000  UE  DON           531,300,000             531,300,000",
    "Actor: European Union multilateral — allied. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle bridges_roads; Haiti under-covered.",
    "hunt_cycle911",
    investment_type="financing",
)
pip(
    "haiti_pip_travaux_ponctuels_100m_htg_fy2526",
    "infrastructure", "bridges_roads", "other",
    "FER — Travaux ponctuels d'urgence (PIP FY2025–26)",
    "PIP FY2025–26 line 1114-1-12-53-72 TRAVAUX PONCTUELS D'URGENCE NATIONAL: FER 100,000,000 HTG "
    "= TOTAL PIP 100,000,000 HTG. CapEx/maintenance envelope FY face (HTG; USD blank).",
    "100000000", "", "",
    "Haiti national emergency punctual road works program — lat/lon blank.",
    "1114-1-12-53-72- TRAVAUX PONCTUELS D'URGENCE NATIONAL                                -                 100,000,000  FER            100,000,000                              -                                      -                               -               100,000,000",
    "Actor: MTPTC / FER — other. Official MPCE PIP PDF. FY face HTG; USD blank. Shuffle bridges_roads.",
    "hunt_cycle911",
    investment_type="maintenance",
)

# === Cycle 912 ===
usa(
    "css_miragoane_eoc_drw_fs_2p11m_2011",
    "infrastructure", "building_materials",
    "CSS International Holdings, Inc. — Miragoâne EOC / DRW / fire station",
    "24 Aug 2011: DoD awards contract N6945011C0068 to CSS International Holdings, Inc. for "
    "Emergency Operation Center, Disaster Relief Warehouse, and Fire Station in Miragoâne, Haiti; "
    "obligated USD 2,113,831.32. CapEx face = award obligation. Distinct from "
    "css_jacmel_eoc_drw_fs_2p13m_2011.",
    "2113831.32", "2011-08-24", "2011", "18.445", "-73.089",
    "EOC / DRW / fire station, Miragoâne, Nippes, Haiti (USASpending PoP Haiti; Miragoâne pin).",
    "usaspending_css_miragoane_eoc_20110824",
    "EMERGENCY OPERATION CENTER, DISASTER RELIEF WAREHOUSE, AND FIRE STATION MIRAGOANE, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0068_9700_-NONE-_-NONE-/",
    "Actor: CSS International Holdings, Inc. (U.S.) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle912",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0068_9700_-NONE-_-NONE- "
    "(CSS International Holdings; Miragoâne EOC/DRW/FS). Signed 24 August 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0068_9700_-NONE-_-NONE-/.",
    "USASpending: CSS Miragoâne EOC/DRW/FS USD 2.114m. Supports css_miragoane_eoc_drw_fs_2p11m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,113,831.32; date_signed 2011-08-24.",
)
usa(
    "css_fort_liberte_eoc_drw_fs_2p04m_2011",
    "infrastructure", "building_materials",
    "CSS International Holdings, Inc. — Fort-Liberté EOC / DRW / fire station",
    "5 Aug 2011: DoD awards contract N6945011C0067 to CSS International Holdings, Inc. for "
    "Emergency Operation Center, Disaster Relief Warehouse, and Fire Station in Fort-Liberté, "
    "Haiti; obligated USD 2,041,036.23. CapEx face = award obligation. Distinct from "
    "dfs_fort_liberte_prison_6p74m_2014 / css_jacmel_eoc_drw_fs_2p13m_2011.",
    "2041036.23", "2011-08-05", "2011", "19.668", "-71.838",
    "EOC / DRW / fire station, Fort-Liberté, Nord-Est, Haiti (USASpending PoP Haiti; Fort-Liberté pin).",
    "usaspending_css_fort_liberte_eoc_20110805",
    "EMERGENCY OPERATION CENTER, DISASTER RELIEF WAREHOUSE AND FIRE STATION, FORT LIBERTE HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0067_9700_-NONE-_-NONE-/",
    "Actor: CSS International Holdings, Inc. (U.S.) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle912",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0067_9700_-NONE-_-NONE- "
    "(CSS International Holdings; Fort-Liberté EOC/DRW/FS). Signed 5 August 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0067_9700_-NONE-_-NONE-/.",
    "USASpending: CSS Fort-Liberté EOC/DRW/FS USD 2.041m. Supports css_fort_liberte_eoc_drw_fs_2p04m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,041,036.23; date_signed 2011-08-05.",
)
usa(
    "olgoonik_stecher_roumain_electrical_2p87m_2020",
    "energy", "power_plants_grid",
    "Olgoonik Federal, LLC — Stecher-Roumain / Reyes warehouse electrical utility connection",
    "30 Sep 2020: Department of State awards contract 19AQMM20C0228 to Olgoonik Federal, LLC "
    "for electrical connection of Stecher-Roumain housing complex and Reyes warehouse to the "
    "local electrical utility; obligated USD 2,866,404.00. CapEx face = award obligation. "
    "Distinct from spectrum_haiti_switchgear_7p02m_2021.",
    "2866404.00", "2020-09-30", "2020", "18.540", "-72.340",
    "Stecher-Roumain housing / Reyes warehouse electrical connection, Haiti (USASpending PoP "
    "Haiti; Port-au-Prince approximate).",
    "usaspending_olgoonik_stecher_elec_20200930",
    "ELECTRICAL CONNECTION TO STECHER-ROUMAIN HOUSING COMPLEX AND REYES WAREHOUSE TO THE LOCAL "
    "ELECTRICAL UTILITY F",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0228_1900_-NONE-_-NONE-/",
    "Actor: Olgoonik Federal, LLC (U.S. Alaska Native Corp subsidiary) under State — us. Official "
    "USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle912",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0228_1900_-NONE-_-NONE- "
    "(Olgoonik Federal, LLC; Stecher-Roumain electrical). Signed 30 September 2020. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0228_1900_-NONE-_-NONE-/.",
    "USASpending: Olgoonik Stecher-Roumain electrical USD 2.866m. Supports olgoonik_stecher_roumain_electrical_2p87m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,866,404.00; date_signed 2020-09-30.",
)
row_doc(
    "palgag_gonaives_clusters_3p55m_2011",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd — Gonaïves community clusters",
    "Haiti",
    "14 Jan 2011: DoD awards contract N6945011C0029 to Palgag Building Technologies Ltd (Israel) "
    "for community clusters in Gonaïves, Haiti; obligated USD 3,554,540.43. CapEx face = award "
    "obligation. Distinct from css_jacmel_eoc_drw_fs_2p13m_2011.",
    "3554540.43", "2011-01-14", "2011", "19.450", "-72.690",
    "Community clusters, Gonaïves, Artibonite, Haiti (USASpending PoP Haiti; Gonaïves pin).",
    "usaspending_palgag_gonaives_20110114",
    "COMMUNITY CLUSTERS; GONAIVES, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0029_9700_-NONE-_-NONE-/",
    "Actor: Palgag Building Technologies Ltd (Kibutz Gaash, Israel) under DoD — allied. Official "
    "USASpending Award API. Shuffle building_materials.",
    "hunt_cycle912",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_N6945011C0029_9700_-NONE-_-NONE- (Palgag Building Technologies Ltd; Gonaïves "
        "community clusters). Signed 14 January 2011. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0029_9700_-NONE-_-NONE-/."
    ),
    annotation="USASpending: Palgag Gonaïves clusters USD 3.555m. Supports palgag_gonaives_clusters_3p55m_2011.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 3,554,540.43; recipient Israel.",
)
pip(
    "haiti_pip_etudes_routes_50m_htg_fy2526",
    "infrastructure", "bridges_roads", "other",
    "MTPTC — Études de réhabilitation et construction de routes d'intégration locale (PIP FY2025–26)",
    "PIP FY2025–26 line 11141-1-25-32-04 ETUDES DE REHABILITATION ET CONSTRUCTION DE ROUTES "
    "D'INTEGRATION LOCALE NATIONAL: Trésor 50,000,000 HTG = TOTAL PIP 50,000,000 HTG. CapEx/study "
    "FY face (HTG; USD blank). Distinct from haiti_pip_integration_routiere_locale_527m_htg_fy2526.",
    "50000000", "", "",
    "Haiti national local road-integration studies program — lat/lon blank.",
    "11141-1-25-32-04- ETUDES DE REHABILITATION ET CONSTRUCTION DE ROUTES D'INTEGRATION LOCALE NATIONAL                 50,000,000                                -                50,000,000                              -                                      -                               -                 50,000,000",
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle bridges_roads.",
    "hunt_cycle912",
    investment_type="other",
)

# === Cycle 913 ===
usa(
    "global_communities_nazon_debris_3p39m_2011",
    "infrastructure", "building_materials",
    "Global Communities, Inc. — Nazon earthquake debris removal (Port-au-Prince)",
    "14 Jan 2011: USAID awards contract AID521C001100004 to Global Communities, Inc. to remove "
    "earthquake debris in the Nazon area of Port-au-Prince and transport it to the Truitier "
    "landfill dump site to clear sites for transitional shelter construction; obligated USD "
    "3,389,117.88. CapEx face = award obligation.",
    "3389117.88", "2011-01-14", "2011", "18.540", "-72.340",
    "Nazon debris clearance / Truitier landfill corridor, Port-au-Prince, Haiti (USASpending PoP Haiti).",
    "usaspending_global_communities_nazon_20110114",
    "THIS IS A CONTRACT TO REMOVE EARTHQUAKE DEBRIS IN THE NAZON AREA OF PORT AU PRINCE, HAITI "
    "AND TO TRANSPORT IT TO THE TRUITIER LANDFILL DUMP SITE IN ORDER TO MAKE THE CLEARED SITES "
    "AVAILABLE FOR CONSTRUCTION OF TRANSITIONAL SHELTERS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001100004_7200_-NONE-_-NONE-/",
    "Actor: Global Communities, Inc. (U.S.) under USAID — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle913",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_AID521C001100004_7200_-NONE-_-NONE- (Global Communities; Nazon debris). Signed 14 "
    "January 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001100004_7200_-NONE-_-NONE-/.",
    "USASpending: Global Communities Nazon debris USD 3.389m. Supports global_communities_nazon_debris_3p39m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,389,117.88; date_signed 2011-01-14.",
)
usa(
    "palgag_us_modular_1p73m_2016",
    "infrastructure", "building_materials",
    "Palgag US LLC — Haiti modular construction",
    "18 Apr 2016: Department of State awards contract SAQMMA16C0099 to Palgag US LLC for Haiti "
    "modular construction; obligated USD 1,727,009.56. CapEx face = award obligation. Distinct "
    "from palgag_gonaives_clusters_3p55m_2011 (Israeli parent entity).",
    "1727009.56", "2016-04-18", "2016", "18.540", "-72.340",
    "Haiti modular construction (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_palgag_us_modular_20160418",
    "HAITI MODULAR CONSTRUCTION CONTRACT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0099_1900_-NONE-_-NONE-/",
    "Actor: Palgag US LLC (U.S. entity) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle913",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16C0099_1900_-NONE-_-NONE- "
    "(Palgag US LLC; Haiti modular). Signed 18 April 2016. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0099_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag US modular USD 1.727m. Supports palgag_us_modular_1p73m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,727,009.56; date_signed 2016-04-18.",
)
row_doc(
    "palgag_port_de_paix_eoc_1p93m_2011",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd — Port-de-Paix EOC / DRW / fire station",
    "Haiti",
    "26 Sep 2011: DoD awards contract N6945011C0060 to Palgag Building Technologies Ltd (Israel) "
    "for EOC, DRW, and fire station in Port-de-Paix, Haiti; obligated USD 1,932,723.48. CapEx "
    "face = award obligation. Distinct from palgag_gonaives_clusters_3p55m_2011 / "
    "css_jacmel_eoc_drw_fs_2p13m_2011.",
    "1932723.48", "2011-09-26", "2011", "19.940", "-72.830",
    "EOC / DRW / fire station, Port-de-Paix, Nord-Ouest, Haiti (USASpending PoP Haiti; Port-de-Paix pin).",
    "usaspending_palgag_port_de_paix_20110926",
    "EOC, DRW AND FIRE STATION PORT DE PAIX HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0060_9700_-NONE-_-NONE-/",
    "Actor: Palgag Building Technologies Ltd (Israel) under DoD — allied. Official USASpending "
    "Award API. Shuffle building_materials.",
    "hunt_cycle913",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_N6945011C0060_9700_-NONE-_-NONE- (Palgag Building Technologies Ltd; Port-de-Paix "
        "EOC/DRW/FS). Signed 26 September 2011. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0060_9700_-NONE-_-NONE-/."
    ),
    annotation="USASpending: Palgag Port-de-Paix EOC USD 1.933m. Supports palgag_port_de_paix_eoc_1p93m_2011.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 1,932,723.48; recipient Israel.",
)
pip(
    "haiti_pip_rue_des_hall_delmas_18m_htg_fy2526",
    "infrastructure", "bridges_roads", "other",
    "MTPTC — Réhabilitation de la Rue des Hall à Delmas (PIP FY2025–26)",
    "PIP FY2025–26 line 11141-1-25-31-17 REHABILITATION DE LA RUE DES HALL A DELMAS (Ouest): "
    "Trésor 18,296,750 HTG = TOTAL PIP 18,296,750 HTG. CapEx: FY PIP face (HTG; USD blank).",
    "18296750", "18.550", "-72.300",
    "Rue des Hall, Delmas, Ouest, Haiti (PIP localisation; approximate).",
    "11141-1-25-31-17- REHABILITATION DE LA RUE DES HALL A DELMAS OUEST                 18,296,750                                -                18,296,750                              -                                      -                               -                 18,296,750",
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle bridges_roads.",
    "hunt_cycle913",
)
pip(
    "haiti_pip_drainage_ouanaminthe_20m_htg_fy2526",
    "resources", "water", "other",
    "MTPTC — Curage au centre-ville de Ouanaminthe 7 km (PIP FY2025–26)",
    "PIP FY2025–26 line 1114-1-12-54-27 CURAGE AU CENTRE VILLE DE OUANAMINTHE (7KM) (Nord-Est): "
    "Trésor 20,000,000 HTG = TOTAL PIP 20,000,000 HTG. CapEx: FY PIP face (HTG; USD blank). "
    "Distinct from haiti_pip_drainage_pap_metro_100m_htg_fy2526 / "
    "haiti_pip_betonnage_ouanaminthe_100m_htg_fy2526.",
    "20000000", "19.550", "-71.730",
    "Centre-ville drainage curage 7 km, Ouanaminthe, Nord-Est, Haiti (PIP localisation; approximate).",
    "1114-1-12-54-27- CURAGE AU CENTRE VILLE DE OUANAMINTHE (7KM) NORD-EST                 20,000,000                                -                20,000,000                              -                                      -                               -                 20,000,000",
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle water.",
    "hunt_cycle913",
    investment_type="maintenance",
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
    print(f"cycles910-913 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
