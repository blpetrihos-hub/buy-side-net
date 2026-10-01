"""Read codebook CSV + evidence; recompute gap; write docs/data JSON for the map."""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "data" / "codebook" / "observations.csv"
CODEBOOK_YML = ROOT / "data" / "codebook" / "codebook.yml"
EVIDENCE_DIR = ROOT / "data" / "attribution" / "evidence"
OUT = ROOT / "docs" / "data"

FIELDS = [
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

USD_EVIDENCE = {"paired", "one_sided", "documented"}
MAP_STATUS = {"active", "hunt"}
READOUT_STATUS = {"active"}

# Fallback if codebook.yml is missing; keep in sync with geography.latin_america_caribbean.
LATAM_CARIBBEAN_FALLBACK = {
    "Argentina", "Belize", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica",
    "Cuba", "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Guyana",
    "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay",
    "Peru", "Suriname", "Uruguay", "Venezuela", "Antigua and Barbuda", "Bahamas",
    "Barbados", "Dominica", "Grenada", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Trinidad and Tobago", "Puerto Rico",
}


def blank(v: str | None) -> bool:
    return v is None or str(v).strip() == ""


def region_countries(meta: dict) -> set[str]:
    geo = meta.get("geography") or {}
    listed = geo.get("latin_america_caribbean") or []
    if listed:
        return {str(c).strip() for c in listed if str(c).strip()}
    return set(LATAM_CARIBBEAN_FALLBACK)


def approx_in_latam(lat: float | None, lon: float | None) -> bool:
    """Rough bounding box for Latin America & the Caribbean (incl. Mexico/Caribbean)."""
    if lat is None or lon is None:
        return False
    return -56.0 <= lat <= 33.5 and -120.0 <= lon <= -30.0


def enforce_geography(row: dict, countries: set[str]) -> dict:
    """Archive out-of-region rows. Blank country is allowed for hunts but never mapped."""
    country = (row.get("country") or "").strip()
    if country and country not in countries:
        row["status"] = "archived"
        if (row.get("layer") or "") != "archived":
            note = row.get("note") or ""
            marker = "Archived: country outside Latin America and the Caribbean."
            if marker not in note:
                row["note"] = (note + " " + marker).strip()
            row["layer"] = "archived"
        row["lat"] = ""
        row["lon"] = ""
        return row

    # Drop pins that fall outside the regional bounding box (e.g. seller HQ in China).
    lat = to_float(row.get("lat"))
    lon = to_float(row.get("lon"))
    if lat is not None and lon is not None and not approx_in_latam(lat, lon):
        note = row.get("note") or ""
        marker = "Coordinates cleared: pin was outside Latin America and the Caribbean."
        if marker not in note:
            row["note"] = (note + " " + marker).strip()
        row["lat"] = ""
        row["lon"] = ""
        geo = row.get("geo_note") or ""
        if "outside region" not in geo.lower():
            row["geo_note"] = (geo + " Pin removed — coordinates were outside the region.").strip()
    return row


def to_float(v: str | None) -> float | None:
    if blank(v):
        return None
    try:
        return float(str(v).strip())
    except ValueError:
        return None


def to_intish(v: str | None) -> str:
    if blank(v):
        return ""
    s = str(v).strip()
    try:
        return str(int(float(s)))
    except ValueError:
        return s


def compute_gap(row: dict) -> float | None:
    """Matched buy-side gap when both USD figures exist.

    Denominator is the U.S./allied figure. Positive ⇒ PRC figure is lower.
    """
    evidence = (row.get("evidence") or "").strip().lower()
    if evidence != "paired":
        # Still compute when both sides present (legacy proxies with both numbers)
        pass
    side = (row.get("side") or "").strip().lower()
    cside = (row.get("counterpart_side") or "").strip().lower()
    val = to_float(row.get("value_usd"))
    cval = to_float(row.get("counterpart_value_usd"))
    if val is None or cval is None:
        return None

    # Identify us/allied USD and prc USD
    us_usd = None
    prc_usd = None
    if side in ("us", "allied") and cside == "prc":
        us_usd, prc_usd = val, cval
    elif side == "prc" and cside in ("us", "allied"):
        us_usd, prc_usd = cval, val
    elif side == "prc" and blank(cside):
        return None
    else:
        # Fallback: treat value as non-PRC when side is not prc
        if side == "prc":
            prc_usd, us_usd = val, cval
        else:
            us_usd, prc_usd = val, cval

    if us_usd is None or prc_usd is None or us_usd == 0:
        return None
    return (us_usd - prc_usd) / us_usd


def load_codebook_meta() -> dict:
    if CODEBOOK_YML.exists():
        return yaml.safe_load(CODEBOOK_YML.read_text(encoding="utf-8")) or {}
    return {}


def load_rows(meta: dict | None = None) -> list[dict]:
    meta = meta or {}
    countries = region_countries(meta)
    with CODE.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for raw in reader:
            row = {k: (raw.get(k) or "").strip() for k in FIELDS}
            row = enforce_geography(row, countries)
            gap = compute_gap(row)
            if gap is None:
                row["gap"] = ""
            else:
                row["gap"] = f"{gap:.6f}".rstrip("0").rstrip(".")
                if abs(gap) < 1e-12:
                    row["gap"] = "0"
            rows.append(row)
        return rows


def write_codebook(rows: list[dict]) -> None:
    with CODE.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in FIELDS})


def evidence_index() -> dict[str, dict]:
    out = {}
    if not EVIDENCE_DIR.exists():
        return out
    for path in EVIDENCE_DIR.glob("*.json"):
        try:
            out[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
    return out


def in_region(country: str, countries: set[str]) -> bool:
    c = (country or "").strip()
    return bool(c) and c in countries


def row_to_json(row: dict, evidence: dict, countries: set[str]) -> dict:
    status = row["status"]
    evidence_class = row["evidence"]
    country = row["country"]
    # Map only in-region, non-archived, non-exclude rows with coordinates.
    # Blank country ⇒ never mapped (hunt seeds allowed until a site is named).
    eligible = (
        status in MAP_STATUS
        and evidence_class != "exclude"
        and in_region(country, countries)
    )
    lat = to_float(row.get("lat")) if eligible else None
    lon = to_float(row.get("lon")) if eligible else None
    if not eligible:
        lat, lon = None, None
    elif lat is None or lon is None:
        lat, lon = None, None

    return {
        "id": row["id"],
        "layer": row["layer"],
        "subcategory": row["subcategory"],
        "side": row["side"],
        "counterpart": row["counterpart"],
        "country": country,
        "asset": row["asset"],
        "investment_type": row["investment_type"],
        "value": to_float(row.get("value")),
        "currency": row["currency"],
        "value_usd": to_float(row.get("value_usd")),
        "fx_usd": to_float(row.get("fx_usd")),
        "fx_date": row["fx_date"],
        "year": to_intish(row.get("year")),
        "status": status,
        "lat": lat,
        "lon": lon,
        "geo_note": row["geo_note"],
        "evidence": evidence_class,
        "source_id": row["source_id"],
        "note": row["note"],
        "pair_id": row["pair_id"],
        "counterpart_side": row["counterpart_side"],
        "counterpart_actor": row["counterpart_actor"],
        "counterpart_value": to_float(row.get("counterpart_value")),
        "counterpart_currency": row["counterpart_currency"],
        "counterpart_value_usd": to_float(row.get("counterpart_value_usd")),
        "gap": to_float(row.get("gap")),
        "evidence_url": (evidence.get("url") or "") if evidence else "",
        "quote": (evidence.get("quote") or "") if evidence else "",
        "on_map": eligible and lat is not None and lon is not None,
        "on_readouts": (
            status in READOUT_STATUS
            and evidence_class != "exclude"
            and in_region(country, countries)
            and row["layer"] in ("infrastructure", "resources", "energy")
        ),
        "on_usd_sum": (
            status in READOUT_STATUS
            and evidence_class in USD_EVIDENCE
            and in_region(country, countries)
            and row["layer"] in ("infrastructure", "resources", "energy")
            and to_float(row.get("value_usd")) is not None
        ),
    }


def side_bucket(side: str) -> str:
    s = (side or "").lower()
    if s == "us":
        return "us"
    if s == "prc":
        return "prc"
    if s in ("allied", "other"):
        return "allied"
    return "other"


def build_layer_readouts(rows: list[dict]) -> list[dict]:
    # counts and usd sums per layer × side
    layers = ["infrastructure", "resources", "energy"]
    out = []
    for layer in layers:
        subset = [r for r in rows if r["layer"] == layer and r["on_readouts"]]
        counts = defaultdict(int)
        usd = defaultdict(float)
        usd_n = defaultdict(int)
        gaps = []
        for r in subset:
            b = side_bucket(r["side"])
            counts[b] += 1
            if r["on_usd_sum"] and r["value_usd"] is not None:
                usd[b] += r["value_usd"]
                usd_n[b] += 1
            if r["evidence"] == "paired" and r["gap"] is not None:
                gaps.append(r["gap"])
        out.append(
            {
                "layer": layer,
                "counts": {
                    "us": counts["us"],
                    "prc": counts["prc"],
                    "allied": counts["allied"],
                    "n": sum(counts.values()),
                },
                "usd": {
                    "us": usd["us"],
                    "us_n": usd_n["us"],
                    "prc": usd["prc"],
                    "prc_n": usd_n["prc"],
                    "allied": usd["allied"],
                    "allied_n": usd_n["allied"],
                },
                "matched_gaps": {
                    "n": len(gaps),
                    "values": gaps,
                },
            }
        )
    return out


def build_country_readouts(rows: list[dict]) -> list[dict]:
    bucket: dict[str, dict] = {}
    for r in rows:
        if not r["on_readouts"]:
            continue
        c = r["country"] or "(unspecified)"
        if c not in bucket:
            bucket[c] = {
                "country": c,
                "counts": {"us": 0, "prc": 0, "allied": 0, "n": 0},
                "usd": {
                    "us": 0.0,
                    "us_n": 0,
                    "prc": 0.0,
                    "prc_n": 0,
                    "allied": 0.0,
                    "allied_n": 0,
                },
                "by_layer": defaultdict(lambda: {"us": 0, "prc": 0, "allied": 0}),
            }
        b = side_bucket(r["side"])
        bucket[c]["counts"][b] += 1
        bucket[c]["counts"]["n"] += 1
        bucket[c]["by_layer"][r["layer"]][b] += 1
        if r["on_usd_sum"] and r["value_usd"] is not None:
            bucket[c]["usd"][b] += r["value_usd"]
            bucket[c]["usd"][f"{b}_n"] += 1

    out = []
    for c in sorted(bucket.keys()):
        item = bucket[c]
        item["by_layer"] = {
            layer: dict(sides) for layer, sides in sorted(item["by_layer"].items())
        }
        out.append(item)
    return out


def counts_meta(rows: list[dict]) -> dict:
    c = {
        "total": len(rows),
        "active": 0,
        "hunt": 0,
        "archived": 0,
        "paired": 0,
        "one_sided": 0,
        "proxy": 0,
        "exclude": 0,
        "documented": 0,
        "on_map": 0,
    }
    for r in rows:
        st = r.get("status") or ""
        if st in c:
            c[st] += 1
        ev = r.get("evidence") or ""
        if ev in c:
            c[ev] += 1
        if r.get("on_map"):
            c["on_map"] += 1
    return c


def taxonomy_for_dashboard(meta: dict) -> dict:
    layers = meta.get("layers") or {}
    out = {}
    for key, layer in layers.items():
        out[key] = {
            "label": layer.get("label", key),
            "marker_shape": layer.get("marker_shape", "circle"),
            "subcategories": {
                sk: (sv.get("label") if isinstance(sv, dict) else str(sv))
                for sk, sv in (layer.get("subcategories") or {}).items()
            },
        }
    return out


def main() -> None:
    meta = load_codebook_meta()
    countries = region_countries(meta)
    rows = load_rows(meta)
    write_codebook(rows)
    ev = evidence_index()
    observations = [row_to_json(r, ev.get(r["id"], {}), countries) for r in rows]

    site = meta.get("site") or {}
    geo = meta.get("geography") or {}
    dashboard = {
        "generated_from": "commanding-heights codebook",
        "title": site.get("title", "Commanding Heights of Latin America"),
        "subtitle": site.get("subtitle", ""),
        "caption": site.get(
            "caption",
            "Descriptive net assessment. Nothing here is a recommendation.",
        ),
        "geography": {
            "region": geo.get("region", "Latin America and the Caribbean"),
            "rule": geo.get("rule", ""),
            "countries": sorted(countries),
        },
        "colors": {
            "us": ((meta.get("sides") or {}).get("us") or {}).get("color", "#2f5d73"),
            "prc": ((meta.get("sides") or {}).get("prc") or {}).get("color", "#8c3a2b"),
            "allied": ((meta.get("sides") or {}).get("allied") or {}).get(
                "color", "#6b7c3c"
            ),
            "hunt": ((meta.get("sides") or {}).get("hunt") or {}).get(
                "color", "#8a9096"
            ),
        },
        "taxonomy": taxonomy_for_dashboard(meta),
        "meta": {
            "n_rows": len(rows),
            "counts": counts_meta(observations),
        },
        "layer_readouts": build_layer_readouts(observations),
        "country_readouts": build_country_readouts(observations),
        "lists": {
            "active": [
                o["id"]
                for o in observations
                if o["status"] == "active" and o["evidence"] != "exclude"
            ],
            "hunt": [o["id"] for o in observations if o["status"] == "hunt"],
            "paired": [o["id"] for o in observations if o["evidence"] == "paired"],
            "archived": [o["id"] for o in observations if o["status"] == "archived"],
        },
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "dashboard.json").write_text(
        json.dumps(dashboard, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "observations.json").write_text(
        json.dumps(observations, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("WROTE", OUT / "dashboard.json")
    print("WROTE", OUT / "observations.json")
    print(
        "rows",
        len(rows),
        "on_map",
        counts_meta(observations)["on_map"],
        "archived",
        counts_meta(observations)["archived"],
    )


if __name__ == "__main__":
    main()
