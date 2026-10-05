#!/usr/bin/env python3
"""Cycles 1242–1247: USASpending LatAm CapEx (US vendor stock + residual other).

Seeds: 20262242–20262247. Thin top-up dry.
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

# === Cycle 1242 ===
row_doc(
    "mesan_martinez_panama_balboa_building_reno_567k_2010",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez JV — Panama Balboa building #745 construction/renovation",
    "Panama",
    "3 Sep 2010: Department of State awards task order to MESAN-MARTINEZ JOINT VENTURE LLP for construction/renovation services on building #745-Balboa (PoP Panama); obligated USD 567420. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "567420", "2010-09-03", "2010", "", "",
    "THE CONTRACTOR WILL PROVIDE ALL PLANT, LABOR, MATERIALS, ETC. REQUIRED TO PROVIDE CONSTRUCTION/RE..., Panama (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_mesan_martinez_panama_balboa_building_reno_567k_2010",
    "THE CONTRACTOR WILL PROVIDE ALL PLANT, LABOR, MATERIALS, ETC. REQUIRED TO PROVIDE CONSTRUCTION/RENOVATION SERVICES ON BUILDING #745-BALBOA, FOR THE PANAMA MATADOR BUILDING, RENOVATION PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC10F0094_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1242",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC10F0094_1900_SAQMMA08D0015_1900 (mesan_martinez_panama_balboa_building_reno_567k_2010). Signed 2010-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC10F0094_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_martinez_panama_balboa_building_reno_567k_2010 USD 0.567m. Supports mesan_martinez_panama_balboa_building_reno_567k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 567420.0; date_signed 2010-09-03.",
)

# === Cycle 1242 ===
row_doc(
    "rafay_mobile_panama_cctv_surveillance_29k_2022",
    "infrastructure", "building_materials", "us",
    "Rafay Mobile — Panama CCTV surveillance system",
    "Panama",
    "22 Apr 2022: Department of State awards task order to RAFAY MOBILE, INC. for CCTV surveillance system (PoP Panama); obligated USD 28809. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "28809", "2022-04-22", "2022", "", "",
    "CCTV SURVEILLANCE SYSTEM, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_rafay_mobile_panama_cctv_surveillance_29k_2022",
    "CCTV SURVEILLANCE SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722F0132_1900_47QTCA22D000T_4732/",
    "Actor: RAFAY MOBILE (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1242",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0722F0132_1900_47QTCA22D000T_4732 (rafay_mobile_panama_cctv_surveillance_29k_2022). Signed 2022-04-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722F0132_1900_47QTCA22D000T_4732/.",
    "USASpending: rafay_mobile_panama_cctv_surveillance_29k_2022 USD 0.029m. Supports rafay_mobile_panama_cctv_surveillance_29k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28809.0; date_signed 2022-04-22.",
)

# === Cycle 1242 ===
row_doc(
    "misc_mexico_nld_generators_replacement_205k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico NLD-FAC generators replacement",
    "Mexico",
    "19 Sep 2022: Department of State awards contract for NLD-FAC-7901S-CCS-generators replacement (PoP Mexico); obligated USD 205200. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "205200", "2022-09-19", "2022", "", "",
    "NLD-FAC-7901S-CCS-GENERATORS REPLACEMENT, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_nld_generators_replacement_205k_2022",
    "NLD-FAC-7901S-CCS-GENERATORS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6122P0181_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1242",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6122P0181_1900_-NONE-_-NONE- (misc_mexico_nld_generators_replacement_205k_2022). Signed 2022-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6122P0181_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nld_generators_replacement_205k_2022 USD 0.205m. Supports misc_mexico_nld_generators_replacement_205k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205200.0; date_signed 2022-09-19.",
)

# === Cycle 1242 ===
row_doc(
    "misc_haiti_stecher_roumain_cctv_164k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti CCTV installation at Stecher Roumain",
    "Haiti",
    "21 Jun 2023: Department of State awards contract for CCTV installation at Stecher Roumain (PoP Haiti); obligated USD 163900. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "163900", "2023-06-21", "2023", "", "",
    "CCTV INSTALLATION AT STECHER ROUMAIN, Haiti (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_stecher_roumain_cctv_164k_2023",
    "CCTV INSTALLATION AT STECHER ROUMAIN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P0704_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1242",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P0704_1900_-NONE-_-NONE- (misc_haiti_stecher_roumain_cctv_164k_2023). Signed 2023-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P0704_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_stecher_roumain_cctv_164k_2023 USD 0.164m. Supports misc_haiti_stecher_roumain_cctv_164k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 163900.0; date_signed 2023-06-21.",
)

# === Cycle 1242 ===
row_doc(
    "misc_argentina_cmr_cctv_system_133k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina RSO RSP CCTV system for CMR",
    "Argentina",
    "27 Aug 2025: Department of State awards contract for RSO RSP CCTV system for CMR (PoP Argentina); obligated USD 132960.85. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "132960.85", "2025-08-27", "2025", "", "",
    "RSO - RSP CCTV SYSTEM FOR CMR, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_argentina_cmr_cctv_system_133k_2025",
    "RSO - RSP CCTV SYSTEM FOR CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2025C0005_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1242",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2025C0005_1900_-NONE-_-NONE- (misc_argentina_cmr_cctv_system_133k_2025). Signed 2025-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2025C0005_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_cmr_cctv_system_133k_2025 USD 0.133m. Supports misc_argentina_cmr_cctv_system_133k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 132960.85; date_signed 2025-08-27.",
)

# === Cycle 1243 ===
row_doc(
    "export_220volt_brazil_make_ready_transformers_26k_2020",
    "energy", "power_plants_grid", "us",
    "Export 220Volt — Brazil transformers for residences make-ready",
    "Brazil",
    "18 Mar 2020: Department of State awards contract to EXPORT 220VOLT INC. for transformers for residences make ready (PoP Brazil); obligated USD 25800. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "25800", "2020-03-18", "2020", "", "",
    "TRANSFORMERS FOR RESIDENCES MAKE READY, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_export_220volt_brazil_make_ready_transformers_26k_2020",
    "TRANSFORMERS FOR RESIDENCES MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0300_1900_-NONE-_-NONE-/",
    "Actor: EXPORT 220VOLT INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1243",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0300_1900_-NONE-_-NONE- (export_220volt_brazil_make_ready_transformers_26k_2020). Signed 2020-03-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0300_1900_-NONE-_-NONE-/.",
    "USASpending: export_220volt_brazil_make_ready_transformers_26k_2020 USD 0.026m. Supports export_220volt_brazil_make_ready_transformers_26k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25800.0; date_signed 2020-03-18.",
)

# === Cycle 1243 ===
row_doc(
    "export_220volt_brazil_make_ready_transformers_25k_2021",
    "energy", "power_plants_grid", "us",
    "Export 220Volt — Brazil Brasília transformers for make-ready residences",
    "Brazil",
    "23 Aug 2021: Department of State awards contract to EXPORT 220VOLT INC. for BSB PSW/GSO transformers for make-ready residences (PoP Brazil); obligated USD 24680. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "24680", "2021-08-23", "2021", "", "",
    "BSB - PSW/GSO - TRANSFORMERS FOR MAKE READY RESIDENCES - FAP, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_export_220volt_brazil_make_ready_transformers_25k_2021",
    "BSB - PSW/GSO - TRANSFORMERS FOR MAKE READY RESIDENCES - FAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0820_1900_-NONE-_-NONE-/",
    "Actor: EXPORT 220VOLT INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1243",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2521P0820_1900_-NONE-_-NONE- (export_220volt_brazil_make_ready_transformers_25k_2021). Signed 2021-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0820_1900_-NONE-_-NONE-/.",
    "USASpending: export_220volt_brazil_make_ready_transformers_25k_2021 USD 0.025m. Supports export_220volt_brazil_make_ready_transformers_25k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24680.0; date_signed 2021-08-23.",
)

# === Cycle 1243 ===
row_doc(
    "misc_mexico_palmas_dcr_make_ready_103k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico make-ready new DCR Palmas 1615",
    "Mexico",
    "1 Jun 2015: Department of State awards contract for MEX/FAC make-ready new DCR Palmas 1615 urgent (PoP Mexico); obligated USD 103252.78. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "103252.78", "2015-06-01", "2015", "", "",
    "IGF::OT::IGF MEX/FAC - /MAKE READY NEW DCR PALMAS 1615 URGENT, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_palmas_dcr_make_ready_103k_2015",
    "IGF::OT::IGF MEX/FAC - /MAKE READY NEW DCR PALMAS 1615 URGENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0964_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1243",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015M0964_1900_-NONE-_-NONE- (misc_mexico_palmas_dcr_make_ready_103k_2015). Signed 2015-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0964_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_palmas_dcr_make_ready_103k_2015 USD 0.103m. Supports misc_mexico_palmas_dcr_make_ready_103k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 103252.78; date_signed 2015-06-01.",
)

# === Cycle 1243 ===
row_doc(
    "misc_dominican_los_bambues_cctv_102k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic CCTV cameras monitoring system Los Bambues compound",
    "Dominican Republic",
    "2 Jun 2017: Department of State awards contract for CCTV cameras monitoring system for Los Bambues compound (PoP Dominican Republic); obligated USD 101593.47. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "101593.47", "2017-06-02", "2017", "", "",
    "IGF::CL::IGF CCTV CAMERAS MONITORING SYSTEM FOR LOS BAMBUES COMPOUND., Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_los_bambues_cctv_102k_2017",
    "IGF::CL::IGF CCTV CAMERAS MONITORING SYSTEM FOR LOS BAMBUES COMPOUND.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0588_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1243",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86017M0588_1900_-NONE-_-NONE- (misc_dominican_los_bambues_cctv_102k_2017). Signed 2017-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0588_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_los_bambues_cctv_102k_2017 USD 0.102m. Supports misc_dominican_los_bambues_cctv_102k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 101593.47; date_signed 2017-06-02.",
)

# === Cycle 1243 ===
row_doc(
    "misc_brazil_make_ready_transf_110_220_95k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil GFCIS store transformers 110V to 220V make-ready 2018",
    "Brazil",
    "14 Sep 2018: Department of State awards contract for GFCIS store transf 110V to 220V make-ready 2018 (PoP Brazil); obligated USD 94845.38. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "94845.38", "2018-09-14", "2018", "", "",
    "GFCIS - STORE - TRANSF 110V TO 220V - MAKE READY 2018, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_make_ready_transf_110_220_95k_2018",
    "GFCIS - STORE - TRANSF 110V TO 220V - MAKE READY 2018",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2518P1521_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1243",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2518P1521_1900_-NONE-_-NONE- (misc_brazil_make_ready_transf_110_220_95k_2018). Signed 2018-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2518P1521_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_make_ready_transf_110_220_95k_2018 USD 0.095m. Supports misc_brazil_make_ready_transf_110_220_95k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94845.38; date_signed 2018-09-14.",
)

# === Cycle 1244 ===
row_doc(
    "red_orange_bahamas_marine_house_cctv_23k_2020",
    "infrastructure", "building_materials", "us",
    "Red Orange North America — Bahamas Marine House CCTV",
    "Bahamas",
    "26 Jun 2020: Department of State awards contract to RED ORANGE NORTH AMERICA INC. for Marine House CCTV (PoP Bahamas); obligated USD 23074.24. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "23074.24", "2020-06-26", "2020", "", "",
    "MARINE HOUSE CCTV, Bahamas (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_red_orange_bahamas_marine_house_cctv_23k_2020",
    "MARINE HOUSE CCTV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5020P0389_1900_-NONE-_-NONE-/",
    "Actor: RED ORANGE NORTH AMERICA INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1244",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5020P0389_1900_-NONE-_-NONE- (red_orange_bahamas_marine_house_cctv_23k_2020). Signed 2020-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5020P0389_1900_-NONE-_-NONE-/.",
    "USASpending: red_orange_bahamas_marine_house_cctv_23k_2020 USD 0.023m. Supports red_orange_bahamas_marine_house_cctv_23k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 23074.24; date_signed 2020-06-26.",
)

# === Cycle 1244 ===
row_doc(
    "stateside_brazil_make_ready_transformers_22k_2025",
    "energy", "power_plants_grid", "us",
    "Stateside Procurement Services — Brazil Brasília transformers for make-ready residences",
    "Brazil",
    "27 Jan 2025: Department of State awards contract to STATESIDE PROCUREMENT SERVICES, INC. for BSB PSW transformers for make-ready residences (PoP Brazil); obligated USD 21504. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "21504", "2025-01-27", "2025", "", "",
    "BSB|PSW |TRANSFORMERS FOR MAKE READY RESIDENCES, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_stateside_brazil_make_ready_transformers_22k_2025",
    "BSB|PSW |TRANSFORMERS FOR MAKE READY RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P0314_1900_-NONE-_-NONE-/",
    "Actor: STATESIDE PROCUREMENT SERVICES (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1244",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2525P0314_1900_-NONE-_-NONE- (stateside_brazil_make_ready_transformers_22k_2025). Signed 2025-01-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P0314_1900_-NONE-_-NONE-/.",
    "USASpending: stateside_brazil_make_ready_transformers_22k_2025 USD 0.022m. Supports stateside_brazil_make_ready_transformers_22k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21504.0; date_signed 2025-01-27.",
)

# === Cycle 1244 ===
row_doc(
    "misc_brazil_make_ready_barriers_92k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil Brasília make-ready TCMR barriers",
    "Brazil",
    "20 Dec 2019: Department of State awards contract for BSB-FAC make-ready TCMR QI 05 CH 46 barriers (PoP Brazil); obligated USD 92173.88. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "92173.88", "2019-12-20", "2019", "", "",
    "BSB-FAC: MAKE READY TCMR QI 05 CH 46. BARRIERS, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_make_ready_barriers_92k_2020",
    "BSB-FAC: MAKE READY TCMR QI 05 CH 46. BARRIERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0043_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1244",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0043_1900_-NONE-_-NONE- (misc_brazil_make_ready_barriers_92k_2020). Signed 2019-12-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0043_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_make_ready_barriers_92k_2020 USD 0.092m. Supports misc_brazil_make_ready_barriers_92k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92173.88; date_signed 2019-12-20.",
)

# === Cycle 1244 ===
row_doc(
    "misc_dominican_ambassador_residence_cctv_92k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic CCTV for ambassador residence",
    "Dominican Republic",
    "14 Jul 2014: Department of State awards contract for CCTV for ambassador residence (PoP Dominican Republic); obligated USD 92256.6. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "92256.6", "2014-07-14", "2014", "", "",
    "IGF::CL::IGF FOR CLOSELY ASSOCIATED   CCTV FOR AMBASSADOR'S RESIDENCE, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_ambassador_residence_cctv_92k_2014",
    "IGF::CL::IGF FOR CLOSELY ASSOCIATED   CCTV FOR AMBASSADOR'S RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1622_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1244",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M1622_1900_-NONE-_-NONE- (misc_dominican_ambassador_residence_cctv_92k_2014). Signed 2014-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1622_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_ambassador_residence_cctv_92k_2014 USD 0.092m. Supports misc_dominican_ambassador_residence_cctv_92k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92256.6; date_signed 2014-07-14.",
)

# === Cycle 1244 ===
row_doc(
    "misc_el_salvador_rso_cctv_cameras_90k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador RSO purchase of CCTV cameras",
    "El Salvador",
    "27 Sep 2011: Department of State awards contract for RSO purchase of CCTV cameras (PoP El Salvador); obligated USD 89572.4. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "89572.4", "2011-09-27", "2011", "", "",
    "RSO PURCHASE OF CCTV CAMERAS, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_rso_cctv_cameras_90k_2011",
    "RSO PURCHASE OF CCTV CAMERAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M1150_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1244",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60011M1150_1900_-NONE-_-NONE- (misc_el_salvador_rso_cctv_cameras_90k_2011). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M1150_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_rso_cctv_cameras_90k_2011 USD 0.090m. Supports misc_el_salvador_rso_cctv_cameras_90k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89572.4; date_signed 2011-09-27.",
)

# === Cycle 1245 ===
row_doc(
    "red_orange_colombia_usms_portable_generator_15k_2020",
    "energy", "power_plants_grid", "us",
    "Red Orange North America — Colombia USMS portable power station generator",
    "Colombia",
    "10 Aug 2020: Department of State awards contract to RED ORANGE NORTH AMERICA INC. for USMS portable power station generator for USMS CFFO/FIU (PoP Colombia); obligated USD 15150. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15150", "2020-08-10", "2020", "", "",
    "USMS_PORTABLE POWER STATION GENERATOR FOR USMS CFFO/FIU, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_red_orange_colombia_usms_portable_generator_15k_2020",
    "USMS_PORTABLE POWER STATION GENERATOR FOR USMS CFFO/FIU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02020P0940_1900_-NONE-_-NONE-/",
    "Actor: RED ORANGE NORTH AMERICA INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1245",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02020P0940_1900_-NONE-_-NONE- (red_orange_colombia_usms_portable_generator_15k_2020). Signed 2020-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02020P0940_1900_-NONE-_-NONE-/.",
    "USASpending: red_orange_colombia_usms_portable_generator_15k_2020 USD 0.015m. Supports red_orange_colombia_usms_portable_generator_15k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15150.0; date_signed 2020-08-10.",
)

# === Cycle 1245 ===
row_doc(
    "vanguard_el_salvador_metal_door_screen_11k_2018",
    "infrastructure", "building_materials", "us",
    "Vanguard International — El Salvador metal door screen",
    "El Salvador",
    "25 Sep 2018: Department of State awards contract to VANGUARD INTERNATIONAL INC for metal door screen etc. (PoP El Salvador); obligated USD 10758. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "10758", "2018-09-25", "2018", "", "",
    "METAL DOOR SCREEN ETC., El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_vanguard_el_salvador_metal_door_screen_11k_2018",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P2460_1900_-NONE-_-NONE-/",
    "Actor: VANGUARD INTERNATIONAL INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1245",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P2460_1900_-NONE-_-NONE- (vanguard_el_salvador_metal_door_screen_11k_2018). Signed 2018-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P2460_1900_-NONE-_-NONE-/.",
    "USASpending: vanguard_el_salvador_metal_door_screen_11k_2018 USD 0.011m. Supports vanguard_el_salvador_metal_door_screen_11k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10758.0; date_signed 2018-09-25.",
)

# === Cycle 1245 ===
row_doc(
    "misc_argentina_fernandez_espiro_make_ready_74k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina make-ready GOP Fernandez Espiro 457 Acassuso",
    "Argentina",
    "9 Aug 2017: Department of State awards contract for make-ready for GOP Fernandez Espiro 457 Acassuso (PoP Argentina); obligated USD 74031.43. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "74031.43", "2017-08-09", "2017", "", "",
    "IGF::OT::IGF MAKE READY FOR GOP FERNANDEZ ESPIRO 457 ACASSUSO, Argentina (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_fernandez_espiro_make_ready_74k_2017",
    "IGF::OT::IGF MAKE READY FOR GOP FERNANDEZ ESPIRO 457 ACASSUSO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0529_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1245",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20017M0529_1900_-NONE-_-NONE- (misc_argentina_fernandez_espiro_make_ready_74k_2017). Signed 2017-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0529_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_fernandez_espiro_make_ready_74k_2017 USD 0.074m. Supports misc_argentina_fernandez_espiro_make_ready_74k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74031.43; date_signed 2017-08-09.",
)

# === Cycle 1245 ===
row_doc(
    "misc_argentina_dattr_make_ready_70k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina FM make-ready works at DATTR",
    "Argentina",
    "30 Aug 2016: Department of State awards contract for FM make-ready works at DATTR (PoP Argentina); obligated USD 70070.31. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "70070.31", "2016-08-30", "2016", "", "",
    "FM - MAKE READY WORKS @ DATTR IGF::OT::IGF, Argentina (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_dattr_make_ready_70k_2016",
    "FM - MAKE READY WORKS @ DATTR IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20016M0685_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1245",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20016M0685_1900_-NONE-_-NONE- (misc_argentina_dattr_make_ready_70k_2016). Signed 2016-08-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20016M0685_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_dattr_make_ready_70k_2016 USD 0.070m. Supports misc_argentina_dattr_make_ready_70k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70070.31; date_signed 2016-08-30.",
)

# === Cycle 1245 ===
row_doc(
    "misc_paraguay_msgq_make_ready_61k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay urgent FAC new MSGQ make-ready",
    "Paraguay",
    "21 Jul 2015: Department of State awards contract for urgent FAC new MSGQ make-ready (PoP Paraguay); obligated USD 60581.34. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "60581.34", "2015-07-21", "2015", "", "",
    "URGENT-FAC-NEW MSGQ MAKE READY IGF::OT::IGF, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_paraguay_msgq_make_ready_61k_2015",
    "URGENT-FAC-NEW MSGQ MAKE READY IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10015M0292_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1245",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPA10015M0292_1900_-NONE-_-NONE- (misc_paraguay_msgq_make_ready_61k_2015). Signed 2015-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10015M0292_1900_-NONE-_-NONE-/.",
    "USASpending: misc_paraguay_msgq_make_ready_61k_2015 USD 0.061m. Supports misc_paraguay_msgq_make_ready_61k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60581.34; date_signed 2015-07-21.",
)

# === Cycle 1246 ===
row_doc(
    "millenium_el_salvador_comalapa_light_tower_11k_2015",
    "energy", "power_plants_grid", "us",
    "Millenium Products — El Salvador CSL mini light tower Comalapa",
    "El Salvador",
    "24 Sep 2015: Department of State awards contract to MILLENIUM PRODUCTS, INC for CSL mini light tower for CSL Comalapa (PoP El Salvador); obligated USD 11200. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "11200", "2015-09-24", "2015", "", "",
    "CSL- MINI LIGHT TOWER FOR CSL COMALAPA, El Salvador (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_millenium_el_salvador_comalapa_light_tower_11k_2015",
    "CSL- MINI LIGHT TOWER FOR CSL COMALAPA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60015M1186_1900_-NONE-_-NONE-/",
    "Actor: MILLENIUM PRODUCTS (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1246",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60015M1186_1900_-NONE-_-NONE- (millenium_el_salvador_comalapa_light_tower_11k_2015). Signed 2015-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60015M1186_1900_-NONE-_-NONE-/.",
    "USASpending: millenium_el_salvador_comalapa_light_tower_11k_2015 USD 0.011m. Supports millenium_el_salvador_comalapa_light_tower_11k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11200.0; date_signed 2015-09-24.",
)

# === Cycle 1246 ===
row_doc(
    "trane_peru_elevator_machine_room_ac_9k_2013",
    "energy", "power_plants_grid", "us",
    "Trane U.S. — Peru replace AC R-1 for elevator machine room",
    "Peru",
    "18 Mar 2013: Department of State awards contract to TRANE U.S. INC. for replace AC R-1 for elevator machine room (PoP Peru); obligated USD 8931.76. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8931.76", "2013-03-18", "2013", "", "",
    "03/15-REPLACE AC R-1 FOR ELEVATOR MACHINE ROOM, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_trane_peru_elevator_machine_room_ac_9k_2013",
    "03/15-REPLACE AC R-1 FOR ELEVATOR MACHINE ROOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013M0793_1900_-NONE-_-NONE-/",
    "Actor: TRANE U.S. INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1246",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50013M0793_1900_-NONE-_-NONE- (trane_peru_elevator_machine_room_ac_9k_2013). Signed 2013-03-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013M0793_1900_-NONE-_-NONE-/.",
    "USASpending: trane_peru_elevator_machine_room_ac_9k_2013 USD 0.009m. Supports trane_peru_elevator_machine_room_ac_9k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8931.76; date_signed 2013-03-18.",
)

# === Cycle 1246 ===
row_doc(
    "misc_brazil_make_ready_electrical_57k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil Brasília make-ready TCMR electrical",
    "Brazil",
    "20 Dec 2019: Department of State awards contract for BSB-FAC make-ready TCMR QI 05 CH 46 electrical (PoP Brazil); obligated USD 57491.67. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "57491.67", "2019-12-20", "2019", "", "",
    "BSB-FAC: MAKE READY TCMR QI 05 CH 46. ELECTRICAL, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_make_ready_electrical_57k_2020",
    "BSB-FAC: MAKE READY TCMR QI 05 CH 46. ELECTRICAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0041_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1246",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0041_1900_-NONE-_-NONE- (misc_brazil_make_ready_electrical_57k_2020). Signed 2019-12-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0041_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_make_ready_electrical_57k_2020 USD 0.057m. Supports misc_brazil_make_ready_electrical_57k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57491.67; date_signed 2019-12-20.",
)

# === Cycle 1246 ===
row_doc(
    "misc_ecuador_make_ready_55k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador make-ready",
    "Ecuador",
    "21 Sep 2026: Department of State awards contract for make ready (PoP Ecuador); obligated USD 55040.74. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "55040.74", "2026-09-21", "2026", "", "",
    "MAKE READY, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_make_ready_55k_2026",
    "MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3026P0659_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1246",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3026P0659_1900_-NONE-_-NONE- (misc_ecuador_make_ready_55k_2026). Signed 2026-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3026P0659_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_make_ready_55k_2026 USD 0.055m. Supports misc_ecuador_make_ready_55k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 55040.74; date_signed 2026-09-21.",
)

# === Cycle 1246 ===
row_doc(
    "misc_costa_rica_cmr_make_ready_54k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica CMR/ICASS make-ready 2013",
    "Costa Rica",
    "30 Sep 2013: Department of State awards contract for CMR/ICASS make-ready 2013 (PoP Costa Rica); obligated USD 54471.78. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "54471.78", "2013-09-30", "2013", "", "",
    "CMR/ICASS 1901.0 MAKE READY 2013 IGF::CL::IGF, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_costa_rica_cmr_make_ready_54k_2013",
    "CMR/ICASS 1901.0 MAKE READY 2013 IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013C0063_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1246",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80013C0063_1900_-NONE-_-NONE- (misc_costa_rica_cmr_make_ready_54k_2013). Signed 2013-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013C0063_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_cmr_make_ready_54k_2013 USD 0.054m. Supports misc_costa_rica_cmr_make_ready_54k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 54471.78; date_signed 2013-09-30.",
)

# === Cycle 1247 ===
row_doc(
    "office_tree_bahamas_msgr_bathroom_reno_8k_2016",
    "infrastructure", "building_materials", "us",
    "Office Tree — Bahamas MSGR bathroom renovations shower enclosures",
    "Bahamas",
    "27 Sep 2016: Department of State awards contract to OFFICE TREE LLC for MSGR bathroom renovations — shower enclosures (PoP Bahamas); obligated USD 7799.94. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "7799.94", "2016-09-27", "2016", "", "",
    "MSGR BATHROOM RENOVATIONS - SHOWER ENCLOSURES, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_office_tree_bahamas_msgr_bathroom_reno_8k_2016",
    "MSGR BATHROOM RENOVATIONS - SHOWER ENCLOSURES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50016M1188_1900_-NONE-_-NONE-/",
    "Actor: OFFICE TREE LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1247",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50016M1188_1900_-NONE-_-NONE- (office_tree_bahamas_msgr_bathroom_reno_8k_2016). Signed 2016-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50016M1188_1900_-NONE-_-NONE-/.",
    "USASpending: office_tree_bahamas_msgr_bathroom_reno_8k_2016 USD 0.008m. Supports office_tree_bahamas_msgr_bathroom_reno_8k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7799.94; date_signed 2016-09-27.",
)

# === Cycle 1247 ===
row_doc(
    "york_panama_cooling_tower_vsd_7k_2012",
    "energy", "power_plants_grid", "us",
    "York International — Panama NEC variable speed drive for cooling tower",
    "Panama",
    "31 Jul 2012: Department of State awards contract to YORK INTERNATIONAL CORPORATION for variable speed drive for cooling tower — NEC (PoP Panama); obligated USD 6843. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "6843", "2012-07-31", "2012", "", "",
    "VARIABLE SPEED DRIVE FOR COOLING TOWER - NEC -7901, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_york_panama_cooling_tower_vsd_7k_2012",
    "VARIABLE SPEED DRIVE FOR COOLING TOWER - NEC -7901",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0480M001_1900_-NONE-_-NONE-/",
    "Actor: YORK INTERNATIONAL CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1247",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07011M0480M001_1900_-NONE-_-NONE- (york_panama_cooling_tower_vsd_7k_2012). Signed 2012-07-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0480M001_1900_-NONE-_-NONE-/.",
    "USASpending: york_panama_cooling_tower_vsd_7k_2012 USD 0.007m. Supports york_panama_cooling_tower_vsd_7k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6843.0; date_signed 2012-07-31.",
)

# === Cycle 1247 ===
row_doc(
    "misc_ecuador_house_make_ready_50k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador house make-ready",
    "Ecuador",
    "10 Jul 2026: Department of State awards contract for house make ready (PoP Ecuador); obligated USD 49680. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49680", "2026-07-10", "2026", "", "",
    "HOUSE MAKE READY, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_house_make_ready_50k_2026",
    "HOUSE MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3026P0427_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1247",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3026P0427_1900_-NONE-_-NONE- (misc_ecuador_house_make_ready_50k_2026). Signed 2026-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3026P0427_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_house_make_ready_50k_2026 USD 0.050m. Supports misc_ecuador_house_make_ready_50k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49680.0; date_signed 2026-07-10.",
)

# === Cycle 1247 ===
row_doc(
    "misc_argentina_villate_make_ready_46k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina make-ready works at GOP Villate 1395 Olivos",
    "Argentina",
    "19 Jul 2017: Department of State awards contract for make-ready works at GOP Villate 1395 Olivos (PoP Argentina); obligated USD 46054.53. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "46054.53", "2017-07-19", "2017", "", "",
    "IGF::OT::IGF MAKE READY WORKS AT GOP VILLATE 1395 - OLIVOS, Argentina (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_villate_make_ready_46k_2017",
    "IGF::OT::IGF MAKE READY WORKS AT GOP VILLATE 1395 - OLIVOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0471_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1247",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20017M0471_1900_-NONE-_-NONE- (misc_argentina_villate_make_ready_46k_2017). Signed 2017-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0471_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_villate_make_ready_46k_2017 USD 0.046m. Supports misc_argentina_villate_make_ready_46k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 46054.53; date_signed 2017-07-19.",
)

# === Cycle 1247 ===
row_doc(
    "misc_venezuela_dcr_make_ready_40k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela DCR make-ready",
    "Venezuela",
    "11 Jul 2011: Department of State awards contract for DCR make ready (PoP Venezuela); obligated USD 39559.66. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "39559.66", "2011-07-11", "2011", "", "",
    "DCR: MAKE READY, Venezuela (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_venezuela_dcr_make_ready_40k_2011",
    "DCR: MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0558_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1247",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30011M0558_1900_-NONE-_-NONE- (misc_venezuela_dcr_make_ready_40k_2011). Signed 2011-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0558_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_dcr_make_ready_40k_2011 USD 0.040m. Supports misc_venezuela_dcr_make_ready_40k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 39559.66; date_signed 2011-07-11.",
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
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
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
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
