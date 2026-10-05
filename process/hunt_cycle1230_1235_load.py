#!/usr/bin/env python3
"""Cycles 1230–1235: USASpending LatAm CapEx (US vendor stock + residual other).

Seeds: 20262230–20262235. Thin top-up dry.
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

# === Cycle 1230 ===
row_doc(
    "oes_mexico_psu_forced_entry_3p83m_2011",
    "infrastructure", "building_materials", "us",
    "O.E.S. — Mexico Phase II/III/IV physical security upgrade (PSU) and forced-entry/ballistic",
    "Mexico",
    "6 Sep 2011: Department of State awards task order to O.E.S., INC. for Phase II/III/IV physical security upgrade (PSU) and forced entry/ballistic (PoP Mexico); obligated USD 3831820.16. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3831820.16", "2011-09-06", "2011", "", "",
    "PHASE II/III/IV - PHYSICAL SECURITY UPGRADE (PSU) AND FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PR..., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_oes_mexico_psu_forced_entry_3p83m_2011",
    "PHASE II/III/IV - PHYSICAL SECURITY UPGRADE (PSU) AND FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT - NUEVO LAREDO, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3244_1900_SAQMMA07D0009_1900/",
    "Actor: O.E.S. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1230",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3244_1900_SAQMMA07D0009_1900 (oes_mexico_psu_forced_entry_3p83m_2011). Signed 2011-09-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3244_1900_SAQMMA07D0009_1900/.",
    "USASpending: oes_mexico_psu_forced_entry_3p83m_2011 USD 3.832m. Supports oes_mexico_psu_forced_entry_3p83m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3831820.16; date_signed 2011-09-06.",
)

# === Cycle 1230 ===
row_doc(
    "jj_maintenance_panama_pier_jet_docks_1p67m_2010",
    "infrastructure", "port_ownership", "us",
    "J & J Maintenance — Panama CN pier renovations and jet docks La Palma",
    "Panama",
    "30 Sep 2010: Department of Defense awards task order to J & J MAINTENANCE INC for CN pier renovations and jet docks, La Palma, Panama (PoP Panama); obligated USD 1671707.26. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "1671707.26", "2010-09-30", "2010", "", "",
    "CN PIER RENOVATIONS AND JET DOCKS, LA PAMA, PANAMA, Panama (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_jj_maintenance_panama_pier_jet_docks_1p67m_2010",
    "CN PIER RENOVATIONS AND JET DOCKS, LA PAMA, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0014_9700_W9127809D0068_9700/",
    "Actor: J & J MAINTENANCE INC (U.S.) — us. Official USASpending Award API. Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1230",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0014_9700_W9127809D0068_9700 (jj_maintenance_panama_pier_jet_docks_1p67m_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0014_9700_W9127809D0068_9700/.",
    "USASpending: jj_maintenance_panama_pier_jet_docks_1p67m_2010 USD 1.672m. Supports jj_maintenance_panama_pier_jet_docks_1p67m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1671707.26; date_signed 2010-09-30.",
)

# === Cycle 1230 ===
row_doc(
    "misc_colombia_tolemaida_parking_shops_renovation_1p40m_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Tolemaida parking lot and renovation of existing shops",
    "Colombia",
    "5 Sep 2012: Department of Defense awards task order for parking lot and renovation of existing shops at Tolemaida, Colombia (PoP Colombia); obligated USD 1400975.14. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "1400975.14", "2012-09-05", "2012", "", "",
    "PARKING LOT&RENOVATION OF EXISTING SHOPS AT TOLEMAIDA, COLOMBIA, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_tolemaida_parking_shops_renovation_1p40m_2012",
    "PARKING LOT&RENOVATION OF EXISTING SHOPS AT TOLEMAIDA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127809D0077_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1230",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127809D0077_9700 (misc_colombia_tolemaida_parking_shops_renovation_1p40m_2012). Signed 2012-09-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127809D0077_9700/.",
    "USASpending: misc_colombia_tolemaida_parking_shops_renovation_1p40m_2012 USD 1.401m. Supports misc_colombia_tolemaida_parking_shops_renovation_1p40m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1400975.14; date_signed 2012-09-05.",
)

# === Cycle 1230 ===
row_doc(
    "misc_honduras_renovation_1p32m_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras renovation",
    "Honduras",
    "22 Sep 2017: Department of Defense awards task order for renovation (PoP Honduras); obligated USD 1318513.95. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "1318513.95", "2017-09-22", "2017", "", "",
    "IGF::OT::IGF RENOVATION, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_renovation_1p32m_2017",
    "IGF::OT::IGF RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0219_9700_W9127816D0099_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1230",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0219_9700_W9127816D0099_9700 (misc_honduras_renovation_1p32m_2017). Signed 2017-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0219_9700_W9127816D0099_9700/.",
    "USASpending: misc_honduras_renovation_1p32m_2017 USD 1.319m. Supports misc_honduras_renovation_1p32m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1318513.95; date_signed 2017-09-22.",
)

# === Cycle 1230 ===
row_doc(
    "misc_colombia_brcna_cucuta_renovations_1p18m_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia BRCNA Cúcuta renovations",
    "Colombia",
    "5 Jul 2022: Department of State awards task order for BRCNA Cúcuta renovations (PoP Colombia); obligated USD 1184064.26. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "1184064.26", "2022-07-05", "2022", "", "",
    "BRCNA CUCUTA RENOVATIONS, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_brcna_cucuta_renovations_1p18m_2022",
    "BRCNA CUCUTA RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1806_1900_19AQMM21D0037_1900/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1230",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F1806_1900_19AQMM21D0037_1900 (misc_colombia_brcna_cucuta_renovations_1p18m_2022). Signed 2022-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1806_1900_19AQMM21D0037_1900/.",
    "USASpending: misc_colombia_brcna_cucuta_renovations_1p18m_2022 USD 1.184m. Supports misc_colombia_brcna_cucuta_renovations_1p18m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1184064.26; date_signed 2022-07-05.",
)

# === Cycle 1231 ===
row_doc(
    "horizon_havana_embassy_space_renovation_1p22m_2023",
    "infrastructure", "building_materials", "us",
    "Horizon Construction Group — Havana U.S. Embassy space renovation",
    "Cuba",
    "20 Sep 2023: Department of State awards task order to HORIZON CONSTRUCTION GROUP/INTERNATIONAL for space renovation U.S. Embassy Havana, Cuba (PoP Cuba); obligated USD 1217362.37. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "1217362.37", "2023-09-20", "2023", "", "",
    "SPACE RENOVATION US EMBASSY HAVANA CUBA, Cuba (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_horizon_havana_embassy_space_renovation_1p22m_2023",
    "SPACE RENOVATION US EMBASSY HAVANA CUBA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2980_1900_19AQMM22D0063_1900/",
    "Actor: HORIZON CONSTRUCTION GROUP/INTERNATIONAL CONSTRUCTION SERVICES JV (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1231",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F2980_1900_19AQMM22D0063_1900 (horizon_havana_embassy_space_renovation_1p22m_2023). Signed 2023-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2980_1900_19AQMM22D0063_1900/.",
    "USASpending: horizon_havana_embassy_space_renovation_1p22m_2023 USD 1.217m. Supports horizon_havana_embassy_space_renovation_1p22m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1217362.37; date_signed 2023-09-20.",
)

# === Cycle 1231 ===
row_doc(
    "wells_global_bahamas_south_bimini_generator_807k_2025",
    "energy", "power_plants_grid", "us",
    "Wells Global — Bahamas South Bimini engine generator installation",
    "Bahamas",
    "5 Aug 2025: Department of Transportation awards task order to WELLS GLOBAL, LLC for F&E funded engine generator installation at South Bimini (ZBV) (PoP Bahamas); obligated USD 806951.18. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "806951.18", "2025-08-05", "2025", "", "",
    "F&E FUNDED ENGINE GENERATOR INSTALLATION, SITE SPECIFIC: SOUTH BIMINI (ZBV) VOR, BAHAMAS-BHS, JCN..., Bahamas (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_wells_global_bahamas_south_bimini_generator_807k_2025",
    "F&E FUNDED ENGINE GENERATOR INSTALLATION, SITE SPECIFIC: SOUTH BIMINI (ZBV) VOR, BAHAMAS-BHS, JCN:22005476, PER ELD PMO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_6973GH25F01203_6920_6973GH22D00017_6920/",
    "Actor: WELLS GLOBAL (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1231",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_6973GH25F01203_6920_6973GH22D00017_6920 (wells_global_bahamas_south_bimini_generator_807k_2025). Signed 2025-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_6973GH25F01203_6920_6973GH22D00017_6920/.",
    "USASpending: wells_global_bahamas_south_bimini_generator_807k_2025 USD 0.807m. Supports wells_global_bahamas_south_bimini_generator_807k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 806951.18; date_signed 2025-08-05.",
)

# === Cycle 1231 ===
row_doc(
    "misc_honduras_metal_dorms_renovation_1p06m_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras renovation of metal dorms N-62–N-64",
    "Honduras",
    "29 Sep 2011: Department of Defense awards task order for renovation of metal dorms (N-62–N-64) (PoP Honduras); obligated USD 1060680.98. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "1060680.98", "2011-09-29", "2011", "", "",
    "TAS::21 2020::TAS RENOVATION OF METAL DORMS (N-62--N-64), Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_metal_dorms_renovation_1p06m_2011",
    "TAS::21 2020::TAS RENOVATION OF METAL DORMS (N-62--N-64)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127811D0046_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1231",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127811D0046_9700 (misc_honduras_metal_dorms_renovation_1p06m_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127811D0046_9700/.",
    "USASpending: misc_honduras_metal_dorms_renovation_1p06m_2011 USD 1.061m. Supports misc_honduras_metal_dorms_renovation_1p06m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1060680.98; date_signed 2011-09-29.",
)

# === Cycle 1231 ===
row_doc(
    "misc_paraguay_motor_pool_barracks_renovation_958k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay design and construction motor pool/barracks renovation",
    "Paraguay",
    "5 Mar 2012: Department of Defense awards task order for design and construction motor pool/barracks renovation (PoP Paraguay); obligated USD 958149.59. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "958149.59", "2012-03-05", "2012", "", "",
    "TAS::21 2050::TAS DESIGN AND CONSTRUCTION MOTOR POOL/BARRACKS RENOVATION ASUNCION, PARAGUAY, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_paraguay_motor_pool_barracks_renovation_958k_2012",
    "TAS::21 2050::TAS DESIGN AND CONSTRUCTION MOTOR POOL/BARRACKS RENOVATION ASUNCION, PARAGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0078_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1231",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0012_9700_W9127809D0078_9700 (misc_paraguay_motor_pool_barracks_renovation_958k_2012). Signed 2012-03-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0078_9700/.",
    "USASpending: misc_paraguay_motor_pool_barracks_renovation_958k_2012 USD 0.958m. Supports misc_paraguay_motor_pool_barracks_renovation_958k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 958149.59; date_signed 2012-03-05.",
)

# === Cycle 1231 ===
row_doc(
    "misc_honduras_soto_cano_hvac_renovation_948k_2014",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras HVAC renovation at Soto Cano",
    "Honduras",
    "19 Sep 2014: Department of Defense awards task order for HVAC renovation at Soto Cano, Honduras (PoP Honduras); obligated USD 948076.11. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "948076.11", "2014-09-19", "2014", "", "",
    "IGF::OT::IGF  HVAC RENOVATION AT SOTO CANO, HONDURAS, Honduras (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_soto_cano_hvac_renovation_948k_2014",
    "IGF::OT::IGF  HVAC RENOVATION AT SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0018_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1231",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127813D0018_9700 (misc_honduras_soto_cano_hvac_renovation_948k_2014). Signed 2014-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0018_9700/.",
    "USASpending: misc_honduras_soto_cano_hvac_renovation_948k_2014 USD 0.948m. Supports misc_honduras_soto_cano_hvac_renovation_948k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 948076.11; date_signed 2014-09-19.",
)

# === Cycle 1232 ===
row_doc(
    "hsu_brazil_rio_pcc_generator_replacement_569k_2015",
    "energy", "power_plants_grid", "us",
    "HSU Development — Brazil Rio de Janeiro PCC generator system replacement",
    "Brazil",
    "13 Jul 2015: Department of State awards task order to HSU DEVELOPMENT, INC. for design-build replacement of PCC generator system in Rio de Janeiro (PoP Brazil); obligated USD 568972. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "568972", "2015-07-13", "2015", "", "",
    "DESIGN BUILD SERVICES FOR THE REPLACEMENT OF PCC GENERATOR SYSTEM IN RIO DE JANEIRO, BRAZIL IGF::..., Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_hsu_brazil_rio_pcc_generator_replacement_569k_2015",
    "DESIGN BUILD SERVICES FOR THE REPLACEMENT OF PCC GENERATOR SYSTEM IN RIO DE JANEIRO, BRAZIL IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1968_1900_SAQMMA14D0058_1900/",
    "Actor: HSU DEVELOPMENT (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1232",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F1968_1900_SAQMMA14D0058_1900 (hsu_brazil_rio_pcc_generator_replacement_569k_2015). Signed 2015-07-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1968_1900_SAQMMA14D0058_1900/.",
    "USASpending: hsu_brazil_rio_pcc_generator_replacement_569k_2015 USD 0.569m. Supports hsu_brazil_rio_pcc_generator_replacement_569k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 568972.0; date_signed 2015-07-13.",
)

# === Cycle 1232 ===
row_doc(
    "us21_panama_inl_cctv_access_alarm_561k_2022",
    "infrastructure", "building_materials", "us",
    "US21 — Panama INL CCTV, access control and alarm system",
    "Panama",
    "23 Sep 2022: Department of State awards contract to US21 INC for CCTV, access control and alarm system for INL Panama (PoP Panama); obligated USD 561419.74. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "561419.74", "2022-09-23", "2022", "", "",
    "CCTV, ACCESS CONTROL AND ALARM SYSTEM FOR INL PANAMA, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_us21_panama_inl_cctv_access_alarm_561k_2022",
    "CCTV, ACCESS CONTROL AND ALARM SYSTEM FOR INL PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22C0007_1900_-NONE-_-NONE-/",
    "Actor: US21 INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1232",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22C0007_1900_-NONE-_-NONE- (us21_panama_inl_cctv_access_alarm_561k_2022). Signed 2022-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22C0007_1900_-NONE-_-NONE-/.",
    "USASpending: us21_panama_inl_cctv_access_alarm_561k_2022 USD 0.561m. Supports us21_panama_inl_cctv_access_alarm_561k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 561419.74; date_signed 2022-09-23.",
)

# === Cycle 1232 ===
row_doc(
    "misc_mexico_nld_residence_make_ready_803k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico NLD/GSO/OBO/PO residence make-ready 2021",
    "Mexico",
    "30 Jul 2021: Department of State awards contract for NLD/GSO/OBO/PO residence make-ready/2021 (PoP Mexico); obligated USD 803104.05. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "803104.05", "2021-07-30", "2021", "", "",
    "NLD/GSO/OBO/PO RESIDENCE MAKE READY/2021, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_nld_residence_make_ready_803k_2021",
    "NLD/GSO/OBO/PO RESIDENCE MAKE READY/2021",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6121P0166_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1232",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6121P0166_1900_-NONE-_-NONE- (misc_mexico_nld_residence_make_ready_803k_2021). Signed 2021-07-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6121P0166_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nld_residence_make_ready_803k_2021 USD 0.803m. Supports misc_mexico_nld_residence_make_ready_803k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 803104.05; date_signed 2021-07-30.",
)

# === Cycle 1232 ===
row_doc(
    "misc_honduras_ups_joc_battery_building_792k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras design and construction of UPS JOC battery building",
    "Honduras",
    "24 Sep 2024: Department of Defense awards task order for design and construction of UPS JOC battery building (PoP Honduras); obligated USD 792397.48. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "792397.48", "2024-09-24", "2024", "", "",
    "DESIGN AND CONSTRUCTION OF UPS JOC BATTERY BUILDING, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_ups_joc_battery_building_792k_2024",
    "DESIGN AND CONSTRUCTION OF UPS JOC BATTERY BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0328_9700_W9127823D0073_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1232",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0328_9700_W9127823D0073_9700 (misc_honduras_ups_joc_battery_building_792k_2024). Signed 2024-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0328_9700_W9127823D0073_9700/.",
    "USASpending: misc_honduras_ups_joc_battery_building_792k_2024 USD 0.792m. Supports misc_honduras_ups_joc_battery_building_792k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 792397.48; date_signed 2024-09-24.",
)

# === Cycle 1232 ===
row_doc(
    "misc_honduras_sierra_tanks_soto_cano_785k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras renovation of Sierra tanks Soto Cano Air Base",
    "Honduras",
    "17 Sep 2018: Department of Defense awards task order for renovation of Sierra tanks, Soto Cano Air Base, Honduras (PoP Honduras); obligated USD 785034.31. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "785034.31", "2018-09-17", "2018", "", "",
    "RENOVATION OF SIERRA TANKS, SOTO CANO AIR BASE, HONDURAS, Honduras (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_sierra_tanks_soto_cano_785k_2018",
    "RENOVATION OF SIERRA TANKS, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0537_9700_W9127816D0099_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1232",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0537_9700_W9127816D0099_9700 (misc_honduras_sierra_tanks_soto_cano_785k_2018). Signed 2018-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0537_9700_W9127816D0099_9700/.",
    "USASpending: misc_honduras_sierra_tanks_soto_cano_785k_2018 USD 0.785m. Supports misc_honduras_sierra_tanks_soto_cano_785k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 785034.31; date_signed 2018-09-17.",
)

# === Cycle 1233 ===
row_doc(
    "hsu_bahamas_nassau_pcc_isc_server_room_542k_2015",
    "infrastructure", "building_materials", "us",
    "HSU Development — Bahamas Nassau PCC and ISC server room upgrades",
    "Bahamas",
    "18 Sep 2015: Department of State awards task order to HSU DEVELOPMENT, INC. for FAC design/build services for PCC and ISC server room upgrades at U.S. Embassy Nassau (PoP Bahamas); obligated USD 541975.65. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "541975.65", "2015-09-18", "2015", "", "",
    "IGF::OT::IGF HSU DEVELOPMENT INC. - SAQMMA14D0058- TO: SAQMMA15F3219 - FAC DESIGN/BUILD SERVICES ..., Bahamas (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_hsu_bahamas_nassau_pcc_isc_server_room_542k_2015",
    "IGF::OT::IGF HSU DEVELOPMENT INC. - SAQMMA14D0058- TO: SAQMMA15F3219 - FAC DESIGN/BUILD SERVICES FOR PCC AND ISC SERVER ROOM UPGRADES - US EMBASSY NASSAU, BAHAMAS - PERIOD OF PERFORMANCE: 09/18/2015 TO 04/25/2016",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F3219_1900_SAQMMA14D0058_1900/",
    "Actor: HSU DEVELOPMENT (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1233",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F3219_1900_SAQMMA14D0058_1900 (hsu_bahamas_nassau_pcc_isc_server_room_542k_2015). Signed 2015-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F3219_1900_SAQMMA14D0058_1900/.",
    "USASpending: hsu_bahamas_nassau_pcc_isc_server_room_542k_2015 USD 0.542m. Supports hsu_bahamas_nassau_pcc_isc_server_room_542k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 541975.65; date_signed 2015-09-18.",
)

# === Cycle 1233 ===
row_doc(
    "alban_tractor_haiti_generators_513k_2010",
    "energy", "power_plants_grid", "us",
    "Alban Tractor — Haiti generators",
    "Haiti",
    "22 Feb 2010: Department of Defense awards contract to ALBAN TRACTOR, LLC for generators (PoP Haiti); obligated USD 512833.75. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "512833.75", "2010-02-22", "2010", "", "",
    "GENERATORS (FIRM PERIOD, 84 DAYS), Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_alban_tractor_haiti_generators_513k_2010",
    "GENERATORS (FIRM PERIOD, 84 DAYS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003310P9017_9700_-NONE-_-NONE-/",
    "Actor: ALBAN TRACTOR (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1233",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N0003310P9017_9700_-NONE-_-NONE- (alban_tractor_haiti_generators_513k_2010). Signed 2010-02-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003310P9017_9700_-NONE-_-NONE-/.",
    "USASpending: alban_tractor_haiti_generators_513k_2010 USD 0.513m. Supports alban_tractor_haiti_generators_513k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 512833.75; date_signed 2010-02-22.",
)

# === Cycle 1233 ===
row_doc(
    "misc_mexico_nld_residence_make_ready_750k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico NLD/GSO/OBO/PO residence make-ready 2021 (2022 award)",
    "Mexico",
    "31 Mar 2022: Department of State awards contract for NLD/GSO/OBO/PO residence make-ready/2021 (PoP Mexico); obligated USD 750000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "750000", "2022-03-31", "2022", "", "",
    "NLD/GSO/OBO/PO RESIDENCE MAKE READY/2021, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_nld_residence_make_ready_750k_2022",
    "NLD/GSO/OBO/PO RESIDENCE MAKE READY/2021",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6122P0083_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1233",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6122P0083_1900_-NONE-_-NONE- (misc_mexico_nld_residence_make_ready_750k_2022). Signed 2022-03-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6122P0083_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nld_residence_make_ready_750k_2022 USD 0.750m. Supports misc_mexico_nld_residence_make_ready_750k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 750000.0; date_signed 2022-03-31.",
)

# === Cycle 1233 ===
row_doc(
    "misc_el_salvador_diesel_generator_water_well_735k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — El Salvador diesel generator and water well",
    "El Salvador",
    "30 Sep 2012: Department of Defense awards task order for diesel generator and water well (PoP El Salvador); obligated USD 735485.84. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "735485.84", "2012-09-30", "2012", "", "",
    "DIESEL GENERATOR AND WATER WELL, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_diesel_generator_water_well_735k_2012",
    "DIESEL GENERATOR AND WATER WELL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127809D0064_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1233",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127809D0064_9700 (misc_el_salvador_diesel_generator_water_well_735k_2012). Signed 2012-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127809D0064_9700/.",
    "USASpending: misc_el_salvador_diesel_generator_water_well_735k_2012 USD 0.735m. Supports misc_el_salvador_diesel_generator_water_well_735k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 735485.84; date_signed 2012-09-30.",
)

# === Cycle 1233 ===
row_doc(
    "misc_honduras_dorm_l02_l04_renovation_733k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras renovation of dorm L-02 and L-04",
    "Honduras",
    "29 Sep 2011: Department of Defense awards task order for renovation of dorm L-02 and L-04 (PoP Honduras); obligated USD 733013.66. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "733013.66", "2011-09-29", "2011", "", "",
    "TAS::21 2020::TAS RENOVATION OF DORM L-02 AND L-04, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_dorm_l02_l04_renovation_733k_2011",
    "TAS::21 2020::TAS RENOVATION OF DORM L-02 AND L-04",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127811D0046_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1233",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0012_9700_W9127811D0046_9700 (misc_honduras_dorm_l02_l04_renovation_733k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127811D0046_9700/.",
    "USASpending: misc_honduras_dorm_l02_l04_renovation_733k_2011 USD 0.733m. Supports misc_honduras_dorm_l02_l04_renovation_733k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 733013.66; date_signed 2011-09-29.",
)

# === Cycle 1234 ===
row_doc(
    "hsu_mexico_city_sprinkler_office_renovation_450k_2018",
    "infrastructure", "building_materials", "us",
    "HSU Development — Mexico City embassy fire sprinkler replacement and office renovation",
    "Mexico",
    "19 Sep 2018: Department of State awards task order to HSU DEVELOPMENT, INC. for FAC fire sprinkler replacement and office renovation U.S. Embassy Mexico City (PoP Mexico); obligated USD 449931.37. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "449931.37", "2018-09-19", "2018", "", "",
    "FAC FIRE SPRINKLER REPLACEMENT AND OFFICE RENOVATION US EMBASSY MEXICO CITY, MEXICO, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_hsu_mexico_city_sprinkler_office_renovation_450k_2018",
    "FAC FIRE SPRINKLER REPLACEMENT AND OFFICE RENOVATION US EMBASSY MEXICO CITY, MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F3573_1900_SAQMMA14D0058_1900/",
    "Actor: HSU DEVELOPMENT (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1234",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F3573_1900_SAQMMA14D0058_1900 (hsu_mexico_city_sprinkler_office_renovation_450k_2018). Signed 2018-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F3573_1900_SAQMMA14D0058_1900/.",
    "USASpending: hsu_mexico_city_sprinkler_office_renovation_450k_2018 USD 0.450m. Supports hsu_mexico_city_sprinkler_office_renovation_450k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 449931.37; date_signed 2018-09-19.",
)

# === Cycle 1234 ===
row_doc(
    "koniag_haiti_esps_installation_441k_2013",
    "infrastructure", "building_materials", "us",
    "Koniag Technology Solutions — Haiti environmental security protection system installation",
    "Haiti",
    "29 Sep 2013: Department of State awards task order to KONIAG TECHNOLOGY SOLUTIONS INC for installation of an environmental security protection system (PoP Haiti); obligated USD 440565.07. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "440565.07", "2013-09-29", "2013", "", "",
    "IGF::CL::IGF  INSTALLATION OF AN ENVIRONMENTAL SECURITY PROTECTION SYSTEM IN THE US EMBASSY LOCAT..., Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_koniag_haiti_esps_installation_441k_2013",
    "IGF::CL::IGF  INSTALLATION OF AN ENVIRONMENTAL SECURITY PROTECTION SYSTEM IN THE US EMBASSY LOCATED IN PORT AU PRINCE, HAITI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F4029_1900_SAQMMA13D0121_1900/",
    "Actor: KONIAG TECHNOLOGY SOLUTIONS INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1234",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F4029_1900_SAQMMA13D0121_1900 (koniag_haiti_esps_installation_441k_2013). Signed 2013-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F4029_1900_SAQMMA13D0121_1900/.",
    "USASpending: koniag_haiti_esps_installation_441k_2013 USD 0.441m. Supports koniag_haiti_esps_installation_441k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 440565.07; date_signed 2013-09-29.",
)

# === Cycle 1234 ===
row_doc(
    "misc_colombia_larandia_cctv_infrastructure_714k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia CCTV cameras and infrastructure Larandia",
    "Colombia",
    "27 Sep 2010: Department of Defense awards contract for CCTV cameras and infrastructure Larandia (PoP Colombia); obligated USD 713727.02. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "713727.02", "2010-09-27", "2010", "", "",
    "CCTV CAMERAS&INFRASTRUCTURE LARANDIA, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_larandia_cctv_infrastructure_714k_2010",
    "CCTV CAMERAS&INFRASTRUCTURE LARANDIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0049_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1234",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0049_9700_-NONE-_-NONE- (misc_colombia_larandia_cctv_infrastructure_714k_2010). Signed 2010-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0049_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_larandia_cctv_infrastructure_714k_2010 USD 0.714m. Supports misc_colombia_larandia_cctv_infrastructure_714k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 713727.02; date_signed 2010-09-27.",
)

# === Cycle 1234 ===
row_doc(
    "misc_haiti_embassy_generator_engines_665k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti replacement engines for American Embassy generators",
    "Haiti",
    "30 Aug 2013: Department of State awards contract for replacement engines for American Embassy generators (PoP Haiti); obligated USD 665350.71. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "665350.71", "2013-08-30", "2013", "", "",
    "REPLACEMENT ENGINES FOR AMERICAN EMBASSY GENERATORS., Haiti (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_embassy_generator_engines_665k_2013",
    "REPLACEMENT ENGINES FOR AMERICAN EMBASSY GENERATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC13M0015_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1234",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC13M0015_1900_-NONE-_-NONE- (misc_haiti_embassy_generator_engines_665k_2013). Signed 2013-08-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC13M0015_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_embassy_generator_engines_665k_2013 USD 0.665m. Supports misc_haiti_embassy_generator_engines_665k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 665350.71; date_signed 2013-08-30.",
)

# === Cycle 1234 ===
row_doc(
    "misc_colombia_cefop_cucuta_construction_637k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia CEFOP Cúcuta construction and upgrades",
    "Colombia",
    "23 Sep 2015: Department of State awards contract for CEFOP Colombia Cúcuta construction and upgrades (PoP Colombia); obligated USD 636673.58. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "636673.58", "2015-09-23", "2015", "", "",
    "CEFOP COLOMBIA CUCUTA CONSTRUCTION AND UPGRADES IGF::OT::IGF, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_cefop_cucuta_construction_637k_2015",
    "CEFOP COLOMBIA CUCUTA CONSTRUCTION AND UPGRADES IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1234",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15C0006_1900_-NONE-_-NONE- (misc_colombia_cefop_cucuta_construction_637k_2015). Signed 2015-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15C0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_cefop_cucuta_construction_637k_2015 USD 0.637m. Supports misc_colombia_cefop_cucuta_construction_637k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 636673.58; date_signed 2015-09-23.",
)

# === Cycle 1235 ===
row_doc(
    "reagent_world_honduras_ac_ventilation_375k_2018",
    "energy", "power_plants_grid", "us",
    "Reagent World — Honduras AC systems and ventilation",
    "Honduras",
    "28 Sep 2018: Department of State awards contract to REAGENT WORLD, INC. for AC systems and ventilation, Honduras (PoP Honduras); obligated USD 374750. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "374750", "2018-09-28", "2018", "", "",
    "AC SYSTEMS AND VENTILATION, HONDURAS, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_reagent_world_honduras_ac_ventilation_375k_2018",
    "AC SYSTEMS AND VENTILATION, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0233_1900_-NONE-_-NONE-/",
    "Actor: REAGENT WORLD (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1235",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0233_1900_-NONE-_-NONE- (reagent_world_honduras_ac_ventilation_375k_2018). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0233_1900_-NONE-_-NONE-/.",
    "USASpending: reagent_world_honduras_ac_ventilation_375k_2018 USD 0.375m. Supports reagent_world_honduras_ac_ventilation_375k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 374750.0; date_signed 2018-09-28.",
)

# === Cycle 1235 ===
row_doc(
    "waypoint_chile_50kw_generator_368k_2024",
    "energy", "power_plants_grid", "us",
    "Waypoint — Chile 50 kW generator",
    "Chile",
    "27 Aug 2024: Department of Defense awards contract to WAYPOINT LLC for 50 kilowatt generator (PoP Chile); obligated USD 367696.1. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "367696.1", "2024-08-27", "2024", "", "",
    "50 KILOWATT GENERATOR -, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_waypoint_chile_50kw_generator_368k_2024",
    "50 KILOWATT GENERATOR -",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710024F0024_9700_N6264921D0034_9700/",
    "Actor: WAYPOINT LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1235",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_M2710024F0024_9700_N6264921D0034_9700 (waypoint_chile_50kw_generator_368k_2024). Signed 2024-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710024F0024_9700_N6264921D0034_9700/.",
    "USASpending: waypoint_chile_50kw_generator_368k_2024 USD 0.368m. Supports waypoint_chile_50kw_generator_368k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 367696.1; date_signed 2024-08-27.",
)

# === Cycle 1235 ===
row_doc(
    "misc_nicaragua_bluefields_hospital_renovation_630k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Nicaragua hospital renovation Bluefields",
    "Nicaragua",
    "28 Sep 2013: Department of Defense awards task order for hospital renovation Bluefields, Nicaragua (PoP Nicaragua); obligated USD 630227.31. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "630227.31", "2013-09-28", "2013", "", "",
    "IGF::OT::IGF  HOSPITAL RENOVATION BLUEFIELDS NICARAGUA, Nicaragua (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_nicaragua_bluefields_hospital_renovation_630k_2013",
    "IGF::OT::IGF  HOSPITAL RENOVATION BLUEFIELDS NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0014_9700/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1235",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127813D0014_9700 (misc_nicaragua_bluefields_hospital_renovation_630k_2013). Signed 2013-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0014_9700/.",
    "USASpending: misc_nicaragua_bluefields_hospital_renovation_630k_2013 USD 0.630m. Supports misc_nicaragua_bluefields_hospital_renovation_630k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 630227.31; date_signed 2013-09-28.",
)

# === Cycle 1235 ===
row_doc(
    "misc_guatemala_barracks_renovations_electrical_615k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala barracks renovations and electrical",
    "Guatemala",
    "9 Apr 2019: Department of Defense awards contract for barracks renovations and electrical (PoP Guatemala); obligated USD 615108. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "615108", "2019-04-09", "2019", "", "",
    "BARRACKS RENOVATIONS AND ELECTRICAL, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_barracks_renovations_electrical_615k_2019",
    "BARRACKS RENOVATIONS AND ELECTRICAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM19C0002_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1235",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM19C0002_9700_-NONE-_-NONE- (misc_guatemala_barracks_renovations_electrical_615k_2019). Signed 2019-04-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM19C0002_9700_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_barracks_renovations_electrical_615k_2019 USD 0.615m. Supports misc_guatemala_barracks_renovations_electrical_615k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 615108.0; date_signed 2019-04-09.",
)

# === Cycle 1235 ===
row_doc(
    "misc_colombia_villagarzon_tumaco_ops_rooms_reno_579k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia renovation of operations rooms in Villagarzón and Tumaco",
    "Colombia",
    "17 Dec 2018: Department of State awards contract for renovation of operations rooms in Villagarzón and Tumaco, Colombia (PoP Colombia); obligated USD 578608.31. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "578608.31", "2018-12-17", "2018", "", "",
    "RENOVATION OF OPERATIONS ROOMS IN VILLAGARZON AND TUMACO, COLOMBIA, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_villagarzon_tumaco_ops_rooms_reno_579k_2018",
    "RENOVATION OF OPERATIONS ROOMS IN VILLAGARZON AND TUMACO, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0020_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1235",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0020_1900_-NONE-_-NONE- (misc_colombia_villagarzon_tumaco_ops_rooms_reno_579k_2018). Signed 2018-12-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0020_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_villagarzon_tumaco_ops_rooms_reno_579k_2018 USD 0.579m. Supports misc_colombia_villagarzon_tumaco_ops_rooms_reno_579k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 578608.31; date_signed 2018-12-17.",
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
