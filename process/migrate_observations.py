#!/usr/bin/env python3
"""One-shot migration: old buy-side lanes → three-layer commanding-heights schema.

Run once from repo root. Idempotent only if observations.csv is still in the old
schema (detects by header). After migration, build_site_data.py owns the CSV.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / "data" / "codebook" / "observations.csv"
EVIDENCE_DIR = ROOT / "data" / "attribution" / "evidence"

NEW_FIELDS = [
    "id",
    "layer",
    "subcategory",
    "side",
    "counterpart",
    "country",
    "asset",
    "investment_type",
    "value",
    "currency",
    "value_usd",
    "fx_usd",
    "fx_date",
    "year",
    "status",
    "lat",
    "lon",
    "geo_note",
    "evidence",
    "source_id",
    "note",
    "pair_id",
    "counterpart_side",
    "counterpart_actor",
    "counterpart_value",
    "counterpart_currency",
    "counterpart_value_usd",
    "gap",
]

# Legacy id → (layer, subcategory, status, investment_type overrides)
SPECIAL = {
    "hunt_br_power_equip": ("energy", "power_plants_grid", "hunt", "equipment_supply"),
    "hunt_cl_power_equip": ("energy", "power_plants_grid", "hunt", "equipment_supply"),
    "hunt_mx_power_equip": ("energy", "power_plants_grid", "hunt", "equipment_supply"),
    "hunt_fenb_araxa": ("resources", "niobium", "hunt", "offtake"),
    "hunt_ascend_chip": ("archived", "ai_chips", "archived", "other"),
    "hunt_icbc_rate": ("archived", "icbc_finance", "archived", "financing"),
    "hunt_latam_rail_telecom": ("infrastructure", "rail", "hunt", "equipment_supply"),
    "sp_metro_crrc_alstom_2024": ("infrastructure", "rail", "active", "equipment_supply"),
    "efe_crrc_emu_2023": ("infrastructure", "rail", "active", "equipment_supply"),
    "fenb_china_mkt_202309": ("resources", "niobium", "active", "offtake"),
    "h20_ascend910b_2024": ("archived", "ai_chips", "archived", "other"),
    "icbc_huawei_wire_2019": ("archived", "icbc_finance", "archived", "financing"),
    "aneel_state_grid_rap_2023": ("energy", "power_plants_grid", "active", "concession"),
    "cen_parinas_elecnor_powerchina_2024": ("energy", "power_plants_grid", "active", "epc"),
    "fenb65_brazil_china_mkt_20230925": ("resources", "niobium", "active", "offtake"),
    "atlas900_a3_superpod_sysu_2024": ("archived", "ai_chips", "archived", "other"),
    "exim_cirr_usd_5y_202412": ("archived", "icbc_finance", "archived", "financing"),
    "csm_fenb_range_context": ("resources", "niobium", "active", "other"),
    "siemens_furnas_itaipu_fsc_2023": ("energy", "power_plants_grid", "active", "epc"),
    "siemens_eletrobras_grid_pkg_2024": ("energy", "power_plants_grid", "active", "epc"),
    "xdcb_brazil_ne_uhv_ct_2024": ("energy", "power_plants_grid", "active", "equipment_supply"),
    "atlas800t_a2_wust_2024": ("archived", "ai_chips", "archived", "other"),
    "eximbank_china_barbados_scotland_2022": ("archived", "icbc_finance", "archived", "financing"),
    "cen_fengfan_g03_2024": ("energy", "power_plants_grid", "active", "epc"),
    "ustc_suzhou_hgx_h20_2024": ("archived", "ai_chips", "archived", "other"),
    "ucas_h20_ascend910b4_2025": ("archived", "ai_chips", "archived", "other"),
    "usgs_fenb_us_unit_2024": ("resources", "niobium", "active", "offtake"),
    "fenb60a_china_mkt_20241230": ("resources", "niobium", "active", "offtake"),
    "wits_eu_fenb_br_imp_2024": ("resources", "niobium", "active", "offtake"),
    "wits_china_fenb_br_imp_2024": ("resources", "niobium", "active", "offtake"),
    "mysteel_fenb_br_vs_cn_20260929": ("resources", "niobium", "active", "offtake"),
    "cmoc_argus_fenb_kgNb_2025": ("resources", "niobium", "active", "offtake"),
    "ucas_h20_xe9680_202504": ("archived", "ai_chips", "archived", "other"),
    "cip_atlas800i_a2_2025": ("archived", "ai_chips", "archived", "other"),
    "snnu_atlas800i_a2_2025": ("archived", "ai_chips", "archived", "other"),
    "uestc_huakun_at800_a2_2025": ("archived", "ai_chips", "archived", "other"),
    "hust_ascend910_card_2026": ("archived", "ai_chips", "archived", "other"),
    "h20_96g_smm_module_202609": ("archived", "ai_chips", "archived", "other"),
    "cupl_a800_card_2025": ("archived", "ai_chips", "archived", "other"),
    "bfsu_inspur_8gpu_2026": ("archived", "ai_chips", "archived", "other"),
    "huatai_ascend910c_cloud_2026": ("archived", "ai_chips", "archived", "other"),
    "qilu_rtxa6000_card_2026": ("archived", "ai_chips", "archived", "other"),
    "ascend910b4_smm_module_202608": ("archived", "ai_chips", "archived", "other"),
    "ascend910c_mysteel_ind_202609": ("archived", "ai_chips", "archived", "other"),
    "exim_us_guyana_gte_2025": ("archived", "icbc_finance", "archived", "financing"),
    "xd_eletrobras_wave4_xfmr_2025": ("energy", "power_plants_grid", "active", "equipment_supply"),
    "xd_kimal_lo_aguirre_cs_2022": ("energy", "power_plants_grid", "active", "epc"),
    "huawei_ctg_arinos_inv_2022": ("energy", "solar", "active", "equipment_supply"),
    "siemens_terranova_gis_xfmr_2026": ("energy", "power_plants_grid", "active", "epc"),
    "fenb_br_vs_cn_20240523": ("resources", "niobium", "active", "offtake"),
    "niocorp_argus_fenb_us_2024": ("resources", "niobium", "active", "offtake"),
    "fenb_br66_vs_cn60a_20260921": ("resources", "niobium", "active", "offtake"),
}

# New hunt seeds for empty subcategories (no prices, no invented coords)
NEW_HUNTS = [
    {
        "id": "hunt_infra_port_ownership",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm port ownership / concession with U.S. or PRC operator",
        "investment_type": "concession",
        "note": "Hunt: port authority or ministry notice naming a U.S. or PRC terminal operator / concessionaire in Latin America, 2021–2026. No pin until a named port is located.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_infra_port_cranes",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm STS / RTG crane or terminal equipment award",
        "investment_type": "equipment_supply",
        "note": "Hunt: procurement or press naming ZPMC or a U.S. crane supplier for a named Latin American terminal. No pin until the terminal is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_infra_bridges_roads",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm bridge or highway concession / EPC with U.S. or PRC contractor",
        "investment_type": "epc",
        "note": "Hunt: ministry or concessionaire award for a bridge or road package naming a U.S. or PRC EPC. No pin until the corridor is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_infra_building_materials",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm cement, steel, or building-materials investment by U.S. or PRC firm",
        "investment_type": "ownership_equity",
        "note": "Hunt: company filing or ministry notice for a cement, steel, or materials plant / stake in Latin America. No pin until a plant city is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_infra_engineering_epc",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm engineering / design / EPC firm award (non-energy grid)",
        "investment_type": "epc",
        "note": "Hunt: published EPC or design-firm contract in Latin America with a U.S. or PRC lead. Energy-grid EPCs stay under energy/power_plants_grid.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_res_lithium",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm lithium mine, brine, or offtake with U.S. or PRC participation",
        "investment_type": "ownership_equity",
        "note": "Hunt: Chile/Argentina/Bolivia lithium project with disclosed U.S. or PRC equity, offtake, or financing. No pin until the salar or plant is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_res_copper",
        "layer": "resources",
        "subcategory": "copper",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm copper mine or smelter with U.S. or PRC participation",
        "investment_type": "ownership_equity",
        "note": "Hunt: copper project equity, offtake, or EPC in Latin America naming a U.S. or PRC firm. No pin until the mine is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_res_nickel",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm nickel mine or offtake with U.S. or PRC participation",
        "investment_type": "offtake",
        "note": "Hunt: nickel project or offtake in Latin America (Brazil, Cuba, others) with U.S. or PRC participation. No pin until the site is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_res_dimension_stone",
        "layer": "resources",
        "subcategory": "dimension_stone",
        "side": "other",
        "counterpart": "",
        "country": "Brazil",
        "asset": "Brazilian dimension stone / granite export or quarry stake involving U.S. or PRC buyer",
        "investment_type": "offtake",
        "note": "Hunt: granite / dimension-stone trade or quarry investment linking Brazil (or other LatAm) to a U.S. or PRC buyer. No pin until a quarry or port is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_res_balsa",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "other",
        "counterpart": "",
        "country": "Ecuador",
        "asset": "Ecuador balsa supply into U.S. or PRC wind-blade / industrial offtake",
        "investment_type": "offtake",
        "note": "Hunt: published offtake or export figure for Ecuadorian balsa to a named U.S. or PRC industrial buyer. No pin until a mill or port is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_res_water",
        "layer": "resources",
        "subcategory": "water",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm desalination, aqueduct, or water concession with U.S. or PRC firm",
        "investment_type": "concession",
        "note": "Hunt: desalination plant, aqueduct, or water concession naming a U.S. or PRC contractor/operator. No pin until the plant is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_energy_fission_smr",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm SMR or large fission reactor deal with U.S. or PRC technology",
        "investment_type": "epc",
        "note": "Hunt: Argentina, Brazil, or other LatAm nuclear/SMR award or MoU with disclosed U.S. or PRC technology supplier. No pin until the site is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_energy_wind",
        "layer": "energy",
        "subcategory": "wind",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm wind farm turbine supply or equity with U.S. or PRC firm",
        "investment_type": "equipment_supply",
        "note": "Hunt: wind-farm turbine supply or stake naming Goldwind, Vestas, GE Vernova, or similar in Latin America. No pin until the park is named.",
        "source_id": "methods_clock",
    },
    {
        "id": "hunt_energy_other_renewables",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "other",
        "counterpart": "",
        "country": "",
        "asset": "LatAm geothermal or small-hydro project with U.S. or PRC participation",
        "investment_type": "epc",
        "note": "Hunt: geothermal or small-hydro (PCH) award naming a U.S. or PRC firm. No pin until the plant is named.",
        "source_id": "methods_clock",
    },
]


def blank(v) -> bool:
    return v is None or str(v).strip() == ""


def infer_side(row: dict) -> str:
    us_side = (row.get("us_side") or "").strip().lower()
    has_us = not blank(row.get("us_price")) or not blank(row.get("us_price_usd")) or not blank(row.get("seller_us"))
    has_prc = not blank(row.get("prc_price")) or not blank(row.get("prc_price_usd")) or not blank(row.get("seller_prc"))
    evidence = (row.get("evidence") or "").strip().lower()

    if us_side == "us":
        return "us"
    if us_side == "allied":
        return "allied"
    # unknown / blank
    if has_prc and not has_us:
        return "prc"
    if has_us and not has_prc:
        return "us" if us_side == "us" else "allied"
    if evidence == "hunt":
        return "other"
    if has_prc:
        return "prc"
    return "other"


def primary_value(row: dict, side: str) -> tuple[str, str, str]:
    """Return (value, currency, value_usd) for the row's primary side."""
    if side == "prc":
        return (
            row.get("prc_price") or "",
            row.get("currency") or "",
            row.get("prc_price_usd") or "",
        )
    # us / allied / other — prefer us_* fields
    if not blank(row.get("us_price")) or not blank(row.get("us_price_usd")):
        return (
            row.get("us_price") or "",
            row.get("currency") or "",
            row.get("us_price_usd") or "",
        )
    if not blank(row.get("prc_price")) or not blank(row.get("prc_price_usd")):
        return (
            row.get("prc_price") or "",
            row.get("currency") or "",
            row.get("prc_price_usd") or "",
        )
    return ("", row.get("currency") or "", "")


def counterpart_fields(row: dict, side: str) -> dict:
    out = {
        "pair_id": "",
        "counterpart_side": "",
        "counterpart_actor": "",
        "counterpart_value": "",
        "counterpart_currency": "",
        "counterpart_value_usd": "",
        "gap": row.get("gap") or "",
    }
    evidence = (row.get("evidence") or "").strip().lower()
    has_us = not blank(row.get("us_price_usd")) or not blank(row.get("us_price"))
    has_prc = not blank(row.get("prc_price_usd")) or not blank(row.get("prc_price"))
    if evidence == "paired" or (has_us and has_prc):
        if side == "prc":
            out["counterpart_side"] = "us" if (row.get("us_side") or "").lower() == "us" else "allied"
            out["counterpart_actor"] = row.get("seller_us") or ""
            out["counterpart_value"] = row.get("us_price") or ""
            out["counterpart_currency"] = row.get("currency") or ""
            out["counterpart_value_usd"] = row.get("us_price_usd") or ""
        else:
            out["counterpart_side"] = "prc"
            out["counterpart_actor"] = row.get("seller_prc") or ""
            out["counterpart_value"] = row.get("prc_price") or ""
            out["counterpart_currency"] = row.get("currency") or ""
            out["counterpart_value_usd"] = row.get("prc_price_usd") or ""
    return out


# ISO-style display names used in the codebook. Must stay in sync with codebook.yml.
LATAM_CARIBBEAN = {
    "Argentina", "Belize", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica",
    "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Guyana",
    "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay",
    "Peru", "Suriname", "Uruguay", "Venezuela", "Antigua and Barbuda", "Bahamas",
    "Barbados", "Dominica", "Grenada", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Trinidad and Tobago", "Puerto Rico",
}


def migrate_row(row: dict) -> dict:
    rid = row["id"]
    if rid not in SPECIAL:
        raise SystemExit(f"Unmapped legacy id: {rid}")
    layer, subcat, status, inv = SPECIAL[rid]
    side = infer_side(row)
    # Hunt rows without a priced side stay other
    if status == "hunt" and blank(row.get("us_price")) and blank(row.get("prc_price")):
        side = "other"
    if status == "archived" and side == "other":
        # keep inferred side for archived chips/finance where possible
        side = infer_side(row)

    value, currency, value_usd = primary_value(row, side)
    # For exclude RAP-style rows that only stored a figure in us_price_usd oddly
    if blank(value_usd) and not blank(row.get("us_price_usd")) and side != "prc":
        value_usd = row.get("us_price_usd") or ""
        value = row.get("us_price") or value
    if blank(value_usd) and not blank(row.get("prc_price_usd")) and side == "prc":
        value_usd = row.get("prc_price_usd") or ""

    asset = row.get("spec") or row.get("spec_class") or ""
    counterpart = row.get("buyer") or ""
    actor_note = ""
    if side == "prc" and row.get("seller_prc"):
        actor_note = f"Actor: {row['seller_prc']}. "
    elif side in ("us", "allied") and row.get("seller_us"):
        actor_note = f"Actor: {row['seller_us']}. "
    elif row.get("seller_prc") or row.get("seller_us"):
        bits = []
        if row.get("seller_us"):
            bits.append(f"non-PRC={row['seller_us']}")
        if row.get("seller_prc"):
            bits.append(f"PRC={row['seller_prc']}")
        actor_note = "Actors: " + "; ".join(bits) + ". "

    legacy = f"Migrated from lane={row.get('lane')} spec_class={row.get('spec_class')}."
    note = (actor_note + (row.get("note") or "") + " " + legacy).strip()

    cf = counterpart_fields(row, side)
    # For paired energy/infra awards won by PRC, primary side is the awardee
    if rid in ("cen_parinas_elecnor_powerchina_2024",) and not blank(row.get("seller_prc")):
        side = "prc"
        value, currency, value_usd = primary_value(row, "prc")
        cf = counterpart_fields(row, "prc")
    if rid in ("sp_metro_crrc_alstom_2024",) and not blank(row.get("seller_prc")):
        # CRRC won; Alstom was the competing allied bid
        side = "prc"
        value, currency, value_usd = primary_value(row, "prc")
        cf = counterpart_fields(row, "prc")
        cf["counterpart_side"] = "allied"

    country = (row.get("country") or "").strip()
    # Geography rule: Latin America and the Caribbean only.
    # Out-of-region countries are archived and never mapped (build script re-enforces).
    if country and country not in LATAM_CARIBBEAN:
        if status != "archived":
            note = (
                note
                + f" Archived: country '{country}' is outside Latin America and the Caribbean."
            ).strip()
        status = "archived"
        if layer != "archived":
            layer = "archived"

    return {
        "id": rid,
        "layer": layer,
        "subcategory": subcat,
        "side": side,
        "counterpart": counterpart,
        "country": country,
        "asset": asset,
        "investment_type": inv,
        "value": value,
        "currency": currency,
        "value_usd": value_usd,
        "fx_usd": row.get("fx_usd") or "",
        "fx_date": row.get("fx_date") or "",
        "year": row.get("price_year") or "",
        "status": status,
        "lat": row.get("lat") or "",
        "lon": row.get("lon") or "",
        "geo_note": row.get("geo_note") or "",
        "evidence": row.get("evidence") or "",
        "source_id": row.get("source_id") or "",
        "note": note,
        **cf,
    }


def hunt_seed(h: dict) -> dict:
    return {
        "id": h["id"],
        "layer": h["layer"],
        "subcategory": h["subcategory"],
        "side": h.get("side", "other"),
        "counterpart": h.get("counterpart", ""),
        "country": h.get("country", ""),
        "asset": h["asset"],
        "investment_type": h["investment_type"],
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "",
        "status": "hunt",
        "lat": "",
        "lon": "",
        "geo_note": "",
        "evidence": "hunt",
        "source_id": h["source_id"],
        "note": h["note"],
        "pair_id": "",
        "counterpart_side": "",
        "counterpart_actor": "",
        "counterpart_value": "",
        "counterpart_currency": "",
        "counterpart_value_usd": "",
        "gap": "",
    }


def write_hunt_evidence(h: dict) -> None:
    path = EVIDENCE_DIR / f"{h['id']}.json"
    if path.exists():
        return
    payload = {
        "id": h["id"],
        "retrieved": "2026-10-01",
        "source_id": h["source_id"],
        "url": "",
        "price_year": "",
        "evidence": "hunt",
        "quote": "",
        "note": h["note"],
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    with OLD.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        if "layer" in fields and "lane" not in fields:
            print("Already migrated (layer present). Skipping.")
            return
        old_rows = list(reader)

    new_rows = [migrate_row(r) for r in old_rows]
    existing_ids = {r["id"] for r in new_rows}
    for h in NEW_HUNTS:
        if h["id"] not in existing_ids:
            new_rows.append(hunt_seed(h))
            write_hunt_evidence(h)

    with OLD.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=NEW_FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in new_rows:
            w.writerow({k: r.get(k, "") for k in NEW_FIELDS})

    # Summary
    from collections import Counter

    layers = Counter(r["layer"] for r in new_rows)
    sides = Counter(r["side"] for r in new_rows if r["status"] != "archived")
    status = Counter(r["status"] for r in new_rows)
    print("Migrated", len(old_rows), "legacy rows; total now", len(new_rows))
    print("layers:", dict(layers))
    print("status:", dict(status))
    print("sides (non-archived):", dict(sides))


if __name__ == "__main__":
    main()
