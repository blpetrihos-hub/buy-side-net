#!/usr/bin/env python3
"""Cycles 1256–1261: USASpending LatAm CapEx (US fire-alarm/electrical tranche + residual other).

Seeds: 20262256–20262261. Thin top-up dry. Fire-alarm CapEx tranche unlocked; residual other make-ready.
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

# === Cycle 1256 ===
row_doc(
    "hsu_peru_fire_alarm_upgrade_839k_2014",
    "infrastructure", "building_materials", "us",
    "HSU Development — Peru fire alarm upgrade",
    "Peru",
    "10 Sep 2014: Department of State awards contract to HSU DEVELOPMENT, INC. for fire alarm upgrade at U.S. post (PoP Peru); obligated USD 839263.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "839263.67", "2014-09-10", "2014", "", "",
    "FIRE ALARM UPGRADE IGF::CT::IGF, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_hsu_peru_fire_alarm_upgrade_839k_2014",
    "FIRE ALARM UPGRADE IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3378_1900_SAQMMA14D0058_1900/",
    "Actor: HSU DEVELOPMENT, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1256",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F3378_1900_SAQMMA14D0058_1900 (hsu_peru_fire_alarm_upgrade_839k_2014). Signed 2014-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3378_1900_SAQMMA14D0058_1900/.",
    "USASpending: hsu_peru_fire_alarm_upgrade_839k_2014 USD 0.839m. Supports hsu_peru_fire_alarm_upgrade_839k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 839263.67; date_signed 2014-09-10.",
    investment_type="epc",
)

# === Cycle 1256 ===
row_doc(
    "fdc_chile_fire_alarm_upgrade_681k_2015",
    "infrastructure", "building_materials", "us",
    "Facilities Development Corporation — Chile fire alarm upgrade",
    "Chile",
    "9 Jun 2015: Department of State awards contract to FACILITIES DEVELOPMENT CORPORATION for fire alarm upgrade at U.S. post (PoP Chile); obligated USD 681509. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "681509", "2015-06-09", "2015", "", "",
    "IGF::CT::IGF FIRE ALARM UPGRADE, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_fdc_chile_fire_alarm_upgrade_681k_2015",
    "IGF::CT::IGF FIRE ALARM UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1663_1900_SAQMMA14D0055_1900/",
    "Actor: FACILITIES DEVELOPMENT CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1256",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F1663_1900_SAQMMA14D0055_1900 (fdc_chile_fire_alarm_upgrade_681k_2015). Signed 2015-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1663_1900_SAQMMA14D0055_1900/.",
    "USASpending: fdc_chile_fire_alarm_upgrade_681k_2015 USD 0.682m. Supports fdc_chile_fire_alarm_upgrade_681k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 681509.0; date_signed 2015-06-09.",
    investment_type="epc",
)

# === Cycle 1256 ===
row_doc(
    "enel_colombia_cmr_transformer_replacement_176k_2024",
    "energy", "power_plants_grid", "other",
    "Enel Colombia — CMR transformer replacement improvements",
    "Colombia",
    "11 Jul 2024: Department of State awards contract to ENEL COLOMBIA S.A. E.S.P. for FAC X2002 transformer replacement CMR improvements (PoP Colombia); obligated USD 176380.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "176380.40", "2024-07-11", "2024", "", "",
    "FAC_X2002 TRANSFORMER REPLACEMENT CMR IMPROVEMENTS_7919, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_enel_colombia_cmr_transformer_replacement_176k_2024",
    "FAC_X2002 TRANSFORMER REPLACEMENT CMR IMPROVEMENTS_7919",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P1314_1900_-NONE-_-NONE-/",
    "Actor: ENEL COLOMBIA S.A. E.S.P. — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1256",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024P1314_1900_-NONE-_-NONE- (enel_colombia_cmr_transformer_replacement_176k_2024). Signed 2024-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P1314_1900_-NONE-_-NONE-/.",
    "USASpending: enel_colombia_cmr_transformer_replacement_176k_2024 USD 0.176m. Supports enel_colombia_cmr_transformer_replacement_176k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 176380.4; date_signed 2024-07-11.",
    investment_type="equipment_supply",
)

# === Cycle 1256 ===
row_doc(
    "carvajal_colombia_office_renovation_136k_2020",
    "infrastructure", "building_materials", "other",
    "Carvajal Espacios — Colombia office renovation 2020",
    "Colombia",
    "25 Aug 2020: Agency for International Development awards contract to CARVAJAL ESPACIOS S.A.S. BIC for office renovation project 2020 (PoP Colombia); obligated USD 136409.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "136409.17", "2020-08-25", "2020", "", "",
    "OFFICE RENOVATION PROJECT 2020, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_carvajal_colombia_office_renovation_136k_2020",
    "OFFICE RENOVATION PROJECT 2020",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72051420P00070_7200_-NONE-_-NONE-/",
    "Actor: CARVAJAL ESPACIOS S.A.S. BIC — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1256",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_72051420P00070_7200_-NONE-_-NONE- (carvajal_colombia_office_renovation_136k_2020). Signed 2020-08-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_72051420P00070_7200_-NONE-_-NONE-/.",
    "USASpending: carvajal_colombia_office_renovation_136k_2020 USD 0.136m. Supports carvajal_colombia_office_renovation_136k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 136409.17; date_signed 2020-08-25.",
    investment_type="epc",
)

# === Cycle 1256 ===
row_doc(
    "misc_dominican_skarrn_make_ready_34k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready Skarrn Ryvnine",
    "Dominican Republic",
    "8 Apr 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for consular landlord make-ready Skarrn Ryvnine (PoP Dominican Republic); obligated USD 34521.05. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "34521.05", "2014-04-08", "2014", "", "",
    "CONS- LANDLORD MAKE READY SKARRN RYVNINE   IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_skarrn_make_ready_34k_2014",
    "CONS- LANDLORD MAKE READY SKARRN RYVNINE   IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M0946_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1256",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M0946_1900_-NONE-_-NONE- (misc_dominican_skarrn_make_ready_34k_2014). Signed 2014-04-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M0946_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_skarrn_make_ready_34k_2014 USD 0.035m. Supports misc_dominican_skarrn_make_ready_34k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34521.05; date_signed 2014-04-08.",
    investment_type="epc",
)

# === Cycle 1257 ===
row_doc(
    "ics_jamaica_kingston_fire_alarm_676k_2014",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Kingston fire alarm upgrade",
    "Jamaica",
    "10 Sep 2014: Department of State awards contract to INTERNATIONAL CONSTRUCTION SERVICES, LLC for Kingston fire alarm upgrade (PoP Jamaica); obligated USD 676732. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "676732", "2014-09-10", "2014", "", "",
    "KINGSTON FIRE ALARM UPGRADE  IGF::CT::IGF, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_jamaica_kingston_fire_alarm_676k_2014",
    "KINGSTON FIRE ALARM UPGRADE  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3380_1900_SAQMMA14D0059_1900/",
    "Actor: INTERNATIONAL CONSTRUCTION SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1257",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F3380_1900_SAQMMA14D0059_1900 (ics_jamaica_kingston_fire_alarm_676k_2014). Signed 2014-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3380_1900_SAQMMA14D0059_1900/.",
    "USASpending: ics_jamaica_kingston_fire_alarm_676k_2014 USD 0.677m. Supports ics_jamaica_kingston_fire_alarm_676k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 676732.0; date_signed 2014-09-10.",
    investment_type="epc",
)

# === Cycle 1257 ===
row_doc(
    "greenway_bolivia_fire_alarm_upgrade_676k_2015",
    "infrastructure", "building_materials", "us",
    "Greenway Enterprises — Bolivia fire alarm upgrade",
    "Bolivia",
    "10 Jun 2015: Department of State awards contract to GREENWAY ENTERPRISES INC for fire alarm upgrade at U.S. post (PoP Bolivia); obligated USD 676562.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "676562.89", "2015-06-10", "2015", "", "",
    "FIRE ALARM UPGRADE IGF::CT::IGF, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_greenway_bolivia_fire_alarm_upgrade_676k_2015",
    "FIRE ALARM UPGRADE IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1665_1900_SAQMMA14D0050_1900/",
    "Actor: GREENWAY ENTERPRISES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1257",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F1665_1900_SAQMMA14D0050_1900 (greenway_bolivia_fire_alarm_upgrade_676k_2015). Signed 2015-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1665_1900_SAQMMA14D0050_1900/.",
    "USASpending: greenway_bolivia_fire_alarm_upgrade_676k_2015 USD 0.677m. Supports greenway_bolivia_fire_alarm_upgrade_676k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 676562.89; date_signed 2015-06-10.",
    investment_type="epc",
)

# === Cycle 1257 ===
row_doc(
    "akj_mexico_musset_fire_alarm_93k_2022",
    "infrastructure", "building_materials", "other",
    "Servicios AKJ — Mexico Musset fire alarm system",
    "Mexico",
    "5 Apr 2022: Department of State awards contract to SERVICIOS AKJ, S.A DE C.V for Musset fire alarm system (PoP Mexico); obligated USD 93531.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "93531.90", "2022-04-05", "2022", "", "",
    "MEX-FAC-MCI-XJ2L0183-7344-MUSSET FIRE ALARM SYSTEM, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_akj_mexico_musset_fire_alarm_93k_2022",
    "MEX-FAC-MCI-XJ2L0183-7344-MUSSET FIRE ALARM SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5322C0004_1900_-NONE-_-NONE-/",
    "Actor: SERVICIOS AKJ, S.A DE C.V — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1257",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5322C0004_1900_-NONE-_-NONE- (akj_mexico_musset_fire_alarm_93k_2022). Signed 2022-04-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5322C0004_1900_-NONE-_-NONE-/.",
    "USASpending: akj_mexico_musset_fire_alarm_93k_2022 USD 0.094m. Supports akj_mexico_musset_fire_alarm_93k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 93531.9; date_signed 2022-04-05.",
    investment_type="epc",
)

# === Cycle 1257 ===
row_doc(
    "advtech_ecuador_cmr_cctv_floresta_85k_2023",
    "infrastructure", "building_materials", "other",
    "Advanced Technologies Vandetsa — Ecuador CMR Floresta CCTV",
    "Ecuador",
    "15 Jun 2023: Department of State awards contract to ADVANCED TECHNOLOGIES S.A. VANDETSA for new CCTV system for CMR Floresta (PoP Ecuador); obligated USD 85733.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "85733.20", "2023-06-15", "2023", "", "",
    "PR11768911-FC5841 NEW CCTV SYSTEM FOR CMR - FLORESTA, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_advtech_ecuador_cmr_cctv_floresta_85k_2023",
    "PR11768911-FC5841 NEW CCTV SYSTEM FOR CMR - FLORESTA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P1021_1900_-NONE-_-NONE-/",
    "Actor: ADVANCED TECHNOLOGIES S.A. VANDETSA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1257",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P1021_1900_-NONE-_-NONE- (advtech_ecuador_cmr_cctv_floresta_85k_2023). Signed 2023-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P1021_1900_-NONE-_-NONE-/.",
    "USASpending: advtech_ecuador_cmr_cctv_floresta_85k_2023 USD 0.086m. Supports advtech_ecuador_cmr_cctv_floresta_85k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85733.2; date_signed 2023-06-15.",
    investment_type="equipment_supply",
)

# === Cycle 1257 ===
row_doc(
    "misc_ecuador_driveway_floor_make_ready_29k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador CGR driveway floor repairs make-ready",
    "Ecuador",
    "18 Jun 2020: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for driveway floor repairs make-ready 2020 CGR (PoP Ecuador); obligated USD 29274. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "29274", "2020-06-18", "2020", "", "",
    "DRIVEWAY FLOOR REPAIRS MAKE READY 2020 CGR, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_driveway_floor_make_ready_29k_2020",
    "DRIVEWAY FLOOR REPAIRS MAKE READY 2020 CGR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3020P0380_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1257",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3020P0380_1900_-NONE-_-NONE- (misc_ecuador_driveway_floor_make_ready_29k_2020). Signed 2020-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3020P0380_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_driveway_floor_make_ready_29k_2020 USD 0.029m. Supports misc_ecuador_driveway_floor_make_ready_29k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29274.0; date_signed 2020-06-18.",
    investment_type="epc",
)

# === Cycle 1258 ===
row_doc(
    "kva_jamaica_kingston_switchgear_320k_2018",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Kingston switchgear replacement",
    "Jamaica",
    "24 Sep 2018: Department of State awards contract to KVA ELECTRIC INC for Kingston switchgear replacement (PoP Jamaica); obligated USD 320283.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "320283.12", "2018-09-24", "2018", "", "",
    "KINGSTON SWITCHGEAR REPLACEMENT, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_jamaica_kingston_switchgear_320k_2018",
    "KINGSTON SWITCHGEAR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4205_1900_19AQMM18D0076_1900/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1258",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F4205_1900_19AQMM18D0076_1900 (kva_jamaica_kingston_switchgear_320k_2018). Signed 2018-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4205_1900_19AQMM18D0076_1900/.",
    "USASpending: kva_jamaica_kingston_switchgear_320k_2018 USD 0.320m. Supports kva_jamaica_kingston_switchgear_320k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 320283.12; date_signed 2018-09-24.",
    investment_type="epc",
)

# === Cycle 1258 ===
row_doc(
    "grainger_peru_residential_transformers_142k_2020",
    "energy", "power_plants_grid", "us",
    "W.W. Grainger — Peru residential transformer replacement",
    "Peru",
    "17 Jan 2020: Department of State awards contract to W.W. GRAINGER, INC. for GSO/WHSE replacement of residential transformers FAP (PoP Peru); obligated USD 142347.50. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "142347.50", "2020-01-17", "2020", "", "",
    "GSO/WHSE - REPLACEMENT OF RESIDENTIAL TRANSFORMERS (FAP), Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_grainger_peru_residential_transformers_142k_2020",
    "GSO/WHSE - REPLACEMENT OF RESIDENTIAL TRANSFORMERS (FAP)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5020F0151_1900_47QSHA19A000D_4732/",
    "Actor: W.W. GRAINGER, INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1258",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5020F0151_1900_47QSHA19A000D_4732 (grainger_peru_residential_transformers_142k_2020). Signed 2020-01-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5020F0151_1900_47QSHA19A000D_4732/.",
    "USASpending: grainger_peru_residential_transformers_142k_2020 USD 0.142m. Supports grainger_peru_residential_transformers_142k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 142347.5; date_signed 2020-01-17.",
    investment_type="equipment_supply",
)

# === Cycle 1258 ===
row_doc(
    "schneider_panama_embassy_switchgear_breaker_193k_2026",
    "energy", "power_plants_grid", "allied",
    "Schneider Electric Centroamérica — Panama embassy switchgear breaker replacement",
    "Panama",
    "13 Aug 2026: Department of State awards contract to SCHNEIDER ELECTRIC CENTROAMERICA LTDA for embassy switch gear breaker replacement (PoP Panama); obligated USD 193942.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "193942.01", "2026-08-13", "2026", "", "",
    "EMBASSY SWITCH GEAR BREAKER REPLACEMENT, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_schneider_panama_embassy_switchgear_breaker_193k_2026",
    "EMBASSY SWITCH GEAR BREAKER REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0726P0457_1900_-NONE-_-NONE-/",
    "Actor: SCHNEIDER ELECTRIC CENTROAMERICA LTDA (Schneider Electric Centroamérica / French Schneider group) — allied. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1258",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0726P0457_1900_-NONE-_-NONE- (schneider_panama_embassy_switchgear_breaker_193k_2026). Signed 2026-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0726P0457_1900_-NONE-_-NONE-/.",
    "USASpending: schneider_panama_embassy_switchgear_breaker_193k_2026 USD 0.194m. Supports schneider_panama_embassy_switchgear_breaker_193k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 193942.01; date_signed 2026-08-13.",
    investment_type="equipment_supply",
)

# === Cycle 1258 ===
row_doc(
    "solano_elsalvador_comalapa_solar_72k_2018",
    "energy", "solar", "other",
    "Arturo Enrique Solano Urrutia — Comalapa solar panels",
    "El Salvador",
    "25 Sep 2018: Department of State awards contract to ARTURO ENRIQUE SOLANO URRUTIA for supply and installation of solar panels at Comalapa (PoP El Salvador); obligated USD 72769.96. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "72769.96", "2018-09-25", "2018", "", "",
    "SUPPLY AND INSTALLATION OF SOLAR PANELS AT COMALAPA, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_solano_elsalvador_comalapa_solar_72k_2018",
    "SUPPLY AND INSTALLATION OF SOLAR PANELS AT COMALAPA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6018P0996_1900_-NONE-_-NONE-/",
    "Actor: ARTURO ENRIQUE SOLANO URRUTIA — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1258",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6018P0996_1900_-NONE-_-NONE- (solano_elsalvador_comalapa_solar_72k_2018). Signed 2018-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6018P0996_1900_-NONE-_-NONE-/.",
    "USASpending: solano_elsalvador_comalapa_solar_72k_2018 USD 0.073m. Supports solano_elsalvador_comalapa_solar_72k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 72769.96; date_signed 2018-09-25.",
    investment_type="equipment_supply",
)

# === Cycle 1258 ===
row_doc(
    "misc_mexico_cdj_cgr_make_ready_28k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juárez CGR make-ready",
    "Mexico",
    "17 Aug 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CDJ 7901 make-ready work at the CGR (PoP Mexico); obligated USD 28256.92. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "28256.92", "2015-08-17", "2015", "", "",
    "CDJ 7901 MAKE READY WORK AT THE CGR. IGF::OT::IGF - FOR OTHER FUNCTIONS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_cgr_make_ready_28k_2015",
    "CDJ 7901 MAKE READY WORK AT THE CGR. IGF::OT::IGF - FOR OTHER FUNCTIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11515M0421_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1258",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11515M0421_1900_-NONE-_-NONE- (misc_mexico_cdj_cgr_make_ready_28k_2015). Signed 2015-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11515M0421_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cdj_cgr_make_ready_28k_2015 USD 0.028m. Supports misc_mexico_cdj_cgr_make_ready_28k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28256.92; date_signed 2015-08-17.",
    investment_type="epc",
)

# === Cycle 1259 ===
row_doc(
    "ics_bahamas_nassau_fire_alarm_603k_2017",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Nassau fire detection/alarm replacement",
    "Bahamas",
    "21 Aug 2017: Department of State awards contract to INTERNATIONAL CONSTRUCTION SERVICES, LLC for Nassau fire detection/alarm system replacement project (PoP Bahamas); obligated USD 603944. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "603944", "2017-08-21", "2017", "", "",
    "NASSAU FIRE DETECTION/ALARM SYSTEM REPLACEMENT PROJECT # XJ-04-0008. THIS PR6622971 IS FOR PHASE I (, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_bahamas_nassau_fire_alarm_603k_2017",
    "NASSAU FIRE DETECTION/ALARM SYSTEM REPLACEMENT PROJECT # XJ-04-0008. THIS PR6622971 IS FOR PHASE I (SITE SURVEY), PHASE II (DESIGN&PLANNING), PHASE III (CONSTRUCTION) AT THE U. S. EMBASSY IN NASSAU, THE BAHAMAS - TO INCLUDE OPTION 1 - NEW FIRE ALARM SYSTEM IN THE MSGQ. POC IS MIKE BRYCE: 703-875-5099. CONTRACT # IS SAQMMA-14-D-0059.   IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F2638_1900_SAQMMA14D0059_1900/",
    "Actor: INTERNATIONAL CONSTRUCTION SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1259",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17F2638_1900_SAQMMA14D0059_1900 (ics_bahamas_nassau_fire_alarm_603k_2017). Signed 2017-08-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F2638_1900_SAQMMA14D0059_1900/.",
    "USASpending: ics_bahamas_nassau_fire_alarm_603k_2017 USD 0.604m. Supports ics_bahamas_nassau_fire_alarm_603k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 603944.0; date_signed 2017-08-21.",
    investment_type="epc",
)

# === Cycle 1259 ===
row_doc(
    "futron_costa_rica_fire_alarm_487k_2014",
    "infrastructure", "building_materials", "us",
    "Futron — Costa Rica fire alarm upgrade",
    "Costa Rica",
    "19 Sep 2014: Department of State awards contract to FUTRON, INC. for fire alarm upgrade at U.S. post (PoP Costa Rica); obligated USD 487826. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "487826", "2014-09-19", "2014", "", "",
    "FIRE ALARM UPGRADE  IGF::CT::IGF, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_futron_costa_rica_fire_alarm_487k_2014",
    "FIRE ALARM UPGRADE  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3759_1900_SAQMMA14D0064_1900/",
    "Actor: FUTRON, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1259",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F3759_1900_SAQMMA14D0064_1900 (futron_costa_rica_fire_alarm_487k_2014). Signed 2014-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3759_1900_SAQMMA14D0064_1900/.",
    "USASpending: futron_costa_rica_fire_alarm_487k_2014 USD 0.488m. Supports futron_costa_rica_fire_alarm_487k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 487826.0; date_signed 2014-09-19.",
    investment_type="epc",
)

# === Cycle 1259 ===
row_doc(
    "polo_panama_coibita_solar_32k_2023",
    "energy", "solar", "other",
    "Grupo Polo — Panama Coibita PV solar panels",
    "Panama",
    "26 Apr 2023: Smithsonian Institution awards contract to GRUPO POLO S.A. for STRI install PV solar panels at Coibita (PoP Panama); obligated USD 32200. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "32200", "2023-04-26", "2023", "", "",
    "STRI: INSTALL PV SOLAR PANELS AT COIBITA., Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_polo_panama_coibita_solar_32k_2023",
    "STRI: INSTALL PV SOLAR PANELS AT COIBITA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223CF0010152_3300_-NONE-_-NONE-/",
    "Actor: GRUPO POLO S.A. — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1259",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330223CF0010152_3300_-NONE-_-NONE- (polo_panama_coibita_solar_32k_2023). Signed 2023-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223CF0010152_3300_-NONE-_-NONE-/.",
    "USASpending: polo_panama_coibita_solar_32k_2023 USD 0.032m. Supports polo_panama_coibita_solar_32k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 32200.0; date_signed 2023-04-26.",
    investment_type="equipment_supply",
)

# === Cycle 1259 ===
row_doc(
    "misc_dominican_los_bambues_make_ready_27k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Los Bambues 10 make-ready",
    "Dominican Republic",
    "2 Jul 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for SRM & make-ready work Los Bambues 10 PID 824 (PoP Dominican Republic); obligated USD 27620.86. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "27620.86", "2024-07-02", "2024", "", "",
    "PROG- SRM & MAKE READY WORK LOS BAMBUES 10 PID 824 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_los_bambues_make_ready_27k_2024",
    "PROG- SRM & MAKE READY WORK LOS BAMBUES 10 PID 824 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0049_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1259",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0049_1900_-NONE-_-NONE- (misc_dominican_los_bambues_make_ready_27k_2024). Signed 2024-07-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0049_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_los_bambues_make_ready_27k_2024 USD 0.028m. Supports misc_dominican_los_bambues_make_ready_27k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27620.86; date_signed 2024-07-02.",
    investment_type="epc",
)

# === Cycle 1259 ===
row_doc(
    "misc_mexico_sevilla20_make_ready_26k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Hermosillo Sevilla #20 make-ready",
    "Mexico",
    "12 Aug 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for OBO-LD HMO Sevilla #20 make-ready (PoP Mexico); obligated USD 26587.92. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "26587.92", "2011-08-12", "2011", "", "",
    "OBO-LD:/HMO-SEVILLA #20-MAKE READY (4128-163112), Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_sevilla20_make_ready_26k_2011",
    "OBO-LD:/HMO-SEVILLA #20-MAKE READY (4128-163112)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX57011M0170_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1259",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX57011M0170_1900_-NONE-_-NONE- (misc_mexico_sevilla20_make_ready_26k_2011). Signed 2011-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX57011M0170_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_sevilla20_make_ready_26k_2011 USD 0.027m. Supports misc_mexico_sevilla20_make_ready_26k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26587.92; date_signed 2011-08-12.",
    investment_type="epc",
)

# === Cycle 1260 ===
row_doc(
    "emr_honduras_fire_alarm_upgrade_429k_2012",
    "infrastructure", "building_materials", "us",
    "Enviro-Management & Research — Honduras fire alarm upgrade",
    "Honduras",
    "14 May 2012: Department of State awards contract to ENVIRO-MANAGEMENT & RESEARCH, INC. for fire alarm upgrade at U.S. post (PoP Honduras); obligated USD 429576. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "429576", "2012-05-14", "2012", "", "",
    "FIRE ALARM UPGRADE  IGF::CT::IGF, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_emr_honduras_fire_alarm_upgrade_429k_2012",
    "FIRE ALARM UPGRADE  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1702_1900_SAQMMA08D0010_1900/",
    "Actor: ENVIRO-MANAGEMENT & RESEARCH, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1260",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F1702_1900_SAQMMA08D0010_1900 (emr_honduras_fire_alarm_upgrade_429k_2012). Signed 2012-05-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1702_1900_SAQMMA08D0010_1900/.",
    "USASpending: emr_honduras_fire_alarm_upgrade_429k_2012 USD 0.430m. Supports emr_honduras_fire_alarm_upgrade_429k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 429576.0; date_signed 2012-05-14.",
    investment_type="epc",
)

# === Cycle 1260 ===
row_doc(
    "spectrum_paraguay_fire_alarm_upgrade_398k_2012",
    "infrastructure", "building_materials", "us",
    "Spectrum Electrical Services — Paraguay fire alarm upgrade",
    "Paraguay",
    "21 Mar 2012: Department of State awards contract to SPECTRUM ELECTRICAL SERVICES, INC for fire alarm upgrade at U.S. post (PoP Paraguay); obligated USD 398779.28. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "398779.28", "2012-03-21", "2012", "", "",
    "FIRE ALARM UPGRADE, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_spectrum_paraguay_fire_alarm_upgrade_398k_2012",
    "FIRE ALARM UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1065_1900_SAQMMA08D0007_1900/",
    "Actor: SPECTRUM ELECTRICAL SERVICES, INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1260",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F1065_1900_SAQMMA08D0007_1900 (spectrum_paraguay_fire_alarm_upgrade_398k_2012). Signed 2012-03-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1065_1900_SAQMMA08D0007_1900/.",
    "USASpending: spectrum_paraguay_fire_alarm_upgrade_398k_2012 USD 0.399m. Supports spectrum_paraguay_fire_alarm_upgrade_398k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 398779.28; date_signed 2012-03-21.",
    investment_type="epc",
)

# === Cycle 1260 ===
row_doc(
    "misc_venezuela_piedras_arriba_make_ready_26k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela Piedras Arriba apt 31 make-ready",
    "Venezuela",
    "9 Aug 2018: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC-CMR make-ready for Res. Piedras Arriba apt 31 (PoP Venezuela); obligated USD 26478.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "26478.22", "2018-08-09", "2018", "", "",
    "FAC-CMR: MAKE READY FOR RES. PIEDRAS ARRIBA, APT 31, Venezuela (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_piedras_arriba_make_ready_26k_2018",
    "FAC-CMR: MAKE READY FOR RES. PIEDRAS ARRIBA, APT 31",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19VE3018P0715_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1260",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19VE3018P0715_1900_-NONE-_-NONE- (misc_venezuela_piedras_arriba_make_ready_26k_2018). Signed 2018-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19VE3018P0715_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_piedras_arriba_make_ready_26k_2018 USD 0.026m. Supports misc_venezuela_piedras_arriba_make_ready_26k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26478.22; date_signed 2018-08-09.",
    investment_type="epc",
)

# === Cycle 1260 ===
row_doc(
    "misc_venezuela_cmr_make_ready_urgent_26k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela CMR urgent make-ready",
    "Venezuela",
    "12 Aug 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for make-ready at CMR urgent (PoP Venezuela); obligated USD 26136.81. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "26136.81", "2010-08-12", "2010", "", "",
    "MAKE READY AT CMR URGENT, Venezuela (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_cmr_make_ready_urgent_26k_2010",
    "MAKE READY AT CMR URGENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30010M0671_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1260",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30010M0671_1900_-NONE-_-NONE- (misc_venezuela_cmr_make_ready_urgent_26k_2010). Signed 2010-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30010M0671_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_cmr_make_ready_urgent_26k_2010 USD 0.026m. Supports misc_venezuela_cmr_make_ready_urgent_26k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26136.81; date_signed 2010-08-12.",
    investment_type="epc",
)

# === Cycle 1260 ===
row_doc(
    "misc_mexico_castillo_miramar_make_ready_25k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Castillo de Miramar 65 make-ready",
    "Mexico",
    "4 Jun 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for MX-DAO make-ready Castillo de Miramar 65 FY19 (PoP Mexico); obligated USD 25440.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "25440.17", "2019-06-04", "2019", "", "",
    "MX-DAO-MAKE READY/CASTILLO DE MIRAMAR 65-FY19, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_castillo_miramar_make_ready_25k_2019",
    "MX-DAO-MAKE READY/CASTILLO DE MIRAMAR 65-FY19",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319P0836_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1260",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319P0836_1900_-NONE-_-NONE- (misc_mexico_castillo_miramar_make_ready_25k_2019). Signed 2019-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319P0836_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_castillo_miramar_make_ready_25k_2019 USD 0.025m. Supports misc_mexico_castillo_miramar_make_ready_25k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25440.17; date_signed 2019-06-04.",
    investment_type="epc",
)

# === Cycle 1261 ===
row_doc(
    "monaco_honduras_fire_alarm_system_151k_2016",
    "infrastructure", "building_materials", "us",
    "Monaco Enterprises — Honduras fire alarm system",
    "Honduras",
    "23 Sep 2016: Department of Defense awards contract to MONACO ENTERPRISES, INC. for Monaco fire alarm system (PoP Honduras); obligated USD 151765.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "151765.67", "2016-09-23", "2016", "", "",
    "MONACO FIRE ALARM SYSTEM, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_monaco_honduras_fire_alarm_system_151k_2016",
    "MONACO FIRE ALARM SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM16P0072_9700_-NONE-_-NONE-/",
    "Actor: MONACO ENTERPRISES, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1261",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM16P0072_9700_-NONE-_-NONE- (monaco_honduras_fire_alarm_system_151k_2016). Signed 2016-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM16P0072_9700_-NONE-_-NONE-/.",
    "USASpending: monaco_honduras_fire_alarm_system_151k_2016 USD 0.152m. Supports monaco_honduras_fire_alarm_system_151k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 151765.67; date_signed 2016-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1261 ===
row_doc(
    "hsu_venezuela_fire_alarm_replacement_145k_2016",
    "infrastructure", "building_materials", "us",
    "HSU Development — Venezuela fire alarm replacement",
    "Venezuela",
    "28 Sep 2016: Department of State awards contract to HSU DEVELOPMENT, INC. for fire alarm replacement at U.S. post (PoP Venezuela); obligated USD 145565.06. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "145565.06", "2016-09-28", "2016", "", "",
    "FIRE ALARM REPLACEMENT  IGF::CT::IGF, Venezuela (USASpending description; site not named — lat/lon blank).",
    "usaspending_hsu_venezuela_fire_alarm_replacement_145k_2016",
    "FIRE ALARM REPLACEMENT  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5358_1900_SAQMMA14D0058_1900/",
    "Actor: HSU DEVELOPMENT, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1261",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F5358_1900_SAQMMA14D0058_1900 (hsu_venezuela_fire_alarm_replacement_145k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5358_1900_SAQMMA14D0058_1900/.",
    "USASpending: hsu_venezuela_fire_alarm_replacement_145k_2016 USD 0.146m. Supports hsu_venezuela_fire_alarm_replacement_145k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 145565.06; date_signed 2016-09-28.",
    investment_type="epc",
)

# === Cycle 1261 ===
row_doc(
    "misc_mexico_mty_panfilo_make_ready_24k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Monterrey Panfilo Narvaez 115 make-ready",
    "Mexico",
    "20 Mar 2025: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for MTY/ICE make-ready house works Panfilo Narvaez 115 FY25 (PoP Mexico); obligated USD 24990.27. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "24990.27", "2025-03-20", "2025", "", "",
    "MTY/ICE/MAKE READY HOUSE WORKS PANFILO NARVAEZ 115/FY25, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_mty_panfilo_make_ready_24k_2025",
    "MTY/ICE/MAKE READY HOUSE WORKS PANFILO NARVAEZ 115/FY25",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5625P0249_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1261",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5625P0249_1900_-NONE-_-NONE- (misc_mexico_mty_panfilo_make_ready_24k_2025). Signed 2025-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5625P0249_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_mty_panfilo_make_ready_24k_2025 USD 0.025m. Supports misc_mexico_mty_panfilo_make_ready_24k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24990.27; date_signed 2025-03-20.",
    investment_type="epc",
)

# === Cycle 1261 ===
row_doc(
    "misc_argentina_las_heras_make_ready_24k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Las Heras 2651 Martinez make-ready",
    "Argentina",
    "14 Jul 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FM make-ready 2014 Las Heras 2651 Martinez (PoP Argentina); obligated USD 24250.61. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "24250.61", "2014-07-14", "2014", "", "",
    "FM - MAKE READY 2014 - LAS HERAS 2651 - MARTINEZ IGF::OT::IGF, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_las_heras_make_ready_24k_2014",
    "FM - MAKE READY 2014 - LAS HERAS 2651 - MARTINEZ IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20014M0381_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1261",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20014M0381_1900_-NONE-_-NONE- (misc_argentina_las_heras_make_ready_24k_2014). Signed 2014-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20014M0381_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_las_heras_make_ready_24k_2014 USD 0.024m. Supports misc_argentina_las_heras_make_ready_24k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24250.61; date_signed 2014-07-14.",
    investment_type="epc",
)

# === Cycle 1261 ===
row_doc(
    "misc_mexico_calizas_make_ready_23k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Calizas 476 make-ready",
    "Mexico",
    "27 Mar 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC-7901 make-ready works Calizas 476 X4004 (PoP Mexico); obligated USD 23965.65. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "23965.65", "2015-03-27", "2015", "", "",
    "MEX/FAC-7901/MAKE READY WORKS/CALIZAS 476/X4004 IGF::OT::IGF, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_calizas_make_ready_23k_2015",
    "MEX/FAC-7901/MAKE READY WORKS/CALIZAS 476/X4004 IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0743_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1261",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015M0743_1900_-NONE-_-NONE- (misc_mexico_calizas_make_ready_23k_2015). Signed 2015-03-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0743_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_calizas_make_ready_23k_2015 USD 0.024m. Supports misc_mexico_calizas_make_ready_23k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 23965.65; date_signed 2015-03-27.",
    investment_type="epc",
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
