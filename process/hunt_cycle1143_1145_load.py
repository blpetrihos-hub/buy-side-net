#!/usr/bin/env python3
"""Cycles 1143–1145: USASpending LatAm CapEx residual (~USD0.008–0.033m).

Seeds: 20262143–20262145. Thin top-up dry.
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


# === Cycle 1143 (seed 20262143) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "automation_aids_mexico_inl_21st_floor_ups_units_12k_2019",
    "energy", "power_plants_grid", "us",
    "Automation Aids — Mexico INL PD&S UPS units for the 21st floor",
    "Mexico",
    "19 Jul 2019: Department of State awards contract 19MX9019F0027 to Automation Aids Inc for INL PD&S UPS units for the 21st floor (PoP Mexico); obligated USD 11,998. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "11998", "2019-07-19", "2019", "", "",
    "INL PD&S UPS units for the 21st floor, Mexico (USASpending description; floor named, site coords not stated — lat/lon blank).",
    "usaspending_automation_aids_mexico_inl_21st_floor_ups_units_12k_2019",
    "INL-MI-IN81MXM1-INL PD&S - UPS UNITS FOR THE 21ST FLOOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX9019F0027_1900_47QSEA19D0074_4732/",
    "Actor: Automation Aids Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1143",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX9019F0027_1900_47QSEA19D0074_4732 (automation_aids_mexico_inl_21st_floor_ups_units_12k_2019). Signed 2019-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX9019F0027_1900_47QSEA19D0074_4732/.",
    "USASpending: automation_aids_mexico_inl_21st_floor_ups_units_12k_2019 USD 0.012m. Supports automation_aids_mexico_inl_21st_floor_ups_units_12k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11998; date_signed 2019-07-19.",
)
row_doc(
    "harden_mexico_metal_door_screen_8k_2022",
    "infrastructure", "building_materials", "us",
    "Harden Architectural Security Products — Mexico metal door screen for international embassies",
    "Mexico",
    "2 May 2022: Department of State awards contract 19AQMM22P0489 to Harden Architectural Security Products, LLC for metal door screen etc. (PoP Mexico); obligated USD 8,000. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "8000", "2022-05-02", "2022", "", "",
    "Metal door screen etc., Mexico (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_harden_mexico_metal_door_screen_8k_2022",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0489_1900_-NONE-_-NONE-/",
    "Actor: Harden Architectural Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1143",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0489_1900_-NONE-_-NONE- (harden_mexico_metal_door_screen_8k_2022). Signed 2022-05-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0489_1900_-NONE-_-NONE-/.",
    "USASpending: harden_mexico_metal_door_screen_8k_2022 USD 0.008m. Supports harden_mexico_metal_door_screen_8k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8000; date_signed 2022-05-02.",
)
row_doc(
    "automatica_el_salvador_transformer_33k_2020",
    "energy", "power_plants_grid", "other",
    "Automatica Consultoria y Sistemas — El Salvador transformer",
    "El Salvador",
    "29 Sep 2020: Department of State awards contract 19ES6020P0915 to Automatica Consultoria y Sistemas SA de CV for transformer (PoP El Salvador); obligated USD 32,883. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "32883", "2020-09-29", "2020", "", "",
    "Transformer, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_automatica_el_salvador_transformer_33k_2020",
    "TRANSFORMER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0915_1900_-NONE-_-NONE-/",
    "Actor: Automatica Consultoria y Sistemas SA de CV (El Salvador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1143",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6020P0915_1900_-NONE-_-NONE- (automatica_el_salvador_transformer_33k_2020). Signed 2020-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0915_1900_-NONE-_-NONE-/.",
    "USASpending: automatica_el_salvador_transformer_33k_2020 USD 0.033m. Supports automatica_el_salvador_transformer_33k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 32883; date_signed 2020-09-29.",
)
row_doc(
    "misc_haiti_ups_purchasing_12k_2021",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti UPS purchasing",
    "Haiti",
    "15 Dec 2021: Department of State awards contract 19HA7022P0086 for UPS purchasing (PoP Haiti); obligated USD 12,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12000", "2021-12-15", "2021", "", "",
    "UPS purchasing, Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_haiti_ups_purchasing_12k_2021",
    "UPS PURCHASING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7022P0086_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1143",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7022P0086_1900_-NONE-_-NONE- (misc_haiti_ups_purchasing_12k_2021). Signed 2021-12-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7022P0086_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_ups_purchasing_12k_2021 USD 0.012m. Supports misc_haiti_ups_purchasing_12k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12000; date_signed 2021-12-15.",
)
row_doc(
    "misc_chile_rso_grills_installation_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile RSO grills installation",
    "Chile",
    "29 Jun 2016: Department of State awards contract SCI80016L0129 for BPA call - RSO grills installation (PoP Chile); obligated USD 13,998.80. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13998.8", "2016-06-29", "2016", "", "",
    "RSO grills installation, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_chile_rso_grills_installation_14k_2016",
    "BPA CALL - RSO GRILLS INSTALLATION IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80016L0129_1900_SCI80015A0006_1900/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1143",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80016L0129_1900_SCI80015A0006_1900 (misc_chile_rso_grills_installation_14k_2016). Signed 2016-06-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80016L0129_1900_SCI80015A0006_1900/.",
    "USASpending: misc_chile_rso_grills_installation_14k_2016 USD 0.014m. Supports misc_chile_rso_grills_installation_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13998.8; date_signed 2016-06-29.",
)

# === Cycle 1144 (seed 20262144) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "montage_colombia_chiller_upgrade_8k_2016",
    "energy", "power_plants_grid", "us",
    "Montage — Colombia chiller upgrade",
    "Colombia",
    "29 Sep 2016: Department of State awards contract SAQMMA16M2952 to Montage, Inc. for chiller upgrade (PoP Colombia); obligated USD 8,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8000", "2016-09-29", "2016", "", "",
    "Chiller upgrade, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_montage_colombia_chiller_upgrade_8k_2016",
    "CHILLER UPGRADE  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M2952_1900_-NONE-_-NONE-/",
    "Actor: Montage, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1144",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M2952_1900_-NONE-_-NONE- (montage_colombia_chiller_upgrade_8k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M2952_1900_-NONE-_-NONE-/.",
    "USASpending: montage_colombia_chiller_upgrade_8k_2016 USD 0.008m. Supports montage_colombia_chiller_upgrade_8k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8000; date_signed 2016-09-29.",
)
row_doc(
    "supplies_services_venezuela_hvac_variable_frequency_drivers_11k_2014",
    "energy", "power_plants_grid", "us",
    "Supplies & Services International — Venezuela variable frequency drivers for HVAC systems",
    "Venezuela",
    "10 Sep 2014: Department of State awards contract SVE30014M0640 to Supplies & Services International Inc for variable frequency drivers for HVAC systems (PoP Venezuela); obligated USD 10,968. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "10968", "2014-09-10", "2014", "", "",
    "Variable frequency drivers for HVAC systems, Venezuela (USASpending description; site not named — lat/lon blank).",
    "usaspending_supplies_services_venezuela_hvac_variable_frequency_drivers_11k_2014",
    "7901.C - VARIABLE FRECUENCY DRIVERS FOR HVAC SYSTEMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0640_1900_-NONE-_-NONE-/",
    "Actor: Supplies & Services International Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1144",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30014M0640_1900_-NONE-_-NONE- (supplies_services_venezuela_hvac_variable_frequency_drivers_11k_2014). Signed 2014-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0640_1900_-NONE-_-NONE-/.",
    "USASpending: supplies_services_venezuela_hvac_variable_frequency_drivers_11k_2014 USD 0.011m. Supports supplies_services_venezuela_hvac_variable_frequency_drivers_11k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10968; date_signed 2014-09-10.",
)
row_doc(
    "misc_honduras_caratasca_navy_base_generator_30k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras HO Navy Base Caratasca generator",
    "Honduras",
    "18 Aug 2011: Department of State awards contract SHO80011M0413 for MILGP generator for HO Navy Base in Caratasca (PoP Honduras); obligated USD 30,000. CapEx face = award obligation. Caratasca Navy Base named; site coords not stated — lat/lon blank.",
    "30000", "2011-08-18", "2011", "", "",
    "Generator for HO Navy Base in Caratasca, Honduras (USASpending description; Caratasca named, site coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_caratasca_navy_base_generator_30k_2011",
    "MILGP - GENERATOR FOR HO NAVY BASE IN CARATASCA 1150.0",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80011M0413_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1144",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80011M0413_1900_-NONE-_-NONE- (misc_honduras_caratasca_navy_base_generator_30k_2011). Signed 2011-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80011M0413_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_caratasca_navy_base_generator_30k_2011 USD 0.030m. Supports misc_honduras_caratasca_navy_base_generator_30k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 30000; date_signed 2011-08-18.",
)
row_doc(
    "misc_ecuador_dea_five_generators_glqs_install_30k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador DEA installation of five generators at GLQS",
    "Ecuador",
    "22 Aug 2011: Department of State awards contract SEC30011M0388 for G-DEA installation of five generators at GLQS (PoP Ecuador); obligated USD 30,000. CapEx face = award obligation. GLQS named; site coords not stated — lat/lon blank.",
    "30000", "2011-08-22", "2011", "", "",
    "Installation of five generators at GLQS, Ecuador (USASpending description; GLQS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_dea_five_generators_glqs_install_30k_2011",
    "G-DEA INSTALLATION OF FIVE GENERATORS AT GLQS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30011M0388_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1144",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC30011M0388_1900_-NONE-_-NONE- (misc_ecuador_dea_five_generators_glqs_install_30k_2011). Signed 2011-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30011M0388_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_dea_five_generators_glqs_install_30k_2011 USD 0.030m. Supports misc_ecuador_dea_five_generators_glqs_install_30k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 30000; date_signed 2011-08-22.",
)
row_doc(
    "misc_costa_rica_sng_drake_perimeter_security_fence_30k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica INL perimetral security fence for SNG Drake Station",
    "Costa Rica",
    "19 Apr 2024: Department of State awards contract 19CS8024P0652 for INL perimetral security fence for SNG Drake Station (PoP Costa Rica); obligated USD 29,985. CapEx face = award obligation. SNG Drake Station named; site coords not stated — lat/lon blank.",
    "29985", "2024-04-19", "2024", "", "",
    "Perimetral security fence for SNG Drake Station, Costa Rica (USASpending description; Drake Station named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_sng_drake_perimeter_security_fence_30k_2024",
    "1930.0 INL PERIMETRAL SECURITY FENCE FOR SNG DRAKE STATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P0652_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1144",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8024P0652_1900_-NONE-_-NONE- (misc_costa_rica_sng_drake_perimeter_security_fence_30k_2024). Signed 2024-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P0652_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_sng_drake_perimeter_security_fence_30k_2024 USD 0.030m. Supports misc_costa_rica_sng_drake_perimeter_security_fence_30k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29985; date_signed 2024-04-19.",
)

# === Cycle 1145 (seed 20262145) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "bh_foto_haiti_pap_pd_cameras_12k_2024",
    "infrastructure", "building_materials", "us",
    "B & H Foto & Electronics — Haiti Port-au-Prince PD cameras for public diplomacy office",
    "Haiti",
    "18 Sep 2024: Department of State awards contract 19HA7024P1303 to B & H Foto & Electronics Corp. for PAP PD camera order for the office of public diplomacy (PoP Haiti); obligated USD 11,999.80. CapEx face = award obligation. PAP PD named; site coords not stated — lat/lon blank.",
    "11999.8", "2024-09-18", "2024", "", "",
    "PAP PD cameras for public diplomacy office, Haiti (USASpending description; PAP PD named, site coords not stated — lat/lon blank).",
    "usaspending_bh_foto_haiti_pap_pd_cameras_12k_2024",
    "PAP PD CAMERA ORDER FOR THE OFFICE OF PUBLLIC DIPLOMACY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P1303_1900_-NONE-_-NONE-/",
    "Actor: B & H Foto & Electronics Corp. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1145",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7024P1303_1900_-NONE-_-NONE- (bh_foto_haiti_pap_pd_cameras_12k_2024). Signed 2024-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P1303_1900_-NONE-_-NONE-/.",
    "USASpending: bh_foto_haiti_pap_pd_cameras_12k_2024 USD 0.012m. Supports bh_foto_haiti_pap_pd_cameras_12k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11999.8; date_signed 2024-09-18.",
)
row_doc(
    "global_integration_colombia_hsi_camera_13k_2023",
    "infrastructure", "building_materials", "us",
    "Global Integration Logistics — Colombia camera for HSI",
    "Colombia",
    "11 May 2023: Department of State awards contract 19C01523P0234 to Global Integration Logistics Corp for camera for HSI (PoP Colombia); obligated USD 12,939.16. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12939.16", "2023-05-11", "2023", "", "",
    "Camera for HSI, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_global_integration_colombia_hsi_camera_13k_2023",
    "45/2310 CAMERA FOR HSI /0623",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523P0234_1900_-NONE-_-NONE-/",
    "Actor: Global Integration Logistics Corp (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1145",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01523P0234_1900_-NONE-_-NONE- (global_integration_colombia_hsi_camera_13k_2023). Signed 2023-05-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523P0234_1900_-NONE-_-NONE-/.",
    "USASpending: global_integration_colombia_hsi_camera_13k_2023 USD 0.013m. Supports global_integration_colombia_hsi_camera_13k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12939.16; date_signed 2023-05-11.",
)
row_doc(
    "misc_brazil_dcmr_generator_30k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil DCMR generator",
    "Brazil",
    "29 Feb 2024: Department of State awards contract 19BR2524P0290 for generator DCMR (PoP Brazil); obligated USD 29,997.55. CapEx face = award obligation. DCMR named; site coords not stated — lat/lon blank.",
    "29997.55", "2024-02-29", "2024", "", "",
    "Generator DCMR, Brazil (USASpending description; DCMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_dcmr_generator_30k_2024",
    "GENERATOR DCMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2524P0290_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1145",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2524P0290_1900_-NONE-_-NONE- (misc_brazil_dcmr_generator_30k_2024). Signed 2024-02-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2524P0290_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_dcmr_generator_30k_2024 USD 0.030m. Supports misc_brazil_dcmr_generator_30k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29997.55; date_signed 2024-02-29.",
)
row_doc(
    "misc_costa_rica_obc_switchgear_15ton_ac_install_29k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica install 15 tons A/C unit in OBC switchgear",
    "Costa Rica",
    "30 Sep 2013: Department of State awards contract SCS80013C0059 for install 15 tons A/C unit in OBC switchgear (PoP Costa Rica); obligated USD 28,937.68. CapEx face = award obligation. OBC switchgear named; site coords not stated — lat/lon blank.",
    "28937.68", "2013-09-30", "2013", "", "",
    "Install 15 tons A/C unit in OBC switchgear, Costa Rica (USASpending description; OBC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_obc_switchgear_15ton_ac_install_29k_2013",
    "7901.C/1901.0  INSTALL 15 TONS A/C UNIT IN OBC SWITCHGEAR. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013C0059_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1145",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80013C0059_1900_-NONE-_-NONE- (misc_costa_rica_obc_switchgear_15ton_ac_install_29k_2013). Signed 2013-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013C0059_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_obc_switchgear_15ton_ac_install_29k_2013 USD 0.029m. Supports misc_costa_rica_obc_switchgear_15ton_ac_install_29k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28937.68; date_signed 2013-09-30.",
)
row_doc(
    "misc_jamaica_police_college_office_renovation_29k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica INL interior renovation of office building at police college",
    "Jamaica",
    "9 Aug 2021: Department of State awards contract 19JM3721C0003 for INL interior renovation of office building at police college (PoP Jamaica); obligated USD 28,947.04. CapEx face = award obligation. Police college named; site coords not stated — lat/lon blank.",
    "28947.04", "2021-08-09", "2021", "", "",
    "Interior renovation of office building at police college, Jamaica (USASpending description; police college named, site coords not stated — lat/lon blank).",
    "usaspending_misc_jamaica_police_college_office_renovation_29k_2021",
    "INL - INTERIOR RENOVATION OF OFFICE BUILDING AT POLICE COLLEGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3721C0003_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1145",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3721C0003_1900_-NONE-_-NONE- (misc_jamaica_police_college_office_renovation_29k_2021). Signed 2021-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3721C0003_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_police_college_office_renovation_29k_2021 USD 0.029m. Supports misc_jamaica_police_college_office_renovation_29k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28947.04; date_signed 2021-08-09.",
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
