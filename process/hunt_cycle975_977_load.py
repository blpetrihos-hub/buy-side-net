#!/usr/bin/env python3
"""Cycles 975–977: USASpending LatAm CapEx residual (~USD0.48–0.70m).

Seeds: 20261975–20261977. Thin top-up dry.
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


# === Cycle 975 ===
row_doc(
    "western_necocli_barrier_701k_2017",
    "infrastructure", "bridges_roads", "other",
    "Western Support Service — Necoclí steel barrier wall",
    "Colombia",
    "27 Jun 2017: Department of State awards contract SAQMMA17C0134 to Western Support Service for construction of a steel barrier wall in Necoclí, Colombia; obligated USD 700,587. CapEx face = award obligation.",
    "700587", "2017-06-27", "2017", "8.426", "-76.779",
    "Steel barrier wall, Necoclí, Colombia (USASpending description).",
    "usaspending_western_necocli_barrier_701k_2017",
    "CONSTRUCT STEEL BARRIER WALL NECOCLI, COLOMBIA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0134_1900_-NONE-_-NONE-/",
    "Actor: Western Support Service S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle975",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0134_1900_-NONE-_-NONE- (Western Necoclí barrier). Signed 2017-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0134_1900_-NONE-_-NONE-/.",
    "USASpending: Western Necoclí barrier USD 0.701m. Supports western_necocli_barrier_701k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 700587; date_signed 2017-06-27.",
)

row_doc(
    "marago_carabineros_690k_2018",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — CNP Carabineros facilities",
    "Colombia",
    "11 Apr 2018: Department of State awards contract 19AQMM18C0086 to Constructora Marago for construction of CNP Carabineros facilities; obligated USD 690,103.70. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "690103.70", "2018-04-11", "2018", "", "",
    "CNP Carabineros facilities, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_marago_carabineros_690k_2018",
    "CONSTRUCTION OF THE CNP CARABINEROS FACILITIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0086_1900_-NONE-_-NONE-/",
    "Actor: Constructora Marago S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle975",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0086_1900_-NONE-_-NONE- (Marago Carabineros). Signed 2018-04-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0086_1900_-NONE-_-NONE-/.",
    "USASpending: Marago Carabineros USD 0.690m. Supports marago_carabineros_690k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 690103.70; date_signed 2018-04-11.",
)

row_doc(
    "marago_popayan_cefop_688k_2015",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — CEFOP construction upgrades Popayán",
    "Colombia",
    "23 Sep 2015: Department of State awards contract SWHARC15C0005 to Constructora Marago for CEFOP construction upgrades in Popayán; obligated USD 688,224.75. CapEx face = award obligation.",
    "688224.75", "2015-09-23", "2015", "2.441", "-76.606",
    "CEFOP construction upgrades, Popayán, Colombia (USASpending description).",
    "usaspending_marago_popayan_cefop_688k_2015",
    "CEFOP CONSTRUCTION UPGRADES POPAYAN IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15C0005_1900_-NONE-_-NONE-/",
    "Actor: Constructora Marago S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle975",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15C0005_1900_-NONE-_-NONE- (Marago Popayán CEFOP). Signed 2015-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15C0005_1900_-NONE-_-NONE-/.",
    "USASpending: Marago Popayán CEFOP USD 0.688m. Supports marago_popayan_cefop_688k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 688224.75; date_signed 2015-09-23.",
)

row_doc(
    "kwaan_espinal_modular_668k_2023",
    "infrastructure", "building_materials", "us",
    "Kwaan Tech — Espinal modular lodging building",
    "Colombia",
    "5 Sep 2023: Department of State awards task order 19AQMM23F1722 to Kwaan Tech for modular lodging building in Espinal; obligated USD 668,312.13. CapEx face = award obligation.",
    "668312.13", "2023-09-05", "2023", "4.149", "-74.884",
    "Modular lodging building, Espinal, Colombia (USASpending description).",
    "usaspending_kwaan_espinal_modular_668k_2023",
    "MODULAR LODGING BUILDING ESPINAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1722_1900_19AQMM23D0037_1900/",
    "Actor: Kwaan Tech LLC (Manassas VA, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle975",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1722_1900_19AQMM23D0037_1900 (Kwaan Espinal modular). Signed 2023-09-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1722_1900_19AQMM23D0037_1900/.",
    "USASpending: Kwaan Espinal modular USD 0.668m. Supports kwaan_espinal_modular_668k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 668312.13; date_signed 2023-09-05.",
)

row_doc(
    "seobra_slv_fitness_664k_2017",
    "infrastructure", "building_materials", "other",
    "Seobra — El Salvador fitness facility design/build",
    "El Salvador",
    "30 Sep 2017: U.S. Army Corps of Engineers awards task order W9127817F0496 to Seobra for design/build of a fitness facility in El Salvador; obligated USD 663,995. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "663995", "2017-09-30", "2017", "", "",
    "Fitness facility design/build, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_seobra_slv_fitness_664k_2017",
    "IGF::OT::IGF  DESIGN/BUILD OF FITNESS FACILITY, EL SAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0496_9700_W9127816D0098_9700/",
    "Actor: Seobra S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle975",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0496_9700_W9127816D0098_9700 (Seobra SLV fitness). Signed 2017-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0496_9700_W9127816D0098_9700/.",
    "USASpending: Seobra SLV fitness USD 0.664m. Supports seobra_slv_fitness_664k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 663995; date_signed 2017-09-30.",
)

# === Cycle 976 ===
row_doc(
    "marago_cenop_warehouses_659k_2019",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — CENOP-Pijaos two warehouses",
    "Colombia",
    "15 Jul 2019: Department of State awards contract 19AQMM19C0100 to Constructora Marago for construction of two warehouses at CENOP-Pijaos, Colombia; obligated USD 658,704.67. CapEx face = award obligation.",
    "658704.67", "2019-07-15", "2019", "4.090", "-75.150",
    "Two warehouses, CENOP-Pijaos, Colombia (USASpending description; approximate Tolima/Pijaos pin).",
    "usaspending_marago_cenop_warehouses_659k_2019",
    "CONSTRUCTION OF TWO WAREHOUSES AT CENOP-PIJAOS, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0100_1900_-NONE-_-NONE-/",
    "Actor: Constructora Marago S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle976",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0100_1900_-NONE-_-NONE- (Marago CENOP warehouses). Signed 2019-07-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0100_1900_-NONE-_-NONE-/.",
    "USASpending: Marago CENOP warehouses USD 0.659m. Supports marago_cenop_warehouses_659k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 658704.67; date_signed 2019-07-15.",
)

row_doc(
    "kunkel_panama_egress_653k_2019",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction — Building A secondary egress and panelboard roof",
    "Panama",
    "17 Sep 2019: Smithsonian awards contract 33330219CF0010397 to Kunkel Construction for secondary means of egress for Building A and roof for panelboards (PoP Panama); obligated USD 652,507.70. CapEx face = award obligation. Exact campus unnamed — lat/lon blank.",
    "652507.70", "2019-09-17", "2019", "", "",
    "Building A secondary egress / panelboard roof, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_kunkel_panama_egress_653k_2019",
    "CONSTRUCTION SERVICES FOR SECONDARY MEAN OF EGRESS FOR BUILDING A AND ROOF FOR PANELBOARDS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010397_3300_-NONE-_-NONE-/",
    "Actor: Kunkel Construction Inc. (Panama City) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle976",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330219CF0010397_3300_-NONE-_-NONE- (Kunkel Panama egress). Signed 2019-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010397_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Panama egress USD 0.653m. Supports kunkel_panama_egress_653k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 652507.70; date_signed 2019-09-17.",
)

row_doc(
    "martinez_mexico_accessibility_630k_2011",
    "infrastructure", "building_materials", "us",
    "Martinez International — U.S. Embassy Mexico City accessibility improvements",
    "Mexico",
    "22 Sep 2011: Department of State awards task order SAQMMA11F4166 to Martinez International for barrier-free accessibility construction improvements at the U.S. Embassy Mexico City; obligated USD 629,991. CapEx face = award obligation.",
    "629991", "2011-09-22", "2011", "19.432", "-99.133",
    "Barrier-free accessibility improvements, U.S. Embassy Mexico City (USASpending description).",
    "usaspending_martinez_mexico_accessibility_630k_2011",
    "CONSTRUCTION SERVICES FOR BARRIER FREE ACCESSIBILITY IMPROVEMENTS AT THE U.S. EMBASSY MEXI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4166_1900_SAQMMA08D0002_1900/",
    "Actor: Martinez International Corporation (Parker CO, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle976",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F4166_1900_SAQMMA08D0002_1900 (Martinez Mexico accessibility). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4166_1900_SAQMMA08D0002_1900/.",
    "USASpending: Martinez Mexico accessibility USD 0.630m. Supports martinez_mexico_accessibility_630k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 629991; date_signed 2011-09-22.",
)

row_doc(
    "john_d_darien_lumber_607k_2011",
    "infrastructure", "building_materials", "other",
    "John D Engineering — HAP 8869 Darién community lumber yard",
    "Panama",
    "28 Sep 2011: U.S. Army Corps of Engineers awards contract W912CL11C0048 to John D Engineering for HAP 8869 construction of a community lumber yard in Darién Province, Panama; obligated USD 606,753.84. CapEx face = award obligation. Exact village unnamed — lat/lon blank.",
    "606753.84", "2011-09-28", "2011", "", "",
    "Community lumber yard, Darién Province, Panama (USASpending description; site not named beyond province — lat/lon blank).",
    "usaspending_john_d_darien_lumber_607k_2011",
    "HAP 8869 CONSTRUCT COMMUNITY LUMBER YARD IN DARIEN PROVINCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0048_9700_-NONE-_-NONE-/",
    "Actor: John D Engineering Ltd. (Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle976",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0048_9700_-NONE-_-NONE- (John D Darién lumber). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0048_9700_-NONE-_-NONE-/.",
    "USASpending: John D Darién lumber yard USD 0.607m. Supports john_d_darien_lumber_607k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 606753.84; date_signed 2011-09-28.",
)

row_doc(
    "power_engineers_lima_electrical_590k_2010",
    "energy", "power_plants_grid", "us",
    "POWER Engineers — Lima power systems electrical work",
    "Peru",
    "7 Apr 2010: Department of State awards task order SAQMMA10F1225 to POWER Engineers for power systems engineering electrical work in Lima, Peru; obligated USD 590,265.14. CapEx face = award obligation.",
    "590265.14", "2010-04-07", "2010", "-12.046", "-77.043",
    "Power systems electrical work, Lima, Peru (USASpending description).",
    "usaspending_power_engineers_lima_electrical_590k_2010",
    "POWER SYSTEMS ENGINEERING- LIMA, PERU ELECTRICAL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F1225_1900_SALMEC05D0010_1900/",
    "Actor: POWER Engineers Inc. (Hailey ID, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle976",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F1225_1900_SALMEC05D0010_1900 (POWER Engineers Lima electrical). Signed 2010-04-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F1225_1900_SALMEC05D0010_1900/.",
    "USASpending: POWER Engineers Lima electrical USD 0.590m. Supports power_engineers_lima_electrical_590k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 590265.14; date_signed 2010-04-07.",
)

# === Cycle 977 ===
row_doc(
    "misc_ecuador_patios_595k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador construction patios/soil stabilization",
    "Ecuador",
    "3 Apr 2013: Department of State awards contract SEC75013C0001 for construction patios/soil stabilization (PoP Ecuador); obligated USD 594,936.20. CapEx face = award obligation. Recipient redacted; site not named — lat/lon blank.",
    "594936.20", "2013-04-03", "2013", "", "",
    "Construction patios/soil stabilization, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_patios_595k_2013",
    "IGF::OT::IGF 1930-L-1/1-PR2339096-CONSTRUCTION PATIOS/SOILSTABILIZATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75013C0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle977",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75013C0001_1900_-NONE-_-NONE- (Ecuador patios/soil). Signed 2013-04-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75013C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador patios/soil stabilization USD 0.595m. Supports misc_ecuador_patios_595k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 594936.20; date_signed 2013-04-03.",
)

row_doc(
    "hulke_exuma_opbat_583k_2010",
    "infrastructure", "building_materials", "us",
    "Hulke Construction — OPBAT maintenance facility FOL Exuma",
    "Bahamas",
    "25 Sep 2010: Department of Defense awards contract N6945010C0035 to Hulke Construction for OPBAT maintenance facility at FOL Exuma, Bahamas; obligated USD 583,112.80. CapEx face = award obligation.",
    "583112.80", "2010-09-25", "2010", "23.473", "-75.762",
    "OPBAT maintenance facility, FOL Exuma, Bahamas (USASpending description).",
    "usaspending_hulke_exuma_opbat_583k_2010",
    "OPBAT MAINTENANCE FACILITY; FOL EXUMA, BAHAMAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0035_9700_-NONE-_-NONE-/",
    "Actor: Hulke Construction Company LLC (Sanford FL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle977",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945010C0035_9700_-NONE-_-NONE- (Hulke Exuma OPBAT). Signed 2010-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0035_9700_-NONE-_-NONE-/.",
    "USASpending: Hulke Exuma OPBAT USD 0.583m. Supports hulke_exuma_opbat_583k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 583112.80; date_signed 2010-09-25.",
)

row_doc(
    "partenon_hap28294_drw_572k_2018",
    "infrastructure", "building_materials", "other",
    "Partenon Contratistas — HAP 28294 disaster relief warehouse",
    "Peru",
    "16 Jan 2018: U.S. Army Corps of Engineers awards task order W9127818F0169 to Partenon Contratistas for design/construct HAP 28294 DRW (disaster relief warehouse); obligated USD 571,822.03. CapEx face = award obligation. Exact site unnamed beyond HAP ID — lat/lon blank.",
    "571822.03", "2018-01-16", "2018", "", "",
    "HAP 28294 disaster relief warehouse, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_partenon_hap28294_drw_572k_2018",
    "DESIGN/CONSTRUCT HAP 28294 DRW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0169_9700_W9127813D0012_9700/",
    "Actor: Partenon Contratistas E.I.R.L. (Tarapoto, Peru) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle977",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0169_9700_W9127813D0012_9700 (Partenon HAP 28294 DRW). Signed 2018-01-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0169_9700_W9127813D0012_9700/.",
    "USASpending: Partenon HAP 28294 DRW USD 0.572m. Supports partenon_hap28294_drw_572k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 571822.03; date_signed 2018-01-16.",
)

row_doc(
    "seobra_chiman_clinic_488k_2011",
    "infrastructure", "building_materials", "other",
    "Seobra — HAP 7654 medical clinic renovation Chimán",
    "Panama",
    "15 Jun 2011: U.S. Army Corps of Engineers awards contract W912CL11C0023 to Seobra for HAP 7654 renovation of existing medical clinic in Chimán, Panama; obligated USD 487,535.69. CapEx face = award obligation.",
    "487535.69", "2011-06-15", "2011", "8.520", "-78.330",
    "Medical clinic renovation, Chimán, Panama (USASpending description; approximate community pin).",
    "usaspending_seobra_chiman_clinic_488k_2011",
    "HUMANITARIAN PROJECT - RENOVATION OF EXISTING MEDICAL CLINIC - HAP PROJECT 7654 CHIMAN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0023_9700_-NONE-_-NONE-/",
    "Actor: Seobra S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle977",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0023_9700_-NONE-_-NONE- (Seobra Chimán clinic). Signed 2011-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0023_9700_-NONE-_-NONE-/.",
    "USASpending: Seobra Chimán clinic USD 0.488m. Supports seobra_chiman_clinic_488k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 487535.69; date_signed 2011-06-15.",
)

row_doc(
    "almeida_brasilia_embassy_480k_2025",
    "infrastructure", "building_materials", "other",
    "Almeida Franca Engenharia — U.S. Embassy Brasília life-cycle renovation",
    "Brazil",
    "19 Sep 2025: Department of State awards contract 19GE5025C0136 to Almeida Franca Engenharia for design/build life-cycle renovation at U.S. Embassy Brasília; obligated USD 480,321.39. CapEx face = award obligation.",
    "480321.39", "2025-09-19", "2025", "-15.794", "-47.883",
    "Life-cycle renovation, U.S. Embassy Brasília (USASpending description).",
    "usaspending_almeida_brasilia_embassy_480k_2025",
    "DESIGN/BUILD LIFE CYCLE RENOVATION, U.S. EMBASSY BRASILIA, BRAZIL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0136_1900_-NONE-_-NONE-/",
    "Actor: Almeida Franca Engenharia Ltda. (Brasília) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle977",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5025C0136_1900_-NONE-_-NONE- (Almeida Brasília embassy). Signed 2025-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0136_1900_-NONE-_-NONE-/.",
    "USASpending: Almeida Brasília embassy USD 0.480m. Supports almeida_brasilia_embassy_480k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 480321.39; date_signed 2025-09-19.",
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
    print(f"cycles975-977 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
