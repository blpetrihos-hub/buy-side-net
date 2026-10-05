#!/usr/bin/env python3
"""Cycles 1204–1209: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262204–20262209. Thin top-up dry.
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

# === Cycle 1204 ===
row_doc(
    "hdr_honduras_design_build_98k_2010",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Honduras design build",
    "Honduras",
    "2 Feb 2010: Department of Defense awards contract 0004 to HDR ENGINEERING INC for Design build CapEx delivery order (PoP Honduras); obligated USD 97844. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "97844", "2010-02-02", "2010", "", "",
    "Design build CapEx delivery order, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_honduras_design_build_98k_2010",
    "DESIGN BUILD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1204",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127810D0022_9700 (hdr_honduras_design_build_98k_2010). Signed 2010-02-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127810D0022_9700/.",
    "USASpending: hdr_honduras_design_build_98k_2010 USD 0.098m. Supports hdr_honduras_design_build_98k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 97844.0; date_signed 2010-02-02.",
)

# === Cycle 1204 ===
row_doc(
    "hdr_belize_design_bid_build_solicitation_89k_2013",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Belize prepare design bid build solicitation",
    "Belize",
    "20 Jun 2013: Department of Defense awards contract CK02 to HDR ENGINEERING, INC. for Prepare design bid build solicitation (PoP Belize); obligated USD 88941. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "88941", "2013-06-20", "2013", "", "",
    "Prepare design bid build solicitation, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_belize_design_bid_build_solicitation_89k_2013",
    "IGF::OT::IGF PREPARE DESIGN BID BUILD SOLICITATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_CK02_9700_W912P709D0001_9700/",
    "Actor: HDR ENGINEERING, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1204",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_CK02_9700_W912P709D0001_9700 (hdr_belize_design_bid_build_solicitation_89k_2013). Signed 2013-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_CK02_9700_W912P709D0001_9700/.",
    "USASpending: hdr_belize_design_bid_build_solicitation_89k_2013 USD 0.089m. Supports hdr_belize_design_bid_build_solicitation_89k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88941.0; date_signed 2013-06-20.",
)

# === Cycle 1204 ===
row_doc(
    "misc_bolivia_us_embassy_pavilion_design_construction_14k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bolivia PAS design and construction of U.S. Embassy pavilion",
    "Bolivia",
    "15 Jun 2015: Department of State awards contract SBL40015M0221 for PAS design and construction of the U.S. Embassy pavilion (PoP Bolivia); obligated USD 14426.02. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14426.02", "2015-06-15", "2015", "", "",
    "PAS design and construction of the U.S. Embassy pavilion, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bolivia_us_embassy_pavilion_design_construction_14k_2015",
    "IGF::CL,CT::IGF OR IGF::CT,CL::IGF PAS: DESIGN AND CONSTRUCTION OF THE U.S. EMBASSY STAND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40015M0221_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1204",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40015M0221_1900_-NONE-_-NONE- (misc_bolivia_us_embassy_pavilion_design_construction_14k_2015). Signed 2015-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40015M0221_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_us_embassy_pavilion_design_construction_14k_2015 USD 0.014m. Supports misc_bolivia_us_embassy_pavilion_design_construction_14k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14426.02; date_signed 2015-06-15.",
)

# === Cycle 1204 ===
row_doc(
    "misc_colombia_cmr_annex_building_design_14k_2025",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia design for annex building at CMR",
    "Colombia",
    "20 Aug 2025: Department of State awards contract 19C02025P1489 for Design for annex building at CMR (PoP Colombia); obligated USD 14253.79. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14253.79", "2025-08-20", "2025", "", "",
    "Design for annex building at CMR, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_cmr_annex_building_design_14k_2025",
    "PR15547176: DESIGN FOR ANNEX BUILDING AT CMR -7919 XJ1D0119",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025P1489_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1204",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02025P1489_1900_-NONE-_-NONE- (misc_colombia_cmr_annex_building_design_14k_2025). Signed 2025-08-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025P1489_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_cmr_annex_building_design_14k_2025 USD 0.014m. Supports misc_colombia_cmr_annex_building_design_14k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14253.79; date_signed 2025-08-20.",
)

# === Cycle 1204 ===
row_doc(
    "misc_panama_warehouse_fan_coil_units_14k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Panama fan coil units warehouse area",
    "Panama",
    "6 Sep 2016: Department of State awards contract SPM07016M0719 for Fan coil units — warehouse area (PoP Panama); obligated USD 14187.82. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14187.82", "2016-09-06", "2016", "", "",
    "Fan coil units — warehouse area, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_panama_warehouse_fan_coil_units_14k_2016",
    "FAN COIL UNITS - WAREHOUSE AREA (7901.C)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07016M0719_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1204",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07016M0719_1900_-NONE-_-NONE- (misc_panama_warehouse_fan_coil_units_14k_2016). Signed 2016-09-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07016M0719_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_warehouse_fan_coil_units_14k_2016 USD 0.014m. Supports misc_panama_warehouse_fan_coil_units_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14187.82; date_signed 2016-09-06.",
)

# === Cycle 1205 ===
row_doc(
    "hdr_el_salvador_ae_design_51k_2012",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — El Salvador A-E design",
    "El Salvador",
    "19 Jun 2014: Department of Defense awards contract CK01 to HDR ENGINEERING INC for A-E design (PoP El Salvador); obligated USD 50541.51. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "50541.51", "2014-06-19", "2014", "", "",
    "A-E design, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_el_salvador_ae_design_51k_2012",
    "IGF::OT::IGF  A-E DESIGN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_CK01_9700_W9128F12D0012_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1205",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_CK01_9700_W9128F12D0012_9700 (hdr_el_salvador_ae_design_51k_2012). Signed 2014-06-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_CK01_9700_W9128F12D0012_9700/.",
    "USASpending: hdr_el_salvador_ae_design_51k_2012 USD 0.051m. Supports hdr_el_salvador_ae_design_51k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 50541.51; date_signed 2014-06-19.",
)

# === Cycle 1205 ===
row_doc(
    "hdr_honduras_fy12_barracks_50k_2011",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Honduras FY-12 barracks",
    "Honduras",
    "12 Jan 2011: Department of Defense awards contract 0019 to HDR ENGINEERING INC for FY-12 barracks (PoP Honduras); obligated USD 49934. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49934", "2011-01-12", "2011", "", "",
    "FY-12 barracks, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_honduras_fy12_barracks_50k_2011",
    "FY-12 BARRACKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0019_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1205",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0019_9700_W9127810D0022_9700 (hdr_honduras_fy12_barracks_50k_2011). Signed 2011-01-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0019_9700_W9127810D0022_9700/.",
    "USASpending: hdr_honduras_fy12_barracks_50k_2011 USD 0.050m. Supports hdr_honduras_fy12_barracks_50k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49934.0; date_signed 2011-01-12.",
)

# === Cycle 1205 ===
row_doc(
    "misc_peru_warehouse_shelving_14k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru purchase of shelving for new warehouse",
    "Peru",
    "21 Dec 2010: Department of State awards contract SPE50011M0169 for Purchase of shelving for new warehouse (PoP Peru); obligated USD 14244.35. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14244.35", "2010-12-21", "2010", "", "",
    "Purchase of shelving for new warehouse, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_warehouse_shelving_14k_2011",
    "11/30 WHSE-PURCHASE OF SHELVING FOR NEW WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50011M0169_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1205",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50011M0169_1900_-NONE-_-NONE- (misc_peru_warehouse_shelving_14k_2011). Signed 2010-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50011M0169_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_warehouse_shelving_14k_2011 USD 0.014m. Supports misc_peru_warehouse_shelving_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14244.35; date_signed 2010-12-21.",
)

# === Cycle 1205 ===
row_doc(
    "misc_el_salvador_stainless_steel_pipe_well_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador stainless steel pipe for well #1",
    "El Salvador",
    "10 Apr 2014: Department of State awards contract SES60014M0353 for Stainless steel pipe for well #1 (PoP El Salvador); obligated USD 14170. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14170", "2014-04-10", "2014", "", "",
    "Stainless steel pipe for well #1, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_stainless_steel_pipe_well_14k_2014",
    "IGF::OT::IGF   7901 FUNDS- STAINLESS STEEL PIPE FOR WELL #1",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60014M0353_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1205",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60014M0353_1900_-NONE-_-NONE- (misc_el_salvador_stainless_steel_pipe_well_14k_2014). Signed 2014-04-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60014M0353_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_stainless_steel_pipe_well_14k_2014 USD 0.014m. Supports misc_el_salvador_stainless_steel_pipe_well_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14170.0; date_signed 2014-04-10.",
)

# === Cycle 1205 ===
row_doc(
    "misc_costa_rica_ac_equip_border_police_km35_14k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica INL purchase of A/C equipment for border police KM35",
    "Costa Rica",
    "12 May 2017: Department of State awards contract SCS80017M0093 for INL purchase of A/C equip border police KM35 (PoP Costa Rica); obligated USD 14098.26. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14098.26", "2017-05-12", "2017", "", "",
    "INL purchase of A/C equip border police KM35, Costa Rica (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_ac_equip_border_police_km35_14k_2017",
    "PR5822972 - INL 1930.0 PURCHASE OF A/C EQUIP. BORDER POLICE KM35",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80017M0093_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1205",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80017M0093_1900_-NONE-_-NONE- (misc_costa_rica_ac_equip_border_police_km35_14k_2017). Signed 2017-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80017M0093_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_ac_equip_border_police_km35_14k_2017 USD 0.014m. Supports misc_costa_rica_ac_equip_border_police_km35_14k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14098.26; date_signed 2017-05-12.",
)

# === Cycle 1206 ===
row_doc(
    "honeywell_security_brazil_residential_security_rso_28k_2011",
    "infrastructure", "building_materials", "us",
    "Honeywell Security Americas — Brazil residential security RSO",
    "Brazil",
    "19 Sep 2011: Department of State awards contract SBR25011F0213 to HONEYWELL SECURITY AMERICAS LLC for Residential security — RSO (PoP Brazil); obligated USD 28042.40. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "28042.40", "2011-09-19", "2011", "", "",
    "Residential security — RSO, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_honeywell_security_brazil_residential_security_rso_28k_2011",
    "PURCHASE ORDER - RESIDENTIAL SECURITY - RSO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011F0213_1900_GS07F0450K_4730/",
    "Actor: HONEYWELL SECURITY AMERICAS LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1206",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25011F0213_1900_GS07F0450K_4730 (honeywell_security_brazil_residential_security_rso_28k_2011). Signed 2011-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011F0213_1900_GS07F0450K_4730/.",
    "USASpending: honeywell_security_brazil_residential_security_rso_28k_2011 USD 0.028m. Supports honeywell_security_brazil_residential_security_rso_28k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28042.4; date_signed 2011-09-19.",
)

# === Cycle 1206 ===
row_doc(
    "multistack_brazil_refrigeration_equipment_12k_2018",
    "energy", "power_plants_grid", "us",
    "Multistack — Brazil refrigeration equipment",
    "Brazil",
    "8 Mar 2018: Department of State awards contract 19BR8218K0195 to MULTISTACK LLC for Refrigeration equipment (PoP Brazil); obligated USD 12009. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12009", "2018-03-08", "2018", "", "",
    "Refrigeration equipment, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_multistack_brazil_refrigeration_equipment_12k_2018",
    "REFRIGERATION EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8218K0195_1900_-NONE-_-NONE-/",
    "Actor: MULTISTACK LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1206",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8218K0195_1900_-NONE-_-NONE- (multistack_brazil_refrigeration_equipment_12k_2018). Signed 2018-03-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8218K0195_1900_-NONE-_-NONE-/.",
    "USASpending: multistack_brazil_refrigeration_equipment_12k_2018 USD 0.012m. Supports multistack_brazil_refrigeration_equipment_12k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12009.0; date_signed 2018-03-08.",
)

# === Cycle 1206 ===
row_doc(
    "misc_mexico_tres_canadas_make_ready_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico FAC and POL make-ready works in Tres Canadas II-12",
    "Mexico",
    "12 Jul 2013: Department of State awards contract SMX53013M0998 for FAC and POL make-ready works in Tres Canadas II-12 (PoP Mexico); obligated USD 14012.07. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14012.07", "2013-07-12", "2013", "", "",
    "FAC and POL make-ready works in Tres Canadas II-12, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_tres_canadas_make_ready_14k_2013",
    "MEX/FAC AND POL-MAKE READY WORKS IN TRES CANADAS II-12  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0998_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1206",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M0998_1900_-NONE-_-NONE- (misc_mexico_tres_canadas_make_ready_14k_2013). Signed 2013-07-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0998_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_tres_canadas_make_ready_14k_2013 USD 0.014m. Supports misc_mexico_tres_canadas_make_ready_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14012.07; date_signed 2013-07-12.",
)

# === Cycle 1206 ===
row_doc(
    "misc_mexico_cmr_wiring_electrical_restoration_14k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico FAC-OBO wiring/electrical restoration landscape CMR",
    "Mexico",
    "24 Feb 2020: Department of State awards contract 19MX5320P0426 for Wiring/electrical restoration landscape CMR (PoP Mexico); obligated USD 13960.88. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13960.88", "2020-02-24", "2020", "", "",
    "Wiring/electrical restoration landscape CMR, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cmr_wiring_electrical_restoration_14k_2020",
    "MX-FAC-OBO-WIRING/ELECTRICAL RESTORATION LANDSCAPE CMR-FY20",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5320P0426_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1206",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5320P0426_1900_-NONE-_-NONE- (misc_mexico_cmr_wiring_electrical_restoration_14k_2020). Signed 2020-02-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5320P0426_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cmr_wiring_electrical_restoration_14k_2020 USD 0.014m. Supports misc_mexico_cmr_wiring_electrical_restoration_14k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13960.88; date_signed 2020-02-24.",
)

# === Cycle 1206 ===
row_doc(
    "misc_dominican_make_ready_bambues_04_14k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic FAC make-ready Bambues 04",
    "Dominican Republic",
    "2 Jun 2025: Department of State awards contract 19DR8625C0046 for FAC make-ready work Bambues 04 PID 829 (PoP Dominican Republic); obligated USD 13964.08. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13964.08", "2025-06-02", "2025", "", "",
    "FAC make-ready work Bambues 04 PID 829, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_bambues_04_14k_2025",
    "FAC-MAKE READY WORK BAMBUES 04 PID 829 MRV - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625C0046_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1206",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8625C0046_1900_-NONE-_-NONE- (misc_dominican_make_ready_bambues_04_14k_2025). Signed 2025-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625C0046_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_bambues_04_14k_2025 USD 0.014m. Supports misc_dominican_make_ready_bambues_04_14k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13964.08; date_signed 2025-06-02.",
)

# === Cycle 1207 ===
row_doc(
    "ross_technology_mexico_metal_door_steel_8k_2019",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Mexico metal door steel",
    "Mexico",
    "5 Mar 2019: Department of State awards contract 19AQMM19P0371 to ROSS TECHNOLOGY COMPANY for Metal door steel etc. (PoP Mexico); obligated USD 8216. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8216", "2019-03-05", "2019", "", "",
    "Metal door steel etc., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_ross_technology_mexico_metal_door_steel_8k_2019",
    "METAL DOOR STEEL ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0371_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1207",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0371_1900_-NONE-_-NONE- (ross_technology_mexico_metal_door_steel_8k_2019). Signed 2019-03-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0371_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_mexico_metal_door_steel_8k_2019 USD 0.008m. Supports ross_technology_mexico_metal_door_steel_8k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8216.0; date_signed 2019-03-05.",
)

# === Cycle 1207 ===
row_doc(
    "norshield_brazil_metal_door_screen_8k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen",
    "Brazil",
    "7 Nov 2019: Department of State awards contract 19AQMM20P0071 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen etc. (PoP Brazil); obligated USD 8015. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8015", "2019-11-07", "2019", "", "",
    "Metal door screen etc., Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_8k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0071_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1207",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0071_1900_-NONE-_-NONE- (norshield_brazil_metal_door_screen_8k_2020). Signed 2019-11-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0071_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_screen_8k_2020 USD 0.008m. Supports norshield_brazil_metal_door_screen_8k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8015.0; date_signed 2019-11-07.",
)

# === Cycle 1207 ===
row_doc(
    "misc_colombia_natura_makeready_7apts_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia facilities/safety make-ready work 7 apts Natura building",
    "Colombia",
    "8 Jun 2016: Department of State awards contract SCO20016M0531 for Facilities/safety make-ready work 7 apts Natura building (PoP Colombia); obligated USD 13961.95. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13961.95", "2016-06-08", "2016", "", "",
    "Facilities/safety make-ready work 7 apts Natura building, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_natura_makeready_7apts_14k_2016",
    "IGF::OT::IGF FACILITES/SAFETY MAKEREADY WORK 7 APTS NATURA BUILDING/GENER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20016M0531_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1207",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20016M0531_1900_-NONE-_-NONE- (misc_colombia_natura_makeready_7apts_14k_2016). Signed 2016-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20016M0531_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_natura_makeready_7apts_14k_2016 USD 0.014m. Supports misc_colombia_natura_makeready_7apts_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13961.95; date_signed 2016-06-08.",
)

# === Cycle 1207 ===
row_doc(
    "misc_usaid_dominican_make_ready_los_bambues_01_14k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic USAID make-ready Los Bambues 01",
    "Dominican Republic",
    "2 Jul 2024: Department of State awards contract 19DR8624C0047 for USAID make-ready work Los Bambues 01 PID 822 (PoP Dominican Republic); obligated USD 13907.24. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13907.24", "2024-07-02", "2024", "", "",
    "USAID make-ready work Los Bambues 01 PID 822, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_usaid_dominican_make_ready_los_bambues_01_14k_2024",
    "USAID MAKE READY WORK LOS BAMBUES 01 PID 822 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0047_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1207",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0047_1900_-NONE-_-NONE- (misc_usaid_dominican_make_ready_los_bambues_01_14k_2024). Signed 2024-07-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0047_1900_-NONE-_-NONE-/.",
    "USASpending: misc_usaid_dominican_make_ready_los_bambues_01_14k_2024 USD 0.014m. Supports misc_usaid_dominican_make_ready_los_bambues_01_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13907.24; date_signed 2024-07-02.",
)

# === Cycle 1207 ===
row_doc(
    "johnson_controls_mexico_chancery_ahu_replacement_14k_2020",
    "energy", "power_plants_grid", "other",
    "Johnson Controls BE Operations México — Mexico chancery AHU replacement FY20",
    "Mexico",
    "26 Aug 2020: Department of State awards contract 19MX5320P0937 for Chancery AHU replacement FY20 (PoP Mexico); obligated USD 14283.88. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14283.88", "2020-08-26", "2020", "", "",
    "Chancery AHU replacement FY20, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_johnson_controls_mexico_chancery_ahu_replacement_14k_2020",
    "MX-FAC-OBO-CHANCERY AHU REPLACEMENT-FY20",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5320P0937_1900_-NONE-_-NONE-/",
    "Actor: JOHNSON CONTROLS BE OPERATIONS MÉXICO, S (Mexico-incorporated) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1207",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5320P0937_1900_-NONE-_-NONE- (johnson_controls_mexico_chancery_ahu_replacement_14k_2020). Signed 2020-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5320P0937_1900_-NONE-_-NONE-/.",
    "USASpending: johnson_controls_mexico_chancery_ahu_replacement_14k_2020 USD 0.014m. Supports johnson_controls_mexico_chancery_ahu_replacement_14k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14283.88; date_signed 2020-08-26.",
)

# === Cycle 1208 ===
row_doc(
    "norshield_trinidad_metal_door_screen_frame_8k_2025",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Trinidad and Tobago metal door screen frame for international embassies",
    "Trinidad and Tobago",
    "6 Dec 2024: Department of State awards contract 19AQMM25P0152 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen frame etc. for international embassies (PoP Trinidad and Tobago); obligated USD 7860. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "7860", "2024-12-06", "2024", "", "",
    "Metal door screen frame etc. for international embassies, Trinidad and Tobago (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_trinidad_metal_door_screen_frame_8k_2025",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0152_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1208",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0152_1900_-NONE-_-NONE- (norshield_trinidad_metal_door_screen_frame_8k_2025). Signed 2024-12-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0152_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_trinidad_metal_door_screen_frame_8k_2025 USD 0.008m. Supports norshield_trinidad_metal_door_screen_frame_8k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7860.0; date_signed 2024-12-06.",
)

# === Cycle 1208 ===
row_doc(
    "ross_technology_brazil_metal_screening_glazing_panel_8k_2015",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Brazil metal screening glazing panel",
    "Brazil",
    "4 Nov 2014: Department of State awards contract SAQMMA15M0065 to ROSS TECHNOLOGY COMPANY for Metal screening glazing panel etc. (PoP Brazil); obligated USD 7839. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "7839", "2014-11-04", "2014", "", "",
    "Metal screening glazing panel etc., Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_ross_technology_brazil_metal_screening_glazing_panel_8k_2015",
    "METAL SCREENING GLAZING PANEL ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15M0065_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1208",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15M0065_1900_-NONE-_-NONE- (ross_technology_brazil_metal_screening_glazing_panel_8k_2015). Signed 2014-11-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15M0065_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_brazil_metal_screening_glazing_panel_8k_2015 USD 0.008m. Supports ross_technology_brazil_metal_screening_glazing_panel_8k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7839.0; date_signed 2014-11-04.",
)

# === Cycle 1208 ===
row_doc(
    "misc_mexico_data_wiring_dcr_make_ready_14k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico IMO data wiring for DCR make-ready",
    "Mexico",
    "13 Aug 2015: Department of State awards contract SMX53015M1509 for Data wiring for DCR make-ready (PoP Mexico); obligated USD 13946.41. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13946.41", "2015-08-13", "2015", "", "",
    "Data wiring for DCR make-ready, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_data_wiring_dcr_make_ready_14k_2015",
    "IGF::OT::IGF EOY15/MEX/IMO/DATA WIRING FOR DCR - MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M1509_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1208",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015M1509_1900_-NONE-_-NONE- (misc_mexico_data_wiring_dcr_make_ready_14k_2015). Signed 2015-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M1509_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_data_wiring_dcr_make_ready_14k_2015 USD 0.014m. Supports misc_mexico_data_wiring_dcr_make_ready_14k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13946.41; date_signed 2015-08-13.",
)

# === Cycle 1208 ===
row_doc(
    "misc_peru_replace_led_reflectors_14k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru replace services reflectors LED 200W",
    "Peru",
    "15 Jun 2022: Department of Defense awards contract N4485222P0032 for Replace services reflectors LED 200W (PoP Peru); obligated USD 13932. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13932", "2022-06-15", "2022", "", "",
    "Replace services reflectors LED 200W, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_replace_led_reflectors_14k_2022",
    "REPLACE SERVICES REFLECTORS LED 200W.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N4485222P0032_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1208",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N4485222P0032_9700_-NONE-_-NONE- (misc_peru_replace_led_reflectors_14k_2022). Signed 2022-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N4485222P0032_9700_-NONE-_-NONE-/.",
    "USASpending: misc_peru_replace_led_reflectors_14k_2022 USD 0.014m. Supports misc_peru_replace_led_reflectors_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13932.0; date_signed 2022-06-15.",
)

# === Cycle 1208 ===
row_doc(
    "misc_brazil_dehumidifier_make_ready_residences_14k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil dehumidifier 220V for make-ready residences",
    "Brazil",
    "8 Jun 2022: Department of State awards contract 19BR2522P1002 for Dehumidifier 220V for make-ready residences (PoP Brazil); obligated USD 14109.79. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14109.79", "2022-06-08", "2022", "", "",
    "Dehumidifier 220V for make-ready residences, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_dehumidifier_make_ready_residences_14k_2022",
    "BSB/PSW - DEHUMIDIFIER 220V FOR MAKE READY RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P1002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1208",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2522P1002_1900_-NONE-_-NONE- (misc_brazil_dehumidifier_make_ready_residences_14k_2022). Signed 2022-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P1002_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_dehumidifier_make_ready_residences_14k_2022 USD 0.014m. Supports misc_brazil_dehumidifier_make_ready_residences_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14109.79; date_signed 2022-06-08.",
)

# === Cycle 1209 ===
row_doc(
    "generac_honduras_portable_light_tower_generator_7k_2010",
    "energy", "power_plants_grid", "us",
    "Generac Mobile Products — Honduras portable light tower with generator",
    "Honduras",
    "10 Sep 2010: Department of Defense awards contract W912QM10F0021 to GENERAC MOBILE PRODUCTS, LLC for Portable light tower with generator (PoP Honduras); obligated USD 7186.57. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "7186.57", "2010-09-10", "2010", "", "",
    "Portable light tower with generator, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_generac_honduras_portable_light_tower_generator_7k_2010",
    "PORTABLE LIGHT TOWER WITH GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM10F0021_9700_GS07F0211M_4730/",
    "Actor: GENERAC MOBILE PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1209",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM10F0021_9700_GS07F0211M_4730 (generac_honduras_portable_light_tower_generator_7k_2010). Signed 2010-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM10F0021_9700_GS07F0211M_4730/.",
    "USASpending: generac_honduras_portable_light_tower_generator_7k_2010 USD 0.007m. Supports generac_honduras_portable_light_tower_generator_7k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7186.57; date_signed 2010-09-10.",
)

# === Cycle 1209 ===
row_doc(
    "fabrication_designs_jamaica_teller_window_acs_mobay_7k_2010",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Jamaica teller window for ACS Mobay",
    "Jamaica",
    "12 Apr 2010: Department of State awards contract SJM37010M0505 to FABRICATION DESIGNS, INC. for Teller window for ACS Mobay (PoP Jamaica); obligated USD 6954. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "6954", "2010-04-12", "2010", "", "",
    "Teller window for ACS Mobay, Jamaica (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_fabrication_designs_jamaica_teller_window_acs_mobay_7k_2010",
    "FM: TELLER WINDOW FOR ACS MOBAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010M0505_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1209",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37010M0505_1900_-NONE-_-NONE- (fabrication_designs_jamaica_teller_window_acs_mobay_7k_2010). Signed 2010-04-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010M0505_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_jamaica_teller_window_acs_mobay_7k_2010 USD 0.007m. Supports fabrication_designs_jamaica_teller_window_acs_mobay_7k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6954.0; date_signed 2010-04-12.",
)

# === Cycle 1209 ===
row_doc(
    "misc_el_salvador_ilea_laminate_floor_gym_13k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador ILEA laminate floor installation for ILEA gym",
    "El Salvador",
    "27 Nov 2020: Department of State awards contract 19ES6021P0074 for ILEA laminate floor installation for ILEA gym (PoP El Salvador); obligated USD 13305. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13305", "2020-11-27", "2020", "", "",
    "ILEA laminate floor installation for ILEA gym, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_ilea_laminate_floor_gym_13k_2021",
    "ILEA-LAMINATE FLOOR INSTALLATION FOR ILEA GYM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0074_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1209",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6021P0074_1900_-NONE-_-NONE- (misc_el_salvador_ilea_laminate_floor_gym_13k_2021). Signed 2020-11-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0074_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_ilea_laminate_floor_gym_13k_2021 USD 0.013m. Supports misc_el_salvador_ilea_laminate_floor_gym_13k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13305.0; date_signed 2020-11-27.",
)

# === Cycle 1209 ===
row_doc(
    "misc_mexico_obo_fire_pump_labor_13k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico OBO labor for fire pump replacement",
    "Mexico",
    "23 Mar 2011: Department of State awards contract SMX11511M0251 for OBO labor for fire pump replacement (PoP Mexico); obligated USD 13292.91. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13292.91", "2011-03-23", "2011", "", "",
    "OBO labor for fire pump replacement, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_obo_fire_pump_labor_13k_2011",
    "OBO-LABOR FOR FIRE PUMP REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11511M0251_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1209",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11511M0251_1900_-NONE-_-NONE- (misc_mexico_obo_fire_pump_labor_13k_2011). Signed 2011-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11511M0251_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_obo_fire_pump_labor_13k_2011 USD 0.013m. Supports misc_mexico_obo_fire_pump_labor_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13292.91; date_signed 2011-03-23.",
)

# === Cycle 1209 ===
row_doc(
    "misc_dominican_obo_repairs_make_ready_lbb45_14k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic OBO CONS repairs make-ready LBB 45",
    "Dominican Republic",
    "19 Jan 2024: Department of State awards contract 19DR8624C0007 for OBO CONS repairs make-ready work LBB 45 PID803 (PoP Dominican Republic); obligated USD 13947.76. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13947.76", "2024-01-19", "2024", "", "",
    "OBO CONS repairs make-ready work LBB 45 PID803, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_obo_repairs_make_ready_lbb45_14k_2024",
    "OBO CONS REPAIRS MAKE READY WORK LBB 45 PID803 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1209",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0007_1900_-NONE-_-NONE- (misc_dominican_obo_repairs_make_ready_lbb45_14k_2024). Signed 2024-01-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_obo_repairs_make_ready_lbb45_14k_2024 USD 0.014m. Supports misc_dominican_obo_repairs_make_ready_lbb45_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13947.76; date_signed 2024-01-19.",
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
