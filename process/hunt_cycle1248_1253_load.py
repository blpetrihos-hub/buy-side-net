#!/usr/bin/env python3
"""Cycles 1248–1253: USASpending LatAm CapEx (US vendor stock + residual other).

Seeds: 20262248–20262253. Thin top-up dry.
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

# === Cycle 1248 ===
row_doc(
    "sea_pac_peru_cooling_towers_replacement_630k_2021",
    "energy", "power_plants_grid", "us",
    "SEA PAC Engineering — Peru cooling towers replacement",
    "Peru",
    "29 Sep 2021: Department of State awards contract to SEA PAC ENGINEERING INC for cooling towers replacement (PoP Peru); obligated USD 630000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "630000", "2021-09-29", "2021", "", "",
    "COOLING TOWERS REPLACEMENT, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_sea_pac_peru_cooling_towers_replacement_630k_2021",
    "COOLING TOWERS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0063_1900_-NONE-_-NONE-/",
    "Actor: SEA PAC ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1248",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0063_1900_-NONE-_-NONE- (sea_pac_peru_cooling_towers_replacement_630k_2021). Signed 2021-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0063_1900_-NONE-_-NONE-/.",
    "USASpending: sea_pac_peru_cooling_towers_replacement_630k_2021 USD 0.630m. Supports sea_pac_peru_cooling_towers_replacement_630k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 630000.0; date_signed 2021-09-29.",
)

# === Cycle 1248 ===
row_doc(
    "greenway_colombia_chiller_replacement_614k_2016",
    "energy", "power_plants_grid", "us",
    "Greenway Enterprises — Colombia chiller replacement",
    "Colombia",
    "27 Sep 2016: Department of State awards task order to GREENWAY ENTERPRISES INC for chiller replacement (PoP Colombia); obligated USD 613686.82. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "613686.82", "2016-09-27", "2016", "", "",
    "CHILLER REPLACEMENT  IGF::CT::IGF, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_greenway_colombia_chiller_replacement_614k_2016",
    "CHILLER REPLACEMENT  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5204_1900_SAQMMA14D0050_1900/",
    "Actor: GREENWAY ENTERPRISES INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1248",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F5204_1900_SAQMMA14D0050_1900 (greenway_colombia_chiller_replacement_614k_2016). Signed 2016-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5204_1900_SAQMMA14D0050_1900/.",
    "USASpending: greenway_colombia_chiller_replacement_614k_2016 USD 0.614m. Supports greenway_colombia_chiller_replacement_614k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 613686.82; date_signed 2016-09-27.",
)

# === Cycle 1248 ===
row_doc(
    "misc_peru_annex_chillers_replacement_246k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru annex chillers replacement",
    "Peru",
    "30 Sep 2018: Department of State awards contract for annex chillers replacement (PoP Peru); obligated USD 246480.21. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "246480.21", "2018-09-30", "2018", "", "",
    "ANNEX CHILLERS REPLACEMENT, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_annex_chillers_replacement_246k_2018",
    "ANNEX CHILLERS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0030_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1248",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5018C0030_1900_-NONE-_-NONE- (misc_peru_annex_chillers_replacement_246k_2018). Signed 2018-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0030_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_annex_chillers_replacement_246k_2018 USD 0.246m. Supports misc_peru_annex_chillers_replacement_246k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 246480.21; date_signed 2018-09-30.",
)

# === Cycle 1248 ===
row_doc(
    "misc_peru_lima_cooling_tower_replacement_226k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru Lima cooling tower replacement project",
    "Peru",
    "13 Aug 2016: Department of State awards contract for Lima cooling tower replacement project (PoP Peru); obligated USD 225551.16. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "225551.16", "2016-08-13", "2016", "", "",
    "IGF::CL::IGF LIMA COOLING TOWER REPALCEMENT PROJECT - CONTRACT, Peru (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_peru_lima_cooling_tower_replacement_226k_2016",
    "IGF::CL::IGF LIMA COOLING TOWER REPALCEMENT PROJECT - CONTRACT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0027_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1248",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0027_1900_-NONE-_-NONE- (misc_peru_lima_cooling_tower_replacement_226k_2016). Signed 2016-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0027_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_lima_cooling_tower_replacement_226k_2016 USD 0.226m. Supports misc_peru_lima_cooling_tower_replacement_226k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 225551.16; date_signed 2016-08-13.",
)

# === Cycle 1248 ===
row_doc(
    "misc_dominican_make_ready_ac_equip_206k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic program make-ready AC equipment",
    "Dominican Republic",
    "27 Sep 2012: Department of State awards contract for program make-ready AC equipment (PoP Dominican Republic); obligated USD 205530.75. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "205530.75", "2012-09-27", "2012", "", "",
    "PROGRAM - MKE.RDY. AC EQUIP., Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_ac_equip_206k_2012",
    "PROGRAM - MKE.RDY. AC EQUIP.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M1968_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1248",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86012M1968_1900_-NONE-_-NONE- (misc_dominican_make_ready_ac_equip_206k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M1968_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_ac_equip_206k_2012 USD 0.206m. Supports misc_dominican_make_ready_ac_equip_206k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205530.75; date_signed 2012-09-27.",
)

# === Cycle 1249 ===
row_doc(
    "fluid_solutions_mexico_tijuana_fire_alarm_199k_2026",
    "infrastructure", "building_materials", "us",
    "Fluid Solutions — Mexico Tijuana fire alarm replacement project",
    "Mexico",
    "29 Aug 2026: Department of State awards task order to FLUID SOLUTIONS LLC for Tijuana fire alarm replacement project (PoP Mexico); obligated USD 199417.61. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "199417.61", "2026-08-29", "2026", "", "",
    "TIJUANA FIRE ALARM REPLACEMENT PROJECT: FLUID SOLUTIONS - WINNING CONTRACTOR WILL PROVIDE 2 TECHN..., Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_fluid_solutions_mexico_tijuana_fire_alarm_199k_2026",
    "TIJUANA FIRE ALARM REPLACEMENT PROJECT: FLUID SOLUTIONS - WINNING CONTRACTOR WILL PROVIDE 2 TECHNICIANS TO REPLACE AND INSTALL FIRE ALARM DEVICES THROUGHOUT COMPOUND UNDER THE DIRECTION OF ON SITE OBO FIRE FIRE ALARM TECHNICIAN - APPROX 6 WEEK PROJEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F1293_1900_19AQMM23D0032_1900/",
    "Actor: FLUID SOLUTIONS LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1249",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM26F1293_1900_19AQMM23D0032_1900 (fluid_solutions_mexico_tijuana_fire_alarm_199k_2026). Signed 2026-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F1293_1900_19AQMM23D0032_1900/.",
    "USASpending: fluid_solutions_mexico_tijuana_fire_alarm_199k_2026 USD 0.199m. Supports fluid_solutions_mexico_tijuana_fire_alarm_199k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 199417.61; date_signed 2026-08-29.",
)

# === Cycle 1249 ===
row_doc(
    "fluid_solutions_brazil_fire_pump_replacement_192k_2022",
    "infrastructure", "water", "us",
    "Fluid Solutions — Brazil São Paulo fire pump replacement project",
    "Brazil",
    "8 Sep 2022: Department of State awards contract to FLUID SOLUTIONS LLC for SP/FAC/7901 fire pump replacement project (PoP Brazil); obligated USD 192298.78. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "192298.78", "2022-09-08", "2022", "", "",
    "SP / FAC / 7901 FIRE PUMP REPLACEMENT PROJECT, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_fluid_solutions_brazil_fire_pump_replacement_192k_2022",
    "SP / FAC / 7901 FIRE PUMP REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9322P0782_1900_-NONE-_-NONE-/",
    "Actor: FLUID SOLUTIONS LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1249",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9322P0782_1900_-NONE-_-NONE- (fluid_solutions_brazil_fire_pump_replacement_192k_2022). Signed 2022-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9322P0782_1900_-NONE-_-NONE-/.",
    "USASpending: fluid_solutions_brazil_fire_pump_replacement_192k_2022 USD 0.192m. Supports fluid_solutions_brazil_fire_pump_replacement_192k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 192298.78; date_signed 2022-09-08.",
)

# === Cycle 1249 ===
row_doc(
    "misc_bolivia_residential_ac_install_197k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bolivia air conditioners for residential use accessories and installation",
    "Bolivia",
    "26 Sep 2011: Department of State awards contract for air conditioners for residential use, accessories and installation (PoP Bolivia); obligated USD 197400. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "197400", "2011-09-26", "2011", "", "",
    "AIR CONDITIONERS FOR RESIDENTIAL USE, ACCESORIES AND INSTALLATION, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bolivia_residential_ac_install_197k_2011",
    "AIR CONDITIONERS FOR RESIDENTIAL USE, ACCESORIES AND INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40011M0912_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1249",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40011M0912_1900_-NONE-_-NONE- (misc_bolivia_residential_ac_install_197k_2011). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40011M0912_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_residential_ac_install_197k_2011 USD 0.197m. Supports misc_bolivia_residential_ac_install_197k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 197400.0; date_signed 2011-09-26.",
)

# === Cycle 1249 ===
row_doc(
    "misc_ecuador_bme_hvac_system_equipment_184k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador BME HVAC system equipment",
    "Ecuador",
    "15 Sep 2017: Department of State awards contract for BME HVAC system equipment (PoP Ecuador); obligated USD 183906.09. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "183906.09", "2017-09-15", "2017", "", "",
    "IGF::OT::IGF  1900.0_7904-BME HVAC SYSTEM EQUIPMENT, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_bme_hvac_system_equipment_184k_2017",
    "IGF::OT::IGF  1900.0_7904-BME HVAC SYSTEM EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75017C0005_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1249",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75017C0005_1900_-NONE-_-NONE- (misc_ecuador_bme_hvac_system_equipment_184k_2017). Signed 2017-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75017C0005_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_bme_hvac_system_equipment_184k_2017 USD 0.184m. Supports misc_ecuador_bme_hvac_system_equipment_184k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183906.09; date_signed 2017-09-15.",
)

# === Cycle 1249 ===
row_doc(
    "misc_mexico_generator_transport_install_173k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico NAS transportation/installation generator",
    "Mexico",
    "22 Oct 2012: Department of State awards contract for NAS-MI transportation/installation generator (PoP Mexico); obligated USD 172666.22. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "172666.22", "2012-10-22", "2012", "", "",
    "NAS-MI-IN23MX91-TRANSPORTATION/INSTALLATION GENERATOR, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_generator_transport_install_173k_2012",
    "NAS-MI-IN23MX91-TRANSPORTATION/INSTALLATION GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90013M0011_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1249",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX90013M0011_1900_-NONE-_-NONE- (misc_mexico_generator_transport_install_173k_2012). Signed 2012-10-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90013M0011_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_generator_transport_install_173k_2012 USD 0.173m. Supports misc_mexico_generator_transport_install_173k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 172666.22; date_signed 2012-10-22.",
)

# === Cycle 1250 ===
row_doc(
    "fluid_solutions_dominican_filtration_skid_92k_2022",
    "infrastructure", "water", "us",
    "Fluid Solutions — Dominican Republic filtration skid replacement in WTP at compound",
    "Dominican Republic",
    "29 Apr 2022: Department of State awards contract to FLUID SOLUTIONS LLC for OBO7901 filtration skid replacement in WTP at compound (PoP Dominican Republic); obligated USD 91959.58. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "91959.58", "2022-04-29", "2022", "", "",
    "OBO7901 - FILTRATION SKID REPLACEMENT IN WTP AT COMPOUND, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_fluid_solutions_dominican_filtration_skid_92k_2022",
    "OBO7901 - FILTRATION SKID REPLACEMENT IN WTP AT COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P0875_1900_-NONE-_-NONE-/",
    "Actor: FLUID SOLUTIONS LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1250",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622P0875_1900_-NONE-_-NONE- (fluid_solutions_dominican_filtration_skid_92k_2022). Signed 2022-04-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P0875_1900_-NONE-_-NONE-/.",
    "USASpending: fluid_solutions_dominican_filtration_skid_92k_2022 USD 0.092m. Supports fluid_solutions_dominican_filtration_skid_92k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 91959.58; date_signed 2022-04-29.",
)

# === Cycle 1250 ===
row_doc(
    "global_integration_el_salvador_air_conditioners_62k_2022",
    "energy", "power_plants_grid", "us",
    "Global Integration Systems — El Salvador air conditioners",
    "El Salvador",
    "23 May 2022: Department of State awards contract to GLOBAL INTEGRATION SYSTEMS CORP for air conditioners (PoP El Salvador); obligated USD 61510. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "61510", "2022-05-23", "2022", "", "",
    "AIR CONDITIONERS, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_global_integration_el_salvador_air_conditioners_62k_2022",
    "AIR CONDITIONERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0455_1900_-NONE-_-NONE-/",
    "Actor: GLOBAL INTEGRATION SYSTEMS CORP (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1250",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0455_1900_-NONE-_-NONE- (global_integration_el_salvador_air_conditioners_62k_2022). Signed 2022-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0455_1900_-NONE-_-NONE-/.",
    "USASpending: global_integration_el_salvador_air_conditioners_62k_2022 USD 0.062m. Supports global_integration_el_salvador_air_conditioners_62k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61510.0; date_signed 2022-05-23.",
)

# === Cycle 1250 ===
row_doc(
    "misc_guatemala_generators_incinerator_electrical_169k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala generators and electrical supplies for incinerator",
    "Guatemala",
    "18 Sep 2017: Department of State awards contract for generators and electrical supplies for incinerator (PoP Guatemala); obligated USD 169011.81. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "169011.81", "2017-09-18", "2017", "", "",
    "IGF::CL::IGF GENERATORS AND ELECTRICAL SUPPLIES FOR INCINERATOR, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_generators_incinerator_electrical_169k_2017",
    "IGF::CL::IGF GENERATORS AND ELECTRICAL SUPPLIES FOR INCINERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0887_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1250",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50017M0887_1900_-NONE-_-NONE- (misc_guatemala_generators_incinerator_electrical_169k_2017). Signed 2017-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0887_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_generators_incinerator_electrical_169k_2017 USD 0.169m. Supports misc_guatemala_generators_incinerator_electrical_169k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 169011.81; date_signed 2017-09-18.",
)

# === Cycle 1250 ===
row_doc(
    "misc_brazil_embassy_residences_ac_renovation_157k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil AC units for embassy residences renovation",
    "Brazil",
    "9 Sep 2011: Department of State awards contract for EOFY-11 prog AC units for embassy residences renovation (PoP Brazil); obligated USD 157345.83. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "157345.83", "2011-09-09", "2011", "", "",
    "EOFY-11 PROG- AC UNITS FOR EMBASSY RESIDENCES RENOVATION, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_embassy_residences_ac_renovation_157k_2011",
    "EOFY-11 PROG- AC UNITS FOR EMBASSY RESIDENCES RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011M1855_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1250",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25011M1855_1900_-NONE-_-NONE- (misc_brazil_embassy_residences_ac_renovation_157k_2011). Signed 2011-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011M1855_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_embassy_residences_ac_renovation_157k_2011 USD 0.157m. Supports misc_brazil_embassy_residences_ac_renovation_157k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 157345.83; date_signed 2011-09-09.",
)

# === Cycle 1250 ===
row_doc(
    "misc_dominican_residential_make_ready_ac_129k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic residential make-ready AC units",
    "Dominican Republic",
    "10 Sep 2015: Department of State awards contract for residential make-ready AC units (PoP Dominican Republic); obligated USD 129162. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "129162", "2015-09-10", "2015", "", "",
    "RSDNT'L MKE. RDY. AC UNITS IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_residential_make_ready_ac_129k_2015",
    "RSDNT'L MKE. RDY. AC UNITS IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1904_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1250",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M1904_1900_-NONE-_-NONE- (misc_dominican_residential_make_ready_ac_129k_2015). Signed 2015-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1904_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_residential_make_ready_ac_129k_2015 USD 0.129m. Supports misc_dominican_residential_make_ready_ac_129k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 129162.0; date_signed 2015-09-10.",
)

# === Cycle 1251 ===
row_doc(
    "global_integration_el_salvador_container_bathroom_30k_2022",
    "infrastructure", "building_materials", "us",
    "Global Integration Systems — El Salvador CSL container with bathroom",
    "El Salvador",
    "11 Aug 2022: Department of State awards contract to GLOBAL INTEGRATION SYSTEMS CORP for CSL RFQ container with bathroom (PoP El Salvador); obligated USD 29645. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "29645", "2022-08-11", "2022", "", "",
    "CSL - RFQ CONTAINER WITH BATHROOM, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_global_integration_el_salvador_container_bathroom_30k_2022",
    "CSL - RFQ CONTAINER WITH BATHROOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0738_1900_-NONE-_-NONE-/",
    "Actor: GLOBAL INTEGRATION SYSTEMS CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1251",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0738_1900_-NONE-_-NONE- (global_integration_el_salvador_container_bathroom_30k_2022). Signed 2022-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0738_1900_-NONE-_-NONE-/.",
    "USASpending: global_integration_el_salvador_container_bathroom_30k_2022 USD 0.030m. Supports global_integration_el_salvador_container_bathroom_30k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29645.0; date_signed 2022-08-11.",
)

# === Cycle 1251 ===
row_doc(
    "red_orange_mexico_portable_ac_fap_23k_2025",
    "energy", "power_plants_grid", "us",
    "Red Orange North America — Mexico GSO warehouse portable AC FAP",
    "Mexico",
    "19 May 2025: Department of State awards contract to RED ORANGE NORTH AMERICA INC. for MEX-GSO/property-warehouse portable AC FAP FY25 (PoP Mexico); obligated USD 23100. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "23100", "2025-05-19", "2025", "", "",
    "MEX-GSO/PROPERTY-WAREHOUSE/PORTABLE AC FAP-FY25, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_red_orange_mexico_portable_ac_fap_23k_2025",
    "MEX-GSO/PROPERTY-WAREHOUSE/PORTABLE AC FAP-FY25",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5325P0782_1900_-NONE-_-NONE-/",
    "Actor: RED ORANGE NORTH AMERICA INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1251",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5325P0782_1900_-NONE-_-NONE- (red_orange_mexico_portable_ac_fap_23k_2025). Signed 2025-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5325P0782_1900_-NONE-_-NONE-/.",
    "USASpending: red_orange_mexico_portable_ac_fap_23k_2025 USD 0.023m. Supports red_orange_mexico_portable_ac_fap_23k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 23100.0; date_signed 2025-05-19.",
)

# === Cycle 1251 ===
row_doc(
    "misc_dominican_new_ac_units_rodriguez_129k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic new AC units Res Rodriguez",
    "Dominican Republic",
    "26 Jul 2010: Department of State awards contract for new AC units Res Rodriguez (PoP Dominican Republic); obligated USD 129000. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "129000", "2010-07-26", "2010", "", "",
    "NEW AC UNITS RES RODRIGUEZ, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_new_ac_units_rodriguez_129k_2010",
    "NEW AC UNITS RES RODRIGUEZ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86010M0999M001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1251",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86010M0999M001_1900_-NONE-_-NONE- (misc_dominican_new_ac_units_rodriguez_129k_2010). Signed 2010-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86010M0999M001_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_new_ac_units_rodriguez_129k_2010 USD 0.129m. Supports misc_dominican_new_ac_units_rodriguez_129k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 129000.0; date_signed 2010-07-26.",
)

# === Cycle 1251 ===
row_doc(
    "misc_mexico_cdj_bathroom_tile_fixtures_121k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juárez replace bathroom tile and fixtures",
    "Mexico",
    "26 Aug 2015: Department of State awards contract for CDJ replace bathroom tile and fixtures gov prop 1001 (PoP Mexico); obligated USD 120504.78. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "120504.78", "2015-08-26", "2015", "", "",
    "7901-CDJ REPLACE BATHROOM TILE AND FIXTURES GOV PROP 1001 IGF::OT::IGF - FOR OTHER FUNCTIONS, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_bathroom_tile_fixtures_121k_2015",
    "7901-CDJ REPLACE BATHROOM TILE AND FIXTURES GOV PROP 1001 IGF::OT::IGF - FOR OTHER FUNCTIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11515M0433_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1251",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11515M0433_1900_-NONE-_-NONE- (misc_mexico_cdj_bathroom_tile_fixtures_121k_2015). Signed 2015-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11515M0433_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cdj_bathroom_tile_fixtures_121k_2015 USD 0.121m. Supports misc_mexico_cdj_bathroom_tile_fixtures_121k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 120504.78; date_signed 2015-08-26.",
)

# === Cycle 1251 ===
row_doc(
    "misc_brazil_public_bathrooms_refurbishment_116k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil refurbishment project for public bathrooms CA",
    "Brazil",
    "12 May 2014: Department of State awards contract for refurbishment project for the public bathrooms — CA (PoP Brazil); obligated USD 115822.11. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "115822.11", "2014-05-12", "2014", "", "",
    "REFURBISHMENT PROJECT FOR THE PUBLIC BATHROOMS - CA ''IGF::OT::IGF'', Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_public_bathrooms_refurbishment_116k_2014",
    "REFURBISHMENT PROJECT FOR THE PUBLIC BATHROOMS - CA ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93014C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1251",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93014C0007_1900_-NONE-_-NONE- (misc_brazil_public_bathrooms_refurbishment_116k_2014). Signed 2014-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93014C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_public_bathrooms_refurbishment_116k_2014 USD 0.116m. Supports misc_brazil_public_bathrooms_refurbishment_116k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 115822.11; date_signed 2014-05-12.",
)

# === Cycle 1252 ===
row_doc(
    "comfort_systems_mexico_chilled_water_pumps_15k_2012",
    "energy", "power_plants_grid", "us",
    "Comfort Systems USA Arkansas — Mexico provide and install 2 replacement chilled water pumps",
    "Mexico",
    "15 May 2012: Department of Health and Human Services awards contract to COMFORT SYSTEMS USA ARKANSAS, INC for provide and install 2 replacement chilled water pump motors (PoP Mexico); obligated USD 15418. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15418", "2012-05-15", "2012", "", "",
    "PROVIDE AND INSTALL 2 REPLACEMENT CHILLED WATER PUMP MOTORS AT BLDG. 53 COOLING TOWER., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_comfort_systems_mexico_chilled_water_pumps_15k_2012",
    "PROVIDE AND INSTALL 2 REPLACEMENT CHILLED WATER PUMP MOTORS AT BLDG. 53 COOLING TOWER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_HHSF223201210042A_7524_-NONE-_-NONE-/",
    "Actor: COMFORT SYSTEMS USA ARKANSAS (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1252",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_HHSF223201210042A_7524_-NONE-_-NONE- (comfort_systems_mexico_chilled_water_pumps_15k_2012). Signed 2012-05-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_HHSF223201210042A_7524_-NONE-_-NONE-/.",
    "USASpending: comfort_systems_mexico_chilled_water_pumps_15k_2012 USD 0.015m. Supports comfort_systems_mexico_chilled_water_pumps_15k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15418.0; date_signed 2012-05-15.",
)

# === Cycle 1252 ===
row_doc(
    "mcs_tampa_colombia_cctv_arms_room_15k_2012",
    "infrastructure", "building_materials", "us",
    "MCS of Tampa — Colombia CCTV for arms room",
    "Colombia",
    "23 Jan 2012: Department of State awards contract to MCS OF TAMPA, INC. for INTERD (D) CCTV for arms room (PoP Colombia); obligated USD 15014.16. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15014.16", "2012-01-23", "2012", "", "",
    "INTERD (D) CCTV FOR ARMS ROOM, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_mcs_tampa_colombia_cctv_arms_room_15k_2012",
    "INTERD (D) CCTV FOR ARMS ROOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M0550_1900_-NONE-_-NONE-/",
    "Actor: MCS OF TAMPA (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1252",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012M0550_1900_-NONE-_-NONE- (mcs_tampa_colombia_cctv_arms_room_15k_2012). Signed 2012-01-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M0550_1900_-NONE-_-NONE-/.",
    "USASpending: mcs_tampa_colombia_cctv_arms_room_15k_2012 USD 0.015m. Supports mcs_tampa_colombia_cctv_arms_room_15k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15014.16; date_signed 2012-01-23.",
)

# === Cycle 1252 ===
row_doc(
    "misc_colombia_containers_offices_bathrooms_89k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia 20ft containers for offices and bathrooms",
    "Colombia",
    "23 Feb 2012: Department of State awards contract for INTERD (J) 20ft containers for offices and bathrooms (PoP Colombia); obligated USD 89119.05. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "89119.05", "2012-02-23", "2012", "", "",
    "INTERD (J). 20FT CONTAINERS FOR OFFICES AND BATHROOMS., Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_colombia_containers_offices_bathrooms_89k_2012",
    "INTERD (J). 20FT CONTAINERS FOR OFFICES AND BATHROOMS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M0727_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1252",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012M0727_1900_-NONE-_-NONE- (misc_colombia_containers_offices_bathrooms_89k_2012). Signed 2012-02-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M0727_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_containers_offices_bathrooms_89k_2012 USD 0.089m. Supports misc_colombia_containers_offices_bathrooms_89k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89119.05; date_signed 2012-02-23.",
)

# === Cycle 1252 ===
row_doc(
    "misc_guatemala_barracks_bathrooms_76k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala barracks 1,2 and bathrooms",
    "Guatemala",
    "5 Feb 2016: Department of Defense awards contract for barracks 1,2 and bathrooms (PoP Guatemala); obligated USD 75581.53. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "75581.53", "2016-02-05", "2016", "", "",
    "IGF::CL::IGF BARRACKS 1,2 AND BATHROOMS, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_barracks_bathrooms_76k_2016",
    "IGF::CL::IGF BARRACKS 1,2 AND BATHROOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM16C0002_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1252",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM16C0002_9700_-NONE-_-NONE- (misc_guatemala_barracks_bathrooms_76k_2016). Signed 2016-02-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM16C0002_9700_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_barracks_bathrooms_76k_2016 USD 0.076m. Supports misc_guatemala_barracks_bathrooms_76k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 75581.53; date_signed 2016-02-05.",
)

# === Cycle 1252 ===
row_doc(
    "misc_uruguay_family_residences_cctv_71k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Uruguay RSO CCTV project for family residences",
    "Uruguay",
    "20 Sep 2021: Department of State awards contract for RSO CCTV project for family residences (PoP Uruguay); obligated USD 71370. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "71370", "2021-09-20", "2021", "", "",
    "RSO - CCTV PROJECT FOR FAMILY RESIDENCES, Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_uruguay_family_residences_cctv_71k_2021",
    "RSO - CCTV PROJECT FOR FAMILY RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6021P0747_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1252",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6021P0747_1900_-NONE-_-NONE- (misc_uruguay_family_residences_cctv_71k_2021). Signed 2021-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6021P0747_1900_-NONE-_-NONE-/.",
    "USASpending: misc_uruguay_family_residences_cctv_71k_2021 USD 0.071m. Supports misc_uruguay_family_residences_cctv_71k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71370.0; date_signed 2021-09-20.",
)

# === Cycle 1253 ===
row_doc(
    "mcs_tampa_colombia_cctv_bodyscan_13k_2011",
    "infrastructure", "building_materials", "us",
    "MCS of Tampa — Colombia port security CCTV for bodyscan rooms",
    "Colombia",
    "14 Jan 2011: Department of State awards contract to MCS OF TAMPA, INC. for port sec prog CCTV for bodyscan rooms (PoP Colombia); obligated USD 13029.36. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13029.36", "2011-01-14", "2011", "", "",
    "PORT SEC PROG. CCTV FOR BODYSCAN ROOMS, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_mcs_tampa_colombia_cctv_bodyscan_13k_2011",
    "PORT SEC PROG. CCTV FOR BODYSCAN ROOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M0441_1900_-NONE-_-NONE-/",
    "Actor: MCS OF TAMPA (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1253",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15011M0441_1900_-NONE-_-NONE- (mcs_tampa_colombia_cctv_bodyscan_13k_2011). Signed 2011-01-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M0441_1900_-NONE-_-NONE-/.",
    "USASpending: mcs_tampa_colombia_cctv_bodyscan_13k_2011 USD 0.013m. Supports mcs_tampa_colombia_cctv_bodyscan_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13029.36; date_signed 2011-01-14.",
)

# === Cycle 1253 ===
row_doc(
    "ssi_belize_vsd_replacement_13k_2011",
    "energy", "power_plants_grid", "us",
    "Supplies & Services International — Belize FM replacement of variable speed drive",
    "Belize",
    "15 Sep 2011: Department of State awards contract to SUPPLIES & SERVICES INTERNATIONAL INC for FM replacement of variable speed drive (PoP Belize); obligated USD 13420. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13420", "2011-09-15", "2011", "", "",
    "FM- REPLACEMENT OF VARIABLE SPEED DRIVE, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_ssi_belize_vsd_replacement_13k_2011",
    "FM- REPLACEMENT OF VARIABLE SPEED DRIVE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20011M0209_1900_-NONE-_-NONE-/",
    "Actor: SUPPLIES & SERVICES INTERNATIONAL INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1253",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20011M0209_1900_-NONE-_-NONE- (ssi_belize_vsd_replacement_13k_2011). Signed 2011-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20011M0209_1900_-NONE-_-NONE-/.",
    "USASpending: ssi_belize_vsd_replacement_13k_2011 USD 0.013m. Supports ssi_belize_vsd_replacement_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13420.0; date_signed 2011-09-15.",
)

# === Cycle 1253 ===
row_doc(
    "misc_honduras_milgp_cctv_security_upgrade_69k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras MILGP new CCTV system and security upgrade",
    "Honduras",
    "7 Aug 2012: Department of State awards contract for MILGP 2122.1 new CCTV system and security upgrade (PoP Honduras); obligated USD 68837.29. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "68837.29", "2012-08-07", "2012", "", "",
    "MILGP 2122.1 - NEW CCTV SYSTEM AND SECURITY UPGRADE, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_milgp_cctv_security_upgrade_69k_2012",
    "MILGP 2122.1 - NEW CCTV SYSTEM AND SECURITY UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012M0597_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1253",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80012M0597_1900_-NONE-_-NONE- (misc_honduras_milgp_cctv_security_upgrade_69k_2012). Signed 2012-08-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012M0597_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_milgp_cctv_security_upgrade_69k_2012 USD 0.069m. Supports misc_honduras_milgp_cctv_security_upgrade_69k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68837.29; date_signed 2012-08-07.",
)

# === Cycle 1253 ===
row_doc(
    "misc_dominican_cctv_system_51k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic CCTV system",
    "Dominican Republic",
    "8 Apr 2022: Department of State awards contract for CCTV system (PoP Dominican Republic); obligated USD 51100.3. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "51100.3", "2022-04-08", "2022", "", "",
    "CCTV SYSTEM, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_cctv_system_51k_2022",
    "CCTV SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P0400_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1253",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622P0400_1900_-NONE-_-NONE- (misc_dominican_cctv_system_51k_2022). Signed 2022-04-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P0400_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_cctv_system_51k_2022 USD 0.051m. Supports misc_dominican_cctv_system_51k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51100.3; date_signed 2022-04-08.",
)

# === Cycle 1253 ===
row_doc(
    "misc_mexico_gdl_ncgr_alarm_cctv_49k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Guadalajara NCGR alarm and CCTV system FY26",
    "Mexico",
    "12 Aug 2026: Department of State awards contract for GDL-DS-RESSEC NCGR alarm and CCTV system FY26 (PoP Mexico); obligated USD 48509.86. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "48509.86", "2026-08-12", "2026", "", "",
    "GDL-DS-RESSEC - NCGR ALARM AND CCTV SYSTEM FY26, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_gdl_ncgr_alarm_cctv_49k_2026",
    "GDL-DS-RESSEC - NCGR ALARM AND CCTV SYSTEM FY26",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3026P0314_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1253",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX3026P0314_1900_-NONE-_-NONE- (misc_mexico_gdl_ncgr_alarm_cctv_49k_2026). Signed 2026-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3026P0314_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_gdl_ncgr_alarm_cctv_49k_2026 USD 0.049m. Supports misc_mexico_gdl_ncgr_alarm_cctv_49k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 48509.86; date_signed 2026-08-12.",
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
