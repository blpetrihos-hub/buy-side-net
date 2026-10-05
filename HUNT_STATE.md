updated: 2026-10-05
cycle: 246
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 247 shuffle_seed=20261247; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us406/prc376/allied407); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco. No U.S. territories.
next_row_id: (follow cycle-247 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 246) ===
# Filled this cycle: Brazil×engineering_epc NEW (us Equinix Brazil USD 270m breakout);
#   Brazil×power_plants_grid NEW×3 (prc CPFL RGE R$9.3bn; allied Neoenergia Coelba
#   R$25bn; allied Neoenergia Pernambuco R$9.7bn).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Equinix Brazil NEW + honest residual).
# PRC equal-budget: CPFL RGE NEW.

# === Cycle 246 (seed 20261246) ===
# Shuffled order (BRIEF.md numbered + Random(20261246).shuffle): solar, graphite, wind,
#   fission_smr, rail, bridges_roads, port_cranes, engineering_epc, copper, niobium,
#   nickel, other_renewables, balsa, lithium, building_materials, water,
#   power_plants_grid, port_ownership.
# Logged 4 new (1 US / 1 PRC / 2 allied / 0 other; ≥1/3 US hunt budget via Equinix
#   Brazil NEW + honest residual):
#   us engineering_epc NEW: equinix_brazil_270m_2025_2026 (USD 270m).
#   prc power_plants_grid NEW: cpfl_rge_9p3bn_brl_2025_2029 (~USD 1791.18m).
#   allied power_plants_grid NEW: neoenergia_coelba_25bn_brl_2026_2030 (~USD 4815.01m).
#   allied power_plants_grid NEW: neoenergia_pernambuco_9p7bn_brl_2026_2030 (~USD 1868.22m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: solar, graphite, wind, fission_smr, rail, bridges_roads,
#   port_cranes, copper, niobium, nickel, other_renewables, balsa, lithium,
#   building_materials, water, port_ownership
#   (catalog dense; Progress Rail R$430m Teclemídia conflicts with logged R$200m;
#   Sungrow–BHP no CapEx face; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 246: us406 / prc376 / allied407 / other91 (n=1280).
shuffle_seed: 20261246
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- resources/graphite
- energy/wind
- energy/fission_smr
- infrastructure/rail
- infrastructure/bridges_roads
- infrastructure/port_cranes
- infrastructure/engineering_epc
- resources/copper
- resources/niobium
- resources/nickel
- energy/other_renewables
- resources/balsa
- resources/lithium
- infrastructure/building_materials
- resources/water
- energy/power_plants_grid
- infrastructure/port_ownership
rows_found_this_cycle:
  energy/solar: 0
  resources/graphite: 0
  energy/wind: 0
  energy/fission_smr: 0
  infrastructure/rail: 0
  infrastructure/bridges_roads: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 1
  resources/copper: 0
  resources/niobium: 0
  resources/nickel: 0
  energy/other_renewables: 0
  resources/balsa: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  resources/water: 0
  energy/power_plants_grid: 3
  infrastructure/port_ownership: 0
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
  us: 406
  prc: 376
  allied: 407
  other: 91
  n: 1280
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
