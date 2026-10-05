#!/usr/bin/env python3
"""Cycles 981–983: USASpending LatAm CapEx residual (~USD0.40–0.44m).

Seeds: 20261981–20261983. Thin top-up dry.
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


# === Cycle 981 ===
row_doc(
    "bendig_oij_sanjose_438k_2018",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — OIJ San José building renovation/extension",
    "Costa Rica",
    "21 Sep 2018: Department of State awards contract 19AQMM18C0200 to Industrias Bendig for renovation (including remodeling and extending) of an existing building at the Organization of Judicial Investigation (OIJ) in San José, Costa Rica; obligated USD 438,029.16. CapEx face = award obligation.",
    "438029.16", "2018-09-21", "2018", "9.928", "-84.091",
    "OIJ building renovation/extension, San José, Costa Rica (USASpending description).",
    "usaspending_bendig_oij_sanjose_438k_2018",
    "RENOVATION (INCLUDING REMODELING AND EXTENDING) OF AN EXISTING BUILDING AT THE ORGANIZATION OF THE JUDICIAL INVESTIGATION OF COSTA RICAN (OIJ) IN SAN JOSE, COSTA RICA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0200_1900_-NONE-_-NONE-/",
    "Actor: Industrias Bendig SA (Desamparados, Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle981",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0200_1900_-NONE-_-NONE- (Bendig OIJ San José). Signed 2018-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0200_1900_-NONE-_-NONE-/.",
    "USASpending: Bendig OIJ San José USD 0.438m. Supports bendig_oij_sanjose_438k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 438029.16; date_signed 2018-09-21.",
)

row_doc(
    "misc_el_bambu_clinic_436k_2008",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Bambú clinic construction",
    "Costa Rica",
    "7 Aug 2008: U.S. Army Corps of Engineers awards contract W912CL08C0008 for construction of new clinic at El Bambú (PoP Costa Rica); obligated USD 435,920.51. CapEx face = award obligation. Recipient redacted.",
    "435920.51", "2008-08-07", "2008", "10.470", "-84.010",
    "New clinic at El Bambú, Costa Rica (USASpending description; approximate community pin).",
    "usaspending_misc_el_bambu_clinic_436k_2008",
    "CONSTRUCTION OF NEW CLINIC AT EL BAMBU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL08C0008_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle981",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL08C0008_9700_-NONE-_-NONE- (El Bambú clinic). Signed 2008-08-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL08C0008_9700_-NONE-_-NONE-/.",
    "USASpending: El Bambú clinic USD 0.436m. Supports misc_el_bambu_clinic_436k_2008.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 435920.51; date_signed 2008-08-07.",
)

row_doc(
    "ect_hap7594_warehouse_cr_436k_2010",
    "infrastructure", "building_materials", "other",
    "ECT — HAP 7594 disaster relief warehouse Costa Rica",
    "Costa Rica",
    "30 Sep 2010: U.S. Army Corps of Engineers awards task order 0023 under W9127809D0071 to Empresa de Construcción y Transporte for design/build HAP 7594 disaster relief warehouse in Costa Rica; obligated USD 435,762.50. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "435762.50", "2010-09-30", "2010", "", "",
    "HAP 7594 disaster relief warehouse, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_ect_hap7594_warehouse_cr_436k_2010",
    "D/B HAP 7594 DISASTER RELIEF WAREHOUSE, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0023_9700_W9127809D0071_9700/",
    "Actor: Empresa de Construcción y Transporte (San Pedro Sula, Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle981",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0023_9700_W9127809D0071_9700 (ECT HAP 7594 warehouse). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0023_9700_W9127809D0071_9700/.",
    "USASpending: ECT HAP 7594 warehouse USD 0.436m. Supports ect_hap7594_warehouse_cr_436k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 435762.50; date_signed 2010-09-30.",
)

row_doc(
    "equipos_pavana_432k_2018",
    "infrastructure", "building_materials", "other",
    "Equipos de Construcción — Pavana facilities construction",
    "Honduras",
    "28 Sep 2018: Department of State awards contract 19AQMM18C0222 to Equipos de Construcción for facilities construction in Pavana, Honduras; obligated USD 432,323.83. CapEx face = award obligation.",
    "432323.83", "2018-09-28", "2018", "13.410", "-87.330",
    "Facilities construction, Pavana, Honduras (USASpending description).",
    "usaspending_equipos_pavana_432k_2018",
    "FACILITIES CONSTRUCTION, PAVANA, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0222_1900_-NONE-_-NONE-/",
    "Actor: Equipos de Construcción S.A. de C.V. (Tegucigalpa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle981",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0222_1900_-NONE-_-NONE- (Equipos Pavana). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0222_1900_-NONE-_-NONE-/.",
    "USASpending: Equipos Pavana USD 0.432m. Supports equipos_pavana_432k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 432323.83; date_signed 2018-09-28.",
)

row_doc(
    "misc_villa_garzon_hydrosan_429k_2008",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Villa Garzón CNP hydro-sanitary system",
    "Colombia",
    "7 Feb 2008: Department of State awards contract SWHARC08C0012 for construction of hydro-sanitary system at Colombia National Police station in Villa Garzón, Colombia; obligated USD 428,931.13. CapEx face = award obligation. Recipient redacted.",
    "428931.13", "2008-02-07", "2008", "0.870", "-76.620",
    "Hydro-sanitary system, CNP station Villa Garzón, Colombia (USASpending description).",
    "usaspending_misc_villa_garzon_hydrosan_429k_2008",
    "CONSTRUCTION OF HYDRO-SANITARY SYSTEM AT COLOMBIA NATIONAL POLICE STATION IN VILLA GARZON, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC08C0012_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle981",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC08C0012_1900_-NONE-_-NONE- (Villa Garzón hydro-sanitary). Signed 2008-02-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC08C0012_1900_-NONE-_-NONE-/.",
    "USASpending: Villa Garzón hydro-sanitary USD 0.429m. Supports misc_villa_garzon_hydrosan_429k_2008.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 428931.13; date_signed 2008-02-07.",
)

# === Cycle 982 ===
row_doc(
    "partenon_lima_cmr_roof_428k_2017",
    "infrastructure", "building_materials", "other",
    "Partenon Contratistas — Lima CMR residence roof replacement",
    "Peru",
    "21 Apr 2017: Department of State awards contract SGE50017C0022 to Partenon Contratistas for Lima CMR residence roof replacement project; obligated USD 428,245.06. CapEx face = award obligation.",
    "428245.06", "2017-04-21", "2017", "-12.046", "-77.043",
    "CMR residence roof replacement, Lima, Peru (USASpending description).",
    "usaspending_partenon_lima_cmr_roof_428k_2017",
    "IGF::OT::IGF LIMA, PERU - CMR RESIDENCE ROOF REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50017C0022_1900_-NONE-_-NONE-/",
    "Actor: Partenon Contratistas E.I.R.L. (Peru) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle982",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50017C0022_1900_-NONE-_-NONE- (Partenon Lima CMR roof). Signed 2017-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50017C0022_1900_-NONE-_-NONE-/.",
    "USASpending: Partenon Lima CMR roof USD 0.428m. Supports partenon_lima_cmr_roof_428k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 428245.06; date_signed 2017-04-21.",
)

row_doc(
    "proyectos_cicor_425k_2018",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — CICOR operations room renovation",
    "Colombia",
    "2 Mar 2018: Department of State awards contract 19AQMM18C0061 to Proyectos Civiles for CICOR operations room renovation; obligated USD 425,387.23. CapEx face = award obligation. Exact site unnamed beyond CICOR — lat/lon blank.",
    "425387.23", "2018-03-02", "2018", "", "",
    "CICOR operations room renovation, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_proyectos_cicor_425k_2018",
    "CICOR OPERATIONS ROOM RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0061_1900_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle982",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0061_1900_-NONE-_-NONE- (Proyectos CICOR). Signed 2018-03-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0061_1900_-NONE-_-NONE-/.",
    "USASpending: Proyectos CICOR USD 0.425m. Supports proyectos_cicor_425k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 425387.23; date_signed 2018-03-02.",
)

row_doc(
    "seapac_guyana_elevator_420k_2021",
    "infrastructure", "building_materials", "us",
    "Sea Pac Engineering — U.S. Embassy Georgetown chancery elevator",
    "Guyana",
    "2 Feb 2021: Department of State awards contract 19GE5021C0006 to Sea Pac Engineering for construction services to replace the elevator within the U.S. Embassy Georgetown, Guyana chancery; obligated USD 419,890. CapEx face = award obligation.",
    "419890", "2021-02-02", "2021", "6.801", "-58.155",
    "Chancery elevator replacement, U.S. Embassy Georgetown, Guyana (USASpending description).",
    "usaspending_seapac_guyana_elevator_420k_2021",
    "CONSTRUCTION SERVICES TO REPLACEMENT OF THE ELEVATOR WITHIN THE US EMBASSY GEORGETOWN, GUYANA CHANCERY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0006_1900_-NONE-_-NONE-/",
    "Actor: Sea Pac Engineering Inc. (Los Angeles CA, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle982",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0006_1900_-NONE-_-NONE- (Sea Pac Georgetown elevator). Signed 2021-02-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0006_1900_-NONE-_-NONE-/.",
    "USASpending: Sea Pac Georgetown elevator USD 0.420m. Supports seapac_guyana_elevator_420k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 419890; date_signed 2021-02-02.",
)

row_doc(
    "proyectos_warehouse_exp_419k_2009",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — warehouse expansion construction",
    "Colombia",
    "25 Jun 2009: Department of State awards contract SWHARC09C0001 to Proyectos Civiles for warehouse expansion construction (PoP Colombia); obligated USD 419,074.94. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "419074.94", "2009-06-25", "2009", "", "",
    "Warehouse expansion construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_proyectos_warehouse_exp_419k_2009",
    "WAREHOUSE EXPANSION CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09C0001_1900_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle982",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC09C0001_1900_-NONE-_-NONE- (Proyectos warehouse expansion). Signed 2009-06-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Proyectos warehouse expansion USD 0.419m. Supports proyectos_warehouse_exp_419k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 419074.94; date_signed 2009-06-25.",
)

row_doc(
    "marago_diran_facatativa_419k_2018",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — DIRAN Int and Facatativá operations rooms",
    "Colombia",
    "28 Sep 2018: Department of State awards contract 19AQMM18C0236 to Constructora Marago for renovation of operations rooms at DIRAN Int and Facatativá, Colombia; obligated USD 418,950. CapEx face = award obligation.",
    "418950", "2018-09-28", "2018", "4.814", "-74.355",
    "DIRAN Int / Facatativá operations rooms renovation, Colombia (USASpending description; Facatativá pin).",
    "usaspending_marago_diran_facatativa_419k_2018",
    "RENOVATION OF THE OPERATION ROOMS AT DIRAN INT AND  FACATATIVA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0236_1900_-NONE-_-NONE-/",
    "Actor: Constructora Marago S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle982",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0236_1900_-NONE-_-NONE- (Marago DIRAN Facatativá). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0236_1900_-NONE-_-NONE-/.",
    "USASpending: Marago DIRAN Facatativá USD 0.419m. Supports marago_diran_facatativa_419k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 418950; date_signed 2018-09-28.",
)

# === Cycle 983 ===
row_doc(
    "sepdes_sono_bouy_warehouse_415k_2013",
    "infrastructure", "building_materials", "other",
    "Servicios para el Desarrollo — sono-bouy warehouse",
    "El Salvador",
    "29 Sep 2013: U.S. Army Corps of Engineers awards task order 0009 under W9127813D0022 to Servicios para el Desarrollo for sono-bouy warehouse (PoP El Salvador); obligated USD 415,098.86. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "415098.86", "2013-09-29", "2013", "", "",
    "Sono-bouy warehouse, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_sepdes_sono_bouy_warehouse_415k_2013",
    "IGF::OT::IGF SONO-BOUY WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127813D0022_9700/",
    "Actor: Servicios para el Desarrollo de la Infraestructura (San Pedro Sula) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle983",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127813D0022_9700 (SEP DES sono-bouy warehouse). Signed 2013-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127813D0022_9700/.",
    "USASpending: SEP DES sono-bouy warehouse USD 0.415m. Supports sepdes_sono_bouy_warehouse_415k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 415098.86; date_signed 2013-09-29.",
)

row_doc(
    "john_d_belize_warehouse_448k_2006",
    "infrastructure", "building_materials", "other",
    "John D Engineering — Belize warehouse construction",
    "Belize",
    "14 Aug 2006: Department of Defense awards contract N6247006C6017 to John D Engineering for warehouse construction in Belize; obligated USD 447,842.32. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "447842.32", "2006-08-14", "2006", "", "",
    "Warehouse construction, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_john_d_belize_warehouse_448k_2006",
    "CONSTRUCT  WAREHOUSE, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6247006C6017_9700_-NONE-_-NONE-/",
    "Actor: John D Engineering Ltd. (Ladyville, Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle983",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6247006C6017_9700_-NONE-_-NONE- (John D Belize warehouse). Signed 2006-08-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6247006C6017_9700_-NONE-_-NONE-/.",
    "USASpending: John D Belize warehouse USD 0.448m. Supports john_d_belize_warehouse_448k_2006.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 447842.32; date_signed 2006-08-14.",
)

row_doc(
    "medina_hattieville_411k_2014",
    "infrastructure", "building_materials", "other",
    "Medina's Construction — Hattieville community center",
    "Belize",
    "26 Sep 2014: U.S. Army Corps of Engineers awards contract W912CL14C0029 to Medina's Construction for construction of community center in Hattieville, Belize; obligated USD 410,743.79. CapEx face = award obligation.",
    "410743.79", "2014-09-26", "2014", "17.450", "-88.350",
    "Community center, Hattieville, Belize (USASpending description).",
    "usaspending_medina_hattieville_411k_2014",
    "CONSTRUCTION OF COMMUNITY CENTER, HATTIEVILLE, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL14C0029_9700_-NONE-_-NONE-/",
    "Actor: Medina's Construction Limited (Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle983",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL14C0029_9700_-NONE-_-NONE- (Medina Hattieville). Signed 2014-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL14C0029_9700_-NONE-_-NONE-/.",
    "USASpending: Medina Hattieville community center USD 0.411m. Supports medina_hattieville_411k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 410743.79; date_signed 2014-09-26.",
)

row_doc(
    "seobra_gamboa_shop_406k_2021",
    "infrastructure", "building_materials", "other",
    "Seobra — Gamboa maintenance shop construction",
    "Panama",
    "22 Sep 2021: Smithsonian awards contract 33330221CF0010433 to Seobra for construction services for the maintenance shop at Gamboa Project, Gamboa, Province of Colón, Panama; obligated USD 406,342.21. CapEx face = award obligation.",
    "406342.21", "2021-09-22", "2021", "9.120", "-79.700",
    "Maintenance shop, Gamboa, Colón Province, Panama (USASpending description).",
    "usaspending_seobra_gamboa_shop_406k_2021",
    "CONSTRUCTION SERVICES FOR THE MAINTENANCE SHOP AT GAMBOA PROJECT LOCATED AT GAMBOA, PROVINCE OF COLON, REPUBLI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010433_3300_-NONE-_-NONE-/",
    "Actor: Seobra S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle983",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330221CF0010433_3300_-NONE-_-NONE- (Seobra Gamboa shop). Signed 2021-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010433_3300_-NONE-_-NONE-/.",
    "USASpending: Seobra Gamboa shop USD 0.406m. Supports seobra_gamboa_shop_406k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 406342.21; date_signed 2021-09-22.",
)

row_doc(
    "eei_guayaquil_vetting_404k_2026",
    "infrastructure", "building_materials", "other",
    "EEI — Guayaquil vetting center construction",
    "Ecuador",
    "25 Sep 2026: Department of State awards contract 19GE5026C0123 to Estudios Edificaciones e Interventorías for construction of a vetting center in Guayaquil, Ecuador; obligated USD 403,803.39. CapEx face = award obligation.",
    "403803.39", "2026-09-25", "2026", "-2.170", "-79.922",
    "Vetting center, Guayaquil, Ecuador (USASpending description).",
    "usaspending_eei_guayaquil_vetting_404k_2026",
    "CONSTRUCTION OF A VETTING CENTER IN GUAYAQUIL, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0123_1900_-NONE-_-NONE-/",
    "Actor: EEI S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle983",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0123_1900_-NONE-_-NONE- (EEI Guayaquil vetting). Signed 2026-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0123_1900_-NONE-_-NONE-/.",
    "USASpending: EEI Guayaquil vetting center USD 0.404m. Supports eei_guayaquil_vetting_404k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 403803.39; date_signed 2026-09-25.",
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
    print(f"cycles981-983 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
