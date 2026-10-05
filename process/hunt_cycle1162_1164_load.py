#!/usr/bin/env python3
"""Cycles 1162–1164: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262162–20262164. Thin top-up dry.
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


# === Cycle 1162 (seed 20262162) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "valkyrie_colombia_bogota_tss_security_installation_239k_2010",
    "infrastructure", "building_materials", "us",
    "Valkyrie Enterprises — Colombia Bogota technical security services security installation",
    "Colombia",
    "6 Dec 2010: Department of State awards contract SAQMMA11F0228 to Valkyrie Enterprises, LLC for technical security services Bogota, Colombia security installation (PoP Colombia); obligated USD 238,970.01. CapEx face = award obligation. Bogota named; site coords not stated — lat/lon blank.",
    "238970.01", "2010-12-06", "2010", "", "",
    "Technical security services security installation, Bogota, Colombia (USASpending description; Bogota named, site coords not stated — lat/lon blank).",
    "usaspending_valkyrie_colombia_bogota_tss_security_installation_239k_2010",
    "TECHNICAL SECURITY SERVICES BOGOTA, COLUMBIA SECURITY INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0228_1900_SAQMMA07D0026_1900/",
    "Actor: VALKYRIE ENTERPRISES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1162",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F0228_1900_SAQMMA07D0026_1900 (valkyrie_colombia_bogota_tss_security_installation_239k_2010). Signed 2010-12-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0228_1900_SAQMMA07D0026_1900/.",
    "USASpending: valkyrie_colombia_bogota_tss_security_installation_239k_2010 USD 0.239m. Supports valkyrie_colombia_bogota_tss_security_installation_239k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 238970.01; date_signed 2010-12-06.",
)
row_doc(
    "spectrum_electrical_brazil_brasilia_electrical_work_139k_2016",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical Services — Brazil Brasilia electrical work",
    "Brazil",
    "24 Sep 2016: Department of State awards contract SAQMMA16F4973 to Spectrum Electrical Services, Inc for electrical work Brasilia (PoP Brazil); obligated USD 138,710.6. CapEx face = award obligation. Brasilia named; site coords not stated — lat/lon blank.",
    "138710.60", "2016-09-24", "2016", "", "",
    "Electrical work Brasilia, Brazil (USASpending description; Brasilia named, site coords not stated — lat/lon blank).",
    "usaspending_spectrum_electrical_brazil_brasilia_electrical_work_139k_2016",
    "ELECTRICAL WORK BRASILIA IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F4973_1900_SAQMMA15D0025_1900/",
    "Actor: SPECTRUM ELECTRICAL SERVICES, INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1162",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F4973_1900_SAQMMA15D0025_1900 (spectrum_electrical_brazil_brasilia_electrical_work_139k_2016). Signed 2016-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F4973_1900_SAQMMA15D0025_1900/.",
    "USASpending: spectrum_electrical_brazil_brasilia_electrical_work_139k_2016 USD 0.139m. Supports spectrum_electrical_brazil_brasilia_electrical_work_139k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 138710.6; date_signed 2016-09-24.",
)
row_doc(
    "misc_haiti_cas20_cas21_tiles_install_15k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti FAC installation of tiles in CAS20 and CAS21",
    "Haiti",
    "19 Sep 2023: Department of State awards contract 19HA7023P1309 for FAC installation of tiles in CAS20 and CAS21 (PoP Haiti); obligated USD 14,919.68. CapEx face = award obligation. CAS20/CAS21 named; site coords not stated — lat/lon blank.",
    "14919.68", "2023-09-19", "2023", "", "",
    "Installation of tiles in CAS20 and CAS21, Haiti (USASpending description; CAS units named, site coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_cas20_cas21_tiles_install_15k_2023",
    "FAC-INSTALLATION OF TILES IN CAS20 AND CAS21",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1309_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1162",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P1309_1900_-NONE-_-NONE- (misc_haiti_cas20_cas21_tiles_install_15k_2023). Signed 2023-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1309_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_cas20_cas21_tiles_install_15k_2023 USD 0.015m. Supports misc_haiti_cas20_cas21_tiles_install_15k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14919.68; date_signed 2023-09-19.",
)
row_doc(
    "misc_brazil_spds_residence_door_security_locks_15k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil SPDS door security locks for residences",
    "Brazil",
    "25 Jul 2019: Department of State awards contract 19BR9319P0672 for SPDS door security locks for residences (PoP Brazil); obligated USD 14,859.52. CapEx face = award obligation. Residences unnamed — lat/lon blank.",
    "14859.52", "2019-07-25", "2019", "", "",
    "SPDS door security locks for residences, Brazil (USASpending description; residences unnamed — lat/lon blank).",
    "usaspending_misc_brazil_spds_residence_door_security_locks_15k_2019",
    "SPDS  DOOR SECURITY LOCKS FOR RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0672_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1162",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9319P0672_1900_-NONE-_-NONE- (misc_brazil_spds_residence_door_security_locks_15k_2019). Signed 2019-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0672_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_spds_residence_door_security_locks_15k_2019 USD 0.015m. Supports misc_brazil_spds_residence_door_security_locks_15k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14859.52; date_signed 2019-07-25.",
)
row_doc(
    "misc_mexico_led_lamp_fixture_replacement_15k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico LED lamps fixture replacement",
    "Mexico",
    "6 Sep 2013: Department of State awards contract SMX11513M0462 for LED lamps fixture replacement (PoP Mexico); obligated USD 14,953.26. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14953.26", "2013-09-06", "2013", "", "",
    "LED lamps fixture replacement, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_led_lamp_fixture_replacement_15k_2013",
    "7901-LAMPS FIXTURE REPLACEMENT LED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11513M0462_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1162",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11513M0462_1900_-NONE-_-NONE- (misc_mexico_led_lamp_fixture_replacement_15k_2013). Signed 2013-09-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11513M0462_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_led_lamp_fixture_replacement_15k_2013 USD 0.015m. Supports misc_mexico_led_lamp_fixture_replacement_15k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14953.26; date_signed 2013-09-06.",
)

# === Cycle 1163 (seed 20262163) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "spectrum_electrical_uruguay_fire_alarm_upgrade_122k_2012",
    "infrastructure", "building_materials", "us",
    "Spectrum Electrical Services — Uruguay fire alarm upgrade",
    "Uruguay",
    "21 Mar 2012: Department of State awards contract SAQMMA12F1064 to Spectrum Electrical Services, Inc for fire alarm upgrade (PoP Uruguay); obligated USD 122,351.01. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "122351.01", "2012-03-21", "2012", "", "",
    "Fire alarm upgrade, Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_spectrum_electrical_uruguay_fire_alarm_upgrade_122k_2012",
    "FIRE ALARM UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1064_1900_SAQMMA08D0007_1900/",
    "Actor: SPECTRUM ELECTRICAL SERVICES, INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1163",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F1064_1900_SAQMMA08D0007_1900 (spectrum_electrical_uruguay_fire_alarm_upgrade_122k_2012). Signed 2012-03-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1064_1900_SAQMMA08D0007_1900/.",
    "USASpending: spectrum_electrical_uruguay_fire_alarm_upgrade_122k_2012 USD 0.122m. Supports spectrum_electrical_uruguay_fire_alarm_upgrade_122k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 122351.01; date_signed 2012-03-21.",
)
row_doc(
    "valkyrie_brazil_brasilia_security_installation_119k_2012",
    "infrastructure", "building_materials", "us",
    "Valkyrie Enterprises — Brazil Brasilia security installation",
    "Brazil",
    "23 Aug 2012: Department of State awards contract SAQMMA12F3006 to Valkyrie Enterprises, LLC for security installation Brasilia, Brazil (PoP Brazil); obligated USD 118,721.71. CapEx face = award obligation. Brasilia named; site coords not stated — lat/lon blank.",
    "118721.71", "2012-08-23", "2012", "", "",
    "Security installation, Brasilia, Brazil (USASpending description; Brasilia named, site coords not stated — lat/lon blank).",
    "usaspending_valkyrie_brazil_brasilia_security_installation_119k_2012",
    "SECURITY INSTALLATION BRASILIA, BRAZIL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3006_1900_SAQMMA07D0026_1900/",
    "Actor: VALKYRIE ENTERPRISES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1163",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F3006_1900_SAQMMA07D0026_1900 (valkyrie_brazil_brasilia_security_installation_119k_2012). Signed 2012-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3006_1900_SAQMMA07D0026_1900/.",
    "USASpending: valkyrie_brazil_brasilia_security_installation_119k_2012 USD 0.119m. Supports valkyrie_brazil_brasilia_security_installation_119k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 118721.71; date_signed 2012-08-23.",
)
row_doc(
    "misc_mexico_merida_cgr_pool_barrier_fence_replacement_15k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Merida CGR pool barrier fence replacement",
    "Mexico",
    "7 Jun 2024: Department of State awards contract 19MX5224P0104 for Merida CGR pool barrier fence replacement (PoP Mexico); obligated USD 14,900.34. CapEx face = award obligation. Merida CGR named; site coords not stated — lat/lon blank.",
    "14900.34", "2024-06-07", "2024", "", "",
    "Pool barrier fence replacement, Merida CGR, Mexico (USASpending description; Merida named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_merida_cgr_pool_barrier_fence_replacement_15k_2024",
    "MER/FAC/7355RSTR/FWP99/CGR/POOL BARRIER FENCE REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5224P0104_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1163",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5224P0104_1900_-NONE-_-NONE- (misc_mexico_merida_cgr_pool_barrier_fence_replacement_15k_2024). Signed 2024-06-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5224P0104_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_merida_cgr_pool_barrier_fence_replacement_15k_2024 USD 0.015m. Supports misc_mexico_merida_cgr_pool_barrier_fence_replacement_15k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14900.34; date_signed 2024-06-07.",
)
row_doc(
    "misc_peru_cmr_pool_bathrooms_upgrade_15k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru CMR pool bathrooms upgrade",
    "Peru",
    "25 Sep 2014: Department of State awards contract SPE50014C0018 to upgrade pool bathrooms at CMR Lima (PoP Peru); obligated USD 14,999.99. CapEx face = award obligation. CMR Lima named; site coords not stated — lat/lon blank.",
    "14999.99", "2014-09-25", "2014", "", "",
    "Upgrade pool bathrooms at CMR, Lima, Peru (USASpending description; CMR Lima named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_cmr_pool_bathrooms_upgrade_15k_2014",
    "LIMA- CONTRACT SERVICES TO UPGRADE POOL BATHROOMS AT CMR IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0018_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1163",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014C0018_1900_-NONE-_-NONE- (misc_peru_cmr_pool_bathrooms_upgrade_15k_2014). Signed 2014-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0018_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_cmr_pool_bathrooms_upgrade_15k_2014 USD 0.015m. Supports misc_peru_cmr_pool_bathrooms_upgrade_15k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14999.99; date_signed 2014-09-25.",
)
row_doc(
    "misc_peru_corah_da_ups_15k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru CORAH DA UPS",
    "Peru",
    "18 Jun 2015: Department of State awards contract SPE50015M1583 for UPS for CORAH DA (PoP Peru); obligated USD 14,935.8. CapEx face = award obligation. CORAH DA named; site coords not stated — lat/lon blank.",
    "14935.80", "2015-06-18", "2015", "", "",
    "UPS for CORAH DA, Peru (USASpending description; CORAH DA named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_corah_da_ups_15k_2015",
    "IN21PE04 UPS FOR CORAH DA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M1583_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1163",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015M1583_1900_-NONE-_-NONE- (misc_peru_corah_da_ups_15k_2015). Signed 2015-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M1583_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_corah_da_ups_15k_2015 USD 0.015m. Supports misc_peru_corah_da_ups_15k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14935.8; date_signed 2015-06-18.",
)

# === Cycle 1164 (seed 20262164) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_honduras_housing_6_complete_gensets_117k_2015",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Honduras housing purchase of 6 complete gensets",
    "Honduras",
    "13 Apr 2015: Department of State awards contract SHO80015F0195 to Cummins Power Generation Inc. for housing purchase of 6 complete gensets/generators (PoP Honduras); obligated USD 117,048.35. CapEx face = award obligation. Housing sites unnamed; site coords not stated — lat/lon blank.",
    "117048.35", "2015-04-13", "2015", "", "",
    "Purchase of 6 complete gensets for housing, Honduras (USASpending description; housing sites unnamed, site coords not stated — lat/lon blank).",
    "usaspending_cummins_honduras_housing_6_complete_gensets_117k_2015",
    "HOUSING - PURCHASE OF  6 COMPLETE GENSETS (GENERATORS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80015F0195_1900_GS07F9004D_4730/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1164",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80015F0195_1900_GS07F9004D_4730 (cummins_honduras_housing_6_complete_gensets_117k_2015). Signed 2015-04-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80015F0195_1900_GS07F9004D_4730/.",
    "USASpending: cummins_honduras_housing_6_complete_gensets_117k_2015 USD 0.117m. Supports cummins_honduras_housing_6_complete_gensets_117k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 117048.35; date_signed 2015-04-13.",
)
row_doc(
    "applied_security_colombia_bogota_tss_security_installation_115k_2010",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Colombia Bogota TSS security installation",
    "Colombia",
    "24 Jun 2010: Department of State awards contract SAQMMA10F2260 to Applied Security Technologies Inc for TSS Bogota, Colombia security installation (PoP Colombia); obligated USD 114,927.44. CapEx face = award obligation. Bogota named; site coords not stated — lat/lon blank.",
    "114927.44", "2010-06-24", "2010", "", "",
    "TSS security installation, Bogota, Colombia (USASpending description; Bogota named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_colombia_bogota_tss_security_installation_115k_2010",
    "TSS BOGOTA, COLOMBIA SECURITY INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F2260_1900_SAQMMA07D0030_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1164",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F2260_1900_SAQMMA07D0030_1900 (applied_security_colombia_bogota_tss_security_installation_115k_2010). Signed 2010-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F2260_1900_SAQMMA07D0030_1900/.",
    "USASpending: applied_security_colombia_bogota_tss_security_installation_115k_2010 USD 0.115m. Supports applied_security_colombia_bogota_tss_security_installation_115k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 114927.44; date_signed 2010-06-24.",
)
row_doc(
    "misc_honduras_new_properties_acs_supply_install_15k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras supply and installation of A/Cs on new properties FAP",
    "Honduras",
    "26 May 2016: Department of State awards contract SHO80016M0754 for housing supply and installation of A/Cs on new properties FAP (PoP Honduras); obligated USD 14,844.45. CapEx face = award obligation. Exact properties unnamed — lat/lon blank.",
    "14844.45", "2016-05-26", "2016", "", "",
    "Supply and installation of A/Cs on new properties FAP, Honduras (USASpending description; properties unnamed — lat/lon blank).",
    "usaspending_misc_honduras_new_properties_acs_supply_install_15k_2016",
    "HOUSING_SUPPLY AND INSTALLATION OF A/CS ON NEW PROPERTIES _FAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80016M0754_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1164",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80016M0754_1900_-NONE-_-NONE- (misc_honduras_new_properties_acs_supply_install_15k_2016). Signed 2016-05-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80016M0754_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_new_properties_acs_supply_install_15k_2016 USD 0.015m. Supports misc_honduras_new_properties_acs_supply_install_15k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14844.45; date_signed 2016-05-26.",
)
row_doc(
    "misc_honduras_windows_and_frames_15k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras windows and frames",
    "Honduras",
    "12 Sep 2023: Department of State awards contract 19H08023K0603 for windows and frames (PoP Honduras); obligated USD 14,743.85. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14743.85", "2023-09-12", "2023", "", "",
    "Windows and frames, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_windows_and_frames_15k_2023",
    "WINDOWS AND FRAMES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08023K0603_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1164",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08023K0603_1900_-NONE-_-NONE- (misc_honduras_windows_and_frames_15k_2023). Signed 2023-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08023K0603_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_windows_and_frames_15k_2023 USD 0.015m. Supports misc_honduras_windows_and_frames_15k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14743.85; date_signed 2023-09-12.",
)
row_doc(
    "misc_costa_rica_bedroom_closets_install_15k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica provide and install bedroom closets",
    "Costa Rica",
    "13 Sep 2017: Department of State awards contract SCS80017M0726 for provide and install bedroom closets (PoP Costa Rica); obligated USD 14,999.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14999", "2017-09-13", "2017", "", "",
    "Provide and install bedroom closets, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_costa_rica_bedroom_closets_install_15k_2017",
    "PROVIDE AND INSTALL BEDROOM CLOSETS  IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80017M0726_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1164",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80017M0726_1900_-NONE-_-NONE- (misc_costa_rica_bedroom_closets_install_15k_2017). Signed 2017-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80017M0726_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_bedroom_closets_install_15k_2017 USD 0.015m. Supports misc_costa_rica_bedroom_closets_install_15k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14999.0; date_signed 2017-09-13.",
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
