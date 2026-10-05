#!/usr/bin/env python3
"""Cycles 969–971: USASpending LatAm CapEx residual (~USD0.9–1.15m).

Seeds: 20261969–20261971. Thin top-up dry.
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


# === Cycle 969 ===
row_doc(
    "eterna_soto_cano_india_apron_1p04m_2024",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Soto Cano India apron repairs",
    "Honduras",
    "26 Sep 2024: U.S. Army Corps of Engineers awards task order W9127824F0368 to Eterna for design and construction of India apron repairs at Soto Cano Air Base; obligated USD 1,040,279.92. CapEx face = award obligation.",
    "1040279.92", "2024-09-26", "2024", "14.382", "-87.621",
    "India apron repairs, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_india_apron_1p04m_2024",
    "DESIGN AND CONSTRUCTION OF INDIA APRON REPAIRS, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0368_9700_W9127823D0073_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle bridges_roads/airside CapEx.",
    "hunt_cycle969",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0368_9700_W9127823D0073_9700 (Eterna Soto Cano India apron). Signed 2024-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0368_9700_W9127823D0073_9700/.",
    "USASpending: Eterna Soto Cano India apron USD 1.040m. Supports eterna_soto_cano_india_apron_1p04m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1040279.92; date_signed 2024-09-26.",
)

row_doc(
    "seobra_colombia_2story_school_1p06m_2017",
    "infrastructure", "building_materials", "other",
    "Seobra — Colombia 2-story school building",
    "Colombia",
    "21 Sep 2017: U.S. Army Corps of Engineers awards contract W912CL17C0006 to Seobra for construction of a 2-story school building (PoP Colombia); obligated USD 1,056,740.20. CapEx face = award obligation.",
    "1056740.20", "2017-09-21", "2017", "", "",
    "2-story school building, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_seobra_colombia_2story_school_1p06m_2017",
    "IGF::OT::IGF CONSTRUCTION OF A 2-STORY SCHOOL BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0006_9700_-NONE-_-NONE-/",
    "Actor: Seobra (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle969",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17C0006_9700_-NONE-_-NONE- (Seobra Colombia 2-story school). Signed 2017-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0006_9700_-NONE-_-NONE-/.",
    "USASpending: Seobra Colombia 2-story school USD 1.057m. Supports seobra_colombia_2story_school_1p06m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1056740.20; date_signed 2017-09-21.",
)

row_doc(
    "kuk_peru_post_security_1p09m_2006",
    "infrastructure", "building_materials", "us",
    "KUK/KBRS Global — Peru overseas post security areas construction",
    "Peru",
    "16 Jun 2006: Department of State awards order SALMEC02D0051O121 to KUK/KBRS Global for construction of overseas post security areas (PoP Peru); obligated USD 1,093,987.16. CapEx face = award obligation.",
    "1093987.16", "2006-06-16", "2006", "-12.046", "-77.043",
    "Overseas post security areas, Peru (USASpending PoP Peru; Lima pin).",
    "usaspending_kuk_peru_post_security_1p09m_2006",
    "CONSTRUCTION OF OVERSEAS POST SECURITY AREAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC02D0051O121_1900_SALMEC02D0051_1900/",
    "Actor: KUK/KBRS Global (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle969",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SALMEC02D0051O121_1900_SALMEC02D0051_1900 (KUK Peru post security). Signed 2006-06-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC02D0051O121_1900_SALMEC02D0051_1900/.",
    "USASpending: KUK Peru post security USD 1.094m. Supports kuk_peru_post_security_1p09m_2006.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1093987.16; date_signed 2006-06-16.",
)

row_doc(
    "seobra_hap42189_school_1p04m_2022",
    "infrastructure", "building_materials", "other",
    "Seobra — HAP #42189 school base bid",
    "Colombia",
    "28 Sep 2022: U.S. Army Corps of Engineers awards task order W9127822F0436 to Seobra for HAP #42189 base bid school; obligated USD 1,039,255. CapEx face = award obligation.",
    "1039255", "2022-09-28", "2022", "", "",
    "HAP #42189 school, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_seobra_hap42189_school_1p04m_2022",
    "HAP #42189, BASE BID, SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0436_9700_W9127817D0097_9700/",
    "Actor: Seobra (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle969",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0436_9700_W9127817D0097_9700 (Seobra HAP #42189 school). Signed 2022-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0436_9700_W9127817D0097_9700/.",
    "USASpending: Seobra HAP #42189 school USD 1.039m. Supports seobra_hap42189_school_1p04m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1039255; date_signed 2022-09-28.",
)

row_doc(
    "eterna_hap42212_school_1p01m_2022",
    "infrastructure", "building_materials", "other",
    "Eterna — HAP #42212 school base bid",
    "Colombia",
    "28 Sep 2022: U.S. Army Corps of Engineers awards task order W9127822F0439 to Eterna for HAP #42212 base bid school; obligated USD 1,005,825.24. CapEx face = award obligation.",
    "1005825.24", "2022-09-28", "2022", "", "",
    "HAP #42212 school, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_eterna_hap42212_school_1p01m_2022",
    "HAP #42212, BASE BID, SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0439_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle969",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0439_9700_W9127817D0095_9700 (Eterna HAP #42212 school). Signed 2022-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0439_9700_W9127817D0095_9700/.",
    "USASpending: Eterna HAP #42212 school USD 1.006m. Supports eterna_hap42212_school_1p01m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1005825.24; date_signed 2022-09-28.",
)

# === Cycle 970 ===
row_doc(
    "eterna_soto_cano_warehouse_r71_r73_999k_2025",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano warehouse R71 and R73 renovation",
    "Honduras",
    "28 Sep 2025: U.S. Army Corps of Engineers awards task order W9127825FA297 to Eterna for renovation of warehouses R71 and R73 at Soto Cano; obligated USD 999,197.91. CapEx face = award obligation.",
    "999197.91", "2025-09-28", "2025", "14.382", "-87.621",
    "Warehouse R71/R73 renovation, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_warehouse_r71_r73_999k_2025",
    "RENOVATION WAREHOUSE R71 AND R73 IN SOTO CANO AIR BASE, HONDURAS. THE TASK WILL BE PE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA297_9700_W9127823D0073_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle970",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA297_9700_W9127823D0073_9700 (Eterna Soto Cano R71/R73). Signed 2025-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA297_9700_W9127823D0073_9700/.",
    "USASpending: Eterna Soto Cano R71/R73 USD 0.999m. Supports eterna_soto_cano_warehouse_r71_r73_999k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 999197.91; date_signed 2025-09-28.",
)

row_doc(
    "venturia_bolivia_elevator_987k_2026",
    "infrastructure", "building_materials", "other",
    "Venturia — Bolivia design/build elevator replacement",
    "Bolivia",
    "10 Sep 2026: Department of State awards purchase 19GE5026P0015 to Venturia for design/build elevator replacement (PoP Bolivia); obligated USD 986,800. CapEx face = award obligation.",
    "986800", "2026-09-10", "2026", "-16.500", "-68.150",
    "Elevator replacement, Bolivia (USASpending PoP Bolivia; La Paz pin).",
    "usaspending_venturia_bolivia_elevator_987k_2026",
    "DESIGN/BUILD ELEVATOR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026P0015_1900_-NONE-_-NONE-/",
    "Actor: Venturia (Slovenia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle970",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026P0015_1900_-NONE-_-NONE- (Venturia Bolivia elevator). Signed 2026-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026P0015_1900_-NONE-_-NONE-/.",
    "USASpending: Venturia Bolivia elevator USD 0.987m. Supports venturia_bolivia_elevator_987k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 986800; date_signed 2026-09-10.",
)

row_doc(
    "bonatti_comalapa_apron_984k_2024",
    "infrastructure", "bridges_roads", "other",
    "Bonatti — CSL Comalapa apron shoulder repair",
    "El Salvador",
    "27 Sep 2024: U.S. Army Corps of Engineers awards task order W9127824F0386 to Bonatti for design and construction of apron shoulder repair at CSL Comalapa; obligated USD 983,513.79. CapEx face = award obligation.",
    "983513.79", "2024-09-27", "2024", "13.440", "-89.056",
    "Apron shoulder repair, CSL Comalapa, El Salvador (USASpending PoP El Salvador).",
    "usaspending_bonatti_comalapa_apron_984k_2024",
    "DESIGN AND CONSTRUCTION OF APRON SHOULDER REPAIR AT CSL COMALAPA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0386_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle bridges_roads/airside CapEx.",
    "hunt_cycle970",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0386_9700_W9127823D0072_9700 (Bonatti Comalapa apron). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0386_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Comalapa apron USD 0.984m. Supports bonatti_comalapa_apron_984k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 983513.79; date_signed 2024-09-27.",
)

row_doc(
    "tecpro_soto_cano_12plex_p2_973k_2019",
    "infrastructure", "building_materials", "other",
    "Tecnología de Proyectos — Soto Cano 12-plex housing Phase II",
    "Honduras",
    "24 Sep 2019: U.S. Army Corps of Engineers awards task order W9127819F0493 to Tecnología de Proyectos to design, build and construct 12-plex housing Phase II at Soto Cano; obligated USD 972,927.22. CapEx face = award obligation. Distinct from eterna_soto_cano_12plex.",
    "972927.22", "2019-09-24", "2019", "14.382", "-87.621",
    "12-plex housing Phase II, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_tecpro_soto_cano_12plex_p2_973k_2019",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN, BUILD AND CONSTRUCT 12 PLEX HOUSING, PHA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0493_9700_W9127816D0103_9700/",
    "Actor: Tecnología de Proyectos (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle970",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0493_9700_W9127816D0103_9700 (TecPro Soto Cano 12-plex Phase II). Signed 2019-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0493_9700_W9127816D0103_9700/.",
    "USASpending: TecPro Soto Cano 12-plex Phase II USD 0.973m. Supports tecpro_soto_cano_12plex_p2_973k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 972927.22; date_signed 2019-09-24.",
)

row_doc(
    "seobra_tres_esquinas_health_957k_2021",
    "infrastructure", "building_materials", "other",
    "Seobra — Tres Esquinas health center HAP #39683",
    "Colombia",
    "16 Jun 2021: U.S. Army Corps of Engineers awards task order W9127821F0205 to Seobra for design and construction of HAP #39683 health center Tres Esquinas, Solano; obligated USD 957,171.38. CapEx face = award obligation.",
    "957171.38", "2021-06-16", "2021", "0.745", "-75.260",
    "Health center HAP #39683, Tres Esquinas, Solano, Colombia (USASpending PoP Colombia).",
    "usaspending_seobra_tres_esquinas_health_957k_2021",
    "DESIGN AND CONSTRUCTION OF HAP #39683 HEALTH CENTER TRES ESQUINAS, SOLANO, COLOMBIA (",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0205_9700_W9127817D0097_9700/",
    "Actor: Seobra (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle970",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0205_9700_W9127817D0097_9700 (Seobra Tres Esquinas health). Signed 2021-06-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0205_9700_W9127817D0097_9700/.",
    "USASpending: Seobra Tres Esquinas health USD 0.957m. Supports seobra_tres_esquinas_health_957k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 957171.38; date_signed 2021-06-16.",
)

# === Cycle 971 ===
row_doc(
    "eterna_puerto_cortes_clinic_952k_2025",
    "infrastructure", "building_materials", "other",
    "Eterna — Puerto Cortés medical clinic HAP 70398",
    "Honduras",
    "15 Jan 2025: U.S. Army Corps of Engineers awards task order W9127825F0072 to Eterna for design and construction of HAP 70398 medical clinic in Puerto Cortés; obligated USD 952,075.22. CapEx face = award obligation.",
    "952075.22", "2025-01-15", "2025", "15.833", "-87.933",
    "Medical clinic HAP 70398, Puerto Cortés, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_puerto_cortes_clinic_952k_2025",
    "DESIGN AND CONSTRUCTION OF HAP 70398, MEDICAL CLINIC IN PUERTO CORTEZ, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0072_9700_W9127823D0073_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle971",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825F0072_9700_W9127823D0073_9700 (Eterna Puerto Cortés clinic). Signed 2025-01-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0072_9700_W9127823D0073_9700/.",
    "USASpending: Eterna Puerto Cortés clinic USD 0.952m. Supports eterna_puerto_cortes_clinic_952k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 952075.22; date_signed 2025-01-15.",
)

row_doc(
    "proksol_lima_security_admin_928k_2011",
    "infrastructure", "building_materials", "other",
    "Proksol — Lima security/screening and administration buildings design/build",
    "Peru",
    "15 Sep 2011: U.S. Army Corps of Engineers awards contract W9127811C0031 to Proksol for design/build security and screening building and administration building, Lima; obligated USD 928,382.02. CapEx face = award obligation.",
    "928382.02", "2011-09-15", "2011", "-12.046", "-77.043",
    "Security/screening and administration buildings, Lima, Peru (USASpending PoP Peru).",
    "usaspending_proksol_lima_security_admin_928k_2011",
    "TAS::21 2050::TAS DESIGN/BUILD SECURITY AND SCREENING BLDG AND ADMINISTRATION BLDG LI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811C0031_9700_-NONE-_-NONE-/",
    "Actor: Proksol (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle971",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811C0031_9700_-NONE-_-NONE- (Proksol Lima security/admin). Signed 2011-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811C0031_9700_-NONE-_-NONE-/.",
    "USASpending: Proksol Lima security/admin USD 0.928m. Supports proksol_lima_security_admin_928k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 928382.02; date_signed 2011-09-15.",
)

row_doc(
    "absolute_storage_semar_prefab_928k_2019",
    "infrastructure", "building_materials", "us",
    "Absolute Storage — SEMAR metallic pre-fabricated buildings",
    "Mexico",
    "11 Jan 2019: Department of State awards task order 191NLE19F0019 to Absolute Storage to deliver metallic pre-fabricated buildings to SEMAR warehouse (PoP Mexico); obligated USD 927,782.50. CapEx face = award obligation.",
    "927782.50", "2019-01-11", "2019", "19.433", "-99.133",
    "Metallic pre-fabricated buildings for SEMAR warehouse, Mexico (USASpending PoP Mexico; Mexico City pin).",
    "usaspending_absolute_storage_semar_prefab_928k_2019",
    "TASK ORDER FOR INL/MEXICO TO DELIVER METALLIC PRE-FABRICATED BUILDINGS TO SEMAR WAREHOUSE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE19F0019_1900_GS07F9481S_4730/",
    "Actor: Absolute Storage (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle971",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE19F0019_1900_GS07F9481S_4730 (Absolute Storage SEMAR prefab). Signed 2019-01-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE19F0019_1900_GS07F9481S_4730/.",
    "USASpending: Absolute Storage SEMAR prefab USD 0.928m. Supports absolute_storage_semar_prefab_928k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 927782.50; date_signed 2019-01-11.",
)

row_doc(
    "bonatti_la_union_pier_927k_2024",
    "infrastructure", "port_ownership", "other",
    "Bonatti — La Unión pier repair",
    "El Salvador",
    "26 Sep 2024: U.S. Army Corps of Engineers awards task order W9127824F0351 to Bonatti for pier repair La Unión; obligated USD 927,069.38. CapEx face = award obligation.",
    "927069.38", "2024-09-26", "2024", "13.337", "-87.843",
    "Pier repair, La Unión, El Salvador (USASpending PoP El Salvador).",
    "usaspending_bonatti_la_union_pier_927k_2024",
    "PIER REPAIR LA UNION, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0351_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle971",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0351_9700_W9127823D0072_9700 (Bonatti La Unión pier). Signed 2024-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0351_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti La Unión pier USD 0.927m. Supports bonatti_la_union_pier_927k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 927069.38; date_signed 2024-09-26.",
)

row_doc(
    "eterna_hap_medical_clinic_1p15m_2021",
    "infrastructure", "building_materials", "other",
    "Eterna — HAP #42239 and #42240 medical clinic",
    "Honduras",
    "29 Sep 2021: U.S. Army Corps of Engineers awards task order W9127821F0460 to Eterna for HAP #42239 and #42240 medical clinic; obligated USD 1,148,493.58. CapEx face = award obligation. Site not named beyond HAP IDs.",
    "1148493.58", "2021-09-29", "2021", "", "",
    "HAP #42239/#42240 medical clinic, Honduras (USASpending PoP Honduras; site not named — lat/lon blank).",
    "usaspending_eterna_hap_medical_clinic_1p15m_2021",
    "HAP #42239 AND #42240 MEDICAL CLINIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0460_9700_W9127821D0075_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle971",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0460_9700_W9127821D0075_9700 (Eterna HAP medical clinic). Signed 2021-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0460_9700_W9127821D0075_9700/.",
    "USASpending: Eterna HAP medical clinic USD 1.148m. Supports eterna_hap_medical_clinic_1p15m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1148493.58; date_signed 2021-09-29.",
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
    print(f"cycles969-971 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
