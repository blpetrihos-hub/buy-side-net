#!/usr/bin/env python3
"""Cycles 1149–1150: USASpending LatAm CapEx residual (~USD0.005–0.027m).

Seeds: 20262149–20262150. Thin top-up dry.
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


# === Cycle 1149 (seed 20262149) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_panama_metal_door_screen_14k_2019",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Panama metal door screen for international embassies",
    "Panama",
    "7 Mar 2019: Department of State awards contract 19AQMM19P0391 to Norshield Security Products, LLC for metal door screen etc. (PoP Panama); obligated USD 13,900. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "13900", "2019-03-07", "2019", "", "",
    "Metal door screen etc., Panama (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_panama_metal_door_screen_14k_2019",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0391_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1149",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0391_1900_-NONE-_-NONE- (norshield_panama_metal_door_screen_14k_2019). Signed 2019-03-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0391_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_panama_metal_door_screen_14k_2019 USD 0.014m. Supports norshield_panama_metal_door_screen_14k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13900; date_signed 2019-03-07.",
)
row_doc(
    "portable_air_group_mexico_portable_air_conditioner_14k_2013",
    "energy", "power_plants_grid", "us",
    "Portable Air Group — Mexico portable air conditioner",
    "Mexico",
    "30 May 2013: Department of Defense awards contract N0018913F0135 to Portable Air Group LLC for portable air conditioner (PoP Mexico); obligated USD 13,950. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13950", "2013-05-30", "2013", "", "",
    "Portable air conditioner, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_portable_air_group_mexico_portable_air_conditioner_14k_2013",
    "PORTABLE AIR CONDITIONER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0018913F0135_9700_GS06F0024T_4730/",
    "Actor: Portable Air Group LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1149",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N0018913F0135_9700_GS06F0024T_4730 (portable_air_group_mexico_portable_air_conditioner_14k_2013). Signed 2013-05-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0018913F0135_9700_GS06F0024T_4730/.",
    "USASpending: portable_air_group_mexico_portable_air_conditioner_14k_2013 USD 0.014m. Supports portable_air_group_mexico_portable_air_conditioner_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13950; date_signed 2013-05-30.",
)
row_doc(
    "misc_mexico_ice_juarez_cubicle_construction_27k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico ICE Juarez cubicle construction",
    "Mexico",
    "20 Aug 2010: Department of State awards contract SMX11510M0281 for 2010 ICE Juarez cubicle construction (PoP Mexico); obligated USD 27,000. CapEx face = award obligation. Juarez named; site coords not stated — lat/lon blank.",
    "27000", "2010-08-20", "2010", "", "",
    "ICE Juarez cubicle construction, Mexico (USASpending description; Juarez named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_ice_juarez_cubicle_construction_27k_2010",
    "2010 ICE JUAREZ CUBICLE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11510M0281_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1149",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11510M0281_1900_-NONE-_-NONE- (misc_mexico_ice_juarez_cubicle_construction_27k_2010). Signed 2010-08-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11510M0281_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_ice_juarez_cubicle_construction_27k_2010 USD 0.027m. Supports misc_mexico_ice_juarez_cubicle_construction_27k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27000; date_signed 2010-08-20.",
)
row_doc(
    "misc_argentina_goyena_windows_25k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Goyena windows",
    "Argentina",
    "12 Mar 2019: Department of State awards contract 19AR2019P0395 for FAC - Goyena - URG/windows (PoP Argentina); obligated USD 24,990.30. CapEx face = award obligation. Goyena named; site coords not stated — lat/lon blank.",
    "24990.3", "2019-03-12", "2019", "", "",
    "Goyena windows, Argentina (USASpending description; Goyena named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_goyena_windows_25k_2019",
    "FAC - GOYENA - URG/WINDOWS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2019P0395_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1149",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2019P0395_1900_-NONE-_-NONE- (misc_argentina_goyena_windows_25k_2019). Signed 2019-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2019P0395_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_goyena_windows_25k_2019 USD 0.025m. Supports misc_argentina_goyena_windows_25k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24990.3; date_signed 2019-03-12.",
)
row_doc(
    "ferreteria_epa_el_salvador_fap_air_conditioning_units_27k_2015",
    "energy", "power_plants_grid", "other",
    "Ferreteria EPA — El Salvador ICASS air conditioning units for FAP",
    "El Salvador",
    "23 Nov 2015: Department of State awards contract SES60016M0112 to Ferreteria EPA SA de CV for ICASS air conditioning units for FAP (PoP El Salvador); obligated USD 26,946.90. CapEx face = award obligation. FAP named; site coords not stated — lat/lon blank.",
    "26946.9", "2015-11-23", "2015", "", "",
    "ICASS air conditioning units for FAP, El Salvador (USASpending description; FAP named, site coords not stated — lat/lon blank).",
    "usaspending_ferreteria_epa_el_salvador_fap_air_conditioning_units_27k_2015",
    "(ICASS) AIR CONDITIONING UNITS FOR FAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M0112_1900_-NONE-_-NONE-/",
    "Actor: Ferreteria EPA SA de CV (El Salvador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1149",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60016M0112_1900_-NONE-_-NONE- (ferreteria_epa_el_salvador_fap_air_conditioning_units_27k_2015). Signed 2015-11-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M0112_1900_-NONE-_-NONE-/.",
    "USASpending: ferreteria_epa_el_salvador_fap_air_conditioning_units_27k_2015 USD 0.027m. Supports ferreteria_epa_el_salvador_fap_air_conditioning_units_27k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26946.9; date_signed 2015-11-23.",
)

# === Cycle 1150 (seed 20262150) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "bw_color_prints_brazil_science_on_a_sphere_install_16k_2012",
    "infrastructure", "building_materials", "us",
    "B/W Color Prints — Brazil Science on a Sphere installation Sao Paulo",
    "Brazil",
    "13 Apr 2012: Department of Commerce awards contract DOCAB133009CQ0068T0035 to B/W Color Prints, LLC for Science on a Sphere installation for display in Sao Paolo, Brazil (PoP Brazil); obligated USD 15,794.27. CapEx face = award obligation. Sao Paulo named; site coords not stated — lat/lon blank.",
    "15794.27", "2012-04-13", "2012", "", "",
    "Science on a Sphere installation for display in Sao Paulo, Brazil (USASpending description; Sao Paulo named, site coords not stated — lat/lon blank).",
    "usaspending_bw_color_prints_brazil_science_on_a_sphere_install_16k_2012",
    "SCIENCE ON A SPHERE INSTALLATION FOR DISPLAY IN SAO PAOLO, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DOCAB133009CQ0068T0035_1330_DOCAB133009CQ0068_1330/",
    "Actor: B/W Color Prints, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1150",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_DOCAB133009CQ0068T0035_1330_DOCAB133009CQ0068_1330 (bw_color_prints_brazil_science_on_a_sphere_install_16k_2012). Signed 2012-04-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_DOCAB133009CQ0068T0035_1330_DOCAB133009CQ0068_1330/.",
    "USASpending: bw_color_prints_brazil_science_on_a_sphere_install_16k_2012 USD 0.016m. Supports bw_color_prints_brazil_science_on_a_sphere_install_16k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15794.27; date_signed 2012-04-13.",
)
row_doc(
    "frank_p_frey_dominican_republic_roof_material_hoist_5k_2010",
    "infrastructure", "building_materials", "us",
    "Frank P. Frey and Company — Dominican Republic ICASS hoist for moving material to roofs",
    "Dominican Republic",
    "13 Sep 2010: Department of State awards contract SDR86010M1514 to Frank P. Frey and Company for ICASS-hoist for moving material to roofs (PoP Dominican Republic); obligated USD 5,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "5000", "2010-09-13", "2010", "", "",
    "ICASS hoist for moving material to roofs, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_frank_p_frey_dominican_republic_roof_material_hoist_5k_2010",
    "ICASS-HOIST FOR MOVING MATERIAL TO ROOFS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86010M1514_1900_-NONE-_-NONE-/",
    "Actor: Frank P. Frey and Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1150",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86010M1514_1900_-NONE-_-NONE- (frank_p_frey_dominican_republic_roof_material_hoist_5k_2010). Signed 2010-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86010M1514_1900_-NONE-_-NONE-/.",
    "USASpending: frank_p_frey_dominican_republic_roof_material_hoist_5k_2010 USD 0.005m. Supports frank_p_frey_dominican_republic_roof_material_hoist_5k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5000; date_signed 2010-09-13.",
)
row_doc(
    "fg_sas_colombia_tulua_base_electrical_installation_11k_2023",
    "energy", "power_plants_grid", "other",
    "Ingenieria y Servicios FG — Colombia Tulua base electrical installation",
    "Colombia",
    "3 Aug 2023: Department of State awards contract 19C01523P0380 to Ingenieria y Servicios FG SAS for electrical installation-Tulua base (PoP Colombia); obligated USD 10,974.92. CapEx face = award obligation. Tulua base named; site coords not stated — lat/lon blank.",
    "10974.92", "2023-08-03", "2023", "", "",
    "Electrical installation at Tulua base, Colombia (USASpending description; Tulua named, site coords not stated — lat/lon blank).",
    "usaspending_fg_sas_colombia_tulua_base_electrical_installation_11k_2023",
    "ELECTRICAL INSTALLATION-TULUA BASE/0823",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523P0380_1900_-NONE-_-NONE-/",
    "Actor: Ingenieria y Servicios FG SAS (Colombia) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1150",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01523P0380_1900_-NONE-_-NONE- (fg_sas_colombia_tulua_base_electrical_installation_11k_2023). Signed 2023-08-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523P0380_1900_-NONE-_-NONE-/.",
    "USASpending: fg_sas_colombia_tulua_base_electrical_installation_11k_2023 USD 0.011m. Supports fg_sas_colombia_tulua_base_electrical_installation_11k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10974.92; date_signed 2023-08-03.",
)
row_doc(
    "misc_uruguay_stgl_residence_metal_grills_doors_11k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Uruguay STGL residence metal grills, reinforced metal doors and security upgrades",
    "Uruguay",
    "15 Sep 2010: Department of State awards contract SUY60010M0855 for labor and materials to install metal grills, reinforced metal doors and other security upgrades to STGL residence (PoP Uruguay); obligated USD 10,965. CapEx face = award obligation. STGL residence named; site coords not stated — lat/lon blank.",
    "10965", "2010-09-15", "2010", "", "",
    "Metal grills, reinforced metal doors and security upgrades to STGL residence, Uruguay (USASpending description; STGL named, site coords not stated — lat/lon blank).",
    "usaspending_misc_uruguay_stgl_residence_metal_grills_doors_11k_2010",
    "LABOR AND MATERIALS TO INSTALL METAL GRILLS, REINFORED METAL DOORS AND OTHER SECURITY UPGRADES TO STGL RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60010M0855_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1150",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60010M0855_1900_-NONE-_-NONE- (misc_uruguay_stgl_residence_metal_grills_doors_11k_2010). Signed 2010-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60010M0855_1900_-NONE-_-NONE-/.",
    "USASpending: misc_uruguay_stgl_residence_metal_grills_doors_11k_2010 USD 0.011m. Supports misc_uruguay_stgl_residence_metal_grills_doors_11k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10965; date_signed 2010-09-15.",
)
row_doc(
    "sarti_guatemala_aviation_landing_zone_lights_access_gate_9k_2019",
    "infrastructure", "building_materials", "other",
    "Luis Alberto Sarti Calvillo — Guatemala aviation landing zone lights and access gate",
    "Guatemala",
    "5 Apr 2019: Department of Defense awards contract W912QM19C0003 to Luis Alberto Sarti Calvillo for aviation landing zone lights and access gate (PoP Guatemala); obligated USD 9,000. CapEx face = award obligation. Exact landing zone unnamed — lat/lon blank.",
    "9000", "2019-04-05", "2019", "", "",
    "Aviation landing zone lights and access gate, Guatemala (USASpending description; landing zone not named — lat/lon blank).",
    "usaspending_sarti_guatemala_aviation_landing_zone_lights_access_gate_9k_2019",
    "AVIATION LANDING ZONE LIGHTS AND ACCESS GATE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM19C0003_9700_-NONE-_-NONE-/",
    "Actor: Luis Alberto Sarti Calvillo (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1150",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM19C0003_9700_-NONE-_-NONE- (sarti_guatemala_aviation_landing_zone_lights_access_gate_9k_2019). Signed 2019-04-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM19C0003_9700_-NONE-_-NONE-/.",
    "USASpending: sarti_guatemala_aviation_landing_zone_lights_access_gate_9k_2019 USD 0.009m. Supports sarti_guatemala_aviation_landing_zone_lights_access_gate_9k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9000; date_signed 2019-04-05.",
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
