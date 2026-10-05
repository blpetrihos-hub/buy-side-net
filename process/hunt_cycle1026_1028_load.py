#!/usr/bin/env python3
"""Cycles 1026–1028: USASpending LatAm CapEx residual (~USD0.07–0.11m).

Seeds: 20262026–20262028. Thin top-up dry.
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

# === Cycle 1026 ===
row_doc(
    "nobelcons_lita_helipad_107k_2011",
    "infrastructure", "building_materials", "other",
    "Nobelcons — Ecuador Lita helicopter landing pad",
    "Ecuador",
    "22 Sep 2011: DoD awards contract W9127811P0330 to Nobelcons for construction with incidental design of helicopter landing pad, Lita, Ecuador; obligated USD 106,543.04. CapEx face = award obligation.",
    "106543.04", "2011-09-22", "2011", "", "",
    "Helicopter landing pad, Lita, Ecuador (USASpending description; Lita named but coordinates not sourced — lat/lon blank).",
    "usaspending_nobelcons_lita_helipad_107k_2011",
    "TAS::21 2020::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF HELICOPTER LANDING PAD, LITA, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0330_9700_-NONE-_-NONE-/",
    "Actor: Nobelcons Nobelconstrucciones Cía. Ltda. (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1026",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0330_9700_-NONE-_-NONE- (Nobelcons Lita helipad). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0330_9700_-NONE-_-NONE-/.",
    "USASpending: Nobelcons Lita helipad USD 0.107m. Supports nobelcons_lita_helipad_107k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 106543.04; date_signed 2011-09-22.",
)

row_doc(
    "misc_brazil_dcmr_renovation_106k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil DCMR renovation",
    "Brazil",
    "23 Sep 2021: Department of State awards contract 19BR2521P0931 for DCMR renovation project (PoP Brazil); obligated USD 106,302.20. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "106302.2", "2021-09-23", "2021", "", "",
    "DCMR renovation project, Brazil (USASpending PoP Brazil; site not named — lat/lon blank).",
    "usaspending_misc_brazil_dcmr_renovation_106k_2021",
    "DCMR RENOVATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0931_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1026",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2521P0931_1900_-NONE-_-NONE- (Brazil DCMR renovation). Signed 2021-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0931_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil DCMR renovation USD 0.106m. Supports misc_brazil_dcmr_renovation_106k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 106302.2; date_signed 2021-09-23.",
)

row_doc(
    "cruise_haiti_generators_95k_2010",
    "energy", "power_plants_grid", "us",
    "Cruise Logistics — Haiti 15 generator sets",
    "Haiti",
    "9 Apr 2010: USAID awards contract AIDTRNC001000073 to Cruise Logistics for 15 generator sets and additional maintenance equipment (PoP Haiti); obligated USD 94,840. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "94840", "2010-04-09", "2010", "", "",
    "Fifteen generator sets, Haiti (USASpending PoP Haiti; site not named — lat/lon blank).",
    "usaspending_cruise_haiti_generators_95k_2010",
    "15 GENERATOR SETS AND ADDITIONAL MAINTENANCE EQUIPMENTTAS::72 1000::TAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AIDTRNC001000073_7200_-NONE-_-NONE-/",
    "Actor: Cruise Logistics LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1026",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AIDTRNC001000073_7200_-NONE-_-NONE- (Cruise Haiti generators). Signed 2010-04-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AIDTRNC001000073_7200_-NONE-_-NONE-/.",
    "USASpending: Cruise Haiti generators USD 0.095m. Supports cruise_haiti_generators_95k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94840; date_signed 2010-04-09.",
)

row_doc(
    "misc_guatemala_electrical_94k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala electrical system upgrade",
    "Guatemala",
    "29 Aug 2019: Department of State awards contract 19GT5019P0843 for electrical system upgrade (PoP Guatemala); obligated USD 94,293.19. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "94293.19", "2019-08-29", "2019", "", "",
    "Electrical system upgrade, Guatemala (USASpending PoP Guatemala; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_electrical_94k_2019",
    "ELECTRICAL SYSTEM UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5019P0843_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1026",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5019P0843_1900_-NONE-_-NONE- (Guatemala electrical). Signed 2019-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5019P0843_1900_-NONE-_-NONE-/.",
    "USASpending: Guatemala electrical USD 0.094m. Supports misc_guatemala_electrical_94k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94293.19; date_signed 2019-08-29.",
)

row_doc(
    "misc_honduras_roofs_92k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras roofs ceilings hallways refurbish",
    "Honduras",
    "30 Sep 2013: USAID awards contract AID522O1300070 for refurbish of roofs, ceilings and hallways of the office (PoP Honduras); obligated USD 92,400.06. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "92400.06", "2013-09-30", "2013", "", "",
    "Roofs, ceilings and hallways refurbish, Honduras (USASpending PoP Honduras; site not named — lat/lon blank).",
    "usaspending_misc_honduras_roofs_92k_2013",
    "IGF::OT::IGF REFURBISH OF ROOFS, CEILINGS AND HALLWAYS OF THE OFF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1300070_7200_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1026",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1300070_7200_-NONE-_-NONE- (Honduras roofs). Signed 2013-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1300070_7200_-NONE-_-NONE-/.",
    "USASpending: Honduras roofs USD 0.092m. Supports misc_honduras_roofs_92k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92400.06; date_signed 2013-09-30.",
)

# === Cycle 1027 ===
row_doc(
    "misc_juarez_generator_92k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juárez electric generator",
    "Mexico",
    "26 Sep 2016: Department of State awards contract SMX11516C0004 for BME CDJ electric generator prop 1000 (PoP Mexico); obligated USD 92,399.22. CapEx face = award obligation. Recipient redacted.",
    "92399.22", "2016-09-26", "2016", "31.690", "-106.425",
    "Electric generator, Ciudad Juárez, Mexico (USASpending description CDJ; Ciudad Juárez named).",
    "usaspending_misc_juarez_generator_92k_2016",
    "IGF::OT::IGF - BME CDJ-ELECTRIC GENERATOR PROP 1000 FY16",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1027",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516C0004_1900_-NONE-_-NONE- (Juárez generator). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Juárez generator USD 0.092m. Supports misc_juarez_generator_92k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92399.22; date_signed 2016-09-26.",
)

row_doc(
    "misc_colombia_parking_asphalt_92k_2020",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Colombia parking lot C re-asphalt",
    "Colombia",
    "26 Sep 2020: Department of State awards contract 19C02020C0008 for repair parking lot C — re asphalt (PoP Colombia); obligated USD 91,952.61. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "91952.61", "2020-09-26", "2020", "", "",
    "Parking lot C re-asphalt, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_misc_colombia_parking_asphalt_92k_2020",
    "REPAIR PARKING LOT C - RE ASPHALT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02020C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1027",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02020C0008_1900_-NONE-_-NONE- (Colombia parking asphalt). Signed 2020-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02020C0008_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia parking asphalt USD 0.092m. Supports misc_colombia_parking_asphalt_92k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 91952.61; date_signed 2020-09-26.",
)

row_doc(
    "bolanos_ecuador_ac_92k_2021",
    "energy", "power_plants_grid", "other",
    "Bolaños Albán — Ecuador Oro Province A/C system renovation",
    "Ecuador",
    "26 May 2021: Department of State awards contract 19EC7521P0641 to Bolaños Albán Fausto Tarquino for renovation of A/C system Oro Province (PoP Ecuador); obligated USD 91,917.73. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "91917.73", "2021-05-26", "2021", "", "",
    "A/C system renovation, Oro Province, Ecuador (USASpending description; province named; site not named — lat/lon blank).",
    "usaspending_bolanos_ecuador_ac_92k_2021",
    "1930-PR9746732IN36-DNA_RENOVATION OF A/C SYSTEM_ORO PROVINCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7521P0641_1900_-NONE-_-NONE-/",
    "Actor: Bolaños Albán Fausto Tarquino (Ecuador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1027",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7521P0641_1900_-NONE-_-NONE- (Bolaños Ecuador A/C). Signed 2021-05-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7521P0641_1900_-NONE-_-NONE-/.",
    "USASpending: Bolaños Ecuador A/C USD 0.092m. Supports bolanos_ecuador_ac_92k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 91917.73; date_signed 2021-05-26.",
)

row_doc(
    "hcs_colombia_force_protection_91k_2011",
    "infrastructure", "building_materials", "us",
    "HCS Group — Colombia force protection facilities",
    "Colombia",
    "27 Jun 2011: DoD awards delivery order 0021 under W9127810D0050 to HCS Group for force protection facilities (PoP Colombia); obligated USD 90,533. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "90533", "2011-06-27", "2011", "", "",
    "Force protection facilities, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_hcs_colombia_force_protection_91k_2011",
    "TAS::21 2020::TAS FORCE PROTECTION FACILITIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0021_9700_W9127810D0050_9700/",
    "Actor: HCS Group, P.C. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1027",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0021_9700_W9127810D0050_9700 (HCS Colombia force protection). Signed 2011-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0021_9700_W9127810D0050_9700/.",
    "USASpending: HCS Colombia force protection USD 0.091m. Supports hcs_colombia_force_protection_91k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 90533; date_signed 2011-06-27.",
)

row_doc(
    "wkl_panama_fence_91k_2019",
    "infrastructure", "building_materials", "other",
    "W.K.L. Arquitectos — Panama CMR perimeter fence repair",
    "Panama",
    "13 Aug 2019: Department of State awards contract 19PM0719P0819 to W.K.L. Arquitectos for CMR perimeter fence repair (PoP Panama); obligated USD 90,575. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "90575", "2019-08-13", "2019", "", "",
    "CMR perimeter fence repair, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_wkl_panama_fence_91k_2019",
    "19PM0719P0819 CMR PERIMETER FENCE REPAIR (WKL)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0819_1900_-NONE-_-NONE-/",
    "Actor: W.K.L. Arquitectos S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1027",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0719P0819_1900_-NONE-_-NONE- (WKL Panama fence). Signed 2019-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0819_1900_-NONE-_-NONE-/.",
    "USASpending: WKL Panama fence USD 0.091m. Supports wkl_panama_fence_91k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 90575; date_signed 2019-08-13.",
)

# === Cycle 1028 ===
row_doc(
    "misc_cr_parking_pavement_90k_2015",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Costa Rica EE parking lot east re-pavement",
    "Costa Rica",
    "28 Sep 2015: Department of State awards contract SCS80015C0038 for re-pavement EE parking lot east side (PoP Costa Rica); obligated USD 90,382.94. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "90382.94", "2015-09-28", "2015", "", "",
    "EE parking lot east side re-pavement, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_misc_cr_parking_pavement_90k_2015",
    "FAC-ST 1900.0 7901.C RE-PAVEMENT EE PARKING LOT EAST SIDE IGF::CL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80015C0038_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1028",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80015C0038_1900_-NONE-_-NONE- (CR parking pavement). Signed 2015-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80015C0038_1900_-NONE-_-NONE-/.",
    "USASpending: CR parking pavement USD 0.090m. Supports misc_cr_parking_pavement_90k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 90382.94; date_signed 2015-09-28.",
)

row_doc(
    "atlas_haiti_darius_denis_90k_2014",
    "infrastructure", "building_materials", "other",
    "Atlas Construction — Haiti École Nationale Darius Denis renovation",
    "Haiti",
    "13 Nov 2014: USAID awards BPA call AID521BC1500002 to Atlas Construction for renovation of École Nationale Darius Denis (PoP Haiti); obligated USD 90,343. CapEx face = award obligation. Exact coordinates not sourced — lat/lon blank.",
    "90343", "2014-11-13", "2014", "", "",
    "Renovation of École Nationale Darius Denis, Haiti (USASpending description; school named; coordinates not sourced — lat/lon blank).",
    "usaspending_atlas_haiti_darius_denis_90k_2014",
    "IGF::OT::IGF THE PURPOSE OF THIS BPA CALL IS FOR THE RENOVATION OF ECOLE NATIONALE DARIUS DENIS UNDER THE BLANKET PURCHASE AGREEMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1500002_7200_AID521E1200002_7200/",
    "Actor: Atlas Construction (Haiti) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1028",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521BC1500002_7200_AID521E1200002_7200 (Atlas Darius Denis). Signed 2014-11-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1500002_7200_AID521E1200002_7200/.",
    "USASpending: Atlas Darius Denis USD 0.090m. Supports atlas_haiti_darius_denis_90k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 90343; date_signed 2014-11-13.",
)

row_doc(
    "cummins_honduras_generators_87k_2015",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Honduras five diesel prime-rated generators",
    "Honduras",
    "15 Sep 2015: Department of State awards order SHO80015F0339 to Cummins Power Generation for five complete diesel prime-rated generators (PoP Honduras); obligated USD 87,376.80. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "87376.8", "2015-09-15", "2015", "", "",
    "Five diesel prime-rated generators, Honduras (USASpending PoP Honduras; site not named — lat/lon blank).",
    "usaspending_cummins_honduras_generators_87k_2015",
    "IGF::OT::IGF   FIVE (5) COMPLETE DIESEL PRIME-RATED GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80015F0339_1900_GS07F9004D_4730/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1028",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80015F0339_1900_GS07F9004D_4730 (Cummins Honduras generators). Signed 2015-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80015F0339_1900_GS07F9004D_4730/.",
    "USASpending: Cummins Honduras generators USD 0.087m. Supports cummins_honduras_generators_87k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87376.8; date_signed 2015-09-15.",
)

row_doc(
    "merrick_reynosa_ae_85k_2014",
    "infrastructure", "engineering_epc", "us",
    "Merrick & Company — Mexico Reynosa A&E electrical design",
    "Mexico",
    "29 Sep 2014: USDA awards order AG32KWD140291 to Merrick & Company for A&E electrical design for IS Reynosa MX; obligated USD 85,380. CapEx face = award obligation.",
    "85380", "2014-09-29", "2014", "26.093", "-98.279",
    "A&E electrical design, Reynosa, Mexico (USASpending description; Reynosa named).",
    "usaspending_merrick_reynosa_ae_85k_2014",
    "IGF::OT::IGF A&E ELECTRICAL DESIGN FOR IS REYNOSA MX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWD140291_12K3_AG6395C110097_12K3/",
    "Actor: Merrick & Company (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1028",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AG32KWD140291_12K3_AG6395C110097_12K3 (Merrick Reynosa A&E). Signed 2014-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWD140291_12K3_AG6395C110097_12K3/.",
    "USASpending: Merrick Reynosa A&E USD 0.085m. Supports merrick_reynosa_ae_85k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85380; date_signed 2014-09-29.",
)

row_doc(
    "misc_brazil_go_fences_89k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil GO residence security fences",
    "Brazil",
    "3 Sep 2021: Department of State awards contract 19BR2521P0768 for GO residence security fences / grills (PoP Brazil); obligated USD 89,356.99. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "89356.99", "2021-09-03", "2021", "", "",
    "GO residence security fences/grills, Brazil (USASpending PoP Brazil; site not named — lat/lon blank).",
    "usaspending_misc_brazil_go_fences_89k_2021",
    "GO RESIDENCE- SECURITY FENCES / GRILLS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0768_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1028",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2521P0768_1900_-NONE-_-NONE- (Brazil GO fences). Signed 2021-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0768_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil GO fences USD 0.089m. Supports misc_brazil_go_fences_89k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89356.99; date_signed 2021-09-03.",
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
    added = []
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
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        upsert_bib(bib, bib_by, bib_entry)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    BIB.write_text(yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"cycles1026-1028 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
