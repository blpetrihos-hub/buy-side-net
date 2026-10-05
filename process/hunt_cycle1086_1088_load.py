#!/usr/bin/env python3
"""Cycles 1086–1088: USASpending LatAm CapEx residual (~USD0.048–0.056m).

Seeds: 20262086–20262088. Thin top-up dry.
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


# === Cycle 1086 (seed 20262086) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fabas_colombia_portable_electric_plant_55k_2016",
    "energy", "power_plants_grid", "us",
    "Fabas Consulting Int'l — Colombia portable electric plant for ARECI",
    "Colombia",
    "20 Jun 2016: Department of State awards contract SCO15016M0435 to Fabas Consulting Int'l, Inc. for portable electric plant for ARECI (PoP Colombia); obligated USD 54,855. CapEx face = award obligation. Exact ARECI site unnamed — lat/lon blank.",
    "54855", "2016-06-20", "2016", "", "",
    "Portable electric plant for ARECI, Colombia (USASpending description; ARECI named, site coords not stated — lat/lon blank).",
    "usaspending_fabas_colombia_portable_electric_plant_55k_2016",
    "INTERD (BS) PORTABLE ELECTRIC PLANT FOR ARECI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15016M0435_1900_-NONE-_-NONE-/",
    "Actor: Fabas Consulting Int'l, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1086",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15016M0435_1900_-NONE-_-NONE- (Fabas Colombia portable electric plant). Signed 2016-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15016M0435_1900_-NONE-_-NONE-/.",
    "USASpending: Fabas Colombia portable electric plant USD 0.055m. Supports fabas_colombia_portable_electric_plant_55k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 54855; date_signed 2016-06-20.",
)

row_doc(
    "us_chemical_storage_colombia_storage_building_54k_2012",
    "infrastructure", "building_materials", "us",
    "U.S. Chemical Storage — Colombia storage building",
    "Colombia",
    "2 May 2012: Department of Defense awards order W913FT12F0003 under IDV GS27F0006V to U.S. Chemical Storage, Inc. for a storage building (PoP Colombia); obligated USD 53,717.75. CapEx face = award obligation. Exact storage site unnamed — lat/lon blank.",
    "53717.75", "2012-05-02", "2012", "", "",
    "Storage building, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_us_chemical_storage_colombia_storage_building_54k_2012",
    "STORAGE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12F0003_9700_GS27F0006V_4730/",
    "Actor: U.S. Chemical Storage, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1086",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12F0003_9700_GS27F0006V_4730 (U.S. Chemical Storage Colombia). Signed 2012-05-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12F0003_9700_GS27F0006V_4730/.",
    "USASpending: U.S. Chemical Storage Colombia USD 0.054m. Supports us_chemical_storage_colombia_storage_building_54k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 53717.75; date_signed 2012-05-02.",
)

row_doc(
    "corporacion_recreativa_guatemala_garden_pavers_56k_2022",
    "infrastructure", "bridges_roads", "other",
    "Corporacion Recreativa — Guatemala garden pavers pathway repair",
    "Guatemala",
    "25 Jul 2022: Department of State awards contract 19GT5022C0019 to Corporacion Recreativa SA for garden pavers pathway repair (PoP Guatemala); obligated USD 55,976.82. CapEx face = award obligation. Exact pathway unnamed — lat/lon blank.",
    "55976.82", "2022-07-25", "2022", "", "",
    "Garden pavers pathway repair, Guatemala (USASpending description; pathway not named — lat/lon blank).",
    "usaspending_corporacion_recreativa_guatemala_garden_pavers_56k_2022",
    "GARDEN PAVERS PATHWAY REPAIR VENDOR M7L2EVK9C9J5 CORPORACION RECREATIVA SA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5022C0019_1900_-NONE-_-NONE-/",
    "Actor: Corporacion Recreativa SA (Guatemala) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1086",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5022C0019_1900_-NONE-_-NONE- (Corporacion Recreativa Guatemala garden pavers). Signed 2022-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5022C0019_1900_-NONE-_-NONE-/.",
    "USASpending: Corporacion Recreativa Guatemala garden pavers USD 0.056m. Supports corporacion_recreativa_guatemala_garden_pavers_56k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55976.82; date_signed 2022-07-25.",
)

row_doc(
    "eterna_guatemala_puertos_barrios_design_build_56k_2018",
    "infrastructure", "engineering_epc", "other",
    "Empresa de Construccion y Transporte Eterna — Guatemala Puertos Barrios limited support facility design/build",
    "Guatemala",
    "29 Sep 2018: Department of Defense awards task order W9127818F0811 under IDV W9127816D0102 to Empresa de Construccion y Transporte Eterna S.A. de C.V. to design/build a limited support facility in Puertos Barrios, Guatemala under the Central America MATOC; obligated USD 55,923.80. CapEx face = award obligation. Exact facility footprint unnamed — lat/lon blank.",
    "55923.80", "2018-09-29", "2018", "", "",
    "Design/build limited support facility in Puertos Barrios, Guatemala (USASpending description; Puertos Barrios named, site coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_puertos_barrios_design_build_56k_2018",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/ BUILD A LIMITED SUPPORT FACILITY IN PUERTOS BARRIOS, GUATEMALA UNDER THE CENTRAL AMERICA MATOC.  CONTRACT W91278-16-D-0102.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0811_9700_W9127816D0102_9700/",
    "Actor: Empresa de Construccion y Transporte Eterna S.A. de C.V. (Honduras contractor; PoP Guatemala) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1086",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0811_9700_W9127816D0102_9700 (Eterna Guatemala Puertos Barrios design/build). Signed 2018-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0811_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Guatemala Puertos Barrios design/build USD 0.056m. Supports eterna_guatemala_puertos_barrios_design_build_56k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55923.80; date_signed 2018-09-29.",
)

row_doc(
    "econsa_el_salvador_prefab_wall_razor_wire_56k_2020",
    "infrastructure", "building_materials", "other",
    "Econsa Constructores — El Salvador prefab wall and razor wire for K9 unit",
    "El Salvador",
    "28 Sep 2020: Department of State awards contract 19ES6020P0911 to Econsa Constructores, S.A. de C.V. for supply and installation of prefab wall and razor wire for K9 unit (PoP El Salvador); obligated USD 55,676.61. CapEx face = award obligation. Exact K9 unit site unnamed — lat/lon blank.",
    "55676.61", "2020-09-28", "2020", "", "",
    "Supply and installation of prefab wall and razor wire for K9 unit, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_econsa_el_salvador_prefab_wall_razor_wire_56k_2020",
    "INL- SUPPLY&INSTALL. OF PREFAB. WALL&RAZOR WIRE  F/K9 U.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0911_1900_-NONE-_-NONE-/",
    "Actor: Econsa Constructores, S.A. de C.V. (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1086",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6020P0911_1900_-NONE-_-NONE- (Econsa El Salvador prefab wall). Signed 2020-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0911_1900_-NONE-_-NONE-/.",
    "USASpending: Econsa El Salvador prefab wall USD 0.056m. Supports econsa_el_salvador_prefab_wall_razor_wire_56k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55676.61; date_signed 2020-09-28.",
)

# === Cycle 1087 (seed 20262087) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "kpff_ecuador_quito_seismic_survey_53k_2013",
    "infrastructure", "engineering_epc", "us",
    "KPFF — Ecuador Quito seismic survey engineering services",
    "Ecuador",
    "2 Jul 2013: Department of State awards order SAQMMA13F1953 under IDV SAQMMA08D0070 to KPFF, Inc. for seismic survey engineering services in Quito, Ecuador; obligated USD 53,211.39. CapEx face = award obligation. Exact survey footprint unnamed — lat/lon blank.",
    "53211.39", "2013-07-02", "2013", "", "",
    "Seismic survey engineering services, Quito, Ecuador (USASpending description; Quito named, site coords not stated — lat/lon blank).",
    "usaspending_kpff_ecuador_quito_seismic_survey_53k_2013",
    "IGF::OT::IGF - SEISMIC SURVEY ENGINEERING SERVICES - QUITO ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F1953_1900_SAQMMA08D0070_1900/",
    "Actor: KPFF, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1087",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F1953_1900_SAQMMA08D0070_1900 (KPFF Ecuador Quito seismic survey). Signed 2013-07-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F1953_1900_SAQMMA08D0070_1900/.",
    "USASpending: KPFF Ecuador Quito seismic survey USD 0.053m. Supports kpff_ecuador_quito_seismic_survey_53k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 53211.39; date_signed 2013-07-02.",
)

row_doc(
    "wje_bolivia_lapaz_seismic_support_49k_2014",
    "infrastructure", "engineering_epc", "us",
    "Wiss Janney Elstner — Bolivia La Paz AE seismic support",
    "Bolivia",
    "26 Aug 2014: Department of State awards order SAQMMA14F2968 under IDV SAQMMA14D0021 to Wiss Janney Elstner Associates Inc for AE service seismic support in La Paz, Bolivia; obligated USD 49,282.16. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49282.16", "2014-08-26", "2014", "", "",
    "AE service seismic support in La Paz, Bolivia (USASpending description; La Paz named, site coords not stated — lat/lon blank).",
    "usaspending_wje_bolivia_lapaz_seismic_support_49k_2014",
    "IGF::OT::IGF AE SERVICE SEISMIC SUPPORT IN LAPAZ BOLIVIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F2968_1900_SAQMMA14D0021_1900/",
    "Actor: Wiss Janney Elstner Associates Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1087",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F2968_1900_SAQMMA14D0021_1900 (WJE Bolivia La Paz seismic). Signed 2014-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F2968_1900_SAQMMA14D0021_1900/.",
    "USASpending: WJE Bolivia La Paz seismic USD 0.049m. Supports wje_bolivia_lapaz_seismic_support_49k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49282.16; date_signed 2014-08-26.",
)

row_doc(
    "misc_bahamas_chancery_air_handler_replace_56k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bahamas chancery 8-ton air handler replacement",
    "Bahamas",
    "31 Aug 2017: Department of State awards contract SBF50017M0315 for chancery replacement of 8-ton air handler units on the 2nd floor (PoP Bahamas); obligated USD 55,893.63. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "55893.63", "2017-08-31", "2017", "", "",
    "Chancery replace 8-ton air handler units on the 2nd floor, Bahamas (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_chancery_air_handler_replace_56k_2017",
    "CHANCERY - REPLACE 8TON AIR HANDLER UNITS ON THE 2ND FLOOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017M0315_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1087",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017M0315_1900_-NONE-_-NONE- (Bahamas chancery air handler). Signed 2017-08-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017M0315_1900_-NONE-_-NONE-/.",
    "USASpending: Bahamas chancery air handler USD 0.056m. Supports misc_bahamas_chancery_air_handler_replace_56k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55893.63; date_signed 2017-08-31.",
)

row_doc(
    "misc_argentina_exec_carpet_replacement_56k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina executive carpet replacement",
    "Argentina",
    "28 Sep 2023: Department of State awards contract 19AR2023P1382 for FAC executive carpet replacement (PoP Argentina); obligated USD 55,864.49. CapEx face = award obligation. Exact floor unnamed — lat/lon blank.",
    "55864.49", "2023-09-28", "2023", "", "",
    "FAC executive carpet replacement, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_argentina_exec_carpet_replacement_56k_2023",
    "FAC - EXEC - CARPET REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2023P1382_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1087",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2023P1382_1900_-NONE-_-NONE- (Argentina executive carpet). Signed 2023-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2023P1382_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina executive carpet USD 0.056m. Supports misc_argentina_exec_carpet_replacement_56k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55864.49; date_signed 2023-09-28.",
)

row_doc(
    "misc_paraguay_rssi_drainage_barriers_56k_2017",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Paraguay RSSI drainage for barriers at CAC 1 and CAC 3",
    "Paraguay",
    "11 Aug 2017: Department of State awards contract SPA10017M0323 for RSSI drainage for barriers at CAC 1 and CAC 3 (PoP Paraguay); obligated USD 55,752. CapEx face = award obligation. Exact CAC sites unnamed — lat/lon blank.",
    "55752", "2017-08-11", "2017", "", "",
    "RSSI drainage for barriers at CAC 1 and CAC 3, Paraguay (USASpending description; CAC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_paraguay_rssi_drainage_barriers_56k_2017",
    "IGF::OT::IGF RSSI DRAINAGE FOR BARRIERS AT CAC 1&CAC 3",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10017M0323_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1087",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPA10017M0323_1900_-NONE-_-NONE- (Paraguay RSSI drainage barriers). Signed 2017-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10017M0323_1900_-NONE-_-NONE-/.",
    "USASpending: Paraguay RSSI drainage barriers USD 0.056m. Supports misc_paraguay_rssi_drainage_barriers_56k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55752; date_signed 2017-08-11.",
)

# === Cycle 1088 (seed 20262088) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "crosby_guatemala_cdc_seismic_evaluation_49k_2013",
    "infrastructure", "engineering_epc", "us",
    "The Crosby Group — Guatemala CDC building seismic evaluation",
    "Guatemala",
    "2 May 2013: Department of State awards order SAQMMA13F1448 under IDV SAQMMA08D0068 to The Crosby Group-Engineers/Architects for seismic evaluation of CDC building Guatemala; obligated USD 48,910. CapEx face = award obligation. Exact CDC building unnamed — lat/lon blank.",
    "48910", "2013-05-02", "2013", "", "",
    "Seismic evaluation CDC building, Guatemala (USASpending description; CDC building named, site coords not stated — lat/lon blank).",
    "usaspending_crosby_guatemala_cdc_seismic_evaluation_49k_2013",
    "IGF::OT::IGF  SEISMIC EVALUATION CDC BUILDING GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F1448_1900_SAQMMA08D0068_1900/",
    "Actor: The Crosby Group-Engineers/Architects (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1088",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F1448_1900_SAQMMA08D0068_1900 (Crosby Guatemala CDC seismic). Signed 2013-05-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F1448_1900_SAQMMA08D0068_1900/.",
    "USASpending: Crosby Guatemala CDC seismic USD 0.049m. Supports crosby_guatemala_cdc_seismic_evaluation_49k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 48910; date_signed 2013-05-02.",
)

row_doc(
    "alpha_tec_panama_inl_roofing_incinerator_48k_2023",
    "infrastructure", "building_materials", "us",
    "Alpha Tec Services — Panama INL roofing construction materials for incinerator",
    "Panama",
    "19 Feb 2023: Department of State awards contract 19PM0723P0216 to Alpha Tec Services Inc for INL roofing construction materials incinerator (PoP Panama); obligated USD 47,687.26. CapEx face = award obligation. Exact incinerator site unnamed — lat/lon blank.",
    "47687.26", "2023-02-19", "2023", "", "",
    "INL roofing construction materials for incinerator, Panama (USASpending description; incinerator named, site coords not stated — lat/lon blank).",
    "usaspending_alpha_tec_panama_inl_roofing_incinerator_48k_2023",
    "INL ROOFING CONSTRUCTION MATERIALS INCINERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0723P0216_1900_-NONE-_-NONE-/",
    "Actor: Alpha Tec Services Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1088",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0723P0216_1900_-NONE-_-NONE- (Alpha Tec Panama INL roofing). Signed 2023-02-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0723P0216_1900_-NONE-_-NONE-/.",
    "USASpending: Alpha Tec Panama INL roofing USD 0.048m. Supports alpha_tec_panama_inl_roofing_incinerator_48k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47687.26; date_signed 2023-02-19.",
)

row_doc(
    "misc_uruguay_warehouse_insulation_56k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Uruguay new warehouse building insulation install",
    "Uruguay",
    "10 Sep 2010: Department of State awards contract SUY60010M0772 for labor and materials to install building insulation at new warehouse (PoP Uruguay); obligated USD 55,749. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.",
    "55749", "2010-09-10", "2010", "", "",
    "Labor and materials to install building insulation at new warehouse, Uruguay (USASpending description; warehouse not named — lat/lon blank).",
    "usaspending_misc_uruguay_warehouse_insulation_56k_2010",
    "LABOR AND MATERIALS TO INSTALL BUILDING INSULATION AT NEW WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60010M0772_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1088",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60010M0772_1900_-NONE-_-NONE- (Uruguay warehouse insulation). Signed 2010-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60010M0772_1900_-NONE-_-NONE-/.",
    "USASpending: Uruguay warehouse insulation USD 0.056m. Supports misc_uruguay_warehouse_insulation_56k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55749; date_signed 2010-09-10.",
)

row_doc(
    "misc_brazil_2nd_floor_refurbish_56k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil 2nd floor area refurbishing",
    "Brazil",
    "29 Sep 2010: Department of State awards contract SBR82010M3894 for refurbishing service of 2nd floor area (PoP Brazil); obligated USD 55,580. CapEx face = award obligation. Exact floor unnamed — lat/lon blank.",
    "55580", "2010-09-29", "2010", "", "",
    "Refurbishing service of 2nd floor area, Brazil (USASpending description; floor not named — lat/lon blank).",
    "usaspending_misc_brazil_2nd_floor_refurbish_56k_2010",
    "REFURBISHING SERVICE OF 2ND FLOOR AREA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82010M3894_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1088",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82010M3894_1900_-NONE-_-NONE- (Brazil 2nd floor refurbish). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82010M3894_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil 2nd floor refurbish USD 0.056m. Supports misc_brazil_2nd_floor_refurbish_56k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55580; date_signed 2010-09-29.",
)

row_doc(
    "misc_mexico_cdj_pavement_seal_56k_2018",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juarez government property pavement seal",
    "Mexico",
    "28 Aug 2018: Department of State awards contract 19MX1118P0178 for CDJ FAC 7901 pavement seal on government property 1000 (PoP Mexico); obligated USD 55,500.20. CapEx face = award obligation. Exact property unnamed — lat/lon blank.",
    "55500.20", "2018-08-28", "2018", "", "",
    "CDJ FAC 7901 pavement seal government property 1000, Mexico (USASpending description; Ciudad Juarez implied, property coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_pavement_seal_56k_2018",
    "IGF::OT::IGF - CDJ FAC 7901 PAVEMENT SEAL GOV PROP 1000",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1118P0178_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1088",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1118P0178_1900_-NONE-_-NONE- (Mexico CDJ pavement seal). Signed 2018-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1118P0178_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico CDJ pavement seal USD 0.056m. Supports misc_mexico_cdj_pavement_seal_56k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55500.20; date_signed 2018-08-28.",
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
