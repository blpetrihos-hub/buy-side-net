"""Generate docs/methods.html from data/codebook/codebook.yml so methods match code."""
from __future__ import annotations

import html
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_assets import css_href, stamp_docs_html  # noqa: E402

SRC = ROOT / "data" / "codebook" / "codebook.yml"
OUT = ROOT / "docs" / "methods.html"


def esc(s) -> str:
    return html.escape("" if s is None else str(s))


def nav(title: str, subtitle: str) -> str:
    return f"""
<header class="site-header">
  <div class="inner">
    <nav aria-label="Site">
      <a href="index.html">Interactive map</a>
      <a href="methods.html" aria-current="page">Methods</a>
      <a href="bibliography.html">Bibliography</a>
    </nav>
    <div class="header-brand">
      <p class="kicker">William &amp; Mary · GIAS Futures Group · Team 2</p>
      <h1>{esc(title)}</h1>
      <p class="sub">{esc(subtitle)}</p>
    </div>
  </div>
</header>
"""


def main() -> None:
    meta = yaml.safe_load(SRC.read_text(encoding="utf-8")) or {}
    site = meta.get("site") or {}
    method = meta.get("method") or {}
    title = site.get("title", "Commanding Heights of Latin America")
    subtitle = site.get("subtitle", "")

    blocks: list[str] = []
    blocks.append("<h2>What this measures</h2>")
    blocks.append(
        "<p>This site is a <strong>net assessment</strong> of the commanding heights of "
        "Latin America: comparative, diagnostic, and forward-looking. It compares U.S. and "
        "PRC investment and presence across three layers — Infrastructure, Scarce Natural "
        "Resources, and Energy — with allied/other non-PRC actors shown separately. "
        "The product is an asymmetry you can check. "
        f"{esc(method.get('voice', 'Descriptive. No recommendations.'))}</p>"
    )
    blocks.append(
        f"<p>The clock is <strong>{esc(method.get('timeframe_horizon', '2026–2036'))}</strong>. "
        f"Observation years may run <strong>{esc(method.get('observation_years', '2021–2026'))}</strong>. "
        f"Citations are {esc(method.get('citations', 'Chicago'))}. "
        f"{esc(method.get('never_fabricate_rule', ''))}</p>"
    )
    geo = meta.get("geography") or {}
    blocks.append("<h2>Geography</h2>")
    blocks.append(
        f"<p><strong>{esc(geo.get('region', 'Latin America and the Caribbean'))} only.</strong> "
        f"{esc(geo.get('rule', method.get('geography', '')))}</p>"
    )
    countries = geo.get("latin_america_caribbean") or []
    if countries:
        blocks.append(
            "<p>Allowed countries (codebook): "
            + ", ".join(esc(c) for c in countries)
            + ".</p>"
        )

    blocks.append("<h2>Three layers</h2>")
    blocks.append("<p>Generated from <code>data/codebook/codebook.yml</code>. Marker shape encodes layer; color encodes side.</p>")
    for layer_key, layer in (meta.get("layers") or {}).items():
        shape = esc(layer.get("marker_shape", "circle"))
        blocks.append(
            f"<h3>{esc(layer.get('label', layer_key))} "
            f"(<code>{esc(layer_key)}</code> · marker: {shape})</h3>"
        )
        blocks.append("<ul>")
        for sk, sv in (layer.get("subcategories") or {}).items():
            label = sv.get("label") if isinstance(sv, dict) else sv
            blocks.append(f"<li><code>{esc(sk)}</code> — {esc(label)}</li>")
        blocks.append("</ul>")

    blocks.append("<h2>Side definitions</h2>")
    blocks.append("<ul>")
    for sk, sv in (meta.get("sides") or {}).items():
        if sk == "hunt":
            continue
        note = f" {esc(sv.get('note'))}" if sv.get("note") else ""
        blocks.append(
            f"<li><code>{esc(sk)}</code> — {esc(sv.get('label', sk))} "
            f"(color <code>{esc(sv.get('color', ''))}</code>).{note}</li>"
        )
    blocks.append("</ul>")

    blocks.append("<h2>Investment types</h2>")
    blocks.append("<ul>")
    for k, label in (meta.get("investment_types") or {}).items():
        blocks.append(f"<li><code>{esc(k)}</code> — {esc(label)}</li>")
    blocks.append("</ul>")

    blocks.append("<h2>Evidence classes</h2>")
    blocks.append("<ul>")
    for k, ev in (meta.get("evidence_classes") or {}).items():
        flags = []
        if ev.get("on_map"):
            flags.append("on map")
        if ev.get("on_usd_sum"):
            flags.append("in USD sums")
        if ev.get("on_gap_readout"):
            flags.append("gap readout")
        flag_s = "; ".join(flags) if flags else "off map and sums"
        blocks.append(
            f"<li><code>{esc(k)}</code> — {esc(ev.get('description', ''))} "
            f"<em>({esc(flag_s)})</em></li>"
        )
    blocks.append("</ul>")

    blocks.append("<h2>Status</h2>")
    blocks.append("<ul>")
    for k, st in (meta.get("status_values") or {}).items():
        extra = f" {esc(st.get('description'))}" if st.get("description") else ""
        blocks.append(
            f"<li><code>{esc(k)}</code> — {esc(st.get('label', k))}."
            f"{extra}</li>"
        )
    blocks.append("</ul>")

    fx = meta.get("fx_rule") or {}
    blocks.append("<h2>FX rule</h2>")
    blocks.append(f"<p>{esc(fx.get('rule', ''))}</p>")

    blocks.append("<h2>What counts toward each readout</h2>")
    readouts = meta.get("readouts") or {}
    blocks.append("<ul>")
    for key in (
        "layer_counts",
        "layer_usd",
        "country_counts",
        "country_usd",
        "matched_gap",
    ):
        r = readouts.get(key) or {}
        if r:
            blocks.append(
                f"<li><strong>{esc(key)}</strong> — {esc(r.get('description', ''))}</li>"
            )
    blocks.append("</ul>")
    excl = readouts.get("excluded_from_readouts") or []
    if excl:
        blocks.append("<p>Excluded from readouts:</p><ul>")
        for item in excl:
            blocks.append(f"<li>{esc(item)}</li>")
        blocks.append("</ul>")

    blocks.append("<h2>Observation fields</h2>")
    blocks.append("<ul>")
    for field in meta.get("observation_fields") or []:
        name = field.get("name", "")
        desc = field.get("description", "")
        allowed = field.get("allowed")
        extra = f" Allowed: {', '.join(allowed)}." if allowed else ""
        blocks.append(
            f"<li><code>{esc(name)}</code>"
            + (f" — {esc(desc)}" if desc else "")
            + esc(extra)
            + "</li>"
        )
    blocks.append("</ul>")

    bib = meta.get("bibliography") or {}
    if bib:
        blocks.append("<h2>Bibliography</h2>")
        blocks.append(f"<p>{esc(bib.get('rule', ''))}</p>")

    blocks.append("<h2>Public-source limits</h2>")
    blocks.append("<ul>")
    for item in meta.get("public_source_limits") or []:
        blocks.append(f"<li>{esc(item)}</li>")
    blocks.append("</ul>")

    blocks.append("<h2>Smith’s rules (always in force)</h2>")
    blocks.append(
        "<ol>"
        "<li><strong>Method</strong> is net assessment: comparative, diagnostic, forward-looking. "
        "The product is an asymmetry you can check.</li>"
        "<li><strong>Timeframe</strong> on this page is 2026–2036. Observations may be dated "
        "2021–2026 when that is the award or deal year.</li>"
        "<li><strong>Mandate</strong>: U.S. and PRC capabilities and presence in Latin America "
        "across the three layers.</li>"
        "<li><strong>Voice</strong>: descriptive. The pages do not say “the U.S. should,” and "
        "they do not offer an implementation roadmap.</li>"
        "<li><strong>Citations</strong>: Chicago. Never fabricate a source, a value, a buyer, "
        "or a coordinate.</li>"
        "</ol>"
    )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Methods · {esc(title)}</title>
  <link rel="stylesheet" href="{css_href()}">
</head>
<body>
{nav(title, subtitle)}
<main class="page">
{"".join(blocks)}
<p class="note">This page is generated by <code>process/render_methods.py</code> from
<code>data/codebook/codebook.yml</code>. Do not hand-edit it.</p>
</main>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print("WROTE", OUT)
    for path in stamp_docs_html():
        print("STAMPED", path)


if __name__ == "__main__":
    main()
