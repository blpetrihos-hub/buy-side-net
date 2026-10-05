#!/usr/bin/env python3
"""Cycles 1065–1067: USASpending LatAm CapEx residual (~USD0.033–0.065m).

Seeds: 20262065–20262067. Thin top-up dry.
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


# === Cycle 1065 (seed 20262065) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fluid_solutions_mexico_merida_fire_pump_52k_2023",
    "resources", "water", "us",
    "Fluid Solutions — Merida consulate fire pump and controller repair",
    "Mexico",
    "11 Sep 2023: Department of State awards contract 19MX5223P0211 to Fluid Solutions LLC for Merida OBO FAC consulate fire pump and controller repair FY23 (PoP Mexico); obligated USD 52,263.04. CapEx face = award obligation. Exact consulate site unnamed — lat/lon blank.",
    "52263.04", "2023-09-11", "2023", "", "",
    "Consulate fire pump and controller repair, Merida, Mexico (USASpending description; Merida named, site coords not stated — lat/lon blank).",
    "usaspending_fluid_solutions_mexico_merida_fire_pump_52k_2023",
    "MER-OBO-FAC CONSULATE FIRE PUMP & CONTROLLER REPAIR FY23",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5223P0211_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1065",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5223P0211_1900_-NONE-_-NONE- (Fluid Solutions Merida fire pump). Signed 2023-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5223P0211_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions Merida fire pump USD 0.052m. Supports fluid_solutions_mexico_merida_fire_pump_52k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52263.04; date_signed 2023-09-11.",
)

row_doc(
    "price_consulting_peru_residence_roof_ae_52k_2017",
    "infrastructure", "engineering_epc", "us",
    "Price Consulting — Peru residence roof replacement A&E",
    "Peru",
    "20 Sep 2017: Department of State awards contract SPE50017C0039 to Price Consulting Inc. for A&E for residence roof replacement (PoP Peru); obligated USD 52,219. CapEx face = award obligation. Exact residence unnamed — lat/lon blank.",
    "52219", "2017-09-20", "2017", "", "",
    "A&E for residence roof replacement, Peru (USASpending description; residence not named — lat/lon blank).",
    "usaspending_price_consulting_peru_residence_roof_ae_52k_2017",
    "CONTRACT A&E X 10010RESIDENCE ROOF REPLACEMENT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017C0039_1900_-NONE-_-NONE-/",
    "Actor: Price Consulting Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1065",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50017C0039_1900_-NONE-_-NONE- (Price Consulting Peru roof A&E). Signed 2017-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017C0039_1900_-NONE-_-NONE-/.",
    "USASpending: Price Consulting Peru roof A&E USD 0.052m. Supports price_consulting_peru_residence_roof_ae_52k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52219; date_signed 2017-09-20.",
)

row_doc(
    "cme_panama_tupper_exterior_paint_65k_2025",
    "infrastructure", "building_materials", "other",
    "Construcciones y Mantenimientos Eficientes — Panama Tupper exterior paint and repairs",
    "Panama",
    "4 Sep 2025: Smithsonian Tropical Research Institute awards contract 33312925P00527554 to Construcciones y Mantenimientos Eficientes S.A. for Tupper building exterior paint and repairs (PoP Panama); obligated USD 64,900. CapEx face = award obligation. Exact Tupper site unnamed — lat/lon blank.",
    "64900", "2025-09-04", "2025", "", "",
    "Tupper building exterior paint and repairs, Panama (USASpending description; Tupper named, site coords not stated — lat/lon blank).",
    "usaspending_cme_panama_tupper_exterior_paint_65k_2025",
    "BM05-2025/ TUPPER BUILDING EXTERIOR PAINT AND REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312925P00527554_3300_-NONE-_-NONE-/",
    "Actor: Construcciones y Mantenimientos Eficientes S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1065",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33312925P00527554_3300_-NONE-_-NONE- (CME Tupper exterior paint). Signed 2025-09-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312925P00527554_3300_-NONE-_-NONE-/.",
    "USASpending: CME Tupper exterior paint USD 0.065m. Supports cme_panama_tupper_exterior_paint_65k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64900; date_signed 2025-09-04.",
)

row_doc(
    "climatizadora_panama_cooling_tower_fill_65k_2022",
    "energy", "power_plants_grid", "other",
    "Compania Climatizadora — Panama cooling tower plastic fill replacement",
    "Panama",
    "22 Jul 2022: Department of State awards contract 19PM0722P0669 to Compania Climatizadora S.A. for cooling tower plastic fill replacement (PoP Panama); obligated USD 64,994.90. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "64994.90", "2022-07-22", "2022", "", "",
    "Cooling tower plastic fill replacement, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_climatizadora_panama_cooling_tower_fill_65k_2022",
    "COOLING TOWER PLASTIC FILL REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0669_1900_-NONE-_-NONE-/",
    "Actor: Compania Climatizadora S.A. (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1065",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0722P0669_1900_-NONE-_-NONE- (Climatizadora cooling-tower fill). Signed 2022-07-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0669_1900_-NONE-_-NONE-/.",
    "USASpending: Climatizadora cooling-tower fill USD 0.065m. Supports climatizadora_panama_cooling_tower_fill_65k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64994.90; date_signed 2022-07-22.",
)

row_doc(
    "bj_soluciones_panama_tupper_york_chiller_64k_2015",
    "energy", "power_plants_grid", "other",
    "B J Soluciones Termicas — Panama Tupper York 140-ton chiller installation",
    "Panama",
    "20 Feb 2015: Smithsonian Tropical Research Institute awards purchase order F15PO7390000319130 to B J Soluciones Termicas for York 140-ton chiller installation at Tupper complex (PoP Panama); obligated USD 64,457.19. CapEx face = award obligation. Exact Tupper site unnamed — lat/lon blank.",
    "64457.19", "2015-02-20", "2015", "", "",
    "York 140-ton chiller installation at Tupper complex, Panama (USASpending description; Tupper named, site coords not stated — lat/lon blank).",
    "usaspending_bj_soluciones_panama_tupper_york_chiller_64k_2015",
    "IGF::OT::IGF  REQUIRED SERVICES ARE NOT PROVIDED BY AGENCY EMPLOYEES. FY2015- CHILLER INSTALLATION YORK 140 TON- TUPPER COMPLEX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F15PO7390000319130_3300_-NONE-_-NONE-/",
    "Actor: B J Soluciones Termicas (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1065",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F15PO7390000319130_3300_-NONE-_-NONE- (BJ Soluciones Tupper York chiller). Signed 2015-02-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F15PO7390000319130_3300_-NONE-_-NONE-/.",
    "USASpending: BJ Soluciones Tupper York chiller USD 0.064m. Supports bj_soluciones_panama_tupper_york_chiller_64k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64457.19; date_signed 2015-02-20.",
)

# === Cycle 1066 (seed 20262066) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_mexico_tss_62k_2022",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico TSS security systems",
    "Mexico",
    "7 Feb 2022: Department of State awards order 19AQMM22F0641 to Applied Security Technologies Inc for TSS security systems (PoP Mexico); obligated USD 62,438. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "62438", "2022-02-07", "2022", "", "",
    "TSS security systems, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_mexico_tss_62k_2022",
    "TSS SECURITY SYSTEMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0641_1900_19AQMM19D0002_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1066",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F0641_1900_19AQMM19D0002_1900 (Applied Security Mexico TSS). Signed 2022-02-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0641_1900_19AQMM19D0002_1900/.",
    "USASpending: Applied Security Mexico TSS USD 0.062m. Supports applied_security_mexico_tss_62k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62438; date_signed 2022-02-07.",
)

row_doc(
    "orion_guyana_tss_34k_2019",
    "infrastructure", "building_materials", "us",
    "Orion Management — Guyana technical security systems installation",
    "Guyana",
    "7 Nov 2019: Department of State awards order 19AQMM20F0107 to Orion Management, LLC for technical security systems installation TSS (PoP Guyana); obligated USD 33,522.60. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "33522.60", "2019-11-07", "2019", "", "",
    "Technical security systems installation (TSS), Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_orion_guyana_tss_34k_2019",
    "TECHNICAL SECURITY SYSTEMS INSTALLATION (TSS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0107_1900_19AQMM19D0008_1900/",
    "Actor: Orion Management, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1066",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F0107_1900_19AQMM19D0008_1900 (Orion Guyana TSS). Signed 2019-11-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0107_1900_19AQMM19D0008_1900/.",
    "USASpending: Orion Guyana TSS USD 0.034m. Supports orion_guyana_tss_34k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 33522.60; date_signed 2019-11-07.",
)

row_doc(
    "misc_mexico_bfl_york_chiller_64k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico BFL York 50 TR chiller replacement",
    "Mexico",
    "12 Sep 2017: Department of State awards contract SMX53017M1694 for replacement of BFL York chiller of 50 T.R. (PoP Mexico); obligated USD 63,830.18. CapEx face = award obligation. Exact BFL site unnamed — lat/lon blank.",
    "63830.18", "2017-09-12", "2017", "", "",
    "Replacement of BFL York chiller of 50 T.R., Mexico (USASpending description; BFL named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_bfl_york_chiller_64k_2017",
    "IGF::OT::IGF MEX/FAC/REPLACEMENT OF BFL YOTK CHILLER OF 50 T.R.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017M1694_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1066",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53017M1694_1900_-NONE-_-NONE- (Mexico BFL York chiller). Signed 2017-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017M1694_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico BFL York chiller USD 0.064m. Supports misc_mexico_bfl_york_chiller_64k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63830.18; date_signed 2017-09-12.",
)

row_doc(
    "misc_colombia_la_macarena_fence_64k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia La Macarena security fence construction",
    "Colombia",
    "18 Sep 2010: Department of the Army awards contract W913FT10P0219 for La Macarena security fence construction (PoP Colombia); obligated USD 63,750.20. CapEx face = award obligation. Exact fence alignment unnamed — lat/lon blank.",
    "63750.20", "2010-09-18", "2010", "", "",
    "La Macarena security fence construction, Colombia (USASpending description; La Macarena named, fence coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_la_macarena_fence_64k_2010",
    "LA MACARENA SECURITY FENCE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10P0219_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1066",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10P0219_9700_-NONE-_-NONE- (Colombia La Macarena fence). Signed 2010-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10P0219_9700_-NONE-_-NONE-/.",
    "USASpending: Colombia La Macarena fence USD 0.064m. Supports misc_colombia_la_macarena_fence_64k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63750.20; date_signed 2010-09-18.",
)

row_doc(
    "vinpar_colombia_cmr_facade_63k_2025",
    "infrastructure", "building_materials", "other",
    "Construcciones Vinpar — Colombia CMR facade repair",
    "Colombia",
    "23 Sep 2025: Department of State awards contract 19C02025P1743 to Construcciones Vinpar S.A.S. for CMR facade repair (PoP Colombia); obligated USD 63,319.47. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "63319.47", "2025-09-23", "2025", "", "",
    "CMR facade repair, Colombia (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_vinpar_colombia_cmr_facade_63k_2025",
    "PR15468587 CMR FACADE REPAIR 7919 XJ-1D-0119",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025P1743_1900_-NONE-_-NONE-/",
    "Actor: Construcciones Vinpar S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1066",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02025P1743_1900_-NONE-_-NONE- (Vinpar Colombia CMR facade). Signed 2025-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025P1743_1900_-NONE-_-NONE-/.",
    "USASpending: Vinpar Colombia CMR facade USD 0.063m. Supports vinpar_colombia_cmr_facade_63k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63319.47; date_signed 2025-09-23.",
)

# === Cycle 1067 (seed 20262067) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "johnson_controls_barbados_chiller_compressor_58k_2015",
    "energy", "power_plants_grid", "us",
    "Johnson Controls — Barbados NEC chiller compressor",
    "Barbados",
    "11 Aug 2015: Department of State awards contract SBB21015M0838 to Johnson Controls Inc for compressor for chillers at NEC (PoP Barbados); obligated USD 58,480. CapEx face = award obligation. Exact NEC site unnamed — lat/lon blank.",
    "58480", "2015-08-11", "2015", "", "",
    "Compressor for chillers at NEC, Barbados (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_johnson_controls_barbados_chiller_compressor_58k_2015",
    "COMPRESSOR FOR CHILLERS-NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21015M0838_1900_-NONE-_-NONE-/",
    "Actor: Johnson Controls Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1067",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21015M0838_1900_-NONE-_-NONE- (Johnson Controls Barbados compressor). Signed 2015-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21015M0838_1900_-NONE-_-NONE-/.",
    "USASpending: Johnson Controls Barbados compressor USD 0.058m. Supports johnson_controls_barbados_chiller_compressor_58k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58480; date_signed 2015-08-11.",
)

row_doc(
    "valkyrie_uruguay_telecom_cabling_50k_2022",
    "infrastructure", "engineering_epc", "us",
    "Valkyrie Enterprises — Uruguay OBO telecommunications cabling engineering",
    "Uruguay",
    "20 Sep 2022: Department of State awards order 19AQMM22F3970 to Valkyrie Enterprises, LLC for OBO/PDCS/DE/EE telecommunications cabling engineering services (PoP Uruguay); obligated USD 49,980.58. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49980.58", "2022-09-20", "2022", "", "",
    "OBO telecommunications cabling engineering services, Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_valkyrie_uruguay_telecom_cabling_50k_2022",
    "THE US DEPARTMENT OF STATE, BUREAU OF OVERSEAS BUILDING OPERATIONS, PROGRAM DEVELOPMENT, COORDINATION, AND SUPPORT, OFFICE OF DESIGN AND ENGINEERING, ELECTRICAL ENGINEERING DIVISION (OBO/PDCS/DE/EE), TO USE THE SERVICES OF A TELECOMMUNICATIONS CABLIN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F3970_1900_19AQMM21D0155_1900/",
    "Actor: Valkyrie Enterprises, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1067",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F3970_1900_19AQMM21D0155_1900 (Valkyrie Uruguay telecom cabling). Signed 2022-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F3970_1900_19AQMM21D0155_1900/.",
    "USASpending: Valkyrie Uruguay telecom cabling USD 0.050m. Supports valkyrie_uruguay_telecom_cabling_50k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49980.58; date_signed 2022-09-20.",
)

row_doc(
    "misc_dr_cmr_cctv_63k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic CMR CCTV security system",
    "Dominican Republic",
    "30 Jun 2025: Department of State awards contract 19DR8625P1555 for RSO/CMR CCTV security system purchase and installation (PoP Dominican Republic); obligated USD 63,222.71. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "63222.71", "2025-06-30", "2025", "", "",
    "RSO/CMR CCTV security system purchase and installation, Dominican Republic (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dr_cmr_cctv_63k_2025",
    "RSO/CMR CCTV SEC. SYSTEM PURCHASE AND INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625P1555_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1067",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8625P1555_1900_-NONE-_-NONE- (DR CMR CCTV). Signed 2025-06-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625P1555_1900_-NONE-_-NONE-/.",
    "USASpending: DR CMR CCTV USD 0.063m. Supports misc_dr_cmr_cctv_63k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63222.71; date_signed 2025-06-30.",
)

row_doc(
    "limon_mexico_cmr_driveway_63k_2021",
    "infrastructure", "bridges_roads", "other",
    "Limón Noriega — Mexico CMR driveway stone floor repairs",
    "Mexico",
    "30 Apr 2021: Department of State awards contract 19MX5321C0003 to Limón Noriega, Abelardo for driveway stone floor repairs at CMR (PoP Mexico); obligated USD 62,940.48. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "62940.48", "2021-04-30", "2021", "", "",
    "Driveway stone floor repairs at CMR, Mexico (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_limon_mexico_cmr_driveway_63k_2021",
    "MEX-FAC-7355-DRIVEWAY STONE FLOOR REPAIRS AT CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321C0003_1900_-NONE-_-NONE-/",
    "Actor: Limón Noriega, Abelardo (Mexico) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1067",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5321C0003_1900_-NONE-_-NONE- (Limón Mexico CMR driveway). Signed 2021-04-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Limón Mexico CMR driveway USD 0.063m. Supports limon_mexico_cmr_driveway_63k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62940.48; date_signed 2021-04-30.",
)

row_doc(
    "misc_colombia_santa_marta_barracks_ae_63k_2017",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia Santa Marta barracks A&E",
    "Colombia",
    "27 Sep 2017: Department of State awards contract SCO15017M0452 for INL Bogota A&E for barracks in Santa Marta (PoP Colombia); obligated USD 63,122.61. CapEx face = award obligation. Exact barracks site unnamed — lat/lon blank.",
    "63122.61", "2017-09-27", "2017", "", "",
    "A&E for barracks in Santa Marta, Colombia (USASpending description; Santa Marta named, barracks coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_santa_marta_barracks_ae_63k_2017",
    "IGF::OT::IGF INL BOGOTA - A&E FOR BARRACKS IN SANTA MARTA 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017M0452_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1067",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15017M0452_1900_-NONE-_-NONE- (Colombia Santa Marta barracks A&E). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017M0452_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia Santa Marta barracks A&E USD 0.063m. Supports misc_colombia_santa_marta_barracks_ae_63k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63122.61; date_signed 2017-09-27.",
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
