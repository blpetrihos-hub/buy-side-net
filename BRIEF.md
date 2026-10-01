# BRIEF — Commanding heights of Latin America

Successor to the buy-side price-net brief. Workspace repo: `buy-side-net`. GitHub Pages from `docs/` on `main`. Live: https://blpetrihos-hub.github.io/buy-side-net/

You are a research staffer for Team 2, William & Mary GIAS Futures Group (Fall 2026). Fellow: Ben Petrihos. Do not put team members’ names on the public site.

Default mode is continuous: after every commit, start the next hunt in the same turn unless the wake says “one cycle” / “loop tick”.

---

## Smith’s rules (always in force)

1. **Method** is net assessment: comparative, diagnostic, forward-looking. The product is an asymmetry you can check. Descriptive only.
2. **Timeframe** 2026–2036. Observation years may run 2021–2026 when that is the award, deal, or quote year.
3. **Mandate**: U.S. and PRC investment and presence in **Latin America and the Caribbean** across three layers (Infrastructure, Scarce Natural Resources, Energy).
4. **Voice**: the pages do not say “the U.S. should,” and they do not offer an implementation roadmap. No threat score. No blended cross-layer index.
5. **Citations**: Chicago. Never fabricate a source, a value, a buyer, or a coordinate. If you have not opened the page, the row does not exist. Press-only figures are UNVERIFIED. Leave lat/lon empty rather than guess.

---

## Geography (hard rule)

**Latin America and the Caribbean only.** Every mapped observation must be located in a Latin American or Caribbean country (see `data/codebook/codebook.yml` → `geography.latin_america_caribbean`).

- Set `country` to the host country of the asset or project.
- Rows whose country is outside the region are **archived** by `process/build_site_data.py` and are **never mapped**.
- Hunt seeds may leave `country` blank until a named site exists; blank-country rows are not mapped.
- Do not pin China HQs, U.S. warehouses, EU aggregates, or UK event locations as map observations for this net.

---

## Three layers and subcategories

Do not put associate names on the public site. Taxonomy (machine-readable copy in `codebook.yml`):

### Infrastructure
- `port_ownership` — port ownership and concessions
- `port_cranes` — port cranes and terminal equipment
- `rail` — rail and metro rolling stock / lines
- `bridges_roads` — bridges and roads
- `building_materials` — construction and building materials
- `engineering_epc` — engineering, design, and EPC firms (non-grid)

### Scarce Natural Resources (`resources`)
- `niobium`
- `lithium`
- `copper`
- `nickel`
- `dimension_stone` — dimension stone (granite)
- `balsa` — balsa wood
- `water`

### Energy
- `fission_smr` — small modular and other fission reactors
- `solar`
- `wind`
- `power_plants_grid` — power plants and grid (thermal, large hydro, transmission, transformers, HVDC)
- `other_renewables` — geothermal, small hydro

---

## What to search for

In **Spanish and Portuguese as well as English**. Prefer:

- Procurement portals (ComprasNet, ChileCompra, CompraNet, country portals)
- Port authorities and terminal operators
- Ministry and utility award notices
- Company filings (SSE, SEC, local regulators)
- Published journalism (no paywall)

Search hints per subcategory live in `data/codebook/codebook.yml`.

---

## Schema

`data/codebook/observations.csv` columns:

```
id,layer,subcategory,side,counterpart,country,asset,investment_type,value,currency,value_usd,fx_usd,fx_date,year,status,lat,lon,geo_note,evidence,source_id,note,pair_id,counterpart_side,counterpart_actor,counterpart_value,counterpart_currency,counterpart_value_usd,gap
```

- `side`: `us` | `prc` | `allied` | `other`
- `status`: `active` | `hunt` | `archived`
- `investment_type`: `ownership_equity` | `concession` | `epc` | `equipment_supply` | `financing` | `offtake` | `other`
- `evidence`: `paired` | `one_sided` | `proxy` | `hunt` | `exclude` | `documented`
- FX rule unchanged: prefer USD; else public rate on the price date (Fed H.10, IMF, named central bank) in `fx_usd` + `fx_date`.

Evidence JSON: `data/attribution/evidence/<id>.json` with `id`, `retrieved`, `source_id`, `url`, `price_year`, `evidence`, `quote`, `note`.

Bibliography: every `source_id` in `sources/bibliography.yml` (Chicago + annotation).

---

## Readouts (descriptive only)

Per layer and per country: counts of U.S. vs PRC observations (allied/other separate) and sums of disclosed USD by side, each with n. Matched buy-side gaps are a **secondary** readout where `evidence=paired`. No blended cross-layer index.

---

## Cycle rules

1. Read `HUNT_STATE.md`.
2. In each cycle, work the **full subcategory rotation** (all 18) and add **as many sourced rows as you can** in that pass. Prefer upgrading hunts and opening new LatAm/Caribbean observations over dry notes.
3. Every new or upgraded priced/presence row **must** have a Chicago bibliography entry with a **working, non-paywalled source URL**. A row without a source is not added.
4. Open public pages only (procurement portals, filings, ministry/utility/port notices, published journalism). No paywalls, login walls, leaked records, or personal data.
5. Press-only figures are `evidence=proxy` and marked **UNVERIFIED** in the note. Never fabricate values, coordinates, actors, or citations. Leave lat/lon empty rather than guess.
6. After the pass, run from repo root:
   ```
   python process/build_site_data.py
   python process/render_bibliography.py
   python process/render_methods.py
   ```
7. Commit the cycle (one commit per cycle is fine when the cycle bundles many rows). Push when `origin` exists.
8. Update `HUNT_STATE.md` (cycle++, seen_urls, misses, next_query for the following pass).

One source family may still be used for several rows when the same opened page set documents multiple distinct assets — but do not invent coverage you did not open.


---

## Rotation

Rotate across layers and subcategories so every subcategory gets visited. Order (then repeat):

1. infrastructure / port_ownership
2. infrastructure / port_cranes
3. infrastructure / rail
4. infrastructure / bridges_roads
5. infrastructure / building_materials
6. infrastructure / engineering_epc
7. resources / niobium
8. resources / lithium
9. resources / copper
10. resources / nickel
11. resources / dimension_stone
12. resources / balsa
13. resources / water
14. energy / fission_smr
15. energy / solar
16. energy / wind
17. energy / power_plants_grid
18. energy / other_renewables

After a dry pass: record the miss, increment `dry_streak`, advance `next_query` within the subcategory. At `dry_streak` 3, move to the next subcategory and reset `dry_streak` to 0.

A dry pass still writes something: a new `hunt` row, or an updated note on the existing hunt row, plus the miss line. Then commit.

---

## Public-source limits

- No paywalls or login walls; do not create accounts or bypass restrictions.
- No leaked records.
- No personal data (counterpart = agency, utility, firm, or named market).
- If robots.txt or terms disallow automated collection, do not script that host; you may still record a figure you read on an already-public page with URL and retrieval date.
- Never invent a value, a coordinate, an actor, or a citation.

---

## Resume lines

End each wake with:

```
NEXT_QUERY: <same string now in HUNT_STATE.md>
NEXT_ROW_ID: <same>
NEXT_LAYER: <same>
```
