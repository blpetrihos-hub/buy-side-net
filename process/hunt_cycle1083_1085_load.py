#!/usr/bin/env python3
"""Cycles 1083–1085: USASpending LatAm CapEx residual (~USD0.048–0.060m).

Seeds: 20262083–20262085. Thin top-up dry.
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


# === Cycle 1083 (seed 20262083) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hdr_el_salvador_engineering_services_60k_2013",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — El Salvador engineering services",
    "El Salvador",
    "13 Sep 2013: Department of Defense awards task order CK05 under IDV W912P709D0001 to HDR Engineering, Inc. for engineering services (PoP El Salvador); obligated USD 60,138. CapEx face = award obligation. Exact project site unnamed — lat/lon blank.",
    "60138", "2013-09-13", "2013", "", "",
    "Engineering services, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_el_salvador_engineering_services_60k_2013",
    "ENGINEERING SERVICES  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_CK05_9700_W912P709D0001_9700/",
    "Actor: HDR Engineering, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1083",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_CK05_9700_W912P709D0001_9700 (HDR El Salvador engineering). Signed 2013-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_CK05_9700_W912P709D0001_9700/.",
    "USASpending: HDR El Salvador engineering USD 0.060m. Supports hdr_el_salvador_engineering_services_60k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60138; date_signed 2013-09-13.",
)

row_doc(
    "ace_roof_coatings_honduras_obx_51k_2014",
    "infrastructure", "building_materials", "us",
    "ACE Roof Coatings — Honduras OBX roof coating products",
    "Honduras",
    "17 Jan 2014: Department of State awards order SHO80014F0116 to ACE Roof Coatings, Inc. for purchase of roof coating products for OBX (PoP Honduras); obligated USD 51,092.95. CapEx face = award obligation. Exact OBX site unnamed — lat/lon blank.",
    "51092.95", "2014-01-17", "2014", "", "",
    "Roof coating products for OBX, Honduras (USASpending description; OBX named, site coords not stated — lat/lon blank).",
    "usaspending_ace_roof_coatings_honduras_obx_51k_2014",
    "PURCHASE OF ROOF COATING PRODUCTS FOR OBX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014F0116_1900_GS07F177AA_4732/",
    "Actor: ACE Roof Coatings, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1083",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80014F0116_1900_GS07F177AA_4732 (ACE Roof Coatings Honduras). Signed 2014-01-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014F0116_1900_GS07F177AA_4732/.",
    "USASpending: ACE Roof Coatings Honduras USD 0.051m. Supports ace_roof_coatings_honduras_obx_51k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51092.95; date_signed 2014-01-17.",
)

row_doc(
    "misc_guatemala_water_distribution_system_60k_2014",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Guatemala MLGP new water distribution system",
    "Guatemala",
    "30 Sep 2014: Department of State awards contract SGT50014C0008 for installation of a new water distribution system (PoP Guatemala); obligated USD 59,602.53. CapEx face = award obligation. Exact system alignment unnamed — lat/lon blank.",
    "59602.53", "2014-09-30", "2014", "", "",
    "Installation of a new water distribution system, Guatemala (USASpending description; alignment not named — lat/lon blank).",
    "usaspending_misc_guatemala_water_distribution_system_60k_2014",
    "IGF::CL::IGF GUATE-MLGP-INSTALLATION OF A NEW WATER DISTRIBUTION SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50014C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water. Holdover closed.",
    "hunt_cycle1083",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50014C0008_1900_-NONE-_-NONE- (Guatemala water distribution). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50014C0008_1900_-NONE-_-NONE-/.",
    "USASpending: Guatemala water distribution USD 0.060m. Supports misc_guatemala_water_distribution_system_60k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59602.53; date_signed 2014-09-30.",
)

row_doc(
    "misc_venezuela_consular_parking_awning_60k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela chancery consular/parking awning",
    "Venezuela",
    "29 Sep 2011: Department of State awards contract SVE30011M0901 for chancery consular/parking awning (PoP Venezuela); obligated USD 59,568.37. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "59568.37", "2011-09-29", "2011", "", "",
    "Chancery consular/parking awning, Venezuela (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_consular_parking_awning_60k_2011",
    "CHANCERY: CONSULAR/PARKING AWNING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0901_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed. Weight under-covered Venezuela.",
    "hunt_cycle1083",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30011M0901_1900_-NONE-_-NONE- (Venezuela consular parking awning). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0901_1900_-NONE-_-NONE-/.",
    "USASpending: Venezuela consular parking awning USD 0.060m. Supports misc_venezuela_consular_parking_awning_60k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59568.37; date_signed 2011-09-29.",
)

row_doc(
    "gutierrez_mexico_kitchen_renovation_59k_2021",
    "infrastructure", "building_materials", "other",
    "Norma Isabel Gutierrez Lopez — Mexico kitchen renovation FY21",
    "Mexico",
    "8 Feb 2021: Department of State awards order 19MX5321F0369 to Norma Isabel Gutierrez Lopez for kitchen renovation FY21 (PoP Mexico); obligated USD 59,497.96. CapEx face = award obligation. Exact kitchen site unnamed — lat/lon blank.",
    "59497.96", "2021-02-08", "2021", "", "",
    "Kitchen renovation FY21, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_gutierrez_mexico_kitchen_renovation_59k_2021",
    "MEX-FAC-KITCHEN RENOVATION-FY21",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321F0369_1900_19MX5319D0013_1900/",
    "Actor: Norma Isabel Gutierrez Lopez (Mexico) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1083",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5321F0369_1900_19MX5319D0013_1900 (Gutierrez Mexico kitchen renovation). Signed 2021-02-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321F0369_1900_19MX5319D0013_1900/.",
    "USASpending: Gutierrez Mexico kitchen renovation USD 0.059m. Supports gutierrez_mexico_kitchen_renovation_59k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59497.96; date_signed 2021-02-08.",
)

# === Cycle 1084 (seed 20262084) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "commercial_marketing_barbados_carpet_tiles_51k_2015",
    "infrastructure", "building_materials", "us",
    "Commercial Marketing Associates — Barbados embassy carpet tiles",
    "Barbados",
    "21 Sep 2015: Department of State awards contract SBB21015M1076 to Commercial Marketing Associates, Inc. for carpet tiles for embassy (PoP Barbados); obligated USD 51,207. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.",
    "51207", "2015-09-21", "2015", "", "",
    "Carpet tiles for embassy, Barbados (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_commercial_marketing_barbados_carpet_tiles_51k_2015",
    "PROGRAM: CARPET TILES FOR EMBASSY - PROPOSAL# 18947",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21015M1076_1900_-NONE-_-NONE-/",
    "Actor: Commercial Marketing Associates, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1084",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21015M1076_1900_-NONE-_-NONE- (Commercial Marketing Barbados carpet). Signed 2015-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21015M1076_1900_-NONE-_-NONE-/.",
    "USASpending: Commercial Marketing Barbados carpet USD 0.051m. Supports commercial_marketing_barbados_carpet_tiles_51k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51207; date_signed 2015-09-21.",
)

row_doc(
    "fluid_solutions_dr_fuel_tank_manholes_49k_2021",
    "infrastructure", "building_materials", "us",
    "Fluid Solutions — Dominican Republic compound fuel tanks manholes replacement",
    "Dominican Republic",
    "2 Sep 2021: Department of State awards contract 19DR8621P1316 to Fluid Solutions LLC for fuel tanks manholes replacement compound (PoP Dominican Republic); obligated USD 49,012.80. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "49012.80", "2021-09-02", "2021", "", "",
    "Fuel tanks manholes replacement at compound, Dominican Republic (USASpending description; compound not named — lat/lon blank).",
    "usaspending_fluid_solutions_dr_fuel_tank_manholes_49k_2021",
    "OBO7901 - FUEL TANKS MANHOLES REPLACEMENT COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8621P1316_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1084",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8621P1316_1900_-NONE-_-NONE- (Fluid Solutions DR fuel-tank manholes). Signed 2021-09-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8621P1316_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions DR fuel-tank manholes USD 0.049m. Supports fluid_solutions_dr_fuel_tank_manholes_49k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49012.80; date_signed 2021-09-02.",
)

row_doc(
    "misc_mexico_hermosillo_hvac_replacement_59k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico Hermosillo consulate general HVAC equipment replacement",
    "Mexico",
    "6 Aug 2013: Department of State awards contract SMX57013M0095 for HVAC equipment replacement at consulate general Hermosillo (PoP Mexico); obligated USD 59,347.82. CapEx face = award obligation. Exact consulate site unnamed — lat/lon blank.",
    "59347.82", "2013-08-06", "2013", "", "",
    "HVAC equipment replacement at consulate general Hermosillo, Mexico (USASpending description; Hermosillo named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_hermosillo_hvac_replacement_59k_2013",
    "OBO/HMO-HVAC EQUIPMENT REPLACEMENT AT CONGEN HERMOSILLO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX57013M0095_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1084",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX57013M0095_1900_-NONE-_-NONE- (Mexico Hermosillo HVAC). Signed 2013-08-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX57013M0095_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico Hermosillo HVAC USD 0.059m. Supports misc_mexico_hermosillo_hvac_replacement_59k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59347.82; date_signed 2013-08-06.",
)

row_doc(
    "misc_brazil_perimeter_fence_paint_59k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil painting of perimeter fence and gates",
    "Brazil",
    "22 Jul 2019: Department of State awards contract 19BR9319P0573 for painting of perimeter fence and gates (PoP Brazil); obligated USD 59,145.35. CapEx face = award obligation. Exact fence unnamed — lat/lon blank.",
    "59145.35", "2019-07-22", "2019", "", "",
    "Painting of perimeter fence and gates, Brazil (USASpending description; fence not named — lat/lon blank).",
    "usaspending_misc_brazil_perimeter_fence_paint_59k_2019",
    "PAINTING OF PERIMETER FENCE AND GATES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0573_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1084",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9319P0573_1900_-NONE-_-NONE- (Brazil perimeter fence paint). Signed 2019-07-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0573_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil perimeter fence paint USD 0.059m. Supports misc_brazil_perimeter_fence_paint_59k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59145.35; date_signed 2019-07-22.",
)

row_doc(
    "misc_peru_parking_lot_b_structural_roof_59k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru Lima parking lot B structural roof",
    "Peru",
    "29 Sep 2014: Department of State awards contract SPE50014C0020 for contract to build parking lot B structural roof (PoP Peru); obligated USD 58,891.44. CapEx face = award obligation. Exact lot unnamed — lat/lon blank.",
    "58891.44", "2014-09-29", "2014", "", "",
    "Build parking lot B structural roof, Lima, Peru (USASpending description; lot B named, coords not stated — lat/lon blank).",
    "usaspending_misc_peru_parking_lot_b_structural_roof_59k_2014",
    "LIMA- CONTRACT TO BUILD PARKING LOT B STRUCTURAL ROOF IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0020_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1084",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014C0020_1900_-NONE-_-NONE- (Peru parking lot B structural roof). Signed 2014-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0020_1900_-NONE-_-NONE-/.",
    "USASpending: Peru parking lot B structural roof USD 0.059m. Supports misc_peru_parking_lot_b_structural_roof_59k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58891.44; date_signed 2014-09-29.",
)

# === Cycle 1085 (seed 20262085) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "acoustiblok_el_salvador_sound_barrier_panels_48k_2012",
    "infrastructure", "building_materials", "us",
    "Acoustiblok — El Salvador outdoor sound barrier panels",
    "El Salvador",
    "28 Sep 2012: Department of State awards contract SES60012M1169 to Acoustiblok Inc for outdoor sound barrier panels (PoP El Salvador); obligated USD 48,370. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "48370", "2012-09-28", "2012", "", "",
    "Outdoor sound barrier panels, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_acoustiblok_el_salvador_sound_barrier_panels_48k_2012",
    "2120 FUNDS - SOUND BARRIER PANELS OUTDOOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60012M1169_1900_-NONE-_-NONE-/",
    "Actor: Acoustiblok Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1085",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60012M1169_1900_-NONE-_-NONE- (Acoustiblok El Salvador sound barriers). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60012M1169_1900_-NONE-_-NONE-/.",
    "USASpending: Acoustiblok El Salvador sound barriers USD 0.048m. Supports acoustiblok_el_salvador_sound_barrier_panels_48k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 48370; date_signed 2012-09-28.",
)

row_doc(
    "wje_chile_santiago_msg_seismic_model_48k_2018",
    "infrastructure", "engineering_epc", "us",
    "Wiss Janney Elstner — Chile Santiago MSG residence seismic model and IBC parameters",
    "Chile",
    "24 Sep 2018: Department of State awards order 19AQMM18F4441 to Wiss Janney Elstner Associates Inc to collect geologic source data, prepare seismic model, derive IBC MCE spectral response acceleration values and submit report supporting renovations to a Marine Security Guard residence planned for Santiago (PoP Chile); obligated USD 48,242.11. CapEx face = award obligation. Exact MSG site unnamed — lat/lon blank.",
    "48242.11", "2018-09-24", "2018", "", "",
    "Seismic model and IBC parameters for MSG residence renovations planned for Santiago, Chile (USASpending description; Santiago named, site coords not stated — lat/lon blank).",
    "usaspending_wje_chile_santiago_msg_seismic_model_48k_2018",
    "COLLECT GEOLOGIC SOURCE DATA, PREPARE SEISMIC MODEL, DERIVE IBC, MCE, SPECTRAL RESPONSE ACCELERATION VALUES AND PREPARE   SUBMIT REPORT.  THIS IS TO SUPPORT RENOVATIONS TO A MARINE SECURITY GUARD RESIDENCE PLANNED FOR SANTIAGO, CHILE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4441_1900_SAQMMA14D0021_1900/",
    "Actor: Wiss Janney Elstner Associates Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1085",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F4441_1900_SAQMMA14D0021_1900 (WJE Chile Santiago MSG seismic). Signed 2018-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4441_1900_SAQMMA14D0021_1900/.",
    "USASpending: WJE Chile Santiago MSG seismic USD 0.048m. Supports wje_chile_santiago_msg_seismic_model_48k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 48242.11; date_signed 2018-09-24.",
)

row_doc(
    "misc_brazil_cmr_perimeter_light_poles_59k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil CMR perimeter light poles installation",
    "Brazil",
    "9 Apr 2019: Department of State awards contract 19BR2519P0435 for CMR M&R perimeter light poles installation (PoP Brazil); obligated USD 59,127.29. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "59127.29", "2019-04-09", "2019", "", "",
    "CMR perimeter light poles installation, Brazil (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_cmr_perimeter_light_poles_59k_2019",
    "BSB-FAC - CMR M&R - PERIMETER LIGHT POLES INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0435_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1085",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P0435_1900_-NONE-_-NONE- (Brazil CMR perimeter light poles). Signed 2019-04-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0435_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil CMR perimeter light poles USD 0.059m. Supports misc_brazil_cmr_perimeter_light_poles_59k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59127.29; date_signed 2019-04-09.",
)

row_doc(
    "misc_haiti_cdc_delr_office_renovation_59k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti CDC DELR office renovation (CDC annex)",
    "Haiti",
    "15 Sep 2023: Department of State awards contract 19HA7023C0001 for CDC renovation of DELR office CDC annex (PoP Haiti); obligated USD 59,064.15. CapEx face = award obligation. Exact annex unnamed — lat/lon blank.",
    "59064.15", "2023-09-15", "2023", "", "",
    "CDC renovation of DELR office (CDC annex), Haiti (USASpending description; annex not named — lat/lon blank).",
    "usaspending_misc_haiti_cdc_delr_office_renovation_59k_2023",
    "PAP-7553.0- CDC RENOVATION OF DELR OFFICE (CDC ANNEX) A",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023C0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Weight under-covered Haiti.",
    "hunt_cycle1085",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023C0001_1900_-NONE-_-NONE- (Haiti CDC DELR renovation). Signed 2023-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Haiti CDC DELR renovation USD 0.059m. Supports misc_haiti_cdc_delr_office_renovation_59k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59064.15; date_signed 2023-09-15.",
)

row_doc(
    "misc_ecuador_compound_domestic_water_pump_59k_2020",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Ecuador compound domestic water pump replacement",
    "Ecuador",
    "15 Sep 2020: Department of State awards contract 19EC7520P1117 for compound domestic water pump replacement (PoP Ecuador); obligated USD 59,018.40. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "59018.40", "2020-09-15", "2020", "", "",
    "Compound domestic water pump replacement, Ecuador (USASpending description; compound not named — lat/lon blank).",
    "usaspending_misc_ecuador_compound_domestic_water_pump_59k_2020",
    "7901-PR9334624-COMPOUND DOMESTIC WATER PUMP - REPLACEME",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7520P1117_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1085",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7520P1117_1900_-NONE-_-NONE- (Ecuador compound domestic water pump). Signed 2020-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7520P1117_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador compound domestic water pump USD 0.059m. Supports misc_ecuador_compound_domestic_water_pump_59k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59018.40; date_signed 2020-09-15.",
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
