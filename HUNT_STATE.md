updated: 2026-10-05
cycle: 240
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 241 shuffle_seed=20261241; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us399/prc370/allied397); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-241 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 240) ===
# Filled this cycle: Brazil×lithium CapEx-fill (us Atlas Neves 71% contracted
#   ~USD 34.31m); Brazil×power_plants_grid CapEx-upgrade (prc SPIC São Simão UG7
#   R$1.4bn); Brazil×port_cranes NEW (allied Portonave TIL >R$500m electric package).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Atlas Neves CapEx-fill + honest residual).
# PRC equal-budget: SPIC São Simão CapEx-upgrade.

# === Cycle 240 (seed 20261240) ===
# Shuffled order (BRIEF.md numbered + Random(20261240).shuffle): rail, solar,
#   port_cranes, building_materials, graphite, niobium, other_renewables, wind,
#   port_ownership, lithium, engineering_epc, balsa, power_plants_grid,
#   bridges_roads, fission_smr, nickel, copper, water.
# Logged 1 new + 2 CapEx-fill/upgrade (1 US / 1 PRC / 1 allied / 0 other; ≥1/3 US hunt
#   budget via Atlas Neves CapEx-fill + honest residual):
#   us lithium CapEx-fill: atlas_lithium_neves_71pct_capex_2026 (~USD 34.31m contracted).
#   prc power_plants_grid CapEx-upgrade: spic_sao_simao_ug7_lrcap_2026 (R$1.4bn).
#   allied port_cranes NEW: portonave_electric_equip_500m_brl_2026 (~USD 96.30m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: rail, solar, building_materials, graphite, niobium,
#   other_renewables, wind, port_ownership, engineering_epc, balsa, bridges_roads,
#   fission_smr, nickel, copper, water
#   (catalog dense; CRRC Salvador/Line4 / ZPMC Santos / Konecranes Portonave RTG /
#   State Grid GATE / ENGIE Jaguara already loaded; Konecranes Arica CapEx
#   undisclosed; Aldesa EUR / RAP / Huaxin–CSN / Xinhai MoU / COP/CLP/PEN skipped;
#   holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 240: us399 / prc370 / allied397 / other91 (n=1257).
shuffle_seed: 20261240
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/rail
- energy/solar
- infrastructure/port_cranes
- infrastructure/building_materials
- resources/graphite
- resources/niobium
- energy/other_renewables
- energy/wind
- infrastructure/port_ownership
- resources/lithium
- infrastructure/engineering_epc
- resources/balsa
- energy/power_plants_grid
- infrastructure/bridges_roads
- energy/fission_smr
- resources/nickel
- resources/copper
- resources/water
rows_found_this_cycle:
  infrastructure/rail: 0
  energy/solar: 0
  infrastructure/port_cranes: 1
  infrastructure/building_materials: 0
  resources/graphite: 0
  resources/niobium: 0
  energy/other_renewables: 0
  energy/wind: 0
  infrastructure/port_ownership: 0
  resources/lithium: 1
  infrastructure/engineering_epc: 0
  resources/balsa: 0
  energy/power_plants_grid: 1
  infrastructure/bridges_roads: 0
  energy/fission_smr: 0
  resources/nickel: 0
  resources/copper: 0
  resources/water: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 1
  other: 0
thin_topup_after_pass:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0
active_after_cycle:
  us: 399
  prc: 370
  allied: 397
  other: 91
  n: 1257
NEXT_QUERY: Cycle 241 shuffle_seed=20261241; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us399/prc370/allied397); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
NEXT_ROW_ID: (follow cycle-241 shuffled_order)
NEXT_LAYER: energy
