#!/usr/bin/env python3
"""Cycles 1319–1323: USASpending LatAm CapEx (Viken/Alutiiq/Smiths + Eterna/Marago/Estudios EPC).

Seeds: 20262319–20262323. Thin top-up dry.
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

# === Cycle 1319 ===
row_doc(
    "viken_costarica_mobile_scanners_3088k_2025",
    "infrastructure", "port_cranes", "us",
    "Viken Detection — Costa Rica mobile scanners",
    "Costa Rica",
    "21 Aug 2025: Department of State awards contract to VIKEN DETECTION CORPORATION for mobile scanners, warranty, maintenance, and training (CapEx face = award obligation); obligated USD 3087755.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3087755.00", "2025-08-21", "2025", "", "",
    "NEW CONTRACT IN THE AMOUNT OF $2,019,100, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_viken_costarica_mobile_scanners_3088k_2025",
    "NEW CONTRACT IN THE AMOUNT OF $2,019,100.00 FOR MOBILE SCANNERS, WARRANTY, MAINTENANCE, AND TRAINING, WITH A PERFORMANCE PERIOD OF 08/25/2025 THROUGH 08/24/2026. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY SAN JOSE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE25C0033_1900_-NONE-_-NONE-/",
    "Actor: VIKEN DETECTION CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle port_cranes; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1319",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE25C0033_1900_-NONE-_-NONE- (viken_costarica_mobile_scanners_3088k_2025). Signed 2025-08-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE25C0033_1900_-NONE-_-NONE-/.",
    "USASpending: viken_costarica_mobile_scanners_3088k_2025 USD 3.088m. Supports viken_costarica_mobile_scanners_3088k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3087755.0; date_signed 2025-08-21.",
    investment_type="equipment_supply",
)

# === Cycle 1319 ===
row_doc(
    "alutiiq_ecuador_it_equipment_install_566k_2024",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Ecuador IT equipment installation",
    "Ecuador",
    "8 Apr 2024: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT equipment, installation, and training; obligated USD 566126.02. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "566126.02", "2024-04-08", "2024", "", "",
    "NEW TASK ORDER IN THE AMOUNT OF $566,126, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_ecuador_it_equipment_install_566k_2024",
    "NEW TASK ORDER IN THE AMOUNT OF $566,126.02 FOR IT EQUIPMENT, INSTALLATION, AND TRAINING, WITH A PERIOD OF PERFORMANCE OF 04/08/2024 THROUGH 04/07/2025. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0018_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1319",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0018_1900_19AQMM20D0010_1900 (alutiiq_ecuador_it_equipment_install_566k_2024). Signed 2024-04-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0018_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_ecuador_it_equipment_install_566k_2024 USD 0.566m. Supports alutiiq_ecuador_it_equipment_install_566k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 566126.02; date_signed 2024-04-08.",
    investment_type="equipment_supply",
)

# === Cycle 1319 ===
row_doc(
    "eterna_honduras_ueph_housing_18977k_2019",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano unaccompanied enlisted personnel housing",
    "Honduras",
    "13 Jun 2019: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for unaccompanied enlisted personnel housing Soto Cano Air Base, Honduras; obligated USD 18976737.74. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18976737.74", "2019-06-13", "2019", "", "",
    "UNACCOMPANIED ENLISTED PERSONNEL HOUSING SOTO CANO AIR BASE, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_ueph_housing_18977k_2019",
    "UNACCOMPANIED ENLISTED PERSONNEL HOUSING SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819C0019_9700_-NONE-_-NONE-/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1319",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819C0019_9700_-NONE-_-NONE- (eterna_honduras_ueph_housing_18977k_2019). Signed 2019-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819C0019_9700_-NONE-_-NONE-/.",
    "USASpending: eterna_honduras_ueph_housing_18977k_2019 USD 18.977m. Supports eterna_honduras_ueph_housing_18977k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18976737.74; date_signed 2019-06-13.",
    investment_type="epc",
)

# === Cycle 1319 ===
row_doc(
    "palgag_haiti_les_cayes_community_clusters_3089k_2010",
    "infrastructure", "building_materials", "other",
    "Palgag Building Technologies — Haiti Les Cayes community clusters",
    "Haiti",
    "6 Dec 2010: Department of State awards contract to PALGAG BUILDING TECHNOLOGIES LTD for community clusters; Les Cayes, Haiti; obligated USD 3089281.43. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3089281.43", "2010-12-06", "2010", "", "",
    "COMMUNITY CLUSTERS; LES CAYES, HAITI, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_palgag_haiti_les_cayes_community_clusters_3089k_2010",
    "COMMUNITY CLUSTERS; LES CAYES, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0028_9700_-NONE-_-NONE-/",
    "Actor: PALGAG BUILDING TECHNOLOGIES LTD — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1319",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0028_9700_-NONE-_-NONE- (palgag_haiti_les_cayes_community_clusters_3089k_2010). Signed 2010-12-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0028_9700_-NONE-_-NONE-/.",
    "USASpending: palgag_haiti_les_cayes_community_clusters_3089k_2010 USD 3.089m. Supports palgag_haiti_les_cayes_community_clusters_3089k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3089281.43; date_signed 2010-12-06.",
    investment_type="epc",
)

# === Cycle 1319 ===
row_doc(
    "eterna_panama_pier_repair_2796k_2015",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Panama pier repair",
    "Panama",
    "29 Sep 2015: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for Panama pier repair; obligated USD 2796045.39. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2796045.39", "2015-09-29", "2015", "", "",
    "IGF::OT::IGF PANAMA PEIR REPAIR, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_panama_pier_repair_2796k_2015",
    "IGF::OT::IGF PANAMA PEIR REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127815C0024_9700_-NONE-_-NONE-/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1319",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127815C0024_9700_-NONE-_-NONE- (eterna_panama_pier_repair_2796k_2015). Signed 2015-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127815C0024_9700_-NONE-_-NONE-/.",
    "USASpending: eterna_panama_pier_repair_2796k_2015 USD 2.796m. Supports eterna_panama_pier_repair_2796k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2796045.39; date_signed 2015-09-29.",
    investment_type="epc",
)

# === Cycle 1320 ===
row_doc(
    "dre_mexico_chihuahua_xray_177k_2016",
    "infrastructure", "engineering_epc", "us",
    "D.R.E. Medical Group — Mexico Chihuahua x-ray machine",
    "Mexico",
    "15 Jul 2016: Department of State awards contract to D.R.E. MEDICAL GROUP, INC. for x-ray machine for Chihuahua FEEPYMJ and SEDENA; obligated USD 176953.96. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "176953.96", "2016-07-15", "2016", "", "",
    "INL-IN23MX87-X-RAY MACHINE FOR CHIHUAHA FEEPYMJ AND SEDENA IGF::OT::IGF, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_dre_mexico_chihuahua_xray_177k_2016",
    "INL-IN23MX87-X-RAY MACHINE FOR CHIHUAHA FEEPYMJ AND SEDENA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90016M0264_1900_-NONE-_-NONE-/",
    "Actor: D.R.E. MEDICAL GROUP, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1320",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX90016M0264_1900_-NONE-_-NONE- (dre_mexico_chihuahua_xray_177k_2016). Signed 2016-07-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90016M0264_1900_-NONE-_-NONE-/.",
    "USASpending: dre_mexico_chihuahua_xray_177k_2016 USD 0.177m. Supports dre_mexico_chihuahua_xray_177k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 176953.96; date_signed 2016-07-15.",
    investment_type="equipment_supply",
)

# === Cycle 1320 ===
row_doc(
    "fidelitad_colombia_intel_fusion_center_138k_2011",
    "infrastructure", "engineering_epc", "us",
    "Fidelitad — Colombia intel fusion center",
    "Colombia",
    "1 Aug 2011: Department of State awards contract to FIDELITAD, INC. for intel fusion center; obligated USD 138152.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "138152.00", "2011-08-01", "2011", "", "",
    "INTEL FUSION CENTER, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fidelitad_colombia_intel_fusion_center_138k_2011",
    "INTEL FUSION CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0018_9700_-NONE-_-NONE-/",
    "Actor: FIDELITAD, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1320",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0018_9700_-NONE-_-NONE- (fidelitad_colombia_intel_fusion_center_138k_2011). Signed 2011-08-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0018_9700_-NONE-_-NONE-/.",
    "USASpending: fidelitad_colombia_intel_fusion_center_138k_2011 USD 0.138m. Supports fidelitad_colombia_intel_fusion_center_138k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 138152.0; date_signed 2011-08-01.",
    investment_type="epc",
)

# === Cycle 1320 ===
row_doc(
    "eterna_peru_relocate_gate_2749k_2022",
    "infrastructure", "bridges_roads", "other",
    "Empresa Eterna — Peru design/construction relocate Gate 1",
    "Peru",
    "1 Dec 2022: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design/construction of relocate Gate 1; obligated USD 2748614.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2748614.80", "2022-12-01", "2022", "", "",
    "DESIGN/CONSTRUCTION OF RELOCATE GATE 1, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_peru_relocate_gate_2749k_2022",
    "DESIGN/CONSTRUCTION OF RELOCATE GATE 1",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0018_9700_W9127817D0095_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1320",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0018_9700_W9127817D0095_9700 (eterna_peru_relocate_gate_2749k_2022). Signed 2022-12-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0018_9700_W9127817D0095_9700/.",
    "USASpending: eterna_peru_relocate_gate_2749k_2022 USD 2.749m. Supports eterna_peru_relocate_gate_2749k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2748614.8; date_signed 2022-12-01.",
    investment_type="epc",
)

# === Cycle 1320 ===
row_doc(
    "eterna_colombia_miraflores_police_station_2679k_2023",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Colombia Miraflores INL rural police station",
    "Colombia",
    "22 Feb 2023: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for INL rural police station, Miraflores Colombia; obligated USD 2679328.84. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2679328.84", "2023-02-22", "2023", "", "",
    "INL RURAL POLICE STATION, MIRAFLORES COL, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_miraflores_police_station_2679k_2023",
    "INL RURAL POLICE STATION, MIRAFLORES COL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0081_9700_W9127817D0095_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1320",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0081_9700_W9127817D0095_9700 (eterna_colombia_miraflores_police_station_2679k_2023). Signed 2023-02-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0081_9700_W9127817D0095_9700/.",
    "USASpending: eterna_colombia_miraflores_police_station_2679k_2023 USD 2.679m. Supports eterna_colombia_miraflores_police_station_2679k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2679328.84; date_signed 2023-02-22.",
    investment_type="epc",
)

# === Cycle 1320 ===
row_doc(
    "eterna_panama_firehouse_drw_2564k_2022",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Panama HAP firehouse and DRW",
    "Panama",
    "27 Sep 2022: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for HAP 67257 firehouse and DRW; obligated USD 2563859.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2563859.90", "2022-09-27", "2022", "", "",
    "HAP 67257 FIREHOUSE AND DRW, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_panama_firehouse_drw_2564k_2022",
    "HAP 67257 FIREHOUSE AND DRW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0403_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1320",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0403_9700_W9127821D0075_9700 (eterna_panama_firehouse_drw_2564k_2022). Signed 2022-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0403_9700_W9127821D0075_9700/.",
    "USASpending: eterna_panama_firehouse_drw_2564k_2022 USD 2.564m. Supports eterna_panama_firehouse_drw_2564k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2563859.9; date_signed 2022-09-27.",
    investment_type="epc",
)

# === Cycle 1321 ===
row_doc(
    "wrigglesworth_honduras_drive_in_containment_115k_2017",
    "infrastructure", "engineering_epc", "us",
    "Wrigglesworth Enterprises — Honduras drive-in containment system",
    "Honduras",
    "19 Jul 2017: Department of State awards contract to WRIGGLESWORTH ENTERPRISES INC for drive-in containment system and accessories; obligated USD 114980.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "114980.00", "2017-07-19", "2017", "", "",
    "DRIVE-IN CONTAINMENT SYSTEM AND ACCESORI, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_wrigglesworth_honduras_drive_in_containment_115k_2017",
    "DRIVE-IN CONTAINMENT SYSTEM AND ACCESORI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM17F0005_9700_GS21F0015X_4732/",
    "Actor: WRIGGLESWORTH ENTERPRISES INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1321",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM17F0005_9700_GS21F0015X_4732 (wrigglesworth_honduras_drive_in_containment_115k_2017). Signed 2017-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM17F0005_9700_GS21F0015X_4732/.",
    "USASpending: wrigglesworth_honduras_drive_in_containment_115k_2017 USD 0.115m. Supports wrigglesworth_honduras_drive_in_containment_115k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 114980.0; date_signed 2017-07-19.",
    investment_type="equipment_supply",
)

# === Cycle 1321 ===
row_doc(
    "redguard_colombia_mail_screening_109k_2026",
    "infrastructure", "engineering_epc", "us",
    "Redguard — Colombia mail screening facility",
    "Colombia",
    "15 Sep 2026: Department of State awards contract to REDGUARD LLC for mail screening facility; obligated USD 109278.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "109278.00", "2026-09-15", "2026", "", "",
    "MAIL SCREENING FACILITY, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_redguard_colombia_mail_screening_109k_2026",
    "MAIL SCREENING FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026F0491_1900_19GE5023D0037_1900/",
    "Actor: REDGUARD LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1321",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026F0491_1900_19GE5023D0037_1900 (redguard_colombia_mail_screening_109k_2026). Signed 2026-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026F0491_1900_19GE5023D0037_1900/.",
    "USASpending: redguard_colombia_mail_screening_109k_2026 USD 0.109m. Supports redguard_colombia_mail_screening_109k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 109278.0; date_signed 2026-09-15.",
    investment_type="equipment_supply",
)

# === Cycle 1321 ===
row_doc(
    "eterna_honduras_maternity_ward_1890k_2017",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Honduras HAP maternity ward",
    "Honduras",
    "29 Sep 2017: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for HAP #28261 maternity ward; obligated USD 1890465.75. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1890465.75", "2017-09-29", "2017", "", "",
    "IGF::OT::IGF HAP # 28261 MATERNITY WARD, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_maternity_ward_1890k_2017",
    "IGF::OT::IGF HAP # 28261 MATERNITY WARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0477_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1321",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0477_9700_W9127816D0102_9700 (eterna_honduras_maternity_ward_1890k_2017). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0477_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_maternity_ward_1890k_2017 USD 1.890m. Supports eterna_honduras_maternity_ward_1890k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1890465.75; date_signed 2017-09-29.",
    investment_type="epc",
)

# === Cycle 1321 ===
row_doc(
    "eterna_honduras_soto_cano_roads_phase5_1855k_2024",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Honduras Soto Cano roads repair Phase V",
    "Honduras",
    "29 Sep 2024: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for repair roads Phase V at Soto Cano AB, Honduras; obligated USD 1854829.98. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1854829.98", "2024-09-29", "2024", "", "",
    "REPAIR ROADS PHASE V AT SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_soto_cano_roads_phase5_1855k_2024",
    "REPAIR ROADS PHASE V AT SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0408_9700_W9127823D0073_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1321",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0408_9700_W9127823D0073_9700 (eterna_honduras_soto_cano_roads_phase5_1855k_2024). Signed 2024-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0408_9700_W9127823D0073_9700/.",
    "USASpending: eterna_honduras_soto_cano_roads_phase5_1855k_2024 USD 1.855m. Supports eterna_honduras_soto_cano_roads_phase5_1855k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1854829.98; date_signed 2024-09-29.",
    investment_type="epc",
)

# === Cycle 1321 ===
row_doc(
    "eterna_argentina_eoc_drw_1757k_2019",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Argentina Neuquen EOC and DRW design/build",
    "Argentina",
    "27 Sep 2019: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B HAP 32040 EOC and HAP 32089 DRW — Neuquen, Argentina; obligated USD 1757183.26. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1757183.26", "2019-09-27", "2019", "", "",
    "D/B HAP 32040 EOC AND HAP 32089 DRW - NEUQUEN, ARGENTINA, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_argentina_eoc_drw_1757k_2019",
    "D/B HAP 32040 EOC AND HAP 32089 DRW - NEUQUEN, ARGENTINA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0528_9700_W9127817D0095_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1321",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0528_9700_W9127817D0095_9700 (eterna_argentina_eoc_drw_1757k_2019). Signed 2019-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0528_9700_W9127817D0095_9700/.",
    "USASpending: eterna_argentina_eoc_drw_1757k_2019 USD 1.757m. Supports eterna_argentina_eoc_drw_1757k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1757183.26; date_signed 2019-09-27.",
    investment_type="epc",
)

# === Cycle 1322 ===
row_doc(
    "smiths_colombia_xray_unit_107k_2012",
    "infrastructure", "engineering_epc", "us",
    "Smiths Detection — Colombia Smiths x-ray unit",
    "Colombia",
    "15 Sep 2012: Department of State awards contract to SMITHS DETECTION INC. for Smiths x-ray unit; obligated USD 106610.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "106610.00", "2012-09-15", "2012", "", "",
    "RSO/EOY /SMITHS X-RAY UNIT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_smiths_colombia_xray_unit_107k_2012",
    "RSO/EOY /SMITHS X-RAY UNIT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M3156_1900_-NONE-_-NONE-/",
    "Actor: SMITHS DETECTION INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1322",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20012M3156_1900_-NONE-_-NONE- (smiths_colombia_xray_unit_107k_2012). Signed 2012-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M3156_1900_-NONE-_-NONE-/.",
    "USASpending: smiths_colombia_xray_unit_107k_2012 USD 0.107m. Supports smiths_colombia_xray_unit_107k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 106610.0; date_signed 2012-09-15.",
    investment_type="equipment_supply",
)

# === Cycle 1322 ===
row_doc(
    "american_warehouse_haiti_pallet_rack_100k_2012",
    "infrastructure", "engineering_epc", "us",
    "American Warehouse Systems — Haiti USAID warehouse pallet rack",
    "Haiti",
    "17 Dec 2012: Department of State awards contract to AMERICAN WAREHOUSE SYSTEMS, LLC for pallet rack for USAID warehouse; obligated USD 100159.95. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "100159.95", "2012-12-17", "2012", "", "",
    "IGF::OT::IGF - PALLET RACK FOR USAID WAREHOUSE, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_american_warehouse_haiti_pallet_rack_100k_2012",
    "IGF::OT::IGF - PALLET RACK FOR USAID WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O1300010_7200_-NONE-_-NONE-/",
    "Actor: AMERICAN WAREHOUSE SYSTEMS, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1322",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521O1300010_7200_-NONE-_-NONE- (american_warehouse_haiti_pallet_rack_100k_2012). Signed 2012-12-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O1300010_7200_-NONE-_-NONE-/.",
    "USASpending: american_warehouse_haiti_pallet_rack_100k_2012 USD 0.100m. Supports american_warehouse_haiti_pallet_rack_100k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 100159.95; date_signed 2012-12-17.",
    investment_type="equipment_supply",
)

# === Cycle 1322 ===
row_doc(
    "marago_colombia_facatativa_kennels_1640k_2022",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia Facatativa kennels",
    "Colombia",
    "6 Apr 2022: Department of State awards contract to CONSTRUCTORA MARAGO S A S for kennels in Facatativa; obligated USD 1640398.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1640398.12", "2022-04-06", "2022", "", "",
    "KENNELS IN FACATATIVA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_facatativa_kennels_1640k_2022",
    "KENNELS IN FACATATIVA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0079_1900_19AQMM21D0036_1900/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1322",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F0079_1900_19AQMM21D0036_1900 (marago_colombia_facatativa_kennels_1640k_2022). Signed 2022-04-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0079_1900_19AQMM21D0036_1900/.",
    "USASpending: marago_colombia_facatativa_kennels_1640k_2022 USD 1.640m. Supports marago_colombia_facatativa_kennels_1640k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1640398.12; date_signed 2022-04-06.",
    investment_type="epc",
)

# === Cycle 1322 ===
row_doc(
    "marago_colombia_muzu_athenea_intel_lab_1526k_2023",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia Muzu Athenea and intel lab",
    "Colombia",
    "9 Jun 2023: Department of State awards contract to CONSTRUCTORA MARAGO S A S for Athenea and intel lab, Muzu; obligated USD 1525971.56. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1525971.56", "2023-06-09", "2023", "", "",
    "ATHENEA AND INTEL LAB, MUZU, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_muzu_athenea_intel_lab_1526k_2023",
    "ATHENEA AND INTEL LAB, MUZU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1153_1900_19AQMM21D0036_1900/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1322",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1153_1900_19AQMM21D0036_1900 (marago_colombia_muzu_athenea_intel_lab_1526k_2023). Signed 2023-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1153_1900_19AQMM21D0036_1900/.",
    "USASpending: marago_colombia_muzu_athenea_intel_lab_1526k_2023 USD 1.526m. Supports marago_colombia_muzu_athenea_intel_lab_1526k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1525971.56; date_signed 2023-06-09.",
    investment_type="epc",
)

# === Cycle 1322 ===
row_doc(
    "eterna_panama_health_center_1409k_2021",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Panama HAP health center",
    "Panama",
    "30 Sep 2021: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for HAP #42015 health center in Panama; obligated USD 1408992.96. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1408992.96", "2021-09-30", "2021", "", "",
    "HAP #42015 HEALTH CENTER IN PANAMA, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_panama_health_center_1409k_2021",
    "HAP #42015 HEALTH CENTER IN PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0462_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1322",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0462_9700_W9127821D0075_9700 (eterna_panama_health_center_1409k_2021). Signed 2021-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0462_9700_W9127821D0075_9700/.",
    "USASpending: eterna_panama_health_center_1409k_2021 USD 1.409m. Supports eterna_panama_health_center_1409k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1408992.96; date_signed 2021-09-30.",
    investment_type="epc",
)

# === Cycle 1323 ===
row_doc(
    "edifice_honduras_febr_windows_install_98k_2019",
    "infrastructure", "engineering_epc", "us",
    "Edifice — Honduras emergency FE/BR windows installation",
    "Honduras",
    "19 Jun 2019: Department of State awards contract to EDIFICE LLC for emergency FE/BR services: three FE/BR installers and air shipment of two GFCI FE/BR windows with steel tubes and plates; obligated USD 98055.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "98055.34", "2019-06-19", "2019", "", "",
    "EMERGENCY FE/BR SERVICES FOR THE CONTRACTOR TO PROVIDE THREE FE/BR INSTALLERS AND AIR SHIPMENT OF TWO GFCI FE/BR WINDOWS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_edifice_honduras_febr_windows_install_98k_2019",
    "EMERGENCY FE/BR SERVICES FOR THE CONTRACTOR TO PROVIDE THREE FE/BR INSTALLERS AND AIR SHIPMENT OF TWO GFCI FE/BR WINDOWS ALONG WITH STEEL TUBES AND PLATES TO POST.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F2032_1900_SAQMMA14D0083_1900/",
    "Actor: EDIFICE LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1323",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F2032_1900_SAQMMA14D0083_1900 (edifice_honduras_febr_windows_install_98k_2019). Signed 2019-06-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F2032_1900_SAQMMA14D0083_1900/.",
    "USASpending: edifice_honduras_febr_windows_install_98k_2019 USD 0.098m. Supports edifice_honduras_febr_windows_install_98k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 98055.34; date_signed 2019-06-19.",
    investment_type="equipment_supply",
)

# === Cycle 1323 ===
row_doc(
    "isobox_panama_mobile_offices_panamax_90k_2026",
    "infrastructure", "engineering_epc", "us",
    "IsoBOX — Panama mobile offices for PANAMAX 2026",
    "Panama",
    "5 Jun 2026: Department of State awards contract to ISOBOX INC for mobile offices in support of PANAMAX 2026; obligated USD 89660.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "89660.00", "2026-06-05", "2026", "", "",
    "MOBILE OFFICES IN SUPPORT OF PANAMAX 2026, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_mobile_offices_panamax_90k_2026",
    "MOBILE OFFICES IN SUPPORT OF PANAMAX 2026",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM26PA018_9700_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1323",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM26PA018_9700_-NONE-_-NONE- (isobox_panama_mobile_offices_panamax_90k_2026). Signed 2026-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM26PA018_9700_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_mobile_offices_panamax_90k_2026 USD 0.090m. Supports isobox_panama_mobile_offices_panamax_90k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89660.0; date_signed 2026-06-05.",
    investment_type="equipment_supply",
)

# === Cycle 1323 ===
row_doc(
    "estudios_colombia_cnp_rural_station_1322k_2019",
    "infrastructure", "engineering_epc", "other",
    "Estudios Edificaciones EEII — Colombia CNP rural station building",
    "Colombia",
    "3 Jul 2019: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for CNP rural station building; obligated USD 1321526.21. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1321526.21", "2019-07-03", "2019", "", "",
    "CNP RURAL STATION BUILDING, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_cnp_rural_station_1322k_2019",
    "CNP RURAL STATION BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0093_1900_-NONE-_-NONE-/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1323",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0093_1900_-NONE-_-NONE- (estudios_colombia_cnp_rural_station_1322k_2019). Signed 2019-07-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0093_1900_-NONE-_-NONE-/.",
    "USASpending: estudios_colombia_cnp_rural_station_1322k_2019 USD 1.322m. Supports estudios_colombia_cnp_rural_station_1322k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1321526.21; date_signed 2019-07-03.",
    investment_type="epc",
)

# === Cycle 1323 ===
row_doc(
    "estudios_colombia_corozal_modular_lodging_1202k_2023",
    "infrastructure", "engineering_epc", "other",
    "Estudios Edificaciones EEII — Colombia Corozal modular lodging buildings",
    "Colombia",
    "18 Aug 2023: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for modular lodging buildings Corozal; obligated USD 1202172.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1202172.11", "2023-08-18", "2023", "", "",
    "MODULAR LODGING BUILDINGS COROZAL, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_corozal_modular_lodging_1202k_2023",
    "MODULAR LODGING BUILDINGS COROZAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1721_1900_19AQMM21D0037_1900/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1323",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1721_1900_19AQMM21D0037_1900 (estudios_colombia_corozal_modular_lodging_1202k_2023). Signed 2023-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1721_1900_19AQMM21D0037_1900/.",
    "USASpending: estudios_colombia_corozal_modular_lodging_1202k_2023 USD 1.202m. Supports estudios_colombia_corozal_modular_lodging_1202k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1202172.11; date_signed 2023-08-18.",
    investment_type="epc",
)

# === Cycle 1323 ===
row_doc(
    "eterna_honduras_latrine_november_block_1151k_2017",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Honduras new latrine November block",
    "Honduras",
    "21 Sep 2017: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for new latrine November block; obligated USD 1150606.75. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1150606.75", "2017-09-21", "2017", "", "",
    "IGF::OT::IGF NEW LATRINE NOVEMBER BLOCK, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_latrine_november_block_1151k_2017",
    "IGF::OT::IGF NEW LATRINE NOVEMBER BLOCK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0321_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1323",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0321_9700_W9127816D0102_9700 (eterna_honduras_latrine_november_block_1151k_2017). Signed 2017-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0321_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_latrine_november_block_1151k_2017 USD 1.151m. Supports eterna_honduras_latrine_november_block_1151k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1150606.75; date_signed 2017-09-21.",
    investment_type="epc",
)

def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    for row, _ev, _bib in ITEMS:
        rid = row["id"]
        if rid in by_id: raise SystemExit(f"duplicate id: {rid}")
        rows.append(row); by_id[rid] = row
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
                if s not in (existing.get("supports") or []): existing.setdefault("supports", []).append(s)
        else: bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
