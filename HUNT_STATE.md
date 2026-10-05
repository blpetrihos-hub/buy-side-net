updated: 2026-10-05
cycle: 244
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 245 shuffle_seed=20261245; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us404/prc374/allied402); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Neoenergia Cosern Tabatinga R$40m nested; Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable. No U.S. territories.
next_row_id: (follow cycle-245 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 244) ===
# Filled this cycle: Brazil×rail CapEx-fill (us Progress Rail VLI SD70 ~R$200m);
#   Brazil×other_renewables NEW (prc BYD Manaus bus-battery R$50m floor);
#   Brazil×power_plants_grid NEW×2 (allied EDP ES ~R$5bn; allied Neoenergia Cosern
#   Estivas >R$100m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Progress Rail CapEx-fill + honest residual).
# PRC equal-budget: BYD Manaus bus-battery NEW.

# === Cycle 244 (seed 20261244) ===
# Shuffled order (BRIEF.md numbered + Random(20261244).shuffle): bridges_roads,
#   port_ownership, wind, fission_smr, rail, solar, port_cranes, niobium, water,
#   copper, power_plants_grid, building_materials, lithium, other_renewables, nickel,
#   graphite, engineering_epc, balsa.
# Logged 3 new + 1 CapEx-fill (1 US / 1 PRC / 2 allied / 0 other; ≥1/3 US hunt budget
#   via Progress Rail CapEx-fill + honest residual):
#   us rail CapEx-fill: progress_rail_vli_sd70_2026 (~USD 38.52m).
#   prc other_renewables NEW: byd_manaus_bus_battery_50m_brl_2026 (~USD 9.63m).
#   allied power_plants_grid NEW: edp_es_dist_5bn_brl_2025_2030 (~USD 962.99m).
#   allied power_plants_grid NEW: neoenergia_cosern_estivas_100m_brl_2026 (~USD 19.26m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: bridges_roads, port_ownership, wind, fission_smr, solar,
#   port_cranes, niobium, water, copper, building_materials, lithium, nickel, graphite,
#   engineering_epc, balsa
#   (catalog dense; Ascenty Sumaré 3 USD 720m Valor breakout not on company English;
#   Pacto Coronel Vivida CapEx is Brazilian distributor; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 244: us404 / prc374 / allied402 / other91 (n=1271).
shuffle_seed: 20261244
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- infrastructure/port_ownership
- energy/wind
- energy/fission_smr
- infrastructure/rail
- energy/solar
- infrastructure/port_cranes
- resources/niobium
- resources/water
- resources/copper
- energy/power_plants_grid
- infrastructure/building_materials
- resources/lithium
- energy/other_renewables
- resources/nickel
- resources/graphite
- infrastructure/engineering_epc
- resources/balsa
rows_found_this_cycle:
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  energy/wind: 0
  energy/fission_smr: 0
  infrastructure/rail: 1
  energy/solar: 0
  infrastructure/port_cranes: 0
  resources/niobium: 0
  resources/water: 0
  resources/copper: 0
  energy/power_plants_grid: 2
  infrastructure/building_materials: 0
  resources/lithium: 0
  energy/other_renewables: 1
  resources/nickel: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  resources/balsa: 0
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
  prc: 374
  allied: 402
  other: 91
  n: 1271
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
