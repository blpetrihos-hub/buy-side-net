#!/usr/bin/env python3
"""Cycles 966–968: USASpending LatAm CapEx residual (clinics, Soto Cano, materials, fire).

Seeds: 20261966–20261968. Thin top-up dry.
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


# === Cycle 966 ===
row_doc(
    "bonatti_san_marcos_trujillo_clinics_1p22m_2019",
    "infrastructure", "building_materials", "other",
    "Bonatti — San Marcos de Colón clinic renovation + Trujillo HIV facility",
    "Honduras",
    "28 Sep 2019: U.S. Army Corps of Engineers awards task order W9127819F0584 to Bonatti for HAP #37570 clinic renovation San Marcos de Colón and HAP #34876 HIV treatment facility Trujillo; obligated USD 1,220,565.34. CapEx face = award obligation.",
    "1220565.34", "2019-09-28", "2019", "13.433", "-86.800",
    "Clinic renovation San Marcos de Colón / HIV facility Trujillo, Honduras (USASpending PoP Honduras; San Marcos pin).",
    "usaspending_bonatti_san_marcos_trujillo_clinics_1p22m_2019",
    "DESIGN AND CONSTRUCTION OF HAP #37570 CLINIC RENOVATION SAN MARCOS DE COLON, HONDURAS (CADD NO. SBA19005)&HAP #34876 HIV TREATMENT FACILITY TRUJILLO, HONDURAS (CADD NO. SEA19011)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0584_9700_W9127816D0099_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle966",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0584_9700_W9127816D0099_9700 (Bonatti San Marcos/Trujillo clinics). Signed 2019-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0584_9700_W9127816D0099_9700/.",
    "USASpending: Bonatti San Marcos/Trujillo clinics USD 1.221m. Supports bonatti_san_marcos_trujillo_clinics_1p22m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1220565.34; date_signed 2019-09-28.",
)

row_doc(
    "eterna_soto_cano_p03_p04_1p25m_2018",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano P-03 & P-04 design-build renovation",
    "Honduras",
    "13 Sep 2018: U.S. Army Corps of Engineers awards task order W9127818F0513 to Eterna for design-build P-03 & P-04 renovation at Soto Cano; obligated USD 1,253,956.82. CapEx face = award obligation.",
    "1253956.82", "2018-09-13", "2018", "14.382", "-87.621",
    "P-03 & P-04 renovation, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_p03_p04_1p25m_2018",
    "DESIGN-BUILD P-03&P-04 RENO, SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0513_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle966",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0513_9700_W9127816D0102_9700 (Eterna Soto Cano P-03/P-04). Signed 2018-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0513_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Soto Cano P-03/P-04 USD 1.254m. Supports eterna_soto_cano_p03_p04_1p25m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1253956.82; date_signed 2018-09-13.",
)

row_doc(
    "olgoonik_montevideo_materials_1p23m_2026",
    "infrastructure", "building_materials", "us",
    "Olgoonik Innovations — Montevideo embassy construction materials",
    "Uruguay",
    "10 Sep 2026: Department of State awards task order 19AQMM26F1398 to Olgoonik Innovations to purchase construction materials for U.S. Embassy Montevideo; obligated USD 1,230,061. CapEx face = award obligation.",
    "1230061", "2026-09-10", "2026", "-34.901", "-56.164",
    "Construction materials for U.S. Embassy, Montevideo, Uruguay (USASpending PoP Uruguay).",
    "usaspending_olgoonik_montevideo_materials_1p23m_2026",
    "THIS ORDER IS TO PURCHASE CONSTRUCTION MATERIALS FOR THE US EMBASSY AT MONTEVIDEO, URUGUAY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F1398_1900_19AQMM25D0612_1900/",
    "Actor: Olgoonik Innovations (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle966",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM26F1398_1900_19AQMM25D0612_1900 (Olgoonik Montevideo materials). Signed 2026-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F1398_1900_19AQMM25D0612_1900/.",
    "USASpending: Olgoonik Montevideo materials USD 1.230m. Supports olgoonik_montevideo_materials_1p23m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1230061; date_signed 2026-09-10.",
)

row_doc(
    "infraestructuras_peru_steel_towers_1p17m_2012",
    "infrastructure", "power_plants_grid", "other",
    "Infraestructuras S.A.C. — Peru steel towers and WiFi telecommunications",
    "Peru",
    "26 Sep 2012: U.S. Army Corps of Engineers awards contract W912CL12C0022 to Infraestructuras to construct steel towers and add WiFi telecommunications (PoP Peru); obligated USD 1,171,572.54. CapEx face = award obligation.",
    "1171572.54", "2012-09-26", "2012", "-12.046", "-77.043",
    "Steel towers and WiFi telecommunications, Peru (USASpending PoP Peru; Lima pin).",
    "usaspending_infraestructuras_peru_steel_towers_1p17m_2012",
    "CONSTRUCT STEEL TOWERS AND ADD WIFI TELECOMMUNICATIONS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0022_9700_-NONE-_-NONE-/",
    "Actor: Infraestructuras S.A.C. (Peru) — other. Official USASpending Award API. Shuffle power_plants_grid/telecom CapEx.",
    "hunt_cycle966",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL12C0022_9700_-NONE-_-NONE- (Infraestructuras Peru steel towers). Signed 2012-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0022_9700_-NONE-_-NONE-/.",
    "USASpending: Infraestructuras Peru steel towers USD 1.172m. Supports infraestructuras_peru_steel_towers_1p17m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1171572.54; date_signed 2012-09-26.",
)

row_doc(
    "eterna_san_lorenzo_eoc_drw_1p15m_2018",
    "infrastructure", "building_materials", "other",
    "Eterna — San Lorenzo EOC / disaster relief warehouse HAP 32260",
    "Honduras",
    "27 Sep 2018: U.S. Army Corps of Engineers awards task order W9127818F0762 to Eterna for design and construction of HAP 32260 EOC / disaster relief warehouse in San Lorenzo; obligated USD 1,151,055.85. CapEx face = award obligation.",
    "1151055.85", "2018-09-27", "2018", "13.424", "-87.447",
    "EOC / disaster relief warehouse, San Lorenzo, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_san_lorenzo_eoc_drw_1p15m_2018",
    "TASK ORDER FOR DESIGN AND CONSTRUCTION FOR HAP 32260 EMERGENCY OPERATION CENTER (EOC) / DISASTER RELIEF WAREHOUSE (DRW), IN SAN LORENZO, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0762_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle966",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0762_9700_W9127816D0102_9700 (Eterna San Lorenzo EOC/DRW). Signed 2018-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0762_9700_W9127816D0102_9700/.",
    "USASpending: Eterna San Lorenzo EOC/DRW USD 1.151m. Supports eterna_san_lorenzo_eoc_drw_1p15m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1151055.85; date_signed 2018-09-27.",
)

# === Cycle 967 ===
row_doc(
    "marago_siart_cenop_1p14m_2024",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — CNP SIART CENOP construction",
    "Colombia",
    "3 Sep 2024: Department of State awards task order 19AQMM24F1768 to Constructora Marago for CNP SIART CENOP construction; obligated USD 1,141,211.91. CapEx face = award obligation.",
    "1141211.91", "2024-09-03", "2024", "4.624", "-74.065",
    "CNP SIART CENOP construction, Colombia (USASpending PoP Colombia; Bogotá pin).",
    "usaspending_marago_siart_cenop_1p14m_2024",
    "CNP SIART CENOP CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1768_1900_19AQMM21D0036_1900/",
    "Actor: Constructora Marago (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle967",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F1768_1900_19AQMM21D0036_1900 (Marago SIART CENOP). Signed 2024-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1768_1900_19AQMM21D0036_1900/.",
    "USASpending: Marago SIART CENOP USD 1.141m. Supports marago_siart_cenop_1p14m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1141211.91; date_signed 2024-09-03.",
)

row_doc(
    "eterna_narino_fire_station_1p13m_2024",
    "infrastructure", "building_materials", "other",
    "Eterna — Nariño fire station",
    "Colombia",
    "20 May 2024: U.S. Army Corps of Engineers awards task order W9127824F0099 to Eterna for design and construction of fire station in Nariño; obligated USD 1,129,995.28. CapEx face = award obligation.",
    "1129995.28", "2024-05-20", "2024", "1.213", "-77.278",
    "Fire station, Nariño, Colombia (USASpending PoP Colombia; Pasto-area pin).",
    "usaspending_eterna_narino_fire_station_1p13m_2024",
    "DESIGN AND CONSTRUCTION OF FIRE STATION IN NARINO, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0099_9700_W9127823D0059_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle967",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0099_9700_W9127823D0059_9700 (Eterna Nariño fire station). Signed 2024-05-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0099_9700_W9127823D0059_9700/.",
    "USASpending: Eterna Nariño fire station USD 1.130m. Supports eterna_narino_fire_station_1p13m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1129995.28; date_signed 2024-05-20.",
)

row_doc(
    "eterna_soto_cano_roof_1p11m_2020",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano roof repairs",
    "Honduras",
    "29 Sep 2020: U.S. Army Corps of Engineers awards task order W9127820F0543 to Eterna for roof repairs at Soto Cano; obligated USD 1,109,306.20. CapEx face = award obligation.",
    "1109306.20", "2020-09-29", "2020", "14.382", "-87.621",
    "Roof repairs, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_roof_1p11m_2020",
    "ROOF REPAIRS AT SOTO CANO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0543_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle967",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0543_9700_W9127816D0102_9700 (Eterna Soto Cano roof). Signed 2020-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0543_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Soto Cano roof USD 1.109m. Supports eterna_soto_cano_roof_1p11m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1109306.20; date_signed 2020-09-29.",
)

row_doc(
    "eterna_copeco_santa_barbara_1p08m_2022",
    "infrastructure", "building_materials", "other",
    "Eterna — COPECO warehouse HAP #67612 Santa Bárbara",
    "Honduras",
    "22 Sep 2022: U.S. Army Corps of Engineers awards task order W9127822F0364 to Eterna for design/build HAP #67612 COPECO warehouse, Santa Bárbara; obligated USD 1,076,533.59. CapEx face = award obligation.",
    "1076533.59", "2022-09-22", "2022", "14.917", "-88.233",
    "COPECO warehouse, Santa Bárbara, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_copeco_santa_barbara_1p08m_2022",
    "D/B HAP #67612 COPECO WAREHOUSE, SANTA BARBARA, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0364_9700_W9127821D0075_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle967",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0364_9700_W9127821D0075_9700 (Eterna COPECO Santa Bárbara). Signed 2022-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0364_9700_W9127821D0075_9700/.",
    "USASpending: Eterna COPECO Santa Bárbara USD 1.077m. Supports eterna_copeco_santa_barbara_1p08m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1076533.59; date_signed 2022-09-22.",
)

row_doc(
    "kuk_suriname_post_security_1p14m_2005",
    "infrastructure", "building_materials", "us",
    "KUK/KBRS Global — Suriname overseas post security areas construction",
    "Suriname",
    "23 Aug 2005: Department of State awards order SALMEC02D0051O104 to KUK/KBRS Global for construction of overseas post security areas (PoP Suriname); obligated USD 1,136,000. CapEx face = award obligation.",
    "1136000", "2005-08-23", "2005", "5.852", "-55.204",
    "Overseas post security areas, Suriname (USASpending PoP Suriname; Paramaribo pin).",
    "usaspending_kuk_suriname_post_security_1p14m_2005",
    "CONSTRUCTION OF OVERSEAS POST SECURITY AREAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC02D0051O104_1900_SALMEC02D0051_1900/",
    "Actor: KUK/KBRS Global (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle967",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SALMEC02D0051O104_1900_SALMEC02D0051_1900 (KUK Suriname post security). Signed 2005-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC02D0051O104_1900_SALMEC02D0051_1900/.",
    "USASpending: KUK Suriname post security USD 1.136m. Supports kuk_suriname_post_security_1p14m_2005.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1136000; date_signed 2005-08-23.",
)

# === Cycle 968 ===
row_doc(
    "bonatti_soto_cano_aob_8mile_1p06m_2019",
    "infrastructure", "building_materials", "other",
    "Bonatti — Soto Cano emergent AOB 8 Mile facility",
    "Honduras",
    "24 May 2019: U.S. Army Corps of Engineers awards task order W9127819F0219 to Bonatti for design and construction of emergent AOB 8 Mile facility at Soto Cano; obligated USD 1,062,328.50. CapEx face = award obligation.",
    "1062328.50", "2019-05-24", "2019", "14.382", "-87.621",
    "Emergent AOB 8 Mile facility, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_bonatti_soto_cano_aob_8mile_1p06m_2019",
    "DESIGN AND CONSTRUCTION OF EMERGENT AOB 8 MILE FACILITY, SOTO CANO AIR BARSE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0219_9700_W9127816D0099_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle968",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0219_9700_W9127816D0099_9700 (Bonatti Soto Cano AOB 8 Mile). Signed 2019-05-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0219_9700_W9127816D0099_9700/.",
    "USASpending: Bonatti Soto Cano AOB 8 Mile USD 1.062m. Supports bonatti_soto_cano_aob_8mile_1p06m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1062328.50; date_signed 2019-05-24.",
)

row_doc(
    "eterna_soto_cano_12plex_1p06m_2019",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano 12-plex housing design/build",
    "Honduras",
    "8 Aug 2019: U.S. Army Corps of Engineers awards task order W9127819F0312 to Eterna for design/build and construction of 12-plex housing at Soto Cano; obligated USD 1,060,581.96. CapEx face = award obligation.",
    "1060581.96", "2019-08-08", "2019", "14.382", "-87.621",
    "12-plex housing, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_12plex_1p06m_2019",
    "THE PURPOSE OF THIS TASK ORDER IS FOR THE DESIGN/ BUILD AND  CONSTRUCTION OF 12 PLEX HOUSING AT SOTO CANO AIR BASE, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0312_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle968",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0312_9700_W9127816D0102_9700 (Eterna Soto Cano 12-plex). Signed 2019-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0312_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Soto Cano 12-plex USD 1.061m. Supports eterna_soto_cano_12plex_1p06m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1060581.96; date_signed 2019-08-08.",
)

row_doc(
    "eterna_scab_road_phase3_1p06m_2022",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Soto Cano Air Base road repairs Phase III",
    "Honduras",
    "27 Sep 2022: U.S. Army Corps of Engineers awards task order W9127822F0402 to Eterna for design and construction of road repairs Phase III, SCAB; obligated USD 1,059,215.01. CapEx face = award obligation.",
    "1059215.01", "2022-09-27", "2022", "14.382", "-87.621",
    "Road repairs Phase III, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_scab_road_phase3_1p06m_2022",
    "DESIGN AND CONSTRUCTION OF ROAD REPAIRS PHASE III, SCAB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0402_9700_W9127821D0075_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle968",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0402_9700_W9127821D0075_9700 (Eterna SCAB road Phase III). Signed 2022-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0402_9700_W9127821D0075_9700/.",
    "USASpending: Eterna SCAB road Phase III USD 1.059m. Supports eterna_scab_road_phase3_1p06m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1059215.01; date_signed 2022-09-27.",
)

row_doc(
    "castillo_dr_erc_barracks_1p04m_2023",
    "infrastructure", "building_materials", "other",
    "Construcciones Castillo Fernández — Dominican Republic ERC barracks design/build",
    "Dominican Republic",
    "2 Aug 2023: Department of the Navy awards contract N6945023C0027 to Construcciones Castillo Fernández for design/build ERC barracks in Dominican Republic; obligated USD 1,038,310. CapEx face = award obligation.",
    "1038310", "2023-08-02", "2023", "18.486", "-69.931",
    "ERC barracks design/build, Dominican Republic (USASpending PoP Dominican Republic; Santo Domingo pin).",
    "usaspending_castillo_dr_erc_barracks_1p04m_2023",
    "DB ERC BARRACKS AT DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945023C0027_9700_-NONE-_-NONE-/",
    "Actor: Construcciones Castillo Fernández (Dominican Republic) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle968",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945023C0027_9700_-NONE-_-NONE- (Castillo DR ERC barracks). Signed 2023-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945023C0027_9700_-NONE-_-NONE-/.",
    "USASpending: Castillo DR ERC barracks USD 1.038m. Supports castillo_dr_erc_barracks_1p04m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1038310; date_signed 2023-08-02.",
)

row_doc(
    "eterna_isla_gallinazo_clinic_1p02m_2021",
    "infrastructure", "building_materials", "other",
    "Eterna — Isla El Gallinazo clinic repair HAP #39537",
    "Colombia",
    "16 Jun 2021: U.S. Army Corps of Engineers awards task order W9127821F0204 to Eterna for design and construction of HAP #39537 clinic repair Isla El Gallinazo, Sucre; obligated USD 1,017,379.55. CapEx face = award obligation.",
    "1017379.55", "2021-06-16", "2021", "9.550", "-75.580",
    "Clinic repair, Isla El Gallinazo, Sucre, Colombia (USASpending PoP Colombia).",
    "usaspending_eterna_isla_gallinazo_clinic_1p02m_2021",
    "DESIGN AND CONSTRUCTION OF HAP #39537 CLINIC REPAIR ISLA EL GALLINAZO, SUCRE, COLOMBIA (CADD NO. SEA19013)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0204_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle968",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0204_9700_W9127817D0095_9700 (Eterna Isla El Gallinazo clinic). Signed 2021-06-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0204_9700_W9127817D0095_9700/.",
    "USASpending: Eterna Isla El Gallinazo clinic USD 1.017m. Supports eterna_isla_gallinazo_clinic_1p02m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1017379.55; date_signed 2021-06-16.",
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
    print(f"cycles966-968 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
