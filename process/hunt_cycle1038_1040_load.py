#!/usr/bin/env python3
"""Cycles 1038–1040: USASpending LatAm CapEx residual (~USD0.05–0.08m).

Seeds: 20262038–20262040. Thin top-up dry.
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

# === Cycle 1038 ===
row_doc(
    "misc_argentina_oro_bathrooms_75k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina CMR Oro building bathroom repair",
    "Argentina",
    "23 Sep 2021: Department of State awards contract 19AR2021C0016 for FAC/CMR repair bathrooms in Oro building (PoP Argentina); obligated USD 74,992.26. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "74992.26", "2021-09-23", "2021", "", "",
    "Bathroom repair in Oro building at CMR, Argentina (USASpending PoP Argentina; site not named — lat/lon blank).",
    "usaspending_misc_argentina_oro_bathrooms_75k_2021",
    "FAC/ CMR - REPAIR BATHROOMS IN ORO BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021C0016_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1038",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2021C0016_1900_-NONE-_-NONE- (Argentina Oro bathrooms). Signed 2021-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021C0016_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina Oro bathrooms USD 0.075m. Supports misc_argentina_oro_bathrooms_75k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74992.26; date_signed 2021-09-23.",
)

row_doc(
    "misc_brazil_hr_renovation_75k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil Porto Alegre consulate HR renovation",
    "Brazil",
    "18 Jul 2024: Department of State awards contract 19BR7224P0117 for HR renovation — consulate building (PoP Brazil); obligated USD 74,778.95. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "74778.95", "2024-07-18", "2024", "", "",
    "HR renovation at consulate building, Brazil (USASpending PoP Brazil; site not named — lat/lon blank).",
    "usaspending_misc_brazil_hr_renovation_75k_2024",
    "19BR7224P0117-POA-FAC-MCIXJ-0G-0006-HR RENOVATION-CONSULATE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR7224P0117_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1038",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR7224P0117_1900_-NONE-_-NONE- (Brazil HR renovation). Signed 2024-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR7224P0117_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil HR renovation USD 0.075m. Supports misc_brazil_hr_renovation_75k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74778.95; date_signed 2024-07-18.",
)

row_doc(
    "morera_cr_hazmat_75k_2020",
    "infrastructure", "building_materials", "other",
    "José Gustavo Morera Rojas — Costa Rica INL hazmat storage room",
    "Costa Rica",
    "23 Jul 2020: Department of State awards contract 19CS8020P0732 to José Gustavo Morera Rojas for INL hazmat storage room and other civil works at base (PoP Costa Rica); obligated USD 74,644.53. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "74644.53", "2020-07-23", "2020", "", "",
    "Hazmat storage room and civil works at base, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_morera_cr_hazmat_75k_2020",
    "INL 1930.0 HAZMAT STORAGE ROOM AND OTHER CIVIL WORKS AT BASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8020P0732_1900_-NONE-_-NONE-/",
    "Actor: José Gustavo Morera Rojas (Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1038",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8020P0732_1900_-NONE-_-NONE- (Morera CR hazmat). Signed 2020-07-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8020P0732_1900_-NONE-_-NONE-/.",
    "USASpending: Morera CR hazmat USD 0.075m. Supports morera_cr_hazmat_75k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74644.53; date_signed 2020-07-23.",
)

row_doc(
    "rogers_punta_culebra_butterfly_75k_2023",
    "infrastructure", "building_materials", "other",
    "Constructora Rogers — Panama STRI butterfly dome at Punta Culebra",
    "Panama",
    "18 Aug 2023: Smithsonian awards order 33330223FF0010425 to Constructora Rogers for construct butterfly dome at Punta Culebra; obligated USD 74,547.47. CapEx face = award obligation.",
    "74547.47", "2023-08-18", "2023", "8.912", "-79.530",
    "Butterfly dome construction at Punta Culebra, Panama (USASpending description; Punta Culebra named).",
    "usaspending_rogers_punta_culebra_butterfly_75k_2023",
    "STRI: CONSTRUCT BUTTERFLY DOME AT PUNTA CULEBRA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223FF0010425_3300_F15CC10192_3300/",
    "Actor: Constructora Rogers S.A. (CONROSA) (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1038",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330223FF0010425_3300_F15CC10192_3300 (Rogers Punta Culebra butterfly). Signed 2023-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223FF0010425_3300_F15CC10192_3300/.",
    "USASpending: Rogers Punta Culebra butterfly USD 0.075m. Supports rogers_punta_culebra_butterfly_75k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74547.47; date_signed 2023-08-18.",
)

row_doc(
    "alban_bolivia_generators_74k_2016",
    "energy", "power_plants_grid", "us",
    "Alban Tractor — Bolivia La Paz generators",
    "Bolivia",
    "4 Mar 2016: Department of State awards order SAQMMA16F1054 to Alban Tractor for generators La Paz (PoP Bolivia); obligated USD 73,759. CapEx face = award obligation.",
    "73759", "2016-03-04", "2016", "-16.500", "-68.150",
    "Generators, La Paz, Bolivia (USASpending description; La Paz named).",
    "usaspending_alban_bolivia_generators_74k_2016",
    "GENERATORS LA PAZ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F1054_1900_SAQMMA15D0050_1900/",
    "Actor: Alban Tractor, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1038",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F1054_1900_SAQMMA15D0050_1900 (Alban Bolivia generators). Signed 2016-03-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F1054_1900_SAQMMA15D0050_1900/.",
    "USASpending: Alban Bolivia generators USD 0.074m. Supports alban_bolivia_generators_74k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 73759; date_signed 2016-03-04.",
)

# === Cycle 1039 ===
row_doc(
    "flores_ecuador_bathrooms_74k_2022",
    "infrastructure", "building_materials", "other",
    "Flores Serrano — Ecuador annex building bathroom remodel",
    "Ecuador",
    "20 Jul 2022: Department of State awards contract 19EC7522C0014 to Flores Serrano Guillermo Sebastian for annex building remodel 2 bathrooms (PoP Ecuador); obligated USD 74,499.60. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "74499.6", "2022-07-20", "2022", "", "",
    "Annex building bathroom remodel, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_flores_ecuador_bathrooms_74k_2022",
    "PR10801601-7901RSTR-ANNEX BUILDING-FWP275-REMODEL2BATHROOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0014_1900_-NONE-_-NONE-/",
    "Actor: Flores Serrano Guillermo Sebastian (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1039",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0014_1900_-NONE-_-NONE- (Flores Ecuador bathrooms). Signed 2022-07-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0014_1900_-NONE-_-NONE-/.",
    "USASpending: Flores Ecuador bathrooms USD 0.074m. Supports flores_ecuador_bathrooms_74k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74499.6; date_signed 2022-07-20.",
)

row_doc(
    "iscar_colombia_warehouse_deck_74k_2024",
    "infrastructure", "building_materials", "us",
    "Iscar GSE — Colombia GSO warehouse decking finish",
    "Colombia",
    "27 Sep 2024: Department of State awards contract 19C02024P1978 to Iscar GSE for finish the decking in the warehouse (PoP Colombia); obligated USD 74,450.60. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "74450.6", "2024-09-27", "2024", "", "",
    "GSO warehouse decking finish, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_iscar_colombia_warehouse_deck_74k_2024",
    "PR12630183: EOY GSO PR3 FINISH THE DECKING IN THE WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P1978_1900_-NONE-_-NONE-/",
    "Actor: Iscar GSE Corp. (Miami FL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1039",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024P1978_1900_-NONE-_-NONE- (Iscar Colombia warehouse deck). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P1978_1900_-NONE-_-NONE-/.",
    "USASpending: Iscar Colombia warehouse deck USD 0.074m. Supports iscar_colombia_warehouse_deck_74k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74450.6; date_signed 2024-09-27.",
)

row_doc(
    "misc_argentina_dcmr_ae_74k_2021",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Argentina DCMR Virrey del Pino renovation A&E",
    "Argentina",
    "19 Aug 2021: Department of State awards contract 19AR2021C0008 for A&E for renovation at DCMR Virrey del Pino (PoP Argentina); obligated USD 74,391.63. CapEx face = award obligation. Recipient redacted.",
    "74391.63", "2021-08-19", "2021", "-34.567", "-58.435",
    "A&E for DCMR renovation at Virrey del Pino, Argentina (USASpending description; Virrey del Pino named).",
    "usaspending_misc_argentina_dcmr_ae_74k_2021",
    "FAC- A&E FOR RENOVATION AT DCMR VIRREY DEL PINO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1039",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2021C0008_1900_-NONE-_-NONE- (Argentina DCMR A&E). Signed 2021-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021C0008_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina DCMR A&E USD 0.074m. Supports misc_argentina_dcmr_ae_74k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74391.63; date_signed 2021-08-19.",
)

row_doc(
    "chang_salvador_barracks_74k_2011",
    "infrastructure", "building_materials", "other",
    "Edwing Alberto Chang — El Salvador barracks E renovation and SOF construct",
    "El Salvador",
    "23 Mar 2011: DoD awards contract W9127811P0154 to Edwing Alberto Chang to renovate barracks E and construct SOF (PoP El Salvador); obligated USD 74,219.02. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "74219.02", "2011-03-23", "2011", "", "",
    "Barracks E renovation and SOF construction, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_chang_salvador_barracks_74k_2011",
    "TAS::97 0500::TAS RENOVATE BARRACKS E AND CONSTRUCT SOF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0154_9700_-NONE-_-NONE-/",
    "Actor: Edwing Alberto Chang (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1039",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0154_9700_-NONE-_-NONE- (Chang Salvador barracks). Signed 2011-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0154_9700_-NONE-_-NONE-/.",
    "USASpending: Chang Salvador barracks USD 0.074m. Supports chang_salvador_barracks_74k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74219.02; date_signed 2011-03-23.",
)

row_doc(
    "misc_peru_asphalt_road_74k_2011",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Peru interior asphalt road repair",
    "Peru",
    "24 Aug 2011: DoD awards contract SPE50011C0059 for repair interior asphalt road (PoP Peru); obligated USD 73,755.17. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "73755.17", "2011-08-24", "2011", "", "",
    "Interior asphalt road repair, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_misc_peru_asphalt_road_74k_2011",
    "FAC - CONTRACT REPAIR INTERIOR ASPHALT ROAD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50011C0059_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1039",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50011C0059_1900_-NONE-_-NONE- (Peru asphalt road). Signed 2011-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50011C0059_1900_-NONE-_-NONE-/.",
    "USASpending: Peru asphalt road USD 0.074m. Supports misc_peru_asphalt_road_74k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 73755.17; date_signed 2011-08-24.",
)

# === Cycle 1040 ===
row_doc(
    "misc_peru_chancery_roof_74k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru Lima chancery roof repair",
    "Peru",
    "30 Sep 2014: DoD awards contract SPE50014C0021 to repair chancery roof Lima (PoP Peru); obligated USD 73,557.28. CapEx face = award obligation. Recipient redacted.",
    "73557.28", "2014-09-30", "2014", "-12.099", "-76.969",
    "Chancery roof repair, Lima, Peru (USASpending description; Lima named).",
    "usaspending_misc_peru_chancery_roof_74k_2014",
    "LIMA- CONTRACT TO REPAIR CHANCERY ROOF IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0021_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1040",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014C0021_1900_-NONE-_-NONE- (Peru chancery roof). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0021_1900_-NONE-_-NONE-/.",
    "USASpending: Peru chancery roof USD 0.074m. Supports misc_peru_chancery_roof_74k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 73557.28; date_signed 2014-09-30.",
)

row_doc(
    "misc_mexico_canadas_roof_73k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Cañadas roof repairs",
    "Mexico",
    "11 Jun 2019: Department of State awards contract 19MX5319C0009 for OBO roof repairs at Cañadas (PoP Mexico); obligated USD 73,220.73. CapEx face = award obligation. Recipient redacted.",
    "73220.73", "2019-06-11", "2019", "", "",
    "Roof repairs at Cañadas, Mexico (USASpending description; Cañadas named but coordinates not sourced — lat/lon blank).",
    "usaspending_misc_mexico_canadas_roof_73k_2019",
    "MEX-FAC-OBO-ROOF REPAIRS AT CANADAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0009_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1040",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319C0009_1900_-NONE-_-NONE- (Mexico Cañadas roof). Signed 2019-06-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0009_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico Cañadas roof USD 0.073m. Supports misc_mexico_canadas_roof_73k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 73220.73; date_signed 2019-06-11.",
)

row_doc(
    "misc_chile_chancery_bathrooms_73k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile chancery LV2 and LV3 bathrooms",
    "Chile",
    "10 Apr 2024: Department of State awards contract 19C18024P0584 for chancery LV2 and LV3 bathrooms (PoP Chile); obligated USD 73,183.40. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "73183.4", "2024-04-10", "2024", "", "",
    "Chancery LV2 and LV3 bathrooms, Chile (USASpending PoP Chile; site not named — lat/lon blank).",
    "usaspending_misc_chile_chancery_bathrooms_73k_2024",
    "FWP #343.02 CHANCERY LV2 AND LV3 BATHROOMS / 7901R",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18024P0584_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1040",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18024P0584_1900_-NONE-_-NONE- (Chile chancery bathrooms). Signed 2024-04-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18024P0584_1900_-NONE-_-NONE-/.",
    "USASpending: Chile chancery bathrooms USD 0.073m. Supports misc_chile_chancery_bathrooms_73k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 73183.4; date_signed 2024-04-10.",
)

row_doc(
    "jj_soto_cano_electric_gate_72k_2010",
    "infrastructure", "building_materials", "us",
    "J & J Maintenance — Soto Cano electric gate access AT/FP",
    "Honduras",
    "22 Sep 2010: DoD awards delivery order 0009 under W9127809D0068 to J & J Maintenance for AT/FP electric gate access, Soto Cano Air Base, Honduras; obligated USD 71,526.17. CapEx face = award obligation.",
    "71526.17", "2010-09-22", "2010", "14.382", "-87.621",
    "Electric gate access AT/FP, Soto Cano Air Base, Honduras (USASpending description; Soto Cano named).",
    "usaspending_jj_soto_cano_electric_gate_72k_2010",
    "AT/FP FOR ELECTRIC GATE ACCESS, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0068_9700/",
    "Actor: J & J Maintenance Inc. (Austin TX, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1040",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127809D0068_9700 (J&J Soto Cano electric gate). Signed 2010-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0068_9700/.",
    "USASpending: J&J Soto Cano electric gate USD 0.072m. Supports jj_soto_cano_electric_gate_72k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71526.17; date_signed 2010-09-22.",
)

row_doc(
    "siegel_guatemala_roof_ae_72k_2020",
    "infrastructure", "engineering_epc", "us",
    "Robert Siegel — Guatemala City A&E roofing services",
    "Guatemala",
    "9 Nov 2020: Department of State awards order 19AQMM21F0063 to Robert Siegel for Guatemala City A&E roofing services; obligated USD 72,113.60. CapEx face = award obligation.",
    "72113.6", "2020-11-09", "2020", "14.635", "-90.507",
    "A&E roofing services, Guatemala City, Guatemala (USASpending description; Guatemala City named).",
    "usaspending_siegel_guatemala_roof_ae_72k_2020",
    "GUATEMALA CITY, GUATEMALA AE ROOFING SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0063_1900_19AQMM19D0046_1900/",
    "Actor: Robert Siegel (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1040",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F0063_1900_19AQMM19D0046_1900 (Siegel Guatemala roof A&E). Signed 2020-11-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0063_1900_19AQMM19D0046_1900/.",
    "USASpending: Siegel Guatemala roof A&E USD 0.072m. Supports siegel_guatemala_roof_ae_72k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 72113.6; date_signed 2020-11-09.",
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
    print(f"cycles1038-1040 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
