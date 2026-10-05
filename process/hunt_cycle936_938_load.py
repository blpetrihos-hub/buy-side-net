#!/usr/bin/env python3
"""Cycles 936–938: USASpending page-2 LatAm CapEx residual.

Seeds: 20261936–20261938. Thin top-up dry.
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


# === 936 ===
row_doc(
    "emr_tijuana_msgr_9p60m_2015",
    "infrastructure", "building_materials", "us",
    "Enviro-Management & Research, Inc. — Tijuana MSGR base construction",
    "Mexico",
    "13 Mar 2015: Department of State awards contract SAQMMA15C0085 to Enviro-Management & Research, "
    "Inc. as base contract for Tijuana, Mexico Marine Security Guard Residence (MSGR); obligated "
    "USD 9,600,586.50. CapEx face = award obligation. Distinct from arkel_tijuana_msgr_14p5m_2021.",
    "9600586.50", "2015-03-13", "2015", "32.515", "-117.038",
    "MSGR base construction, Tijuana, Mexico (USASpending PoP Mexico).",
    "usaspending_emr_tijuana_msgr_20150313",
    "IGF::CL::IGF  BASE CONTRACT FOR TIJUANA, MEXICO MARINE SECURITY GUARD RESIDENCE (MSGR).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0085_1900_-NONE-_-NONE-/",
    "Actor: Enviro-Management & Research, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle936",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA15C0085_1900_-NONE-_-NONE- (EMR; Tijuana MSGR). Signed 13 March 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0085_1900_-NONE-_-NONE-/.",
    "USASpending: EMR Tijuana MSGR USD 9.601m. Supports emr_tijuana_msgr_9p60m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9,600,586.50; date_signed 2015-03-13.",
)
row_doc(
    "ics_lima_msgr_reno_5p47m_2018",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Lima off-compound MSGR renovation design/build",
    "Peru",
    "27 Sep 2018: Department of State awards task order 19AQMM18F4387 to International Construction "
    "Services for design/build renovation of existing off-compound USG-owned MSGR (PoP Peru); "
    "obligated USD 5,469,044.18. CapEx face = award obligation.",
    "5469044.18", "2018-09-27", "2018", "-12.046", "-77.043",
    "Off-compound MSGR renovation, Lima, Peru (USASpending PoP Peru).",
    "usaspending_ics_lima_msgr_20180927",
    "DESIGN/BUILD SERVICES FOR THE RENOVATION OF THE EXISTING OFF-COMPOUND USG OWNED MSGR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4387_1900_SAQMMA14D0059_1900/",
    "Actor: International Construction Services (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle936",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F4387_1900_SAQMMA14D0059_1900 (ICS; Lima MSGR). Signed 27 September 2018. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4387_1900_SAQMMA14D0059_1900/.",
    "USASpending: ICS Lima MSGR reno USD 5.469m. Supports ics_lima_msgr_reno_5p47m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,469,044.18; date_signed 2018-09-27.",
)
row_doc(
    "venesco_lima_ahu_5p25m_2023",
    "infrastructure", "building_materials", "us",
    "Venesco LLC — Lima embassy air handling unit replacement",
    "Peru",
    "18 Dec 2023: Department of State awards task order 19AQMM24F0140 to Venesco LLC for air "
    "handling replacement units at U.S. Embassy Lima, Peru; obligated USD 5,245,515.54. CapEx "
    "face = award obligation. Distinct from venesco_ciudad_juarez_msgr_16p5m_2017.",
    "5245515.54", "2023-12-18", "2023", "-12.046", "-77.043",
    "AHU replacement, U.S. Embassy Lima, Peru (USASpending PoP Peru).",
    "usaspending_venesco_lima_ahu_20231218",
    "AIR HANDLING REPLACEMENT UNITS AT U.S. EMBASSY LIMA PERU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0140_1900_19AQMM23D0015_1900/",
    "Actor: Venesco LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle936",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F0140_1900_19AQMM23D0015_1900 (Venesco; Lima AHU). Signed 18 December 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0140_1900_19AQMM23D0015_1900/.",
    "USASpending: Venesco Lima AHU USD 5.246m. Supports venesco_lima_ahu_5p25m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,245,515.54; date_signed 2023-12-18.",
)
row_doc(
    "eei_gorgona_colnav_pier_8p18m_2017",
    "infrastructure", "port_ownership", "other",
    "Estudios Edificaciones e Interventoría — ColNav pier Gorgona",
    "Colombia",
    "2 Feb 2017: Department of State awards contract SAQMMA17C0087 to Estudios Edificaciones e "
    "Interventoría for ColNav pier in Gorgona, Colombia; obligated USD 8,178,681.54. CapEx face = "
    "award obligation.",
    "8178681.54", "2017-02-02", "2017", "2.967", "-78.183",
    "ColNav pier, Isla Gorgona, Colombia (USASpending PoP Colombia; Gorgona pin).",
    "usaspending_eei_gorgona_pier_20170202",
    "COLNAV PIER IN GORGONA, COLUMBIA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0087_1900_-NONE-_-NONE-/",
    "Actor: Estudios Edificaciones e Interventoría (Colombia) under State — other. Official "
    "USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle936",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA17C0087_1900_-NONE-_-NONE- (EEI; Gorgona ColNav pier). Signed 2 February 2017. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0087_1900_-NONE-_-NONE-/.",
    "USASpending: EEI Gorgona pier USD 8.179m. Supports eei_gorgona_colnav_pier_8p18m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8,178,681.54; date_signed 2017-02-02.",
)
row_doc(
    "eterna_soto_cano_pv_8p14m_2018",
    "energy", "solar", "other",
    "Empresa de Construcción y Transporte Eterna — Soto Cano 2 MW PV solar farm",
    "Honduras",
    "14 Sep 2018: DoD awards contract W9127818C0023 to Empresa de Construcción y Transporte Eterna "
    "S.A. de C.V. to install 2 MW PV solar farm (PoP Honduras / Soto Cano); obligated USD "
    "8,140,715.16. CapEx face = award obligation.",
    "8140715.16", "2018-09-14", "2018", "14.382", "-87.621",
    "2 MW PV solar farm, Soto Cano Air Base, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_pv_20180914",
    "INSTALL 2MW PV SOLAR FARM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818C0023_9700_-NONE-_-NONE-/",
    "Actor: Eterna (Honduras/San Pedro Sula) under DoD — other. Official USASpending Award API. "
    "Shuffle solar.",
    "hunt_cycle936",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127818C0023_9700_-NONE-_-NONE- (Eterna; Soto Cano 2 MW PV). Signed 14 September "
    "2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818C0023_9700_-NONE-_-NONE-/.",
    "USASpending: Eterna Soto Cano PV USD 8.141m. Supports eterna_soto_cano_pv_8p14m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8,140,715.16; date_signed 2018-09-14.",
)

# === 937 ===
row_doc(
    "nbc_san_salvador_roof_5p68m_2018",
    "infrastructure", "building_materials", "us",
    "National Building Contractors, Inc. — San Salvador roofing project",
    "El Salvador",
    "18 Sep 2018: Department of State awards task order 19AQMM18F3908 to National Building "
    "Contractors, Inc. for San Salvador, El Salvador roofing project; obligated USD 5,675,994. "
    "CapEx face = award obligation. Distinct from ds_san_salvador_design_17p9m_2024.",
    "5675994", "2018-09-18", "2018", "13.693", "-89.219",
    "Roofing project, San Salvador, El Salvador (USASpending PoP El Salvador).",
    "usaspending_nbc_san_salvador_roof_20180918",
    "SAN SALVADOR, EL SALVADOR ROOFING PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F3908_1900_SAQMMA13D0134_1900/",
    "Actor: National Building Contractors, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle937",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F3908_1900_SAQMMA13D0134_1900 (NBC; San Salvador roof). Signed 18 September "
    "2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F3908_1900_SAQMMA13D0134_1900/.",
    "USASpending: NBC San Salvador roof USD 5.676m. Supports nbc_san_salvador_roof_5p68m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,675,994; date_signed 2018-09-18.",
)
row_doc(
    "tidewater_rio_cgr_2p47m_2022",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. — Rio de Janeiro Consulate General Residence renovation",
    "Brazil",
    "28 Sep 2022: Department of State awards task order 19AQMM22F4215 to Tidewater, Inc. for "
    "renovation of the Consulate General Residence in Rio de Janeiro, Brazil; obligated USD "
    "2,467,105.79. CapEx face = award obligation. Distinct from tidewater_rio_esw_3p56m_2019.",
    "2467105.79", "2022-09-28", "2022", "-22.907", "-43.173",
    "Consulate General Residence renovation, Rio de Janeiro, Brazil (USASpending PoP Brazil).",
    "usaspending_tidewater_rio_cgr_20220928",
    "RENOVATION OF THE CONSULATE GENERAL RESIDENCE IN RIO DE JANEIRO, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F4215_1900_19AQMM22D0058_1900/",
    "Actor: Tidewater, Inc. (U.S./Elkridge) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle937",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM22F4215_1900_19AQMM22D0058_1900 (Tidewater; Rio CGR). Signed 28 September 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F4215_1900_19AQMM22D0058_1900/.",
    "USASpending: Tidewater Rio CGR USD 2.467m. Supports tidewater_rio_cgr_2p47m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,467,105.79; date_signed 2022-09-28.",
)
row_doc(
    "framaco_bozdemir_lima_msg_3p52m_2022",
    "infrastructure", "building_materials", "us",
    "Framaco-Bozdemir JV — Lima MSG living areas renovation",
    "Peru",
    "27 Sep 2022: Department of State awards contract 19GE5022C0038 to Framaco-Bozdemir Joint Venture "
    "LLC for MSG living areas renovation (PoP Peru); obligated USD 3,515,967.73. CapEx face = "
    "award obligation. Distinct from ics_lima_msgr_reno_5p47m_2018 / framaco Barbados rows.",
    "3515967.73", "2022-09-27", "2022", "-12.046", "-77.043",
    "MSG living areas renovation, Lima, Peru (USASpending PoP Peru).",
    "usaspending_framaco_bozdemir_lima_msg_20220927",
    "MSG LIVING AREAS RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0038_1900_-NONE-_-NONE-/",
    "Actor: Framaco-Bozdemir JV (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle937",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5022C0038_1900_-NONE-_-NONE- (Framaco-Bozdemir; Lima MSG). Signed 27 September "
    "2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0038_1900_-NONE-_-NONE-/.",
    "USASpending: Framaco-Bozdemir Lima MSG USD 3.516m. Supports framaco_bozdemir_lima_msg_3p52m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,515,967.73; date_signed 2022-09-27.",
)
row_doc(
    "omni_acahuapa_bridge_4p29m_2013",
    "infrastructure", "bridges_roads", "other",
    "Inversiones Omni, S.A. de C.V. — Acahuapa Bridge IDA reconstruction",
    "El Salvador",
    "3 Dec 2013: USAID awards contract AID519C1400001 to Inversiones Omni, S.A. de C.V. for Acahuapa "
    "Bridge — IDA reconstruction; obligated USD 4,286,054.10. CapEx face = award obligation.",
    "4286054.10", "2013-12-03", "2013", "13.700", "-88.900",
    "Acahuapa Bridge reconstruction, El Salvador (USASpending PoP El Salvador; approximate corridor pin).",
    "usaspending_omni_acahuapa_bridge_20131203",
    "IGF::CL::IGF - ACAHUAPA BRIDGE - IDA RECONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID519C1400001_7200_-NONE-_-NONE-/",
    "Actor: Inversiones Omni, S.A. de C.V. (El Salvador) under USAID — other. Official USASpending "
    "Award API. Shuffle bridges_roads.",
    "hunt_cycle937",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_AID519C1400001_7200_-NONE-_-NONE- (Omni; Acahuapa Bridge). Signed 3 December 2013. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID519C1400001_7200_-NONE-_-NONE-/.",
    "USASpending: Omni Acahuapa Bridge USD 4.286m. Supports omni_acahuapa_bridge_4p29m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,286,054.10; date_signed 2013-12-03.",
)
row_doc(
    "eterna_soto_cano_bridge_7p64m_2021",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Soto Cano hurricane river repairs and vehicle bridge design-build",
    "Honduras",
    "28 Sep 2021: USACE awards task order W9127821F0444 to Eterna for design-build hurricane river "
    "repairs and vehicle bridge, Soto Cano Air Base, Honduras; obligated USD 7,636,503.85. CapEx "
    "face = award obligation. Distinct from eterna_soto_cano_pv_8p14m_2018.",
    "7636503.85", "2021-09-28", "2021", "14.382", "-87.621",
    "Hurricane river repairs + vehicle bridge, Soto Cano Air Base, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_bridge_20210928",
    "TASK ORDER FOR THE DESIGN-BUILD HURRICANE RIVER REPAIRS AND VEHICLE BRIDGE, SOTO CANO AIR BASE, "
    "HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0444_9700_W9127821D0075_9700/",
    "Actor: Eterna (Honduras) under DoD/USACE — other. Official USASpending Award API. Shuffle "
    "bridges_roads.",
    "hunt_cycle937",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127821F0444_9700_W9127821D0075_9700 (Eterna; Soto Cano bridge). Signed 28 September "
    "2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0444_9700_W9127821D0075_9700/.",
    "USASpending: Eterna Soto Cano bridge USD 7.637m. Supports eterna_soto_cano_bridge_7p64m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7,636,503.85; date_signed 2021-09-28.",
)

# === 938 ===
row_doc(
    "almeida_brasilia_cmr_2p56m_2020",
    "infrastructure", "building_materials", "other",
    "Almeida França Engenharia — Brasília CMR residence expansion",
    "Brazil",
    "30 Jun 2020: Department of State awards contract 19GE5020C0018 to Almeida França Engenharia "
    "Ltda for construction services CMR residence expansion project, Brasília, Brazil; obligated "
    "USD 2,556,808.90. CapEx face = award obligation.",
    "2556808.90", "2020-06-30", "2020", "-15.797", "-47.892",
    "CMR residence expansion, Brasília, Brazil (USASpending PoP Brazil).",
    "usaspending_almeida_brasilia_cmr_20200630",
    "BRASILIA, BRAZIL - CONSTRUCTION SERVICES CMR RESIDENCE EXPANSION PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020C0018_1900_-NONE-_-NONE-/",
    "Actor: Almeida França Engenharia Ltda (Brazil) under State — other. Official USASpending Award "
    "API. Shuffle building_materials.",
    "hunt_cycle938",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5020C0018_1900_-NONE-_-NONE- (Almeida França; Brasília CMR). Signed 30 June 2020. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020C0018_1900_-NONE-_-NONE-/.",
    "USASpending: Almeida Brasília CMR USD 2.557m. Supports almeida_brasilia_cmr_2p56m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,556,808.90; date_signed 2020-06-30.",
)
row_doc(
    "relyant_guatemala_ha_db_2p92m_2023",
    "infrastructure", "building_materials", "us",
    "Relyant Global LLC — Guatemala humanitarian assistance design-build construction",
    "Guatemala",
    "18 Sep 2023: USACE awards contract W9127823C0024 to Relyant Global LLC for two-phase "
    "design-build construction humanitarian assistance requirements in Guatemala; obligated USD "
    "2,924,261.98. CapEx face = award obligation.",
    "2924261.98", "2023-09-18", "2023", "14.635", "-90.507",
    "Humanitarian assistance design-build construction, Guatemala (USASpending PoP Guatemala; "
    "national pin).",
    "usaspending_relyant_guatemala_ha_20230918",
    "TWO-PHASE DESIGN-BUILD CONSTRUCTION \"C\" STANDALONE CONTRACT FOR HUMANITARIAN ASSISTANCE "
    "REQUIREMENTS IN GUATEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823C0024_9700_-NONE-_-NONE-/",
    "Actor: Relyant Global LLC (U.S.) under DoD/USACE — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle938",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127823C0024_9700_-NONE-_-NONE- (Relyant; Guatemala HA DB). Signed 18 September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823C0024_9700_-NONE-_-NONE-/.",
    "USASpending: Relyant Guatemala HA USD 2.924m. Supports relyant_guatemala_ha_db_2p92m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,924,261.98; date_signed 2023-09-18.",
)
row_doc(
    "torres_solola_municipal_1p80m_2024",
    "infrastructure", "building_materials", "other",
    "Torres In Situ S.A. — Sololá municipal building construction",
    "Guatemala",
    "6 Aug 2024: Department of State awards contract 19AQMM24C0084 to Torres In Situ Sociedad "
    "Anónima for Sololá municipal building construction; obligated USD 1,803,758.63. CapEx face = "
    "award obligation.",
    "1803758.63", "2024-08-06", "2024", "14.773", "-91.184",
    "Municipal building construction, Sololá, Guatemala (USASpending PoP Guatemala).",
    "usaspending_torres_solola_20240806",
    "SOLOLA MUNICIPAL BUILDING CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0084_1900_-NONE-_-NONE-/",
    "Actor: Torres In Situ S.A. (Guatemala) under State — other. Official USASpending Award API. "
    "Shuffle building_materials.",
    "hunt_cycle938",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24C0084_1900_-NONE-_-NONE- (Torres; Sololá municipal). Signed 6 August 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0084_1900_-NONE-_-NONE-/.",
    "USASpending: Torres Sololá municipal USD 1.804m. Supports torres_solola_municipal_1p80m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,803,758.63; date_signed 2024-08-06.",
)
row_doc(
    "eterna_chitre_eoc_1p68m_2021",
    "infrastructure", "building_materials", "other",
    "Eterna — Chitré Emergency Operations Center design and construction",
    "Panama",
    "8 Jun 2021: USACE awards task order W9127821F0182 to Eterna for design and construction of HAP "
    "#39626 Emergency Operations Center Chitré, Panama; obligated USD 1,676,066.66. CapEx face = "
    "award obligation.",
    "1676066.66", "2021-06-08", "2021", "7.987", "-80.430",
    "Emergency Operations Center, Chitré, Panama (USASpending PoP Panama).",
    "usaspending_eterna_chitre_eoc_20210608",
    "DESIGN AND CONSTRUCTION OF HAP #39626 EMERGENCY OPERATIONS CENTER CHITRE, PANAMA (CADD NO:",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0182_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) under DoD/USACE — other. Official USASpending Award API. Shuffle "
    "building_materials.",
    "hunt_cycle938",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127821F0182_9700_W9127816D0102_9700 (Eterna; Chitré EOC). Signed 8 June 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0182_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Chitré EOC USD 1.676m. Supports eterna_chitre_eoc_1p68m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,676,066.66; date_signed 2021-06-08.",
)
row_doc(
    "ect_santo_domingo_cmr_roof_665k_2023",
    "infrastructure", "building_materials", "us",
    "East Coast Technologies, LLC — Santo Domingo CMR roof replacement",
    "Dominican Republic",
    "21 Apr 2023: Department of State awards contract 19GE5023C0009 to East Coast Technologies, LLC "
    "for replacement of the roof on the Chief of Mission Residence of the U.S. Embassy Santo "
    "Domingo; obligated USD 664,776.09. CapEx face = award obligation.",
    "664776.09", "2023-04-21", "2023", "18.486", "-69.931",
    "CMR roof replacement, Santo Domingo, Dominican Republic (USASpending PoP Dominican Republic).",
    "usaspending_ect_sd_cmr_roof_20230421",
    "REPLACEMENT OF THE ROOF ON THE CHIEF OF MISSION RESIDENCE OF THE US EMBASSY SANTO DOMINGO,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0009_1900_-NONE-_-NONE-/",
    "Actor: East Coast Technologies, LLC (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle938",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5023C0009_1900_-NONE-_-NONE- (ECT; Santo Domingo CMR roof). Signed 21 April 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0009_1900_-NONE-_-NONE-/.",
    "USASpending: ECT Santo Domingo CMR roof USD 0.665m. Supports ect_santo_domingo_cmr_roof_665k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 664,776.09; date_signed 2023-04-21.",
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
    print(f"cycles936-938 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
