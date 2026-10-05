#!/usr/bin/env python3
"""Cycles 914–916: USASpending Haiti CapEx residual (ports, fire stations, A&E).

Seeds: 20261914–20261916. Thin top-up dry (balsa/nickel/fission/niobium).
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


def usa(
    rid,
    layer,
    sub,
    counterpart,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    sid,
    quote,
    url,
    note,
    hunt,
    chicago,
    annotation,
    evid_note,
    investment_type="epc",
    side="us",
    country="Haiti",
):
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": sub,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": "USD",
            "value_usd": value,
            "fx_usd": "1",
            "fx_date": fx_date,
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": "documented",
            "source_id": sid,
            "note": note,
            "pair_id": "",
            "counterpart_side": "",
            "counterpart_actor": "",
            "counterpart_value": "",
            "counterpart_currency": "",
            "counterpart_value_usd": "",
            "gap": "",
        },
        {
            "id": rid,
            "retrieved": "2026-10-05",
            "source_id": sid,
            "url": url,
            "price_year": year,
            "evidence": "documented",
            "quote": quote,
            "note": evid_note,
        },
        {
            "id": sid,
            "type": "government",
            "chicago": chicago,
            "url": url,
            "accessed": "2026-10-05",
            "annotation": annotation,
            "supports": [rid, hunt],
        },
    )


# === Cycle 914 ===
usa(
    "panexus_haiti_construction_17p1m_2013",
    "infrastructure", "building_materials",
    "Panexus Haiti S.A. — local construction project (State)",
    "12 Jul 2013: Department of State awards contract SAQMMA13C0174 to Panexus Haiti S.A. for "
    "local construction project in Haiti; obligated USD 17,056,105.00. CapEx face = award "
    "obligation. Distinct from palgag_us_modular_1p73m_2016 / dfs_fort_liberte_prison_6p74m_2014.",
    "17056105.00", "2013-07-12", "2013", "18.540", "-72.340",
    "Local construction project, Haiti (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_panexus_haiti_construction_20130712",
    "LOCAL CONSTRUCTION PROJECT HAITI IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0174_1900_-NONE-_-NONE-/",
    "Actor: Panexus Haiti S.A. (Port-au-Prince, Haiti) under State — other. Official USASpending "
    "Award API. Shuffle building_materials.",
    "hunt_cycle914",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13C0174_1900_-NONE-_-NONE- "
    "(Panexus Haiti S.A.; local construction). Signed 12 July 2013. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0174_1900_-NONE-_-NONE-/.",
    "USASpending: Panexus Haiti construction USD 17.056m. Supports panexus_haiti_construction_17p1m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17,056,105.00; recipient Haiti.",
    side="other",
)
usa(
    "northern_ports_feasibility_4p15m_2011",
    "infrastructure", "port_ownership",
    "USAID — feasibility study of northern ports in Haiti (domestic awardee undisclosed)",
    "23 Sep 2011: USAID awards task order AID521TO1100001 for feasibility study of northern ports "
    "in Haiti; obligated USD 4,154,181.54 (domestic awardee undisclosed). CapEx/services face = "
    "award obligation. Distinct from nathan_cap_haitien_customs_5p97m_2016 / "
    "nathan_cap_haitien_port_reg_3p07m_2015.",
    "4154181.54", "2011-09-23", "2011", "19.760", "-72.200",
    "Northern Haiti ports feasibility (USASpending PoP Haiti; Cap-Haïtien corridor approximate).",
    "usaspending_northern_ports_feasibility_20110923",
    "FEASIBILITY STUDY OF NORTHERN PORTS IN HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1100001_7200_AIDEDHI000800025_7200/",
    "Actor: USAID domestic awardee (undisclosed) — us. Official USASpending Award API. Shuffle "
    "port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle914",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_AID521TO1100001_7200_AIDEDHI000800025_7200 (northern ports feasibility). Signed 23 "
    "September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1100001_7200_AIDEDHI000800025_7200/.",
    "USASpending: northern ports feasibility USD 4.154m. Supports northern_ports_feasibility_4p15m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,154,181.54; date_signed 2011-09-23.",
    investment_type="services_contract",
)
usa(
    "sca_carrefour_cdb_fire_1p61m_2016",
    "infrastructure", "building_materials",
    "Strategic Consulting Alliances, LLC — Carrefour and Croix-des-Bouquets fire stations",
    "29 Sep 2016: DoD awards contract N6945016C0109 to Strategic Consulting Alliances, LLC to "
    "construct fire stations at Carrefour and Croix-des-Bouquets, Haiti; obligated USD 1,611,705.90. "
    "CapEx face = award obligation. Distinct from css_jacmel_eoc_drw_fs_2p13m_2011.",
    "1611705.90", "2016-09-29", "2016", "18.540", "-72.400",
    "Fire stations at Carrefour and Croix-des-Bouquets, Ouest, Haiti (USASpending PoP Haiti; "
    "Carrefour approximate).",
    "usaspending_sca_carrefour_cdb_fire_20160929",
    "CONSTRUCT FIRE STATION AT CARREFOUR AND CROIX DE BOUQUETS, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945016C0109_9700_-NONE-_-NONE-/",
    "Actor: Strategic Consulting Alliances, LLC (U.S.) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle914",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945016C0109_9700_-NONE-_-NONE- "
    "(SCA LLC; Carrefour/Croix-des-Bouquets fire stations). Signed 29 September 2016. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945016C0109_9700_-NONE-_-NONE-/.",
    "USASpending: SCA Carrefour/CdB fire stations USD 1.612m. Supports sca_carrefour_cdb_fire_1p61m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,611,705.90; date_signed 2016-09-29.",
)
usa(
    "olgoonik_recp_msg_ae_1p40m_2022",
    "infrastructure", "engineering_epc",
    "Olgoonik Federal, LLC — A&E for Marine Security Guard residence (Port-au-Prince)",
    "8 Jun 2022: Department of State awards contract 19AQMM22C0110 to Olgoonik Federal, LLC under "
    "Rapid Engineering Construction Program for A&E services for the Marine Security Guard "
    "residence in Port-au-Prince, Haiti; obligated USD 1,404,318.00. CapEx face = award obligation. "
    "Distinct from olgoonik_stecher_roumain_electrical_2p87m_2020.",
    "1404318.00", "2022-06-08", "2022", "18.540", "-72.340",
    "Marine Security Guard residence A&E, Port-au-Prince, Haiti (USASpending PoP Haiti).",
    "usaspending_olgoonik_recp_msg_20220608",
    "RAPID ENGINEERING CONSTRUCTION PROGRAM, THE PURPOSE OF THIS AWARD IS TO PROVIDE FUNDING FOR "
    "A&E SERVICES FOR THE MARINE SECURITY GUARD RESIDENCE IN PORT AU PRINCE HAITI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0110_1900_-NONE-_-NONE-/",
    "Actor: Olgoonik Federal, LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle914",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0110_1900_-NONE-_-NONE- "
    "(Olgoonik Federal; MSG residence A&E). Signed 8 June 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0110_1900_-NONE-_-NONE-/.",
    "USASpending: Olgoonik MSG A&E USD 1.404m. Supports olgoonik_recp_msg_ae_1p40m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,404,318.00; date_signed 2022-06-08.",
)
usa(
    "cap_haitien_urgent_port_ae_1p03m_2015",
    "infrastructure", "port_ownership",
    "USAID — A&E for urgent Cap-Haïtien port works (domestic awardee undisclosed)",
    "29 Sep 2015: USAID awards task order AID521TO1500006 to provide A&E services for urgent port "
    "works at Cap-Haïtien; obligated USD 1,028,361.67 (domestic awardee undisclosed). CapEx face = "
    "award obligation. Distinct from northern_ports_feasibility_4p15m_2011 / "
    "trigon_cap_haitien_cm_to_3p0m_2023.",
    "1028361.67", "2015-09-29", "2015", "19.759", "-72.201",
    "Urgent Cap-Haïtien port works A&E, Nord, Haiti (USASpending PoP Haiti; Cap-Haïtien port pin).",
    "usaspending_cap_haitien_urgent_port_ae_20150929",
    "THIS AWARD IS TO PROVIDE A&E SERVICES TO THE URGENT PORT WORKS AT CAP HAITIEN.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1500006_7200_AIDEDHI000800024_7200/",
    "Actor: USAID domestic awardee (undisclosed) — us. Official USASpending Award API. Shuffle "
    "port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle914",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_AID521TO1500006_7200_AIDEDHI000800024_7200 (Cap-Haïtien urgent port A&E). Signed 29 "
    "September 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1500006_7200_AIDEDHI000800024_7200/.",
    "USASpending: Cap-Haïtien urgent port A&E USD 1.028m. Supports cap_haitien_urgent_port_ae_1p03m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,028,361.67; date_signed 2015-09-29.",
)

# === Cycle 915 ===
usa(
    "annum_cmr_design_1p19m_2022",
    "infrastructure", "engineering_epc",
    "Annum Architects, Inc. — Chief of Mission Residence selective improvements design (PAP)",
    "23 Dec 2022: Department of State awards task order 19AQMM23F0220 to Annum Architects, Inc. "
    "for project development and design services for selective improvements to the Chief of "
    "Mission Residence (CMR) in Port-au-Prince, Haiti; obligated USD 1,190,416.00. CapEx face = "
    "award obligation. Distinct from olgoonik_recp_msg_ae_1p40m_2022.",
    "1190416.00", "2022-12-23", "2022", "18.540", "-72.340",
    "Chief of Mission Residence, Port-au-Prince, Haiti (USASpending PoP Haiti).",
    "usaspending_annum_cmr_design_20221223",
    "PROJECT DEVELOPMENT AND DESIGN SERVICES FOR A SELECTIVE IMPROVEMENTS PROJECT TO THE CHIEF OF "
    "MISSION RESIDENCE (CMR) IN PORT AU PRINCE, HAITI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0220_1900_19AQMM19D0059_1900/",
    "Actor: Annum Architects, Inc. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle915",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F0220_1900_19AQMM19D0059_1900 (Annum Architects; CMR design). Signed 23 "
    "December 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0220_1900_19AQMM19D0059_1900/.",
    "USASpending: Annum CMR design USD 1.190m. Supports annum_cmr_design_1p19m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,190,416.00; date_signed 2022-12-23.",
)
usa(
    "futurenet_haiti_cm_1p39m_2011",
    "infrastructure", "engineering_epc",
    "FutureNet Group, Inc. — Haiti engineering technicians and construction managers",
    "12 Sep 2011: DoD awards task order JM01 to FutureNet Group, Inc. for Haiti engineering "
    "technicians (2) and construction managers (2); obligated USD 1,392,374.21. CapEx/services "
    "face = award obligation. Distinct from trigon_cap_haitien_cm_to_3p0m_2023.",
    "1392374.21", "2011-09-12", "2011", "18.540", "-72.340",
    "Haiti engineering/CM staffing (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_futurenet_haiti_cm_20110912",
    "HAITI- ENGINEERING TECHNICIANS (2) AND CONSTRUCTION MANAGERS (2)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_JM01_9700_N0017809D5730_9700/",
    "Actor: FutureNet Group, Inc. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle915",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_JM01_9700_N0017809D5730_9700 "
    "(FutureNet Group; Haiti engineering/CM). Signed 12 September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_JM01_9700_N0017809D5730_9700/.",
    "USASpending: FutureNet Haiti CM USD 1.392m. Supports futurenet_haiti_cm_1p39m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,392,374.21; date_signed 2011-09-12.",
    investment_type="services_contract",
)
usa(
    "edh_electrical_connection_1p03m_2007",
    "energy", "power_plants_grid",
    "Électricité d'Haïti (EDH) — electrical connection construction services",
    "29 Jan 2007: Department of State awards contract SWHARC07M0025 to Électricité d'Haïti to "
    "provide construction services for connecting and providing electrical power; obligated USD "
    "1,034,013.36. CapEx face = award obligation. Distinct from "
    "spectrum_haiti_switchgear_7p02m_2021 / uep_chp_electrical_renewal_4p67m_2023.",
    "1034013.36", "2007-01-29", "2007", "18.540", "-72.340",
    "EDH electrical connection works, Haiti (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_edh_electrical_20070129",
    "THIS PROJECT ENTAILS ALL PLANT, LABOR, MATERIALS, ETC. NECESSARY FOR ELECTRICITY OF HAITI TO "
    "PROVIDE CONSTRUCTION SERVICES FOR THE PURPOSE OF CONNECTING AND PROVIDING ELECTRICAL PO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC07M0025_1900_-NONE-_-NONE-/",
    "Actor: Électricité d'Haïti (Haitian utility) under State — other. Official USASpending Award "
    "API. Shuffle power_plants_grid.",
    "hunt_cycle915",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC07M0025_1900_-NONE-_-NONE- "
    "(Électricité d'Haïti; electrical connection). Signed 29 January 2007. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC07M0025_1900_-NONE-_-NONE-/.",
    "USASpending: EDH electrical connection USD 1.034m. Supports edh_electrical_connection_1p03m_2007.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,034,013.36; recipient Haiti.",
    side="other",
)
usa(
    "slsco_gonaives_fire_ems_722k_2011",
    "infrastructure", "building_materials",
    "SLSCO, Ltd. — Gonaïves fire station / EMS",
    "18 Aug 2011: DoD awards contract N6945011C0064 to SLSCO, Ltd. for fire station / EMS in "
    "Gonaïves, Haiti; obligated USD 722,460.33. CapEx face = award obligation. Distinct from "
    "palgag_gonaives_clusters_3p55m_2011 / css_jacmel_eoc_drw_fs_2p13m_2011.",
    "722460.33", "2011-08-18", "2011", "19.450", "-72.690",
    "Fire station / EMS, Gonaïves, Artibonite, Haiti (USASpending PoP Haiti; Gonaïves pin).",
    "usaspending_slsco_gonaives_fire_20110818",
    "FIRE STATION / EMS FOR GONAIVES, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0064_9700_-NONE-_-NONE-/",
    "Actor: SLSCO, Ltd. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle915",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0064_9700_-NONE-_-NONE- "
    "(SLSCO; Gonaïves fire/EMS). Signed 18 August 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0064_9700_-NONE-_-NONE-/.",
    "USASpending: SLSCO Gonaïves fire/EMS USD 0.722m. Supports slsco_gonaives_fire_ems_722k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 722,460.33; date_signed 2011-08-18.",
)
usa(
    "css_les_cayes_fire_719k_2011",
    "infrastructure", "building_materials",
    "CSS International Holdings, Inc. — Les Cayes fire station",
    "20 Sep 2011: DoD awards contract N6945011C0062 to CSS International Holdings, Inc. for fire "
    "station in Les Cayes, Haiti; obligated USD 719,162.92. CapEx face = award obligation. "
    "Distinct from gdg_les_cayes_drw_1p19m_2010 / css_jacmel_eoc_drw_fs_2p13m_2011.",
    "719162.92", "2011-09-20", "2011", "18.200", "-73.750",
    "Fire station, Les Cayes, Sud, Haiti (USASpending PoP Haiti; Les Cayes pin).",
    "usaspending_css_les_cayes_fire_20110920",
    "FIRE STATION LES CAYES, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0062_9700_-NONE-_-NONE-/",
    "Actor: CSS International Holdings, Inc. (U.S.) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle915",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0062_9700_-NONE-_-NONE- "
    "(CSS; Les Cayes fire station). Signed 20 September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0062_9700_-NONE-_-NONE-/.",
    "USASpending: CSS Les Cayes fire station USD 0.719m. Supports css_les_cayes_fire_719k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 719,162.92; date_signed 2011-09-20.",
)

# === Cycle 916 ===
usa(
    "css_cap_haitien_fire_ems_707k_2011",
    "infrastructure", "building_materials",
    "CSS International Holdings, Inc. — Cap-Haïtien fire station / EMS",
    "23 Aug 2011: DoD awards contract N6945011C0065 to CSS International Holdings, Inc. for fire "
    "station / EMS in Cap-Haïtien, Haiti; obligated USD 706,562.92. CapEx face = award obligation. "
    "Distinct from css_jacmel_eoc_drw_fs_2p13m_2011 / gdg_cap_haitien_drw_1p27m_2010.",
    "706562.92", "2011-08-23", "2011", "19.760", "-72.200",
    "Fire station / EMS, Cap-Haïtien, Nord, Haiti (USASpending PoP Haiti; Cap-Haïtien pin).",
    "usaspending_css_cap_haitien_fire_20110823",
    "FIRE STATION / EMS CAP HAITIAN, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0065_9700_-NONE-_-NONE-/",
    "Actor: CSS International Holdings, Inc. (U.S.) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle916",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0065_9700_-NONE-_-NONE- "
    "(CSS; Cap-Haïtien fire/EMS). Signed 23 August 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0065_9700_-NONE-_-NONE-/.",
    "USASpending: CSS Cap-Haïtien fire/EMS USD 0.707m. Supports css_cap_haitien_fire_ems_707k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 706,562.92; date_signed 2011-08-23.",
)
usa(
    "ycf_jeremie_fire_ems_663k_2011",
    "infrastructure", "building_materials",
    "YCF Group — Jérémie fire station / EMS",
    "27 Sep 2011: DoD awards contract N6945011C0061 to YCF Group for fire station / EMS in "
    "Jérémie, Haiti; obligated USD 663,418.74. CapEx face = award obligation. Distinct from "
    "css_les_cayes_fire_719k_2011.",
    "663418.74", "2011-09-27", "2011", "18.650", "-74.120",
    "Fire station / EMS, Jérémie, Grand'Anse, Haiti (USASpending PoP Haiti; Jérémie pin).",
    "usaspending_ycf_jeremie_fire_20110927",
    "FIRE STATION / EMS- JEREMIE HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0061_9700_-NONE-_-NONE-/",
    "Actor: YCF Group (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle916",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0061_9700_-NONE-_-NONE- "
    "(YCF Group; Jérémie fire/EMS). Signed 27 September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0061_9700_-NONE-_-NONE-/.",
    "USASpending: YCF Jérémie fire/EMS USD 0.663m. Supports ycf_jeremie_fire_ems_663k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 663,418.74; date_signed 2011-09-27.",
)
usa(
    "newco_haiti_eoc_569k_2009",
    "infrastructure", "building_materials",
    "Newco Structures Inc. — Haiti Emergency Operations Center construction",
    "26 Sep 2009: DoD awards contract W912CL09C0032 to Newco Structures Inc. for construction of "
    "EOC in Haiti; obligated USD 569,038.52. CapEx face = award obligation. Distinct from "
    "css_jacmel_eoc_drw_fs_2p13m_2011.",
    "569038.52", "2009-09-26", "2009", "18.540", "-72.340",
    "Emergency Operations Center, Haiti (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_newco_haiti_eoc_20090926",
    "CONSTRUCTION OF EOC  IN HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL09C0032_9700_-NONE-_-NONE-/",
    "Actor: Newco Structures Inc. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle916",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL09C0032_9700_-NONE-_-NONE- "
    "(Newco Structures; Haiti EOC). Signed 26 September 2009. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL09C0032_9700_-NONE-_-NONE-/.",
    "USASpending: Newco Haiti EOC USD 0.569m. Supports newco_haiti_eoc_569k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 569,038.52; date_signed 2009-09-26.",
)
usa(
    "newco_haiti_drw_465k_2009",
    "infrastructure", "building_materials",
    "Newco Structures Inc. — Haiti Disaster Relief Warehouse",
    "24 Sep 2009: DoD awards contract W912CL09C0040 to Newco Structures Inc. for Disaster Relief "
    "Warehouse in Haiti; obligated USD 464,770.10. CapEx face = award obligation. Distinct from "
    "gdg_cap_haitien_drw_1p27m_2010 / newco_haiti_eoc_569k_2009.",
    "464770.10", "2009-09-24", "2009", "18.540", "-72.340",
    "Disaster Relief Warehouse, Haiti (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_newco_haiti_drw_20090924",
    "DISASTER RELIEF WAREHOUSE HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL09C0040_9700_-NONE-_-NONE-/",
    "Actor: Newco Structures Inc. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle916",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL09C0040_9700_-NONE-_-NONE- "
    "(Newco Structures; Haiti DRW). Signed 24 September 2009. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL09C0040_9700_-NONE-_-NONE-/.",
    "USASpending: Newco Haiti DRW USD 0.465m. Supports newco_haiti_drw_465k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 464,770.10; date_signed 2009-09-24.",
)
usa(
    "nathan_port_infra_ta_559k_2014",
    "infrastructure", "port_ownership",
    "Nathan Associates LLC — technical assistance for port infrastructure and operations planning",
    "4 Sep 2014: USAID awards contract AID521C1400014 to Nathan Associates LLC for technical "
    "assistance for port infrastructure and operations planning and project support in Haiti; "
    "obligated USD 558,625.15. CapEx/services face = award obligation. Distinct from "
    "nathan_cap_haitien_customs_5p97m_2016 / nathan_cap_haitien_port_reg_3p07m_2015.",
    "558625.15", "2014-09-04", "2014", "18.540", "-72.340",
    "Haiti port infrastructure/operations TA (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_nathan_port_infra_ta_20140904",
    "TECHNICAL ASSISTANCE FOR PORT INFRASTRUCTURE AND OPERATIONS PLANNING AND PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1400014_7200_-NONE-_-NONE-/",
    "Actor: Nathan Associates LLC (U.S.) under USAID — us. Official USASpending Award API. Shuffle "
    "port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle916",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1400014_7200_-NONE-_-NONE- "
    "(Nathan Associates; port infrastructure TA). Signed 4 September 2014. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1400014_7200_-NONE-_-NONE-/.",
    "USASpending: Nathan port infrastructure TA USD 0.559m. Supports nathan_port_infra_ta_559k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 558,625.15; date_signed 2014-09-04.",
    investment_type="services_contract",
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
    added: list[str] = []

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
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycles914-916 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
