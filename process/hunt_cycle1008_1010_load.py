#!/usr/bin/env python3
"""Cycles 1008–1010: USASpending LatAm CapEx residual (~USD0.11–0.15m).

Seeds: 20262008–20262010. Thin top-up dry. Includes Nicaragua MCAC retention.
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

# === Cycle 1008 ===
row_doc(
    "eei_colombia_asphalt_154k_2026",
    "infrastructure", "bridges_roads", "other",
    "Estudios Edificaciones e Interventoría — Colombia compound perimeter path asphalt",
    "Colombia",
    "22 Sep 2026: Department of State awards contract 19C02026C0010 to Estudios Edificaciones e Interventoría for compound perimeter path asphalt repairs (PoP Colombia); obligated USD 154,362.93. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "154362.93", "2026-09-22", "2026", "", "",
    "Compound perimeter path asphalt repairs, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_eei_colombia_asphalt_154k_2026",
    "PR16301567:X3003 COMPOUND PERIMETER PATH ASPHALT REPA..",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0010_1900_-NONE-_-NONE-/",
    "Actor: Estudios Edificaciones e Interventoría (Colombia) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1008",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02026C0010_1900_-NONE-_-NONE- (EEI Colombia asphalt). Signed 2026-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0010_1900_-NONE-_-NONE-/.",
    "USASpending: EEI Colombia asphalt USD 0.154m. Supports eei_colombia_asphalt_154k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 154362.93; date_signed 2026-09-22.",
)

row_doc(
    "eterna_helo_ramp_154k_2011",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Soto Cano helo ramp pavement repair",
    "Honduras",
    "13 Sep 2011: DoD awards task order 0025 under W9127809D0071 to Empresa de Construcción y Transporte Eterna for repair pavement in helo ramp, Soto Cano Air Base, Honduras; obligated USD 153,505.66. CapEx face = award obligation.",
    "153505.66", "2011-09-13", "2011", "14.382", "-87.621",
    "Helo ramp pavement repair, Soto Cano Air Base, Honduras (USASpending description).",
    "usaspending_eterna_helo_ramp_154k_2011",
    "TAS::21 2020::TAS REPAIR PAVEMENT IN HELO RAMP, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0025_9700_W9127809D0071_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (San Pedro Sula) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1008",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0025_9700_W9127809D0071_9700 (Eterna Soto Cano helo ramp). Signed 2011-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0025_9700_W9127809D0071_9700/.",
    "USASpending: Eterna Soto Cano helo ramp USD 0.154m. Supports eterna_helo_ramp_154k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 153505.66; date_signed 2011-09-13.",
)

row_doc(
    "atlas_edeze_gousse_school_150k_2014",
    "infrastructure", "building_materials", "other",
    "Atlas Construction — Edeze Gousse school renovation Haiti",
    "Haiti",
    "6 Mar 2014: USAID awards BPA call AID521BC1400010 to Atlas Construction to renovate the Edeze Gousse school (PoP Haiti); obligated USD 149,859.47. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "149859.47", "2014-03-06", "2014", "", "",
    "Edeze Gousse school renovation, Haiti (USASpending PoP Haiti; site not named — lat/lon blank).",
    "usaspending_atlas_edeze_gousse_school_150k_2014",
    "IGF::OT::IGF - THE PURPOSE OF THIS BPA CALL IS RENOVATE THE EDEZE GOUSSE SCHOOL UNDER THE BLANKET PURCHASE AGREEMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1400010_7200_AID521E1200002_7200/",
    "Actor: Atlas Construction (Haiti) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1008",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521BC1400010_7200_AID521E1200002_7200 (Atlas Edeze Gousse school). Signed 2014-03-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1400010_7200_AID521E1200002_7200/.",
    "USASpending: Atlas Edeze Gousse school USD 0.150m. Supports atlas_edeze_gousse_school_150k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 149859.47; date_signed 2014-03-06.",
)

row_doc(
    "atlas_hueh_maternity_149k_2012",
    "infrastructure", "building_materials", "other",
    "Atlas Construction — HUEH maternity ward rehabilitation Haiti",
    "Haiti",
    "18 Oct 2012: USAID awards BPA call AID521BC1300001 to Atlas Construction to rehabilitate the maternity ward of HUEH (waterproofing roof, painting, rewiring, doors/windows) (PoP Haiti); obligated USD 149,403. CapEx face = award obligation.",
    "149403", "2012-10-18", "2012", "18.540", "-72.340",
    "Maternity ward rehabilitation, Hôpital Universitaire d’État d’Haïti (HUEH), Port-au-Prince (USASpending description).",
    "usaspending_atlas_hueh_maternity_149k_2012",
    "THE PURPOSE OF THIS BPA CALL IS TO REHABILITATE THE MATERNITY WARD OF HUEH BY WATERPROOFING THE ROOF, PAINTING THE CEILING AND WALLS OF THE ENTIRE BUILDING, REWIRING ELECTRICITY AS NEEDED, AND FIXING DOORS AND WINDOWS IN ORDER SUPPORT THE MINISTRY OF HEALTH AND POPULATION (MSPP) IN ITS EFFORTS TO PROVIDE COMFORTABLE HEALTHCARE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1300001_7200_AID521E1200002_7200/",
    "Actor: Atlas Construction (Haiti) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1008",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521BC1300001_7200_AID521E1200002_7200 (Atlas HUEH maternity). Signed 2012-10-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1300001_7200_AID521E1200002_7200/.",
    "USASpending: Atlas HUEH maternity USD 0.149m. Supports atlas_hueh_maternity_149k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 149403; date_signed 2012-10-18.",
)

row_doc(
    "cym_ancon_bathrooms_149k_2021",
    "infrastructure", "building_materials", "other",
    "Construcciones y Mantenimientos Eficientes — STRI Ancon apartments bathroom refurbish",
    "Panama",
    "26 Aug 2021: Smithsonian awards contract 33330221CF0010410 to Construcciones y Mantenimientos Eficientes for refurbish bathrooms at STRI Ancon apartments; obligated USD 148,811.50. CapEx face = award obligation.",
    "148811.50", "2021-08-26", "2021", "8.960", "-79.550",
    "Bathroom refurbishment, STRI Ancon apartments, Panama (USASpending / Smithsonian).",
    "usaspending_cym_ancon_bathrooms_149k_2021",
    "DM-BM182021/REFURBISH BATHROOMS AT STRI ANCON APARTMENTS:  TO SERVICE LABOR, MAT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010410_3300_-NONE-_-NONE-/",
    "Actor: Construcciones y Mantenimientos Eficientes (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1008",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330221CF0010410_3300_-NONE-_-NONE- (CYM Ancon bathrooms). Signed 2021-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010410_3300_-NONE-_-NONE-/.",
    "USASpending: CYM Ancon bathrooms USD 0.149m. Supports cym_ancon_bathrooms_149k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 148811.50; date_signed 2021-08-26.",
)


# === Cycle 1009 ===
row_doc(
    "misc_argentina_obc_basement_147k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina OBC basement remodel",
    "Argentina",
    "28 Sep 2018: Department of State awards contract 19AR2018C0008 for basement remodel at OBC (PoP Argentina); obligated USD 147,485.01. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "147485.01", "2018-09-28", "2018", "", "",
    "OBC basement remodel, Argentina (USASpending PoP Argentina; site not named — lat/lon blank).",
    "usaspending_misc_argentina_obc_basement_147k_2018",
    "FAC - BASEMENT REMODEL AT OBC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1009",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018C0008_1900_-NONE-_-NONE- (Argentina OBC basement). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0008_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina OBC basement USD 0.147m. Supports misc_argentina_obc_basement_147k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 147485.01; date_signed 2018-09-28.",
)

row_doc(
    "bonatti_sosco_shootsouse_147k_2010",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — SOSCO shoothouse Soto Cano",
    "Honduras",
    "29 Sep 2010: USACE awards task order 0005 under W9127809D0064 to Bonatti Ingenieros for D/B SOSCO shoothouse facility, Soto Cano AB, Honduras; obligated USD 147,241.58. CapEx face = award obligation.",
    "147241.58", "2010-09-29", "2010", "14.382", "-87.621",
    "SOSCO shoothouse facility, Soto Cano Air Base, Honduras (USASpending description).",
    "usaspending_bonatti_sosco_shootsouse_147k_2010",
    "D/B SOSCO SHOOTHOUSE FACILITY, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127809D0064_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos S.A. (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1009",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127809D0064_9700 (Bonatti SOSCO shoothouse). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127809D0064_9700/.",
    "USASpending: Bonatti SOSCO shoothouse USD 0.147m. Supports bonatti_sosco_shootsouse_147k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 147241.58; date_signed 2010-09-29.",
)

row_doc(
    "proksol_ayacucho_school_147k_2010",
    "infrastructure", "building_materials", "other",
    "Proksol — Ayacucho school Peru",
    "Peru",
    "30 Sep 2010: USACE awards task order 0003 under W9127809D0078 to Proksol for D/B Ayacucho school, Ayacucho, Peru; obligated USD 147,200.10. CapEx face = award obligation.",
    "147200.10", "2010-09-30", "2010", "-13.163", "-74.224",
    "Ayacucho school, Ayacucho, Peru (USASpending description).",
    "usaspending_proksol_ayacucho_school_147k_2010",
    "D/B AYACUCHO SCHOOL, AYACUCHO, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0078_9700/",
    "Actor: Proksol SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1009",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127809D0078_9700 (Proksol Ayacucho school). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0078_9700/.",
    "USASpending: Proksol Ayacucho school USD 0.147m. Supports proksol_ayacucho_school_147k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 147200.10; date_signed 2010-09-30.",
)

row_doc(
    "misc_fiemg_bh_renovation_146k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — FIEMG Belo Horizonte building renovation",
    "Brazil",
    "27 Jan 2014: Department of State awards contract SBR25014C0012 for FIEMG BH existing building inside renovation (PoP Brazil); obligated USD 146,489.09. CapEx face = award obligation. Recipient redacted.",
    "146489.09", "2014-01-27", "2014", "-19.920", "-43.940",
    "FIEMG building interior renovation, Belo Horizonte, Brazil (USASpending description).",
    "usaspending_misc_fiemg_bh_renovation_146k_2014",
    "FIEMG BH EXISTING BUILDING INSIDE RENOVATION IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25014C0012_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1009",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25014C0012_1900_-NONE-_-NONE- (FIEMG BH renovation). Signed 2014-01-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25014C0012_1900_-NONE-_-NONE-/.",
    "USASpending: FIEMG BH renovation USD 0.146m. Supports misc_fiemg_bh_renovation_146k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 146489.09; date_signed 2014-01-27.",
)

row_doc(
    "cda_antigua_fence_144k_2013",
    "infrastructure", "building_materials", "us",
    "CDA Solutions — Antigua fence and telemetry boresight antenna",
    "Antigua and Barbuda",
    "15 Feb 2013: DoD awards contract FA252113C0101 to CDA Solutions for construct fence, telemetry boresight antenna (PoP Antigua and Barbuda); obligated USD 144,317. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "144317", "2013-02-15", "2013", "", "",
    "Fence and telemetry boresight antenna construction, Antigua and Barbuda (USASpending PoP Antigua; site not named — lat/lon blank).",
    "usaspending_cda_antigua_fence_144k_2013",
    "CONSTRUCT FENCE, TELEMETRY BORESIGHT ANT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA252113C0101_9700_-NONE-_-NONE-/",
    "Actor: CDA Solutions, Inc. (West Melbourne FL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1009",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA252113C0101_9700_-NONE-_-NONE- (CDA Antigua fence). Signed 2013-02-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA252113C0101_9700_-NONE-_-NONE-/.",
    "USASpending: CDA Antigua fence USD 0.144m. Supports cda_antigua_fence_144k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 144317; date_signed 2013-02-15.",
)


# === Cycle 1010 ===
row_doc(
    "bonatti_poptun_fence_143k_2010",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Poptún fence installation Guatemala",
    "Guatemala",
    "28 Sep 2010: USACE awards task order 0003 under W9127809D0064 to Bonatti Ingenieros for installation of fence, Poptún, Guatemala; obligated USD 142,677.51. CapEx face = award obligation.",
    "142677.51", "2010-09-28", "2010", "16.330", "-89.420",
    "Fence installation, Poptún, Petén, Guatemala (USASpending description).",
    "usaspending_bonatti_poptun_fence_143k_2010",
    "INSTALLATION OF FENCE, POPTUM, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0064_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos S.A. (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1010",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127809D0064_9700 (Bonatti Poptún fence). Signed 2010-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0064_9700/.",
    "USASpending: Bonatti Poptún fence USD 0.143m. Supports bonatti_poptun_fence_143k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 142677.51; date_signed 2010-09-28.",
)

row_doc(
    "abeher_outdoor_storage_141k_2011",
    "infrastructure", "building_materials", "other",
    "Abeher — Panama outdoor storage facility",
    "Panama",
    "15 Jun 2011: DoD awards contract W912CL11C0025 to Abeher for outdoor storage facility (PoP Panama); obligated USD 141,113.14. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "141113.14", "2011-06-15", "2011", "", "",
    "Outdoor storage facility, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_abeher_outdoor_storage_141k_2011",
    "OUTDOOR STORAGE FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0025_9700_-NONE-_-NONE-/",
    "Actor: Abeher S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1010",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0025_9700_-NONE-_-NONE- (Abeher outdoor storage). Signed 2011-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0025_9700_-NONE-_-NONE-/.",
    "USASpending: Abeher outdoor storage USD 0.141m. Supports abeher_outdoor_storage_141k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 141113.14; date_signed 2011-06-15.",
)

row_doc(
    "misc_nicaragua_retention_133k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Nicaragua MCAC retention wall and metal fence",
    "Nicaragua",
    "28 Sep 2022: Department of State awards contract 19NU7022P0615 for construction of retention wall and metal fence outside MCAC (PoP Nicaragua); obligated USD 132,831.34. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "132831.34", "2022-09-28", "2022", "", "",
    "Retention wall and metal fence outside MCAC, Nicaragua (USASpending PoP Nicaragua; site not named — lat/lon blank).",
    "usaspending_misc_nicaragua_retention_133k_2022",
    "CONSTRUCTION OF RETENTION WALL AND METAL FENCE OUTSIDE MCAC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7022P0615_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials; Nicaragua under-covered.",
    "hunt_cycle1010",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NU7022P0615_1900_-NONE-_-NONE- (Nicaragua MCAC retention). Signed 2022-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7022P0615_1900_-NONE-_-NONE-/.",
    "USASpending: Nicaragua MCAC retention USD 0.133m. Supports misc_nicaragua_retention_133k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 132831.34; date_signed 2022-09-28.",
)

row_doc(
    "redguard_montevideo_112k_2025",
    "infrastructure", "building_materials", "us",
    "Redguard — Montevideo embassy mail screening facility container",
    "Uruguay",
    "30 Sep 2025: Department of State awards task order 19GE5025F0533 to Redguard for mail screening facility container for U.S. Embassy Montevideo, Uruguay; obligated USD 112,125. CapEx face = award obligation.",
    "112125", "2025-09-30", "2025", "-34.901", "-56.164",
    "Mail screening facility container, U.S. Embassy Montevideo, Uruguay (USASpending description).",
    "usaspending_redguard_montevideo_112k_2025",
    "MAIL SCREENING FACILITY CONTAINER FOR US EMBASSY MONTEVIDEO, URUGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025F0533_1900_19GE5023D0037_1900/",
    "Actor: Redguard LLC (Wichita KS, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1010",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5025F0533_1900_19GE5023D0037_1900 (Redguard Montevideo). Signed 2025-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025F0533_1900_19GE5023D0037_1900/.",
    "USASpending: Redguard Montevideo USD 0.112m. Supports redguard_montevideo_112k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 112125; date_signed 2025-09-30.",
)

row_doc(
    "carolina_water_paraguay_111k_2023",
    "resources", "water", "us",
    "Carolina Water Specialties — Paraguay portable water system",
    "Paraguay",
    "21 Apr 2023: Department of State awards contract 19PA1023C0003 to Carolina Water Specialties for FAC portable water system (PoP Paraguay); obligated USD 110,581.63. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "110581.63", "2023-04-21", "2023", "", "",
    "Portable water system, Paraguay (USASpending PoP Paraguay; site not named — lat/lon blank).",
    "usaspending_carolina_water_paraguay_111k_2023",
    "FAC - 7901 - PORTABLE WATER SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1023C0003_1900_-NONE-_-NONE-/",
    "Actor: Carolina Water Specialties LLC (South Carolina, U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1010",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1023C0003_1900_-NONE-_-NONE- (Carolina Water Paraguay). Signed 2023-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1023C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Carolina Water Paraguay USD 0.111m. Supports carolina_water_paraguay_111k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 110581.63; date_signed 2023-04-21.",
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
    print(f"cycles1008-1010 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
