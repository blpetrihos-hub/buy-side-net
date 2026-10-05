#!/usr/bin/env python3
"""Cycles 942–944: USASpending page-3 LatAm CapEx residual.

Seeds: 20261942–20261944. Thin top-up dry.
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

row_doc(
    "vistas_recife_consular_1p04m_2012",
    "infrastructure", "building_materials", "us",
    "The Vistas Group Global Inc. \u2014 Recife consular expansion design-build",
    "Brazil",
    "20 Apr 2012: Department of State awards task order SAQMMA12F1463 to The Vistas Group Global Inc. for design-build consular expansion at U.S. Consulate Recife; obligated USD 1,039,218. CapEx face = award obligation. Distinct from trison_recife_cac_2p94m_2024.",
    "1039218", "2012-04-20", "2012", "-8.048", "-34.877",
    "Consular expansion, U.S. Consulate Recife, Brazil (USASpending PoP Brazil).",
    "usaspending_vistas_recife_consular_1p04m_2012",
    "DESIGN-BUILD SERVICES FOR CONSULAR EXPANSION PROJECT AT THE U.S. CONSULATE RECIFE, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1463_1900_SAQMMA08D0006_1900/",
    "Actor: Vistas Group (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle942",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F1463_1900_SAQMMA08D0006_1900 (Vistas Recife consular). Signed 2012-04-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1463_1900_SAQMMA08D0006_1900/.",
    "USASpending: Vistas Recife consular USD 1.039m. Supports vistas_recife_consular_1p04m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1039218; date_signed 2012-04-20.",
)

row_doc(
    "desbuild_rio_consular_elec_810k_2015",
    "infrastructure", "engineering_epc", "us",
    "Desbuild Incorporated \u2014 Rio de Janeiro consular residence electrical upgrade",
    "Brazil",
    "30 Sep 2015: Department of State awards task order SAQMMA15F4224 to Desbuild Incorporated for electrical upgrade at consular residence in Rio de Janeiro; obligated USD 810,334.06. CapEx face = award obligation.",
    "810334.06", "2015-09-30", "2015", "-22.907", "-43.173",
    "Consular residence electrical upgrade, Rio de Janeiro, Brazil (USASpending PoP Brazil).",
    "usaspending_desbuild_rio_consular_elec_810k_2015",
    "ELECTRICAL UPGRADE PROJECT AT CONSULAR RESIDENCE IN RIO DE JANEIRO IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F4224_1900_SAQMMA14D0063_1900/",
    "Actor: Desbuild (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle engineering_epc; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle942",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F4224_1900_SAQMMA14D0063_1900 (Desbuild Rio consular elec). Signed 2015-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F4224_1900_SAQMMA14D0063_1900/.",
    "USASpending: Desbuild Rio consular elec USD 0.810m. Supports desbuild_rio_consular_elec_810k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 810334.06; date_signed 2015-09-30.",
)

row_doc(
    "palgag_haiti_commissariats_4p40m_2013",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd \u2014 Vivy Michel & Martissant commissariat design-build",
    "Haiti",
    "5 Jul 2013: Department of State awards contract SAQMMA13C0126 to Palgag for design-build Vivy Michel and Martissant commissariats; obligated USD 4,404,721. CapEx face = award obligation.",
    "4404721", "2013-07-05", "2013", "18.540", "-72.339",
    "Vivy Michel & Martissant commissariats, Port-au-Prince area, Haiti (USASpending PoP Haiti).",
    "usaspending_palgag_haiti_commissariats_4p40m_2013",
    "IGF::OT::IGF DESIGN BUILD VIVY MICHEL COMMISSARIAT DESIGN BUILD MARTISSANT COMMISSARIAT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0126_1900_-NONE-_-NONE-/",
    "Actor: Palgag (Israel) \u2014 allied. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle942",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13C0126_1900_-NONE-_-NONE- (Palgag Haiti commissariats). Signed 2013-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0126_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag Haiti commissariats USD 4.405m. Supports palgag_haiti_commissariats_4p40m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4404721; date_signed 2013-07-05.",
)

row_doc(
    "edifice_hnp_academy_reno_4p11m_2014",
    "infrastructure", "building_materials", "us",
    "Edifice LLC \u2014 HNP Academy renovation",
    "Haiti",
    "25 Sep 2014: Department of State awards contract SAQMMA14C0194 to Edifice LLC for HNP Academy renovation; obligated USD 4,107,948.30. CapEx face = award obligation. Distinct from cce_hnp_academy_repairs_4p97m_2011.",
    "4107948.30", "2014-09-25", "2014", "18.540", "-72.339",
    "HNP Academy renovation, Haiti (USASpending PoP Haiti; Port-au-Prince pin).",
    "usaspending_edifice_hnp_academy_reno_4p11m_2014",
    "HNP ACADEMY RENOVATION. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0194_1900_-NONE-_-NONE-/",
    "Actor: Edifice LLC (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle942",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0194_1900_-NONE-_-NONE- (Edifice HNP Academy). Signed 2014-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0194_1900_-NONE-_-NONE-/.",
    "USASpending: Edifice HNP Academy USD 4.108m. Supports edifice_hnp_academy_reno_4p11m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4107948.30; date_signed 2014-09-25.",
)

row_doc(
    "seobra_colombia_arws_5p82m_2022",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras Seobra S.A.S. \u2014 72-pax ARWS quarters design and construction",
    "Colombia",
    "7 Feb 2022: USACE awards task order W9127822F0046 to Seobra for design and construction of 72-pax ARWS quarters; obligated USD 5,821,138. CapEx face = award obligation.",
    "5821138", "2022-02-07", "2022", "4.711", "-74.072",
    "72-pax ARWS quarters, Colombia (USASpending PoP Colombia; national pin).",
    "usaspending_seobra_colombia_arws_5p82m_2022",
    "DESIGN AND CONSTRUCTION OF 72PAX ARWS QUARTERS(CADD NO:SHA21001)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0046_9700_W9127817D0097_9700/",
    "Actor: Seobra (Colombia) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle942",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0046_9700_W9127817D0097_9700 (Seobra Colombia ARWS). Signed 2022-02-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0046_9700_W9127817D0097_9700/.",
    "USASpending: Seobra Colombia ARWS USD 5.821m. Supports seobra_colombia_arws_5p82m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5821138; date_signed 2022-02-07.",
)

row_doc(
    "eterna_callao_parking_2p56m_2023",
    "infrastructure", "building_materials", "other",
    "Eterna \u2014 Callao Naval Base parking lot design and construction",
    "Peru",
    "23 Feb 2023: USACE awards task order W9127823F0085 to Eterna for design and construction of parking lot at Callao Naval Base, Peru; obligated USD 2,562,573.56. CapEx face = award obligation. Distinct from aecom_callao_harbor_p2 / kgn_callao.",
    "2562573.56", "2023-02-23", "2023", "-12.051", "-77.126",
    "Parking lot, Callao Naval Base, Peru (USASpending PoP Peru).",
    "usaspending_eterna_callao_parking_2p56m_2023",
    "DESIGN AND CONSTRUCTION OF PARKING LOT IN CALLAO NAVAL BASE, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0085_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle943",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0085_9700_W9127817D0095_9700 (Eterna Callao parking). Signed 2023-02-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0085_9700_W9127817D0095_9700/.",
    "USASpending: Eterna Callao parking USD 2.563m. Supports eterna_callao_parking_2p56m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2562573.56; date_signed 2023-02-23.",
)

row_doc(
    "sea_pac_lima_elevator_2p00m_2021",
    "infrastructure", "engineering_epc", "us",
    "Sea Pac Engineering Inc. \u2014 Lima embassy elevator replacement design/build",
    "Peru",
    "24 Sep 2021: Department of State awards contract 19GE5021C0061 to Sea Pac for design/build elevator replacement (PoP Peru); obligated USD 1,999,811. CapEx face = award obligation.",
    "1999811", "2021-09-24", "2021", "-12.046", "-77.043",
    "Elevator replacement, U.S. Embassy Lima, Peru (USASpending PoP Peru).",
    "usaspending_sea_pac_lima_elevator_2p00m_2021",
    "DESIGN/BUILD ELEVATOR REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0061_1900_-NONE-_-NONE-/",
    "Actor: Sea Pac (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle engineering_epc; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle943",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0061_1900_-NONE-_-NONE- (Sea Pac Lima elevator). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0061_1900_-NONE-_-NONE-/.",
    "USASpending: Sea Pac Lima elevator USD 2.000m. Supports sea_pac_lima_elevator_2p00m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1999811; date_signed 2021-09-24.",
)

row_doc(
    "eei_fort_sherman_1p63m_2025",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones e Interventor\u00eda \u2014 Fort Sherman multiuse training facility",
    "Panama",
    "5 Sep 2025: USACE awards task order W9127825F0164 to EEI for Fort Sherman multiuse training facility; obligated USD 1,625,676.83. CapEx face = award obligation.",
    "1625676.83", "2025-09-05", "2025", "9.367", "-79.950",
    "Fort Sherman multiuse training facility, Panama (USASpending PoP Panama).",
    "usaspending_eei_fort_sherman_1p63m_2025",
    "FORT SHERMAN MULTIUSE TRAINING FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0164_9700_W9127823D0058_9700/",
    "Actor: EEI (Colombia) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle943",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825F0164_9700_W9127823D0058_9700 (EEI Fort Sherman). Signed 2025-09-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0164_9700_W9127823D0058_9700/.",
    "USASpending: EEI Fort Sherman USD 1.626m. Supports eei_fort_sherman_1p63m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1625676.83; date_signed 2025-09-05.",
)

row_doc(
    "eterna_panama_maritime_1p54m_2022",
    "infrastructure", "building_materials", "other",
    "Eterna \u2014 Panama maritime training facility",
    "Panama",
    "29 Sep 2022: USACE awards task order W9127822F0428 to Eterna for maritime training facility base bid; obligated USD 1,543,118.16. CapEx face = award obligation.",
    "1543118.16", "2022-09-29", "2022", "8.982", "-79.520",
    "Maritime training facility, Panama (USASpending PoP Panama; Panama City pin).",
    "usaspending_eterna_panama_maritime_1p54m_2022",
    "MARITIME TRAINING FACILITY BASE BID",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0428_9700_W9127821D0075_9700/",
    "Actor: Eterna (Honduras) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle943",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0428_9700_W9127821D0075_9700 (Eterna Panama maritime). Signed 2022-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0428_9700_W9127821D0075_9700/.",
    "USASpending: Eterna Panama maritime USD 1.543m. Supports eterna_panama_maritime_1p54m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1543118.16; date_signed 2022-09-29.",
)

row_doc(
    "kunkel_gamboa_shop_1p33m_2024",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction \u2014 Gamboa maintenance shop construction",
    "Panama",
    "16 Sep 2024: Smithsonian awards contract 33330224CF0010461 to Kunkel for construction of a maintenance shop at Gamboa; obligated USD 1,331,754.09. CapEx face = award obligation. Distinct from kunkel_gamboa_b56.",
    "1331754.09", "2024-09-16", "2024", "9.117", "-79.700",
    "Maintenance shop, Gamboa, Panama (USASpending PoP Panama).",
    "usaspending_kunkel_gamboa_shop_1p33m_2024",
    "CONSTRUCTION OF A MAINTENANCE SHOP, LOCATED AT GAMBOA, REPUBLIC OF PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330224CF0010461_3300_-NONE-_-NONE-/",
    "Actor: Kunkel (Panama) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle943",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330224CF0010461_3300_-NONE-_-NONE- (Kunkel Gamboa shop). Signed 2024-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330224CF0010461_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Gamboa shop USD 1.332m. Supports kunkel_gamboa_shop_1p33m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1331754.09; date_signed 2024-09-16.",
)

row_doc(
    "tidewater_tegucigalpa_nec_esw_1p88m_2017",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. \u2014 Tegucigalpa NEC early site work",
    "Honduras",
    "26 Oct 2017: Department of State awards task order 19AQMM18F0034 to Tidewater for early site work for New Embassy Compound Tegucigalpa; obligated USD 1,878,127.98. CapEx face = award obligation.",
    "1878127.98", "2017-10-26", "2017", "14.072", "-87.192",
    "NEC early site work, Tegucigalpa, Honduras (USASpending PoP Honduras).",
    "usaspending_tidewater_tegucigalpa_nec_esw_1p88m_2017",
    "TASK ORDER AWARD FOR EARLY SITE WORK FOR THE NEW EMBASSY COMPOUND (NEC) IN TEGUCIGALPA, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F0034_1900_SAQMMA14D0045_1900/",
    "Actor: Tidewater (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle944",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F0034_1900_SAQMMA14D0045_1900 (Tidewater Tegucigalpa NEC ESW). Signed 2017-10-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F0034_1900_SAQMMA14D0045_1900/.",
    "USASpending: Tidewater Tegucigalpa NEC ESW USD 1.878m. Supports tidewater_tegucigalpa_nec_esw_1p88m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1878127.98; date_signed 2017-10-26.",
)

row_doc(
    "civing_san_antonio_bridge_1p84m_2013",
    "infrastructure", "bridges_roads", "other",
    "Civing S.A. de C.V. \u2014 San Antonio Bridge IDA construction",
    "El Salvador",
    "4 Jun 2013: USAID awards contract AID519C1300003 to Civing for IDA San Antonio Bridge construction; obligated USD 1,842,174.75. CapEx face = award obligation. Distinct from omni_acahuapa_bridge.",
    "1842174.75", "2013-06-04", "2013", "13.700", "-89.200",
    "San Antonio Bridge construction, El Salvador (USASpending PoP El Salvador; approximate pin).",
    "usaspending_civing_san_antonio_bridge_1p84m_2013",
    "IGF::CT::IGF - IDA SAN ANTONIO BRIDGE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID519C1300003_7200_-NONE-_-NONE-/",
    "Actor: Civing (El Salvador) \u2014 other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle944",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID519C1300003_7200_-NONE-_-NONE- (Civing San Antonio bridge). Signed 2013-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID519C1300003_7200_-NONE-_-NONE-/.",
    "USASpending: Civing San Antonio bridge USD 1.842m. Supports civing_san_antonio_bridge_1p84m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1842174.75; date_signed 2013-06-04.",
)

row_doc(
    "palgag_el_salvador_roof_1p59m_2026",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd \u2014 El Salvador roof replacement",
    "El Salvador",
    "20 Mar 2026: Department of State awards contract 19GE5026C0025 to Palgag for construction \u2014 roof replacement (PoP El Salvador); obligated USD 1,594,583. CapEx face = award obligation.",
    "1594583", "2026-03-20", "2026", "13.693", "-89.219",
    "Roof replacement, El Salvador diplomatic facilities (USASpending PoP El Salvador; San Salvador pin).",
    "usaspending_palgag_el_salvador_roof_1p59m_2026",
    "CONSTRUCTION - ROOF REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0025_1900_-NONE-_-NONE-/",
    "Actor: Palgag (Israel) \u2014 allied. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle944",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0025_1900_-NONE-_-NONE- (Palgag El Salvador roof). Signed 2026-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0025_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag El Salvador roof USD 1.595m. Supports palgag_el_salvador_roof_1p59m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1594583; date_signed 2026-03-20.",
)

row_doc(
    "akj_enaproc_5p70m_2024",
    "infrastructure", "building_materials", "other",
    "Servicios AKJ, S.A. de C.V. \u2014 ENAPROC facility construction",
    "Mexico",
    "25 Apr 2024: DoD awards contract W912DQ24C4008 to Servicios AKJ for ENAPROC facility; obligated USD 5,704,916.53. CapEx face = award obligation.",
    "5704916.53", "2024-04-25", "2024", "19.433", "-99.133",
    "ENAPROC facility, Mexico (USASpending PoP Mexico; national pin).",
    "usaspending_akj_enaproc_5p70m_2024",
    "ENAPROC FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DQ24C4008_9700_-NONE-_-NONE-/",
    "Actor: Servicios AKJ (Mexico) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle944",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912DQ24C4008_9700_-NONE-_-NONE- (AKJ ENAPROC). Signed 2024-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DQ24C4008_9700_-NONE-_-NONE-/.",
    "USASpending: AKJ ENAPROC USD 5.705m. Supports akj_enaproc_5p70m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5704916.53; date_signed 2024-04-25.",
)

row_doc(
    "bonatti_champerico_school_1p22m_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Champerico school design and construction",
    "Guatemala",
    "11 Sep 2025: USACE awards task order W9127825FA179 to Bonatti for design and construction of HAP 83563 school at Champerico, Guatemala; obligated USD 1,222,363.90. CapEx face = award obligation.",
    "1222363.90", "2025-09-11", "2025", "14.300", "-91.917",
    "School design/construction, Champerico, Guatemala (USASpending PoP Guatemala).",
    "usaspending_bonatti_champerico_school_1p22m_2025",
    "DESIGN AND CONSTRUCTION OF THE HAP 83563 SCHOOL AT CHAMPERICO, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA179_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle944",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA179_9700_W9127823D0072_9700 (Bonatti Champerico school). Signed 2025-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA179_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Champerico school USD 1.222m. Supports bonatti_champerico_school_1p22m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1222363.90; date_signed 2025-09-11.",
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
    print(f"cycles942-944 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
