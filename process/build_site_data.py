"""Read codebook + evidence; recompute gap and on_scoreboard; write docs/data JSON."""
from __future__ import annotations

import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "data" / "codebook" / "observations.csv"
EVIDENCE_DIR = ROOT / "data" / "attribution" / "evidence"
OUT = ROOT / "docs" / "data"

FIELDS = [
    "id",
    "lane",
    "spec_class",
    "evidence",
    "country",
    "buyer",
    "seller_us",
    "seller_prc",
    "city",
    "lat",
    "lon",
    "geo_note",
    "price_year",
    "spec",
    "unit",
    "currency",
    "fx_usd",
    "fx_date",
    "us_price",
    "prc_price",
    "us_price_usd",
    "prc_price_usd",
    "gap",
    "us_side",
    "on_scoreboard",
    "source_id",
    "note",
]

GOODS_LANES = {"commanding_heights", "niobium", "ai_chips"}
FINANCE_LANE = "icbc_finance"


def blank(v: str | None) -> bool:
    return v is None or str(v).strip() == ""


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


def scores(row: dict) -> tuple[float | None, str]:
    """Return (gap, on_scoreboard yes|no). Script is authority over CSV yes."""
    evidence = (row.get("evidence") or "").strip().lower()
    us_side = (row.get("us_side") or "").strip().lower()
    us_usd = to_float(row.get("us_price_usd"))
    prc_usd = to_float(row.get("prc_price_usd"))

    gap = None
    if us_usd is not None and prc_usd is not None and us_usd != 0:
        gap = (us_usd - prc_usd) / us_usd

    on = "no"
    if evidence == "paired" and us_side == "us" and us_usd is not None and prc_usd is not None:
        if not blank(row.get("spec_class")) and not blank(row.get("price_year")) and not blank(row.get("unit")):
            fx = to_float(row.get("fx_usd"))
            fx_ok = fx == 1.0 or (fx is not None and not blank(row.get("fx_date")))
            # USD quotes: fx blank or 1 is fine when currency is USD
            currency = (row.get("currency") or "").strip().upper()
            if currency == "USD" and (fx is None or fx == 1.0):
                fx_ok = True
            if fx_ok and us_usd != 0:
                on = "yes"

    return gap, on


def median_or_none(vals: list[float]) -> float | None:
    if not vals:
        return None
    return float(statistics.median(vals))


def load_rows() -> list[dict]:
    with CODE.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for raw in reader:
            row = {k: (raw.get(k) or "").strip() for k in FIELDS}
            gap, on = scores(row)
            row["gap"] = "" if gap is None else f"{gap:.6f}".rstrip("0").rstrip(".")
            if gap is not None and abs(gap) < 1e-12:
                row["gap"] = "0"
            row["on_scoreboard"] = on
            # Keep numeric strings tidy for JSON
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


def row_to_json(row: dict, evidence: dict) -> dict:
    lat = to_float(row.get("lat"))
    lon = to_float(row.get("lon"))
    gap = to_float(row.get("gap"))
    return {
        "id": row["id"],
        "lane": row["lane"],
        "spec_class": row["spec_class"],
        "evidence": row["evidence"],
        "country": row["country"],
        "buyer": row["buyer"],
        "seller_us": row["seller_us"],
        "seller_prc": row["seller_prc"],
        "city": row["city"],
        "lat": lat,
        "lon": lon,
        "geo_note": row["geo_note"],
        "price_year": to_intish(row.get("price_year")),
        "spec": row["spec"],
        "unit": row["unit"],
        "currency": row["currency"],
        "fx_usd": to_float(row.get("fx_usd")),
        "fx_date": row["fx_date"],
        "us_price": to_float(row.get("us_price")),
        "prc_price": to_float(row.get("prc_price")),
        "us_price_usd": to_float(row.get("us_price_usd")),
        "prc_price_usd": to_float(row.get("prc_price_usd")),
        "gap": gap,
        "us_side": row["us_side"],
        "on_scoreboard": row["on_scoreboard"] == "yes",
        "source_id": row["source_id"],
        "note": row["note"],
        "evidence_url": (evidence.get("url") or "") if evidence else "",
        "quote": (evidence.get("quote") or "") if evidence else "",
    }


def build_scoreboards(rows: list[dict]) -> dict:
    goods: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    finance: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        if row["on_scoreboard"] != "yes":
            continue
        gap = to_float(row.get("gap"))
        if gap is None:
            continue
        lane = row["lane"]
        spec = row["spec_class"]
        if lane in GOODS_LANES:
            goods[lane][spec].append(gap)
        elif lane == FINANCE_LANE:
            finance[spec].append(gap)

    goods_out = []
    for lane in sorted(GOODS_LANES):
        specs = goods.get(lane, {})
        for spec in sorted(specs.keys()):
            vals = specs[spec]
            goods_out.append(
                {
                    "lane": lane,
                    "spec_class": spec,
                    "median_gap": median_or_none(vals),
                    "n": len(vals),
                }
            )
        if lane not in goods:
            # still show empty lane shell only if we want; prefer only populated
            pass

    finance_out = []
    for spec in sorted(finance.keys()):
        vals = finance[spec]
        finance_out.append(
            {
                "lane": FINANCE_LANE,
                "spec_class": spec,
                "median_gap": median_or_none(vals),
                "n": len(vals),
            }
        )

    return {"goods": goods_out, "finance": finance_out}


def build_country_strip(rows: list[dict]) -> list[dict]:
    # country -> lane -> gaps
    bucket: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        if row["on_scoreboard"] != "yes":
            continue
        country = row["country"] or "(unspecified)"
        gap = to_float(row.get("gap"))
        if gap is None:
            continue
        bucket[country][row["lane"]].append(gap)

    out = []
    for country in sorted(bucket.keys()):
        lines = []
        for lane in ["commanding_heights", "niobium", "ai_chips", "icbc_finance"]:
            vals = bucket[country].get(lane)
            if not vals:
                continue
            lines.append(
                {
                    "lane": lane,
                    "median_gap": median_or_none(vals),
                    "n": len(vals),
                }
            )
        out.append({"country": country, "lanes": lines})
    return out


def counts(rows: list[dict]) -> dict:
    c = {"paired": 0, "proxy": 0, "one_sided": 0, "hunt": 0, "exclude": 0, "scored": 0}
    for row in rows:
        ev = (row.get("evidence") or "").lower()
        if ev in c:
            c[ev] += 1
        if row["on_scoreboard"] == "yes":
            c["scored"] += 1
    return c


def main() -> None:
    rows = load_rows()
    write_codebook(rows)
    ev = evidence_index()
    observations = [row_to_json(r, ev.get(r["id"], {})) for r in rows]

    dashboard = {
        "generated_from": "buy-side observations codebook",
        "caption": (
            "Score a pair only when both prices are public and the specification matches. "
            "A lower PRC price is the asymmetry. Hunt pins are places still missing a number. "
            "Nothing here is a recommendation."
        ),
        "meta": {
            "n_rows": len(rows),
            "counts": counts(rows),
        },
        "scoreboards": build_scoreboards(rows),
        "country_strip": build_country_strip(rows),
        "lists": {
            "scored": [o["id"] for o in observations if o["on_scoreboard"]],
            "proxy_one_sided": [
                o["id"]
                for o in observations
                if o["evidence"] in ("proxy", "one_sided")
            ],
            "hunt": [o["id"] for o in observations if o["evidence"] == "hunt"],
            "exclude": [o["id"] for o in observations if o["evidence"] == "exclude"],
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
    print("rows", len(rows), "scored", counts(rows)["scored"])


if __name__ == "__main__":
    main()
