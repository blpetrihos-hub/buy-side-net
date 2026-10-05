updated: 2026-10-05
cycle: 243
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 244 shuffle_seed=20261244; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us404/prc373/allied400); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Neoenergia Cosern Estivas/Tabatinga nested CapEx if not loaded. No U.S. territories.
next_row_id: (follow cycle-244 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 243) ===
# Filled this cycle: Chile×other_renewables NEW×2 (us AES Chile CapEx >USD 1.9bn
#   2024–2027; allied Generadora Metropolitana Dune Plus USD 629m); Brazil×other_renewables
#   NEW (prc Envision SAF USD 1bn); Brazil×power_plants_grid NEW (allied Neoenergia
#   Oeste Baiano ~R$2bn nested).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (AES Chile CapEx NEW + honest residual).
# PRC equal-budget: Envision SAF NEW.

# === Cycle 243 (seed 20261243) ===
# Shuffled order (BRIEF.md numbered + Random(20261243).shuffle): port_ownership,
#   lithium, bridges_roads, port_cranes, other_renewables, niobium, graphite,
#   engineering_epc, fission_smr, balsa, water, copper, nickel, wind, solar,
#   building_materials, power_plants_grid, rail.
# Logged 4 new (1 US / 1 PRC / 2 allied / 0 other; ≥1/3 US hunt budget via AES Chile
#   CapEx NEW + honest residual):
#   us other_renewables NEW: aes_andes_chile_capex_1p9bn_2024_2027 (USD 1.9bn floor).
#   prc other_renewables NEW: envision_brazil_saf_1bn_2025 (USD 1bn press).
#   allied power_plants_grid NEW: neoenergia_oeste_baiano_2bn_brl_2026 (~USD 385.20m).
#   allied other_renewables NEW: gen_metro_dune_plus_629m_2025 (USD 629m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: port_ownership, lithium, bridges_roads, port_cranes, niobium,
#   graphite, engineering_epc, fission_smr, balsa, water, copper, nickel, wind, solar,
#   building_materials, rail
#   (catalog dense; Microsoft Chile IDC ecosystem; ENGIE 2026 CapEx plan figure not
#   cleanly extractable from IR PDF; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 243: us404 / prc373 / allied400 / other91 (n=1268).
shuffle_seed: 20261243
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_ownership
- resources/lithium
- infrastructure/bridges_roads
- infrastructure/port_cranes
- energy/other_renewables
- resources/niobium
- resources/graphite
- infrastructure/engineering_epc
- energy/fission_smr
- resources/balsa
- resources/water
- resources/copper
- resources/nickel
- energy/wind
- energy/solar
- infrastructure/building_materials
- energy/power_plants_grid
- infrastructure/rail
rows_found_this_cycle:
  infrastructure/port_ownership: 0
  resources/lithium: 0
  infrastructure/bridges_roads: 0
  infrastructure/port_cranes: 0
  energy/other_renewables: 3
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  energy/fission_smr: 0
  resources/balsa: 0
  resources/water: 0
  resources/copper: 0
  resources/nickel: 0
  energy/wind: 0
  energy/solar: 0
  infrastructure/building_materials: 0
  energy/power_plants_grid: 1
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 2
  other: 0
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 404
  prc: 373
  allied: 400
  other: 91
  n: 1268
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
