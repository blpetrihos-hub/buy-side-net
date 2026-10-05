#!/usr/bin/env python3
"""Cycles 984–986: USASpending LatAm CapEx residual (~USD0.33–0.42m).

Seeds: 20261984–20261986. Thin top-up dry. Includes Nicaragua Jinotega clinic.
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


# === Cycle 984 ===
row_doc(
    "misc_tegucigalpa_elevator_415k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Tegucigalpa embassy elevator modernization",
    "Honduras",
    "29 Sep 2016: Department of State awards contract SAQMMA16M2836 for elevator repair and modernization at U.S. Embassy Tegucigalpa; obligated USD 415,073.80. CapEx face = award obligation. Recipient redacted.",
    "415073.80", "2016-09-29", "2016", "14.088", "-87.207",
    "Embassy elevator modernization, Tegucigalpa, Honduras (USASpending description).",
    "usaspending_misc_tegucigalpa_elevator_415k_2016",
    "ELEVATOR REPAIR AND MODERNIZATION AT U.S. EMBASSY TEGUCIGALPA, HONDURAS  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M2836_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle984",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M2836_1900_-NONE-_-NONE- (Tegucigalpa elevator). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M2836_1900_-NONE-_-NONE-/.",
    "USASpending: Tegucigalpa elevator USD 0.415m. Supports misc_tegucigalpa_elevator_415k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 415073.80; date_signed 2016-09-29.",
)

row_doc(
    "partenon_uruguay_training_399k_2017",
    "infrastructure", "building_materials", "other",
    "Partenon Contratistas — Uruguay training village construction",
    "Uruguay",
    "28 Sep 2017: U.S. Army Corps of Engineers awards contract W912CL17C0009 to Partenon Contratistas for construction of a training village (PoP Uruguay); obligated USD 399,301.68. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "399301.68", "2017-09-28", "2017", "", "",
    "Training village construction, Uruguay (USASpending PoP Uruguay; site not named — lat/lon blank).",
    "usaspending_partenon_uruguay_training_399k_2017",
    "IGF::OT::IGF::CONSTRUCT TRAINING VILLAGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0009_9700_-NONE-_-NONE-/",
    "Actor: Partenon Contratistas E.I.R.L. (Peru) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle984",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17C0009_9700_-NONE-_-NONE- (Partenon Uruguay training village). Signed 2017-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0009_9700_-NONE-_-NONE-/.",
    "USASpending: Partenon Uruguay training village USD 0.399m. Supports partenon_uruguay_training_399k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 399301.68; date_signed 2017-09-28.",
)

row_doc(
    "romero_alto_caballero_clinic_398k_2011",
    "infrastructure", "building_materials", "other",
    "Arq Rita C Romero — Alto Caballero / Nagabe medical clinic",
    "Panama",
    "23 Sep 2011: U.S. Army Corps of Engineers awards contract W912CL11C0037 to Arq Rita C Romero for HAP construction of a medical clinic at Alto Caballero, Nagabe, Panama; obligated USD 398,416.28. CapEx face = award obligation.",
    "398416.28", "2011-09-23", "2011", "7.760", "-80.270",
    "Medical clinic, Alto Caballero / Nagabe, Panama (USASpending description; approximate pin).",
    "usaspending_romero_alto_caballero_clinic_398k_2011",
    "THIS IS A HUMANITARIAN ASSISTANCE PROJECT FOR THE CONSTRUCTION OF A MEDICAL CLINIC ALTO CABALLERO, NAGABE, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0037_9700_-NONE-_-NONE-/",
    "Actor: Arq Rita C Romero B (Los Santos, Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle984",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0037_9700_-NONE-_-NONE- (Romero Alto Caballero clinic). Signed 2011-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0037_9700_-NONE-_-NONE-/.",
    "USASpending: Romero Alto Caballero clinic USD 0.398m. Supports romero_alto_caballero_clinic_398k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 398416.28; date_signed 2011-09-23.",
)

row_doc(
    "proksol_ancon_gpoi_396k_2011",
    "infrastructure", "building_materials", "other",
    "Proksol — Ancón GPOI building upgrades design/build",
    "Peru",
    "19 Sep 2011: U.S. Army Corps of Engineers awards task order 0007 under W9127809D0078 to Proksol for design/build GPOI building upgrades at Ancón, Peru; obligated USD 396,243.68. CapEx face = award obligation.",
    "396243.68", "2011-09-19", "2011", "-11.740", "-77.170",
    "GPOI building upgrades, Ancón, Peru (USASpending description).",
    "usaspending_proksol_ancon_gpoi_396k_2011",
    "TAS::21 2020::TAS D/B GPOI BUILDING UPGRADES ANCON, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127809D0078_9700/",
    "Actor: Proksol SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle984",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_W9127809D0078_9700 (Proksol Ancón GPOI). Signed 2011-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127809D0078_9700/.",
    "USASpending: Proksol Ancón GPOI USD 0.396m. Supports proksol_ancon_gpoi_396k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 396243.68; date_signed 2011-09-19.",
)

row_doc(
    "john_d_corozal_admin_393k_2022",
    "infrastructure", "building_materials", "other",
    "John D Engineering — Corozal admin building new construction",
    "Belize",
    "31 Mar 2022: U.S. Army Corps of Engineers awards contract W912QM22C0002 to John D Engineering for Corozal Belize admin building new construction; obligated USD 392,954.79. CapEx face = award obligation.",
    "392954.79", "2022-03-31", "2022", "18.390", "-88.390",
    "Admin building new construction, Corozal, Belize (USASpending description).",
    "usaspending_john_d_corozal_admin_393k_2022",
    "COROZAL BLZ. ADMIN BLDG NEW CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22C0002_9700_-NONE-_-NONE-/",
    "Actor: John D Engineering Ltd. (Ladyville, Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle984",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM22C0002_9700_-NONE-_-NONE- (John D Corozal admin). Signed 2022-03-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22C0002_9700_-NONE-_-NONE-/.",
    "USASpending: John D Corozal admin USD 0.393m. Supports john_d_corozal_admin_393k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 392954.79; date_signed 2022-03-31.",
)

# === Cycle 985 ===
row_doc(
    "seobra_lumbaqui_hanger_386k_2011",
    "infrastructure", "building_materials", "other",
    "Seobra — Lumbaquí vehicle hangar design/build",
    "Ecuador",
    "24 Sep 2011: U.S. Army Corps of Engineers awards task order 0004 under W9127809D0081 to Seobra for construction with incidental design of vehicle hangar in Lumbaquí, Ecuador; obligated USD 385,808.80. CapEx face = award obligation.",
    "385808.80", "2011-09-24", "2011", "0.050", "-77.330",
    "Vehicle hangar, Lumbaquí, Ecuador (USASpending description).",
    "usaspending_seobra_lumbaqui_hanger_386k_2011",
    "TAS::21 2020::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF VEHICLE HANGER LUMBAQUI, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127809D0081_9700/",
    "Actor: Seobra S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle985",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127809D0081_9700 (Seobra Lumbaquí hangar). Signed 2011-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127809D0081_9700/.",
    "USASpending: Seobra Lumbaquí hangar USD 0.386m. Supports seobra_lumbaqui_hanger_386k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 385808.80; date_signed 2011-09-24.",
)

row_doc(
    "eterna_jinotega_clinic_384k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — Jinotega HAP clinic design/build",
    "Nicaragua",
    "24 Aug 2010: U.S. Army Corps of Engineers awards task order 0010 under W9127809D0071 to Eterna for design/build Jinotega HAP clinic; obligated USD 383,895.28. CapEx face = award obligation.",
    "383895.28", "2010-08-24", "2010", "13.091", "-86.002",
    "HAP clinic, Jinotega, Nicaragua (USASpending description).",
    "usaspending_eterna_jinotega_clinic_384k_2010",
    "D/B JINOTEGA HAP CLINIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127809D0071_9700/",
    "Actor: Eterna (San Pedro Sula, Honduras) — other. Official USASpending Award API. Shuffle building_materials; Nicaragua under-covered cell.",
    "hunt_cycle985",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127809D0071_9700 (Eterna Jinotega clinic). Signed 2010-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127809D0071_9700/.",
    "USASpending: Eterna Jinotega clinic USD 0.384m. Supports eterna_jinotega_clinic_384k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 383895.28; date_signed 2010-08-24.",
)

row_doc(
    "ycf_haiti_firestations_377k_2012",
    "infrastructure", "building_materials", "us",
    "YCF Group — Delmas and Pétion-Ville fire stations",
    "Haiti",
    "14 Feb 2012: Department of Defense awards contract N6945012C0031 to YCF Group for construction of fire stations at Delmas and Pétion-Ville, Haiti; obligated USD 377,465.38. CapEx face = award obligation.",
    "377465.38", "2012-02-14", "2012", "18.540", "-72.300",
    "Fire stations, Delmas and Pétion-Ville, Haiti (USASpending description; Port-au-Prince metro pin).",
    "usaspending_ycf_haiti_firestations_377k_2012",
    "CONSTRUCTION OF FIRESTATIONS AT DELMAS AND PETIONVILLE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945012C0031_9700_-NONE-_-NONE-/",
    "Actor: YCF Group (Pinellas Park FL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx; Haiti under-covered.",
    "hunt_cycle985",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945012C0031_9700_-NONE-_-NONE- (YCF Haiti fire stations). Signed 2012-02-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945012C0031_9700_-NONE-_-NONE-/.",
    "USASpending: YCF Haiti fire stations USD 0.377m. Supports ycf_haiti_firestations_377k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 377465.38; date_signed 2012-02-14.",
)

row_doc(
    "misc_bucaramanga_siu_377k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bucaramanga CNP SIU construction",
    "Colombia",
    "14 Oct 2014: Department of State awards contract SCO15015C003 for INTER SIU construction for CNP in Bucaramanga; obligated USD 377,198.39. CapEx face = award obligation. Recipient redacted.",
    "377198.39", "2014-10-14", "2014", "7.125", "-73.119",
    "CNP SIU construction, Bucaramanga, Colombia (USASpending description).",
    "usaspending_misc_bucaramanga_siu_377k_2014",
    "INTER SIU CONSTRUCTION FOR CNP IN BUCARAMANGA  3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C003_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle985",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15015C003_1900_-NONE-_-NONE- (Bucaramanga SIU). Signed 2014-10-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C003_1900_-NONE-_-NONE-/.",
    "USASpending: Bucaramanga SIU USD 0.377m. Supports misc_bucaramanga_siu_377k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 377198.39; date_signed 2014-10-14.",
)

row_doc(
    "eterna_soto_cano_taxiway_a_375k_2010",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Soto Cano Taxiway A resurface design/build",
    "Honduras",
    "22 Sep 2010: U.S. Army Corps of Engineers awards task order 0012 under W9127809D0071 to Eterna for design/build resurface of Taxiway A at Soto Cano Air Base, Honduras; obligated USD 374,750.59. CapEx face = award obligation.",
    "374750.59", "2010-09-22", "2010", "14.382", "-87.621",
    "Taxiway A resurface, Soto Cano Air Base, Comayagua, Honduras (USASpending description).",
    "usaspending_eterna_soto_cano_taxiway_a_375k_2010",
    "D/B RESURFACE TAXIWAY A, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0071_9700/",
    "Actor: Eterna (San Pedro Sula, Honduras) — other. Official USASpending Award API. Shuffle bridges_roads/airside.",
    "hunt_cycle985",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0012_9700_W9127809D0071_9700 (Eterna Soto Cano Taxiway A). Signed 2010-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0071_9700/.",
    "USASpending: Eterna Soto Cano Taxiway A USD 0.375m. Supports eterna_soto_cano_taxiway_a_375k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 374750.59; date_signed 2010-09-22.",
)

# === Cycle 986 ===
row_doc(
    "milbau_uruguay_workshop_369k_2017",
    "infrastructure", "building_materials", "other",
    "Milbau — Uruguay small boat engine maintenance workshop renovation",
    "Uruguay",
    "23 Mar 2017: U.S. Army Corps of Engineers awards contract W912CL17C0004 to Milbau for small boat engine maintenance workshop renovation (PoP Uruguay); obligated USD 368,905. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "368905", "2017-03-23", "2017", "", "",
    "Small boat engine maintenance workshop renovation, Uruguay (USASpending PoP Uruguay; site not named — lat/lon blank).",
    "usaspending_milbau_uruguay_workshop_369k_2017",
    "IGF::OT::IGF SMALL BOAT ENGINE MAINTENANCE WORKSHOP RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0004_9700_-NONE-_-NONE-/",
    "Actor: Milbau S.A. (Solymar, Uruguay) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle986",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17C0004_9700_-NONE-_-NONE- (Milbau Uruguay workshop). Signed 2017-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17C0004_9700_-NONE-_-NONE-/.",
    "USASpending: Milbau Uruguay workshop USD 0.369m. Supports milbau_uruguay_workshop_369k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 368905; date_signed 2017-03-23.",
)

row_doc(
    "bendig_icd_warehouse_367k_2016",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica ICD warehouse improvement",
    "Costa Rica",
    "23 Sep 2016: Department of State awards contract SAQMMA16C0247 to Industrias Bendig for Costa Rica ICD warehouse improvement; obligated USD 367,199.30. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "367199.30", "2016-09-23", "2016", "", "",
    "ICD warehouse improvement, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_bendig_icd_warehouse_367k_2016",
    "COSTA RICA ICD WAREHOUSE IMPROVEMENT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0247_1900_-NONE-_-NONE-/",
    "Actor: Industrias Bendig SA (Desamparados, Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle986",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16C0247_1900_-NONE-_-NONE- (Bendig ICD warehouse). Signed 2016-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0247_1900_-NONE-_-NONE-/.",
    "USASpending: Bendig ICD warehouse USD 0.367m. Supports bendig_icd_warehouse_367k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 367199.30; date_signed 2016-09-23.",
)

row_doc(
    "recreativa_guatemala_cmr_roof_357k_2020",
    "infrastructure", "building_materials", "other",
    "Corporación Recreativa — Guatemala City CMR roof replacement",
    "Guatemala",
    "28 Sep 2020: Department of State awards contract 19GE5020C0039 to Corporación Recreativa for CMR roof replacement in Guatemala City; obligated USD 357,268.80. CapEx face = award obligation.",
    "357268.80", "2020-09-28", "2020", "14.635", "-90.507",
    "CMR roof replacement, Guatemala City (USASpending description).",
    "usaspending_recreativa_guatemala_cmr_roof_357k_2020",
    "CMR'S ROOF REPLACEMENT IN GUATEMALA CITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020C0039_1900_-NONE-_-NONE-/",
    "Actor: Corporación Recreativa SA (Guatemala City) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle986",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5020C0039_1900_-NONE-_-NONE- (Recreativa Guatemala CMR roof). Signed 2020-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020C0039_1900_-NONE-_-NONE-/.",
    "USASpending: Recreativa Guatemala CMR roof USD 0.357m. Supports recreativa_guatemala_cmr_roof_357k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 357268.80; date_signed 2020-09-28.",
)

row_doc(
    "jj_soto_cano_n61_dorms_356k_2012",
    "infrastructure", "building_materials", "us",
    "J & J Maintenance — Soto Cano N61 dorms renovation",
    "Honduras",
    "26 Sep 2012: U.S. Army Corps of Engineers awards task order 0003 under W9127811D0047 to J & J Maintenance for renovation of N61 dorms at Soto Cano; obligated USD 356,227.37. CapEx face = award obligation.",
    "356227.37", "2012-09-26", "2012", "14.382", "-87.621",
    "N61 dorms renovation, Soto Cano Air Base, Comayagua, Honduras (USASpending description).",
    "usaspending_jj_soto_cano_n61_dorms_356k_2012",
    "RENOVATION OF N61 DORMS AT SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0047_9700/",
    "Actor: J & J Maintenance Inc. (Austin TX, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle986",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127811D0047_9700 (J&J Soto Cano N61 dorms). Signed 2012-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0047_9700/.",
    "USASpending: J&J Soto Cano N61 dorms USD 0.356m. Supports jj_soto_cano_n61_dorms_356k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 356227.37; date_signed 2012-09-26.",
)

row_doc(
    "rogers_bocas_coastline_334k_2026",
    "resources", "water", "other",
    "Constructora Rogers — Bocas coastline stabilization (BCI)",
    "Panama",
    "22 Jun 2026: Smithsonian awards task order 33330226FF0010291 to Constructora Rogers for BCI stabilize eroded coastline construction (Project # DM-BM05-2026, PoP Panama); obligated USD 334,405. CapEx face = award obligation.",
    "334405", "2026-06-22", "2026", "9.340", "-82.250",
    "Coastline stabilization, Bocas del Toro / BCI, Panama (USASpending description; Bocas pin).",
    "usaspending_rogers_bocas_coastline_334k_2026",
    "BCI STABILIZE ERODED COASTLINE CONSTRUCTION - PROJECT # DM-BM05-2026",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330226FF0010291_3300_33330226DF0010098_3300/",
    "Actor: Constructora Rogers S.A. (CONROSA, Panama) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle986",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330226FF0010291_3300_33330226DF0010098_3300 (Rogers Bocas coastline). Signed 2026-06-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330226FF0010291_3300_33330226DF0010098_3300/.",
    "USASpending: Rogers Bocas coastline USD 0.334m. Supports rogers_bocas_coastline_334k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 334405; date_signed 2026-06-22.",
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
    print(f"cycles984-986 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
