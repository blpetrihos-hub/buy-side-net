#!/usr/bin/env python3
"""Cycles 1050–1052: USASpending LatAm CapEx residual (~USD0.043–0.071m).

Seeds: 20262050–20262052. Thin top-up dry.
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


# === Cycle 1050 (seed 20262050) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "oeg_ecuador_electrical_48k_2013",
    "energy", "power_plants_grid", "us",
    "OEG — Ecuador electrical work",
    "Ecuador",
    "2 Aug 2013: Department of State awards order SAQMMA13F2273 to OEG Inc for electrical work Ecuador (PoP Ecuador); obligated USD 47,988. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "47988", "2013-08-02", "2013", "", "",
    "Electrical work, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_oeg_ecuador_electrical_48k_2013",
    "ELECTRICAL WORK ECUADOR IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F2273_1900_SAQMMA12D0192_1900/",
    "Actor: OEG Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1050",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F2273_1900_SAQMMA12D0192_1900 (OEG Ecuador electrical). Signed 2013-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F2273_1900_SAQMMA12D0192_1900/.",
    "USASpending: OEG Ecuador electrical USD 0.048m. Supports oeg_ecuador_electrical_48k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47988; date_signed 2013-08-02.",
)

row_doc(
    "ge_jamaica_nec_4000a_breaker_44k_2016",
    "energy", "power_plants_grid", "us",
    "General Electric International — Jamaica NEC 4000A breaker replacement",
    "Jamaica",
    "16 Mar 2016: Department of State awards contract SJM37016M0534 to General Electric International, Inc. for replacement 4000A breaker — NEC (7901.C) (PoP Jamaica); obligated USD 43,709. CapEx face = award obligation. Exact NEC site unnamed — lat/lon blank.",
    "43709", "2016-03-16", "2016", "", "",
    "4000A breaker replacement at NEC, Jamaica (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_ge_jamaica_nec_4000a_breaker_44k_2016",
    "IGF::OT::IGF FAC - REPLACEMENT 4000A BREAKER - NEC (7901.C)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M0534_1900_-NONE-_-NONE-/",
    "Actor: General Electric International, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1050",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37016M0534_1900_-NONE-_-NONE- (GE Jamaica NEC 4000A breaker). Signed 2016-03-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M0534_1900_-NONE-_-NONE-/.",
    "USASpending: GE Jamaica NEC 4000A breaker USD 0.044m. Supports ge_jamaica_nec_4000a_breaker_44k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 43709; date_signed 2016-03-16.",
)

row_doc(
    "misc_ecuador_generators_control_69k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador compound generators control system",
    "Ecuador",
    "21 Jul 2023: Department of State awards contract 19EC7523P1200 for new generators control system (PoP Ecuador); obligated USD 68,863.31. CapEx face = award obligation. Recipient redacted; exact compound unnamed — lat/lon blank.",
    "68863.31", "2023-07-21", "2023", "", "",
    "New generators control system at compound, Ecuador (USASpending description; compound not named — lat/lon blank).",
    "usaspending_misc_ecuador_generators_control_69k_2023",
    "1900.FAC-7901RSTR-CMPD-FWP#282-NEW GENERATORS CONTROL SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P1200_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1050",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P1200_1900_-NONE-_-NONE- (Ecuador generators control). Signed 2023-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P1200_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador generators control USD 0.069m. Supports misc_ecuador_generators_control_69k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68863.31; date_signed 2023-07-21.",
)

row_doc(
    "misc_belize_electrical_plumbing_69k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Belize BTH electrical and plumbing",
    "Belize",
    "8 Mar 2017: Department of Defense awards contract W912CL17P0713 for BTH Belize 17 electrical and plumbing (PoP Belize); obligated USD 69,000.46. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "69000.46", "2017-03-08", "2017", "", "",
    "Electrical and plumbing works, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_belize_electrical_plumbing_69k_2017",
    "IGF::OT::IGF/G3/ BTH BELIZE 17/ELECTRICAL AND PLUMBING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17P0713_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1050",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL17P0713_9700_-NONE-_-NONE- (Belize electrical plumbing). Signed 2017-03-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL17P0713_9700_-NONE-_-NONE-/.",
    "USASpending: Belize electrical plumbing USD 0.069m. Supports misc_belize_electrical_plumbing_69k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69000.46; date_signed 2017-03-08.",
)

row_doc(
    "juan_parodi_honduras_fire_hvac_69k_2010",
    "infrastructure", "building_materials", "other",
    "Juan Parodi — Honduras fire station HVAC renovations",
    "Honduras",
    "13 Sep 2010: Department of Defense awards contract W9127810P0357 to Juan Parodi for fire station HVAC renovations (PoP Honduras); obligated USD 68,568. CapEx face = award obligation. Exact fire station unnamed — lat/lon blank.",
    "68568", "2010-09-13", "2010", "", "",
    "Fire station HVAC renovations, Honduras (USASpending description; station not named — lat/lon blank).",
    "usaspending_juan_parodi_honduras_fire_hvac_69k_2010",
    "FIRE STATION HVAC RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0357_9700_-NONE-_-NONE-/",
    "Actor: Juan Parodi (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1050",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0357_9700_-NONE-_-NONE- (Juan Parodi fire HVAC). Signed 2010-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0357_9700_-NONE-_-NONE-/.",
    "USASpending: Juan Parodi fire HVAC USD 0.069m. Supports juan_parodi_honduras_fire_hvac_69k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68568; date_signed 2010-09-13.",
)

# === Cycle 1051 (seed 20262051) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "boykin_stkitts_hvac_control_45k_2010",
    "infrastructure", "building_materials", "us",
    "Boykin Contracting — St. Kitts and Nevis central HVAC control repair B251",
    "Saint Kitts and Nevis",
    "13 Sep 2010: Department of Defense awards order 0008 to Boykin Contracting, Inc. for repair central HVAC control — B251 (PoP Saint Kitts and Nevis); obligated USD 45,415. CapEx face = award obligation. Exact building unnamed beyond B251 — lat/lon blank.",
    "45415", "2010-09-13", "2010", "", "",
    "Central HVAC control repair B251, Saint Kitts and Nevis (USASpending description; building coords not stated — lat/lon blank).",
    "usaspending_boykin_stkitts_hvac_control_45k_2010",
    "REPAIR CENTRAL HVAC CONTROL - B251",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_FA480309D0008_9700/",
    "Actor: Boykin Contracting, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1051",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_FA480309D0008_9700 (Boykin St Kitts HVAC). Signed 2010-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_FA480309D0008_9700/.",
    "USASpending: Boykin St Kitts HVAC USD 0.045m. Supports boykin_stkitts_hvac_control_45k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 45415; date_signed 2010-09-13.",
)

row_doc(
    "oeg_salvador_generator_49k_2011",
    "energy", "power_plants_grid", "us",
    "OEG — El Salvador generator program",
    "El Salvador",
    "10 Aug 2011: Department of State awards contract SES60011M0756 to OEG Inc for generator program (PoP El Salvador); obligated USD 49,246.87. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49246.87", "2011-08-10", "2011", "", "",
    "Generator program, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_oeg_salvador_generator_49k_2011",
    "7561 FUNDS, 19  - X-0535-0003 GENERATOR PROGRAM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M0756_1900_-NONE-_-NONE-/",
    "Actor: OEG Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1051",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60011M0756_1900_-NONE-_-NONE- (OEG El Salvador generator). Signed 2011-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M0756_1900_-NONE-_-NONE-/.",
    "USASpending: OEG El Salvador generator USD 0.049m. Supports oeg_salvador_generator_49k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49246.87; date_signed 2011-08-10.",
)

row_doc(
    "misc_mexico_seneca_kitchen_69k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Seneca 142 kitchen repairs",
    "Mexico",
    "27 Sep 2017: Department of State awards contract SMX53017C0014 for kitchen repairs at Seneca 142 (04 units) (PoP Mexico); obligated USD 68,526.96. CapEx face = award obligation.",
    "68526.96", "2017-09-27", "2017", "", "",
    "Kitchen repairs at Seneca 142 (4 units), Mexico (USASpending description; Seneca 142 named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_seneca_kitchen_69k_2017",
    "IGF::OT::IGF MEX/OBO/KITCHEN REPAIRS AT SENECA 142 (04 UNITS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017C0014_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1051",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53017C0014_1900_-NONE-_-NONE- (Mexico Seneca kitchen). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017C0014_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico Seneca kitchen USD 0.069m. Supports misc_mexico_seneca_kitchen_69k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68526.96; date_signed 2017-09-27.",
)

row_doc(
    "procunsa_ecuador_sanitary_drain_50k_2025",
    "resources", "water", "other",
    "Procunsa — Ecuador sanitary drain building repair",
    "Ecuador",
    "6 May 2025: Department of State awards contract 19EC3025P0381 to Procunsa S.A.S. for sanitary drain building repair (PoP Ecuador); obligated USD 49,983.60. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "49983.60", "2025-05-06", "2025", "", "",
    "Sanitary drain building repair, Ecuador (USASpending description; building not named — lat/lon blank).",
    "usaspending_procunsa_ecuador_sanitary_drain_50k_2025",
    "SANITARY DRAIN  BUILDING REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3025P0381_1900_-NONE-_-NONE-/",
    "Actor: Procunsa S.A.S. (Ecuador) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1051",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3025P0381_1900_-NONE-_-NONE- (Procunsa Ecuador sanitary). Signed 2025-05-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3025P0381_1900_-NONE-_-NONE-/.",
    "USASpending: Procunsa Ecuador sanitary USD 0.050m. Supports procunsa_ecuador_sanitary_drain_50k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49983.60; date_signed 2025-05-06.",
)

row_doc(
    "proyectos_colombia_800m_range_71k_2012",
    "infrastructure", "engineering_epc", "other",
    "Proyectos Civiles S y M — Colombia construction of 800m range",
    "Colombia",
    "21 Mar 2012: Department of Defense awards contract W913FT12P0076 to Proyectos Civiles S y M Limitada for construction of 800m range (PoP Colombia); obligated USD 70,656.40. CapEx face = award obligation. Exact range site unnamed — lat/lon blank.",
    "70656.40", "2012-03-21", "2012", "", "",
    "Construction of 800m range, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_proyectos_colombia_800m_range_71k_2012",
    "001 CONSTRUCTION OF 800M RANGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0076_9700_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Colombia) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1051",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0076_9700_-NONE-_-NONE- (Colombia 800m range). Signed 2012-03-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0076_9700_-NONE-_-NONE-/.",
    "USASpending: Colombia 800m range USD 0.071m. Supports proyectos_colombia_800m_range_71k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 70656.40; date_signed 2012-03-21.",
)

# === Cycle 1052 (seed 20262052) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "miyamoto_haiti_hospital_analysis_45k_2012",
    "infrastructure", "engineering_epc", "us",
    "Miyamoto International — Haiti HUEH hospital structural analysis",
    "Haiti",
    "24 Feb 2012: USAID awards contract AID521O1200049 to Miyamoto International Inc for HUEH structural analysis of hospital building to determine feasibility of remodeling (PoP Haiti); obligated USD 45,000. CapEx face = award obligation.",
    "45000", "2012-02-24", "2012", "18.539", "-72.335",
    "HUEH hospital structural analysis for remodel feasibility, Haiti (USASpending description; HUEH hospital named).",
    "usaspending_miyamoto_haiti_hospital_analysis_45k_2012",
    "HUEH STRUCTURAL ANALYSIS OF HOSPITAL BUILDING TO  DETERMINE FEASIBILITY OF REMODELING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O1200049_7200_-NONE-_-NONE-/",
    "Actor: Miyamoto International Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx. Haiti under-covered weight.",
    "hunt_cycle1052",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521O1200049_7200_-NONE-_-NONE- (Miyamoto Haiti HUEH). Signed 2012-02-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O1200049_7200_-NONE-_-NONE-/.",
    "USASpending: Miyamoto Haiti HUEH USD 0.045m. Supports miyamoto_haiti_hospital_analysis_45k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 45000; date_signed 2012-02-24.",
)

row_doc(
    "wiss_barbados_seismicity_47k_2016",
    "infrastructure", "engineering_epc", "us",
    "Wiss Janney Elstner — Barbados Bridgetown limited seismicity study",
    "Barbados",
    "25 Aug 2016: Department of State awards order SAQMMA16F3651 to Wiss Janney Elstner Associates Inc for Bridgetown limited seismicity (PoP Barbados); obligated USD 47,291. CapEx face = award obligation.",
    "47291", "2016-08-25", "2016", "13.097", "-59.613",
    "Limited seismicity study, Bridgetown, Barbados (USASpending description; Bridgetown named).",
    "usaspending_wiss_barbados_seismicity_47k_2016",
    "IGF::OT::IGF THIS TASK ORDER PROVIDES FUNDING FOR BRIDGETOWN LIMITED SEISMICITY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F3651_1900_SAQMMA14D0021_1900/",
    "Actor: Wiss Janney Elstner Associates Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1052",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F3651_1900_SAQMMA14D0021_1900 (Wiss Barbados seismicity). Signed 2016-08-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F3651_1900_SAQMMA14D0021_1900/.",
    "USASpending: Wiss Barbados seismicity USD 0.047m. Supports wiss_barbados_seismicity_47k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47291; date_signed 2016-08-25.",
)

row_doc(
    "misc_brazil_rso_fences_69k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil RSO make-ready fences",
    "Brazil",
    "8 Sep 2020: Department of State awards contract 19BR2520P0716 for RSO make ready fences (PoP Brazil); obligated USD 68,575.79. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "68575.79", "2020-09-08", "2020", "", "",
    "RSO make-ready fences, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_rso_fences_69k_2020",
    "RSO - MAKE READY - FENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0716_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1052",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0716_1900_-NONE-_-NONE- (Brazil RSO fences). Signed 2020-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0716_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil RSO fences USD 0.069m. Supports misc_brazil_rso_fences_69k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68575.79; date_signed 2020-09-08.",
)

row_doc(
    "misc_dr_pv_equipment_68k_2021",
    "energy", "other_renewables", "other",
    "Miscellaneous foreign awardees — Dominican Republic NEC photovoltaic equipment replacement",
    "Dominican Republic",
    "8 Sep 2021: Department of State awards contract 19DR8621P1357 for photovoltaic equipment replacement and repairs NEC (PoP Dominican Republic); obligated USD 67,855.50. CapEx face = award obligation. Recipient redacted; exact NEC site unnamed — lat/lon blank.",
    "67855.50", "2021-09-08", "2021", "", "",
    "Photovoltaic equipment replacement and repairs at NEC, Dominican Republic (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dr_pv_equipment_68k_2021",
    "PHOTOVOLTAIC EQUIPMENT REPLACEMENT AND REPAIRS NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8621P1357_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle other_renewables.",
    "hunt_cycle1052",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8621P1357_1900_-NONE-_-NONE- (DR PV equipment). Signed 2021-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8621P1357_1900_-NONE-_-NONE-/.",
    "USASpending: DR PV equipment USD 0.068m. Supports misc_dr_pv_equipment_68k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67855.50; date_signed 2021-09-08.",
)

row_doc(
    "misc_haiti_cjtf_fence_68k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti CJTF-Haiti HQ fence site prep",
    "Haiti",
    "12 Mar 2010: Department of Defense awards contract W912CL10M9005 for site prep for DJC2 (fence) CJTF-Haiti HQ (PoP Haiti); obligated USD 68,023.80. CapEx face = award obligation. Exact HQ site unnamed — lat/lon blank.",
    "68023.80", "2010-03-12", "2010", "", "",
    "Fence site prep for CJTF-Haiti HQ, Haiti (USASpending description; HQ not named — lat/lon blank).",
    "usaspending_misc_haiti_cjtf_fence_68k_2010",
    "SITE PREP FOR DJC2 (FENCE)CJTF-HAITI HQ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10M9005_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Haiti under-covered weight.",
    "hunt_cycle1052",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10M9005_9700_-NONE-_-NONE- (Haiti CJTF fence). Signed 2010-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10M9005_9700_-NONE-_-NONE-/.",
    "USASpending: Haiti CJTF fence USD 0.068m. Supports misc_haiti_cjtf_fence_68k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68023.80; date_signed 2010-03-12.",
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
