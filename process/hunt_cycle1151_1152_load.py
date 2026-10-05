#!/usr/bin/env python3
"""Cycles 1151–1152: USASpending LatAm CapEx residual (~USD0.007–0.026m).

Seeds: 20262151–20262152. Thin top-up dry.
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


# === Cycle 1151 (seed 20262151) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_belize_metal_door_screen_25k_2022",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Belize metal door screen for international embassies",
    "Belize",
    "26 Jul 2022: Department of State awards contract 19AQMM22P0891 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Belize); obligated USD 24,800. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "24800", "2022-07-26", "2022", "", "",
    "Metal door screen etc. for international embassies, Belize (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_belize_metal_door_screen_25k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0891_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1151",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0891_1900_-NONE-_-NONE- (norshield_belize_metal_door_screen_25k_2022). Signed 2022-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0891_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_belize_metal_door_screen_25k_2022 USD 0.025m. Supports norshield_belize_metal_door_screen_25k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24800; date_signed 2022-07-26.",
)
row_doc(
    "cummins_belize_generator_bme_19k_2016",
    "energy", "power_plants_grid", "us",
    "Cummins Mid-South — Belize generator BME",
    "Belize",
    "22 Sep 2016: Department of State awards contract SBH20016M0418 to Cummins Mid-South LLC for FM - generator BME (PoP Belize); obligated USD 18,803.71. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "18803.71", "2016-09-22", "2016", "", "",
    "Generator BME, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_cummins_belize_generator_bme_19k_2016",
    "IGF::OT::IGFFM - GENERATOR BME",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20016M0418_1900_-NONE-_-NONE-/",
    "Actor: Cummins Mid-South LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1151",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20016M0418_1900_-NONE-_-NONE- (cummins_belize_generator_bme_19k_2016). Signed 2016-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20016M0418_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_belize_generator_bme_19k_2016 USD 0.019m. Supports cummins_belize_generator_bme_19k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18803.71; date_signed 2016-09-22.",
)
row_doc(
    "misc_mexico_cdj_motor_pump_replacement_gov_prop_14k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juarez motor and pump replacement for gov prop 1000",
    "Mexico",
    "3 Sep 2015: Department of State awards contract SMX11515M0471 for CDJ 7901-motor and pump replacement for gov prop 1000 (PoP Mexico); obligated USD 13,987.27. CapEx face = award obligation. Ciudad Juarez (CDJ) named; site coords not stated — lat/lon blank.",
    "13987.27", "2015-09-03", "2015", "", "",
    "Motor and pump replacement for gov prop 1000, Ciudad Juarez, Mexico (USASpending description; CDJ named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_motor_pump_replacement_gov_prop_14k_2015",
    "CDJ 7901-MOTOR AND PUMP REPLACEMENT FOR GOV PROP 1000",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11515M0471_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1151",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11515M0471_1900_-NONE-_-NONE- (misc_mexico_cdj_motor_pump_replacement_gov_prop_14k_2015). Signed 2015-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11515M0471_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cdj_motor_pump_replacement_gov_prop_14k_2015 USD 0.014m. Supports misc_mexico_cdj_motor_pump_replacement_gov_prop_14k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13987.27; date_signed 2015-09-03.",
)
row_doc(
    "misc_haiti_air_conditioning_units_7k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti air conditioning units",
    "Haiti",
    "18 May 2010: Department of Defense awards contract W912CL10P9021 for air conditioning units (PoP Haiti); obligated USD 7,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "7000", "2010-05-18", "2010", "", "",
    "Air conditioning units, Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_haiti_air_conditioning_units_7k_2010",
    "AIR CONDITIONING UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10P9021_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1151",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10P9021_9700_-NONE-_-NONE- (misc_haiti_air_conditioning_units_7k_2010). Signed 2010-05-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10P9021_9700_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_air_conditioning_units_7k_2010 USD 0.007m. Supports misc_haiti_air_conditioning_units_7k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7000; date_signed 2010-05-18.",
)
row_doc(
    "dicec_panama_galeta_aerogenerator_generator_install_10k_2013",
    "energy", "power_plants_grid", "other",
    "DICEC — Panama install generator for aerogenerator at Galeta",
    "Panama",
    "9 Aug 2013: Smithsonian awards contract F13PO7300000285315 to Design Installation and Consulting Engineering Company Inc. (DICEC) to install 1 generator for the aerogenerator at Galeta (PoP Panama); obligated USD 9,873. CapEx face = award obligation. Galeta named; site coords not stated — lat/lon blank.",
    "9873", "2013-08-09", "2013", "", "",
    "Install 1 generator for the aerogenerator at Galeta, Panama (USASpending description; Galeta named, site coords not stated — lat/lon blank).",
    "usaspending_dicec_panama_galeta_aerogenerator_generator_install_10k_2013",
    "IGF::OT::IGF  REQUIRED SERVICES ARE NOT PROVIDED BY AGENCY EMPLOYEES. TO INSTALL 1 GENERATOR FOR THE AEROGENERATOR AT GALETA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F13PO7300000285315_3300_-NONE-_-NONE-/",
    "Actor: Design Installation and Consulting Engineering Company Inc. (DICEC) (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1151",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F13PO7300000285315_3300_-NONE-_-NONE- (dicec_panama_galeta_aerogenerator_generator_install_10k_2013). Signed 2013-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F13PO7300000285315_3300_-NONE-_-NONE-/.",
    "USASpending: dicec_panama_galeta_aerogenerator_generator_install_10k_2013 USD 0.010m. Supports dicec_panama_galeta_aerogenerator_generator_install_10k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9873; date_signed 2013-08-09.",
)

# === Cycle 1152 (seed 20262152) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "summit_electric_mexico_cdj_lighting_fixture_replacement_8k_2016",
    "infrastructure", "building_materials", "us",
    "Summit Electric Supply — Mexico Ciudad Juarez lighting fixture replacement restroom gov prop 1000",
    "Mexico",
    "22 Jan 2016: Department of State awards contract SMX11516M0061 to Summit Electric Supply, LLC for CDJ-7901 lighting fixture replacement/restroom gov prop 1000 (PoP Mexico); obligated USD 7,929. CapEx face = award obligation. Ciudad Juarez (CDJ) named; site coords not stated — lat/lon blank.",
    "7929", "2016-01-22", "2016", "", "",
    "Lighting fixture replacement/restroom gov prop 1000, Ciudad Juarez, Mexico (USASpending description; CDJ named, site coords not stated — lat/lon blank).",
    "usaspending_summit_electric_mexico_cdj_lighting_fixture_replacement_8k_2016",
    "CDJ-7901 LIGHTING FIXTURE REPLACEMENT/RESTROOM GOV PROP 1000",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0061_1900_-NONE-_-NONE-/",
    "Actor: Summit Electric Supply, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1152",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516M0061_1900_-NONE-_-NONE- (summit_electric_mexico_cdj_lighting_fixture_replacement_8k_2016). Signed 2016-01-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0061_1900_-NONE-_-NONE-/.",
    "USASpending: summit_electric_mexico_cdj_lighting_fixture_replacement_8k_2016 USD 0.008m. Supports summit_electric_mexico_cdj_lighting_fixture_replacement_8k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7929; date_signed 2016-01-22.",
)
row_doc(
    "solar_electric_colombia_solar_powered_street_lights_12k_2011",
    "energy", "other_renewables", "us",
    "Solar Electric Power Company — Colombia solar powered street lights with bracket",
    "Colombia",
    "11 Aug 2011: Department of Defense awards contract W913FT11F0015 to Solar Electric Power Company for street lights, solar powered w/bracket (PoP Colombia); obligated USD 11,895. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "11895", "2011-08-11", "2011", "", "",
    "Solar powered street lights with bracket, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_solar_electric_colombia_solar_powered_street_lights_12k_2011",
    "STREET LIGHTS, SOLAR POWERED W/BRACKET",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11F0015_9700_GS07F0288M_4730/",
    "Actor: Solar Electric Power Company (U.S.) — us. Official USASpending Award API. Shuffle other_renewables; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1152",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11F0015_9700_GS07F0288M_4730 (solar_electric_colombia_solar_powered_street_lights_12k_2011). Signed 2011-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11F0015_9700_GS07F0288M_4730/.",
    "USASpending: solar_electric_colombia_solar_powered_street_lights_12k_2011 USD 0.012m. Supports solar_electric_colombia_solar_powered_street_lights_12k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11895; date_signed 2011-08-11.",
)
row_doc(
    "misc_paraguay_rso_split_ac_units_guard_positions_7k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Paraguay RSO split A/C units for guard positions",
    "Paraguay",
    "19 Jul 2011: Department of State awards contract SPA10011M0252 for RSO split A/C units for guard positions (PoP Paraguay); obligated USD 6,998.85. CapEx face = award obligation. Exact guard positions unnamed — lat/lon blank.",
    "6998.85", "2011-07-19", "2011", "", "",
    "Split A/C units for guard positions, Paraguay (USASpending description; positions not named — lat/lon blank).",
    "usaspending_misc_paraguay_rso_split_ac_units_guard_positions_7k_2011",
    "FOR RSO - SPLIT A/C UNITS FOR GUARD POSITIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10011M0252_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1152",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPA10011M0252_1900_-NONE-_-NONE- (misc_paraguay_rso_split_ac_units_guard_positions_7k_2011). Signed 2011-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10011M0252_1900_-NONE-_-NONE-/.",
    "USASpending: misc_paraguay_rso_split_ac_units_guard_positions_7k_2011 USD 0.007m. Supports misc_paraguay_rso_split_ac_units_guard_positions_7k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6998.85; date_signed 2011-07-19.",
)
row_doc(
    "osegueda_el_salvador_latrine_septic_tank_construct_26k_2010",
    "infrastructure", "building_materials", "other",
    "Heriberto Antonio Osegueda Martinez — El Salvador construct latrine and septic tank",
    "El Salvador",
    "28 Jun 2010: Department of Defense awards contract W9127810P0156 to Heriberto Antonio Osegueda Martinez for construct latrine and septic tank (PoP El Salvador); obligated USD 25,965. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "25965", "2010-06-28", "2010", "", "",
    "Construct latrine and septic tank, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_osegueda_el_salvador_latrine_septic_tank_construct_26k_2010",
    "CONSTRUCT LATRINE AND SEPTIC TANK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0156_9700_-NONE-_-NONE-/",
    "Actor: Heriberto Antonio Osegueda Martinez (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1152",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0156_9700_-NONE-_-NONE- (osegueda_el_salvador_latrine_septic_tank_construct_26k_2010). Signed 2010-06-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0156_9700_-NONE-_-NONE-/.",
    "USASpending: osegueda_el_salvador_latrine_septic_tank_construct_26k_2010 USD 0.026m. Supports osegueda_el_salvador_latrine_septic_tank_construct_26k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25965; date_signed 2010-06-28.",
)
row_doc(
    "misc_honduras_cmr_hvac_purchase_install_8k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras purchase and installation of HVAC for CMR",
    "Honduras",
    "25 Sep 2013: Department of State awards contract SHO80013M0847 for purchase and installation of HVCA for CMR (PoP Honduras); obligated USD 7,984.52. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "7984.52", "2013-09-25", "2013", "", "",
    "Purchase and installation of HVAC for CMR, Honduras (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_cmr_hvac_purchase_install_8k_2013",
    "PURCHASE AND INSTALLATION OF HVCA FOR CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013M0847_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1152",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80013M0847_1900_-NONE-_-NONE- (misc_honduras_cmr_hvac_purchase_install_8k_2013). Signed 2013-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013M0847_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_cmr_hvac_purchase_install_8k_2013 USD 0.008m. Supports misc_honduras_cmr_hvac_purchase_install_8k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7984.52; date_signed 2013-09-25.",
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
