# Commanding heights of Latin America

Net assessment of PRC versus U.S. investment and presence across **Infrastructure**, **Scarce Natural Resources**, and **Energy** in Latin America and the Caribbean. Descriptive only — nothing here is a recommendation.

**Live site:** [https://blpetrihos-hub.github.io/buy-side-net/](https://blpetrihos-hub.github.io/buy-side-net/)

Team 2, William & Mary GIAS Futures Group. Hunt instructions: `BRIEF.md`.

## Preview locally

From `docs/`:

```
python -m http.server 8765
```

Then open `http://127.0.0.1:8765/`.

## Rebuild

From the repo root:

```
python process/build_site_data.py
python process/render_bibliography.py
python process/render_methods.py
```

- `build_site_data.py` reads `data/codebook/observations.csv` + evidence JSON, enforces the LatAm/Caribbean geography rule (out-of-region → archived, never mapped), recomputes gaps, writes `docs/data/dashboard.json` and `docs/data/observations.json`.
- `render_bibliography.py` writes `docs/bibliography.html` from `sources/bibliography.yml`.
- `render_methods.py` writes `docs/methods.html` from `data/codebook/codebook.yml` so methods always match the code.

## Layout

| Path | Role |
| --- | --- |
| `BRIEF.md` | Hunt-agent brief (successor to the buy-side brief) |
| `data/codebook/codebook.yml` | Taxonomy, sides, evidence, FX, readout rules, geography |
| `data/codebook/observations.csv` | Observations |
| `data/attribution/evidence/` | One JSON per row |
| `sources/bibliography.yml` | Chicago citations |
| `process/` | Build scripts |
| `docs/` | GitHub Pages (Leaflet map, no server) |
| `HUNT_STATE.md` | Active subcategory, next query, dry streak, seen URLs |

## Requirements

```
pip install -r requirements.txt
```

Python 3.10+. Only `pyyaml` is required for the build scripts.
