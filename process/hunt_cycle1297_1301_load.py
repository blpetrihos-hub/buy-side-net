#!/usr/bin/env python3
"""Cycles 1297–1301: USASpending LatAm CapEx (OES/Hardline/Inspection Experts/Hana + misc towers/power).

Seeds: 20262297–20262301. Thin top-up dry.
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

# === Cycle 1297 ===
row_doc(
    "inspection_experts_mexico_design_build_3255k_2024",
    "infrastructure", "building_materials", "us",
    "Inspection Experts — Mexico design-build construction services",
    "Mexico",
    "27 Sep 2024: Department of State awards contract to INSPECTION EXPERTS INC for design-build construction services (PoP Mexico); obligated USD 3255388.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3255388.00", "2024-09-27", "2024", "", "",
    "DESIGN BUILD CONSTRUCTION SERVICES, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_inspection_experts_mexico_design_build_3255k_2024",
    "DESIGN BUILD CONSTRUCTION SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2504_1900_19AQMM22D0064_1900/",
    "Actor: INSPECTION EXPERTS INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1297",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F2504_1900_19AQMM22D0064_1900 (inspection_experts_mexico_design_build_3255k_2024). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2504_1900_19AQMM22D0064_1900/.",
    "USASpending: inspection_experts_mexico_design_build_3255k_2024 USD 3.255m. Supports inspection_experts_mexico_design_build_3255k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3255388.0; date_signed 2024-09-27.",
    investment_type="epc",
)

# === Cycle 1297 ===
row_doc(
    "oes_mexico_guadalajara_febr_1723k_2011",
    "infrastructure", "building_materials", "us",
    "O.E.S. — Mexico Guadalajara FE/BR product replacement",
    "Mexico",
    "7 Sep 2011: Department of State awards contract to O.E.S., INC. for Phase III/IV FE/BR product replacement and repair — U.S. Consulate General Guadalajara; obligated USD 1722909.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1722909.73", "2011-09-07", "2011", "", "",
    "PHASE III/IV - FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR PROJECT - U, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_oes_mexico_guadalajara_febr_1723k_2011",
    "PHASE III/IV - FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR PROJECT - U.S. CONSULATE GENERAL GUADALAJARA, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3289_1900_SAQMMA07D0009_1900/",
    "Actor: O.E.S., INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1297",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3289_1900_SAQMMA07D0009_1900 (oes_mexico_guadalajara_febr_1723k_2011). Signed 2011-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3289_1900_SAQMMA07D0009_1900/.",
    "USASpending: oes_mexico_guadalajara_febr_1723k_2011 USD 1.723m. Supports oes_mexico_guadalajara_febr_1723k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1722909.73; date_signed 2011-09-07.",
    investment_type="equipment_supply",
)

# === Cycle 1297 ===
row_doc(
    "misc_mexico_tijuana_fire_main_583k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Tijuana fire-main construction installation",
    "Mexico",
    "6 Aug 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction installation of a fire main in Tijuana, Mexico; obligated USD 583129.63. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "583129.63", "2019-08-06", "2019", "", "",
    "THE PURPOSE OF THIS PURCHASE ORDER IS TO FUND THE CONSTRUCTION INSTALLATION OF A FIRE MAIN IN TIJUANA, MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_tijuana_fire_main_583k_2019",
    "THE PURPOSE OF THIS PURCHASE ORDER IS TO FUND THE CONSTRUCTION INSTALLATION OF A FIRE MAIN IN TIJUANA, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P1282_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1297",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P1282_1900_-NONE-_-NONE- (misc_mexico_tijuana_fire_main_583k_2019). Signed 2019-08-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P1282_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_tijuana_fire_main_583k_2019 USD 0.583m. Supports misc_mexico_tijuana_fire_main_583k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 583129.63; date_signed 2019-08-06.",
    investment_type="epc",
)

# === Cycle 1297 ===
row_doc(
    "idac_colombia_tulua_facatativa_towers_441k_2017",
    "infrastructure", "building_materials", "other",
    "IDAC S.A.S. — Colombia Tulua/Facatativa towers and kennels",
    "Colombia",
    "14 Feb 2017: Department of State awards contract to IDAC S A S for tower (1) and kennels in Tulua and tower (1) in Facatativa, Colombia; obligated USD 441026.87. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "441026.87", "2017-02-14", "2017", "", "",
    "TOWER (1) AND KENNELS IN TULUA AND TOWER (1) IN FACATATIVA, COLOMBIA IGF::OT::IGF, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_idac_colombia_tulua_facatativa_towers_441k_2017",
    "TOWER (1) AND KENNELS IN TULUA AND TOWER (1) IN FACATATIVA, COLOMBIA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0053_1900_-NONE-_-NONE-/",
    "Actor: IDAC S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1297",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0053_1900_-NONE-_-NONE- (idac_colombia_tulua_facatativa_towers_441k_2017). Signed 2017-02-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0053_1900_-NONE-_-NONE-/.",
    "USASpending: idac_colombia_tulua_facatativa_towers_441k_2017 USD 0.441m. Supports idac_colombia_tulua_facatativa_towers_441k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 441026.87; date_signed 2017-02-14.",
    investment_type="epc",
)

# === Cycle 1297 ===
row_doc(
    "misc_mexico_cbscn_towers_388k_2012",
    "infrastructure", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico CBSCN towers (4) installation",
    "Mexico",
    "22 May 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for NAS-MI CBSCN towers (4) installation and repair; obligated USD 387903.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "387903.46", "2012-05-22", "2012", "", "",
    "NAS-MI  CBSCN TOWERS (4) INSTALLATION AND REPAIR, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cbscn_towers_388k_2012",
    "NAS-MI  CBSCN TOWERS (4) INSTALLATION AND REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1028_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1297",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M1028_1900_-NONE-_-NONE- (misc_mexico_cbscn_towers_388k_2012). Signed 2012-05-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1028_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cbscn_towers_388k_2012 USD 0.388m. Supports misc_mexico_cbscn_towers_388k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 387903.46; date_signed 2012-05-22.",
    investment_type="epc",
)

# === Cycle 1298 ===
row_doc(
    "oes_nicaragua_febr_1718k_2010",
    "infrastructure", "building_materials", "us",
    "O.E.S. — Nicaragua FE/BR product replacement",
    "Nicaragua",
    "19 Nov 2010: Department of State awards contract to O.E.S., INC. for Phase III/IV FE/BR product replacement and repair & hardware replacement (PoP Nicaragua); obligated USD 1717931.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1717931.46", "2010-11-19", "2010", "", "",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR&HARDWARE REPLACEMENT (R&HR), Nicaragua (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_oes_nicaragua_febr_1718k_2010",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR&HARDWARE REPLACEMENT (R&HR).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0155_1900_SAQMMA07D0009_1900/",
    "Actor: O.E.S., INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1298",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F0155_1900_SAQMMA07D0009_1900 (oes_nicaragua_febr_1718k_2010). Signed 2010-11-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0155_1900_SAQMMA07D0009_1900/.",
    "USASpending: oes_nicaragua_febr_1718k_2010 USD 1.718m. Supports oes_nicaragua_febr_1718k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1717931.46; date_signed 2010-11-19.",
    investment_type="equipment_supply",
)

# === Cycle 1298 ===
row_doc(
    "oes_panama_febr_1700k_2010",
    "infrastructure", "building_materials", "us",
    "O.E.S. — Panama FE/BR product replacement",
    "Panama",
    "7 Dec 2010: Department of State awards contract to O.E.S., INC. for Phase III/IV FE/BR product replacement and R&HR (PoP Panama); obligated USD 1699850.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1699850.44", "2010-12-07", "2010", "", "",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND R&HR (REPAIR&HARDWARE REPLACEMENT), Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_oes_panama_febr_1700k_2010",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND R&HR (REPAIR&HARDWARE REPLACEMENT).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0232_1900_SAQMMA07D0009_1900/",
    "Actor: O.E.S., INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1298",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F0232_1900_SAQMMA07D0009_1900 (oes_panama_febr_1700k_2010). Signed 2010-12-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0232_1900_SAQMMA07D0009_1900/.",
    "USASpending: oes_panama_febr_1700k_2010 USD 1.700m. Supports oes_panama_febr_1700k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1699850.44; date_signed 2010-12-07.",
    investment_type="equipment_supply",
)

# === Cycle 1298 ===
row_doc(
    "tecno_electric_paraguay_power_feeders_2625k_2018",
    "infrastructure", "power_plants_grid", "other",
    "Tecno Electric — Asuncion dedicated power feeders project",
    "Paraguay",
    "11 May 2018: Department of State awards contract to TECNO ELECTRIC SA for Asuncion, Paraguay dedicated power feeders project; obligated USD 2625048.21. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2625048.21", "2018-05-11", "2018", "", "",
    "ASUNCION, PARAQUAY - DEDICATED POWER FEEDERS PROJECT, Paraguay (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tecno_electric_paraguay_power_feeders_2625k_2018",
    "ASUNCION, PARAQUAY - DEDICATED POWER FEEDERS PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5018C0011_1900_-NONE-_-NONE-/",
    "Actor: TECNO ELECTRIC SA — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1298",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5018C0011_1900_-NONE-_-NONE- (tecno_electric_paraguay_power_feeders_2625k_2018). Signed 2018-05-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5018C0011_1900_-NONE-_-NONE-/.",
    "USASpending: tecno_electric_paraguay_power_feeders_2625k_2018 USD 2.625m. Supports tecno_electric_paraguay_power_feeders_2625k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2625048.21; date_signed 2018-05-11.",
    investment_type="epc",
)

# === Cycle 1298 ===
row_doc(
    "misc_haiti_building_project_1079k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti building project",
    "Haiti",
    "17 May 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for building project Haiti; obligated USD 1078698.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1078698.00", "2013-05-17", "2013", "", "",
    "BUILDING PROJECT HAITI IGF::CL::IGF, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_building_project_1079k_2013",
    "BUILDING PROJECT HAITI IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0113_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1298",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13C0113_1900_-NONE-_-NONE- (misc_haiti_building_project_1079k_2013). Signed 2013-05-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0113_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_building_project_1079k_2013 USD 1.079m. Supports misc_haiti_building_project_1079k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1078698.0; date_signed 2013-05-17.",
    investment_type="epc",
)

# === Cycle 1298 ===
row_doc(
    "misc_ecuador_construction_925k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador construction",
    "Ecuador",
    "2 Apr 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction (PoP Ecuador); obligated USD 925299.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "925299.12", "2013-04-02", "2013", "", "",
    "CONSTRUCTION  IGF::OT::IGF, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_construction_925k_2013",
    "CONSTRUCTION  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50013C0016_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1298",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50013C0016_1900_-NONE-_-NONE- (misc_ecuador_construction_925k_2013). Signed 2013-04-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50013C0016_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_construction_925k_2013 USD 0.925m. Supports misc_ecuador_construction_925k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 925299.12; date_signed 2013-04-02.",
    investment_type="epc",
)

# === Cycle 1299 ===
row_doc(
    "hardline_nati_trinidad_febr_1681k_2014",
    "infrastructure", "engineering_epc", "us",
    "Hardline Nati Construction — Trinidad Port of Spain FE/BR replacement",
    "Trinidad and Tobago",
    "28 Sep 2014: Department of State awards contract to HARDLINE NATI CONSTRUCTION LLC for FE/BR replacement and repair — U.S. Embassy Port of Spain; obligated USD 1680773.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1680773.90", "2014-09-28", "2014", "", "",
    "IGF::OT::IGF HNC, LLC - SAQMMA14-D-0085 - TO: SAQMMA14-F-4413 - FEBR REPLACEMENT AND REPAIR PROJECT - US EMBASSY PORT OF, Trinidad and Tobago (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_nati_trinidad_febr_1681k_2014",
    "IGF::OT::IGF HNC, LLC - SAQMMA14-D-0085 - TO: SAQMMA14-F-4413 - FEBR REPLACEMENT AND REPAIR PROJECT - US EMBASSY PORT OF SPAIN, TRINIDAD AND TOBAGO - PERIOD OF PERFORMANCE: 18 MONTHS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4413_1900_SAQMMA14D0085_1900/",
    "Actor: HARDLINE NATI CONSTRUCTION LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1299",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F4413_1900_SAQMMA14D0085_1900 (hardline_nati_trinidad_febr_1681k_2014). Signed 2014-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4413_1900_SAQMMA14D0085_1900/.",
    "USASpending: hardline_nati_trinidad_febr_1681k_2014 USD 1.681m. Supports hardline_nati_trinidad_febr_1681k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1680773.9; date_signed 2014-09-28.",
    investment_type="equipment_supply",
)

# === Cycle 1299 ===
row_doc(
    "hardline_nati_merida_febr_734k_2015",
    "infrastructure", "engineering_epc", "us",
    "Hardline Nati Construction — Mexico Merida FE/BR door replacement",
    "Mexico",
    "29 Sep 2015: Department of State awards contract to HARDLINE NATI CONSTRUCTION LLC for FE/BR R&R — U.S. Consulate General Merida (replace 13 FE/BR doors; replace 2 non-rated with FE/BR); obligated USD 734437.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "734437.00", "2015-09-29", "2015", "", "",
    "IGF::OT::IGF HNC - SAQMMA14D0085 - TO:SAQMMA15F3366 - FEBR R&R PROJECT -  US CONSULATE GENERAL MERIDA, MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_nati_merida_febr_734k_2015",
    "IGF::OT::IGF HNC - SAQMMA14D0085 - TO:SAQMMA15F3366 - FEBR R&R PROJECT -  US CONSULATE GENERAL MERIDA, MEXICO. REPLACE 13 EXISTING FEBR DOORS AND REPLACE 2 NON-RATED WITH FEBR DOORS AT POST.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F3366_1900_SAQMMA14D0085_1900/",
    "Actor: HARDLINE NATI CONSTRUCTION LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1299",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F3366_1900_SAQMMA14D0085_1900 (hardline_nati_merida_febr_734k_2015). Signed 2015-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F3366_1900_SAQMMA14D0085_1900/.",
    "USASpending: hardline_nati_merida_febr_734k_2015 USD 0.734m. Supports hardline_nati_merida_febr_734k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 734437.0; date_signed 2015-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1299 ===
row_doc(
    "misc_colombia_larandia_towers_760k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Larandia towers infrastructure",
    "Colombia",
    "17 Sep 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for infrastructure Larandia towers; obligated USD 760289.14. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "760289.14", "2010-09-17", "2010", "", "",
    "INFRASTRUCTURE LARANDIA TOWERS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_larandia_towers_760k_2010",
    "INFRASTRUCTURE LARANDIA TOWERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0023_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1299",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0023_9700_-NONE-_-NONE- (misc_colombia_larandia_towers_760k_2010). Signed 2010-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0023_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_larandia_towers_760k_2010 USD 0.760m. Supports misc_colombia_larandia_towers_760k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 760289.14; date_signed 2010-09-17.",
    investment_type="epc",
)

# === Cycle 1299 ===
row_doc(
    "misc_colombia_coast_guard_radar_towers_758k_2014",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia Navy Coast Guard radar towers",
    "Colombia",
    "2 Feb 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Navy Coast Guard radar towers; obligated USD 757732.57. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "757732.57", "2014-02-02", "2014", "", "",
    "NAVY COAST GUARD RADAR TOWERS 3, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_coast_guard_radar_towers_758k_2014",
    "NAVY COAST GUARD RADAR TOWERS 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15014CN0010_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1299",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15014CN0010_1900_-NONE-_-NONE- (misc_colombia_coast_guard_radar_towers_758k_2014). Signed 2014-02-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15014CN0010_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_coast_guard_radar_towers_758k_2014 USD 0.758m. Supports misc_colombia_coast_guard_radar_towers_758k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 757732.57; date_signed 2014-02-02.",
    investment_type="epc",
)

# === Cycle 1299 ===
row_doc(
    "mfg_colombia_heliports_guaviare_517k_2011",
    "infrastructure", "engineering_epc", "other",
    "MFG Ingenieria — Colombia San Jose del Guaviare heliports and taxiways",
    "Colombia",
    "21 Jun 2011: Department of State awards contract to MFG INGENIERIA SAS for construction of heliports and taxiways in the San Jose del Guaviare region of Colombia; obligated USD 516637.28. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "516637.28", "2011-06-21", "2011", "", "",
    "CONSTRUCTION OF HELIPORTS AND TAXIWAYS IN THE SAN JOSE DEL GUAVIARE REGION OF COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_heliports_guaviare_517k_2011",
    "CONSTRUCTION OF HELIPORTS AND TAXIWAYS IN THE SAN JOSE DEL GUAVIARE REGION OF COLOMBIA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0004_1900_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1299",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11C0004_1900_-NONE-_-NONE- (mfg_colombia_heliports_guaviare_517k_2011). Signed 2011-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0004_1900_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_heliports_guaviare_517k_2011 USD 0.517m. Supports mfg_colombia_heliports_guaviare_517k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 516637.28; date_signed 2011-06-21.",
    investment_type="epc",
)

# === Cycle 1300 ===
row_doc(
    "human_tech_colombia_copes_shelters_475k_2023",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia COPES rigid shelters",
    "Colombia",
    "18 Aug 2023: Department of State awards contract to HUMAN TECHNOLOGIES CORP for rigid shelters and accessories for Colombia COPES; obligated USD 475081.60. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "475081.60", "2023-08-18", "2023", "", "",
    "RIGID SHELTERS AND ACCESSORIES FOR COLOMBIA COPES, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_copes_shelters_475k_2023",
    "RIGID SHELTERS AND ACCESSORIES FOR COLOMBIA COPES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE23F0045_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1300",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE23F0045_1900_19AQMM21D0007_1900 (human_tech_colombia_copes_shelters_475k_2023). Signed 2023-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE23F0045_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_copes_shelters_475k_2023 USD 0.475m. Supports human_tech_colombia_copes_shelters_475k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 475081.6; date_signed 2023-08-18.",
    investment_type="equipment_supply",
)

# === Cycle 1300 ===
row_doc(
    "hana_quito_anti_ram_barrier_514k_2022",
    "infrastructure", "building_materials", "us",
    "Hana Technologies Construction — Quito anti-ram barrier installation",
    "Ecuador",
    "13 Jun 2022: Department of State awards contract to HANA TECHNOLOGIES CONSTRUCTION, LLC for Quito anti-ram barrier installation; obligated USD 513727.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "513727.00", "2022-06-13", "2022", "", "",
    "QUITO ANTI RAM BARRIER INSTALLATION, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hana_quito_anti_ram_barrier_514k_2022",
    "QUITO ANTI RAM BARRIER INSTALLATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2122_1900_19AQMM21D0065_1900/",
    "Actor: HANA TECHNOLOGIES CONSTRUCTION, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1300",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F2122_1900_19AQMM21D0065_1900 (hana_quito_anti_ram_barrier_514k_2022). Signed 2022-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2122_1900_19AQMM21D0065_1900/.",
    "USASpending: hana_quito_anti_ram_barrier_514k_2022 USD 0.514m. Supports hana_quito_anti_ram_barrier_514k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 513727.0; date_signed 2022-06-13.",
    investment_type="epc",
)

# === Cycle 1300 ===
row_doc(
    "store_q_panama_fence_196k_2023",
    "infrastructure", "building_materials", "other",
    "Store Q Panama — Consul garden non-hardline fence replacement",
    "Panama",
    "27 Jul 2023: Department of State awards contract to STORE Q PANAMA SA for Consul garden non-hardline fence replacement; obligated USD 196264.18. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "196264.18", "2023-07-27", "2023", "", "",
    "CONSUL GARDEN NON-HARDLINE FENCE REPLACEMENT, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_store_q_panama_fence_196k_2023",
    "CONSUL GARDEN NON-HARDLINE FENCE REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0723P0765_1900_-NONE-_-NONE-/",
    "Actor: STORE Q PANAMA SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1300",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0723P0765_1900_-NONE-_-NONE- (store_q_panama_fence_196k_2023). Signed 2023-07-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0723P0765_1900_-NONE-_-NONE-/.",
    "USASpending: store_q_panama_fence_196k_2023 USD 0.196m. Supports store_q_panama_fence_196k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 196264.18; date_signed 2023-07-27.",
    investment_type="epc",
)

# === Cycle 1300 ===
row_doc(
    "misc_colombia_dijin_lab_renovation_170k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia DIJIN lab renovations Bogota",
    "Colombia",
    "19 Apr 2017: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for DIJIN lab renovations at Bogota; obligated USD 170357.94. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "170357.94", "2017-04-19", "2017", "", "",
    "ENV - DIJIN LAB RENOVATIONS AT BOGOTA 3, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_dijin_lab_renovation_170k_2017",
    "ENV - DIJIN LAB RENOVATIONS AT BOGOTA 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1300",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15017C0004_1900_-NONE-_-NONE- (misc_colombia_dijin_lab_renovation_170k_2017). Signed 2017-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0004_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_dijin_lab_renovation_170k_2017 USD 0.170m. Supports misc_colombia_dijin_lab_renovation_170k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 170357.94; date_signed 2017-04-19.",
    investment_type="epc",
)

# === Cycle 1300 ===
row_doc(
    "misc_brazil_residential_renovation_221k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil residential renovation",
    "Brazil",
    "26 Sep 2020: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for residential renovation (PoP Brazil); obligated USD 220940.10. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "220940.10", "2020-09-26", "2020", "", "",
    "RESIDENTIAL RENOVATION, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_residential_renovation_221k_2020",
    "RESIDENTIAL RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P1007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1300",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P1007_1900_-NONE-_-NONE- (misc_brazil_residential_renovation_221k_2020). Signed 2020-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P1007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_residential_renovation_221k_2020 USD 0.221m. Supports misc_brazil_residential_renovation_221k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 220940.1; date_signed 2020-09-26.",
    investment_type="epc",
)

# === Cycle 1301 ===
row_doc(
    "alutiiq_mexico_southern_border_site_prep_8653k_2017",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Information Management — Mexico southern-border site-prep materials (32 sites)",
    "Mexico",
    "20 Jul 2017: Department of State awards contract to ALUTIIQ INFORMATION MANAGEMENT, LLC for materials to complete site preparation for 32 sites on the southern border of Mexico in support of INL Mexico City; obligated USD 8652768.85. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "8652768.85", "2017-07-20", "2017", "", "",
    "MATERIALS TO COMPLETE SITE PREPARATION FOR 32 SITES ON THE SOUTHERN BORDER OF MEXCO IN SUPPORT OF INL MEXICO CITY   IGF:, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_southern_border_site_prep_8653k_2017",
    "MATERIALS TO COMPLETE SITE PREPARATION FOR 32 SITES ON THE SOUTHERN BORDER OF MEXCO IN SUPPORT OF INL MEXICO CITY   IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0183_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ INFORMATION MANAGEMENT, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1301",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0183_1900_-NONE-_-NONE- (alutiiq_mexico_southern_border_site_prep_8653k_2017). Signed 2017-07-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0183_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_southern_border_site_prep_8653k_2017 USD 8.653m. Supports alutiiq_mexico_southern_border_site_prep_8653k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8652768.85; date_signed 2017-07-20.",
    investment_type="equipment_supply",
)

# === Cycle 1301 ===
row_doc(
    "thermal_dynamics_latam_chiller_upgrade_1228k_2011",
    "infrastructure", "engineering_epc", "us",
    "Thermal Dynamics International — LatAm environmental security and chiller upgrade",
    "Argentina",
    "9 Sep 2011: Department of State awards contract to THERMAL DYNAMICS INTERNATIONAL, INC for environmental security and chiller upgrade (Lima, La Paz, Rio de Janeiro & Buenos Aires; PoP Argentina); obligated USD 1228213.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1228213.00", "2011-09-09", "2011", "", "",
    "LIMA, LA PAZ, RIO DE JANEIRO&BUENOS AIRES - ENVIRONMENTAL SECURITY AND CHILLER UPGRADE, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_thermal_dynamics_latam_chiller_upgrade_1228k_2011",
    "LIMA, LA PAZ, RIO DE JANEIRO&BUENOS AIRES - ENVIRONMENTAL SECURITY AND CHILLER UPGRADE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0208_1900_-NONE-_-NONE-/",
    "Actor: THERMAL DYNAMICS INTERNATIONAL, INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1301",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11C0208_1900_-NONE-_-NONE- (thermal_dynamics_latam_chiller_upgrade_1228k_2011). Signed 2011-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0208_1900_-NONE-_-NONE-/.",
    "USASpending: thermal_dynamics_latam_chiller_upgrade_1228k_2011 USD 1.228m. Supports thermal_dynamics_latam_chiller_upgrade_1228k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1228213.0; date_signed 2011-09-09.",
    investment_type="equipment_supply",
)

# === Cycle 1301 ===
row_doc(
    "misc_brazil_dcr_renovation_198k_2020",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Brazil DCR general renovation",
    "Brazil",
    "23 Sep 2020: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC general renovation at DCR QI 09-07-17; obligated USD 198110.45. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "198110.45", "2020-09-23", "2020", "", "",
    "FAC - GENERAL RENOVATION AT DCR - QI 09-07-17, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_dcr_renovation_198k_2020",
    "FAC - GENERAL RENOVATION AT DCR - QI 09-07-17",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0984_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1301",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0984_1900_-NONE-_-NONE- (misc_brazil_dcr_renovation_198k_2020). Signed 2020-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0984_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_dcr_renovation_198k_2020 USD 0.198m. Supports misc_brazil_dcr_renovation_198k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 198110.45; date_signed 2020-09-23.",
    investment_type="epc",
)

# === Cycle 1301 ===
row_doc(
    "misc_brazil_residence_renovation_phase2_195k_2021",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Brazil residence renovation phase II",
    "Brazil",
    "13 Sep 2021: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for BSB FAC residence general renovation phase II QL 10-04-12; obligated USD 195400.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "195400.73", "2021-09-13", "2021", "", "",
    "BSB|FAC| RESIDENCE-GENERAL RENOVATION-PHASE II-QL 10-04-12, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_residence_renovation_phase2_195k_2021",
    "BSB|FAC| RESIDENCE-GENERAL RENOVATION-PHASE II-QL 10-04-12",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1301",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2521C0007_1900_-NONE-_-NONE- (misc_brazil_residence_renovation_phase2_195k_2021). Signed 2021-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_residence_renovation_phase2_195k_2021 USD 0.195m. Supports misc_brazil_residence_renovation_phase2_195k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 195400.73; date_signed 2021-09-13.",
    investment_type="epc",
)

# === Cycle 1301 ===
row_doc(
    "misc_colombia_jungla_electrical_122k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Jungla Camp Pijaos electrical upgrade",
    "Colombia",
    "2 May 2017: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for electrical upgrade at Jungla Camp in Pijaos; obligated USD 122431.41. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "122431.41", "2017-05-02", "2017", "", "",
    "INTER (6-Y-JUNG) ELECTRICAL UPGRADE AT JUNGLA CAMP IN PIJAOS 3, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_jungla_electrical_122k_2017",
    "INTER (6-Y-JUNG) ELECTRICAL UPGRADE AT JUNGLA CAMP IN PIJAOS 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1301",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15017C0006_1900_-NONE-_-NONE- (misc_colombia_jungla_electrical_122k_2017). Signed 2017-05-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_jungla_electrical_122k_2017 USD 0.122m. Supports misc_colombia_jungla_electrical_122k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 122431.41; date_signed 2017-05-02.",
    investment_type="epc",
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
