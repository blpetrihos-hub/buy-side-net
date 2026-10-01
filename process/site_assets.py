"""Stamp local static asset URLs in docs HTML with a cache-busting query.

Build scripts call stamp_docs_html() (or css_href / js_src) so browsers fetch
fresh css/js after every build. Version is the current git short SHA when
available, otherwise a short content hash of the referenced files.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

_CSS_RE = re.compile(
    r'(href=["\'])(css/[^"\']+\.css)(?:\?v=[^"\']*)?(["\'])'
)
_JS_RE = re.compile(
    r'(src=["\'])(js/[^"\']+\.js)(?:\?v=[^"\']*)?(["\'])'
)


def asset_version() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        if out:
            return out
    except (OSError, subprocess.CalledProcessError):
        pass
    digest = hashlib.sha1()
    for path in sorted((DOCS / "css").glob("*.css")) + sorted(
        (DOCS / "js").glob("*.js")
    ):
        digest.update(path.name.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()[:10]


def css_href(path: str = "css/site.css", version: str | None = None) -> str:
    v = version or asset_version()
    return f"{path}?v={v}"


def js_src(path: str = "js/dashboard.js", version: str | None = None) -> str:
    v = version or asset_version()
    return f"{path}?v={v}"


def stamp_html_text(text: str, version: str | None = None) -> str:
    v = version or asset_version()

    def _css(m: re.Match[str]) -> str:
        return f"{m.group(1)}{m.group(2)}?v={v}{m.group(3)}"

    def _js(m: re.Match[str]) -> str:
        return f"{m.group(1)}{m.group(2)}?v={v}{m.group(3)}"

    return _JS_RE.sub(_js, _CSS_RE.sub(_css, text))


def stamp_html_file(path: Path, version: str | None = None) -> bool:
    original = path.read_text(encoding="utf-8")
    stamped = stamp_html_text(original, version=version)
    if stamped == original:
        return False
    path.write_text(stamped, encoding="utf-8")
    return True


def stamp_docs_html(version: str | None = None) -> list[Path]:
    """Rewrite local css/js refs in every docs/*.html page. Returns changed paths."""
    v = version or asset_version()
    changed: list[Path] = []
    for path in sorted(DOCS.glob("*.html")):
        if stamp_html_file(path, version=v):
            changed.append(path)
    return changed
