#!/usr/bin/env python3
"""Cycles 1017–1019: USASpending LatAm CapEx residual (~USD0.08–0.11m).

Seeds: 20262017–20262019. Thin top-up dry.
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

# === Cycle 1017 ===
row_doc(
    "jj_soto_cano_generator_110k_2011",
    "energy", "power_plants_grid", "us",
    "J & J Maintenance — Soto Cano final backup generator main gate",
    "Honduras",
    "22 Sep 2011: DoD awards delivery order 0001 under W9127811D0047 to J & J Maintenance for construction of final backup generator main gate Soto Cano, Honduras; obligated USD 109,703.19. CapEx face = award obligation.",
    "109703.19", "2011-09-22", "2011", "14.382", "-87.621",
    "Final backup generator at main gate, Soto Cano Air Base, Honduras (USASpending description; Soto Cano named).",
    "usaspending_jj_soto_cano_generator_110k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF FINAL BACKUP GENERATOR MAIN GATE SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0047_9700/",
    "Actor: J & J Maintenance Inc. (Austin TX, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1017",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127811D0047_9700 (J&J Soto Cano generator). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0047_9700/.",
    "USASpending: J&J Soto Cano generator USD 0.110m. Supports jj_soto_cano_generator_110k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 109703.19; date_signed 2011-09-22.",
)

row_doc(
    "eeii_guaymaral_expansion_109k_2020",
    "infrastructure", "building_materials", "other",
    "EEII — Bogotá INL Guaymaral construction expansion phase 2",
    "Colombia",
    "2 Jan 2020: Department of State awards contract 19C01520C0001 to Estudios Edificaciones e Interventorias en Ingenieria EEII for Bogotá-INL construction-expansion-phase 2 at Guaymaral; obligated USD 109,242.35. CapEx face = award obligation.",
    "109242.35", "2020-01-02", "2020", "4.812", "-74.065",
    "INL construction expansion phase 2 at Guaymaral, Bogotá, Colombia (USASpending description; Guaymaral named).",
    "usaspending_eeii_guaymaral_expansion_109k_2020",
    "BOGOTA-INL CONSTRUCTION-EXPANSION-PHASE 2 AT GUAYMARAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520C0001_1900_-NONE-_-NONE-/",
    "Actor: EEII S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1017",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01520C0001_1900_-NONE-_-NONE- (EEII Guaymaral expansion). Signed 2020-01-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520C0001_1900_-NONE-_-NONE-/.",
    "USASpending: EEII Guaymaral expansion USD 0.109m. Supports eeii_guaymaral_expansion_109k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 109242.35; date_signed 2020-01-02.",
)

row_doc(
    "misc_jamaica_guard_booths_109k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica RSO guard booths construction",
    "Jamaica",
    "14 Jul 2021: Department of State awards contract 19JM3721C0001 for RSO construction of guard booths (PoP Jamaica); obligated USD 109,092.84. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "109092.84", "2021-07-14", "2021", "", "",
    "RSO guard booths construction, Jamaica (USASpending PoP Jamaica; site not named — lat/lon blank).",
    "usaspending_misc_jamaica_guard_booths_109k_2021",
    "RSO-CONSTRUCTION OF GUARD BOOTHS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3721C0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1017",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3721C0001_1900_-NONE-_-NONE- (Jamaica guard booths). Signed 2021-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3721C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Jamaica guard booths USD 0.109m. Supports misc_jamaica_guard_booths_109k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 109092.84; date_signed 2021-07-14.",
)

row_doc(
    "mode_powell_ae_100k_2024",
    "infrastructure", "engineering_epc", "other",
    "M.O.D.E. — Jamaica Powell Plaza apartment renovation A&E",
    "Jamaica",
    "16 May 2024: Department of State awards order 19JM3724F0039 to M.O.D.E. Ltd. for A&E services — renovation of apartments at Powell Plaza (PoP Jamaica); obligated USD 99,515.92. CapEx face = award obligation.",
    "99515.92", "2024-05-16", "2024", "18.015", "-76.797",
    "A&E apartment renovation at Powell Plaza, Kingston, Jamaica (USASpending description; Powell Plaza named).",
    "usaspending_mode_powell_ae_100k_2024",
    "FAC - A& E SERVICES - RENOVATION OF APTS AT POWELL PLAZA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3724F0039_1900_19JM3724D0001_1900/",
    "Actor: M.O.D.E. Ltd. (Kingston) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1017",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3724F0039_1900_19JM3724D0001_1900 (MODE Powell A&E). Signed 2024-05-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3724F0039_1900_19JM3724D0001_1900/.",
    "USASpending: MODE Powell A&E USD 0.100m. Supports mode_powell_ae_100k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 99515.92; date_signed 2024-05-16.",
)

row_doc(
    "misc_barbados_solar_91k_2018",
    "energy", "solar", "other",
    "Miscellaneous foreign awardees — Barbados solar energy project",
    "Barbados",
    "12 Jul 2018: Department of State awards contract 19BB2118C0004 for solar energy project (PoP Barbados); obligated USD 91,353.47. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "91353.47", "2018-07-12", "2018", "", "",
    "Solar energy project, Barbados (USASpending PoP Barbados; site not named — lat/lon blank).",
    "usaspending_misc_barbados_solar_91k_2018",
    "SOLAR ENERGY PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2118C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1017",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2118C0004_1900_-NONE-_-NONE- (Barbados solar). Signed 2018-07-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2118C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Barbados solar USD 0.091m. Supports misc_barbados_solar_91k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 91353.47; date_signed 2018-07-12.",
)

# === Cycle 1018 ===
row_doc(
    "beaver_peru_water_tower_93k_2013",
    "resources", "water", "other",
    "Beaver Logística — Peru elevated water storage tower",
    "Peru",
    "8 Apr 2013: DoD awards contract W912CL13C0008 to Beaver Logística & Construcción for construction of an elevated water storage tower (PoP Peru); obligated USD 92,666.20. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "92666.2", "2013-04-08", "2013", "", "",
    "Elevated water storage tower, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_beaver_peru_water_tower_93k_2013",
    "CONSTRUCTION OF AN ELEVATED WATER STORAGE TOWER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0008_9700_-NONE-_-NONE-/",
    "Actor: Beaver Logística & Construcción S.A.C. (Chiclayo) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1018",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL13C0008_9700_-NONE-_-NONE- (Beaver Peru water tower). Signed 2013-04-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0008_9700_-NONE-_-NONE-/.",
    "USASpending: Beaver Peru water tower USD 0.093m. Supports beaver_peru_water_tower_93k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92666.2; date_signed 2013-04-08.",
)

row_doc(
    "misc_uruguay_canalizations_100k_2022",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Uruguay CMR canalizations",
    "Uruguay",
    "9 Sep 2022: Department of State awards contract 19UY6022P0714 for construct canalizations at CMR (PoP Uruguay); obligated USD 100,339.44. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "100339.44", "2022-09-09", "2022", "", "",
    "CMR canalizations construction, Uruguay (USASpending PoP Uruguay; site not named — lat/lon blank).",
    "usaspending_misc_uruguay_canalizations_100k_2022",
    "FAC - CONSTRUCT CANALIZATIONS @ CMR - X2002",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6022P0714_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1018",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6022P0714_1900_-NONE-_-NONE- (Uruguay canalizations). Signed 2022-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6022P0714_1900_-NONE-_-NONE-/.",
    "USASpending: Uruguay canalizations USD 0.100m. Supports misc_uruguay_canalizations_100k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 100339.44; date_signed 2022-09-09.",
)

row_doc(
    "carranza_corn_island_pier_94k_2011",
    "infrastructure", "bridges_roads", "other",
    "Carlos Carranza — Nicaragua Corn Island pier repair",
    "Nicaragua",
    "22 Mar 2011: DoD awards contract W9127811P0142 to Carlos Carranza for pier repair Corn Island (PoP Nicaragua); obligated USD 94,029. CapEx face = award obligation.",
    "94029", "2011-03-22", "2011", "12.171", "-83.061",
    "Pier repair, Corn Island, Nicaragua (USASpending description; Corn Island named).",
    "usaspending_carranza_corn_island_pier_94k_2011",
    "TAS::21 2020::TAS PIER REPAIR CORN ISLAND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0142_9700_-NONE-_-NONE-/",
    "Actor: Carlos Carranza (Tegucigalpa) — other. Official USASpending Award API. Shuffle bridges_roads; Nicaragua under-covered.",
    "hunt_cycle1018",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0142_9700_-NONE-_-NONE- (Carranza Corn Island pier). Signed 2011-03-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0142_9700_-NONE-_-NONE-/.",
    "USASpending: Carranza Corn Island pier USD 0.094m. Supports carranza_corn_island_pier_94k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94029; date_signed 2011-03-22.",
)

row_doc(
    "multistack_salvador_chiller_107k_2010",
    "energy", "power_plants_grid", "us",
    "Multistack — El Salvador CMR chiller",
    "El Salvador",
    "15 Jun 2010: Department of State awards contract SES60010M0578 to Multistack for CMR chiller (PoP El Salvador); obligated USD 106,553. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "106553", "2010-06-15", "2010", "", "",
    "CMR chiller, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_multistack_salvador_chiller_107k_2010",
    "CMR CHILLER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60010M0578_1900_-NONE-_-NONE-/",
    "Actor: Multistack LLC (Sparta WI, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1018",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60010M0578_1900_-NONE-_-NONE- (Multistack El Salvador chiller). Signed 2010-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60010M0578_1900_-NONE-_-NONE-/.",
    "USASpending: Multistack El Salvador chiller USD 0.107m. Supports multistack_salvador_chiller_107k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 106553; date_signed 2010-06-15.",
)

row_doc(
    "tecniservicios_cr_inl_annex_108k_2025",
    "infrastructure", "building_materials", "other",
    "Tecniservicios FBV — Costa Rica INL annex #2 construction",
    "Costa Rica",
    "2 Jun 2025: Department of State awards contract 19CS8025P0612 to Tecniservicios FBV for pending construction works for INL annex #2 (PoP Costa Rica); obligated USD 108,223.63. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "108223.63", "2025-06-02", "2025", "", "",
    "INL annex #2 construction works, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_tecniservicios_cr_inl_annex_108k_2025",
    "INL 1930.0 PENDING CONSTRUCTION WORKS FOR INL ANNEX #2",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8025P0612_1900_-NONE-_-NONE-/",
    "Actor: Tecniservicios FBV S.R.L. (San José) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1018",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8025P0612_1900_-NONE-_-NONE- (Tecniservicios CR INL annex). Signed 2025-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8025P0612_1900_-NONE-_-NONE-/.",
    "USASpending: Tecniservicios CR INL annex USD 0.108m. Supports tecniservicios_cr_inl_annex_108k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 108223.63; date_signed 2025-06-02.",
)

# === Cycle 1019 ===
row_doc(
    "eaton_suriname_electrical_95k_2019",
    "energy", "power_plants_grid", "us",
    "Eaton — Suriname NEC critical electrical equipment repair",
    "Suriname",
    "19 Aug 2019: Department of State awards contract 19NS5019P0494 to Eaton for FAC critical safety repair of electrical equipment (PoP Suriname); obligated USD 94,931. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "94931", "2019-08-19", "2019", "", "",
    "Critical safety repair of electrical equipment at FAC/NEC, Suriname (USASpending PoP Suriname; site not named — lat/lon blank).",
    "usaspending_eaton_suriname_electrical_95k_2019",
    "FAC CRITICAL SAFETY REPAIR OF ELECTRICAL EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5019P0494_1900_-NONE-_-NONE-/",
    "Actor: Eaton Corporation (Hanover MD, U.S.-incorporated) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1019",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NS5019P0494_1900_-NONE-_-NONE- (Eaton Suriname electrical). Signed 2019-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5019P0494_1900_-NONE-_-NONE-/.",
    "USASpending: Eaton Suriname electrical USD 0.095m. Supports eaton_suriname_electrical_95k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94931; date_signed 2019-08-19.",
)

row_doc(
    "relyant_guapi_hospital_87k_2023",
    "infrastructure", "building_materials", "us",
    "Relyant Global — Colombia Guapi HAP hospital refurbishment",
    "Colombia",
    "30 Sep 2023: DoD awards order W9127823F0499 to Relyant Global for design and construction of HAP #67203 hospital refurbishment in Guapi, Colombia; obligated USD 86,836.08. CapEx face = award obligation.",
    "86836.08", "2023-09-30", "2023", "2.570", "-77.898",
    "HAP #67203 hospital refurbishment, Guapi, Colombia (USASpending description; Guapi named).",
    "usaspending_relyant_guapi_hospital_87k_2023",
    "DESIGN AND CONSTRUCTION OF HAP #67203 HOSPITAL REFURBISHMENT IN GUAPI, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0499_9700_W9127823D0063_9700/",
    "Actor: Relyant Global LLC (Maryville TN, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1019",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0499_9700_W9127823D0063_9700 (Relyant Guapi hospital). Signed 2023-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0499_9700_W9127823D0063_9700/.",
    "USASpending: Relyant Guapi hospital USD 0.087m. Supports relyant_guapi_hospital_87k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 86836.08; date_signed 2023-09-30.",
)

row_doc(
    "maheias_ladyville_clinic_96k_2017",
    "infrastructure", "building_materials", "other",
    "Maheias United Concrete — Belize Ladyville medical clinic",
    "Belize",
    "28 Mar 2017: DoD awards contract W912CL17P0728 to Maheias United Concrete & Supplies for BTH Belize 17 block — Ladyville medical clinic; obligated USD 95,772.54. CapEx face = award obligation.",
    "95772.54", "2017-03-28", "2017", "17.552", "-88.295",
    "Medical clinic block, Ladyville, Belize (USASpending description; Ladyville named).",
    "usaspending_maheias_ladyville_clinic_96k_2017",
    "IGF::OT::IGF/G3/BTH BELIZE 17/BLOCK - LADYVILLE MEDICAL CLINIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17P0728_9700_-NONE-_-NONE-/",
    "Actor: Maheias United Concrete & Supplies Ltd (Belize City) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1019",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17P0728_9700_-NONE-_-NONE- (Maheias Ladyville clinic). Signed 2017-03-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17P0728_9700_-NONE-_-NONE-/.",
    "USASpending: Maheias Ladyville clinic USD 0.096m. Supports maheias_ladyville_clinic_96k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 95772.54; date_signed 2017-03-28.",
)

row_doc(
    "misc_dr_k9_range_98k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic K9 shooting range",
    "Dominican Republic",
    "22 Sep 2022: Department of State awards contract 19DR8622C0035 for construction of K9 shooting range (PoP Dominican Republic); obligated USD 97,758.72. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "97758.72", "2022-09-22", "2022", "", "",
    "K9 shooting range construction, Dominican Republic (USASpending PoP Dominican Republic; site not named — lat/lon blank).",
    "usaspending_misc_dr_k9_range_98k_2022",
    "CONSTRUCTION OF K9 SHOOTING RANGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0035_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1019",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622C0035_1900_-NONE-_-NONE- (DR K9 range). Signed 2022-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0035_1900_-NONE-_-NONE-/.",
    "USASpending: DR K9 range USD 0.098m. Supports misc_dr_k9_range_98k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 97758.72; date_signed 2022-09-22.",
)

row_doc(
    "carranza_hap_school_100k_2011",
    "infrastructure", "building_materials", "other",
    "Carlos Carranza — Honduras HAP school nutrition center Tansin",
    "Honduras",
    "22 Sep 2011: DoD awards contract W9127811P0333 to Carlos Carranza for construction with incidental design HAP school nutrition center Tansin, Honduras; obligated USD 100,467.49. CapEx face = award obligation.",
    "100467.49", "2011-09-22", "2011", "", "",
    "HAP school nutrition center, Tansin, Honduras (USASpending description; Tansin named but coordinates not sourced — lat/lon blank).",
    "usaspending_carranza_hap_school_100k_2011",
    "TAS::97 0819::TAS CONSTRUCTION WITH INCIDENTAL DESIGN HAP SCHOOL NUTRITION CENTER TANSIN, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0333_9700_-NONE-_-NONE-/",
    "Actor: Carlos Carranza (Tegucigalpa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1019",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0333_9700_-NONE-_-NONE- (Carranza HAP school). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0333_9700_-NONE-_-NONE-/.",
    "USASpending: Carranza HAP school USD 0.100m. Supports carranza_hap_school_100k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 100467.49; date_signed 2011-09-22.",
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
    print(f"cycles1017-1019 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
