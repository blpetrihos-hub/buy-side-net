#!/usr/bin/env python3
"""Cycles 990–992: USASpending LatAm CapEx residual (~USD0.24–0.27m).

Seeds: 20261990–20261992. Thin top-up dry. Includes Belize solar/wind hybrid.
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


# === Cycle 990 ===
row_doc(
    "cocis_quito_police_265k_2011",
    "infrastructure", "building_materials", "other",
    "COCIS Group — NAS Quito police building refurbishment",
    "Ecuador",
    "10 May 2011: Department of State awards contract SWHARC11C0003 to COCIS Group for NAS Quito refurbishment of a police building in Quito, Ecuador; obligated USD 264,965.76. CapEx face = award obligation.",
    "264965.76", "2011-05-10", "2011", "-0.180", "-78.467",
    "Police building refurbishment, Quito, Ecuador (USASpending description).",
    "usaspending_cocis_quito_police_265k_2011",
    "NAS QUITO- REFURBISHMENT OF A POLICE BUILDING IN QUITO, ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0003_1900_-NONE-_-NONE-/",
    "Actor: COCIS Group S.A. (Quito) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle990",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11C0003_1900_-NONE-_-NONE- (COCIS Quito police). Signed 2011-05-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0003_1900_-NONE-_-NONE-/.",
    "USASpending: COCIS Quito police USD 0.265m. Supports cocis_quito_police_265k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 264965.76; date_signed 2011-05-10.",
)

row_doc(
    "misc_belize_school_medical_siteprep_264k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Belize school and medical buildings site prep",
    "Belize",
    "15 Jan 2014: Department of Defense awards contract FA470414C0001 for foundation and site prep for school and medical buildings (PoP Belize); obligated USD 263,881.68. CapEx face = award obligation. Recipient redacted; exact sites unnamed — lat/lon blank.",
    "263881.68", "2014-01-15", "2014", "", "",
    "Foundation and site prep for school and medical buildings, Belize (USASpending PoP Belize; sites not named — lat/lon blank).",
    "usaspending_misc_belize_school_medical_siteprep_264k_2014",
    "IGF::OT::IGF FOUNDATION&SITE PREP FOR SCHOOL&MEDICAL BUILDINGS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470414C0001_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle990",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470414C0001_9700_-NONE-_-NONE- (Belize school/medical site prep). Signed 2014-01-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470414C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Belize school/medical site prep USD 0.264m. Supports misc_belize_school_medical_siteprep_264k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 263881.68; date_signed 2014-01-15.",
)

row_doc(
    "sima_iquitos_floating_facility_263k_2010",
    "infrastructure", "building_materials", "other",
    "SIMA Iquitos — floating maintenance facility repairs",
    "Peru",
    "3 Mar 2010: U.S. Army Corps of Engineers awards contract W9127810C0038 to SIMA Iquitos for floating maintenance facility repairs including HVAC upgrade and ventilation, spuds anchoring system repair, and exterior sandblasting; obligated USD 262,855.32. CapEx face = award obligation.",
    "262855.32", "2010-03-03", "2010", "-3.749", "-73.254",
    "Floating maintenance facility repairs, Iquitos, Peru (USASpending description).",
    "usaspending_sima_iquitos_floating_facility_263k_2010",
    "FLOATING MAINTENANCE FACILITY REPAIRS TO INCLUDE HVAC UPGRADE AND VENTILATION, SPUDS ANCHORING SYSTEM REPAIR, AND SANDBLASTING OF THE EXTERIOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810C0038_9700_-NONE-_-NONE-/",
    "Actor: SIMA Iquitos S.R.L. (Iquitos, Peru) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle990",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810C0038_9700_-NONE-_-NONE- (SIMA Iquitos floating facility). Signed 2010-03-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810C0038_9700_-NONE-_-NONE-/.",
    "USASpending: SIMA Iquitos floating facility USD 0.263m. Supports sima_iquitos_floating_facility_263k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 262855.32; date_signed 2010-03-03.",
)

row_doc(
    "aei_gualaca_site_260k_2026",
    "infrastructure", "building_materials", "other",
    "Constructora AEI — Los Planes de Gualaca site improvements",
    "Panama",
    "1 Jul 2026: Department of State awards contract 19GE5026P0059 to Constructora AEI for Los Planes de Gualaca site improvements, Panama; obligated USD 259,975.49. CapEx face = award obligation.",
    "259975.49", "2026-07-01", "2026", "8.530", "-82.300",
    "Site improvements, Los Planes de Gualaca, Panama (USASpending description).",
    "usaspending_aei_gualaca_site_260k_2026",
    "CONSTRUCTION ACQUISITION FOR LOS PLANES DE GUALACA SITE IMPROVEMENTS, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026P0059_1900_-NONE-_-NONE-/",
    "Actor: Constructora AEI S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle990",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026P0059_1900_-NONE-_-NONE- (AEI Gualaca). Signed 2026-07-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026P0059_1900_-NONE-_-NONE-/.",
    "USASpending: AEI Gualaca site USD 0.260m. Supports aei_gualaca_site_260k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 259975.49; date_signed 2026-07-01.",
)

row_doc(
    "solano_calabash_solar_wind_260k_2012",
    "energy", "other_renewables", "other",
    "Arturo Solano — Calabash Caye 5 kW solar + vertical-axis wind",
    "Belize",
    "14 Sep 2012: U.S. Army Corps of Engineers awards contract W912CL12C0012 to Arturo Solano for construction and installation of a 5 kW solar panel system and two 5 kW vertical-axis wind turbines at Calabash Caye, Belize; obligated USD 259,723.71. CapEx face = award obligation.",
    "259723.71", "2012-09-14", "2012", "17.280", "-87.810",
    "5 kW solar + two 5 kW VAWTs, Calabash Caye, Belize (USASpending description).",
    "usaspending_solano_calabash_solar_wind_260k_2012",
    "CONSTRUCTION AND INSTALLATION OF A 5 KW SOLAR PANEL SYSTEM AND TWO (5 KW) VERTICAL AXIS WIND TURBINE AT CALABASH CAYE, BELIZE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0012_9700_-NONE-_-NONE-/",
    "Actor: Arturo Solano y Cía de C.V. (San Salvador) — other. Official USASpending Award API. Shuffle other_renewables (solar+wind hybrid).",
    "hunt_cycle990",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL12C0012_9700_-NONE-_-NONE- (Solano Calabash solar/wind). Signed 2012-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0012_9700_-NONE-_-NONE-/.",
    "USASpending: Solano Calabash solar/wind USD 0.260m. Supports solano_calabash_solar_wind_260k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 259723.71; date_signed 2012-09-14.",
)

# === Cycle 991 ===
row_doc(
    "eterna_soto_cano_dining_257k_2008",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano dining facility FY08",
    "Honduras",
    "16 Jul 2008: U.S. Army Corps of Engineers awards task order 0003 under W9127807D0098 to Eterna for FY08 dining facility at Soto Cano Air Base, Honduras; obligated USD 257,335.08. CapEx face = award obligation.",
    "257335.08", "2008-07-16", "2008", "14.382", "-87.621",
    "Dining facility, Soto Cano Air Base, Comayagua, Honduras (USASpending description).",
    "usaspending_eterna_soto_cano_dining_257k_2008",
    "FY 08 DINING FACILITY, SOTO CANO AB HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127807D0098_9700/",
    "Actor: Eterna (San Pedro Sula, Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle991",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127807D0098_9700 (Eterna Soto Cano dining). Signed 2008-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127807D0098_9700/.",
    "USASpending: Eterna Soto Cano dining USD 0.257m. Supports eterna_soto_cano_dining_257k_2008.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 257335.08; date_signed 2008-07-16.",
)

row_doc(
    "john_d_fort_sherman_barracks_253k_2013",
    "infrastructure", "building_materials", "other",
    "John D Engineering — Fort Sherman barracks/bathroom renovation",
    "Panama",
    "18 Jan 2013: U.S. Army Corps of Engineers awards contract W912CL13C0004 to John D Engineering for bathroom and barracks renovation of buildings 208 and 206 at Fort Sherman, Panama; obligated USD 253,378.20. CapEx face = award obligation.",
    "253378.20", "2013-01-18", "2013", "9.370", "-79.950",
    "Barracks/bathroom renovation Bldg 208/206, Fort Sherman, Panama (USASpending description).",
    "usaspending_john_d_fort_sherman_barracks_253k_2013",
    "BATH ROOM&BARRACKS RENOVATION BLDG 208&206 AT FORT SHERMAN, PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0004_9700_-NONE-_-NONE-/",
    "Actor: John D Engineering Ltd. (Ladyville, Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle991",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL13C0004_9700_-NONE-_-NONE- (John D Fort Sherman barracks). Signed 2013-01-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0004_9700_-NONE-_-NONE-/.",
    "USASpending: John D Fort Sherman barracks USD 0.253m. Supports john_d_fort_sherman_barracks_253k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 253378.20; date_signed 2013-01-18.",
)

row_doc(
    "savart_tumaco_santa_marta_ramps_253k_2017",
    "infrastructure", "port_ownership", "other",
    "Montajes Savart — Tumaco and Santa Marta concrete ramps",
    "Colombia",
    "20 Dec 2017: Department of State awards contract 19C01518C0002 to Montajes Savart for INL Navy construction of concrete ramps at Tumaco and Santa Marta; obligated USD 253,114.49. CapEx face = award obligation.",
    "253114.49", "2017-12-20", "2017", "1.806", "-78.765",
    "Concrete ramps, Tumaco and Santa Marta, Colombia (USASpending description; Tumaco pin).",
    "usaspending_savart_tumaco_santa_marta_ramps_253k_2017",
    "INL NAVY CONSTRUCTION CONCRETE RAMPS TUMACO AND SANTA MARTA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01518C0002_1900_-NONE-_-NONE-/",
    "Actor: Montajes Savart S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle991",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01518C0002_1900_-NONE-_-NONE- (Savart Tumaco/Santa Marta ramps). Signed 2017-12-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01518C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Savart Tumaco/Santa Marta ramps USD 0.253m. Supports savart_tumaco_santa_marta_ramps_253k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 253114.49; date_signed 2017-12-20.",
)

row_doc(
    "milbau_ramp_pier_250k_2017",
    "infrastructure", "port_ownership", "other",
    "Milbau — Uruguay ramp pier construction",
    "Uruguay",
    "7 Mar 2017: U.S. Army Corps of Engineers awards contract W912CL17C0003 to Milbau for ramp pier construction (PoP Uruguay); obligated USD 249,781. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "249781", "2017-03-07", "2017", "", "",
    "Ramp pier construction, Uruguay (USASpending PoP Uruguay; site not named — lat/lon blank).",
    "usaspending_milbau_ramp_pier_250k_2017",
    "IGF::OT::IGF RAMP PIER CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0003_9700_-NONE-_-NONE-/",
    "Actor: Milbau S.A. (Solymar, Uruguay) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle991",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17C0003_9700_-NONE-_-NONE- (Milbau ramp pier). Signed 2017-03-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0003_9700_-NONE-_-NONE-/.",
    "USASpending: Milbau ramp pier USD 0.250m. Supports milbau_ramp_pier_250k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 249781; date_signed 2017-03-07.",
)

row_doc(
    "gerinco_health_center_250k_2018",
    "infrastructure", "building_materials", "other",
    "Gerinco Ingeniería — health center construction",
    "Colombia",
    "19 Sep 2018: U.S. Army Corps of Engineers awards contract W913FT18C0001 to Gerinco Ingeniería for construction of a health center (PoP Colombia); obligated USD 249,541.17. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "249541.17", "2018-09-19", "2018", "", "",
    "Health center construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_gerinco_health_center_250k_2018",
    "CONSTRUCTION HEALTH CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT18C0001_9700_-NONE-_-NONE-/",
    "Actor: Gerinco Ingeniería SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle991",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT18C0001_9700_-NONE-_-NONE- (Gerinco health center). Signed 2018-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT18C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Gerinco health center USD 0.250m. Supports gerinco_health_center_250k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 249541.17; date_signed 2018-09-19.",
)

# === Cycle 992 ===
row_doc(
    "qmax_san_salvador_dcr_roof_246k_2019",
    "infrastructure", "building_materials", "us",
    "Q-Max Construction — San Salvador DCR roof replacement",
    "El Salvador",
    "1 Jul 2019: Department of State awards contract 19ES6019P0607 to Q-Max Construction for San Salvador DCR roof replacement project; obligated USD 246,400. CapEx face = award obligation.",
    "246400", "2019-07-01", "2019", "13.693", "-89.218",
    "DCR roof replacement, San Salvador, El Salvador (USASpending description).",
    "usaspending_qmax_san_salvador_dcr_roof_246k_2019",
    "7355-SAN SALVADOR DCR ROOF REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6019P0607_1900_-NONE-_-NONE-/",
    "Actor: Q-Max Construction Company Inc. (Fullerton CA, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle992",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6019P0607_1900_-NONE-_-NONE- (Q-Max San Salvador DCR roof). Signed 2019-07-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6019P0607_1900_-NONE-_-NONE-/.",
    "USASpending: Q-Max San Salvador DCR roof USD 0.246m. Supports qmax_san_salvador_dcr_roof_246k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 246400; date_signed 2019-07-01.",
)

row_doc(
    "pono_haiti_chiller_247k_2021",
    "infrastructure", "building_materials", "us",
    "Pono Aina Management — Haiti chancery chiller/piping/ductwork",
    "Haiti",
    "10 Jun 2021: Department of State awards contract 19AQMM21C0099 to Pono Aina Management for chiller, piping, and rooftop ductwork replacement within the chancery controlled access area (PoP Haiti); obligated USD 246,945.57. CapEx face = award obligation.",
    "246945.57", "2021-06-10", "2021", "18.540", "-72.340",
    "Chancery chiller/piping/ductwork replacement, Haiti (USASpending PoP Haiti; Port-au-Prince pin).",
    "usaspending_pono_haiti_chiller_247k_2021",
    "THE CONTRACTOR SHALL COMPLETE ALL SERVICES REQUIRED FOR CHILLER, PIPING, AND ROOFTOP DUCTWORK REPLACEMENT WITHIN THE CHANCERY, CONTROLLED ACCESS AREA,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0099_1900_-NONE-_-NONE-/",
    "Actor: Pono Aina Management LLC (Midwest City OK, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx; Haiti under-covered.",
    "hunt_cycle992",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21C0099_1900_-NONE-_-NONE- (Pono Haiti chiller). Signed 2021-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0099_1900_-NONE-_-NONE-/.",
    "USASpending: Pono Haiti chiller USD 0.247m. Supports pono_haiti_chiller_247k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 246945.57; date_signed 2021-06-10.",
)

row_doc(
    "baskerville_conchagua_clinic_238k_2019",
    "infrastructure", "building_materials", "us",
    "Baskerville Donovan — Conchagua clinic",
    "El Salvador",
    "10 Feb 2019: U.S. Army Corps of Engineers awards task order W9127819F0094 to Baskerville Donovan for clinic at Conchagua, El Salvador; obligated USD 238,218.95. CapEx face = award obligation.",
    "238218.95", "2019-02-10", "2019", "13.308", "-87.865",
    "Clinic, Conchagua, El Salvador (USASpending description).",
    "usaspending_baskerville_conchagua_clinic_238k_2019",
    "CLINIC-CONCHAGUA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0094_9700_W9127814D0075_9700/",
    "Actor: Baskerville Donovan Inc. (Mobile AL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle992",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0094_9700_W9127814D0075_9700 (Baskerville Conchagua clinic). Signed 2019-02-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0094_9700_W9127814D0075_9700/.",
    "USASpending: Baskerville Conchagua clinic USD 0.238m. Supports baskerville_conchagua_clinic_238k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 238218.95; date_signed 2019-02-10.",
)

row_doc(
    "tropical_price_barracks_243k_2022",
    "infrastructure", "building_materials", "other",
    "Tropical Holdings — Price Barracks renovations",
    "Belize",
    "24 Jan 2022: U.S. Army Corps of Engineers awards contract W912QM22P0008 to Tropical Holdings for Price Barracks Belize barracks renovations; obligated USD 242,611.63. CapEx face = award obligation.",
    "242611.63", "2022-01-24", "2022", "17.540", "-88.300",
    "Barracks renovations, Price Barracks, Belize (USASpending description).",
    "usaspending_tropical_price_barracks_243k_2022",
    "PRICE BARRACKS BLZ. BARRACKS RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22P0008_9700_-NONE-_-NONE-/",
    "Actor: Tropical Holdings Ladyville Ltd. (Ladyville, Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle992",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM22P0008_9700_-NONE-_-NONE- (Tropical Price Barracks). Signed 2022-01-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22P0008_9700_-NONE-_-NONE-/.",
    "USASpending: Tropical Price Barracks USD 0.243m. Supports tropical_price_barracks_243k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 242611.63; date_signed 2022-01-24.",
)

row_doc(
    "chaco_paraguay_fuel_station_244k_2017",
    "infrastructure", "building_materials", "other",
    "Sociedad Constructora Chaco — Paraguay GPO fuel station",
    "Paraguay",
    "24 Sep 2017: U.S. Army Corps of Engineers awards contract W912CL17C0008 to Sociedad Constructora Chaco for Global Peace Keeping Operation construction of a fuel station in Paraguay; obligated USD 243,917.11. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "243917.11", "2017-09-24", "2017", "", "",
    "GPO fuel station construction, Paraguay (USASpending PoP Paraguay; site not named — lat/lon blank).",
    "usaspending_chaco_paraguay_fuel_station_244k_2017",
    "IGF::CT::IGF GLOBAL PEACE KEEPING OPERATION - CONSTRUCTION OF A FUEL STATION - PARAGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0008_9700_-NONE-_-NONE-/",
    "Actor: Sociedad Constructora Chaco S.A. (Asunción) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle992",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17C0008_9700_-NONE-_-NONE- (Chaco Paraguay fuel station). Signed 2017-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0008_9700_-NONE-_-NONE-/.",
    "USASpending: Chaco Paraguay fuel station USD 0.244m. Supports chaco_paraguay_fuel_station_244k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 243917.11; date_signed 2017-09-24.",
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
    print(f"cycles990-992 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
