#!/usr/bin/env python3
"""Cycles 1047–1049: USASpending LatAm CapEx residual (~USD0.05–0.070m).

Seeds: 20262047–20262049. Thin top-up dry.
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


# === Cycle 1047 (seed 20262047) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "bmk_guyana_febr_doors_55k_2018",
    "infrastructure", "building_materials", "us",
    "BMK Construction — Guyana FEBR doors supply and install",
    "Guyana",
    "12 Sep 2018: Department of State awards contract 19GY2018C0002 to BMK Construction Services, Inc. for FAC supply and install FEBR doors (PoP Guyana); obligated USD 55,101.68. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "55101.68", "2018-09-12", "2018", "", "",
    "FEBR doors supply and install, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_bmk_guyana_febr_doors_55k_2018",
    "FAC: SUPPLY AND INSTALL FEBR DOORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2018C0002_1900_-NONE-_-NONE-/",
    "Actor: BMK Construction Services, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1047",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2018C0002_1900_-NONE-_-NONE- (BMK Guyana FEBR doors). Signed 2018-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2018C0002_1900_-NONE-_-NONE-/.",
    "USASpending: BMK Guyana FEBR doors USD 0.055m. Supports bmk_guyana_febr_doors_55k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55101.68; date_signed 2018-09-12.",
)

row_doc(
    "alban_guyana_residence_generators_55k_2014",
    "energy", "power_plants_grid", "us",
    "Alban Tractor — Guyana generator units for new residences",
    "Guyana",
    "18 Nov 2014: Department of State awards contract SGY20015M0033 to Alban Tractor, LLC for GSO generator units for new residences (PoP Guyana); obligated USD 55,000. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.",
    "55000", "2014-11-18", "2014", "", "",
    "Generator units for new residences, Guyana (USASpending description; residences not named — lat/lon blank).",
    "usaspending_alban_guyana_residence_generators_55k_2014",
    "GSO: GENERATOR UNITS FOR NEW RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0033_1900_-NONE-_-NONE-/",
    "Actor: Alban Tractor, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1047",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20015M0033_1900_-NONE-_-NONE- (Alban Guyana residence generators). Signed 2014-11-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0033_1900_-NONE-_-NONE-/.",
    "USASpending: Alban Guyana residence generators USD 0.055m. Supports alban_guyana_residence_generators_55k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55000; date_signed 2014-11-18.",
)

row_doc(
    "industrias_peru_sand_filter_fence_70k_2016",
    "resources", "water", "other",
    "Industrias Servicios Generales — Peru Lima sand filter fence replacement",
    "Peru",
    "31 Mar 2016: Department of State awards contract SPE50016C0008 to Industrias Servicios Generales E.I.R.L. for FAC replace sand filter fence (PoP Peru); obligated USD 69,863.16. CapEx face = award obligation.",
    "69863.16", "2016-03-31", "2016", "-12.092", "-77.049",
    "Sand filter fence replacement, Lima, Peru (USASpending description; Lima named).",
    "usaspending_industrias_peru_sand_filter_fence_70k_2016",
    "LIMA FY2106 FAC REPLACE SAND FILTER FENCE IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0008_1900_-NONE-_-NONE-/",
    "Actor: Industrias Servicios Generales E.I.R.L. (Peru) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1047",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0008_1900_-NONE-_-NONE- (Industrias Peru sand filter fence). Signed 2016-03-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0008_1900_-NONE-_-NONE-/.",
    "USASpending: Industrias Peru sand filter fence USD 0.070m. Supports industrias_peru_sand_filter_fence_70k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69863.16; date_signed 2016-03-31.",
)

row_doc(
    "misc_gtm_main_transformer_70k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala electric main transformer replacement",
    "Guatemala",
    "12 Sep 2017: Department of State awards contract SGT50017M0866 for electric main transformer replacement (PoP Guatemala); obligated USD 69,715.30. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "69715.30", "2017-09-12", "2017", "", "",
    "Electric main transformer replacement, Guatemala (USASpending PoP Guatemala; site not named — lat/lon blank).",
    "usaspending_misc_gtm_main_transformer_70k_2017",
    "IGF::CL::IGF ELECTRIC MAIN TRANSFORMER REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0866_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1047",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50017M0866_1900_-NONE-_-NONE- (Guatemala main transformer). Signed 2017-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0866_1900_-NONE-_-NONE-/.",
    "USASpending: Guatemala main transformer USD 0.070m. Supports misc_gtm_main_transformer_70k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69715.30; date_signed 2017-09-12.",
)

row_doc(
    "trazo_paraguay_grouting_69k_2026",
    "infrastructure", "building_materials", "other",
    "Trazo — Paraguay compound grouting repair",
    "Paraguay",
    "10 Sep 2026: Department of State awards contract 19PA1026C0009 to Trazo SRL for FAC grouting repair project — compound (PoP Paraguay); obligated USD 69,288.73. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "69288.73", "2026-09-10", "2026", "", "",
    "Grouting repair at compound, Paraguay (USASpending description; compound not named — lat/lon blank).",
    "usaspending_trazo_paraguay_grouting_69k_2026",
    "FAC - 7901XJZMRSTR - GROUTING REPAIR PROJECT - COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1026C0009_1900_-NONE-_-NONE-/",
    "Actor: Trazo SRL (Paraguay) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1047",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1026C0009_1900_-NONE-_-NONE- (Trazo Paraguay grouting). Signed 2026-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1026C0009_1900_-NONE-_-NONE-/.",
    "USASpending: Trazo Paraguay grouting USD 0.069m. Supports trazo_paraguay_grouting_69k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69288.73; date_signed 2026-09-10.",
)

# === Cycle 1048 (seed 20262048) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "boland_trane_barbados_meter_56k_2014",
    "energy", "power_plants_grid", "us",
    "Boland Trane — Barbados power quality meter install",
    "Barbados",
    "27 Sep 2014: Department of State awards order SAQMMA14F4379 to Boland Trane Services Inc for purchase and install power quality meter (MeterNet) (PoP Barbados); obligated USD 56,170. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "56170", "2014-09-27", "2014", "", "",
    "Power quality meter (MeterNet) purchase and install, Barbados (USASpending description; site not named — lat/lon blank).",
    "usaspending_boland_trane_barbados_meter_56k_2014",
    "PURCHASE AND INSTALL POWER QUALITY METER (METERNET) IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4379_1900_SAQMMA13D0169_1900/",
    "Actor: Boland Trane Services Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1048",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F4379_1900_SAQMMA13D0169_1900 (Boland Trane Barbados meter). Signed 2014-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4379_1900_SAQMMA13D0169_1900/.",
    "USASpending: Boland Trane Barbados meter USD 0.056m. Supports boland_trane_barbados_meter_56k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 56170; date_signed 2014-09-27.",
)

row_doc(
    "applied_security_ecuador_tss_49k_2011",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Ecuador TSS security installation",
    "Ecuador",
    "23 Nov 2011: Department of State awards order SAQMMA12F0148 to Applied Security Technologies Inc for TSS security installation (PoP Ecuador); obligated USD 48,967.77. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "48967.77", "2011-11-23", "2011", "", "",
    "TSS security installation, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_ecuador_tss_49k_2011",
    "TSS SECURITY INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0148_1900_SAQMMA07D0030_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1048",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F0148_1900_SAQMMA07D0030_1900 (Applied Security Ecuador TSS). Signed 2011-11-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0148_1900_SAQMMA07D0030_1900/.",
    "USASpending: Applied Security Ecuador TSS USD 0.049m. Supports applied_security_ecuador_tss_49k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 48967.77; date_signed 2011-11-23.",
)

row_doc(
    "misc_brazil_mezzanine_fan_coils_70k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil mezzanine fan coil replacement",
    "Brazil",
    "28 Sep 2023: Department of State awards contract 19BR8223P0520 for replace mezzanine fan coils (PoP Brazil); obligated USD 69,767.44. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "69767.44", "2023-09-28", "2023", "", "",
    "Mezzanine fan coil replacement, Brazil (USASpending PoP Brazil; site not named — lat/lon blank).",
    "usaspending_misc_brazil_mezzanine_fan_coils_70k_2023",
    "REPLACE MEZZANINE FAN COILS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8223P0520_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1048",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8223P0520_1900_-NONE-_-NONE- (Brazil mezzanine fan coils). Signed 2023-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8223P0520_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil mezzanine fan coils USD 0.070m. Supports misc_brazil_mezzanine_fan_coils_70k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69767.44; date_signed 2023-09-28.",
)

row_doc(
    "misc_peru_parking_asphalt_70k_2013",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Peru official parking lot asphalt repair",
    "Peru",
    "24 Sep 2013: Department of State awards contract SPE50013C0029 for official parking lot asphalt repair works (PoP Peru); obligated USD 69,652.12. CapEx face = award obligation. Exact lot unnamed — lat/lon blank.",
    "69652.12", "2013-09-24", "2013", "", "",
    "Official parking lot asphalt repair, Peru (USASpending description; lot not named — lat/lon blank).",
    "usaspending_misc_peru_parking_asphalt_70k_2013",
    "CONTRACT FOR OFFICIAL PARKING LOT ASPHALT REPAIR WORKS IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0029_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1048",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50013C0029_1900_-NONE-_-NONE- (Peru parking asphalt). Signed 2013-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0029_1900_-NONE-_-NONE-/.",
    "USASpending: Peru parking asphalt USD 0.070m. Supports misc_peru_parking_asphalt_70k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69652.12; date_signed 2013-09-24.",
)

row_doc(
    "misc_brazil_embassy_lighting_69k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil embassy external lighting replacement",
    "Brazil",
    "10 Nov 2016: Department of State awards contract SBR25016M1680 for external lighting replacement — embassy (PoP Brazil); obligated USD 69,093.58. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.",
    "69093.58", "2016-11-10", "2016", "", "",
    "External lighting replacement at embassy, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_embassy_lighting_69k_2016",
    "EXTERNAL LIGHTING REPLACEMENT - EMBASSY ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25016M1680_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1048",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25016M1680_1900_-NONE-_-NONE- (Brazil embassy lighting). Signed 2016-11-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25016M1680_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil embassy lighting USD 0.069m. Supports misc_brazil_embassy_lighting_69k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69093.58; date_signed 2016-11-10.",
)

# === Cycle 1049 (seed 20262049) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_panama_cmr_generator_49k_2014",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Panama CMR generator",
    "Panama",
    "16 Sep 2014: Department of State awards contract SPM07014M0796 to Cummins Power Generation Inc. for Panama 2014 generator CMR — OBO (PoP Panama); obligated USD 48,766.51. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "48766.51", "2014-09-16", "2014", "", "",
    "CMR generator, Panama (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_cummins_panama_cmr_generator_49k_2014",
    "PANAMA 2014 - GENERATOR CMR - OBO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0796_1900_-NONE-_-NONE-/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1049",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07014M0796_1900_-NONE-_-NONE- (Cummins Panama CMR generator). Signed 2014-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0796_1900_-NONE-_-NONE-/.",
    "USASpending: Cummins Panama CMR generator USD 0.049m. Supports cummins_panama_cmr_generator_49k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 48766.51; date_signed 2014-09-16.",
)

row_doc(
    "fluid_solutions_belize_fire_pump_49k_2017",
    "resources", "water", "us",
    "Fluid Solutions — Belize emergency fire pump repairs",
    "Belize",
    "3 May 2017: Department of State awards contract SBH20017M0138 to Fluid Solutions LLC for emergency fire pump repairs (PoP Belize); obligated USD 49,193.84. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49193.84", "2017-05-03", "2017", "", "",
    "Emergency fire pump repairs, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_fluid_solutions_belize_fire_pump_49k_2017",
    "IGF::OT::IGF THIS PURCHASE IS FOR EMERGENCY FIRE PUMP REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20017M0138_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1049",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20017M0138_1900_-NONE-_-NONE- (Fluid Solutions Belize fire pump). Signed 2017-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20017M0138_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions Belize fire pump USD 0.049m. Supports fluid_solutions_belize_fire_pump_49k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49193.84; date_signed 2017-05-03.",
)

row_doc(
    "misc_ecuador_cmr_roof_69k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador CMR roof repairs",
    "Ecuador",
    "16 May 2023: Department of State awards contract 19EC7523P0846 for roof repairs at the CMR (PoP Ecuador); obligated USD 68,805.73. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "68805.73", "2023-05-16", "2023", "", "",
    "Roof repairs at CMR, Ecuador (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_cmr_roof_69k_2023",
    "PR11687564-7355RSTR-CMR-FWP#330-ROOF REPAIRS AT THE CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0846_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1049",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P0846_1900_-NONE-_-NONE- (Ecuador CMR roof). Signed 2023-05-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0846_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador CMR roof USD 0.069m. Supports misc_ecuador_cmr_roof_69k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68805.73; date_signed 2023-05-16.",
)

row_doc(
    "misc_peru_cmr_baths_69k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru CMR representational baths renovation",
    "Peru",
    "25 Sep 2013: Department of State awards contract SPE50013C0033 to renovate representational baths at CMR (PoP Peru); obligated USD 68,794. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "68794", "2013-09-25", "2013", "", "",
    "Representational baths renovation at CMR, Peru (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_cmr_baths_69k_2013",
    "CONTRACT TO RENOVATE REPRESENTATIONAL BATHS AT CMR IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0033_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1049",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50013C0033_1900_-NONE-_-NONE- (Peru CMR baths). Signed 2013-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0033_1900_-NONE-_-NONE-/.",
    "USASpending: Peru CMR baths USD 0.069m. Supports misc_peru_cmr_baths_69k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68794; date_signed 2013-09-25.",
)

row_doc(
    "miscelaneos_cr_fbu_remodel_50k_2021",
    "infrastructure", "building_materials", "other",
    "Miscelaneos Security Services — Costa Rica FBU office remodeling",
    "Costa Rica",
    "28 Sep 2021: Department of State awards contract 19CS8021P1315 to Miscelaneos Security Services Sociedad Anonima for remodeling of FBU office (PoP Costa Rica); obligated USD 49,992.70. CapEx face = award obligation. Exact office unnamed — lat/lon blank.",
    "49992.70", "2021-09-28", "2021", "", "",
    "FBU office remodeling, Costa Rica (USASpending description; office not named — lat/lon blank).",
    "usaspending_miscelaneos_cr_fbu_remodel_50k_2021",
    "REMODELING OF FBU OFFICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8021P1315_1900_-NONE-_-NONE-/",
    "Actor: Miscelaneos Security Services Sociedad Anonima (Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1049",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8021P1315_1900_-NONE-_-NONE- (CR FBU remodel). Signed 2021-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8021P1315_1900_-NONE-_-NONE-/.",
    "USASpending: CR FBU remodel USD 0.050m. Supports miscelaneos_cr_fbu_remodel_50k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49992.70; date_signed 2021-09-28.",
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
