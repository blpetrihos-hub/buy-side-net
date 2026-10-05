#!/usr/bin/env python3
"""Cycles 1044–1046: USASpending LatAm CapEx residual (~USD0.05–0.072m).

Seeds: 20262044–20262046. Thin top-up dry.
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


# === Cycle 1044 (seed 20262044) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "keller_uruguay_fire_panel_60k_2022",
    "infrastructure", "building_materials", "us",
    "Keller's — Uruguay chancery fire panel repair",
    "Uruguay",
    "1 Feb 2022: Department of State awards contract 19UY6022P0143 to Keller's LLC for FAC repair CHCY fire panel system X1001 (PoP Uruguay); obligated USD 60,000. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "60000", "2022-02-01", "2022", "", "",
    "Chancery fire panel system repair, Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_keller_uruguay_fire_panel_60k_2022",
    "FAC - REPAIR CHCY FIRE PANEL SYSTEM - X1001",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6022P0143_1900_-NONE-_-NONE-/",
    "Actor: Keller's LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1044",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6022P0143_1900_-NONE-_-NONE- (Keller Uruguay fire panel). Signed 2022-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6022P0143_1900_-NONE-_-NONE-/.",
    "USASpending: Keller Uruguay fire panel USD 0.060m. Supports keller_uruguay_fire_panel_60k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60000; date_signed 2022-02-01.",
)

row_doc(
    "project_services_guyana_cams_63k_2019",
    "infrastructure", "building_materials", "us",
    "Project Services International — Guyana residential CAMS install",
    "Guyana",
    "27 Nov 2019: Department of State awards contract 19GE5020P0006 to Project Services International Corporation, Inc. for install central alarm monitoring system equipment into preexisting residential alarms (PoP Guyana); obligated USD 63,430. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.",
    "63430", "2019-11-27", "2019", "", "",
    "Central alarm monitoring system install into residential alarms, Guyana (USASpending description; residences not named — lat/lon blank).",
    "usaspending_project_services_guyana_cams_63k_2019",
    "INSTALL CENTRAL ALARM MONITORING SYSTEM EQUIPMENT INTO THE PREEXISTING RESIDENTIAL ALARMS PROTECTING THE HOMES OF THE DI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020P0006_1900_-NONE-_-NONE-/",
    "Actor: Project Services International Corporation, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1044",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5020P0006_1900_-NONE-_-NONE- (Project Services Guyana CAMS). Signed 2019-11-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020P0006_1900_-NONE-_-NONE-/.",
    "USASpending: Project Services Guyana CAMS USD 0.063m. Supports project_services_guyana_cams_63k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63430; date_signed 2019-11-27.",
)

row_doc(
    "misc_mexico_niv_waterproof_71k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico NIV building waterproof",
    "Mexico",
    "26 Aug 2013: Department of State awards contract SMX53013M1227 for FAC 7901 waterproof of the NIV building (PoP Mexico); obligated USD 71,315.07. CapEx face = award obligation. Recipient redacted; exact building unnamed — lat/lon blank.",
    "71315.07", "2013-08-26", "2013", "", "",
    "Waterproof of NIV building, Mexico (USASpending description; building not named — lat/lon blank).",
    "usaspending_misc_mexico_niv_waterproof_71k_2013",
    "MEX-FAC 7901 WATERPROOF OF THE NIV BUILDING IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M1227_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1044",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M1227_1900_-NONE-_-NONE- (Mexico NIV waterproof). Signed 2013-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M1227_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico NIV waterproof USD 0.071m. Supports misc_mexico_niv_waterproof_71k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71315.07; date_signed 2013-08-26.",
)

row_doc(
    "misc_mexico_odc_remodel_71k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico ODC construction remodel",
    "Mexico",
    "29 Sep 2010: Department of State awards contract SMX53010M0907 for ODC construction project remodel (PoP Mexico); obligated USD 71,296.64. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "71296.64", "2010-09-29", "2010", "", "",
    "ODC construction remodel, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_odc_remodel_71k_2010",
    "MEX/ODC - ODC CONSTRUCTION PROJECT - REMODEL PROJ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0907_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1044",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0907_1900_-NONE-_-NONE- (Mexico ODC remodel). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0907_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico ODC remodel USD 0.071m. Supports misc_mexico_odc_remodel_71k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71296.64; date_signed 2010-09-29.",
)

row_doc(
    "santilli_uruguay_libano_windows_71k_2017",
    "infrastructure", "building_materials", "other",
    "Santilli Federico Elio — Uruguay Libano 1351 window replacement",
    "Uruguay",
    "27 Sep 2017: Department of State awards contract SUY60017C0001 to Santilli Federico, Elio for labor and materials to replace windows at GO property Libano 1351 (PoP Uruguay); obligated USD 71,069.13. CapEx face = award obligation.",
    "71069.13", "2017-09-27", "2017", "-34.894", "-56.152",
    "Window replacement at GO property Libano 1351, Uruguay (USASpending description; Libano 1351 named).",
    "usaspending_santilli_uruguay_libano_windows_71k_2017",
    "IGF::OT::IGF LABOR AND MATERIALS TO REPLACE WINDOWS LOCATED AT GO PROPERTY LOCATED AT LIBANO 1351",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60017C0001_1900_-NONE-_-NONE-/",
    "Actor: Santilli Federico, Elio (Uruguay) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1044",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60017C0001_1900_-NONE-_-NONE- (Santilli Uruguay Libano windows). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60017C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Santilli Uruguay Libano windows USD 0.071m. Supports santilli_uruguay_libano_windows_71k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71069.13; date_signed 2017-09-27.",
)

# === Cycle 1045 (seed 20262045) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fluid_solutions_dr_controller_63k_2026",
    "energy", "power_plants_grid", "us",
    "Fluid Solutions — Dominican Republic UTL building main controller replacement",
    "Dominican Republic",
    "28 Aug 2026: Department of State awards contract 19DR8626P1454 to Fluid Solutions LLC for UTL building (main controller) replacement (PoP Dominican Republic); obligated USD 62,922. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "62922", "2026-08-28", "2026", "", "",
    "UTL building main controller replacement, Dominican Republic (USASpending description; building not named — lat/lon blank).",
    "usaspending_fluid_solutions_dr_controller_63k_2026",
    "UTL BUILDING (MAIN CONTROLLER) REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8626P1454_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1045",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8626P1454_1900_-NONE-_-NONE- (Fluid Solutions DR controller). Signed 2026-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8626P1454_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions DR controller USD 0.063m. Supports fluid_solutions_dr_controller_63k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62922; date_signed 2026-08-28.",
)

row_doc(
    "mcmg_guatemala_generator_65k_2025",
    "energy", "power_plants_grid", "us",
    "MCMG Integrated Service — Guatemala generator, lights, and MHE",
    "Guatemala",
    "1 May 2025: Department of Defense awards contract W912QM25P0014 to MCMG Integrated Service, LLC for generator, lights, and MHE ISO CG25 (PoP Guatemala); obligated USD 65,270. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "65270", "2025-05-01", "2025", "", "",
    "Generator, lights, and MHE, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_mcmg_guatemala_generator_65k_2025",
    "GENERATOR, LIGHTS, AND MHE ISO CG25",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM25P0014_9700_-NONE-_-NONE-/",
    "Actor: MCMG Integrated Service, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1045",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM25P0014_9700_-NONE-_-NONE- (MCMG Guatemala generator). Signed 2025-05-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM25P0014_9700_-NONE-_-NONE-/.",
    "USASpending: MCMG Guatemala generator USD 0.065m. Supports mcmg_guatemala_generator_65k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65270; date_signed 2025-05-01.",
)

row_doc(
    "misc_mazatlan_dea_surveillance_72k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Mazatlán DEA office surveillance install",
    "Mexico",
    "29 Aug 2016: Department of State awards contract SMX53016M1429 for install surveillance for the Matazlan DEA office (PoP Mexico); obligated USD 71,728.40. CapEx face = award obligation.",
    "71728.40", "2016-08-29", "2016", "23.249", "-106.411",
    "Surveillance install at DEA office, Mazatlán, Mexico (USASpending description; Mazatlán named).",
    "usaspending_misc_mazatlan_dea_surveillance_72k_2016",
    "INSTALL SURVEILLANCE FOR THE MATAZLAN DEA OFFICE IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016M1429_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1045",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53016M1429_1900_-NONE-_-NONE- (Mazatlán DEA surveillance). Signed 2016-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016M1429_1900_-NONE-_-NONE-/.",
    "USASpending: Mazatlán DEA surveillance USD 0.072m. Supports misc_mazatlan_dea_surveillance_72k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71728.40; date_signed 2016-08-29.",
)

row_doc(
    "mathews_honduras_genset_install_71k_2016",
    "energy", "power_plants_grid", "other",
    "Casa Comercial Mathews — Honduras Caterpillar genset installation",
    "Honduras",
    "28 Sep 2016: USAID awards contract AID522O1600091 to Casa Comercial Mathews SA de CV for Caterpillar genset installation — labor and materials (PoP Honduras); obligated USD 70,540.06. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "70540.06", "2016-09-28", "2016", "", "",
    "Caterpillar genset installation, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_mathews_honduras_genset_install_71k_2016",
    "IGF::CL::IGF  CATERPILLAR GENSET  INSTALLATION- LABOR AND MATERIALS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1600091_7200_-NONE-_-NONE-/",
    "Actor: Casa Comercial Mathews SA de CV (Honduras) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1045",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1600091_7200_-NONE-_-NONE- (Mathews Honduras genset). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1600091_7200_-NONE-_-NONE-/.",
    "USASpending: Mathews Honduras genset USD 0.071m. Supports mathews_honduras_genset_install_71k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70540.06; date_signed 2016-09-28.",
)

row_doc(
    "misc_dr_roof_truss_71k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic roof truss for vocational school and clinics",
    "Dominican Republic",
    "17 Feb 2016: Department of Defense awards contract FA470416M2002 for roof truss system for vocational school and medical clinics (PoP Dominican Republic); obligated USD 70,978.25. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "70978.25", "2016-02-17", "2016", "", "",
    "Roof truss system for vocational school and medical clinics, Dominican Republic (USASpending description; sites not named — lat/lon blank).",
    "usaspending_misc_dr_roof_truss_71k_2016",
    "ROOF TRUSS SYSTEM FOR VOCATIONAL SCHOOL AND MEDICAL CLINICS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470416M2002_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1045",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470416M2002_9700_-NONE-_-NONE- (DR roof truss). Signed 2016-02-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470416M2002_9700_-NONE-_-NONE-/.",
    "USASpending: DR roof truss USD 0.071m. Supports misc_dr_roof_truss_71k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70978.25; date_signed 2016-02-17.",
)

# === Cycle 1046 (seed 20262046) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "thompson_argentina_eoc_design_71k_2018",
    "infrastructure", "engineering_epc", "us",
    "Thompson Engineering — Argentina EOC/DRW design services",
    "Argentina",
    "24 Sep 2018: Department of Defense awards order W9127818F0662 to Thompson Engineering, Inc. for design services (EOC, DRW) (PoP Argentina); obligated USD 71,238.86. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "71238.86", "2018-09-24", "2018", "", "",
    "Design services for EOC and DRW, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_thompson_argentina_eoc_design_71k_2018",
    "DESIGN SERVICES (EOC, DRW)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0662_9700_W9127814D0067_9700/",
    "Actor: Thompson Engineering, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1046",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0662_9700_W9127814D0067_9700 (Thompson Argentina EOC design). Signed 2018-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0662_9700_W9127814D0067_9700/.",
    "USASpending: Thompson Argentina EOC design USD 0.071m. Supports thompson_argentina_eoc_design_71k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71238.86; date_signed 2018-09-24.",
)

row_doc(
    "export_220volt_brazil_transformers_65k_2024",
    "energy", "power_plants_grid", "us",
    "Export 220Volt — Brazil Brasília transformers for make-ready residences",
    "Brazil",
    "26 Aug 2024: Department of State awards contract 19BR2524P1304 to Export 220Volt Inc. for transformers for make ready residences FAP (PoP Brazil); obligated USD 64,800. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.",
    "64800", "2024-08-26", "2024", "", "",
    "Transformers for make-ready residences, Brasília post, Brazil (USASpending description; residences not named — lat/lon blank).",
    "usaspending_export_220volt_brazil_transformers_65k_2024",
    "BSB | PSW |  TRANSFORMERS FOR MAKE READY RESIDENCES - FAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2524P1304_1900_-NONE-_-NONE-/",
    "Actor: Export 220Volt Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1046",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2524P1304_1900_-NONE-_-NONE- (Export 220Volt Brazil transformers). Signed 2024-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2524P1304_1900_-NONE-_-NONE-/.",
    "USASpending: Export 220Volt Brazil transformers USD 0.065m. Supports export_220volt_brazil_transformers_65k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64800; date_signed 2024-08-26.",
)

row_doc(
    "misc_venezuela_delta_barriers_70k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela delta barriers replacement",
    "Venezuela",
    "7 Aug 2014: Department of State awards contract SVE30014M0321 for delta barriers replacement (PoP Venezuela); obligated USD 69,942.40. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "69942.40", "2014-08-07", "2014", "", "",
    "Delta barriers replacement, Venezuela (USASpending PoP Venezuela; site not named — lat/lon blank).",
    "usaspending_misc_venezuela_delta_barriers_70k_2014",
    "IGF::CL::IGF DELTA BARRIERS REPLACEMENT- CHARGE TO DS/FSE/PME",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0321_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Venezuela beyond-solar weight.",
    "hunt_cycle1046",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30014M0321_1900_-NONE-_-NONE- (Venezuela delta barriers). Signed 2014-08-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0321_1900_-NONE-_-NONE-/.",
    "USASpending: Venezuela delta barriers USD 0.070m. Supports misc_venezuela_delta_barriers_70k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69942.40; date_signed 2014-08-07.",
)

row_doc(
    "misc_barbados_generator_install_70k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Barbados generator installation",
    "Barbados",
    "19 Jul 2022: Department of State awards contract 19BB2122P1089 for generator installation (PoP Barbados); obligated USD 69,652.84. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "69652.84", "2022-07-19", "2022", "", "",
    "Generator installation, Barbados (USASpending PoP Barbados; site not named — lat/lon blank).",
    "usaspending_misc_barbados_generator_install_70k_2022",
    "NOT FOREIGN ASSISTANCE- GENERATOR INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2122P1089_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1046",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2122P1089_1900_-NONE-_-NONE- (Barbados generator install). Signed 2022-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2122P1089_1900_-NONE-_-NONE-/.",
    "USASpending: Barbados generator install USD 0.070m. Supports misc_barbados_generator_install_70k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69652.84; date_signed 2022-07-19.",
)

row_doc(
    "misc_haiti_reyes_razor_wire_69k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti Reyes and CAS compound razor wire",
    "Haiti",
    "18 Sep 2023: Department of State awards contract 19HA7023P1304 for razor wire installation at Reyes and CAS compound (PoP Haiti); obligated USD 69,174.60. CapEx face = award obligation.",
    "69174.60", "2023-09-18", "2023", "18.539", "-72.335",
    "Razor wire installation at Reyes and CAS compound, Haiti (USASpending description; Reyes compound named).",
    "usaspending_misc_haiti_reyes_razor_wire_69k_2023",
    "RAZOR WIRE INSTALLATION AT REYES AND CAS COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1304_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Haiti under-covered weight.",
    "hunt_cycle1046",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P1304_1900_-NONE-_-NONE- (Haiti Reyes razor wire). Signed 2023-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1304_1900_-NONE-_-NONE-/.",
    "USASpending: Haiti Reyes razor wire USD 0.069m. Supports misc_haiti_reyes_razor_wire_69k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69174.60; date_signed 2023-09-18.",
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
        w.writeheader()
        w.writerows(rows)

    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        path = EVID / f"{row['id']}.json"
        path.write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")

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
            bib_docs.append(bib)
            bib_by_id[sid] = bib
    BIB.write_text(
        yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
