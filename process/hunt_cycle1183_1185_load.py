#!/usr/bin/env python3
"""Cycles 1183–1185: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262183–20262185. Thin top-up dry.
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


# === Cycle 1183 (seed 20262183) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "johnson_controls_ecuador_bas_system_upgrade_replace_33k_2018",
    "energy", "power_plants_grid", "us",
    "Johnson Controls Building Automation Systems — Ecuador upgrade/replace BAS system",
    "Ecuador",
    "28 Aug 2018: Department of State awards contract 19EC3018P0563 to Johnson Controls Building Automation Systems, LLC for upgrade/replace BAS system (PoP Ecuador); obligated USD 33,437.78. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "33437.78", "2018-08-28", "2018", "", "",
    "Upgrade/replace BAS system, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_johnson_controls_ecuador_bas_system_upgrade_replace_33k_2018",
    "UPGRADE/REPLACE BAS SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3018P0563_1900_-NONE-_-NONE-/",
    "Actor: JOHNSON CONTROLS BUILDING AUTOMATION SYSTEMS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1183",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3018P0563_1900_-NONE-_-NONE- (johnson_controls_ecuador_bas_system_upgrade_replace_33k_2018). Signed 2018-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3018P0563_1900_-NONE-_-NONE-/.",
    "USASpending: johnson_controls_ecuador_bas_system_upgrade_replace_33k_2018 USD 0.033m. Supports johnson_controls_ecuador_bas_system_upgrade_replace_33k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 33437.78; date_signed 2018-08-28.",
)
row_doc(
    "york_international_barbados_nec_pcc_chiller_condenser_coils_33k_2014",
    "energy", "power_plants_grid", "us",
    "York International — Barbados NEC condenser coils for PCC chillers",
    "Barbados",
    "18 Sep 2014: Department of State awards contract SBB21014M0849 to York International Corporation for NEC condenser coils for PCC chillers (PoP Barbados); obligated USD 33,200.0. CapEx face = award obligation. NEC/PCC named; site coords not stated — lat/lon blank.",
    "33200", "2014-09-18", "2014", "", "",
    "Condenser coils for PCC chillers at NEC, Barbados (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_york_international_barbados_nec_pcc_chiller_condenser_coils_33k_2014",
    "NEC: CONDENSER COILS FOR PCC CHILLERS-NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21014M0849_1900_-NONE-_-NONE-/",
    "Actor: YORK INTERNATIONAL CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1183",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21014M0849_1900_-NONE-_-NONE- (york_international_barbados_nec_pcc_chiller_condenser_coils_33k_2014). Signed 2014-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21014M0849_1900_-NONE-_-NONE-/.",
    "USASpending: york_international_barbados_nec_pcc_chiller_condenser_coils_33k_2014 USD 0.033m. Supports york_international_barbados_nec_pcc_chiller_condenser_coils_33k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 33200.0; date_signed 2014-09-18.",
)
row_doc(
    "misc_mexico_usaid_electrical_generator_14k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico USAID OE electrical generator",
    "Mexico",
    "2 Feb 2011: Department of State awards contract SMX53011M0171 for USAID MEX OE electrical generator (PoP Mexico); obligated USD 14,196.82. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14196.82", "2011-02-02", "2011", "", "",
    "USAID OE electrical generator, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_usaid_electrical_generator_14k_2011",
    "USAID MEX OE-ELECTRICAL GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0171_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1183",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M0171_1900_-NONE-_-NONE- (misc_mexico_usaid_electrical_generator_14k_2011). Signed 2011-02-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0171_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_usaid_electrical_generator_14k_2011 USD 0.014m. Supports misc_mexico_usaid_electrical_generator_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14196.82; date_signed 2011-02-02.",
)
row_doc(
    "misc_colombia_facmilgp_new_ac_unit_install_14k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia install new AC unit for FACMILGP building",
    "Colombia",
    "23 Aug 2023: Department of State awards contract 19C02023P1630 for install new AC unit for FACMILGP building (PoP Colombia); obligated USD 14,192.7. CapEx face = award obligation. FACMILGP named; site coords not stated — lat/lon blank.",
    "14192.70", "2023-08-23", "2023", "", "",
    "Install new AC unit for FACMILGP building, Colombia (USASpending description; FACMILGP named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_facmilgp_new_ac_unit_install_14k_2023",
    "PR11937430 PROP ID X3010 INSTALL NEW AC UNIT FOR FACMILGP BLDG",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02023P1630_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1183",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02023P1630_1900_-NONE-_-NONE- (misc_colombia_facmilgp_new_ac_unit_install_14k_2023). Signed 2023-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02023P1630_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_facmilgp_new_ac_unit_install_14k_2023 USD 0.014m. Supports misc_colombia_facmilgp_new_ac_unit_install_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14192.7; date_signed 2023-08-23.",
)
row_doc(
    "misc_panama_bci_structured_cabling_14k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama structured cabling for BCI",
    "Panama",
    "14 Nov 2023: Department of State awards contract 33330524P00500597 for structured cabling for BCI (PoP Panama); obligated USD 14,190.7. CapEx face = award obligation. BCI named; site coords not stated — lat/lon blank.",
    "14190.70", "2023-11-14", "2023", "", "",
    "Structured cabling for BCI, Panama (USASpending description; BCI named, site coords not stated — lat/lon blank).",
    "usaspending_misc_panama_bci_structured_cabling_14k_2023",
    "STRUCTURED CABLING FOR BCI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330524P00500597_3300_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1183",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330524P00500597_3300_-NONE-_-NONE- (misc_panama_bci_structured_cabling_14k_2023). Signed 2023-11-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330524P00500597_3300_-NONE-_-NONE-/.",
    "USASpending: misc_panama_bci_structured_cabling_14k_2023 USD 0.014m. Supports misc_panama_bci_structured_cabling_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14190.7; date_signed 2023-11-14.",
)

# === Cycle 1184 (seed 20262184) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ross_technology_ecuador_metal_door_steel_15k_2020",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Ecuador metal door steel",
    "Ecuador",
    "6 Jan 2020: Department of State awards contract 19AQMM20P0227 to Ross Technology Company for metal door steel etc. (PoP Ecuador); obligated USD 14,515.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "14515", "2020-01-06", "2020", "", "",
    "Metal door steel etc., Ecuador (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_ross_technology_ecuador_metal_door_steel_15k_2020",
    "METAL DOOR STEEL ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0227_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1184",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0227_1900_-NONE-_-NONE- (ross_technology_ecuador_metal_door_steel_15k_2020). Signed 2020-01-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0227_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_ecuador_metal_door_steel_15k_2020 USD 0.015m. Supports ross_technology_ecuador_metal_door_steel_15k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14515.0; date_signed 2020-01-06.",
)
row_doc(
    "fabrication_designs_guyana_metal_door_screen_frame_14k_2024",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Guyana metal door screen frame for international embassies",
    "Guyana",
    "2 Aug 2024: Department of State awards contract 19AQMM24P0738 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Guyana); obligated USD 14,162.16. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "14162.16", "2024-08-02", "2024", "", "",
    "Metal door screen frame etc. for international embassies, Guyana (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_guyana_metal_door_screen_frame_14k_2024",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0738_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1184",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0738_1900_-NONE-_-NONE- (fabrication_designs_guyana_metal_door_screen_frame_14k_2024). Signed 2024-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0738_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_guyana_metal_door_screen_frame_14k_2024 USD 0.014m. Supports fabrication_designs_guyana_metal_door_screen_frame_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14162.16; date_signed 2024-08-02.",
)
row_doc(
    "misc_guatemala_inl_offices_air_conditioner_units_14k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala air conditioner units for INL Guatemala offices",
    "Guatemala",
    "25 Sep 2017: Department of State awards contract SGT50017V1445 for air conditioner units for INL Guatemala offices (PoP Guatemala); obligated USD 14,181.46. CapEx face = award obligation. INL offices named; site coords not stated — lat/lon blank.",
    "14181.46", "2017-09-25", "2017", "", "",
    "Air conditioner units for INL Guatemala offices (USASpending description; INL offices named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_inl_offices_air_conditioner_units_14k_2017",
    "INL-G PD&S - AIR CONDITIONER UNITS FOR INL GUATEMALA OFFICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017V1445_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1184",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50017V1445_1900_-NONE-_-NONE- (misc_guatemala_inl_offices_air_conditioner_units_14k_2017). Signed 2017-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017V1445_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_inl_offices_air_conditioner_units_14k_2017 USD 0.014m. Supports misc_guatemala_inl_offices_air_conditioner_units_14k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14181.46; date_signed 2017-09-25.",
)
row_doc(
    "misc_honduras_arso_generator_transfer_switch_14k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras ARSO generator and transfer switch",
    "Honduras",
    "16 Sep 2010: Department of State awards contract SHO80010M0478 for ARSO generator and transfer switch (PoP Honduras); obligated USD 14,160.16. CapEx face = award obligation. ARSO named; site coords not stated — lat/lon blank.",
    "14160.16", "2010-09-16", "2010", "", "",
    "ARSO generator and transfer switch, Honduras (USASpending description; ARSO named, site coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_arso_generator_transfer_switch_14k_2010",
    "PROP - ARSO GENERATOR AND TRANSFER SWITCH 1900.0",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80010M0478_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1184",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80010M0478_1900_-NONE-_-NONE- (misc_honduras_arso_generator_transfer_switch_14k_2010). Signed 2010-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80010M0478_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_arso_generator_transfer_switch_14k_2010 USD 0.014m. Supports misc_honduras_arso_generator_transfer_switch_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14160.16; date_signed 2010-09-16.",
)
row_doc(
    "misc_honduras_perimeter_wall_security_upgrade_14k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras perimeter wall security upgrade",
    "Honduras",
    "5 Nov 2021: Department of State awards contract 19H08022P0038 for perimeter wall security upgrade (PoP Honduras); obligated USD 14,150.71. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14150.71", "2021-11-05", "2021", "", "",
    "Perimeter wall security upgrade, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_perimeter_wall_security_upgrade_14k_2021",
    "URGENT! PERIMETER WALL SECURITY UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08022P0038_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1184",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08022P0038_1900_-NONE-_-NONE- (misc_honduras_perimeter_wall_security_upgrade_14k_2021). Signed 2021-11-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08022P0038_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_perimeter_wall_security_upgrade_14k_2021 USD 0.014m. Supports misc_honduras_perimeter_wall_security_upgrade_14k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14150.71; date_signed 2021-11-05.",
)

# === Cycle 1185 (seed 20262185) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fabrication_designs_chile_metal_door_screen_frame_14k_2024",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Chile metal door screen frame for international embassies",
    "Chile",
    "25 Nov 2024: Department of State awards contract 19AQMM25P0110 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Chile); obligated USD 13,716.55. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "13716.55", "2024-11-25", "2024", "", "",
    "Metal door screen frame etc. for international embassies, Chile (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_chile_metal_door_screen_frame_14k_2024",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0110_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1185",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0110_1900_-NONE-_-NONE- (fabrication_designs_chile_metal_door_screen_frame_14k_2024). Signed 2024-11-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0110_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_chile_metal_door_screen_frame_14k_2024 USD 0.014m. Supports fabrication_designs_chile_metal_door_screen_frame_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13716.55; date_signed 2024-11-25.",
)
row_doc(
    "hy_security_el_salvador_chancery_access_road_sliding_gate_drivers_13k_2016",
    "infrastructure", "building_materials", "us",
    "Hy-Security Gate — El Salvador sliding gate drivers for chancery access road",
    "El Salvador",
    "9 Feb 2016: Department of State awards contract SES60016M0345 to Hy-Security Gate, Inc. for sliding gate drivers for chancery access road (PoP El Salvador); obligated USD 12,754.0. CapEx face = award obligation. Chancery access road named; site coords not stated — lat/lon blank.",
    "12754", "2016-02-09", "2016", "", "",
    "Sliding gate drivers for chancery access road, El Salvador (USASpending description; chancery access road named, site coords not stated — lat/lon blank).",
    "usaspending_hy_security_el_salvador_chancery_access_road_sliding_gate_drivers_13k_2016",
    "7901- SLIDING GATE DRIVERS FOR CHANCERY ACCESS ROAD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M0345_1900_-NONE-_-NONE-/",
    "Actor: HY-SECURITY GATE, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1185",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60016M0345_1900_-NONE-_-NONE- (hy_security_el_salvador_chancery_access_road_sliding_gate_drivers_13k_2016). Signed 2016-02-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M0345_1900_-NONE-_-NONE-/.",
    "USASpending: hy_security_el_salvador_chancery_access_road_sliding_gate_drivers_13k_2016 USD 0.013m. Supports hy_security_el_salvador_chancery_access_road_sliding_gate_drivers_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12754.0; date_signed 2016-02-09.",
)
row_doc(
    "misc_dominican_republic_buildings_door_14k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic door for buildings",
    "Dominican Republic",
    "29 Mar 2017: Department of the Air Force awards contract FA470417P1004 for door for buildings in Dominican Republic (PoP Dominican Republic); obligated USD 14,120.66. CapEx face = award obligation. Exact buildings unnamed — lat/lon blank.",
    "14120.66", "2017-03-29", "2017", "", "",
    "Door for buildings, Dominican Republic (USASpending description; buildings unnamed — lat/lon blank).",
    "usaspending_misc_dominican_republic_buildings_door_14k_2017",
    "IGF::OT::IGF DOOR FOR BUILDINGS IN DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417P1004_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1185",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470417P1004_9700_-NONE-_-NONE- (misc_dominican_republic_buildings_door_14k_2017). Signed 2017-03-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417P1004_9700_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_buildings_door_14k_2017 USD 0.014m. Supports misc_dominican_republic_buildings_door_14k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14120.66; date_signed 2017-03-29.",
)
row_doc(
    "misc_peru_drug_rehab_structured_wiring_install_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru installation of structured wiring at drug rehab facility",
    "Peru",
    "8 Sep 2014: Department of State awards contract SPE50014M1485 for installation services of structured wiring at A A drug rehab (PoP Peru); obligated USD 14,115.69. CapEx face = award obligation. Drug rehab facility named; site coords not stated — lat/lon blank.",
    "14115.69", "2014-09-08", "2014", "", "",
    "Structured wiring installation at drug rehab facility, Peru (USASpending description; facility named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_drug_rehab_structured_wiring_install_14k_2014",
    "INSTALLATION SERVICES OF STRUCTURED WIRING @  A A DRUG REHAB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M1485_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1185",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014M1485_1900_-NONE-_-NONE- (misc_peru_drug_rehab_structured_wiring_install_14k_2014). Signed 2014-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M1485_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_drug_rehab_structured_wiring_install_14k_2014 USD 0.014m. Supports misc_peru_drug_rehab_structured_wiring_install_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14115.69; date_signed 2014-09-08.",
)
row_doc(
    "misc_brazil_mrv_ups_50_units_14k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil MRV UPS 50 units / no-breaks",
    "Brazil",
    "25 Jun 2015: Department of State awards contract SBR93015M0481 for MRV UPS 50 units/no-breaks (PoP Brazil); obligated USD 14,038.21. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14038.21", "2015-06-25", "2015", "", "",
    "MRV UPS 50 units, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_mrv_ups_50_units_14k_2015",
    "MRV- UPS (50 UN/NO BREAKS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93015M0481_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1185",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93015M0481_1900_-NONE-_-NONE- (misc_brazil_mrv_ups_50_units_14k_2015). Signed 2015-06-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93015M0481_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_mrv_ups_50_units_14k_2015 USD 0.014m. Supports misc_brazil_mrv_ups_50_units_14k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14038.21; date_signed 2015-06-25.",
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
