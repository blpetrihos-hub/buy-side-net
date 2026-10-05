#!/usr/bin/env python3
"""Cycles 1011–1013: USASpending LatAm CapEx residual (~USD0.11–0.14m).

Seeds: 20262011–20262013. Thin top-up dry.
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

# === Cycle 1011 ===
row_doc(
    "york_panama_chiller_143k_2014",
    "infrastructure", "building_materials", "us",
    "York International — Panama NEC chiller #2 compressor replacement",
    "Panama",
    "18 Aug 2014: DoD awards contract SPM07014M0677 to York International for major repair replace compressor chiller#2-NEC (PoP Panama); obligated USD 142,545.35. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "142545.35", "2014-08-18", "2014", "", "",
    "NEC chiller #2 compressor replacement, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_york_panama_chiller_143k_2014",
    "MAJOR REPAIR REPLACE COMPRESSOR CHILLER#2-NEC - URGENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0677_1900_-NONE-_-NONE-/",
    "Actor: York International Corporation (Pennsylvania, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1011",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07014M0677_1900_-NONE-_-NONE- (York Panama chiller). Signed 2014-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0677_1900_-NONE-_-NONE-/.",
    "USASpending: York Panama chiller USD 0.143m. Supports york_panama_chiller_143k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 142545.35; date_signed 2014-08-18.",
)

row_doc(
    "egarco_ecuador_asphalt_142k_2020",
    "infrastructure", "bridges_roads", "other",
    "Egarco — Ecuador asphalt interior repair",
    "Ecuador",
    "8 Sep 2020: Department of State awards contract 19EC7520P1039 to Egarco Egas Arguello for asphalt interior repair (PoP Ecuador); obligated USD 142,352. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "142352", "2020-09-08", "2020", "", "",
    "Asphalt interior repair, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_egarco_ecuador_asphalt_142k_2020",
    "1901.0-PR9287715-ASPHALT INTERIOR REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7520P1039_1900_-NONE-_-NONE-/",
    "Actor: Egarco Egas Arguello Cía. Ltda. (Ecuador) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1011",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7520P1039_1900_-NONE-_-NONE- (Egarco Ecuador asphalt). Signed 2020-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7520P1039_1900_-NONE-_-NONE-/.",
    "USASpending: Egarco Ecuador asphalt USD 0.142m. Supports egarco_ecuador_asphalt_142k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 142352; date_signed 2020-09-08.",
)

row_doc(
    "misc_argentina_ada_entrance_141k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina CMR ADA entrance construction",
    "Argentina",
    "30 Sep 2016: Department of State awards contract SAR20016M0864 for FM/CMR ADA entrance construction (PoP Argentina); obligated USD 140,947.26. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "140947.26", "2016-09-30", "2016", "", "",
    "CMR ADA entrance construction, Argentina (USASpending PoP Argentina; site not named — lat/lon blank).",
    "usaspending_misc_argentina_ada_entrance_141k_2016",
    "FM/CMR - ADA ENTRANCE CONSTRUCTION IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20016M0864_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1011",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20016M0864_1900_-NONE-_-NONE- (Argentina ADA entrance). Signed 2016-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20016M0864_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina ADA entrance USD 0.141m. Supports misc_argentina_ada_entrance_141k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 140947.26; date_signed 2016-09-30.",
)

row_doc(
    "misc_ecuador_asphalt_139k_2019",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Ecuador asphalt milling and resurfacing",
    "Ecuador",
    "5 Jul 2019: Department of State awards contract 19EC7519P0540 for asphalt milling and resurfacing project (PoP Ecuador); obligated USD 139,471.20. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "139471.20", "2019-07-05", "2019", "", "",
    "Asphalt milling and resurfacing, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_asphalt_139k_2019",
    "7901-PR8163931-ASPHALT MILLING&RESURFACING PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7519P0540_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1011",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7519P0540_1900_-NONE-_-NONE- (Ecuador asphalt resurfacing). Signed 2019-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7519P0540_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador asphalt resurfacing USD 0.139m. Supports misc_ecuador_asphalt_139k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 139471.20; date_signed 2019-07-05.",
)

row_doc(
    "misc_guyana_cmr_roof_139k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guyana CMR roof repairs",
    "Guyana",
    "25 Nov 2014: Department of State awards contract SGY20015M0048 for FAC CMR roof repairs (PoP Guyana); obligated USD 138,860.23. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "138860.23", "2014-11-25", "2014", "", "",
    "CMR roof repairs, Guyana (USASpending PoP Guyana; site not named — lat/lon blank).",
    "usaspending_misc_guyana_cmr_roof_139k_2014",
    "IGF::CL::IGF  FAC - CMR ROOF REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0048_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1011",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20015M0048_1900_-NONE-_-NONE- (Guyana CMR roof). Signed 2014-11-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0048_1900_-NONE-_-NONE-/.",
    "USASpending: Guyana CMR roof USD 0.139m. Supports misc_guyana_cmr_roof_139k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 138860.23; date_signed 2014-11-25.",
)


# === Cycle 1012 ===
row_doc(
    "contemporary_guyana_fence_136k_2025",
    "infrastructure", "building_materials", "other",
    "Contemporary Engineering — Guyana fence extension",
    "Guyana",
    "18 Dec 2025: Department of State awards contract 19GY2026C0001 to Contemporary Engineering and Construction for fence extension project (PoP Guyana); obligated USD 136,278.28. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "136278.28", "2025-12-18", "2025", "", "",
    "Fence extension, Guyana (USASpending PoP Guyana; site not named — lat/lon blank).",
    "usaspending_contemporary_guyana_fence_136k_2025",
    "FENCE EXTENSION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2026C0001_1900_-NONE-_-NONE-/",
    "Actor: Contemporary Engineering and Construction (Guyana) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1012",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2026C0001_1900_-NONE-_-NONE- (Contemporary Guyana fence). Signed 2025-12-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2026C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Contemporary Guyana fence USD 0.136m. Supports contemporary_guyana_fence_136k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 136278.28; date_signed 2025-12-18.",
)

row_doc(
    "misc_cr_vet_clinic_mv_133k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica MJP vet clinic medium voltage",
    "Costa Rica",
    "28 Feb 2023: Department of State awards contract 19CS8023P0376 for INL medium voltage for 2023 MJP vet clinic project (PoP Costa Rica); obligated USD 133,095.13. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "133095.13", "2023-02-28", "2023", "", "",
    "Medium-voltage works for MJP vet clinic, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_misc_cr_vet_clinic_mv_133k_2023",
    "INL 1930.0 MEDIUM VOLTAGE, 2023 MJP VET. CLINIC PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8023P0376_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1012",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8023P0376_1900_-NONE-_-NONE- (CR vet clinic MV). Signed 2023-02-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8023P0376_1900_-NONE-_-NONE-/.",
    "USASpending: CR vet clinic MV USD 0.133m. Supports misc_cr_vet_clinic_mv_133k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 133095.13; date_signed 2023-02-28.",
)

row_doc(
    "medina_belize_roof_132k_2017",
    "infrastructure", "building_materials", "other",
    "Medina's Construction — Belize roof and truss system",
    "Belize",
    "13 Apr 2017: DoD awards contract W912CL17P0730 to Medina's Construction for G3/BTH BLZ 2017 roof and truss system (PoP Belize); obligated USD 132,361.54. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "132361.54", "2017-04-13", "2017", "", "",
    "Roof and truss system, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_medina_belize_roof_132k_2017",
    "IGF::OT::IGF /G3/BTH BLZ 2017 ROOF AND TRUSS SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17P0730_9700_-NONE-_-NONE-/",
    "Actor: Medina's Construction Limited (Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1012",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17P0730_9700_-NONE-_-NONE- (Medina Belize roof). Signed 2017-04-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17P0730_9700_-NONE-_-NONE-/.",
    "USASpending: Medina Belize roof USD 0.132m. Supports medina_belize_roof_132k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 132361.54; date_signed 2017-04-13.",
)

row_doc(
    "misc_murcielago_transformer_130k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Murciélago men barracks electric transformer",
    "Costa Rica",
    "21 Dec 2018: Department of State awards contract 19CS8019P0171 for INL electric transformer system for Murciélago men barracks (PoP Costa Rica); obligated USD 130,150.07. CapEx face = award obligation. Recipient redacted.",
    "130150.07", "2018-12-21", "2018", "10.790", "-85.670",
    "Electric transformer system, Murciélago men barracks, Costa Rica (USASpending description; Guanacaste approximate).",
    "usaspending_misc_murcielago_transformer_130k_2018",
    "PR7887646-V2 - INL 1930.0 ELECTRIC TRANSF. SYST. FOR MURCIELAGO MEN BARRACK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019P0171_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1012",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8019P0171_1900_-NONE-_-NONE- (Murciélago transformer). Signed 2018-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019P0171_1900_-NONE-_-NONE-/.",
    "USASpending: Murciélago transformer USD 0.130m. Supports misc_murcielago_transformer_130k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 130150.07; date_signed 2018-12-21.",
)

row_doc(
    "davalos_vista_alegre_sniper_124k_2026",
    "infrastructure", "building_materials", "other",
    "Dávalos Ayala — Vista Alegre sniper tower Paraguay",
    "Paraguay",
    "11 May 2026: DoD awards contract H9228126CE004 to Edgar Damian Dávalos Ayala for construction of a sniper tower structure on Vista Alegre, Paraguay; obligated USD 124,026.21. CapEx face = award obligation.",
    "124026.21", "2026-05-11", "2026", "-25.300", "-57.580",
    "Sniper tower, Vista Alegre, Paraguay (USASpending description; Asunción-area approximate).",
    "usaspending_davalos_vista_alegre_sniper_124k_2026",
    "CONSTRUCTION OF A SNIPER TOWER STRUCTURE ON VISTA ALEGRE, PARAGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228126CE004_9700_-NONE-_-NONE-/",
    "Actor: Edgar Damian Dávalos Ayala (Paraguay) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1012",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228126CE004_9700_-NONE-_-NONE- (Dávalos Vista Alegre sniper). Signed 2026-05-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228126CE004_9700_-NONE-_-NONE-/.",
    "USASpending: Dávalos Vista Alegre sniper USD 0.124m. Supports davalos_vista_alegre_sniper_124k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 124026.21; date_signed 2026-05-11.",
)


# === Cycle 1013 ===
row_doc(
    "ricketts_jcf_shed_124k_2016",
    "infrastructure", "building_materials", "other",
    "Garnet Ricketts — JCF Marine Police shed Jamaica",
    "Jamaica",
    "13 Apr 2016: Department of State awards contract SJM37016C0001 to Garnet Adolphus Ricketts for INL shed construction Marine Police JCF (PoP Jamaica); obligated USD 123,745.03. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "123745.03", "2016-04-13", "2016", "", "",
    "Marine Police JCF shed construction, Jamaica (USASpending PoP Jamaica; site not named — lat/lon blank).",
    "usaspending_ricketts_jcf_shed_124k_2016",
    "IGF::OT::IGF INL - SHED CONSTRUCTION MARINE POLICE JCF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016C0001_1900_-NONE-_-NONE-/",
    "Actor: Garnet Adolphus Ricketts (Jamaica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1013",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37016C0001_1900_-NONE-_-NONE- (Ricketts JCF shed). Signed 2016-04-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Ricketts JCF shed USD 0.124m. Supports ricketts_jcf_shed_124k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 123745.03; date_signed 2016-04-13.",
)

row_doc(
    "misc_nicaragua_casa_grande_road_124k_2013",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Nicaragua Casa Grande road resurfacing",
    "Nicaragua",
    "30 Sep 2013: Department of State awards contract SNU70013M0350 for road resurfacing Casa Grande (PoP Nicaragua); obligated USD 123,628.92. CapEx face = award obligation. Recipient redacted.",
    "123628.92", "2013-09-30", "2013", "12.140", "-86.250",
    "Road resurfacing, Casa Grande, Nicaragua (USASpending description; Managua-area approximate).",
    "usaspending_misc_nicaragua_casa_grande_road_124k_2013",
    "ROAD RESURFACING - CASA GRANDE  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70013M0350_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads; Nicaragua under-covered.",
    "hunt_cycle1013",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70013M0350_1900_-NONE-_-NONE- (Nicaragua Casa Grande road). Signed 2013-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70013M0350_1900_-NONE-_-NONE-/.",
    "USASpending: Nicaragua Casa Grande road USD 0.124m. Supports misc_nicaragua_casa_grande_road_124k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 123628.92; date_signed 2013-09-30.",
)

row_doc(
    "nobelcons_helipad_121k_2011",
    "infrastructure", "building_materials", "other",
    "Nobelcons — Santa Barbara helicopter pad Ecuador",
    "Ecuador",
    "22 Sep 2011: DoD awards contract W9127811P0329 to Nobelcons Nobelconstrucciones for construction with incidental design of helicopter pad Santa Barbara, Ecuador; obligated USD 120,566.28. CapEx face = award obligation.",
    "120566.28", "2011-09-22", "2011", "-1.630", "-79.560",
    "Helicopter pad, Santa Barbara, Ecuador (USASpending description; Los Ríos approximate).",
    "usaspending_nobelcons_helipad_121k_2011",
    "TAS::21 2020::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF HELICOPTER PAD SANTA BARBRA, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0329_9700_-NONE-_-NONE-/",
    "Actor: Nobelcons Nobelconstrucciones Cía. Ltda. (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1013",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0329_9700_-NONE-_-NONE- (Nobelcons helipad). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0329_9700_-NONE-_-NONE-/.",
    "USASpending: Nobelcons helipad USD 0.121m. Supports nobelcons_helipad_121k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 120566.28; date_signed 2011-09-22.",
)

row_doc(
    "goberdan_dalli_boat_ramp_117k_2011",
    "infrastructure", "port_ownership", "other",
    "Goberdan's Construction — Dalli boat ramp and floating docks Guyana",
    "Guyana",
    "30 Sep 2011: DoD awards contract W9127811P0343 to Goberdan's Construction for boat ramp and floating docks, Dalli, Guyana; obligated USD 116,835. CapEx face = award obligation.",
    "116835", "2011-09-30", "2011", "5.980", "-58.560",
    "Boat ramp and floating docks, Dalli, Guyana (USASpending description; Essequibo approximate).",
    "usaspending_goberdan_dalli_boat_ramp_117k_2011",
    "TAS::21 2020::TAS BOAT RAMP AND FLOATING DOCKS, DALLI, GUYANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0343_9700_-NONE-_-NONE-/",
    "Actor: Goberdan's Construction (Guyana) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle1013",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0343_9700_-NONE-_-NONE- (Goberdan Dalli boat ramp). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0343_9700_-NONE-_-NONE-/.",
    "USASpending: Goberdan Dalli boat ramp USD 0.117m. Supports goberdan_dalli_boat_ramp_117k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 116835; date_signed 2011-09-30.",
)

row_doc(
    "hcs_salvador_ground_support_115k_2016",
    "infrastructure", "building_materials", "us",
    "HCS Group — El Salvador SOFA P8 ground support facility",
    "El Salvador",
    "29 Sep 2016: USACE awards task order 0011 under W9127814D0057 to HCS Group for SOFA Agreement P8 ground support facility (PoP El Salvador); obligated USD 115,027.10. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "115027.10", "2016-09-29", "2016", "", "",
    "SOFA P8 ground support facility, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_hcs_salvador_ground_support_115k_2016",
    "IGF::OT::IGF SOFA AGREEMENT P8 GROUND SUPPORT FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127814D0057_9700/",
    "Actor: HCS Group, P.C. (Montgomery AL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1013",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127814D0057_9700 (HCS El Salvador ground support). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127814D0057_9700/.",
    "USASpending: HCS El Salvador ground support USD 0.115m. Supports hcs_salvador_ground_support_115k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 115027.10; date_signed 2016-09-29.",
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
    print(f"cycles1011-1013 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
