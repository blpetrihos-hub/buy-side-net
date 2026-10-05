#!/usr/bin/env python3
"""Cycles 1032–1034: USASpending LatAm CapEx residual (~USD0.06–0.08m).

Seeds: 20262032–20262034. Thin top-up dry.
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

# === Cycle 1032 ===
row_doc(
    "akj_mexico_roof_80k_2026",
    "infrastructure", "building_materials", "other",
    "Servicios AKJ — Mexico roof coat",
    "Mexico",
    "21 Sep 2026: Department of State awards contract 19MX5326C0035 to Servicios AKJ for roof coat (PoP Mexico); obligated USD 79,992.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "79992.44", "2026-09-21", "2026", "", "",
    "Roof coat, Mexico (USASpending PoP Mexico; site not named — lat/lon blank).",
    "usaspending_akj_mexico_roof_80k_2026",
    "ROOF COAT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5326C0035_1900_-NONE-_-NONE-/",
    "Actor: Servicios AKJ S.A. de C.V. (Mexico) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1032",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5326C0035_1900_-NONE-_-NONE- (AKJ Mexico roof). Signed 2026-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5326C0035_1900_-NONE-_-NONE-/.",
    "USASpending: AKJ Mexico roof USD 0.080m. Supports akj_mexico_roof_80k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79992.44; date_signed 2026-09-21.",
)

row_doc(
    "acct_peru_warehouse_80k_2010",
    "infrastructure", "building_materials", "other",
    "A.C.C.T. — Peru warehouse upgrades",
    "Peru",
    "30 Sep 2010: DoD awards contract W9127810P0372 to A.C.C.T. for warehouse upgrades (PoP Peru); obligated USD 79,912.60. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "79912.6", "2010-09-30", "2010", "", "",
    "Warehouse upgrades, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_acct_peru_warehouse_80k_2010",
    "WAREHOUSE UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0372_9700_-NONE-_-NONE-/",
    "Actor: A.C.C.T. S.A.C. (Peru) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1032",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0372_9700_-NONE-_-NONE- (ACCT Peru warehouse). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0372_9700_-NONE-_-NONE-/.",
    "USASpending: ACCT Peru warehouse USD 0.080m. Supports acct_peru_warehouse_80k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79912.6; date_signed 2010-09-30.",
)

row_doc(
    "constecoin_ecuador_generator_platforms_80k_2025",
    "energy", "power_plants_grid", "other",
    "Constecoin — Ecuador generator platforms construction",
    "Ecuador",
    "22 May 2025: Department of State awards contract 19EC3025P0426 to Constecoin for construction of generator platforms (PoP Ecuador); obligated USD 79,676.57. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "79676.57", "2025-05-22", "2025", "", "",
    "Generator platforms construction, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_constecoin_ecuador_generator_platforms_80k_2025",
    "CONSTRUCTION OF GENERATOR PLATFORMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3025P0426_1900_-NONE-_-NONE-/",
    "Actor: Constecoin Cía. Ltda. (Ecuador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1032",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3025P0426_1900_-NONE-_-NONE- (Constecoin generator platforms). Signed 2025-05-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3025P0426_1900_-NONE-_-NONE-/.",
    "USASpending: Constecoin generator platforms USD 0.080m. Supports constecoin_ecuador_generator_platforms_80k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79676.57; date_signed 2025-05-22.",
)

row_doc(
    "siegel_jamaica_roof_ae_79k_2020",
    "infrastructure", "engineering_epc", "us",
    "Robert Siegel — Jamaica chancery compound roof safety handrail A&E",
    "Jamaica",
    "8 Jan 2020: Department of State awards order 19AQMM20F0433 to Robert Siegel for Kingston A&E chancery compound roof safety handrail assessment and design; obligated USD 79,346.50. CapEx face = award obligation.",
    "79346.5", "2020-01-08", "2020", "17.977", "-76.770",
    "Chancery compound roof safety handrail A&E, Kingston, Jamaica (USASpending description; Kingston named).",
    "usaspending_siegel_jamaica_roof_ae_79k_2020",
    "KINGSTON, JAMAICA A&E CHANCERY COMPOUND ROOF SAFETY HANDRAIL ASSESSMENT&DESIGN SERVICES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0433_1900_19AQMM19D0046_1900/",
    "Actor: Robert Siegel (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1032",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F0433_1900_19AQMM19D0046_1900 (Siegel Jamaica roof A&E). Signed 2020-01-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0433_1900_19AQMM19D0046_1900/.",
    "USASpending: Siegel Jamaica roof A&E USD 0.079m. Supports siegel_jamaica_roof_ae_79k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79346.5; date_signed 2020-01-08.",
)

row_doc(
    "dip_colombia_hsi_renovation_79k_2026",
    "infrastructure", "building_materials", "other",
    "Desarrollo Integral Proyectos — Colombia HSI office renovation",
    "Colombia",
    "16 Sep 2026: Department of State awards contract 19C02026C0006 to Desarrollo Integral Proyectos for HSI office renovation project (PoP Colombia); obligated USD 79,370.79. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "79370.79", "2026-09-16", "2026", "", "",
    "HSI office renovation, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_dip_colombia_hsi_renovation_79k_2026",
    "PR16278369 CONTRACT_HSI OFFICE RENOVATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0006_1900_-NONE-_-NONE-/",
    "Actor: Desarrollo Integral Proyectos (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1032",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02026C0006_1900_-NONE-_-NONE- (DIP HSI renovation). Signed 2026-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0006_1900_-NONE-_-NONE-/.",
    "USASpending: DIP HSI renovation USD 0.079m. Supports dip_colombia_hsi_renovation_79k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79370.79; date_signed 2026-09-16.",
)

# === Cycle 1033 ===
row_doc(
    "misc_mexico_cmr_renovation_79k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico CMR renovation",
    "Mexico",
    "24 Feb 2015: Department of State awards contract SMX53015C0002 for Mexico CMR renovation project (PoP Mexico); obligated USD 79,308.62. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "79308.62", "2015-02-24", "2015", "", "",
    "CMR renovation project, Mexico (USASpending PoP Mexico; site not named — lat/lon blank).",
    "usaspending_misc_mexico_cmr_renovation_79k_2015",
    "IGF::OT::IGF MEX CMR RENOVATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015C0002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1033",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015C0002_1900_-NONE-_-NONE- (Mexico CMR renovation). Signed 2015-02-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico CMR renovation USD 0.079m. Supports misc_mexico_cmr_renovation_79k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79308.62; date_signed 2015-02-24.",
)

row_doc(
    "chang_nejapa_fence_79k_2011",
    "infrastructure", "building_materials", "other",
    "Edwing Alberto Chang — El Salvador Nejapa HAP perimeter fence",
    "El Salvador",
    "27 Sep 2011: DoD awards contract W9127811P0336 to Edwing Alberto Chang for construction with incidental design of HAP 10985 perimeter fence, Nejapa; obligated USD 79,164.11. CapEx face = award obligation.",
    "79164.11", "2011-09-27", "2011", "13.813", "-89.230",
    "HAP perimeter fence, Nejapa, El Salvador (USASpending description; Nejapa named).",
    "usaspending_chang_nejapa_fence_79k_2011",
    "TAS::97 0819::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF HAP 10985 PERIMETER FENCE, NEJAPA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0336_9700_-NONE-_-NONE-/",
    "Actor: Edwing Alberto Chang (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1033",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0336_9700_-NONE-_-NONE- (Chang Nejapa fence). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0336_9700_-NONE-_-NONE-/.",
    "USASpending: Chang Nejapa fence USD 0.079m. Supports chang_nejapa_fence_79k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79164.11; date_signed 2011-09-27.",
)

row_doc(
    "misc_juarez_consulate_renovation_79k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juárez consulate renovations",
    "Mexico",
    "31 Oct 2016: Department of State awards contract SMX11517M0020 for MSG detachments CDJ MSG OBO consulate renovations (PoP Mexico); obligated USD 79,112. CapEx face = award obligation. Recipient redacted.",
    "79112", "2016-10-31", "2016", "31.690", "-106.425",
    "Consulate renovations, Ciudad Juárez, Mexico (USASpending description CDJ; Ciudad Juárez named).",
    "usaspending_misc_juarez_consulate_renovation_79k_2016",
    "MSG DETACHMENTS CDJ-MSG OBO  CONSULATE RENOVATIONS P100",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11517M0020_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1033",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11517M0020_1900_-NONE-_-NONE- (Juárez consulate renovation). Signed 2016-10-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11517M0020_1900_-NONE-_-NONE-/.",
    "USASpending: Juárez consulate renovation USD 0.079m. Supports misc_juarez_consulate_renovation_79k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79112; date_signed 2016-10-31.",
)

row_doc(
    "abb_ecuador_switchgear_77k_2023",
    "energy", "power_plants_grid", "us",
    "ABB — Ecuador compound electrical switchgear",
    "Ecuador",
    "29 Sep 2023: Department of State awards contract 19EC7523P1678 to ABB for electrical switchgear tier service at compound (PoP Ecuador); obligated USD 77,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "77000", "2023-09-29", "2023", "", "",
    "Compound electrical switchgear, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_abb_ecuador_switchgear_77k_2023",
    "PR11930012-7901RSTR-CMPD-FWP282-ELECTRICALSWITCHGEARTIERSRVC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P1678_1900_-NONE-_-NONE-/",
    "Actor: ABB Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1033",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P1678_1900_-NONE-_-NONE- (ABB Ecuador switchgear). Signed 2023-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P1678_1900_-NONE-_-NONE-/.",
    "USASpending: ABB Ecuador switchgear USD 0.077m. Supports abb_ecuador_switchgear_77k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 77000; date_signed 2023-09-29.",
)

row_doc(
    "store_q_visitor_parking_79k_2020",
    "infrastructure", "bridges_roads", "other",
    "Store Q Panama — CMR visitor parking resurfacing",
    "Panama",
    "19 Feb 2020: Department of State awards contract 19PM0720P0254 to Store Q Panama for CMR resurfacing of visitor parking (PoP Panama); obligated USD 78,630. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "78630", "2020-02-19", "2020", "", "",
    "CMR visitor parking resurfacing, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_store_q_visitor_parking_79k_2020",
    "19PM0720P0254 (19Q0052) CMR RESURFACING OF VISITOR PARK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0254_1900_-NONE-_-NONE-/",
    "Actor: Store Q Panama S.A. (Panama) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1033",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0720P0254_1900_-NONE-_-NONE- (Store Q visitor parking). Signed 2020-02-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0254_1900_-NONE-_-NONE-/.",
    "USASpending: Store Q visitor parking USD 0.079m. Supports store_q_visitor_parking_79k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 78630; date_signed 2020-02-19.",
)

# === Cycle 1034 ===
row_doc(
    "romero_bejuco_restrooms_78k_2011",
    "infrastructure", "building_materials", "other",
    "Arq. Rita C. Romero — Panama Bejuco-Chame school restroom construction",
    "Panama",
    "24 Jun 2011: DoD awards contract W912CL11C0024 to Arq Rita C Romero B for HAP #7568 construction of restroom facilities at Berta Elida Fernández Elementary School grounds in Bejuco-Chame; obligated USD 78,365.94. CapEx face = award obligation.",
    "78365.94", "2011-06-24", "2011", "8.607", "-79.883",
    "School restroom facilities, Bejuco-Chame, Panama (USASpending description; Bejuco-Chame named).",
    "usaspending_romero_bejuco_restrooms_78k_2011",
    "HUMANITARIAN PROJECT HAP #7568 - CONSTRUCTION OF RESTROOM FACILITIES IN THE BERTA ELIDA FERNANDEZ ELEMENTARY SCHOOL GROUNDS IN BEJUCO-CHAME PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0024_9700_-NONE-_-NONE-/",
    "Actor: Arq. Rita C. Romero B (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1034",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0024_9700_-NONE-_-NONE- (Romero Bejuco restrooms). Signed 2011-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0024_9700_-NONE-_-NONE-/.",
    "USASpending: Romero Bejuco restrooms USD 0.078m. Supports romero_bejuco_restrooms_78k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 78365.94; date_signed 2011-06-24.",
)

row_doc(
    "treyco_colombia_mezzanine_78k_2019",
    "infrastructure", "building_materials", "other",
    "Treyco — Colombia GSO off-site warehouse mezzanine",
    "Colombia",
    "18 Sep 2019: Department of State awards contract 19C02019P1436 to Treyco for mezzanine for the GSO off-site warehouse (PoP Colombia); obligated USD 77,617.08. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "77617.08", "2019-09-18", "2019", "", "",
    "Mezzanine for GSO off-site warehouse, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_treyco_colombia_mezzanine_78k_2019",
    "MEZZANINE FOR THE GSO OFF-SITE WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02019P1436_1900_-NONE-_-NONE-/",
    "Actor: Treyco S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1034",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02019P1436_1900_-NONE-_-NONE- (Treyco mezzanine). Signed 2019-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02019P1436_1900_-NONE-_-NONE-/.",
    "USASpending: Treyco mezzanine USD 0.078m. Supports treyco_colombia_mezzanine_78k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 77617.08; date_signed 2019-09-18.",
)

row_doc(
    "seal_haiti_roof_ae_73k_2023",
    "infrastructure", "engineering_epc", "us",
    "Seal Engineering — Haiti Port-au-Prince CAS housing roof A&E",
    "Haiti",
    "13 Sep 2023: Department of State awards order 19AQMM23F2827 to Seal Engineering for Port-au-Prince A&E CAS housing roof design services; obligated USD 72,972.48. CapEx face = award obligation.",
    "72972.48", "2023-09-13", "2023", "18.540", "-72.339",
    "CAS housing roof A&E design, Port-au-Prince, Haiti (USASpending description; Port-au-Prince named).",
    "usaspending_seal_haiti_roof_ae_73k_2023",
    "PORT-AU-PRINCE, HAITI A&E CAS HOUSING ROOF DESIGN SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2827_1900_19AQMM19D0048_1900/",
    "Actor: Seal Engineering, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1034",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F2827_1900_19AQMM19D0048_1900 (Seal Haiti roof A&E). Signed 2023-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2827_1900_19AQMM19D0048_1900/.",
    "USASpending: Seal Haiti roof A&E USD 0.073m. Supports seal_haiti_roof_ae_73k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 72972.48; date_signed 2023-09-13.",
)

row_doc(
    "waite_peru_roof_pavers_70k_2014",
    "infrastructure", "building_materials", "us",
    "R.M. Waite — Peru chancery roof walk pavers",
    "Peru",
    "28 Mar 2014: DoD awards contract SPE50014M0741 to R.M. Waite for roof walk pavers for chancery roof (PoP Peru); obligated USD 70,475. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "70475", "2014-03-28", "2014", "", "",
    "Chancery roof walk pavers, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_waite_peru_roof_pavers_70k_2014",
    "ROOF WALK PAVERS FOR CHANCERY ROOF IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0741_1900_-NONE-_-NONE-/",
    "Actor: R.M. Waite Co., LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1034",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014M0741_1900_-NONE-_-NONE- (Waite Peru roof pavers). Signed 2014-03-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0741_1900_-NONE-_-NONE-/.",
    "USASpending: Waite Peru roof pavers USD 0.070m. Supports waite_peru_roof_pavers_70k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70475; date_signed 2014-03-28.",
)

row_doc(
    "eaton_belize_electrical_61k_2019",
    "energy", "power_plants_grid", "us",
    "Eaton — Belize electrical upgrades",
    "Belize",
    "12 Sep 2019: Department of State awards contract 19BH2019P0316 to Eaton for electrical upgrades (PoP Belize); obligated USD 60,771.03. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "60771.03", "2019-09-12", "2019", "", "",
    "Electrical upgrades, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_eaton_belize_electrical_61k_2019",
    "ELECTRICAL UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2019P0316_1900_-NONE-_-NONE-/",
    "Actor: Eaton Corporation (U.S.-incorporated) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1034",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BH2019P0316_1900_-NONE-_-NONE- (Eaton Belize electrical). Signed 2019-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2019P0316_1900_-NONE-_-NONE-/.",
    "USASpending: Eaton Belize electrical USD 0.061m. Supports eaton_belize_electrical_61k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60771.03; date_signed 2019-09-12.",
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
    print(f"cycles1032-1034 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
