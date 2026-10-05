#!/usr/bin/env python3
"""Cycles 1236–1241: USASpending LatAm CapEx (US vendor stock + residual other).

Seeds: 20262236–20262241. Thin top-up dry.
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
    rid, layer, sub, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, sid, quote, url, note, hunt, chicago, annotation, evid_note,
    investment_type="epc",
):
    A(
        {
            "id": rid, "layer": layer, "subcategory": sub, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": "USD",
            "value_usd": value, "fx_usd": "1", "fx_date": fx_date, "year": year,
            "status": "active", "lat": lat, "lon": lon, "geo_note": geo,
            "evidence": "documented", "source_id": sid, "note": note,
            "pair_id": "", "counterpart_side": "", "counterpart_actor": "",
            "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-05", "source_id": sid, "url": url,
            "price_year": year, "evidence": "documented", "quote": quote, "note": evid_note,
        },
        {
            "id": sid, "type": "government", "chicago": chicago, "url": url,
            "accessed": "2026-10-05", "annotation": annotation, "supports": [rid, hunt],
        },
    )

# === Cycle 1236 ===
row_doc(
    "koniag_ecuador_esps_installation_299k_2013",
    "infrastructure", "building_materials", "us",
    "Koniag Technology Solutions — Ecuador environmental security protection system installation",
    "Ecuador",
    "29 Sep 2013: Department of State awards task order to KONIAG TECHNOLOGY SOLUTIONS INC for installation of an environmental security protection system (PoP Ecuador); obligated USD 298909.78. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "298909.78", "2013-09-29", "2013", "", "",
    "IGF::CL::IGF  INSTALLATION OF AN ENVIRONMENTAL SECURITY PROTECTION SYSTEM AT THE US EMBASSY LOCAT..., Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_koniag_ecuador_esps_installation_299k_2013",
    "IGF::CL::IGF  INSTALLATION OF AN ENVIRONMENTAL SECURITY PROTECTION SYSTEM AT THE US EMBASSY LOCATED IN QUITO, ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F4034_1900_SAQMMA13D0121_1900/",
    "Actor: KONIAG TECHNOLOGY SOLUTIONS INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1236",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F4034_1900_SAQMMA13D0121_1900 (koniag_ecuador_esps_installation_299k_2013). Signed 2013-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F4034_1900_SAQMMA13D0121_1900/.",
    "USASpending: koniag_ecuador_esps_installation_299k_2013 USD 0.299m. Supports koniag_ecuador_esps_installation_299k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 298909.78; date_signed 2013-09-29.",
)

# === Cycle 1236 ===
row_doc(
    "ped_concepts_jamaica_classroom_bathroom_714k_2024",
    "infrastructure", "building_materials", "us",
    "PED Concepts — Jamaica design-build classroom and bathroom",
    "Jamaica",
    "22 Apr 2024: Department of Defense awards contract to PED CONCEPTS INC. for design-build classroom and bathroom (PoP Jamaica); obligated USD 714160.78. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "714160.78", "2024-04-22", "2024", "", "",
    "DB CLASSROOM AND BATHROOM, Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_ped_concepts_jamaica_classroom_bathroom_714k_2024",
    "DB CLASSROOM AND BATHROOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945024C0025_9700_-NONE-_-NONE-/",
    "Actor: PED CONCEPTS INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1236",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945024C0025_9700_-NONE-_-NONE- (ped_concepts_jamaica_classroom_bathroom_714k_2024). Signed 2024-04-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945024C0025_9700_-NONE-_-NONE-/.",
    "USASpending: ped_concepts_jamaica_classroom_bathroom_714k_2024 USD 0.714m. Supports ped_concepts_jamaica_classroom_bathroom_714k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 714160.78; date_signed 2024-04-22.",
)

# === Cycle 1236 ===
row_doc(
    "misc_colombia_tolemaida_cctv_replacement_530k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia replacement CCTV cameras Tolemaida",
    "Colombia",
    "26 Sep 2010: Department of Defense awards contract for replacement CCTV cameras Tolemaida (PoP Colombia); obligated USD 530294.02. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "530294.02", "2010-09-26", "2010", "", "",
    "REPLACEMENT CCTV CAMERAS TOLEMAIDA, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_tolemaida_cctv_replacement_530k_2010",
    "REPLACEMENT CCTV CAMERAS TOLEMAIDA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0048_9700_-NONE-_-NONE-/",
    "Actor: INECON SAS — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1236",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0048_9700_-NONE-_-NONE- (misc_colombia_tolemaida_cctv_replacement_530k_2010). Signed 2010-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0048_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_tolemaida_cctv_replacement_530k_2010 USD 0.530m. Supports misc_colombia_tolemaida_cctv_replacement_530k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 530294.02; date_signed 2010-09-26.",
)

# === Cycle 1236 ===
row_doc(
    "proyectos_civiles_panama_medical_clinic_reno_512k_2011",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Panama medical clinic renovation and storage/lab construction",
    "Panama",
    "26 Sep 2011: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA for humanitarian project renovation of existing medical clinic and construction of storage room and lab (PoP Panama); obligated USD 511740.42. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "511740.42", "2011-09-26", "2011", "", "",
    "HUMANITARIAN PROJECT #6718 FOR RENOVATION OF EXISTING MEDICAL CLINIC AND CONSTRUT STORAGES ROOM A..., Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_proyectos_civiles_panama_medical_clinic_reno_512k_2011",
    "HUMANITARIAN PROJECT #6718 FOR RENOVATION OF EXISTING MEDICAL CLINIC AND CONSTRUT STORAGES ROOM AND LAB.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0041_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1236",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0041_9700_-NONE-_-NONE- (proyectos_civiles_panama_medical_clinic_reno_512k_2011). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0041_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_civiles_panama_medical_clinic_reno_512k_2011 USD 0.512m. Supports proyectos_civiles_panama_medical_clinic_reno_512k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 511740.42; date_signed 2011-09-26.",
)

# === Cycle 1236 ===
row_doc(
    "misc_mexico_reynosa_ecloison_security_upgrade_501k_2012",
    "infrastructure", "building_materials", "other",
    "Foreign awardees — Mexico APHIS MFF eclosion facility security upgrade Reynosa",
    "Mexico",
    "9 Sep 2012: Department of Agriculture awards contract for APHIS IS MFF eclosion facility security upgrade Reynosa, MX (PoP Mexico); obligated USD 501444.42. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "501444.42", "2012-09-09", "2012", "", "",
    "IGF::OT::IGF APHIS IS MFF ECLOSION FACILITY SECURITY UPGRADE REYNOSA, MX, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_reynosa_ecloison_security_upgrade_501k_2012",
    "IGF::OT::IGF APHIS IS MFF ECLOSION FACILITY SECURITY UPGRADE REYNOSA, MX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWC120014_12K3_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1236",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AG32KWC120014_12K3_-NONE-_-NONE- (misc_mexico_reynosa_ecloison_security_upgrade_501k_2012). Signed 2012-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWC120014_12K3_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_reynosa_ecloison_security_upgrade_501k_2012 USD 0.501m. Supports misc_mexico_reynosa_ecloison_security_upgrade_501k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 501444.42; date_signed 2012-09-09.",
)

# === Cycle 1237 ===
row_doc(
    "lincoln_colombia_portable_generators_110k_2011",
    "energy", "power_plants_grid", "us",
    "Lincoln Contractors Supply — Colombia COLAR AV CNP ERAD portable generators",
    "Colombia",
    "3 Feb 2011: Department of State awards contract to LINCOLN CONTRACTORS SUPPLY, INC. for COLAR AV CNP ERAD purchase portable generators (PoP Colombia); obligated USD 110355.84. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "110355.84", "2011-02-03", "2011", "", "",
    "COLAR AV CNP ERAD PURCHASE PORTABLE GENERATORS, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_lincoln_colombia_portable_generators_110k_2011",
    "COLAR AV CNP ERAD PURCHASE PORTABLE GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M0506_1900_-NONE-_-NONE-/",
    "Actor: LINCOLN CONTRACTORS SUPPLY (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1237",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15011M0506_1900_-NONE-_-NONE- (lincoln_colombia_portable_generators_110k_2011). Signed 2011-02-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M0506_1900_-NONE-_-NONE-/.",
    "USASpending: lincoln_colombia_portable_generators_110k_2011 USD 0.110m. Supports lincoln_colombia_portable_generators_110k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 110355.84; date_signed 2011-02-03.",
)

# === Cycle 1237 ===
row_doc(
    "mjl_cuba_residence_diesel_generators_92k_2011",
    "energy", "power_plants_grid", "us",
    "MJL Enterprises — Cuba diesel generators for residences with transfer switches",
    "Cuba",
    "2 Sep 2011: Department of State awards contract to MJL ENTERPRISES, LLC for diesel generators for residences + transfer switches (PoP Cuba); obligated USD 92018. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "92018", "2011-09-02", "2011", "", "",
    "DIESEL GENERATORS FOR RESIDENCES + TRANSFER SWITCHES., Cuba (USASpending description; site not named — lat/lon blank).",
    "usaspending_mjl_cuba_residence_diesel_generators_92k_2011",
    "DIESEL GENERATORS FOR RESIDENCES + TRANSFER SWITCHES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCU04011M0423_1900_-NONE-_-NONE-/",
    "Actor: MJL ENTERPRISES (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1237",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCU04011M0423_1900_-NONE-_-NONE- (mjl_cuba_residence_diesel_generators_92k_2011). Signed 2011-09-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCU04011M0423_1900_-NONE-_-NONE-/.",
    "USASpending: mjl_cuba_residence_diesel_generators_92k_2011 USD 0.092m. Supports mjl_cuba_residence_diesel_generators_92k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92018.0; date_signed 2011-09-02.",
)

# === Cycle 1237 ===
row_doc(
    "eterna_honduras_osc_renovations_494k_2016",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras OSC renovations under SOFA agreement",
    "Honduras",
    "28 Sep 2016: Department of Defense awards task order to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for SOFA agreement OSC renovations (PoP Honduras); obligated USD 494215.21. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "494215.21", "2016-09-28", "2016", "", "",
    "IGF::OT::IGF  SOFA AGREEMENT  OSC RENOVATIONS, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_eterna_honduras_osc_renovations_494k_2016",
    "IGF::OT::IGF  SOFA AGREEMENT  OSC RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1237",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127816D0102_9700 (eterna_honduras_osc_renovations_494k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_osc_renovations_494k_2016 USD 0.494m. Supports eterna_honduras_osc_renovations_494k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 494215.21; date_signed 2016-09-28.",
)

# === Cycle 1237 ===
row_doc(
    "eterna_belize_mlo_expansion_renovation_448k_2017",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Belize MLO expansion and renovation",
    "Belize",
    "28 Sep 2017: Department of Defense awards task order to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for MLO expansion and renovation (PoP Belize); obligated USD 448000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "448000", "2017-09-28", "2017", "", "",
    "IGF::OT::IGF MLO EXPANSION&RENOVATION, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_eterna_belize_mlo_expansion_renovation_448k_2017",
    "IGF::OT::IGF MLO EXPANSION&RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0465_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1237",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0465_9700_W9127816D0102_9700 (eterna_belize_mlo_expansion_renovation_448k_2017). Signed 2017-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0465_9700_W9127816D0102_9700/.",
    "USASpending: eterna_belize_mlo_expansion_renovation_448k_2017 USD 0.448m. Supports eterna_belize_mlo_expansion_renovation_448k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 448000.0; date_signed 2017-09-28.",
)

# === Cycle 1237 ===
row_doc(
    "barrail_paraguay_cmr_make_ready_443k_2016",
    "infrastructure", "building_materials", "other",
    "Barrail Hnos. — Paraguay alterations/make-ready improvements for new CMR",
    "Paraguay",
    "23 May 2016: Department of State awards contract to BARRAIL HNOS. S.A. DE CONSTRUCCIONES for alterations/make-ready improvements for the new CMR (PoP Paraguay); obligated USD 442581.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "442581.44", "2016-05-23", "2016", "", "",
    "IGF::OT::IGF  ALTERATIONS / MAKE-READY IMPROVEMENTS FOR THE NEW CMR, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_barrail_paraguay_cmr_make_ready_443k_2016",
    "IGF::OT::IGF  ALTERATIONS / MAKE-READY IMPROVEMENTS FOR THE NEW CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50016C0012_1900_-NONE-_-NONE-/",
    "Actor: BARRAIL HNOS. S.A. DE CONSTRUCCIONES — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1237",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50016C0012_1900_-NONE-_-NONE- (barrail_paraguay_cmr_make_ready_443k_2016). Signed 2016-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50016C0012_1900_-NONE-_-NONE-/.",
    "USASpending: barrail_paraguay_cmr_make_ready_443k_2016 USD 0.443m. Supports barrail_paraguay_cmr_make_ready_443k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 442581.44; date_signed 2016-05-23.",
)

# === Cycle 1238 ===
row_doc(
    "pinnacle_guyana_tradewinds_flood_light_towers_87k_2023",
    "energy", "power_plants_grid", "us",
    "Pinnacle Business Services — Guyana Tradewinds flood light towers",
    "Guyana",
    "15 Jun 2023: Department of Defense awards contract to PINNACLE BUSINESS SERVICES INC. for flood light towers in support of Tradewinds (PoP Guyana); obligated USD 87153. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "87153", "2023-06-15", "2023", "", "",
    "FLOOD LIGHT TOWERS IN SUPPORT OF TRADEWINDS, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_pinnacle_guyana_tradewinds_flood_light_towers_87k_2023",
    "FLOOD LIGHT TOWERS IN SUPPORT OF TRADEWINDS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE23P0042_9700_-NONE-_-NONE-/",
    "Actor: PINNACLE BUSINESS SERVICES INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1238",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W569QE23P0042_9700_-NONE-_-NONE- (pinnacle_guyana_tradewinds_flood_light_towers_87k_2023). Signed 2023-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE23P0042_9700_-NONE-_-NONE-/.",
    "USASpending: pinnacle_guyana_tradewinds_flood_light_towers_87k_2023 USD 0.087m. Supports pinnacle_guyana_tradewinds_flood_light_towers_87k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87153.0; date_signed 2023-06-15.",
)

# === Cycle 1238 ===
row_doc(
    "export_220volt_brazil_make_ready_transformers_82k_2022",
    "energy", "power_plants_grid", "us",
    "Export 220Volt — Brazil Brasília transformers for make-ready residences",
    "Brazil",
    "11 Mar 2022: Department of State awards contract to EXPORT 220VOLT INC. for transformers for make-ready residences FAP (PoP Brazil); obligated USD 81800. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "81800", "2022-03-11", "2022", "", "",
    "BSB | PSW |  TRANSFORMERS FOR MAKE READY RESIDENCES - FAP, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_export_220volt_brazil_make_ready_transformers_82k_2022",
    "BSB | PSW |  TRANSFORMERS FOR MAKE READY RESIDENCES - FAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P0303_1900_-NONE-_-NONE-/",
    "Actor: EXPORT 220VOLT INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1238",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2522P0303_1900_-NONE-_-NONE- (export_220volt_brazil_make_ready_transformers_82k_2022). Signed 2022-03-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P0303_1900_-NONE-_-NONE-/.",
    "USASpending: export_220volt_brazil_make_ready_transformers_82k_2022 USD 0.082m. Supports export_220volt_brazil_make_ready_transformers_82k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 81800.0; date_signed 2022-03-11.",
)

# === Cycle 1238 ===
row_doc(
    "serrano_peru_namru_cctv_lighting_317k_2025",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — Peru NAMRU South Naval Hospital Iquitos CCTV cameras and lighting",
    "Peru",
    "29 Sep 2025: Department of Defense awards task order to SERRANO PROANO DISENO Y CONSTRUCCION S.A. for design and construction of installation of CCTV cameras and lighting, NAMRU South Naval Hospital, Iquitos, Peru (PoP Peru); obligated USD 316677.23. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "316677.23", "2025-09-29", "2025", "", "",
    "DESIGN AND CONSTRUCTION OF INSTALLATION OF CCTV CAMERAS AND LIGHTING, NAMRU SOUTH NAVAL HOSPITAL,..., Peru (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_serrano_peru_namru_cctv_lighting_317k_2025",
    "DESIGN AND CONSTRUCTION OF INSTALLATION OF CCTV CAMERAS AND LIGHTING, NAMRU SOUTH NAVAL HOSPITAL, IQUITOS, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA301_9700_W9127824D0077_9700/",
    "Actor: SERRANO PROANO DISENO Y CONSTRUCCION S.A. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1238",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA301_9700_W9127824D0077_9700 (serrano_peru_namru_cctv_lighting_317k_2025). Signed 2025-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA301_9700_W9127824D0077_9700/.",
    "USASpending: serrano_peru_namru_cctv_lighting_317k_2025 USD 0.317m. Supports serrano_peru_namru_cctv_lighting_317k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 316677.23; date_signed 2025-09-29.",
)

# === Cycle 1238 ===
row_doc(
    "serrano_peru_repair_replace_cctv_293k_2022",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — Peru repair/replace CCTV system",
    "Peru",
    "9 Nov 2022: Department of Defense awards task order to SERRANO PROANO DISENO Y CONSTRUCCION S.A. for repair/replace CCTV system (PoP Peru); obligated USD 292644.28. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "292644.28", "2022-11-09", "2022", "", "",
    "REPAIR/REPLACE CCTV SYSTEM, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_serrano_peru_repair_replace_cctv_293k_2022",
    "REPAIR/REPLACE CCTV SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0005_9700_W9127818D0034_9700/",
    "Actor: SERRANO PROANO DISENO Y CONSTRUCCION S.A. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1238",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0005_9700_W9127818D0034_9700 (serrano_peru_repair_replace_cctv_293k_2022). Signed 2022-11-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0005_9700_W9127818D0034_9700/.",
    "USASpending: serrano_peru_repair_replace_cctv_293k_2022 USD 0.293m. Supports serrano_peru_repair_replace_cctv_293k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 292644.28; date_signed 2022-11-09.",
)

# === Cycle 1238 ===
row_doc(
    "misc_el_salvador_bth_erc_renovations_275k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador BTH 2013 ERC project renovations",
    "El Salvador",
    "18 Jan 2013: Department of Defense awards contract for BTH 2013 ERC project renovations — El Salvador (PoP El Salvador); obligated USD 274846.88. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "274846.88", "2013-01-18", "2013", "", "",
    "BTH 2013 ERC PROJECT RENOVATIONS - EL SALVADOR, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_bth_erc_renovations_275k_2013",
    "BTH 2013 ERC PROJECT RENOVATIONS - EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM13C0001_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1238",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM13C0001_9700_-NONE-_-NONE- (misc_el_salvador_bth_erc_renovations_275k_2013). Signed 2013-01-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM13C0001_9700_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_bth_erc_renovations_275k_2013 USD 0.275m. Supports misc_el_salvador_bth_erc_renovations_275k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 274846.88; date_signed 2013-01-18.",
)

# === Cycle 1239 ===
row_doc(
    "federal_contracts_mexico_semar_light_towers_79k_2012",
    "energy", "power_plants_grid", "us",
    "Federal Contracts — Mexico SEMAR compact heavy duty light towers",
    "Mexico",
    "6 Nov 2012: Department of State awards contract to FEDERAL CONTRACTS LLC for NAS-MI-01281202-SEMAR compact heavy duty light towers (PoP Mexico); obligated USD 79034.13. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "79034.13", "2012-11-06", "2012", "", "",
    "NAS-MI-01281202-SEMAR-COMPACT HEAVY DUTY LIGHT TOWERS, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_federal_contracts_mexico_semar_light_towers_79k_2012",
    "NAS-MI-01281202-SEMAR-COMPACT HEAVY DUTY LIGHT TOWERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90013M0060_1900_-NONE-_-NONE-/",
    "Actor: FEDERAL CONTRACTS LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1239",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX90013M0060_1900_-NONE-_-NONE- (federal_contracts_mexico_semar_light_towers_79k_2012). Signed 2012-11-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90013M0060_1900_-NONE-_-NONE-/.",
    "USASpending: federal_contracts_mexico_semar_light_towers_79k_2012 USD 0.079m. Supports federal_contracts_mexico_semar_light_towers_79k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79034.13; date_signed 2012-11-06.",
)

# === Cycle 1239 ===
row_doc(
    "federal_contracts_mexico_semar_light_towers_72k_2012",
    "energy", "power_plants_grid", "us",
    "Federal Contracts — Mexico SEMAR compact heavy duty light towers (second award)",
    "Mexico",
    "21 Jun 2012: Department of State awards contract to FEDERAL CONTRACTS LLC for NAS-MI-01281202 (SEMAR) compact heavy duty light towers (PoP Mexico); obligated USD 72482.85. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "72482.85", "2012-06-21", "2012", "", "",
    "NAS - MI - 01281202 (SEMAR)- COMPACT HEAVY DUTY LIGHT TOWERS, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_federal_contracts_mexico_semar_light_towers_72k_2012",
    "NAS - MI - 01281202 (SEMAR)- COMPACT HEAVY DUTY LIGHT TOWERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1169_1900_-NONE-_-NONE-/",
    "Actor: FEDERAL CONTRACTS LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1239",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M1169_1900_-NONE-_-NONE- (federal_contracts_mexico_semar_light_towers_72k_2012). Signed 2012-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1169_1900_-NONE-_-NONE-/.",
    "USASpending: federal_contracts_mexico_semar_light_towers_72k_2012 USD 0.072m. Supports federal_contracts_mexico_semar_light_towers_72k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 72482.85; date_signed 2012-06-21.",
)

# === Cycle 1239 ===
row_doc(
    "misc_honduras_prop_generators_264k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras PROP generators program",
    "Honduras",
    "30 Sep 2010: Department of State awards contract for PROP-generators (program) (PoP Honduras); obligated USD 264282. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "264282", "2010-09-30", "2010", "", "",
    "PROP-GENERATORS(PROGRAM) 1900.0, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_prop_generators_264k_2010",
    "PROP-GENERATORS(PROGRAM) 1900.0",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80010M0491_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1239",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80010M0491_1900_-NONE-_-NONE- (misc_honduras_prop_generators_264k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80010M0491_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_prop_generators_264k_2010 USD 0.264m. Supports misc_honduras_prop_generators_264k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 264282.0; date_signed 2010-09-30.",
)

# === Cycle 1239 ===
row_doc(
    "misc_costa_rica_obc_fcu_replacement_223k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica OBC-FCU replacement project floors 1&2",
    "Costa Rica",
    "22 Sep 2020: Department of State awards contract for restoration — OBC-FCU replacement project 1&2 floor (PoP Costa Rica); obligated USD 223263.43. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "223263.43", "2020-09-22", "2020", "", "",
    "RESTORATION - OBC-FCU REPLACEMENT PROJECT 1&2 FLOOR, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_costa_rica_obc_fcu_replacement_223k_2020",
    "RESTORATION - OBC-FCU REPLACEMENT PROJECT 1&2 FLOOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8020C0003_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1239",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8020C0003_1900_-NONE-_-NONE- (misc_costa_rica_obc_fcu_replacement_223k_2020). Signed 2020-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8020C0003_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_obc_fcu_replacement_223k_2020 USD 0.223m. Supports misc_costa_rica_obc_fcu_replacement_223k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 223263.43; date_signed 2020-09-22.",
)

# === Cycle 1239 ===
row_doc(
    "misc_ecuador_hvac_system_equipment_223k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador HVAC system equipment",
    "Ecuador",
    "29 Sep 2022: Department of State awards contract for FAC HVAC system equipment (PoP Ecuador); obligated USD 222571.29. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "222571.29", "2022-09-29", "2022", "", "",
    "FAC-7901SRVC-PR10820271-COMP-PMSC#58-HVAC SYSTEM EQUIPMENT, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_hvac_system_equipment_223k_2022",
    "FAC-7901SRVC-PR10820271-COMP-PMSC#58-HVAC SYSTEM EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0022_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1239",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0022_1900_-NONE-_-NONE- (misc_ecuador_hvac_system_equipment_223k_2022). Signed 2022-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0022_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_hvac_system_equipment_223k_2022 USD 0.223m. Supports misc_ecuador_hvac_system_equipment_223k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 222571.29; date_signed 2022-09-29.",
)

# === Cycle 1240 ===
row_doc(
    "walz_krenzer_cuba_metal_door_replacement_63k_2023",
    "infrastructure", "building_materials", "us",
    "Walz & Krenzer — Cuba metal door replacement",
    "Cuba",
    "3 May 2023: Department of State awards contract to WALZ & KRENZER INC for metal door replacement (PoP Cuba); obligated USD 62638.34. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "62638.34", "2023-05-03", "2023", "", "",
    "METAL DOOR REPLACEMENT, Cuba (USASpending description; site not named — lat/lon blank).",
    "usaspending_walz_krenzer_cuba_metal_door_replacement_63k_2023",
    "METAL DOOR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CU0423P0167_1900_-NONE-_-NONE-/",
    "Actor: WALZ & KRENZER INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1240",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CU0423P0167_1900_-NONE-_-NONE- (walz_krenzer_cuba_metal_door_replacement_63k_2023). Signed 2023-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CU0423P0167_1900_-NONE-_-NONE-/.",
    "USASpending: walz_krenzer_cuba_metal_door_replacement_63k_2023 USD 0.063m. Supports walz_krenzer_cuba_metal_door_replacement_63k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62638.34; date_signed 2023-05-03.",
)

# === Cycle 1240 ===
row_doc(
    "norshield_cuba_metal_door_screen_41k_2018",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Cuba metal door screen",
    "Cuba",
    "6 Feb 2018: Department of State awards contract to NORSHIELD SECURITY PRODUCTS, LLC for metal door screen etc. (PoP Cuba); obligated USD 40603. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "40603", "2018-02-06", "2018", "", "",
    "METAL DOOR SCREEN ETC., Cuba (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_cuba_metal_door_screen_41k_2018",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0354_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1240",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P0354_1900_-NONE-_-NONE- (norshield_cuba_metal_door_screen_41k_2018). Signed 2018-02-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0354_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_cuba_metal_door_screen_41k_2018 USD 0.041m. Supports norshield_cuba_metal_door_screen_41k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 40603.0; date_signed 2018-02-06.",
)

# === Cycle 1240 ===
row_doc(
    "misc_colombia_dipol_cctv_bogota_218k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia CCTV system for CNP DIPOL class Bogotá",
    "Colombia",
    "22 Mar 2013: Department of State awards contract for CCTV system for CNP DIPOL class Bogotá (PoP Colombia); obligated USD 218198.37. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "218198.37", "2013-03-22", "2013", "", "",
    "INTERD (D). CCTV SYSTEM FOR CNP DIPOL AT BOGOTA., Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_dipol_cctv_bogota_218k_2013",
    "INTERD (D). CCTV SYSTEM FOR CNP DIPOL AT BOGOTA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0619_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1240",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15013M0619_1900_-NONE-_-NONE- (misc_colombia_dipol_cctv_bogota_218k_2013). Signed 2013-03-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0619_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_dipol_cctv_bogota_218k_2013 USD 0.218m. Supports misc_colombia_dipol_cctv_bogota_218k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 218198.37; date_signed 2013-03-22.",
)

# === Cycle 1240 ===
row_doc(
    "misc_peru_carpet_make_ready_13k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru carpet wall-to-wall replacement DCR make-ready",
    "Peru",
    "26 Jul 2017: Department of State awards contract for carpet wall to wall replacement DCR due make ready (PoP Peru); obligated USD 13355.83. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13355.83", "2017-07-26", "2017", "", "",
    "CARPET WALL TO WALL REPLACEMENT DCR DUE MAKE READY, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_carpet_make_ready_13k_2017",
    "CARPET WALL TO WALL REPLACEMENT DCR DUE MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017M1844_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1240",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50017M1844_1900_-NONE-_-NONE- (misc_peru_carpet_make_ready_13k_2017). Signed 2017-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017M1844_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_carpet_make_ready_13k_2017 USD 0.013m. Supports misc_peru_carpet_make_ready_13k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13355.83; date_signed 2017-07-26.",
)

# === Cycle 1240 ===
row_doc(
    "misc_mexico_epoxy_sealer_floors_labs_13k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico epoxy sealer to floors labs",
    "Mexico",
    "13 Sep 2019: Department of State awards contract for epoxy sealer to floors labs (PoP Mexico); obligated USD 12935.59. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12935.59", "2019-09-13", "2019", "", "",
    "EPOXY SEALER TO FLOORS LABS, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_epoxy_sealer_floors_labs_13k_2019",
    "EPOXY SEALER TO FLOORS LABS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX7219P0310_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1240",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX7219P0310_1900_-NONE-_-NONE- (misc_mexico_epoxy_sealer_floors_labs_13k_2019). Signed 2019-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX7219P0310_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_epoxy_sealer_floors_labs_13k_2019 USD 0.013m. Supports misc_mexico_epoxy_sealer_floors_labs_13k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12935.59; date_signed 2019-09-13.",
)

# === Cycle 1241 ===
row_doc(
    "norshield_honduras_doors_tegucigalpa_15k_2019",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Honduras delivery of doors and parts to Tegucigalpa",
    "Honduras",
    "21 Jun 2019: Department of State awards contract to NORSHIELD SECURITY PRODUCTS, LLC for delivery of doors and parts to Tegucigalpa, Honduras (PoP Honduras); obligated USD 14590. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14590", "2019-06-21", "2019", "", "",
    "DELIVERY OF DOORS AND PARTS TO TEGUCIGALPA, HONDURAS., Honduras (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_norshield_honduras_doors_tegucigalpa_15k_2019",
    "DELIVERY OF DOORS AND PARTS TO TEGUCIGALPA, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P1024_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1241",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P1024_1900_-NONE-_-NONE- (norshield_honduras_doors_tegucigalpa_15k_2019). Signed 2019-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P1024_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_honduras_doors_tegucigalpa_15k_2019 USD 0.015m. Supports norshield_honduras_doors_tegucigalpa_15k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14590.0; date_signed 2019-06-21.",
)

# === Cycle 1241 ===
row_doc(
    "dh_pace_guyana_security_doors_9k_2016",
    "infrastructure", "building_materials", "us",
    "D. H. Pace — Guyana GSO security doors",
    "Guyana",
    "13 Jun 2016: Department of State awards contract to D. H. PACE COMPANY, INC. for GSO security doors (PoP Guyana); obligated USD 8516.04. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8516.04", "2016-06-13", "2016", "", "",
    "GSO: SECURITY DOORS, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_dh_pace_guyana_security_doors_9k_2016",
    "GSO: SECURITY DOORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20016M0208_1900_-NONE-_-NONE-/",
    "Actor: D. H. PACE COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1241",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20016M0208_1900_-NONE-_-NONE- (dh_pace_guyana_security_doors_9k_2016). Signed 2016-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20016M0208_1900_-NONE-_-NONE-/.",
    "USASpending: dh_pace_guyana_security_doors_9k_2016 USD 0.009m. Supports dh_pace_guyana_security_doors_9k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8516.04; date_signed 2016-06-13.",
)

# === Cycle 1241 ===
row_doc(
    "misc_colombia_torre95_apt302_make_ready_11k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Torre 95 apt 302 make-ready",
    "Colombia",
    "4 Feb 2026: Department of State awards contract for X50034 make ready to Torre 95 302-7903 rest OBO portion (PoP Colombia); obligated USD 10941.03. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "10941.03", "2026-02-04", "2026", "", "",
    "X50034 MAKE READY TO TORRE 95 302-7903 REST OBO PORTION, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_torre95_apt302_make_ready_11k_2026",
    "X50034 MAKE READY TO TORRE 95 302-7903 REST OBO PORTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026P0298_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1241",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02026P0298_1900_-NONE-_-NONE- (misc_colombia_torre95_apt302_make_ready_11k_2026). Signed 2026-02-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026P0298_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_torre95_apt302_make_ready_11k_2026 USD 0.011m. Supports misc_colombia_torre95_apt302_make_ready_11k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10941.03; date_signed 2026-02-04.",
)

# === Cycle 1241 ===
row_doc(
    "johnson_controls_mexico_air_handler_install_14k_2021",
    "energy", "power_plants_grid", "other",
    "Johnson Controls BE Operations México — Monterrey air handler motor and install",
    "Mexico",
    "21 Jan 2021: Department of State awards contract to JOHNSON CONTROLS BE OPERATIONS MÉXICO, S. DE R.L. DE C.V. for MTY-FAC-OBO air handler motor and install/FY21 (PoP Mexico); obligated USD 13784.41. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13784.41", "2021-01-21", "2021", "", "",
    "MTY-FAC-OBO- AIR HANDLER MOTOR AND INSTALL/FY21, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_johnson_controls_mexico_air_handler_install_14k_2021",
    "MTY-FAC-OBO- AIR HANDLER MOTOR AND INSTALL/FY21",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5621P0067_1900_-NONE-_-NONE-/",
    "Actor: JOHNSON CONTROLS BE OPERATIONS MÉXICO, S. DE R.L. DE C.V. — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1241",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5621P0067_1900_-NONE-_-NONE- (johnson_controls_mexico_air_handler_install_14k_2021). Signed 2021-01-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5621P0067_1900_-NONE-_-NONE-/.",
    "USASpending: johnson_controls_mexico_air_handler_install_14k_2021 USD 0.014m. Supports johnson_controls_mexico_air_handler_install_14k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13784.41; date_signed 2021-01-21.",
)

# === Cycle 1241 ===
row_doc(
    "misc_mexico_nld_residence_make_ready_204k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico NLD/GSO/OBO/PO residence make-ready 2023 final",
    "Mexico",
    "24 Apr 2023: Department of State awards contract for NLD/GSO/OBO/PO residence make-ready/2023 final (PoP Mexico); obligated USD 204141.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "204141.99", "2023-04-24", "2023", "", "",
    "NLD/GSO/OBO/PO RESIDENCE MAKE READY/2023 FINAL, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_nld_residence_make_ready_204k_2023",
    "NLD/GSO/OBO/PO RESIDENCE MAKE READY/2023 FINAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6123P0079_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1241",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6123P0079_1900_-NONE-_-NONE- (misc_mexico_nld_residence_make_ready_204k_2023). Signed 2023-04-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6123P0079_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nld_residence_make_ready_204k_2023 USD 0.204m. Supports misc_mexico_nld_residence_make_ready_204k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 204141.99; date_signed 2023-04-24.",
)

def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    for row, _ev, _bib in ITEMS:
        rid = row["id"]
        if rid in by_id:
            raise SystemExit(f"duplicate id: {rid}")
        rows.append(row)
        by_id[rid] = row
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
    bib_docs = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by_id = {b["id"]: b for b in bib_docs}
    for _row, _ev, bib in ITEMS:
        sid = bib["id"]
        if sid in bib_by_id:
            existing = bib_by_id[sid]
            for s in bib.get("supports") or []:
                if s not in (existing.get("supports") or []):
                    existing.setdefault("supports", []).append(s)
        else:
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
