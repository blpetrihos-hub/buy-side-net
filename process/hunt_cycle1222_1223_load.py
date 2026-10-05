#!/usr/bin/env python3
"""Cycles 1222–1223: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262222–20262223. Thin top-up dry.
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

# === Cycle 1222 ===
row_doc(
    "fabrication_designs_venezuela_msgq_window_glass_replace_3k_2014",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Venezuela MSGQ replacement window glass",
    "Venezuela",
    "8 Jul 2014: Department of State awards contract SVE30014M0396 to FABRICATION DESIGNS, INC. for MSGQ replacement window glass for the MSGQ residence (PoP Venezuela); obligated USD 3156. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "3156", "2014-07-08", "2014", "", "",
    "MSGQ replacement window glass for the MSGQ residence, Venezuela (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_fabrication_designs_venezuela_msgq_window_glass_replace_3k_2014",
    "MSGQ - REPLACEMENT WINDOW GLASS FOR THE MSGQ RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0396_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1222",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30014M0396_1900_-NONE-_-NONE- (fabrication_designs_venezuela_msgq_window_glass_replace_3k_2014). Signed 2014-07-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0396_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_venezuela_msgq_window_glass_replace_3k_2014 USD 0.003m. Supports fabrication_designs_venezuela_msgq_window_glass_replace_3k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3156.0; date_signed 2014-07-08.",
)

# === Cycle 1222 ===
row_doc(
    "fabrication_designs_mexico_metal_door_screen_3k_2021",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Mexico metal door screen",
    "Mexico",
    "16 Nov 2021: Department of State awards contract 19AQMM22P0031 to FABRICATION DESIGNS, INC. for Metal door screen etc. (PoP Mexico); obligated USD 3070.03. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3070.03", "2021-11-16", "2021", "", "",
    "Metal door screen etc., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_mexico_metal_door_screen_3k_2021",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0031_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1222",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0031_1900_-NONE-_-NONE- (fabrication_designs_mexico_metal_door_screen_3k_2021). Signed 2021-11-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0031_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_mexico_metal_door_screen_3k_2021 USD 0.003m. Supports fabrication_designs_mexico_metal_door_screen_3k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3070.03; date_signed 2021-11-16.",
)

# === Cycle 1222 ===
row_doc(
    "misc_mexico_cgr_back_patio_floor_replace_13k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico CGR back patio floor replacement",
    "Mexico",
    "26 Jul 2018: Department of State awards contract 19MX1118C0002 for CGR back patio floor replacement (PoP Mexico); obligated USD 12700.84. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12700.84", "2018-07-26", "2018", "", "",
    "CGR back patio floor replacement, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cgr_back_patio_floor_replace_13k_2018",
    "CGR BACK PATIO FLOOR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1118C0002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1222",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1118C0002_1900_-NONE-_-NONE- (misc_mexico_cgr_back_patio_floor_replace_13k_2018). Signed 2018-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1118C0002_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cgr_back_patio_floor_replace_13k_2018 USD 0.013m. Supports misc_mexico_cgr_back_patio_floor_replace_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12700.84; date_signed 2018-07-26.",
)

# === Cycle 1222 ===
row_doc(
    "misc_dominican_usms_office_generator_13k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic new generator for new USMS office offsite",
    "Dominican Republic",
    "26 Sep 2016: Department of State awards contract SDR86016M0931 for New generator for new USMS office offsite (PoP Dominican Republic); obligated USD 12700. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12700", "2016-09-26", "2016", "", "",
    "New generator for new USMS office offsite, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_usms_office_generator_13k_2016",
    "NEW GENERATOR NEEDED FOR NEW USMS OFFICE OFFSITE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86016M0931_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1222",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86016M0931_1900_-NONE-_-NONE- (misc_dominican_usms_office_generator_13k_2016). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86016M0931_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_usms_office_generator_13k_2016 USD 0.013m. Supports misc_dominican_usms_office_generator_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12700.0; date_signed 2016-09-26.",
)

# === Cycle 1222 ===
row_doc(
    "misc_colombia_torre95_apt301_make_ready_13k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Torre 95 apt 301 make-ready",
    "Colombia",
    "5 Apr 2024: Department of State awards contract 19C02024P0763 for Torre 95 X50033 apt 301 make-ready (PoP Colombia); obligated USD 12674.83. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12674.83", "2024-04-05", "2024", "", "",
    "Torre 95 X50033 apt 301 make-ready, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_torre95_apt301_make_ready_13k_2024",
    "PR12444810 - TORRE 95 X50033 APT 301 (MAINT & REP) MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P0763_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1222",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024P0763_1900_-NONE-_-NONE- (misc_colombia_torre95_apt301_make_ready_13k_2024). Signed 2024-04-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P0763_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_torre95_apt301_make_ready_13k_2024 USD 0.013m. Supports misc_colombia_torre95_apt301_make_ready_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12674.83; date_signed 2024-04-05.",
)

# === Cycle 1223 ===
row_doc(
    "norshield_mexico_metal_door_screen_2k_2016",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Mexico metal door screen",
    "Mexico",
    "19 Jan 2016: Department of State awards contract SAQMMA16M0244 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door, screen etc. (PoP Mexico); obligated USD 2425. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "2425", "2016-01-19", "2016", "", "",
    "Metal door, screen etc., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_mexico_metal_door_screen_2k_2016",
    "METAL DOOR, SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M0244_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1223",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M0244_1900_-NONE-_-NONE- (norshield_mexico_metal_door_screen_2k_2016). Signed 2016-01-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M0244_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_mexico_metal_door_screen_2k_2016 USD 0.002m. Supports norshield_mexico_metal_door_screen_2k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2425.0; date_signed 2016-01-19.",
)

# === Cycle 1223 ===
row_doc(
    "generac_jamaica_fire_brigade_light_tower_donation_3k_2011",
    "energy", "power_plants_grid", "us",
    "Generac Mobile Products — Jamaica HAP donation light tower to JA Fire Brigade #7",
    "Jamaica",
    "25 Mar 2011: Department of State awards contract SJM37011F0004 to GENERAC MOBILE PRODUCTS, LLC for HAP donation to JA Fire Brigade #7 (Generac light tower) (PoP Jamaica); obligated USD 3399.26. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "3399.26", "2011-03-25", "2011", "", "",
    "HAP donation to JA Fire Brigade #7 (Generac light tower), Jamaica (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_generac_jamaica_fire_brigade_light_tower_donation_3k_2011",
    "MLO - HAP PROJ #12671 - DONATION TO JA FIRE BRIGADE #7",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37011F0004_1900_GS07F0211M_4730/",
    "Actor: GENERAC MOBILE PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1223",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37011F0004_1900_GS07F0211M_4730 (generac_jamaica_fire_brigade_light_tower_donation_3k_2011). Signed 2011-03-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37011F0004_1900_GS07F0211M_4730/.",
    "USASpending: generac_jamaica_fire_brigade_light_tower_donation_3k_2011 USD 0.003m. Supports generac_jamaica_fire_brigade_light_tower_donation_3k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3399.26; date_signed 2011-03-25.",
)

# === Cycle 1223 ===
row_doc(
    "misc_ecuador_ups_electricity_shortages_13k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador UPS for electricity shortages",
    "Ecuador",
    "27 Sep 2024: Department of State awards contract 19EC3024P0638 for UPS for electricity shortages (PoP Ecuador); obligated USD 12609.75. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12609.75", "2024-09-27", "2024", "", "",
    "UPS for electricity shortages, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_ups_electricity_shortages_13k_2024",
    "UPS FOR ELECTRICITY SHORTAGES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3024P0638_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1223",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3024P0638_1900_-NONE-_-NONE- (misc_ecuador_ups_electricity_shortages_13k_2024). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3024P0638_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_ups_electricity_shortages_13k_2024 USD 0.013m. Supports misc_ecuador_ups_electricity_shortages_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12609.75; date_signed 2024-09-27.",
)

# === Cycle 1223 ===
row_doc(
    "misc_el_salvador_cctv_systems_cat_pnc_13k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador INL CCTV systems for CAT (PNC)",
    "El Salvador",
    "21 Apr 2021: Department of State awards contract 19ES6021P0442 for INL (2) CCTV systems for CAT (PNC) (PoP El Salvador); obligated USD 12594.62. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12594.62", "2021-04-21", "2021", "", "",
    "INL (2) CCTV systems for CAT (PNC), El Salvador (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_cctv_systems_cat_pnc_13k_2021",
    "INL - (2) CCTV SYSTEMS FOR CAT (PNC)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0442_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1223",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6021P0442_1900_-NONE-_-NONE- (misc_el_salvador_cctv_systems_cat_pnc_13k_2021). Signed 2021-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0442_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_cctv_systems_cat_pnc_13k_2021 USD 0.013m. Supports misc_el_salvador_cctv_systems_cat_pnc_13k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12594.62; date_signed 2021-04-21.",
)

# === Cycle 1223 ===
row_doc(
    "misc_mexico_dea_office_renovation_pb_13k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico office renovation PB level DEA",
    "Mexico",
    "26 Jul 2010: Department of State awards contract SMX53010M0601 for Office renovation PB level DEA Mex (PoP Mexico); obligated USD 12588.37. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12588.37", "2010-07-26", "2010", "", "",
    "Office renovation PB level DEA Mex, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_dea_office_renovation_pb_13k_2010",
    "OFFICE RENOVATION PB LEVEL DEA MEX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0601_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1223",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0601_1900_-NONE-_-NONE- (misc_mexico_dea_office_renovation_pb_13k_2010). Signed 2010-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0601_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_dea_office_renovation_pb_13k_2010 USD 0.013m. Supports misc_mexico_dea_office_renovation_pb_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12588.37; date_signed 2010-07-26.",
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
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
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
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
