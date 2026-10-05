#!/usr/bin/env python3
"""Cycles 1041–1043: USASpending LatAm CapEx residual (~USD0.05–0.072m).

Seeds: 20262041–20262043. Thin top-up dry (balsa/nickel/fission_smr).
Holdovers closed: Tabcon Guyana roof hatch; Forte Barbados residence.
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


# === Cycle 1041 (seed 20262041) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "tabcon_guyana_roof_hatch_60k_2025",
    "infrastructure", "building_materials", "us",
    "Tabcon — Guyana Georgetown roof hatch replacement",
    "Guyana",
    "4 Feb 2025: Department of State awards order 19AQMM25F0298 to Tabcon, Inc. for Georgetown, Guyana roof hatch replacement (PoP Guyana); obligated USD 59,828.20. CapEx face = award obligation.",
    "59828.20", "2025-02-04", "2025", "6.801", "-58.155",
    "Roof hatch replacement, Georgetown, Guyana (USASpending description; Georgetown named).",
    "usaspending_tabcon_guyana_roof_hatch_60k_2025",
    "GEORGETOWN, GUYANA ROOF HATCH REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F0298_1900_19AQMM19D0084_1900/",
    "Actor: Tabcon, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1041",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25F0298_1900_19AQMM19D0084_1900 (Tabcon Guyana roof hatch). Signed 2025-02-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F0298_1900_19AQMM19D0084_1900/.",
    "USASpending: Tabcon Guyana roof hatch USD 0.060m. Supports tabcon_guyana_roof_hatch_60k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59828.20; date_signed 2025-02-04.",
)

row_doc(
    "western_extralite_panama_nec_lighting_72k_2014",
    "infrastructure", "building_materials", "us",
    "Western Extralite — Panama NEC lighting repair",
    "Panama",
    "29 Sep 2014: Department of State awards contract SPM07014M0872 to Western Extralite Company for lighting repair project at the NEC (7901.C) (PoP Panama); obligated USD 71,958. CapEx face = award obligation. Exact NEC site unnamed beyond post — lat/lon blank.",
    "71958", "2014-09-29", "2014", "", "",
    "Lighting repair at NEC, Panama (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_western_extralite_panama_nec_lighting_72k_2014",
    "LIGHTING REPAIR PROJECT AT THE NEC (7901.C)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0872_1900_-NONE-_-NONE-/",
    "Actor: Western Extralite Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1041",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07014M0872_1900_-NONE-_-NONE- (Western Extralite Panama NEC lighting). Signed 2014-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0872_1900_-NONE-_-NONE-/.",
    "USASpending: Western Extralite Panama NEC lighting USD 0.072m. Supports western_extralite_panama_nec_lighting_72k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71958; date_signed 2014-09-29.",
)

row_doc(
    "aureliano_brazil_sliding_gates_72k_2025",
    "infrastructure", "building_materials", "other",
    "Aureliano Construções — Brazil Brasília sliding gates safety update",
    "Brazil",
    "30 Apr 2025: Department of State awards contract 19BR2525P0557 to Aureliano Construcoes Ltda for FC 5841 sliding gates safety update (PoP Brazil); obligated USD 71,829.40. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "71829.40", "2025-04-30", "2025", "", "",
    "Sliding gates safety update, Brasília post, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_aureliano_brazil_sliding_gates_72k_2025",
    "BSB|FAC|FC 5841 SLIDING GATES SAFETY UPDATE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P0557_1900_-NONE-_-NONE-/",
    "Actor: Aureliano Construcoes Ltda (Brazil) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1041",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2525P0557_1900_-NONE-_-NONE- (Aureliano Brazil sliding gates). Signed 2025-04-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P0557_1900_-NONE-_-NONE-/.",
    "USASpending: Aureliano Brazil sliding gates USD 0.072m. Supports aureliano_brazil_sliding_gates_72k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71829.40; date_signed 2025-04-30.",
)

row_doc(
    "misc_belize_police_generator_ats_72k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Belize police academy generator and ATS",
    "Belize",
    "23 Dec 2013: Department of State awards contract SBH20014M0040 for INL generator and ATS switch for police academy (PoP Belize); obligated USD 71,687.50. CapEx face = award obligation. Recipient redacted; exact academy unnamed — lat/lon blank.",
    "71687.50", "2013-12-23", "2013", "", "",
    "Generator and ATS switch for police academy, Belize (USASpending description; academy not named — lat/lon blank).",
    "usaspending_misc_belize_police_generator_ats_72k_2013",
    "IGF::OT::IGF - FOR OTHER FUNCTIONS   INLBMP-IN36BZMM-GENERATOR AND ATS SWITCH FOR POLICE ACADEMY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20014M0040_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1041",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20014M0040_1900_-NONE-_-NONE- (Belize police generator ATS). Signed 2013-12-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20014M0040_1900_-NONE-_-NONE-/.",
    "USASpending: Belize police generator ATS USD 0.072m. Supports misc_belize_police_generator_ats_72k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71687.50; date_signed 2013-12-23.",
)

row_doc(
    "romero_peru_sand_filter_72k_2015",
    "resources", "water", "other",
    "Luis Walter Romero Malaga — Peru Lima embassy sand filter repair",
    "Peru",
    "28 Sep 2015: Department of State awards contract SPE50015C0017 to Luis Walter Romero Malaga E.I.R.L. for sand filter repair at embassy compound (PoP Peru); obligated USD 71,767.60. CapEx face = award obligation.",
    "71767.60", "2015-09-28", "2015", "-12.092", "-77.049",
    "Sand filter repair at embassy compound, Lima, Peru (USASpending description; Lima named).",
    "usaspending_romero_peru_sand_filter_72k_2015",
    "LIMA 2015 CONTRACT SAND FILTER REPAIR AT EMBASSY COMPOUND IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015C0017_1900_-NONE-_-NONE-/",
    "Actor: Luis Walter Romero Malaga E.I.R.L. (Peru) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1041",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015C0017_1900_-NONE-_-NONE- (Romero Peru sand filter). Signed 2015-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015C0017_1900_-NONE-_-NONE-/.",
    "USASpending: Romero Peru sand filter USD 0.072m. Supports romero_peru_sand_filter_72k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71767.60; date_signed 2015-09-28.",
)

# === Cycle 1042 (seed 20262042) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_brasilia_72k_2012",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Brazil Brasília security installation",
    "Brazil",
    "27 Nov 2012: Department of State awards order SAQMMA13F0176 to Applied Security Technologies Inc for security installation Brasília (PoP Brazil); obligated USD 71,862.44. CapEx face = award obligation.",
    "71862.44", "2012-11-27", "2012", "-15.794", "-47.882",
    "Security installation, Brasília, Brazil (USASpending description; Brasília named).",
    "usaspending_applied_security_brasilia_72k_2012",
    "SECURITY INSTALLATION BRASILIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0176_1900_SAQMMA07D0030_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1042",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F0176_1900_SAQMMA07D0030_1900 (Applied Security Brasília). Signed 2012-11-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0176_1900_SAQMMA07D0030_1900/.",
    "USASpending: Applied Security Brasília USD 0.072m. Supports applied_security_brasilia_72k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71862.44; date_signed 2012-11-27.",
)

row_doc(
    "usmax_dr_security_install_70k_2013",
    "infrastructure", "building_materials", "us",
    "USMAX — Dominican Republic Santo Domingo security installation",
    "Dominican Republic",
    "2 Aug 2013: Department of State awards order SAQMMA13F2269 to USMAX Corporation for security installation Santo Domingo (PoP Dominican Republic); obligated USD 70,209.39. CapEx face = award obligation.",
    "70209.39", "2013-08-02", "2013", "18.486", "-69.931",
    "Security installation, Santo Domingo, Dominican Republic (USASpending description; Santo Domingo named).",
    "usaspending_usmax_dr_security_install_70k_2013",
    "SECURITY INSTALLATION SANTO DOMINGO, DOMINICAN REPUBLIC IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F2269_1900_SAQMMA13D0055_1900/",
    "Actor: USMAX Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1042",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F2269_1900_SAQMMA13D0055_1900 (USMAX DR security). Signed 2013-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F2269_1900_SAQMMA13D0055_1900/.",
    "USASpending: USMAX DR security USD 0.070m. Supports usmax_dr_security_install_70k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70209.39; date_signed 2013-08-02.",
)

row_doc(
    "forte_barbados_residence_51k_2022",
    "infrastructure", "building_materials", "other",
    "Forte' Design & Construction — Barbados official residence renovations",
    "Barbados",
    "21 Dec 2022: Department of State awards contract 19BB2123C0001 to Forte' Design & Construction Services Inc. for official residence renovations (PoP Barbados); obligated USD 51,004.89. CapEx face = award obligation. Exact residence unnamed — lat/lon blank.",
    "51004.89", "2022-12-21", "2022", "", "",
    "Official residence renovations, Barbados (USASpending description; residence not named — lat/lon blank).",
    "usaspending_forte_barbados_residence_51k_2022",
    "IS NOT FOREIGN ASSISTANCE- OFFICIAL RESIDENCE RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2123C0001_1900_-NONE-_-NONE-/",
    "Actor: Forte' Design & Construction Services Inc. (Barbados) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1042",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2123C0001_1900_-NONE-_-NONE- (Forte Barbados residence). Signed 2022-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2123C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Forte Barbados residence USD 0.051m. Supports forte_barbados_residence_51k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51004.89; date_signed 2022-12-21.",
)

row_doc(
    "insaso_suriname_roof_71k_2022",
    "infrastructure", "building_materials", "other",
    "Bouwbedrijf Insaso — Suriname N9 roof restoration",
    "Suriname",
    "26 Sep 2022: Department of State awards contract 19NS5022P0606 to Bouwbedrijf Insaso NV for FAC 7355 N9 roof restoration project (PoP Suriname); obligated USD 71,351.13. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "71351.13", "2022-09-26", "2022", "", "",
    "N9 roof restoration, Suriname (USASpending description; building not named — lat/lon blank).",
    "usaspending_insaso_suriname_roof_71k_2022",
    "FAC 7355 N9 ROOF RESTORATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5022P0606_1900_-NONE-_-NONE-/",
    "Actor: Bouwbedrijf Insaso NV (Suriname) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1042",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NS5022P0606_1900_-NONE-_-NONE- (Insaso Suriname roof). Signed 2022-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5022P0606_1900_-NONE-_-NONE-/.",
    "USASpending: Insaso Suriname roof USD 0.071m. Supports insaso_suriname_roof_71k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71351.13; date_signed 2022-09-26.",
)

row_doc(
    "bolanos_ecuador_msgq_kitchen_72k_2022",
    "infrastructure", "building_materials", "other",
    "Bolaños Alban — Ecuador MSGQ kitchen restoration",
    "Ecuador",
    "19 May 2022: Department of State awards contract 19EC7522C0010 to Bolanos Alban Fausto Tarquino for restauration of MSGQ kitchen (PoP Ecuador); obligated USD 71,670.01. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "71670.01", "2022-05-19", "2022", "", "",
    "MSGQ kitchen restoration, Ecuador (USASpending description; compound not named — lat/lon blank).",
    "usaspending_bolanos_ecuador_msgq_kitchen_72k_2022",
    "1900.0-7903-R-PR10398406-FWP#283-RESTAURATION OF MSGQ KITCHEN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0010_1900_-NONE-_-NONE-/",
    "Actor: Bolanos Alban Fausto Tarquino (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1042",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0010_1900_-NONE-_-NONE- (Bolaños Ecuador MSGQ kitchen). Signed 2022-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0010_1900_-NONE-_-NONE-/.",
    "USASpending: Bolaños Ecuador MSGQ kitchen USD 0.072m. Supports bolanos_ecuador_msgq_kitchen_72k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 71670.01; date_signed 2022-05-19.",
)

# === Cycle 1043 (seed 20262043) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "kva_electric_bogota_70k_2015",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Colombia Bogotá electrical work",
    "Colombia",
    "28 Dec 2015: Department of State awards order SAQMMA16F0439 to KVA Electric Inc for electrical work Bogotá (PoP Colombia); obligated USD 69,882.99. CapEx face = award obligation.",
    "69882.99", "2015-12-28", "2015", "4.711", "-74.072",
    "Electrical work, Bogotá, Colombia (USASpending description; Bogotá named).",
    "usaspending_kva_electric_bogota_70k_2015",
    "ELECTRICAL WORK BOGOTA, COLUMBIA  IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F0439_1900_SAQMMA13D0022_1900/",
    "Actor: KVA Electric Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1043",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F0439_1900_SAQMMA13D0022_1900 (KVA Electric Bogotá). Signed 2015-12-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F0439_1900_SAQMMA13D0022_1900/.",
    "USASpending: KVA Electric Bogotá USD 0.070m. Supports kva_electric_bogota_70k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69882.99; date_signed 2015-12-28.",
)

row_doc(
    "ge_jamaica_nec_breakers_62k_2016",
    "energy", "power_plants_grid", "us",
    "General Electric International — Jamaica NEC 2000A breaker replacement",
    "Jamaica",
    "25 Feb 2016: Department of State awards contract SJM37016M0460 to General Electric International, Inc. for replacement 2000A breakers for NEC (7901.C) (PoP Jamaica); obligated USD 61,664. CapEx face = award obligation. Exact NEC site unnamed beyond post — lat/lon blank.",
    "61664", "2016-02-25", "2016", "", "",
    "2000A breaker replacement at NEC, Jamaica (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_ge_jamaica_nec_breakers_62k_2016",
    "IGF::OT::IGF FAC - REPLACEMENT 2000A BREAKERS FOR NEC (7901.C)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M0460_1900_-NONE-_-NONE-/",
    "Actor: General Electric International, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1043",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37016M0460_1900_-NONE-_-NONE- (GE Jamaica NEC breakers). Signed 2016-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M0460_1900_-NONE-_-NONE-/.",
    "USASpending: GE Jamaica NEC breakers USD 0.062m. Supports ge_jamaica_nec_breakers_62k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61664; date_signed 2016-02-25.",
)

row_doc(
    "misc_nicaragua_fence_71k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Nicaragua fence construction",
    "Nicaragua",
    "30 May 2017: Department of State awards contract SNU70017M0187 for fence construction (PoP Nicaragua); obligated USD 70,800. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "70800", "2017-05-30", "2017", "", "",
    "Fence construction, Nicaragua (USASpending PoP Nicaragua; site not named — lat/lon blank).",
    "usaspending_misc_nicaragua_fence_71k_2017",
    "FENCE CONSTRUCTION IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70017M0187_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Nicaragua under-covered weight.",
    "hunt_cycle1043",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70017M0187_1900_-NONE-_-NONE- (Nicaragua fence). Signed 2017-05-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70017M0187_1900_-NONE-_-NONE-/.",
    "USASpending: Nicaragua fence USD 0.071m. Supports misc_nicaragua_fence_71k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70800; date_signed 2017-05-30.",
)

row_doc(
    "misc_bahamas_perimeter_fence_71k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas NEC perimeter fence",
    "Bahamas",
    "7 Jun 2017: Department of State awards contract SBF50017C0002 for NEC perimeter fence installation (PoP Bahamas); obligated USD 70,781.23. CapEx face = award obligation. Recipient redacted; exact NEC site unnamed — lat/lon blank.",
    "70781.23", "2017-06-07", "2017", "", "",
    "NEC perimeter fence installation, Bahamas (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_perimeter_fence_71k_2017",
    "IGF::OT::IGF NEC - PERIMETER FENCE INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1043",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017C0002_1900_-NONE-_-NONE- (Bahamas NEC perimeter fence). Signed 2017-06-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Bahamas NEC perimeter fence USD 0.071m. Supports misc_bahamas_perimeter_fence_71k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70781.23; date_signed 2017-06-07.",
)

row_doc(
    "temi_caracas_switchgear_71k_2018",
    "energy", "power_plants_grid", "other",
    "TEMI — Venezuela Caracas switchgear",
    "Venezuela",
    "28 Sep 2018: Department of State awards contract 19AQMM18C0256 to TEMI, C.A. for Caracas switchgear (PoP Venezuela); obligated USD 70,549.12. CapEx face = award obligation.",
    "70549.12", "2018-09-28", "2018", "10.480", "-66.903",
    "Switchgear, Caracas, Venezuela (USASpending description; Caracas named).",
    "usaspending_temi_caracas_switchgear_71k_2018",
    "CARACAS SWITCHGEAR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0256_1900_-NONE-_-NONE-/",
    "Actor: TEMI, C.A. (Venezuela) — other. Official USASpending Award API. Shuffle power_plants_grid. Venezuela beyond-solar weight.",
    "hunt_cycle1043",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0256_1900_-NONE-_-NONE- (TEMI Caracas switchgear). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0256_1900_-NONE-_-NONE-/.",
    "USASpending: TEMI Caracas switchgear USD 0.071m. Supports temi_caracas_switchgear_71k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70549.12; date_signed 2018-09-28.",
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
