#!/usr/bin/env python3
"""Cycles 1062–1064: USASpending LatAm CapEx residual (~USD0.036–0.066m).

Seeds: 20262062–20262064. Thin top-up dry.
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


# === Cycle 1062 (seed 20262062) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "usmax_mexico_tss_65k_2017",
    "infrastructure", "building_materials", "us",
    "USMAX — Mexico technical security system installation",
    "Mexico",
    "11 Apr 2017: Department of State awards order SAQMMA17F1288 to USMAX Corporation for technical security system installation TSS (PoP Mexico); obligated USD 65,148.35. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "65148.35", "2017-04-11", "2017", "", "",
    "Technical security system (TSS) installation, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_usmax_mexico_tss_65k_2017",
    "TECHNICAL SECURITY SYSTEM INSTALLATION TSSIGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F1288_1900_SAQMMA13D0055_1900/",
    "Actor: USMAX Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1062",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17F1288_1900_SAQMMA13D0055_1900 (USMAX Mexico TSS). Signed 2017-04-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F1288_1900_SAQMMA13D0055_1900/.",
    "USASpending: USMAX Mexico TSS USD 0.065m. Supports usmax_mexico_tss_65k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65148.35; date_signed 2017-04-11.",
)

row_doc(
    "trinity_guyana_camera_mounts_38k_2023",
    "infrastructure", "building_materials", "us",
    "Trinity Enterprise Services — Guyana camera mounts installation",
    "Guyana",
    "27 Jul 2023: Department of State awards contract 19GY2023C0001 to Trinity Enterprise Services, LLC for installation of camera mounts (PoP Guyana); obligated USD 37,839.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "37839.44", "2023-07-27", "2023", "", "",
    "Camera mounts installation, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_trinity_guyana_camera_mounts_38k_2023",
    "INSTALLATION OF CAMERA MOUNTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2023C0001_1900_-NONE-_-NONE-/",
    "Actor: Trinity Enterprise Services, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1062",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2023C0001_1900_-NONE-_-NONE- (Trinity Guyana camera mounts). Signed 2023-07-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2023C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Trinity Guyana camera mounts USD 0.038m. Supports trinity_guyana_camera_mounts_38k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 37839.44; date_signed 2023-07-27.",
)

row_doc(
    "misc_argentina_led_panels_66k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina LED light panels and installation",
    "Argentina",
    "30 Sep 2016: Department of State awards contract SAR20016M0849 for LED light panels and installation services (PoP Argentina); obligated USD 66,044.41. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "66044.41", "2016-09-30", "2016", "", "",
    "LED light panels and installation, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_argentina_led_panels_66k_2016",
    "FM - LED LIGHT PANELS AND INSTALLATION SERVICES IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20016M0849_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1062",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20016M0849_1900_-NONE-_-NONE- (Argentina LED panels). Signed 2016-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20016M0849_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina LED panels USD 0.066m. Supports misc_argentina_led_panels_66k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66044.41; date_signed 2016-09-30.",
)

row_doc(
    "flores_ecuador_dcr_kitchen_bath_65k_2024",
    "infrastructure", "building_materials", "other",
    "Flores Serrano — Ecuador DCR kitchen and master bathroom renovation",
    "Ecuador",
    "28 Sep 2024: Department of State awards contract 19EC7524C0020 to Flores Serrano Guillermo Sebastian for DCR kitchen and master bathroom renovation (PoP Ecuador); obligated USD 65,269.40. CapEx face = award obligation. Exact DCR site unnamed — lat/lon blank.",
    "65269.40", "2024-09-28", "2024", "", "",
    "DCR kitchen and master bathroom renovation, Ecuador (USASpending description; DCR named, site coords not stated — lat/lon blank).",
    "usaspending_flores_ecuador_dcr_kitchen_bath_65k_2024",
    "FAC-7355RSTR-DCR-KITCHEN AND MASTER BATHROOM RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7524C0020_1900_-NONE-_-NONE-/",
    "Actor: Flores Serrano Guillermo Sebastian (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1062",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7524C0020_1900_-NONE-_-NONE- (Flores Ecuador DCR kitchen/bath). Signed 2024-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7524C0020_1900_-NONE-_-NONE-/.",
    "USASpending: Flores Ecuador DCR kitchen/bath USD 0.065m. Supports flores_ecuador_dcr_kitchen_bath_65k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65269.40; date_signed 2024-09-28.",
)

row_doc(
    "misc_brazil_cooling_tower_drift_65k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil cooling tower drift eliminators replacement",
    "Brazil",
    "29 Aug 2016: Department of State awards contract SBR93016M0748 for replacement in kind of the cooling tower's drift eliminators (PoP Brazil); obligated USD 65,201.86. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "65201.86", "2016-08-29", "2016", "", "",
    "Cooling tower drift eliminators replacement, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_cooling_tower_drift_65k_2016",
    "REPLACEMENT IN KIND OF THE COOLING TOWER'S DRIFT ELIMINATORS ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93016M0748_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1062",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93016M0748_1900_-NONE-_-NONE- (Brazil cooling tower drift). Signed 2016-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93016M0748_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil cooling tower drift USD 0.065m. Supports misc_brazil_cooling_tower_drift_65k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65201.86; date_signed 2016-08-29.",
)

# === Cycle 1063 (seed 20262063) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "daikin_uruguay_chancery_chillers_36k_2026",
    "energy", "power_plants_grid", "us",
    "Daikin Applied Americas — Uruguay chancery main chillers repair",
    "Uruguay",
    "24 Apr 2026: Department of State awards contract 19UY6026P0251 to Daikin Applied Americas Inc for repair of CHCY main chillers (PoP Uruguay); obligated USD 36,340. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "36340", "2026-04-24", "2026", "", "",
    "Chancery main chillers repair, Uruguay (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_daikin_uruguay_chancery_chillers_36k_2026",
    "FAC - REPAIR OF CHCY MAIN CHILLERS - 7901SUST",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6026P0251_1900_-NONE-_-NONE-/",
    "Actor: Daikin Applied Americas Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1063",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6026P0251_1900_-NONE-_-NONE- (Daikin Uruguay chillers). Signed 2026-04-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6026P0251_1900_-NONE-_-NONE-/.",
    "USASpending: Daikin Uruguay chillers USD 0.036m. Supports daikin_uruguay_chancery_chillers_36k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 36340; date_signed 2026-04-24.",
)

row_doc(
    "fluid_solutions_guyana_fire_pump_36k_2026",
    "resources", "water", "us",
    "Fluid Solutions — Guyana fire engine pump system",
    "Guyana",
    "4 Jun 2026: Department of State awards contract 19GY2026P0234 to Fluid Solutions LLC for fire engine pump system (PoP Guyana); obligated USD 35,660.28. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "35660.28", "2026-06-04", "2026", "", "",
    "Fire engine pump system, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_fluid_solutions_guyana_fire_pump_36k_2026",
    "FIRE ENGINE PUMP SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2026P0234_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1063",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2026P0234_1900_-NONE-_-NONE- (Fluid Solutions Guyana fire pump). Signed 2026-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2026P0234_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions Guyana fire pump USD 0.036m. Supports fluid_solutions_guyana_fire_pump_36k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 35660.28; date_signed 2026-06-04.",
)

row_doc(
    "misc_mexico_little_amigos_65k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico former Little Amigos space remodel",
    "Mexico",
    "20 Sep 2010: Department of State awards contract SMX53010M0814 for OBO remodelation of former Little Amigos space (PoP Mexico); obligated USD 64,957.19. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "64957.19", "2010-09-20", "2010", "", "",
    "Remodel of former Little Amigos space, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_little_amigos_65k_2010",
    "MEX/OBO REMODELATION OF FORMER LITTLE AMIGOS SPACE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0814_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1063",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0814_1900_-NONE-_-NONE- (Mexico Little Amigos remodel). Signed 2010-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0814_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico Little Amigos remodel USD 0.065m. Supports misc_mexico_little_amigos_65k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64957.19; date_signed 2010-09-20.",
)

row_doc(
    "coyservic_honduras_coe_office_64k_2011",
    "infrastructure", "building_materials", "other",
    "Coyservic — Honduras COE field office renovation",
    "Honduras",
    "30 Jun 2011: Department of Defense awards contract W9127811P0250 to Coyservic for renovate COE field office (PoP Honduras); obligated USD 64,442. CapEx face = award obligation. Exact office unnamed — lat/lon blank.",
    "64442", "2011-06-30", "2011", "", "",
    "COE field office renovation, Honduras (USASpending description; office not named — lat/lon blank).",
    "usaspending_coyservic_honduras_coe_office_64k_2011",
    "TAS::96 4902::TAS RENOVATE COE FIELD OFFICE,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0250_9700_-NONE-_-NONE-/",
    "Actor: Coyservic (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1063",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0250_9700_-NONE-_-NONE- (Coyservic Honduras COE office). Signed 2011-06-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0250_9700_-NONE-_-NONE-/.",
    "USASpending: Coyservic Honduras COE office USD 0.064m. Supports coyservic_honduras_coe_office_64k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64442; date_signed 2011-06-30.",
)

row_doc(
    "misc_brazil_mail_room_renovation_64k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil second-floor mail room renovation for consular expansion",
    "Brazil",
    "25 Apr 2012: Department of State awards contract SBR82012C0004 for second floor renovation for mail room for consular expansion (PoP Brazil); obligated USD 64,404.45. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "64404.45", "2012-04-25", "2012", "", "",
    "Second-floor mail room renovation for consular expansion, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_mail_room_renovation_64k_2012",
    "SECOND FLOOR RENOVATION FOR MAIL ROOM FOR CONSULAR EXPANSION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82012C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1063",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82012C0004_1900_-NONE-_-NONE- (Brazil mail room renovation). Signed 2012-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82012C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil mail room renovation USD 0.064m. Supports misc_brazil_mail_room_renovation_64k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64404.45; date_signed 2012-04-25.",
)

# === Cycle 1064 (seed 20262064) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "multistack_peru_chiller_coils_55k_2025",
    "energy", "power_plants_grid", "us",
    "Multistack — Peru chancery Multistack chiller coils replacement",
    "Peru",
    "19 Sep 2025: Department of State awards contract 19PE5025P1524 to Multistack LLC for coils replacement on Multistack chiller at chancery (PoP Peru); obligated USD 55,000. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "55000", "2025-09-19", "2025", "", "",
    "Coils replacement on Multistack chiller at chancery, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_multistack_peru_chiller_coils_55k_2025",
    "FAC - COILS REPLACEMENT ON MULTISTACK CHILER AT CHANCERY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5025P1524_1900_-NONE-_-NONE-/",
    "Actor: Multistack LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1064",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5025P1524_1900_-NONE-_-NONE- (Multistack Peru chiller coils). Signed 2025-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5025P1524_1900_-NONE-_-NONE-/.",
    "USASpending: Multistack Peru chiller coils USD 0.055m. Supports multistack_peru_chiller_coils_55k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55000; date_signed 2025-09-19.",
)

row_doc(
    "hallpass_honduras_cmr_led_53k_2013",
    "infrastructure", "building_materials", "us",
    "Hallpass Capital — Honduras CMR LED lighting",
    "Honduras",
    "27 Sep 2013: Department of State awards order SHO80013F0353 to Hallpass Capital Inc for CMR LED lighting (PoP Honduras); obligated USD 52,641.50. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "52641.50", "2013-09-27", "2013", "", "",
    "CMR LED lighting, Honduras (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_hallpass_honduras_cmr_led_53k_2013",
    "FM- CMR LED LIGHTING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013F0353_1900_GS07F0413Y_4732/",
    "Actor: Hallpass Capital Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1064",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80013F0353_1900_GS07F0413Y_4732 (Hallpass Honduras CMR LED). Signed 2013-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013F0353_1900_GS07F0413Y_4732/.",
    "USASpending: Hallpass Honduras CMR LED USD 0.053m. Supports hallpass_honduras_cmr_led_53k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52641.50; date_signed 2013-09-27.",
)

row_doc(
    "misc_brazil_warehouse_chillers_64k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil warehouse chillers replacement",
    "Brazil",
    "20 Sep 2016: Department of State awards contract SBR25016M1709 for replacement chillers for warehouse bldg (PoP Brazil); obligated USD 64,090.77. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.",
    "64090.77", "2016-09-20", "2016", "", "",
    "Replacement chillers for warehouse building, Brazil (USASpending description; warehouse not named — lat/lon blank).",
    "usaspending_misc_brazil_warehouse_chillers_64k_2016",
    "REPLACEMENT CHILLERS FOR WAREHOUSE BLDG",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25016M1709_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1064",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25016M1709_1900_-NONE-_-NONE- (Brazil warehouse chillers). Signed 2016-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25016M1709_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil warehouse chillers USD 0.064m. Supports misc_brazil_warehouse_chillers_64k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64090.77; date_signed 2016-09-20.",
)

row_doc(
    "misc_honduras_comayagua_transformer_64k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras Comayagua EIC electrical transformer",
    "Honduras",
    "24 Jul 2017: Department of State awards contract SHO80017M0830 for INL CARSI electrical transformer for EIC Comayagua (PoP Honduras); obligated USD 64,000. CapEx face = award obligation.",
    "64000", "2017-07-24", "2017", "14.461", "-87.637",
    "Electrical transformer for EIC Comayagua, Honduras (USASpending description; Comayagua named).",
    "usaspending_misc_honduras_comayagua_transformer_64k_2017",
    "INL CARSI - ELECTRICAL TRANSFORMER FOR EIC COMAYAGUA 1930.0",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M0830_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1064",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80017M0830_1900_-NONE-_-NONE- (Honduras Comayagua transformer). Signed 2017-07-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M0830_1900_-NONE-_-NONE-/.",
    "USASpending: Honduras Comayagua transformer USD 0.064m. Supports misc_honduras_comayagua_transformer_64k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64000; date_signed 2017-07-24.",
)

row_doc(
    "pavimentaciones_peru_asphalt_de_64k_2020",
    "infrastructure", "bridges_roads", "other",
    "Pavimentaciones — Peru asphalt repair parking lots D&E",
    "Peru",
    "16 Sep 2020: Department of State awards contract 19PE5020C0010 to Pavimentaciones Sociedad Anonima Cerrada for asphalt repair to parking lots D&E (PoP Peru); obligated USD 64,105.31. CapEx face = award obligation. Exact lots unnamed — lat/lon blank.",
    "64105.31", "2020-09-16", "2020", "", "",
    "Asphalt repair to parking lots D&E, Peru (USASpending description; lots not named — lat/lon blank).",
    "usaspending_pavimentaciones_peru_asphalt_de_64k_2020",
    "ASPHALT REPAIR TO PARKING LOTS D&E",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5020C0010_1900_-NONE-_-NONE-/",
    "Actor: Pavimentaciones Sociedad Anonima Cerrada (Peru) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1064",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5020C0010_1900_-NONE-_-NONE- (Pavimentaciones Peru lots D&E). Signed 2020-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5020C0010_1900_-NONE-_-NONE-/.",
    "USASpending: Pavimentaciones Peru lots D&E USD 0.064m. Supports pavimentaciones_peru_asphalt_de_64k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64105.31; date_signed 2020-09-16.",
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
