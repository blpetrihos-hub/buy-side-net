#!/usr/bin/env python3
"""Cycles 933–935: USASpending residual Brazil/DR/Nicaragua/Ecuador/Argentina.

Seeds: 20261933–20261935. Thin top-up dry.
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


# === 933 ===
row_doc(
    "hardline_kingston_febr_2p88m_2017",
    "infrastructure", "building_materials", "us",
    "Hardline Nati Construction LLC — Kingston FEBR repair and replacement",
    "Jamaica",
    "18 Sep 2017: Department of State awards task order SAQMMA17F3617 to Hardline Nati Construction "
    "LLC for FEBR repair and replacement at U.S. Embassy Kingston, Jamaica; obligated USD "
    "2,884,039.76. CapEx face = award obligation. Distinct from hardline_lapaz_febr_1p77m_2016 / "
    "tabcon_kingston_nec_roof_6p02m_2024.",
    "2884039.76", "2017-09-18", "2017", "18.018", "-76.810",
    "FEBR repair/replacement, U.S. Embassy Kingston, Jamaica (USASpending PoP Jamaica).",
    "usaspending_hardline_kingston_febr_20170918",
    "FEBR REPAIR AND REPLACEMENT PROJECT - KINGSTON US EMBASSY KINGSTON, JAMAICA   IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F3617_1900_SAQMMA14D0085_1900/",
    "Actor: Hardline Nati Construction LLC (U.S./College Park) under State — us. Official "
    "USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle933",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA17F3617_1900_SAQMMA14D0085_1900 (Hardline; Kingston FEBR). Signed 18 September "
    "2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F3617_1900_SAQMMA14D0085_1900/.",
    "USASpending: Hardline Kingston FEBR USD 2.884m. Supports hardline_kingston_febr_2p88m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,884,039.76; date_signed 2017-09-18.",
)
row_doc(
    "tidewater_managua_db_1p96m_2021",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. — Managua embassy design/build construction",
    "Nicaragua",
    "28 Jan 2021: Department of State awards task order 19AQMM21F0534 to Tidewater, Inc. for "
    "design/build construction project at U.S. Embassy Managua; obligated USD 1,962,338.05. CapEx "
    "face = award obligation. Distinct from tidewater_managua_consular_6p27m_2025.",
    "1962338.05", "2021-01-28", "2021", "12.136", "-86.251",
    "Design/build construction, U.S. Embassy Managua, Nicaragua (USASpending PoP Nicaragua).",
    "usaspending_tidewater_managua_db_20210128",
    "CONTRACT AWARD FOR DESIGN/BUILD CONSTRUCTION PROJECT AT US EMBASSY - MANAGUA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0534_1900_SAQMMA14D0045_1900/",
    "Actor: Tidewater, Inc. (U.S./Elkridge) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle933",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM21F0534_1900_SAQMMA14D0045_1900 (Tidewater; Managua DB). Signed 28 January 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0534_1900_SAQMMA14D0045_1900/.",
    "USASpending: Tidewater Managua DB USD 1.962m. Supports tidewater_managua_db_1p96m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,962,338.05; date_signed 2021-01-28.",
)
row_doc(
    "palgag_managua_roof_1p50m_2024",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd — Managua roof replacement",
    "Nicaragua",
    "20 Sep 2024: Department of State awards contract 19GE5024C0047 to Palgag Building Technologies "
    "Ltd for roof replacement project (PoP Nicaragua); obligated USD 1,499,254.30. CapEx face = "
    "award obligation. Distinct from palgag_namru6_lima_25p4m_2018 / roofing_resources_managua.",
    "1499254.30", "2024-09-20", "2024", "12.136", "-86.251",
    "Roof replacement, U.S. Embassy Managua, Nicaragua (USASpending PoP Nicaragua).",
    "usaspending_palgag_managua_roof_20240920",
    "ROOF REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0047_1900_-NONE-_-NONE-/",
    "Actor: Palgag Building Technologies Ltd (Israel) under State — allied. Official USASpending "
    "Award API. Shuffle building_materials.",
    "hunt_cycle933",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5024C0047_1900_-NONE-_-NONE- (Palgag; Managua roof). Signed 20 September 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0047_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag Managua roof USD 1.499m. Supports palgag_managua_roof_1p50m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,499,254.30; date_signed 2024-09-20.",
)
row_doc(
    "edifice_quito_reno_3p45m_2016",
    "infrastructure", "building_materials", "us",
    "Edifice Worldwide LLC — Quito renovation",
    "Ecuador",
    "29 Sep 2016: Department of State awards task order SAQMMA16F5591 to Edifice Worldwide LLC for "
    "Quito renovation; obligated USD 3,446,328.01. CapEx face = award obligation. Distinct from "
    "edifice_montevideo_msgr_3p63m_2018 / oes_quito_fe_br_1p27m_2012.",
    "3446328.01", "2016-09-29", "2016", "-0.180", "-78.468",
    "Renovation, Quito, Ecuador (USASpending PoP Ecuador).",
    "usaspending_edifice_quito_reno_20160929",
    "QUITO RENOVATION  IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5591_1900_SAQMMA14D0048_1900/",
    "Actor: Edifice Worldwide LLC (U.S./Beltsville) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle933",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA16F5591_1900_SAQMMA14D0048_1900 (Edifice; Quito renovation). Signed 29 September "
    "2016. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5591_1900_SAQMMA14D0048_1900/.",
    "USASpending: Edifice Quito renovation USD 3.446m. Supports edifice_quito_reno_3p45m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,446,328.01; date_signed 2016-09-29.",
)
row_doc(
    "serrano_bariloche_eoc_3p50m_2024",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño Diseño y Construcción — Bariloche/El Bolsón firefighting EOC",
    "Argentina",
    "27 Sep 2024: USACE awards task order W9127824F0366 to Serrano Proaño Diseño y Construcción S.A. "
    "for design and construction of National Firefighting Emergency Operations Center, Bariloche, "
    "El Bolsón, Argentina; obligated USD 3,495,027.63. CapEx face = award obligation.",
    "3495027.63", "2024-09-27", "2024", "-41.134", "-71.310",
    "National firefighting EOC, Bariloche / El Bolsón, Argentina (USASpending PoP Argentina; "
    "Bariloche pin).",
    "usaspending_serrano_bariloche_eoc_20240927",
    "DESIGN AND CONSTRUCTION OF NATIONAL FIREFIGHTING EMERGENCY OPERATIONS CENTER, BARILOCHE, EL "
    "BOLSON, ARGENTINA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0366_9700_W9127823D0060_9700/",
    "Actor: Serrano Proaño Diseño y Construcción S.A. (Ecuador/Quito) under DoD/USACE — other. "
    "Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle933",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127824F0366_9700_W9127823D0060_9700 (Serrano; Bariloche EOC). Signed 27 September "
    "2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0366_9700_W9127823D0060_9700/.",
    "USASpending: Serrano Bariloche EOC USD 3.495m. Supports serrano_bariloche_eoc_3p50m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,495,027.63; date_signed 2024-09-27.",
)

# === 934 ===
row_doc(
    "naku_buenos_aires_cmr_2p15m_2010",
    "infrastructure", "building_materials", "other",
    "Naku Construcciones S.R.L. — Buenos Aires CMR renovation",
    "Argentina",
    "7 May 2010: Department of State awards contract SAQMMA10C0160 to Naku Construcciones S.R.L. for "
    "renovation of the Chief of Mission Residence, Buenos Aires; obligated USD 2,147,788.29. CapEx "
    "face = award obligation. Distinct from framaco_buenos_aires_dcmr / american_roofing_buenos_aires.",
    "2147788.29", "2010-05-07", "2010", "-34.604", "-58.382",
    "Chief of Mission Residence renovation, Buenos Aires, Argentina (USASpending PoP Argentina).",
    "usaspending_naku_buenos_aires_cmr_20100507",
    "RENOVATION OF THE CHIEF OF MISSION RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0160_1900_-NONE-_-NONE-/",
    "Actor: Naku Construcciones S.R.L. (Buenos Aires) under State — other. Official USASpending "
    "Award API. Shuffle building_materials.",
    "hunt_cycle934",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA10C0160_1900_-NONE-_-NONE- (Naku; Buenos Aires CMR). Signed 7 May 2010. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0160_1900_-NONE-_-NONE-/.",
    "USASpending: Naku Buenos Aires CMR USD 2.148m. Supports naku_buenos_aires_cmr_2p15m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,147,788.29; date_signed 2010-05-07.",
)
row_doc(
    "horizon_brasilia_cw_elec_5p56m_2017",
    "infrastructure", "engineering_epc", "us",
    "Horizon Construction Group / ICS JV — Brasília chilled water and electrical",
    "Brazil",
    "29 Sep 2017: Department of State awards task order SAQMMA17F4854 to Horizon Construction Group / "
    "International Construction Services JV for chilled water and electrical construction services, "
    "Brasília; obligated USD 5,556,543.11. CapEx face = award obligation. Distinct from "
    "horizon_costa_rica_msgr_6p37m_2019 / vistas_brasilia_db_6p96m_2012.",
    "5556543.11", "2017-09-29", "2017", "-15.797", "-47.892",
    "Chilled water and electrical construction, Brasília, Brazil (USASpending PoP Brazil).",
    "usaspending_horizon_brasilia_cw_20170929",
    "CONSTRUCTION SERVICES CHILLED WATER AND ELECTRICAL.  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F4854_1900_SAQMMA14D0056_1900/",
    "Actor: Horizon Construction Group / ICS JV (U.S./Memphis) under State — us. Official "
    "USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle934",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA17F4854_1900_SAQMMA14D0056_1900 (Horizon; Brasília CW/elec). Signed 29 September "
    "2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F4854_1900_SAQMMA14D0056_1900/.",
    "USASpending: Horizon Brasília CW/elec USD 5.557m. Supports horizon_brasilia_cw_elec_5p56m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,556,543.11; date_signed 2017-09-29.",
)
row_doc(
    "tidewater_rio_esw_3p56m_2019",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. — Rio de Janeiro early site work construction",
    "Brazil",
    "5 Mar 2019: Department of State awards task order 19AQMM19F0936 to Tidewater, Inc. for Rio "
    "early site work construction; obligated USD 3,563,626.15. CapEx face = award obligation. "
    "Distinct from tidewater_sao_paulo_canopy_4p44m_2023.",
    "3563626.15", "2019-03-05", "2019", "-22.907", "-43.173",
    "Early site work construction, Rio de Janeiro, Brazil (USASpending PoP Brazil; Rio pin).",
    "usaspending_tidewater_rio_esw_20190305",
    "SERVICES - RIO EARLY SITE WORK CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0936_1900_SAQMMA14D0045_1900/",
    "Actor: Tidewater, Inc. (U.S./Elkridge) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle934",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM19F0936_1900_SAQMMA14D0045_1900 (Tidewater; Rio ESW). Signed 5 March 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0936_1900_SAQMMA14D0045_1900/.",
    "USASpending: Tidewater Rio ESW USD 3.564m. Supports tidewater_rio_esw_3p56m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,563,626.15; date_signed 2019-03-05.",
)
row_doc(
    "trison_recife_cac_2p94m_2024",
    "infrastructure", "building_materials", "us",
    "Trison Construction Inc. — Recife employee compound access control design-build",
    "Brazil",
    "23 Sep 2024: Department of State awards task order 19AQMM24F2048 to Trison Construction Inc. "
    "for design-build employee compound access control in Recife, Brazil; obligated USD "
    "2,939,894.92. CapEx face = award obligation. Distinct from trison_georgetown_p2_5p49m_2018.",
    "2939894.92", "2024-09-23", "2024", "-8.048", "-34.877",
    "Employee compound access control, Recife, Brazil (USASpending PoP Brazil; Recife pin).",
    "usaspending_trison_recife_cac_20240923",
    "DESIGN-BUILD SERVICES FOR AN EMPLOYEE COMPOUND ACCESS CONTROL IN RECIFE, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2048_1900_19AQMM22D0066_1900/",
    "Actor: Trison Construction Inc. (U.S./College Park) under State — us. Official USASpending "
    "Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle934",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F2048_1900_19AQMM22D0066_1900 (Trison; Recife CAC). Signed 23 September 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2048_1900_19AQMM22D0066_1900/.",
    "USASpending: Trison Recife CAC USD 2.940m. Supports trison_recife_cac_2p94m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,939,894.92; date_signed 2024-09-23.",
)
row_doc(
    "veyka_santo_domingo_slope_4p36m_2025",
    "infrastructure", "bridges_roads", "other",
    "Veyka İnşaat — Santo Domingo slope stabilization construction",
    "Dominican Republic",
    "30 Sep 2025: Department of State awards contract 19GE5025C0108 to Veyka İnşaat Mimarlık "
    "Mühendislik for construction services for slope stabilization (PoP Dominican Republic); "
    "obligated USD 4,360,315.84. CapEx face = award obligation.",
    "4360315.84", "2025-09-30", "2025", "18.486", "-69.931",
    "Slope stabilization construction, Santo Domingo, Dominican Republic (USASpending PoP Dominican "
    "Republic).",
    "usaspending_veyka_sd_slope_20250930",
    "CONSTRUCTION SERVICES FOR SLOPE STABILIZATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0108_1900_-NONE-_-NONE-/",
    "Actor: Veyka İnşaat (Turkey/Ankara) under State — other. Official USASpending Award API. "
    "Shuffle bridges_roads (slope stabilization civil works).",
    "hunt_cycle934",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5025C0108_1900_-NONE-_-NONE- (Veyka; Santo Domingo slope). Signed 30 September "
    "2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0108_1900_-NONE-_-NONE-/.",
    "USASpending: Veyka Santo Domingo slope USD 4.360m. Supports veyka_santo_domingo_slope_4p36m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,360,315.84; date_signed 2025-09-30.",
)

# === 935 ===
row_doc(
    "palgag_santo_domingo_hvac_2p49m_2024",
    "infrastructure", "building_materials", "allied",
    "Palgag — Z.G.S — Santo Domingo HVAC systems replacement engineer/build",
    "Dominican Republic",
    "30 Sep 2024: Department of State awards task order 19GE5024F0697 to Palgag — Z.G.S for "
    "engineer/build HVAC systems replacement (PoP Dominican Republic); obligated USD 2,493,924.66. "
    "CapEx face = award obligation. Distinct from palgag_managua_roof_1p50m_2024.",
    "2493924.66", "2024-09-30", "2024", "18.486", "-69.931",
    "HVAC systems replacement, Santo Domingo, Dominican Republic (USASpending PoP Dominican Republic).",
    "usaspending_palgag_sd_hvac_20240930",
    "ENGINEER/BUILD HVAC SYSTEMS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0697_1900_19GE5024D0051_1900/",
    "Actor: Palgag — Z.G.S (Israel) under State — allied. Official USASpending Award API. Shuffle "
    "building_materials.",
    "hunt_cycle935",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5024F0697_1900_19GE5024D0051_1900 (Palgag; Santo Domingo HVAC). Signed 30 "
    "September 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0697_1900_19GE5024D0051_1900/.",
    "USASpending: Palgag Santo Domingo HVAC USD 2.494m. Supports palgag_santo_domingo_hvac_2p49m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,493,924.66; date_signed 2024-09-30.",
)
row_doc(
    "spectrum_santo_domingo_elec_1p75m_2015",
    "infrastructure", "engineering_epc", "us",
    "Spectrum Electrical Services, Inc. — Santo Domingo electrical work",
    "Dominican Republic",
    "16 Apr 2015: Department of State awards task order SAQMMA15F1190 to Spectrum Electrical "
    "Services, Inc. for electrical work Santo Domingo, Dominican Republic; obligated USD "
    "1,754,631.42. CapEx face = award obligation. Distinct from spectrum Haiti switchgear residual.",
    "1754631.42", "2015-04-16", "2015", "18.486", "-69.931",
    "Electrical work, Santo Domingo, Dominican Republic (USASpending PoP Dominican Republic).",
    "usaspending_spectrum_sd_elec_20150416",
    "ELECTRICAL WORK SANTO DOMINGO, DOMINICAN REPUBLIC IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1190_1900_SAQMMA12D0194_1900/",
    "Actor: Spectrum Electrical Services, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle935",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA15F1190_1900_SAQMMA12D0194_1900 (Spectrum; Santo Domingo electrical). Signed 16 "
    "April 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1190_1900_SAQMMA12D0194_1900/.",
    "USASpending: Spectrum Santo Domingo elec USD 1.755m. Supports spectrum_santo_domingo_elec_1p75m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,754,631.42; date_signed 2015-04-16.",
)
row_doc(
    "bendig_sierpe_base_camp_1p41m_2022",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig S.A. — Sierpe base camp construction",
    "Costa Rica",
    "30 Sep 2022: Department of State awards contract 19AQMM22C0166 to Industrias Bendig S.A. for "
    "Sierpe base camp construction, Costa Rica; obligated USD 1,410,982.80. CapEx face = award "
    "obligation.",
    "1410982.80", "2022-09-30", "2022", "8.780", "-83.670",
    "Sierpe base camp construction, Puntarenas, Costa Rica (USASpending PoP Costa Rica; Sierpe pin).",
    "usaspending_bendig_sierpe_20220930",
    "SIERPE BASE CAMP CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0166_1900_-NONE-_-NONE-/",
    "Actor: Industrias Bendig S.A. (Costa Rica/Desamparados) under State — other. Official "
    "USASpending Award API. Shuffle building_materials.",
    "hunt_cycle935",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM22C0166_1900_-NONE-_-NONE- (Bendig; Sierpe base camp). Signed 30 September 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0166_1900_-NONE-_-NONE-/.",
    "USASpending: Bendig Sierpe base camp USD 1.411m. Supports bendig_sierpe_base_camp_1p41m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,410,982.80; date_signed 2022-09-30.",
)
row_doc(
    "kunkel_gamboa_b56_4p63m_2024",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction, Inc. — STRI Gamboa Building 56 refurbishment",
    "Panama",
    "11 Dec 2024: Smithsonian Institution awards contract 33330225CF0010042 to Kunkel Construction, "
    "Inc. for STRI Gamboa refurbishment of facilities — Building 56; obligated USD 4,632,417.78. "
    "CapEx face = award obligation.",
    "4632417.78", "2024-12-11", "2024", "9.117", "-79.700",
    "STRI Gamboa Building 56 refurbishment, Panama (USASpending PoP Panama; Gamboa pin).",
    "usaspending_kunkel_gamboa_b56_20241211",
    "STRI - GAMBOA REFURBISHMENT OF FACILITIES - BUILDING 56.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330225CF0010042_3300_-NONE-_-NONE-/",
    "Actor: Kunkel Construction, Inc. (Panama) under Smithsonian — other. Official USASpending "
    "Award API. Shuffle building_materials.",
    "hunt_cycle935",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_33330225CF0010042_3300_-NONE-_-NONE- (Kunkel; Gamboa B56). Signed 11 December 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330225CF0010042_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Gamboa B56 USD 4.632m. Supports kunkel_gamboa_b56_4p63m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,632,417.78; date_signed 2024-12-11.",
)
row_doc(
    "kunkel_tupper_4p19m_2019",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction, Inc. — STRI Tupper Building and site improvement",
    "Panama",
    "25 Mar 2019: Smithsonian Institution awards contract 33330219CF0010092 to Kunkel Construction, "
    "Inc. for construction services for the Tupper Bldg. and site improvement, Tupper Center, "
    "Panama City; obligated USD 4,185,425.03. CapEx face = award obligation. Distinct from "
    "kunkel_gamboa_b56_4p63m_2024.",
    "4185425.03", "2019-03-25", "2019", "8.982", "-79.520",
    "Tupper Building and site improvement, Panama City, Panama (USASpending PoP Panama).",
    "usaspending_kunkel_tupper_20190325",
    "CONSTRUCTION SERVICES FOR THE TUPPER BLDG. AND SITE IMPROVEMENT, TUPPER CENTER, PANAMA CITY, "
    "PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010092_3300_-NONE-_-NONE-/",
    "Actor: Kunkel Construction, Inc. (Panama) under Smithsonian — other. Official USASpending "
    "Award API. Shuffle building_materials.",
    "hunt_cycle935",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_33330219CF0010092_3300_-NONE-_-NONE- (Kunkel; Tupper). Signed 25 March 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010092_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Tupper USD 4.185m. Supports kunkel_tupper_4p19m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,185,425.03; date_signed 2019-03-25.",
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
    print(f"cycles933-935 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
