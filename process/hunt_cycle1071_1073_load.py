#!/usr/bin/env python3
"""Cycles 1071–1073: USASpending LatAm CapEx residual (~USD0.057–0.063m).

Seeds: 20262071–20262073. Thin top-up dry.
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


# === Cycle 1071 (seed 20262071) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hcs_honduras_jlsa_renovations_59k_2016",
    "infrastructure", "building_materials", "us",
    "HCS Group — Honduras FY16 JLSA renovations",
    "Honduras",
    "5 Aug 2016: Department of Defense awards task order 0010 under IDV W9127814D0057 to HCS Group, P.C. for FY16 JLSA renovations (PoP Honduras); obligated USD 58,821.14. CapEx face = award obligation. Exact JLSA site unnamed — lat/lon blank.",
    "58821.14", "2016-08-05", "2016", "", "",
    "FY16 JLSA renovations, Honduras (USASpending description; JLSA named, site coords not stated — lat/lon blank).",
    "usaspending_hcs_honduras_jlsa_renovations_59k_2016",
    "IGF::OT::IGF   FY16 JLSA RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127814D0057_9700/",
    "Actor: HCS Group, P.C. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1071",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127814D0057_9700 (HCS Honduras JLSA renovations). Signed 2016-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127814D0057_9700/.",
    "USASpending: HCS Honduras JLSA renovations USD 0.059m. Supports hcs_honduras_jlsa_renovations_59k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58821.14; date_signed 2016-08-05.",
)

row_doc(
    "patterson_pump_mexico_juarez_sprinkler_57k_2011",
    "resources", "water", "us",
    "Patterson Pump — Mexico Ciudad Juarez fire sprinkler pump",
    "Mexico",
    "23 Mar 2011: Department of State awards contract SMX11511M0246 to Patterson Pump Co for OBO Capital Programs Ciudad Juarez fire sprinkler pump project (PoP Mexico); obligated USD 57,253. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "57253", "2011-03-23", "2011", "", "",
    "Fire sprinkler pump project, Ciudad Juarez, Mexico (USASpending description; Ciudad Juarez named, site coords not stated — lat/lon blank).",
    "usaspending_patterson_pump_mexico_juarez_sprinkler_57k_2011",
    "OBO-CAPITAL PROGRAMS CD JUAREZ FIRE SPRINKLER PUMP PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11511M0246_1900_-NONE-_-NONE-/",
    "Actor: Patterson Pump Co (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1071",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11511M0246_1900_-NONE-_-NONE- (Patterson Pump Juarez sprinkler). Signed 2011-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11511M0246_1900_-NONE-_-NONE-/.",
    "USASpending: Patterson Pump Juarez sprinkler USD 0.057m. Supports patterson_pump_mexico_juarez_sprinkler_57k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57253; date_signed 2011-03-23.",
)

row_doc(
    "misc_ecuador_embassy_painting_63k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador embassy installation and residences painting",
    "Ecuador",
    "26 Jul 2013: Department of State awards contract SEC75013C0004 for painting services embasy installation and residences (PoP Ecuador); obligated USD 62,912.83. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "62912.83", "2013-07-26", "2013", "", "",
    "Painting services for embassy installation and residences, Ecuador (USASpending description; sites not named — lat/lon blank).",
    "usaspending_misc_ecuador_embassy_painting_63k_2013",
    "IGF::OT::IGF 1900-L-1/1-PR2507819PAINTING SERV EMBASSY INST AND RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75013C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1071",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75013C0004_1900_-NONE-_-NONE- (Ecuador embassy painting). Signed 2013-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75013C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador embassy painting USD 0.063m. Supports misc_ecuador_embassy_painting_63k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62912.83; date_signed 2013-07-26.",
)

row_doc(
    "misc_mexico_puebla_asphalt_63k_2012",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Mexico Puebla police academy asphalt",
    "Mexico",
    "9 Apr 2012: Department of State awards contract SMX53012M0742 for asphalt to support Puebla police academy (PoP Mexico); obligated USD 62,713.29. CapEx face = award obligation. Exact academy site unnamed — lat/lon blank.",
    "62713.29", "2012-04-09", "2012", "", "",
    "Asphalt to support Puebla police academy, Mexico (USASpending description; Puebla named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_puebla_asphalt_63k_2012",
    "NAS-MI IN41MX72 2R32 ASPHALT TO SUPPORT PUEBLA POLICE ACADEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M0742_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads. Holdover closed.",
    "hunt_cycle1071",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M0742_1900_-NONE-_-NONE- (Mexico Puebla asphalt). Signed 2012-04-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M0742_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico Puebla asphalt USD 0.063m. Supports misc_mexico_puebla_asphalt_63k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62713.29; date_signed 2012-04-09.",
)

row_doc(
    "misc_colombia_tulua_aravi_building_63k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Tulua CNP air base ARAVI administrative building",
    "Colombia",
    "23 Apr 2012: Department of State awards contract SCO15012M1008 for ARAVI administrative building at Tulua CNP air base (PoP Colombia); obligated USD 62,589.04. CapEx face = award obligation. Exact building coords not stated — lat/lon blank.",
    "62589.04", "2012-04-23", "2012", "", "",
    "ARAVI administrative building at Tulua CNP air base, Colombia (USASpending description; Tulua named, building coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_tulua_aravi_building_63k_2012",
    "ARAVI ADMINISTRATIVE BUILDING AT TULUA CNP AIR BASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M1008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1071",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012M1008_1900_-NONE-_-NONE- (Colombia Tulua ARAVI). Signed 2012-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M1008_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia Tulua ARAVI USD 0.063m. Supports misc_colombia_tulua_aravi_building_63k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62589.04; date_signed 2012-04-23.",
)

# === Cycle 1072 (seed 20262072) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "osc_mexico_hvac_replacement_57k_2017",
    "energy", "power_plants_grid", "us",
    "OSC Solutions — Mexico HVAC replacement units",
    "Mexico",
    "5 Jul 2017: Department of the Air Force awards contract FA521517P8019 to OSC Solutions Inc for HVAC replacement units (PoP Mexico); obligated USD 57,428. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "57428", "2017-07-05", "2017", "", "",
    "HVAC replacement units, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_osc_mexico_hvac_replacement_57k_2017",
    "HVAC REPLACEMENT UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA521517P8019_9700_-NONE-_-NONE-/",
    "Actor: OSC Solutions Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1072",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA521517P8019_9700_-NONE-_-NONE- (OSC Mexico HVAC). Signed 2017-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA521517P8019_9700_-NONE-_-NONE-/.",
    "USASpending: OSC Mexico HVAC USD 0.057m. Supports osc_mexico_hvac_replacement_57k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57428; date_signed 2017-07-05.",
)

row_doc(
    "applied_security_mexico_tss_install_57k_2022",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico technical security installation",
    "Mexico",
    "17 Mar 2022: Department of State awards order 19AQMM22F1283 to Applied Security Technologies Inc for technical security installation service (PoP Mexico); obligated USD 57,336. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "57336", "2022-03-17", "2022", "", "",
    "Technical security installation service, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_mexico_tss_install_57k_2022",
    "TECHNICAL   SECURITY INSTALLATION SERVICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1283_1900_19AQMM19D0002_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1072",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F1283_1900_19AQMM19D0002_1900 (Applied Security Mexico TSS install). Signed 2022-03-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1283_1900_19AQMM19D0002_1900/.",
    "USASpending: Applied Security Mexico TSS install USD 0.057m. Supports applied_security_mexico_tss_install_57k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57336; date_signed 2022-03-17.",
)

row_doc(
    "tecniservicios_costa_rica_lagos_patio_62k_2024",
    "infrastructure", "building_materials", "other",
    "Tecniservicios FBV — Costa Rica Lagos migration police indoor patio reinforcement",
    "Costa Rica",
    "10 Jun 2024: Department of State awards contract 19CS8024P0820 to Tecniservicios FBV SRL for indoor patio reinforcement for migration police Lagos (PoP Costa Rica); obligated USD 62,342.01. CapEx face = award obligation. Exact Lagos site unnamed — lat/lon blank.",
    "62342.01", "2024-06-10", "2024", "", "",
    "Indoor patio reinforcement for migration police Lagos, Costa Rica (USASpending description; Lagos named, site coords not stated — lat/lon blank).",
    "usaspending_tecniservicios_costa_rica_lagos_patio_62k_2024",
    "INL 1930.0 INDOOR PATIO REINFORCEMENT MIGRATION POLICE LAGOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P0820_1900_-NONE-_-NONE-/",
    "Actor: Tecniservicios FBV SRL (Costa Rica) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1072",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8024P0820_1900_-NONE-_-NONE- (Tecniservicios Lagos patio). Signed 2024-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P0820_1900_-NONE-_-NONE-/.",
    "USASpending: Tecniservicios Lagos patio USD 0.062m. Supports tecniservicios_costa_rica_lagos_patio_62k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62342.01; date_signed 2024-06-10.",
)

row_doc(
    "misc_dr_2demarzo_dormitories_62k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic 2 de Marzo military academy dormitories",
    "Dominican Republic",
    "27 Apr 2011: Department of State awards contract SDR86011M0785 for construction dormitories for 2 de Marzo military academy (PoP Dominican Republic); obligated USD 62,282.19. CapEx face = award obligation. Exact academy site unnamed — lat/lon blank.",
    "62282.19", "2011-04-27", "2011", "", "",
    "Construction dormitories for 2 de Marzo military academy, Dominican Republic (USASpending description; academy named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dr_2demarzo_dormitories_62k_2011",
    "NAS-MI-CONSTRUCTION DORMITORIES FOR 2 DE MARZO MILITARY ACADEMY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M0785_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1072",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86011M0785_1900_-NONE-_-NONE- (DR 2 de Marzo dorms). Signed 2011-04-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M0785_1900_-NONE-_-NONE-/.",
    "USASpending: DR 2 de Marzo dorms USD 0.062m. Supports misc_dr_2demarzo_dormitories_62k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62282.19; date_signed 2011-04-27.",
)

row_doc(
    "misc_haiti_water_well_61k_2010",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Haiti water well construction",
    "Haiti",
    "24 Apr 2010: Department of Defense awards contract W912CL10C0016 for water well construction (PoP Haiti); obligated USD 61,276.50. CapEx face = award obligation. Exact well site unnamed — lat/lon blank.",
    "61276.50", "2010-04-24", "2010", "", "",
    "Water well construction, Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_haiti_water_well_61k_2010",
    "WATER WELL CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0016_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water. Holdover closed.",
    "hunt_cycle1072",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0016_9700_-NONE-_-NONE- (Haiti water well). Signed 2010-04-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0016_9700_-NONE-_-NONE-/.",
    "USASpending: Haiti water well USD 0.061m. Supports misc_haiti_water_well_61k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61276.50; date_signed 2010-04-24.",
)

# === Cycle 1073 (seed 20262073) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hmt_peru_chancery_roof_fans_58k_2014",
    "infrastructure", "building_materials", "us",
    "H.M.T. Services — Peru chancery roof utility fans",
    "Peru",
    "2 May 2014: Department of State awards contract SPE50014M0867 to H.M.T. Services Corporation for utility fans for chancery roof (PoP Peru); obligated USD 57,671.50. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "57671.50", "2014-05-02", "2014", "", "",
    "Utility fans for chancery roof, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_hmt_peru_chancery_roof_fans_58k_2014",
    "UTILITY FANS FOR CHANCERY ROOF IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0867_1900_-NONE-_-NONE-/",
    "Actor: H.M.T. Services Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1073",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014M0867_1900_-NONE-_-NONE- (HMT Peru chancery roof fans). Signed 2014-05-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0867_1900_-NONE-_-NONE-/.",
    "USASpending: HMT Peru chancery roof fans USD 0.058m. Supports hmt_peru_chancery_roof_fans_58k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57671.50; date_signed 2014-05-02.",
)

row_doc(
    "brown_campbell_panama_gamboa_dock_grating_57k_2020",
    "infrastructure", "port_ownership", "us",
    "Brown-Campbell — Panama Gamboa dock grating replacement",
    "Panama",
    "19 Mar 2020: Smithsonian Tropical Research Institute awards purchase order 33312920P00442447 to Brown-Campbell Co for Gamboa dock grating replacement (PoP Panama); obligated USD 57,444.53. CapEx face = award obligation. Exact dock coords not stated — lat/lon blank.",
    "57444.53", "2020-03-19", "2020", "", "",
    "Gamboa dock grating replacement, Panama (USASpending description; Gamboa dock named, coords not stated — lat/lon blank).",
    "usaspending_brown_campbell_panama_gamboa_dock_grating_57k_2020",
    "GAMBOA DOCK GRATING REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312920P00442447_3300_-NONE-_-NONE-/",
    "Actor: Brown-Campbell Co (U.S.) — us. Official USASpending Award API. Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1073",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33312920P00442447_3300_-NONE-_-NONE- (Brown-Campbell Gamboa dock grating). Signed 2020-03-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312920P00442447_3300_-NONE-_-NONE-/.",
    "USASpending: Brown-Campbell Gamboa dock grating USD 0.057m. Supports brown_campbell_panama_gamboa_dock_grating_57k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57444.53; date_signed 2020-03-19.",
)

row_doc(
    "egarco_ecuador_msgq_cabinets_61k_2022",
    "infrastructure", "building_materials", "other",
    "Egarco Egas Arguello — Ecuador MSGQ cabinet replacement",
    "Ecuador",
    "25 Apr 2022: Department of State awards contract 19EC7522C0006 to Egarco Egas Arguello Cia Ltda for MSGQ cabinet replacement (PoP Ecuador); obligated USD 61,234.67. CapEx face = award obligation. Exact MSGQ site unnamed — lat/lon blank.",
    "61234.67", "2022-04-25", "2022", "", "",
    "MSGQ cabinet replacement, Ecuador (USASpending description; MSGQ named, site coords not stated — lat/lon blank).",
    "usaspending_egarco_ecuador_msgq_cabinets_61k_2022",
    "PR10554949-FAC-7903RSTR-MSGQ-FWP273-CABINET REPLACEMENT MSGQ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0006_1900_-NONE-_-NONE-/",
    "Actor: Egarco Egas Arguello Cia Ltda (Ecuador) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1073",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0006_1900_-NONE-_-NONE- (Egarco Ecuador MSGQ cabinets). Signed 2022-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0006_1900_-NONE-_-NONE-/.",
    "USASpending: Egarco Ecuador MSGQ cabinets USD 0.061m. Supports egarco_ecuador_msgq_cabinets_61k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61234.67; date_signed 2022-04-25.",
)

row_doc(
    "misc_mexico_safety_metal_doors_61k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico safety metal doors",
    "Mexico",
    "29 May 2024: Department of State awards contract 19MX7224P0180 for safety metal doors (PoP Mexico); obligated USD 61,152.14. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "61152.14", "2024-05-29", "2024", "", "",
    "Safety metal doors, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_safety_metal_doors_61k_2024",
    "SAFETY METAL DOORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX7224P0180_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1073",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX7224P0180_1900_-NONE-_-NONE- (Mexico safety metal doors). Signed 2024-05-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX7224P0180_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico safety metal doors USD 0.061m. Supports misc_mexico_safety_metal_doors_61k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61152.14; date_signed 2024-05-29.",
)

row_doc(
    "ibarra_el_salvador_windows_doors_62k_2018",
    "infrastructure", "building_materials", "other",
    "Ibarra Merino Constructores — El Salvador BTH windows, lintels and doors",
    "El Salvador",
    "11 May 2018: Department of Defense awards contract W912QM18P0040 to Ibarra Merino Constructores S A de C V for windows, lintels and doors in support of BTH El Salvador 18 exercise (PoP El Salvador); obligated USD 61,815.08. CapEx face = award obligation. Exact BTH site unnamed — lat/lon blank.",
    "61815.08", "2018-05-11", "2018", "", "",
    "Windows, lintels and doors for BTH El Salvador 18 exercise (USASpending description; BTH named, site coords not stated — lat/lon blank).",
    "usaspending_ibarra_el_salvador_windows_doors_62k_2018",
    "WINDOWS, LINTELS AND DOORS IN SUPPORT OF BTH EL SALVADOR 18 EXERCISE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM18P0040_9700_-NONE-_-NONE-/",
    "Actor: Ibarra Merino Constructores S A de C V (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1073",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM18P0040_9700_-NONE-_-NONE- (Ibarra El Salvador windows/doors). Signed 2018-05-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM18P0040_9700_-NONE-_-NONE-/.",
    "USASpending: Ibarra El Salvador windows/doors USD 0.062m. Supports ibarra_el_salvador_windows_doors_62k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61815.08; date_signed 2018-05-11.",
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
