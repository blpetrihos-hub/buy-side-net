#!/usr/bin/env python3
"""Cycles 1315–1316: USASpending LatAm CapEx (Leidos/Rapiscan/Culmen NII + misc kennels/walls).

Seeds: 20262315–20262316. Thin top-up dry.
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

# === Cycle 1315 ===
row_doc(
    "leidos_honduras_vacis_ip6500_20460k_2021",
    "infrastructure", "port_cranes", "us",
    "Leidos — Honduras VACIS IP6500 fullscan cargo inspection system",
    "Honduras",
    "13 Jan 2021: Department of State awards contract to LEIDOS, INC. for VACIS IP6500 fullscan integrated cargo inspection system; obligated USD 20459614.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20459614.00", "2021-01-13", "2021", "", "",
    "VACIS IP6500 FULLSCAN INTEGRATED CARGO INSPECTION SYSTEM, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_leidos_honduras_vacis_ip6500_20460k_2021",
    "VACIS IP6500 FULLSCAN INTEGRATED CARGO INSPECTION SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0435_1900_GS35F285DA_4732/",
    "Actor: LEIDOS, INC. (U.S.) — us. Official USASpending Award API. Shuffle port_cranes; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1315",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F0435_1900_GS35F285DA_4732 (leidos_honduras_vacis_ip6500_20460k_2021). Signed 2021-01-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0435_1900_GS35F285DA_4732/.",
    "USASpending: leidos_honduras_vacis_ip6500_20460k_2021 USD 20.460m. Supports leidos_honduras_vacis_ip6500_20460k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20459614.0; date_signed 2021-01-13.",
    investment_type="equipment_supply",
)

# === Cycle 1315 ===
row_doc(
    "rapiscan_panama_mobile_nii_11074k_2022",
    "infrastructure", "port_cranes", "us",
    "Rapiscan Systems — Panama four mobile non-intrusive inspection systems",
    "Panama",
    "3 Aug 2022: Department of State awards contract to RAPISCAN SYSTEMS INC for four mobile non-intrusive inspection systems, training, and related supplies/services (CapEx face = award obligation); obligated USD 11074428.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "11074428.00", "2022-08-03", "2022", "", "",
    "PANAMA - FOUR (4) MOBILE NON-INTRUSIVE INSPECTION SYSTEMS, TRAINING, INSTALLATION, PROGRAM MANAGEMENT SUPPORT, AND EXTEN, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_rapiscan_panama_mobile_nii_11074k_2022",
    "PANAMA - FOUR (4) MOBILE NON-INTRUSIVE INSPECTION SYSTEMS, TRAINING, INSTALLATION, PROGRAM MANAGEMENT SUPPORT, AND EXTENDED WARRANTY PERIODS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1420_1900_19AQMM21D0044_1900/",
    "Actor: RAPISCAN SYSTEMS INC (U.S.) — us. Official USASpending Award API. Shuffle port_cranes; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1315",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F1420_1900_19AQMM21D0044_1900 (rapiscan_panama_mobile_nii_11074k_2022). Signed 2022-08-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1420_1900_19AQMM21D0044_1900/.",
    "USASpending: rapiscan_panama_mobile_nii_11074k_2022 USD 11.074m. Supports rapiscan_panama_mobile_nii_11074k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11074428.0; date_signed 2022-08-03.",
    investment_type="equipment_supply",
)

# === Cycle 1315 ===
row_doc(
    "misc_mexico_juarez_k9_kennels_197k_2011",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Ciudad Juarez K9 kennels",
    "Mexico",
    "3 Jan 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for NAS MI Ciudad Juarez K9 kennels; obligated USD 197312.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "197312.46", "2011-01-03", "2011", "", "",
    "NAS MI-IN23MX64 CIUDAD JUAREZ K9-KENNELS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_juarez_k9_kennels_197k_2011",
    "NAS MI-IN23MX64 CIUDAD JUAREZ K9-KENNELS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0298_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1315",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M0298_1900_-NONE-_-NONE- (misc_mexico_juarez_k9_kennels_197k_2011). Signed 2011-01-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0298_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_juarez_k9_kennels_197k_2011 USD 0.197m. Supports misc_mexico_juarez_k9_kennels_197k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 197312.46; date_signed 2011-01-03.",
    investment_type="equipment_supply",
)

# === Cycle 1315 ===
row_doc(
    "misc_mexico_ssp_canine_kennels_191k_2010",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Mexico SSP canine unit kennels",
    "Mexico",
    "19 Jul 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for NAS-MI 60 kennels for SSP canine unit; obligated USD 190866.96. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "190866.96", "2010-07-19", "2010", "", "",
    "NAS-MI-60 KENNELS FOR SSP CANINE UNIT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_ssp_canine_kennels_191k_2010",
    "NAS-MI-60 KENNELS FOR SSP CANINE UNIT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0580_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1315",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0580_1900_-NONE-_-NONE- (misc_mexico_ssp_canine_kennels_191k_2010). Signed 2010-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0580_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_ssp_canine_kennels_191k_2010 USD 0.191m. Supports misc_mexico_ssp_canine_kennels_191k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 190866.96; date_signed 2010-07-19.",
    investment_type="equipment_supply",
)

# === Cycle 1315 ===
row_doc(
    "misc_colombia_santa_marta_bastion_wall_188k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Santa Marta metal bastion wall",
    "Colombia",
    "6 Jun 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for metal bastion wall for Santa Marta base; obligated USD 188224.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "188224.17", "2013-06-06", "2013", "", "",
    "INTER (BS) - METAL BASTION WALL FOR SANTA MARTA BASE, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_santa_marta_bastion_wall_188k_2013",
    "INTER (BS) - METAL BASTION WALL FOR SANTA MARTA BASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0873_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1315",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15013M0873_1900_-NONE-_-NONE- (misc_colombia_santa_marta_bastion_wall_188k_2013). Signed 2013-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0873_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_santa_marta_bastion_wall_188k_2013 USD 0.188m. Supports misc_colombia_santa_marta_bastion_wall_188k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 188224.17; date_signed 2013-06-06.",
    investment_type="epc",
)

# === Cycle 1316 ===
row_doc(
    "leidos_honduras_vacis_m6500_mobile_3200k_2022",
    "infrastructure", "engineering_epc", "us",
    "Leidos — Honduras mobile scanner VACIS M6500",
    "Honduras",
    "3 Jun 2022: Department of State awards contract to LEIDOS, INC. for mobile scanner VACIS M6500; obligated USD 3200194.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3200194.00", "2022-06-03", "2022", "", "",
    "MOBILE SCANNER VACIS M6500, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_leidos_honduras_vacis_m6500_mobile_3200k_2022",
    "MOBILE SCANNER VACIS M6500",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22P0038_1900_-NONE-_-NONE-/",
    "Actor: LEIDOS, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1316",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22P0038_1900_-NONE-_-NONE- (leidos_honduras_vacis_m6500_mobile_3200k_2022). Signed 2022-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22P0038_1900_-NONE-_-NONE-/.",
    "USASpending: leidos_honduras_vacis_m6500_mobile_3200k_2022 USD 3.200m. Supports leidos_honduras_vacis_m6500_mobile_3200k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3200194.0; date_signed 2022-06-03.",
    investment_type="equipment_supply",
)

# === Cycle 1316 ===
row_doc(
    "culmen_mexico_prison_nii_1597k_2026",
    "infrastructure", "engineering_epc", "us",
    "Culmen International — Mexico federal prisons non-intrusive inspection equipment",
    "Mexico",
    "8 Jun 2026: Department of State awards contract to CULMEN INTERNATIONAL, LLC for non-intrusive inspection equipment for Mexican federal prisons; obligated USD 1596736.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1596736.00", "2026-06-08", "2026", "", "",
    "NON-INTRUSIVE INSPECTION EQUIPMENT FOR MEXICAN FEDERAL PRISONS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_culmen_mexico_prison_nii_1597k_2026",
    "NON-INTRUSIVE INSPECTION EQUIPMENT FOR MEXICAN FEDERAL PRISONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0703_1900_19AQMM21D0041_1900/",
    "Actor: CULMEN INTERNATIONAL, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1316",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM26F0703_1900_19AQMM21D0041_1900 (culmen_mexico_prison_nii_1597k_2026). Signed 2026-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0703_1900_19AQMM21D0041_1900/.",
    "USASpending: culmen_mexico_prison_nii_1597k_2026 USD 1.597m. Supports culmen_mexico_prison_nii_1597k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1596736.0; date_signed 2026-06-08.",
    investment_type="equipment_supply",
)

# === Cycle 1316 ===
row_doc(
    "misc_elsalvador_fiber_coax_cabling_184k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador fiber optic and coaxial network cabling",
    "El Salvador",
    "21 Sep 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for IMO/IPO San Salvador fiber optic and coaxial network cabling; obligated USD 183899.14. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "183899.14", "2015-09-21", "2015", "", "",
    "IMO/IPO- SAN SALV - FIBER OPTIC AND COAXIAL NETWORK CABLING, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_elsalvador_fiber_coax_cabling_184k_2015",
    "IMO/IPO- SAN SALV - FIBER OPTIC AND COAXIAL NETWORK CABLING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60015M1130_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1316",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60015M1130_1900_-NONE-_-NONE- (misc_elsalvador_fiber_coax_cabling_184k_2015). Signed 2015-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60015M1130_1900_-NONE-_-NONE-/.",
    "USASpending: misc_elsalvador_fiber_coax_cabling_184k_2015 USD 0.184m. Supports misc_elsalvador_fiber_coax_cabling_184k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183899.14; date_signed 2015-09-21.",
    investment_type="epc",
)

# === Cycle 1316 ===
row_doc(
    "misc_argentina_chancery_awnings_195k_2024",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Argentina chancery awnings project",
    "Argentina",
    "3 Sep 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC awnings project at chancery; obligated USD 194849.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "194849.22", "2024-09-03", "2024", "", "",
    "FAC - AWNINGS PROJECT AT CHANCERY, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_chancery_awnings_195k_2024",
    "FAC - AWNINGS PROJECT AT CHANCERY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2024C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1316",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2024C0008_1900_-NONE-_-NONE- (misc_argentina_chancery_awnings_195k_2024). Signed 2024-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2024C0008_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_chancery_awnings_195k_2024 USD 0.195m. Supports misc_argentina_chancery_awnings_195k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 194849.22; date_signed 2024-09-03.",
    investment_type="epc",
)

# === Cycle 1316 ===
row_doc(
    "mfg_colombia_cmr_bathrooms_guardhouse_167k_2024",
    "infrastructure", "engineering_epc", "other",
    "MFG Ingenieria — Colombia CMR bathrooms renovations and guardhouse improvements",
    "Colombia",
    "20 Sep 2024: Department of State awards contract to MFG INGENIERIA SAS for CMR bathrooms renovations and guardhouse improvements; obligated USD 166992.48. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "166992.48", "2024-09-20", "2024", "", "",
    "PR12929282_CMR BATHROOMS RENOVATIONS AND GUARDHOUSE IMPROVEMENTS 7919, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_cmr_bathrooms_guardhouse_167k_2024",
    "PR12929282_CMR BATHROOMS RENOVATIONS AND GUARDHOUSE IMPROVEMENTS 7919",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024C0010_1900_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1316",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024C0010_1900_-NONE-_-NONE- (mfg_colombia_cmr_bathrooms_guardhouse_167k_2024). Signed 2024-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024C0010_1900_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_cmr_bathrooms_guardhouse_167k_2024 USD 0.167m. Supports mfg_colombia_cmr_bathrooms_guardhouse_167k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 166992.48; date_signed 2024-09-20.",
    investment_type="epc",
)

def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    for row, _ev, _bib in ITEMS:
        rid = row["id"]
        if rid in by_id: raise SystemExit(f"duplicate id: {rid}")
        rows.append(row); by_id[rid] = row
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
                if s not in (existing.get("supports") or []): existing.setdefault("supports", []).append(s)
        else: bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
