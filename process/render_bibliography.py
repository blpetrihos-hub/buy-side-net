"""Render docs/bibliography.html from sources/bibliography.yml."""
from __future__ import annotations

import html
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "bibliography.yml"
OUT = ROOT / "docs" / "bibliography.html"
JSON_OUT = ROOT / "docs" / "data" / "bibliography.json"

NAV = """
<header class="site-header">
  <div class="inner">
    <p class="kicker">William &amp; Mary · GIAS Futures Group · Team 2</p>
    <h1>Where the PRC price is the lower bid</h1>
    <p class="sub">Matched buy-side prices from the 30 September pitches. A gap is a measurement. The page does not recommend a response.</p>
    <nav>
      <a href="index.html">Dashboard</a>
      <a href="methods.html">Methods</a>
      <a href="bibliography.html" aria-current="page">Bibliography</a>
    </nav>
  </div>
</header>
"""


def page(body: str, title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="css/site.css">
</head>
<body>
{NAV}
<main class="page">
{body}
</main>
</body>
</html>
"""


def render_entry(e: dict) -> str:
    url = e.get("url") or ""
    link = (
        f'<p class="bib-url"><a href="{html.escape(url)}" rel="noopener">{html.escape(url)}</a></p>'
        if url
        else ""
    )
    supports = e.get("supports") or []
    if supports:
        sup = ", ".join(html.escape(str(s)) for s in supports)
        sup_html = f'<p class="bib-supports">Supports: {sup}</p>'
    else:
        sup_html = '<p class="bib-supports">No codebook row. Context only.</p>'
    return f"""
<article class="bib-entry" id="{html.escape(e["id"])}">
  <p class="bib-type">{html.escape(e.get("type", ""))} · <code>{html.escape(e["id"])}</code></p>
  <p class="bib-chicago">{html.escape(e.get("chicago", ""))}</p>
  {link}
  <p class="bib-ann">{html.escape(e.get("annotation", ""))}</p>
  {sup_html}
</article>
"""


def main() -> None:
    entries = yaml.safe_load(SRC.read_text(encoding="utf-8")) or []
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    blocks = [
        "<h2>Annotated bibliography</h2>",
        "<p>Public procurement notices, commodity quotes, company filings, exchange or statistical releases, and published journalism. Built from <code>sources/bibliography.yml</code> so this page cannot drift. Press-only figures stay UNVERIFIED proxy rows until a document confirms them.</p>",
        "<p>Excluded from the median: pitch deck color, market-share narratives, loan sizes without a rate, and any leaked ICBC internal record set.</p>",
    ]
    order = ["official", "journalism", "academic", "methods", "other"]
    labels = {
        "official": "Official / primary",
        "journalism": "Journalism",
        "academic": "Academic / practitioner",
        "methods": "Methods",
        "other": "Other",
    }
    by = {}
    for e in entries:
        by.setdefault(e.get("type", "other"), []).append(e)
    for kind in order:
        if kind not in by:
            continue
        blocks.append(f"<h3>{labels.get(kind, kind)}</h3>")
        for e in by[kind]:
            blocks.append(render_entry(e))
    for kind, group in by.items():
        if kind in order:
            continue
        blocks.append(f"<h3>{html.escape(str(kind))}</h3>")
        for e in group:
            blocks.append(render_entry(e))
    OUT.write_text(
        page("\n".join(blocks), "Bibliography · Where the PRC price is the lower bid"),
        encoding="utf-8",
    )
    print("WROTE", OUT, "n=", len(entries))


if __name__ == "__main__":
    main()
