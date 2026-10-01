"""Render docs/bibliography.html from sources/bibliography.yml.

Only sources cited by at least one non-archived, map-layer observation
(infrastructure / resources / energy; status active or hunt) appear on the
page. Archived-only citations (legacy AI-chip, ICBC-finance, ABIROCHAS stone,
etc.) and uncitable rows stay in sources/bibliography.yml but are filtered
out at build time. Entries are grouped by the three codebook layers, then by
subcategory.
"""
from __future__ import annotations

import csv
import html
import json
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "bibliography.yml"
CODEBOOK_YML = ROOT / "data" / "codebook" / "codebook.yml"
OBS_CSV = ROOT / "data" / "codebook" / "observations.csv"
OUT = ROOT / "docs" / "bibliography.html"
JSON_OUT = ROOT / "docs" / "data" / "bibliography.json"

MAP_LAYERS = ("infrastructure", "resources", "energy")
MAP_STATUS = {"active", "hunt"}


def load_meta() -> dict:
    if CODEBOOK_YML.exists():
        return yaml.safe_load(CODEBOOK_YML.read_text(encoding="utf-8")) or {}
    return {}


def site_meta(meta: dict) -> dict:
    return meta.get("site") or {}


def layer_labels(meta: dict) -> dict[str, str]:
    layers = meta.get("layers") or {}
    out = {}
    for key in MAP_LAYERS:
        layer = layers.get(key) or {}
        out[key] = layer.get("label", key)
    return out


def subcategory_order(meta: dict) -> dict[str, list[tuple[str, str]]]:
    """layer -> [(subcategory_key, label), ...] in codebook order."""
    layers = meta.get("layers") or {}
    out: dict[str, list[tuple[str, str]]] = {}
    for key in MAP_LAYERS:
        layer = layers.get(key) or {}
        pairs = []
        for sk, sv in (layer.get("subcategories") or {}).items():
            label = sv.get("label") if isinstance(sv, dict) else str(sv)
            pairs.append((sk, label or sk))
        out[key] = pairs
    return out


def load_observations() -> list[dict]:
    with OBS_CSV.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def is_map_layer_obs(row: dict) -> bool:
    """Observation that belongs on the map layers (non-archived)."""
    return (
        (row.get("status") or "").strip() in MAP_STATUS
        and (row.get("layer") or "").strip() in MAP_LAYERS
    )


def citing_map_obs(
    entry: dict, by_source: dict[str, list[dict]], obs_by_id: dict[str, dict]
) -> list[dict]:
    """Map-layer observations that cite this source via source_id or supports."""
    seen: set[str] = set()
    out: list[dict] = []
    for row in by_source.get(entry["id"], []):
        if is_map_layer_obs(row) and row["id"] not in seen:
            seen.add(row["id"])
            out.append(row)
    for oid in entry.get("supports") or []:
        row = obs_by_id.get(oid)
        if row and is_map_layer_obs(row) and row["id"] not in seen:
            seen.add(row["id"])
            out.append(row)
    return out


def is_kept(entry: dict, by_source: dict[str, list[dict]]) -> bool:
    """Keep only if at least one map-layer observation lists this as source_id.

    Secondary `supports` links alone do not keep a source (so archived stone
    rows that also tag a graphite hunt seed do not retain ABIROCHAS entries).
    """
    return any(is_map_layer_obs(row) for row in by_source.get(entry["id"], []))


def nav(title: str, subtitle: str) -> str:
    return f"""
<header class="site-header">
  <div class="inner">
    <nav aria-label="Site">
      <a href="index.html">Interactive map</a>
      <a href="methods.html">Methods</a>
      <a href="bibliography.html" aria-current="page">Bibliography</a>
    </nav>
    <div class="header-brand">
      <p class="kicker">William &amp; Mary · GIAS Futures Group · Team 2</p>
      <h1>{html.escape(title)}</h1>
      <p class="sub">{html.escape(subtitle)}</p>
    </div>
  </div>
</header>
"""


def page(body: str, title: str, site_title: str, subtitle: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="css/site.css">
</head>
<body>
{nav(site_title, subtitle)}
<main class="page">
{body}
</main>
</body>
</html>
"""


def render_entry(e: dict, anchor_id: str | None = None) -> str:
    url = e.get("url") or ""
    link = (
        f'<p class="bib-url"><a href="{html.escape(url)}" rel="noopener">{html.escape(url)}</a></p>'
        if url
        else ""
    )
    supports = e.get("supports") or []
    if supports:
        # Show only map-layer supports when the filtered list is provided under _map_supports
        show = e.get("_map_supports") or supports
        sup = ", ".join(html.escape(str(s)) for s in show)
        sup_html = f'<p class="bib-supports">Supports: {sup}</p>'
    else:
        sup_html = '<p class="bib-supports">No codebook row. Context only.</p>'
    aid = anchor_id if anchor_id is not None else e["id"]
    return f"""
<article class="bib-entry" id="{html.escape(aid)}">
  <p class="bib-type">{html.escape(e.get("type", ""))} · <code>{html.escape(e["id"])}</code></p>
  <p class="bib-chicago">{html.escape(e.get("chicago", ""))}</p>
  {link}
  <p class="bib-ann">{html.escape(e.get("annotation", ""))}</p>
  {sup_html}
</article>
"""


def jump_nav(labels: dict[str, str]) -> str:
    links = []
    for key in MAP_LAYERS:
        links.append(
            f'<a href="#layer-{html.escape(key)}">{html.escape(labels[key])}</a>'
        )
    return (
        '<nav class="bib-jump" aria-label="Bibliography layers">'
        + " · ".join(links)
        + "</nav>"
    )


def main() -> None:
    meta = load_meta()
    site = site_meta(meta)
    site_title = site.get("title", "Commanding heights of Latin America")
    subtitle = site.get(
        "subtitle",
        "PRC versus U.S. investment and presence across infrastructure, scarce natural resources, and energy.",
    )
    labels = layer_labels(meta)
    sub_order = subcategory_order(meta)

    entries = yaml.safe_load(SRC.read_text(encoding="utf-8")) or []
    observations = load_observations()
    obs_by_id = {r["id"]: r for r in observations if r.get("id")}
    by_source: dict[str, list[dict]] = defaultdict(list)
    for row in observations:
        sid = (row.get("source_id") or "").strip()
        if sid:
            by_source[sid].append(row)

    kept: list[dict] = []
    # layer -> subcategory -> [entries] (unique per layer-subcat)
    by_layer_sub: dict[str, dict[str, list[dict]]] = {
        layer: defaultdict(list) for layer in MAP_LAYERS
    }
    # layer -> entries that span many subcategories (placed once at layer level)
    by_layer_broad: dict[str, list[dict]] = {layer: [] for layer in MAP_LAYERS}
    seen_layer_sub: dict[tuple[str, str, str], bool] = {}
    seen_layer_broad: dict[tuple[str, str], bool] = {}

    for e in entries:
        if not is_kept(e, by_source):
            continue
        map_obs = citing_map_obs(e, by_source, obs_by_id)
        # Prefer source_id citations for placement; fall back to supports map-obs
        place_obs = [r for r in by_source.get(e["id"], []) if is_map_layer_obs(r)]
        if not place_obs:
            place_obs = map_obs
        map_support_ids = sorted({r["id"] for r in map_obs})
        enriched = dict(e)
        enriched["_map_supports"] = map_support_ids
        kept.append(enriched)

        layers_subs: dict[str, set[str]] = defaultdict(set)
        for row in place_obs:
            layers_subs[row["layer"]].add(row["subcategory"])

        for layer, subs in layers_subs.items():
            if layer not in by_layer_sub:
                continue
            # Broad when the source hits more than two subcategories in this layer
            # (e.g. methods_clock hunt seeds) — list once at layer level.
            if len(subs) > 2:
                key = (layer, e["id"])
                if key not in seen_layer_broad:
                    seen_layer_broad[key] = True
                    by_layer_broad[layer].append(enriched)
                continue
            for sub in subs:
                key = (layer, sub, e["id"])
                if key in seen_layer_sub:
                    continue
                seen_layer_sub[key] = True
                by_layer_sub[layer][sub].append(enriched)

    # Stable sort within groups: type order then id
    type_rank = {"official": 0, "journalism": 1, "academic": 2, "methods": 3, "other": 4}

    def sort_key(e: dict):
        return (type_rank.get(e.get("type", "other"), 9), e.get("id", ""))

    for layer in MAP_LAYERS:
        by_layer_broad[layer].sort(key=sort_key)
        for sub in list(by_layer_sub[layer].keys()):
            by_layer_sub[layer][sub].sort(key=sort_key)

    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    json_payload = []
    for e in kept:
        item = {k: v for k, v in e.items() if not k.startswith("_")}
        item["map_supports"] = e.get("_map_supports") or []
        layers_hit = []
        for layer in MAP_LAYERS:
            in_broad = any(x["id"] == e["id"] for x in by_layer_broad[layer])
            in_sub = any(
                any(x["id"] == e["id"] for x in lst)
                for lst in by_layer_sub[layer].values()
            )
            if in_broad or in_sub:
                layers_hit.append(layer)
        item["layers"] = layers_hit
        json_payload.append(item)
    JSON_OUT.write_text(
        json.dumps(json_payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    used_anchors: set[str] = set()

    def entry_html(e: dict, layer: str, sub: str | None) -> str:
        base = e["id"]
        if base not in used_anchors:
            used_anchors.add(base)
            return render_entry(e, base)
        suffix = f"{layer}--{sub}" if sub else layer
        aid = f"{base}--{suffix}"
        used_anchors.add(aid)
        return render_entry(e, aid)

    blocks = [
        "<h2>Annotated bibliography</h2>",
        "<p>Public procurement notices, company filings, ministry and utility notices, "
        "port-authority releases, and published journalism. Built from "
        "<code>sources/bibliography.yml</code> so this page cannot drift. "
        "Only sources cited by at least one on-map observation "
        "(non-archived Infrastructure, Scarce Natural Resources, or Energy row) "
        "are listed; archived-only citations stay in the YAML and are omitted here. "
        "Press-only figures stay UNVERIFIED until a document confirms them. "
        "Grouped by codebook layer; a source may appear under more than one layer.</p>",
        jump_nav(labels),
    ]

    section_counts: dict[str, int] = {}
    for layer in MAP_LAYERS:
        label = labels[layer]
        blocks.append(f'<h3 id="layer-{html.escape(layer)}">{html.escape(label)}</h3>')
        layer_ids: set[str] = set()

        broad = by_layer_broad[layer]
        if broad:
            blocks.append("<h4>Across subcategories</h4>")
            for e in broad:
                blocks.append(entry_html(e, layer, None))
                layer_ids.add(e["id"])

        for sk, sub_label in sub_order[layer]:
            group = by_layer_sub[layer].get(sk) or []
            if not group:
                continue
            blocks.append(
                f"<h4 id=\"sub-{html.escape(layer)}-{html.escape(sk)}\">"
                f"{html.escape(sub_label)}</h4>"
            )
            for e in group:
                blocks.append(entry_html(e, layer, sk))
                layer_ids.add(e["id"])

        section_counts[layer] = len(layer_ids)
        if not layer_ids:
            blocks.append("<p class=\"empty\">No on-map sources in this layer yet.</p>")

    OUT.write_text(
        page(
            "\n".join(blocks),
            f"Bibliography · {site_title}",
            site_title,
            subtitle,
        ),
        encoding="utf-8",
    )
    print(
        "WROTE",
        OUT,
        "before=",
        len(entries),
        "after=",
        len(kept),
        "sections=",
        section_counts,
    )


if __name__ == "__main__":
    main()
