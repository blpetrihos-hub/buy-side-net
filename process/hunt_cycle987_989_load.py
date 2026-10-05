#!/usr/bin/env python3
"""Cycles 987–989: USASpending LatAm CapEx residual (~USD0.27–0.33m).

Seeds: 20261987–20261989. Thin top-up dry.
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


# === Cycle 987 ===
row_doc(
    "serrano_namru_bldg9_333k_2025",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — NAMRU-S Building 9 repair, Callao Naval Hospital",
    "Peru",
    "26 Sep 2025: U.S. Army Corps of Engineers awards task order W9127825FA270 to Serrano Proaño for repair of Building 9 at NAMRU-S compound, Callao Naval Hospital, Peru; obligated USD 332,682.83. CapEx face = award obligation.",
    "332682.83", "2025-09-26", "2025", "-12.060", "-77.140",
    "Building 9 repair, NAMRU-S / Callao Naval Hospital, Peru (USASpending description).",
    "usaspending_serrano_namru_bldg9_333k_2025",
    "REPAIR BUILDING 9, NAMRU-S COMPOUND, CALLAO NAVAL HOSPITAL, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA270_9700_W9127824D0077_9700/",
    "Actor: Serrano Proaño Diseño y Construcción S.A. (Quito) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle987",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA270_9700_W9127824D0077_9700 (Serrano NAMRU Bldg 9). Signed 2025-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA270_9700_W9127824D0077_9700/.",
    "USASpending: Serrano NAMRU Bldg 9 USD 0.333m. Supports serrano_namru_bldg9_333k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 332682.83; date_signed 2025-09-26.",
)

row_doc(
    "baskerville_callao_water_tower_329k_2025",
    "resources", "water", "us",
    "Baskerville Donovan — Callao Naval Hospital elevated water tower",
    "Peru",
    "20 Jun 2025: U.S. Army Corps of Engineers awards task order W9127825FA045 to Baskerville Donovan for construction of elevated water tower at Peru Naval Hospital, Callao; obligated USD 328,792.71. CapEx face = award obligation.",
    "328792.71", "2025-06-20", "2025", "-12.060", "-77.140",
    "Elevated water tower, Peru Naval Hospital, Callao (USASpending description).",
    "usaspending_baskerville_callao_water_tower_329k_2025",
    "CONSTRUCT ELEVATED WATER TOWER, PERU NAVAL HOSPITAL, CALLAO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA045_9700_W9127824D0012_9700/",
    "Actor: Baskerville Donovan Inc. (Mobile AL, U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle987",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA045_9700_W9127824D0012_9700 (Baskerville Callao water tower). Signed 2025-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA045_9700_W9127824D0012_9700/.",
    "USASpending: Baskerville Callao water tower USD 0.329m. Supports baskerville_callao_water_tower_329k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 328792.71; date_signed 2025-06-20.",
)

row_doc(
    "serrano_namru_bldg10_321k_2025",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — NAMRU-S Building 10 repairs, Callao Naval Hospital",
    "Peru",
    "28 Sep 2025: U.S. Army Corps of Engineers awards task order W9127825FA295 to Serrano Proaño for repairs to Building 10 at NAMRU-S compound, Callao Naval Hospital; obligated USD 320,635.90. CapEx face = award obligation.",
    "320635.90", "2025-09-28", "2025", "-12.060", "-77.140",
    "Building 10 repairs, NAMRU-S / Callao Naval Hospital, Peru (USASpending description).",
    "usaspending_serrano_namru_bldg10_321k_2025",
    "REPAIRS TO BUILDING 10 AT THE NAMRU-S COMPOUND, CALLAO NAVAL HOSPITAL, CALLAO, PERU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA295_9700_W9127824D0077_9700/",
    "Actor: Serrano Proaño Diseño y Construcción S.A. (Quito) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle987",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA295_9700_W9127824D0077_9700 (Serrano NAMRU Bldg 10). Signed 2025-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA295_9700_W9127824D0077_9700/.",
    "USASpending: Serrano NAMRU Bldg 10 USD 0.321m. Supports serrano_namru_bldg10_321k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 320635.90; date_signed 2025-09-28.",
)

row_doc(
    "mava_tupper_roof_315k_2020",
    "infrastructure", "building_materials", "other",
    "Mava Tractor — Tupper general service building roof replacement",
    "Panama",
    "4 Jun 2020: Smithsonian awards contract 33330220CF0010239 to Mava Tractor for Tupper general service building roof replacement (PoP Panama); obligated USD 314,846. CapEx face = award obligation.",
    "314846", "2020-06-04", "2020", "8.980", "-79.550",
    "Tupper general service building roof replacement, Panama (USASpending / Smithsonian; approximate STRI pin).",
    "usaspending_mava_tupper_roof_315k_2020",
    "TO FURNISH LABOR, MATERIAL AND EQUIPMENT FOR TUPPER GENERAL SERVICE BUILDING ROOF REPLACEMENT,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220CF0010239_3300_-NONE-_-NONE-/",
    "Actor: Mava Tractor S.A. (Panama City) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle987",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330220CF0010239_3300_-NONE-_-NONE- (Mava Tupper roof). Signed 2020-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220CF0010239_3300_-NONE-_-NONE-/.",
    "USASpending: Mava Tupper roof USD 0.315m. Supports mava_tupper_roof_315k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 314846; date_signed 2020-06-04.",
)

row_doc(
    "mantech_haiti_drw_314k_2011",
    "infrastructure", "building_materials", "us",
    "ManTech — HAP 12212 Haiti disaster relief warehouse and training",
    "Haiti",
    "13 Apr 2011: U.S. Army Corps of Engineers awards task order 0016 under W912CL07D0010 to ManTech for HAP Project 12212 Haiti disaster relief warehouse and training; obligated USD 313,525.04. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "313525.04", "2011-04-13", "2011", "", "",
    "HAP 12212 disaster relief warehouse and training, Haiti (USASpending PoP Haiti; site not named — lat/lon blank).",
    "usaspending_mantech_haiti_drw_314k_2011",
    "CONTRACT AWARD OF HAP PROJECT 12212- HAITI DISASTER RELIEF WAREHOUSE AND TRAINING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W912CL07D0010_9700/",
    "Actor: ManTech Telecommunications and Information Systems (Chantilly VA, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx; Haiti under-covered.",
    "hunt_cycle987",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0016_9700_W912CL07D0010_9700 (ManTech Haiti DRW). Signed 2011-04-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W912CL07D0010_9700/.",
    "USASpending: ManTech Haiti DRW USD 0.314m. Supports mantech_haiti_drw_314k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 313525.04; date_signed 2011-04-13.",
)

# === Cycle 988 ===
row_doc(
    "quevedo_landslide_313k_2021",
    "infrastructure", "bridges_roads", "other",
    "Quevedo & Villamarín — landslide stabilization construction",
    "Ecuador",
    "15 Jun 2021: Department of State awards contract 19GE5021C0028 to Quevedo & Villamarín for landslide stabilization construction services (PoP Ecuador); obligated USD 312,868.55. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "312868.55", "2021-06-15", "2021", "", "",
    "Landslide stabilization, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_quevedo_landslide_313k_2021",
    "CONSTRUCTION SERVICES: LANDSLIDE STABILIZATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0028_1900_-NONE-_-NONE-/",
    "Actor: Quevedo & Villamarín Constructores (Quito) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle988",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0028_1900_-NONE-_-NONE- (Quevedo landslide). Signed 2021-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0028_1900_-NONE-_-NONE-/.",
    "USASpending: Quevedo landslide stabilization USD 0.313m. Supports quevedo_landslide_313k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 312868.55; date_signed 2021-06-15.",
)

row_doc(
    "eei_ecuador_chem_lab_299k_2026",
    "infrastructure", "building_materials", "other",
    "EEI — Ecuador chemical laboratory construction",
    "Ecuador",
    "23 Sep 2026: Department of State awards contract 19GE5026C0111 to Estudios Edificaciones e Interventorías for construction of a chemical laboratory in Ecuador; obligated USD 299,032.37. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "299032.37", "2026-09-23", "2026", "", "",
    "Chemical laboratory construction, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_eei_ecuador_chem_lab_299k_2026",
    "CONSTRUCTION OF A CHEMICAL LABORATORY IN ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0111_1900_-NONE-_-NONE-/",
    "Actor: EEI S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle988",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0111_1900_-NONE-_-NONE- (EEI Ecuador chem lab). Signed 2026-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0111_1900_-NONE-_-NONE-/.",
    "USASpending: EEI Ecuador chem lab USD 0.299m. Supports eei_ecuador_chem_lab_299k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 299032.37; date_signed 2026-09-23.",
)

row_doc(
    "bendig_murcielago_barracks_297k_2019",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Murciélago Police Academy barracks renovation",
    "Costa Rica",
    "25 Jun 2019: Department of State awards contract 19AQMM19C0066 to Industrias Bendig for renovation of barracks at the Murciélago Police Academy in Costa Rica; obligated USD 297,079.88. CapEx face = award obligation.",
    "297079.88", "2019-06-25", "2019", "10.800", "-85.700",
    "Barracks renovation, Murciélago Police Academy, Costa Rica (USASpending description; approximate Guanacaste pin).",
    "usaspending_bendig_murcielago_barracks_297k_2019",
    "RENOVATION OF BARRACKS AT THE MURCIELAGO POLICE ACADEMY IN COSTA RICA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0066_1900_-NONE-_-NONE-/",
    "Actor: Industrias Bendig SA (Desamparados, Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle988",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0066_1900_-NONE-_-NONE- (Bendig Murciélago barracks). Signed 2019-06-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0066_1900_-NONE-_-NONE-/.",
    "USASpending: Bendig Murciélago barracks USD 0.297m. Supports bendig_murcielago_barracks_297k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 297079.88; date_signed 2019-06-25.",
)

row_doc(
    "cym_bci_dorm_296k_2020",
    "infrastructure", "building_materials", "other",
    "Construcciones y Mantenimientos — BCI game warden dormitory renovation",
    "Panama",
    "16 Jul 2020: Smithsonian awards contract 33330220CF0010272 to Construcciones y Mantenimientos Eficientes for renovation of BCI's game warden dormitory at Barro Colorado Island; obligated USD 296,485. CapEx face = award obligation.",
    "296485", "2020-07-16", "2020", "9.165", "-79.838",
    "Game warden dormitory renovation, Barro Colorado Island, Panama (USASpending / STRI description).",
    "usaspending_cym_bci_dorm_296k_2020",
    "CONSTRUCTION SERVICES FOR THE RENOVATION OF BCI'S GAME WARDEN DORMITORY AT BARRO COLORADO ISLAND - STRI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220CF0010272_3300_-NONE-_-NONE-/",
    "Actor: Construcciones y Mantenimientos Eficientes S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle988",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330220CF0010272_3300_-NONE-_-NONE- (CyM BCI dorm). Signed 2020-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220CF0010272_3300_-NONE-_-NONE-/.",
    "USASpending: CyM BCI dorm USD 0.296m. Supports cym_bci_dorm_296k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 296485; date_signed 2020-07-16.",
)

row_doc(
    "cym_admin_roof_281k_2021",
    "infrastructure", "building_materials", "other",
    "Construcciones y Mantenimientos — administration building roof replacement",
    "Panama",
    "18 Jun 2021: Smithsonian awards contract 33330221CF0010288 to Construcciones y Mantenimientos Eficientes for replacement of roof of administration building (PoP Panama); obligated USD 280,677.50. CapEx face = award obligation. Exact campus unnamed — lat/lon blank.",
    "280677.50", "2021-06-18", "2021", "", "",
    "Administration building roof replacement, Panama (USASpending / Smithsonian; site not named — lat/lon blank).",
    "usaspending_cym_admin_roof_281k_2021",
    "TO FURNISH SERVICE, LABOR, MATERIAL AND TRANSPORT FOR REPLACE ROOF OF ADMINISTRATION BUILD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010288_3300_-NONE-_-NONE-/",
    "Actor: Construcciones y Mantenimientos Eficientes S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle988",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330221CF0010288_3300_-NONE-_-NONE- (CyM admin roof). Signed 2021-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010288_3300_-NONE-_-NONE-/.",
    "USASpending: CyM admin roof USD 0.281m. Supports cym_admin_roof_281k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 280677.50; date_signed 2021-06-18.",
)

# === Cycle 989 ===
row_doc(
    "misc_dr_barracks_276k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic barracks renovation",
    "Dominican Republic",
    "11 Jan 2017: Department of Defense awards contract for barracks renovation in Dominican Republic; obligated USD 276,053.20. CapEx face = award obligation. Recipient redacted; site not named — lat/lon blank.",
    "276053.20", "2017-01-11", "2017", "", "",
    "Barracks renovation, Dominican Republic (USASpending PoP Dominican Republic; site not named — lat/lon blank).",
    "usaspending_misc_dr_barracks_276k_2017",
    "IGF::OT::IGF BARRACKS RENOVATION IN DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417C1002_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle989",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470417C1002_9700_-NONE-_-NONE- (DR barracks renovation). Signed 2017-01-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417C1002_9700_-NONE-_-NONE-/.",
    "USASpending: DR barracks renovation USD 0.276m. Supports misc_dr_barracks_276k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 276053.20; date_signed 2017-01-11.",
)

row_doc(
    "ys_lab_vuelta_obligado_268k_2024",
    "infrastructure", "building_materials", "other",
    "YS Lab — FAC Vuelta de Obligado 1A renovation",
    "Argentina",
    "18 Jul 2024: Department of State awards contract for FAC Vuelta de Obligado 1A renovation to YS Lab S.R.L.; obligated USD 268,344.53. CapEx face = award obligation.",
    "268344.53", "2024-07-18", "2024", "-34.580", "-58.420",
    "FAC Vuelta de Obligado 1A renovation, Argentina (USASpending description; Buenos Aires area pin).",
    "usaspending_ys_lab_vuelta_obligado_268k_2024",
    "FAC - VUELTA DE OBLIGADO 1A RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2024C0003_1900_-NONE-_-NONE-/",
    "Actor: YS Lab S.R.L. (Argentina) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle989",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2024C0003_1900_-NONE-_-NONE- (YS Lab Vuelta de Obligado). Signed 2024-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2024C0003_1900_-NONE-_-NONE-/.",
    "USASpending: YS Lab Vuelta de Obligado USD 0.268m. Supports ys_lab_vuelta_obligado_268k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 268344.53; date_signed 2024-07-18.",
)

row_doc(
    "cym_bci_lab_roof_267k_2019",
    "infrastructure", "building_materials", "other",
    "Construcciones y Mantenimientos — BCI laboratory roof replacement",
    "Panama",
    "27 Sep 2019: Smithsonian awards contract for BCI laboratory roof replacement (north wing) to Construcciones y Mantenimientos Eficientes; obligated USD 266,795. CapEx face = award obligation.",
    "266795", "2019-09-27", "2019", "9.165", "-79.838",
    "BCI laboratory roof replacement (north wing), Barro Colorado Island, Panama (USASpending / STRI).",
    "usaspending_cym_bci_lab_roof_267k_2019",
    "TO FURNISH LABOR, MATERIAL AND EQUIPMENT FOR BCI LABORATORY ROOF REPLACEMENT (NORTH WING 4",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010300_3300_-NONE-_-NONE-/",
    "Actor: Construcciones y Mantenimientos Eficientes S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle989",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330219CF0010300_3300_-NONE-_-NONE- (CyM BCI lab roof). Signed 2019-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010300_3300_-NONE-_-NONE-/.",
    "USASpending: CyM BCI lab roof USD 0.267m. Supports cym_bci_lab_roof_267k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 266795; date_signed 2019-09-27.",
)

row_doc(
    "proyectos_panama_classrooms_320k_2011",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — Panama new classrooms construction",
    "Panama",
    "26 Sep 2011: U.S. Army Corps of Engineers awards contract W912CL11C0043 to Proyectos Civiles for new classrooms construction (PoP Panama); obligated USD 319,524.46. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "319524.46", "2011-09-26", "2011", "", "",
    "New classrooms construction, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_proyectos_panama_classrooms_320k_2011",
    "NEW CLASSROOMS CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0043_9700_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle989",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0043_9700_-NONE-_-NONE- (Proyectos Panama classrooms). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0043_9700_-NONE-_-NONE-/.",
    "USASpending: Proyectos Panama classrooms USD 0.320m. Supports proyectos_panama_classrooms_320k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 319524.46; date_signed 2011-09-26.",
)

row_doc(
    "serrano_callao_water_pump_279k_2025",
    "resources", "water", "other",
    "Serrano Proaño — Callao Naval Hospital water pump No. 6 repair",
    "Peru",
    "28 Sep 2025: U.S. Army Corps of Engineers awards task order to Serrano Proaño for repair of water pump No. 6 at Callao Naval Hospital, Peru; obligated USD 279,172. CapEx face = award obligation.",
    "279172", "2025-09-28", "2025", "-12.060", "-77.140",
    "Water pump No. 6 repair, Callao Naval Hospital, Peru (USASpending description).",
    "usaspending_serrano_callao_water_pump_279k_2025",
    "REPAIR OF WATER PUMP NO. 6 - CALLAO NAVAL HOSPITAL, PERU. THE TASK WILL BE PERFORMED UNDER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA282_9700_W9127824D0077_9700/",
    "Actor: Serrano Proaño Diseño y Construcción S.A. (Quito) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle989",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA282_9700_W9127824D0077_9700 (Serrano Callao water pump). Signed 2025-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA282_9700_W9127824D0077_9700/.",
    "USASpending: Serrano Callao water pump USD 0.279m. Supports serrano_callao_water_pump_279k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 279172; date_signed 2025-09-28.",
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
    print(f"cycles987-989 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
