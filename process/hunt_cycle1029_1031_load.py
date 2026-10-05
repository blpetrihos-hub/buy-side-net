#!/usr/bin/env python3
"""Cycles 1029–1031: USASpending LatAm CapEx residual (~USD0.07–0.09m).

Seeds: 20262029–20262031. Thin top-up dry.
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

# === Cycle 1029 ===
row_doc(
    "olc_peru_ups_94k_2017",
    "energy", "power_plants_grid", "other",
    "OLC Ingenieros — Peru NAMRU-6 emergency UPS Iquitos and Puerto Maldonado",
    "Peru",
    "29 Sep 2017: DoD awards contract SPE50017C0043 to OLC Ingenieros for NAMRU-6 upgrade emergency UPS at Iquitos and Puerto Maldonado; obligated USD 93,845.40. CapEx face = award obligation. Dual-site — lat/lon blank.",
    "93845.4", "2017-09-29", "2017", "", "",
    "Emergency UPS upgrade at Iquitos and Puerto Maldonado, Peru (USASpending description; dual-site — lat/lon blank).",
    "usaspending_olc_peru_ups_94k_2017",
    "NAMRU6 - UPGRADE EMERGENCY UPS AT IQUITOS&P.MALDONADO \"IGF::OT::IGF\"",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017C0043_1900_-NONE-_-NONE-/",
    "Actor: OLC Ingenieros E.I.R.L. (Peru) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1029",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50017C0043_1900_-NONE-_-NONE- (OLC Peru UPS). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017C0043_1900_-NONE-_-NONE-/.",
    "USASpending: OLC Peru UPS USD 0.094m. Supports olc_peru_ups_94k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 93845.4; date_signed 2017-09-29.",
)

row_doc(
    "fg_colombia_conat_generator_92k_2022",
    "energy", "power_plants_grid", "other",
    "Ingeniería y Servicios FG — Colombia CONAT building generator",
    "Colombia",
    "27 Sep 2022: Department of State awards contract 19C01522P0431 to Ingeniería y Servicios FG for generator for CONAT building (PoP Colombia); obligated USD 92,248.11. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "92248.11", "2022-09-27", "2022", "", "",
    "Generator for CONAT building, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_fg_colombia_conat_generator_92k_2022",
    "43/GENERATOR FOR CONAT BUILDING/1022",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01522P0431_1900_-NONE-_-NONE-/",
    "Actor: Ingeniería y Servicios FG S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1029",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01522P0431_1900_-NONE-_-NONE- (FG CONAT generator). Signed 2022-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01522P0431_1900_-NONE-_-NONE-/.",
    "USASpending: FG CONAT generator USD 0.092m. Supports fg_colombia_conat_generator_92k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92248.11; date_signed 2022-09-27.",
)

row_doc(
    "lincoln_colombia_generators_90k_2011",
    "energy", "power_plants_grid", "us",
    "Lincoln Contractors Supply — Colombia BRCNA portable generators",
    "Colombia",
    "8 Jun 2011: Department of State awards contract SCO15011M1088 to Lincoln Contractors Supply for CD Brigade portable generators for BRCNA (PoP Colombia); obligated USD 89,599.86. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "89599.86", "2011-06-08", "2011", "", "",
    "Portable generators for BRCNA, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_lincoln_colombia_generators_90k_2011",
    "CD BRIGADE / PORTABLE GENERATORS FOR BRCNA MAY 2011",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M1088_1900_-NONE-_-NONE-/",
    "Actor: Lincoln Contractors Supply, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1029",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15011M1088_1900_-NONE-_-NONE- (Lincoln Colombia generators). Signed 2011-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M1088_1900_-NONE-_-NONE-/.",
    "USASpending: Lincoln Colombia generators USD 0.090m. Supports lincoln_colombia_generators_90k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89599.86; date_signed 2011-06-08.",
)

row_doc(
    "misc_comayagua_generator_89k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras EIC Comayagua generator",
    "Honduras",
    "14 Jul 2017: Department of State awards contract SHO80017M0718 for INL CARSI generator for EIC Comayagua (PoP Honduras); obligated USD 89,220. CapEx face = award obligation. Recipient redacted.",
    "89220", "2017-07-14", "2017", "14.461", "-87.637",
    "Generator for EIC Comayagua, Honduras (USASpending description; Comayagua named).",
    "usaspending_misc_comayagua_generator_89k_2017",
    "IGF::OT::IGF INL CARSI GENERATOR FOR EIC COMAYAGUA 1930.0",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M0718_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1029",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80017M0718_1900_-NONE-_-NONE- (Comayagua generator). Signed 2017-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M0718_1900_-NONE-_-NONE-/.",
    "USASpending: Comayagua generator USD 0.089m. Supports misc_comayagua_generator_89k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89220; date_signed 2017-07-14.",
)

row_doc(
    "sumba_jamaica_guardrails_89k_2022",
    "infrastructure", "building_materials", "other",
    "Sumba King Pottinger — Jamaica MSGQ and utility building roof guardrails",
    "Jamaica",
    "30 Sep 2022: Department of State awards contract 19JM3722C0009 to Sumba King Pottinger for roof guardrails for MSGQ and utility building (PoP Jamaica); obligated USD 89,061.22. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "89061.22", "2022-09-30", "2022", "", "",
    "Roof guardrails for MSGQ and utility building, Jamaica (USASpending PoP Jamaica; site not named — lat/lon blank).",
    "usaspending_sumba_jamaica_guardrails_89k_2022",
    "FAC - ROOF GUARDRAILS FOR MSGQ & UTILITY BLDG",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3722C0009_1900_-NONE-_-NONE-/",
    "Actor: Sumba King Pottinger (Jamaica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1029",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3722C0009_1900_-NONE-_-NONE- (Sumba Jamaica guardrails). Signed 2022-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3722C0009_1900_-NONE-_-NONE-/.",
    "USASpending: Sumba Jamaica guardrails USD 0.089m. Supports sumba_jamaica_guardrails_89k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89061.22; date_signed 2022-09-30.",
)

# === Cycle 1030 ===
row_doc(
    "mh_cr_asphalt_89k_2019",
    "infrastructure", "bridges_roads", "other",
    "MH Electromecánica — Costa Rica CMR asphalt repair",
    "Costa Rica",
    "21 Aug 2019: Department of State awards contract 19CS8019C0006 to MH Electromecánica for CMR asphalt repair (PoP Costa Rica); obligated USD 88,729.45. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "88729.45", "2019-08-21", "2019", "", "",
    "CMR asphalt repair, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_mh_cr_asphalt_89k_2019",
    "CMR ASPHALT REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019C0006_1900_-NONE-_-NONE-/",
    "Actor: MH Electromecánica S.R.L. (Costa Rica) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1030",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8019C0006_1900_-NONE-_-NONE- (MH CR asphalt). Signed 2019-08-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019C0006_1900_-NONE-_-NONE-/.",
    "USASpending: MH CR asphalt USD 0.089m. Supports mh_cr_asphalt_89k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88729.45; date_signed 2019-08-21.",
)

row_doc(
    "atlas_haiti_semiramis_89k_2014",
    "infrastructure", "building_materials", "other",
    "Atlas Construction — Haiti Lycée Semiramis Télémaque renovation",
    "Haiti",
    "7 Jul 2014: USAID awards BPA call AID521BC1400016 to Atlas Construction for renovation of Lycée Semiramis Télémaque (PoP Haiti); obligated USD 88,539.14. CapEx face = award obligation. Exact coordinates not sourced — lat/lon blank.",
    "88539.14", "2014-07-07", "2014", "", "",
    "Renovation of Lycée Semiramis Télémaque, Haiti (USASpending description; school named; coordinates not sourced — lat/lon blank).",
    "usaspending_atlas_haiti_semiramis_89k_2014",
    "IGF::OT::IGF - THE PURPOSE OF THIS BPA CALL IS FOR THE RENOVATION OF LYCEE SEMIRAMIS TELEMAQUE UNDER THE BPA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1400016_7200_AID521E1200002_7200/",
    "Actor: Atlas Construction (Haiti) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1030",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521BC1400016_7200_AID521E1200002_7200 (Atlas Semiramis). Signed 2014-07-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1400016_7200_AID521E1200002_7200/.",
    "USASpending: Atlas Semiramis USD 0.089m. Supports atlas_haiti_semiramis_89k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88539.14; date_signed 2014-07-07.",
)

row_doc(
    "misc_barbados_chiller_coils_88k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Barbados chancery chiller coils upgrade",
    "Barbados",
    "14 Dec 2011: Department of State awards contract SBB21011M0646 for upgrade chancery chiller coils (PoP Barbados); obligated USD 88,259.90. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "88259.9", "2011-12-14", "2011", "", "",
    "Chancery chiller coils upgrade, Barbados (USASpending PoP Barbados; site not named — lat/lon blank).",
    "usaspending_misc_barbados_chiller_coils_88k_2011",
    "FM: UPGRADE CHANCERY CHILLER COILS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21011M0646_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1030",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21011M0646_1900_-NONE-_-NONE- (Barbados chiller coils). Signed 2011-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21011M0646_1900_-NONE-_-NONE-/.",
    "USASpending: Barbados chiller coils USD 0.088m. Supports misc_barbados_chiller_coils_88k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88259.9; date_signed 2011-12-14.",
)

row_doc(
    "store_q_warehouse_parking_88k_2026",
    "infrastructure", "bridges_roads", "other",
    "Store Q Panama — NEC warehouse parking lot",
    "Panama",
    "29 Sep 2026: Department of State awards contract 19PM0726P0640 to Store Q Panama for NEC warehouse parking lot (PoP Panama); obligated USD 88,107.28. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "88107.28", "2026-09-29", "2026", "", "",
    "NEC warehouse parking lot, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_store_q_warehouse_parking_88k_2026",
    "NEC - WAREHOUSE PARKING LOT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0726P0640_1900_-NONE-_-NONE-/",
    "Actor: Store Q Panama S.A. (Panama) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1030",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0726P0640_1900_-NONE-_-NONE- (Store Q warehouse parking). Signed 2026-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0726P0640_1900_-NONE-_-NONE-/.",
    "USASpending: Store Q warehouse parking USD 0.088m. Supports store_q_warehouse_parking_88k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88107.28; date_signed 2026-09-29.",
)

row_doc(
    "cummins_belize_generator_86k_2012",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Belize residential generator replacement",
    "Belize",
    "21 Dec 2012: Department of State awards contract SBH20013M0036 to Cummins Power Generation for FM generator-replacement residential generator (PoP Belize); obligated USD 85,934. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "85934", "2012-12-21", "2012", "", "",
    "Residential generator replacement, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_cummins_belize_generator_86k_2012",
    "FM- GENERATOR-REPLACEMENT RESIDENTIAL GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20013M0036_1900_-NONE-_-NONE-/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1030",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20013M0036_1900_-NONE-_-NONE- (Cummins Belize generator). Signed 2012-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20013M0036_1900_-NONE-_-NONE-/.",
    "USASpending: Cummins Belize generator USD 0.086m. Supports cummins_belize_generator_86k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85934; date_signed 2012-12-21.",
)

# === Cycle 1031 ===
row_doc(
    "misc_panama_bathrooms_90k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama CMR bathroom remodeling",
    "Panama",
    "29 Jul 2010: DoD awards contract SPM07010M0496 for replace floor tiles-remodeling bathrooms CMR (PoP Panama); obligated USD 89,900. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "89900", "2010-07-29", "2010", "", "",
    "CMR bathroom remodeling and floor tile replacement, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_misc_panama_bathrooms_90k_2010",
    "REPLACE FLOOR TILES-REMODELING BATHROOMS CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07010M0496_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1031",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07010M0496_1900_-NONE-_-NONE- (Panama CMR bathrooms). Signed 2010-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07010M0496_1900_-NONE-_-NONE-/.",
    "USASpending: Panama CMR bathrooms USD 0.090m. Supports misc_panama_bathrooms_90k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89900; date_signed 2010-07-29.",
)

row_doc(
    "urbanus_panama_asphalt_82k_2019",
    "infrastructure", "bridges_roads", "other",
    "Urbanus Group — Panama CMR asphalt driveway resurfacing",
    "Panama",
    "19 Aug 2019: Department of State awards contract 19PM0719P0894 to Urbanus Group for resurfacing asphalt driveway at CMR (PoP Panama); obligated USD 82,362.09. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "82362.09", "2019-08-19", "2019", "", "",
    "CMR asphalt driveway resurfacing, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_urbanus_panama_asphalt_82k_2019",
    "19PM0719P0894 RESURFACING ASPHALT DRIVEWAY AT CMR  7355 (19Q0041)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0894_1900_-NONE-_-NONE-/",
    "Actor: Urbanus Group Inc. (Panama) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1031",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0719P0894_1900_-NONE-_-NONE- (Urbanus Panama asphalt). Signed 2019-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0894_1900_-NONE-_-NONE-/.",
    "USASpending: Urbanus Panama asphalt USD 0.082m. Supports urbanus_panama_asphalt_82k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 82362.09; date_signed 2019-08-19.",
)

row_doc(
    "cummins_nicaragua_generators_78k_2012",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Nicaragua residential generators replacement",
    "Nicaragua",
    "26 Jan 2012: Department of State awards order SNU70012F0003 to Cummins Power Generation for residential generators replacement project (PoP Nicaragua); obligated USD 78,452.35. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "78452.35", "2012-01-26", "2012", "", "",
    "Residential generators replacement, Nicaragua (USASpending PoP Nicaragua; site not named — lat/lon blank).",
    "usaspending_cummins_nicaragua_generators_78k_2012",
    "RESIDENTIAL GENERATORS (REPLACEMENT PROJECT)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70012F0003_1900_GS07F9004D_4730/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx; Nicaragua under-covered.",
    "hunt_cycle1031",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70012F0003_1900_GS07F9004D_4730 (Cummins Nicaragua generators). Signed 2012-01-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70012F0003_1900_GS07F9004D_4730/.",
    "USASpending: Cummins Nicaragua generators USD 0.078m. Supports cummins_nicaragua_generators_78k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 78452.35; date_signed 2012-01-26.",
)

row_doc(
    "cummins_belize_mlo_generators_86k_2012",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Belize MLO generators",
    "Belize",
    "20 Sep 2012: Department of State awards contract SBH20012M0313 to Cummins Power Generation for MLO generators (PoP Belize); obligated USD 85,934. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "85934", "2012-09-20", "2012", "", "",
    "MLO generators, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_cummins_belize_mlo_generators_86k_2012",
    "MLO - GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20012M0313_1900_-NONE-_-NONE-/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1031",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20012M0313_1900_-NONE-_-NONE- (Cummins Belize MLO generators). Signed 2012-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20012M0313_1900_-NONE-_-NONE-/.",
    "USASpending: Cummins Belize MLO generators USD 0.086m. Supports cummins_belize_mlo_generators_86k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85934; date_signed 2012-09-20.",
)

row_doc(
    "machinery_bahamas_generator_92k_2018",
    "energy", "power_plants_grid", "other",
    "Machinery and Energy — Bahamas Tradewinds generator and tower lights",
    "Bahamas",
    "31 May 2018: DoD awards contract W912CL18P0808 to Machinery and Energy for Tradewinds 18 — 20 kW generator and 4 tower light sets (PoP Bahamas); obligated USD 92,450. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "92450", "2018-05-31", "2018", "", "",
    "20 kW generator and tower light sets, Bahamas (USASpending PoP Bahamas; site not named — lat/lon blank).",
    "usaspending_machinery_bahamas_generator_92k_2018",
    "TRADEWINDS 18 - 20 KW GENERATOR AND 4 TOWER LIGHT SETS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL18P0808_9700_-NONE-_-NONE-/",
    "Actor: Machinery and Energy Ltd. (Bahamas) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1031",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL18P0808_9700_-NONE-_-NONE- (Machinery Bahamas generator). Signed 2018-05-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL18P0808_9700_-NONE-_-NONE-/.",
    "USASpending: Machinery Bahamas generator USD 0.092m. Supports machinery_bahamas_generator_92k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92450; date_signed 2018-05-31.",
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
    print(f"cycles1029-1031 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
