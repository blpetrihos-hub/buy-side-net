#!/usr/bin/env python3
"""Cycles 1165–1167: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262165–20262167. Thin top-up dry.
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


# === Cycle 1165 (seed 20262165) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_honduras_six_diesel_prime_generators_107k_2015",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Honduras six complete diesel prime-rated generators",
    "Honduras",
    "28 Sep 2015: Department of State awards contract SHO80015F0355 to Cummins Power Generation Inc. for six complete diesel prime-rated generators (PoP Honduras); obligated USD 107,394.0. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "107394", "2015-09-28", "2015", "", "",
    "Six complete diesel prime-rated generators, Honduras (USASpending description; sites unnamed — lat/lon blank).",
    "usaspending_cummins_honduras_six_diesel_prime_generators_107k_2015",
    "IGF::OT::IGF  SIX (6) COMPLETE DIESEL PRIME-RATED GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80015F0355_1900_GS07F9004D_4730/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1165",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80015F0355_1900_GS07F9004D_4730 (cummins_honduras_six_diesel_prime_generators_107k_2015). Signed 2015-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80015F0355_1900_GS07F9004D_4730/.",
    "USASpending: cummins_honduras_six_diesel_prime_generators_107k_2015 USD 0.107m. Supports cummins_honduras_six_diesel_prime_generators_107k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 107394.0; date_signed 2015-09-28.",
)
row_doc(
    "cummins_ecuador_obo_residential_generator_99k_2012",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Ecuador OBO Cummins generator for residences",
    "Ecuador",
    "27 Sep 2012: Department of State awards contract SEC30012M0506 to Cummins Power Generation Inc. for OBO Cummins generator for residences (PoP Ecuador); obligated USD 99,356.22. CapEx face = award obligation. Residences unnamed; site coords not stated — lat/lon blank.",
    "99356.22", "2012-09-27", "2012", "", "",
    "Cummins generator for residences, Ecuador (USASpending description; residences unnamed, site coords not stated — lat/lon blank).",
    "usaspending_cummins_ecuador_obo_residential_generator_99k_2012",
    "G- OBO - CUMMINS GENERATOR FOR RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30012M0506_1900_-NONE-_-NONE-/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1165",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC30012M0506_1900_-NONE-_-NONE- (cummins_ecuador_obo_residential_generator_99k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30012M0506_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_ecuador_obo_residential_generator_99k_2012 USD 0.099m. Supports cummins_ecuador_obo_residential_generator_99k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 99356.22; date_signed 2012-09-27.",
)
row_doc(
    "misc_dominican_republic_nas_dncd_k9_generator_15k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic NAS-DNCD K9 generator",
    "Dominican Republic",
    "1 Jun 2012: Department of State awards contract SDR86012M0825M001 for NAS-DNCD K9 generator (PoP Dominican Republic); obligated USD 14,950.0. CapEx face = award obligation. DNCD K9 named; site coords not stated — lat/lon blank.",
    "14950", "2012-06-01", "2012", "", "",
    "NAS-DNCD K9 generator, Dominican Republic (USASpending description; DNCD named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_nas_dncd_k9_generator_15k_2012",
    "NAS-DNCD-K9 GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M0825M001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1165",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86012M0825M001_1900_-NONE-_-NONE- (misc_dominican_republic_nas_dncd_k9_generator_15k_2012). Signed 2012-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M0825M001_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_nas_dncd_k9_generator_15k_2012 USD 0.015m. Supports misc_dominican_republic_nas_dncd_k9_generator_15k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14950.0; date_signed 2012-06-01.",
)
row_doc(
    "misc_ecuador_swowboda_house_security_upgrades_15k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador security upgrades for Mr. Swowboda house",
    "Ecuador",
    "4 May 2018: Department of State awards contract 19EC7518P0329 for security upgrades for Mr. Swowboda house (PoP Ecuador); obligated USD 14,591.81. CapEx face = award obligation. Named residence; site coords not stated — lat/lon blank.",
    "14591.81", "2018-05-04", "2018", "", "",
    "Security upgrades for named residence, Ecuador (USASpending description; residence named, site coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_swowboda_house_security_upgrades_15k_2018",
    "PR7317688-FC5841 SECURITY UPGRADES FOR MR. SWOWBODA'S HOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7518P0329_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1165",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7518P0329_1900_-NONE-_-NONE- (misc_ecuador_swowboda_house_security_upgrades_15k_2018). Signed 2018-05-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7518P0329_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_swowboda_house_security_upgrades_15k_2018 USD 0.015m. Supports misc_ecuador_swowboda_house_security_upgrades_15k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14591.81; date_signed 2018-05-04.",
)
row_doc(
    "misc_argentina_pas_office_renovation_15k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina PAS office renovation",
    "Argentina",
    "24 Sep 2021: Department of State awards contract 19AR2021C0013 for FAC PAS office renovation (PoP Argentina); obligated USD 14,567.28. CapEx face = award obligation. PAS office named; site coords not stated — lat/lon blank.",
    "14567.28", "2021-09-24", "2021", "", "",
    "PAS office renovation, Argentina (USASpending description; PAS office named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_pas_office_renovation_15k_2021",
    "FAC - PAS OFFICE RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021C0013_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1165",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2021C0013_1900_-NONE-_-NONE- (misc_argentina_pas_office_renovation_15k_2021). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021C0013_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_pas_office_renovation_15k_2021 USD 0.015m. Supports misc_argentina_pas_office_renovation_15k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14567.28; date_signed 2021-09-24.",
)

# === Cycle 1166 (seed 20262166) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_mexico_pcc_high_level_alarms_install_88k_2022",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico PCC high level alarms technical security installation",
    "Mexico",
    "6 Jun 2022: Department of State awards contract 19AQMM22F2060 to Applied Security Technologies Inc for technical security installation of high level alarms in the PCC (PoP Mexico); obligated USD 87,930.29. CapEx face = award obligation. PCC named; site coords not stated — lat/lon blank.",
    "87930.29", "2022-06-06", "2022", "", "",
    "High level alarms technical security installation in PCC, Mexico (USASpending description; PCC named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_mexico_pcc_high_level_alarms_install_88k_2022",
    ". TECHNICAL SECURITY INSTALLATION OF THE HIGH LEVEL ALARMS IN THE PCC.  .",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2060_1900_19AQMM19D0002_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1166",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F2060_1900_19AQMM19D0002_1900 (applied_security_mexico_pcc_high_level_alarms_install_88k_2022). Signed 2022-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2060_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_mexico_pcc_high_level_alarms_install_88k_2022 USD 0.088m. Supports applied_security_mexico_pcc_high_level_alarms_install_88k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87930.29; date_signed 2022-06-06.",
)
row_doc(
    "applied_security_bahamas_pcc_hla_system_install_86k_2024",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Bahamas PCC HLA system equipment procurement shipment installation",
    "Bahamas",
    "29 Feb 2024: Department of State awards contract 19AQMM24F0479 to Applied Security Technologies Inc for procurement, shipment and installation of HLA system equipment in the PCC (PoP Bahamas); obligated USD 85,657.0. CapEx face = award obligation. PCC named; site coords not stated — lat/lon blank.",
    "85657", "2024-02-29", "2024", "", "",
    "HLA system equipment installation in PCC, Bahamas (USASpending description; PCC named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_bahamas_pcc_hla_system_install_86k_2024",
    "PROCUREMENT, SHIPMENT AND INSTALLATION OF HLA SYSTEM EQUIPMENT IN THE PCC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0479_1900_19AQMM19D0002_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1166",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F0479_1900_19AQMM19D0002_1900 (applied_security_bahamas_pcc_hla_system_install_86k_2024). Signed 2024-02-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0479_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_bahamas_pcc_hla_system_install_86k_2024 USD 0.086m. Supports applied_security_bahamas_pcc_hla_system_install_86k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85657.0; date_signed 2024-02-29.",
)
row_doc(
    "misc_jamaica_vetted_unit_security_fence_wall_15k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica vetted unit security fence and wall improvements",
    "Jamaica",
    "24 Sep 2011: Department of State awards contract SJM37011M1161 for vetted unit security fence and wall improvements (PoP Jamaica); obligated USD 14,518.0. CapEx face = award obligation. Vetted unit named; site coords not stated — lat/lon blank.",
    "14518", "2011-09-24", "2011", "", "",
    "Vetted unit security fence and wall improvements, Jamaica (USASpending description; unit named, site coords not stated — lat/lon blank).",
    "usaspending_misc_jamaica_vetted_unit_security_fence_wall_15k_2011",
    "VETTED UNIT SECURITY FENCE AND WALL IMPROVEMENTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37011M1161_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1166",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37011M1161_1900_-NONE-_-NONE- (misc_jamaica_vetted_unit_security_fence_wall_15k_2011). Signed 2011-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37011M1161_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_vetted_unit_security_fence_wall_15k_2011 USD 0.015m. Supports misc_jamaica_vetted_unit_security_fence_wall_15k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14518.0; date_signed 2011-09-24.",
)
row_doc(
    "misc_guyana_generator_installation_15k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guyana generator installation",
    "Guyana",
    "16 May 2023: Department of State awards contract 19GY2023P0201 for generator installation (PoP Guyana); obligated USD 14,543.82. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14543.82", "2023-05-16", "2023", "", "",
    "Generator installation, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guyana_generator_installation_15k_2023",
    "GENERATOR INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2023P0201_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1166",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2023P0201_1900_-NONE-_-NONE- (misc_guyana_generator_installation_15k_2023). Signed 2023-05-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2023P0201_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guyana_generator_installation_15k_2023 USD 0.015m. Supports misc_guyana_generator_installation_15k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14543.82; date_signed 2023-05-16.",
)
row_doc(
    "misc_venezuela_chancery_restroom_renovation_14k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela chancery restroom renovation project",
    "Venezuela",
    "30 Sep 2011: Department of State awards contract SVE30011M0917 for chancery restroom renovation project (PoP Venezuela); obligated USD 13,937.06. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "13937.06", "2011-09-30", "2011", "", "",
    "Chancery restroom renovation, Venezuela (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_chancery_restroom_renovation_14k_2011",
    "CHANCERY: RESTROOM RENOVATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0917_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1166",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30011M0917_1900_-NONE-_-NONE- (misc_venezuela_chancery_restroom_renovation_14k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0917_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_chancery_restroom_renovation_14k_2011 USD 0.014m. Supports misc_venezuela_chancery_restroom_renovation_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13937.06; date_signed 2011-09-30.",
)

# === Cycle 1167 (seed 20262167) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_peru_lima_tss_security_installation_84k_2011",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Peru Lima TSS security installation",
    "Peru",
    "10 May 2011: Department of State awards contract SAQMMA11F1525 to Applied Security Technologies Inc for TSS Lima, Peru security installation (PoP Peru); obligated USD 84,254.87. CapEx face = award obligation. Lima named; site coords not stated — lat/lon blank.",
    "84254.87", "2011-05-10", "2011", "", "",
    "TSS security installation, Lima, Peru (USASpending description; Lima named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_peru_lima_tss_security_installation_84k_2011",
    "TSS LIMA, PERU SECURITY INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1525_1900_SAQMMA07D0030_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1167",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F1525_1900_SAQMMA07D0030_1900 (applied_security_peru_lima_tss_security_installation_84k_2011). Signed 2011-05-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1525_1900_SAQMMA07D0030_1900/.",
    "USASpending: applied_security_peru_lima_tss_security_installation_84k_2011 USD 0.084m. Supports applied_security_peru_lima_tss_security_installation_84k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 84254.87; date_signed 2011-05-10.",
)
row_doc(
    "applied_security_mexico_core_high_level_alarms_install_86k_2024",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico installation of core high level alarms",
    "Mexico",
    "21 Jul 2024: Department of State awards contract 19AQMM24F1373 to Applied Security Technologies Inc for installation of the core high level alarms (PoP Mexico); obligated USD 85,538.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "85538", "2024-07-21", "2024", "", "",
    "Installation of core high level alarms, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_mexico_core_high_level_alarms_install_86k_2024",
    "INSTALLATION OF THE CORE HIGH LEVEL ALARMS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1373_1900_19AQMM19D0002_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1167",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F1373_1900_19AQMM19D0002_1900 (applied_security_mexico_core_high_level_alarms_install_86k_2024). Signed 2024-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1373_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_mexico_core_high_level_alarms_install_86k_2024 USD 0.086m. Supports applied_security_mexico_core_high_level_alarms_install_86k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85538.0; date_signed 2024-07-21.",
)
row_doc(
    "misc_barbados_gov_building_ac_units_replace_15k_2021",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Barbados replace AC units in government owned building",
    "Barbados",
    "19 Jul 2021: Department of State awards contract 19BB2121P0980 for replace AC units in government owned building (PoP Barbados); obligated USD 14,677.95. CapEx face = award obligation. Building unnamed; site coords not stated — lat/lon blank.",
    "14677.95", "2021-07-19", "2021", "", "",
    "Replace AC units in government owned building, Barbados (USASpending description; building unnamed, site coords not stated — lat/lon blank).",
    "usaspending_misc_barbados_gov_building_ac_units_replace_15k_2021",
    "REPLACE AC UNITS IN GOVERNMENT OWED BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2121P0980_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1167",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2121P0980_1900_-NONE-_-NONE- (misc_barbados_gov_building_ac_units_replace_15k_2021). Signed 2021-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2121P0980_1900_-NONE-_-NONE-/.",
    "USASpending: misc_barbados_gov_building_ac_units_replace_15k_2021 USD 0.015m. Supports misc_barbados_gov_building_ac_units_replace_15k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14677.95; date_signed 2021-07-19.",
)
row_doc(
    "misc_bahamas_security_grills_fabricate_install_15k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas fabrication and installation of security grills",
    "Bahamas",
    "25 Apr 2013: Department of State awards contract SBF50013M0474 for fabrication and installation of security grills (PoP Bahamas); obligated USD 14,645.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14645", "2013-04-25", "2013", "", "",
    "Fabrication and installation of security grills, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bahamas_security_grills_fabricate_install_15k_2013",
    "LF-K- FABRICATION AND INSTALLATION OF SECURITY GRILLS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50013M0474_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1167",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50013M0474_1900_-NONE-_-NONE- (misc_bahamas_security_grills_fabricate_install_15k_2013). Signed 2013-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50013M0474_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_security_grills_fabricate_install_15k_2013 USD 0.015m. Supports misc_bahamas_security_grills_fabricate_install_15k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14645.0; date_signed 2013-04-25.",
)
row_doc(
    "misc_nicaragua_hvac_variable_frequency_drivers_replace_15k_2021",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Nicaragua variable frequency drivers replacements for HVAC system",
    "Nicaragua",
    "16 Aug 2021: Department of State awards contract 19NU7021P0562 for variable frequency drivers for replacements HVAC system (PoP Nicaragua); obligated USD 14,740.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14740", "2021-08-16", "2021", "", "",
    "Variable frequency drivers replacements for HVAC system, Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_nicaragua_hvac_variable_frequency_drivers_replace_15k_2021",
    "VARIABLE FREQUENCY DRIVERS FOR REPLACEMENTS- HVAC SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7021P0562_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1167",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NU7021P0562_1900_-NONE-_-NONE- (misc_nicaragua_hvac_variable_frequency_drivers_replace_15k_2021). Signed 2021-08-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7021P0562_1900_-NONE-_-NONE-/.",
    "USASpending: misc_nicaragua_hvac_variable_frequency_drivers_replace_15k_2021 USD 0.015m. Supports misc_nicaragua_hvac_variable_frequency_drivers_replace_15k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14740.0; date_signed 2021-08-16.",
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
