#!/usr/bin/env python3
"""Cycles 996–998: USASpending LatAm CapEx residual (~USD0.17–0.21m).

Seeds: 20261996–20261998. Thin top-up dry.
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


# === Cycle 996 ===
row_doc(
    "misc_guyana_well_210k_2017",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Guyana well installation",
    "Guyana",
    "18 Apr 2017: Department of State awards contract SGY20017C0001 for well installation (PoP Guyana); obligated USD 210,000. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "210000", "2017-04-18", "2017", "", "",
    "Well installation, Guyana (USASpending PoP Guyana; site not named — lat/lon blank).",
    "usaspending_misc_guyana_well_210k_2017",
    "IGF::CL::IGF WELL INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20017C0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle996",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20017C0001_1900_-NONE-_-NONE- (Guyana well installation). Signed 2017-04-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20017C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Guyana well installation USD 0.210m. Supports misc_guyana_well_210k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 210000; date_signed 2017-04-18.",
)

row_doc(
    "eterna_el_bluff_warehouse_210k_2011",
    "infrastructure", "building_materials", "other",
    "Eterna — El Bluff CN warehouse renovation",
    "Nicaragua",
    "20 Sep 2011: DoD awards task order 0003 under W9127811D0046 to Empresa de Construcción y Transporte Eterna for construction of CN warehouse renovation at El Bluff, Nicaragua; obligated USD 209,505.06. CapEx face = award obligation. Distinct from eterna_el_bluff_ops_1p43m_2011 (task 0004 ops center/boat ramp).",
    "209505.06", "2011-09-20", "2011", "11.990", "-83.690",
    "CN warehouse renovation, El Bluff, Nicaragua (USASpending description; El Bluff pin).",
    "usaspending_eterna_el_bluff_warehouse_210k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF CN WAREHOUSE RENOVATION EL BLUFF, NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0046_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (San Pedro Sula, Honduras) — other. Official USASpending Award API. Shuffle building_materials; Nicaragua under-covered.",
    "hunt_cycle996",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127811D0046_9700 (Eterna El Bluff warehouse). Signed 2011-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0046_9700/.",
    "USASpending: Eterna El Bluff warehouse USD 0.210m. Supports eterna_el_bluff_warehouse_210k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 209505.06; date_signed 2011-09-20.",
)

row_doc(
    "nv5_santo_domingo_hvac_209k_2022",
    "infrastructure", "building_materials", "us",
    "NV5 Consultants — Santo Domingo HVAC",
    "Dominican Republic",
    "26 Aug 2022: Department of State awards task order 19AQMM22F3143 to NV5 Consultants for HVAC work in Santo Domingo (PoP Dominican Republic); obligated USD 209,312. CapEx face = award obligation.",
    "209312", "2022-08-26", "2022", "18.486", "-69.931",
    "HVAC works, Santo Domingo, Dominican Republic (USASpending description).",
    "usaspending_nv5_santo_domingo_hvac_209k_2022",
    "RXCX HVAC SANTO DOMINGO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F3143_1900_19AQMM19D0019_1900/",
    "Actor: NV5 Consultants, Inc. (Saint Paul MN, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle996",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F3143_1900_19AQMM19D0019_1900 (NV5 Santo Domingo HVAC). Signed 2022-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F3143_1900_19AQMM19D0019_1900/.",
    "USASpending: NV5 Santo Domingo HVAC USD 0.209m. Supports nv5_santo_domingo_hvac_209k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 209312; date_signed 2022-08-26.",
)

row_doc(
    "jc_ancon_chillers_208k_2020",
    "infrastructure", "building_materials", "other",
    "Johnson Controls Panama — Ancon CTPA York chiller replacement",
    "Panama",
    "30 Sep 2020: Smithsonian awards contract 33330220CF0010438 to Johnson Controls Panama for labor, material and equipment to replace two York chillers at Ancon CTPA building; obligated USD 207,537.47. CapEx face = award obligation.",
    "207537.47", "2020-09-30", "2020", "8.960", "-79.550",
    "York chiller replacement, Ancon CTPA building, Panama (USASpending / Smithsonian).",
    "usaspending_jc_ancon_chillers_208k_2020",
    "TO FURNISH LABOR, MATERIAL AND EQUIPMENT FOR REPLACE TWO(2)YORK CHILLERS AT ANCONS CTPA BUILDING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220CF0010438_3300_-NONE-_-NONE-/",
    "Actor: Johnson Controls Panama S. de R.L. (Panama City) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle996",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330220CF0010438_3300_-NONE-_-NONE- (JC Ancon chillers). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220CF0010438_3300_-NONE-_-NONE-/.",
    "USASpending: JC Ancon chillers USD 0.208m. Supports jc_ancon_chillers_208k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 207537.47; date_signed 2020-09-30.",
)

row_doc(
    "wiese_ecuador_locker_ae_206k_2023",
    "infrastructure", "engineering_epc", "other",
    "Christian Wiese — A&E compound locker facility Ecuador",
    "Ecuador",
    "7 Jun 2023: Department of State awards contract 19EC7523P0797 to Christian Reinhard Wiese Fernández de Córdova for A&E compound locker facility (PoP Ecuador); obligated USD 205,695. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "205695", "2023-06-07", "2023", "", "",
    "A&E compound locker facility, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_wiese_ecuador_locker_ae_206k_2023",
    "1900.0-PR11662788-A&E COMPOUND LOCKER FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0797_1900_-NONE-_-NONE-/",
    "Actor: Christian Reinhard Wiese Fernández de Córdova (Quito) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle996",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P0797_1900_-NONE-_-NONE- (Wiese locker A&E). Signed 2023-06-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0797_1900_-NONE-_-NONE-/.",
    "USASpending: Wiese locker A&E USD 0.206m. Supports wiese_ecuador_locker_ae_206k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205695; date_signed 2023-06-07.",
)

# === Cycle 997 ===
row_doc(
    "acosta_juarez_multicourt_205k_2024",
    "infrastructure", "building_materials", "other",
    "Anahí Acosta — Ciudad Juárez multi-use court construction",
    "Mexico",
    "4 Jan 2024: Department of State awards contract 19MX1124P0047 to Anahí Rosario Acosta Vargas for construction of a multi-use court (PoP Mexico / Ciudad Juárez); obligated USD 205,214.26. CapEx face = award obligation.",
    "205214.26", "2024-01-04", "2024", "31.690", "-106.425",
    "Multi-use court construction, Ciudad Juárez, Mexico (USASpending description).",
    "usaspending_acosta_juarez_multicourt_205k_2024",
    "FAC 7901-MCI-XJ2M0012-CCS-CONSTRUCTION OF A MULTI-USE COURT-FY24",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1124P0047_1900_-NONE-_-NONE-/",
    "Actor: Anahí Rosario Acosta Vargas (Juárez) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle997",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1124P0047_1900_-NONE-_-NONE- (Acosta Juárez multicourt). Signed 2024-01-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1124P0047_1900_-NONE-_-NONE-/.",
    "USASpending: Acosta Juárez multicourt USD 0.205m. Supports acosta_juarez_multicourt_205k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205214.26; date_signed 2024-01-04.",
)

row_doc(
    "misc_bahamas_msgr_roof_205k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas MSGR roof replacement",
    "Bahamas",
    "15 Jun 2017: Department of State awards contract SBF50017C0006 for MSGR roof replacement (PoP Bahamas); obligated USD 205,136.88. CapEx face = award obligation. Recipient redacted.",
    "205136.88", "2017-06-15", "2017", "25.078", "-77.345",
    "MSGR roof replacement, Bahamas (USASpending PoP Bahamas; Nassau approximate).",
    "usaspending_misc_bahamas_msgr_roof_205k_2017",
    "IGF::OT::IGF MSGR - ROOF REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle997",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017C0006_1900_-NONE-_-NONE- (Bahamas MSGR roof). Signed 2017-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0006_1900_-NONE-_-NONE-/.",
    "USASpending: Bahamas MSGR roof USD 0.205m. Supports misc_bahamas_msgr_roof_205k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205136.88; date_signed 2017-06-15.",
)

row_doc(
    "proksol_apiay_blast_wall_205k_2012",
    "infrastructure", "building_materials", "other",
    "Proksol — Apiay blast wall south ramp",
    "Colombia",
    "3 Aug 2012: U.S. Army Corps of Engineers awards contract W913FT12P0262 to Proksol for Apiay blast wall south ramp (PoP Colombia); obligated USD 204,612.67. CapEx face = award obligation.",
    "204612.67", "2012-08-03", "2012", "4.070", "-73.570",
    "Blast wall south ramp, Apiay Air Base, Meta, Colombia (USASpending description).",
    "usaspending_proksol_apiay_blast_wall_205k_2012",
    "APIAY BLAST WALL SOUTH RAMP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0262_9700_-NONE-_-NONE-/",
    "Actor: Proksol SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle997",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0262_9700_-NONE-_-NONE- (Proksol Apiay blast wall). Signed 2012-08-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0262_9700_-NONE-_-NONE-/.",
    "USASpending: Proksol Apiay blast wall USD 0.205m. Supports proksol_apiay_blast_wall_205k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 204612.67; date_signed 2012-08-03.",
)

row_doc(
    "cec_hnd_pedestrian_gate_205k_2024",
    "infrastructure", "building_materials", "other",
    "Civil Electrical Construction — Honduras pedestrian gate",
    "Honduras",
    "27 Sep 2024: DoD awards contract W912QM24P0039 to Civil Electrical Construction Company for pedestrian gate project (PoP Honduras); obligated USD 204,607.75. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "204607.75", "2024-09-27", "2024", "", "",
    "Pedestrian gate project, Honduras (USASpending PoP Honduras; site not named — lat/lon blank).",
    "usaspending_cec_hnd_pedestrian_gate_205k_2024",
    "PEDESTRIAN GATE PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM24P0039_9700_-NONE-_-NONE-/",
    "Actor: Civil Electrical Construction Company S. de R.L. (Distrito Central, Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle997",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM24P0039_9700_-NONE-_-NONE- (CEC pedestrian gate). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM24P0039_9700_-NONE-_-NONE-/.",
    "USASpending: CEC pedestrian gate USD 0.205m. Supports cec_hnd_pedestrian_gate_205k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 204607.75; date_signed 2024-09-27.",
)

row_doc(
    "tia_haiti_stecher_fence_204k_2011",
    "infrastructure", "building_materials", "other",
    "Technique Industrie Agriculture — Stecher/Romain perimeter fence",
    "Haiti",
    "19 Aug 2011: Department of State awards contract SHA70011M1225 to Technique Industrie Agriculture for construction of a temporary perimeter fence at Stecher/Romain; obligated USD 204,340.80. CapEx face = award obligation. Distinct from olgoonik_stecher_roumain_electrical_2p87m_2020.",
    "204340.80", "2011-08-19", "2011", "18.540", "-72.340",
    "Temporary perimeter fence, Stecher/Romain, Port-au-Prince, Haiti (USASpending description).",
    "usaspending_tia_haiti_stecher_fence_204k_2011",
    "CONSTRUCTION OF A TEMPORARY PERIMETER FENCE AT STECHER/ROMAIN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70011M1225_1900_-NONE-_-NONE-/",
    "Actor: Technique Industrie Agriculture S.A. (Port-au-Prince) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle997",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHA70011M1225_1900_-NONE-_-NONE- (TIA Stecher fence). Signed 2011-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70011M1225_1900_-NONE-_-NONE-/.",
    "USASpending: TIA Stecher fence USD 0.204m. Supports tia_haiti_stecher_fence_204k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 204340.80; date_signed 2011-08-19.",
)

# === Cycle 998 ===
row_doc(
    "eterna_soto_cano_hazwaste_203k_2018",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano hazardous waste storage facility repairs",
    "Honduras",
    "25 Sep 2018: USACE awards task order W9127818F0643 to Empresa de Construcción y Transporte Eterna for design and construction of repairs of hazardous waste storage facility at Soto Cano Air Base, Honduras; obligated USD 203,367.48. CapEx face = award obligation.",
    "203367.48", "2018-09-25", "2018", "14.382", "-87.621",
    "Hazardous waste storage facility repairs, Soto Cano Air Base, Honduras (USASpending description).",
    "usaspending_eterna_soto_cano_hazwaste_203k_2018",
    "DESIGN AND CONSTRUCTION OF REPAIRS OF HAZARDOUS WASTE STORAGE FACILITY SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0643_9700_W9127816D0102_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (San Pedro Sula) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle998",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0643_9700_W9127816D0102_9700 (Eterna Soto Cano hazwaste). Signed 2018-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0643_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Soto Cano hazwaste USD 0.203m. Supports eterna_soto_cano_hazwaste_203k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 203367.48; date_signed 2018-09-25.",
)

row_doc(
    "misc_tto_metro_e_link_203k_2025",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Trinidad Metro E link to NEC site",
    "Trinidad and Tobago",
    "25 Sep 2025: Department of State awards contract 19TD5525P0443 for OBO P2P Metro E link from chancery to NEC construction site (PoP Trinidad and Tobago); obligated USD 202,766.67. CapEx face = award obligation. Recipient redacted.",
    "202766.67", "2025-09-25", "2025", "10.660", "-61.510",
    "Metro E link from chancery to NEC construction site, Port of Spain, Trinidad and Tobago (USASpending description; approximate).",
    "usaspending_misc_tto_metro_e_link_203k_2025",
    "OBO P2P METRO E LINK FROM CHANCERY TO NEC CONSTRUCTION SITE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5525P0443_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle998",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5525P0443_1900_-NONE-_-NONE- (TTO Metro E link). Signed 2025-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5525P0443_1900_-NONE-_-NONE-/.",
    "USASpending: TTO Metro E link USD 0.203m. Supports misc_tto_metro_e_link_203k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 202766.67; date_signed 2025-09-25.",
)

row_doc(
    "misc_haiti_alt_road_201k_2025",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Haiti alternate road/pathway",
    "Haiti",
    "18 Jun 2025: Department of State awards contract 19HA7025P0645 for alternate road/pathway (PoP Haiti); obligated USD 201,336. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "201336", "2025-06-18", "2025", "", "",
    "Alternate road/pathway, Haiti (USASpending PoP Haiti; site not named — lat/lon blank).",
    "usaspending_misc_haiti_alt_road_201k_2025",
    "ALTERNATE ROAD/PATHWAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7025P0645_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle998",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7025P0645_1900_-NONE-_-NONE- (Haiti alternate road). Signed 2025-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7025P0645_1900_-NONE-_-NONE-/.",
    "USASpending: Haiti alternate road USD 0.201m. Supports misc_haiti_alt_road_201k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 201336; date_signed 2025-06-18.",
)

row_doc(
    "baskerville_salvador_pier_176k_2024",
    "infrastructure", "port_ownership", "us",
    "Baskerville Donovan — El Salvador pier repairs",
    "El Salvador",
    "26 Jan 2024: USACE awards task order W9127824F0032 to Baskerville Donovan for DT-B-HAA pier repairs, El Salvador; obligated USD 176,498.93. CapEx face = award obligation.",
    "176498.93", "2024-01-26", "2024", "", "",
    "Pier repairs, El Salvador (USASpending PoP El Salvador; pier site code DT-B-HAA not geocoded — lat/lon blank).",
    "usaspending_baskerville_salvador_pier_176k_2024",
    "DT-B-HAA PIER REPAIRS, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0032_9700_W9127819D0013_9700/",
    "Actor: Baskerville Donovan Inc. (Mobile AL, U.S.) — us. Official USASpending Award API. Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle998",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0032_9700_W9127819D0013_9700 (Baskerville El Salvador pier). Signed 2024-01-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0032_9700_W9127819D0013_9700/.",
    "USASpending: Baskerville El Salvador pier USD 0.176m. Supports baskerville_salvador_pier_176k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 176498.93; date_signed 2024-01-26.",
)

row_doc(
    "otak_barbados_pier_175k_2012",
    "infrastructure", "port_ownership", "us",
    "Otak Group — Barbados exercise-related pier construction",
    "Barbados",
    "16 Mar 2012: DoD awards task order 0001 under N6945012D0038 to Otak Group for exercise-related construction Barbados pier; obligated USD 174,714. CapEx face = award obligation. Distinct from otak_cdema_barbados_4p01m_2013 (task 0004 CDEMA).",
    "174714", "2012-03-16", "2012", "13.097", "-59.615",
    "Exercise-related pier construction, Barbados (USASpending PoP Barbados; Bridgetown approximate).",
    "usaspending_otak_barbados_pier_175k_2012",
    "EXCERCISE RELATED CONSTRUCTION BARBADOS PIER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_N6945012D0038_9700/",
    "Actor: Otak Group, Inc. (Yulee FL, U.S.) — us. Official USASpending Award API. Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle998",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_N6945012D0038_9700 (Otak Barbados pier). Signed 2012-03-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_N6945012D0038_9700/.",
    "USASpending: Otak Barbados pier USD 0.175m. Supports otak_barbados_pier_175k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 174714; date_signed 2012-03-16.",
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
    print(f"cycles996-998 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
