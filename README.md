# Buy-side price net

Matched buy-side prices: what a buyer pays on a U.S. (or allied) offer versus a PRC offer for the same specification. A lower matched PRC price is the asymmetry. Nothing here is a recommendation.

**Live site (after Pages is enabled on `docs/`):** [https://blpetrihos-hub.github.io/buy-side-net/](https://blpetrihos-hub.github.io/buy-side-net/)

Team 2, William & Mary GIAS Futures Group (Ben Petrihos, Anna Nichols, Ryan Silien).

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
```

`build_site_data.py` reads `data/codebook/observations.csv` and `data/attribution/evidence/`, recomputes `gap` and `on_scoreboard`, and writes `docs/data/dashboard.json` and `docs/data/observations.json`. The script is the scoring authority.

`render_bibliography.py` writes `docs/bibliography.html` and `docs/data/bibliography.json` from `sources/bibliography.yml`. Do not hand-edit the bibliography HTML after the renderer exists.

## Layout

| Path | Role |
| --- | --- |
| `data/codebook/observations.csv` | Price observations |
| `data/attribution/evidence/` | One JSON per row (URL, quote, retrieval date) |
| `sources/bibliography.yml` | Chicago citations |
| `process/build_site_data.py` | Scoreboard + map JSON |
| `process/render_bibliography.py` | Bibliography page |
| `docs/` | GitHub Pages (Leaflet map, no server) |
| `HUNT_STATE.md` | Active lane, next query, dry streak, seen URLs |

## Lanes

- `commanding_heights` — power equipment awards in Latin America
- `niobium` — FeNb and (later) Nb₃Sn wire
- `ai_chips` — USD per chip (export Nvidia vs Ascend)
- `icbc_finance` — public all-in rates only; never leaked ICBC records

## Requirements

```
pip install -r requirements.txt
```

Python 3.10+. Only `pyyaml` is required for the two build scripts.
