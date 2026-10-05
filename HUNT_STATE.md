updated: 2026-10-05
cycle: 245
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 246 shuffle_seed=20261246; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us405/prc375/allied405); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable. No U.S. territories.
next_row_id: (follow cycle-246 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 245) ===
# Filled this cycle: Brazil×rail NEW (us Wabtec Contagem loco line R$150m);
#   Brazil×other_renewables NEW (prc CTG Flex BESS Ilha Solteira R$15m);
#   Brazil×power_plants_grid NEW×3 (allied ISA R&M 1H2026 R$815.4m; allied
#   Neoenergia Cosern R$4.1bn; allied Cosern Tabatinga R$40m nested).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Wabtec Contagem loco line NEW + honest residual).
# PRC equal-budget: CTG Flex BESS NEW.

# === Cycle 245 (seed 20261245) ===
# Shuffled order (BRIEF.md numbered + Random(20261245).shuffle): niobium, wind,
#   building_materials, solar, copper, port_cranes, lithium, power_plants_grid,
#   bridges_roads, port_ownership, rail, graphite, other_renewables, nickel,
#   engineering_epc, water, balsa, fission_smr.
# Logged 5 new (1 US / 1 PRC / 3 allied / 0 other; ≥1/3 US hunt budget via Wabtec
#   Contagem loco line NEW + honest residual):
#   us rail NEW: wabtec_contagem_loco_line_150m_brl_2025 (~USD 28.89m).
#   prc other_renewables NEW: ctg_flex_bess_ilha_solteira_15m_brl_2026 (~USD 2.89m).
#   allied power_plants_grid NEW: isa_energia_rm_815m_brl_1s26 (~USD 157.05m).
#   allied power_plants_grid NEW: neoenergia_cosern_4p1bn_brl_2026_2030 (~USD 789.66m).
#   allied power_plants_grid NEW: neoenergia_cosern_tabatinga_40m_brl_2026 (~USD 7.70m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: niobium, wind, building_materials, solar, copper, port_cranes,
#   lithium, bridges_roads, port_ownership, graphite, nickel, engineering_epc, water,
#   balsa, fission_smr
#   (catalog dense; Pacto Coronel Vivida CapEx is Brazilian distributor; Goldwind
#   Camaçari R$100m already filled; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 245: us405 / prc375 / allied405 / other91 (n=1276).
shuffle_seed: 20261245
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- energy/wind
- infrastructure/building_materials
- energy/solar
- resources/copper
- infrastructure/port_cranes
- resources/lithium
- energy/power_plants_grid
- infrastructure/bridges_roads
- infrastructure/port_ownership
- infrastructure/rail
- resources/graphite
- energy/other_renewables
- resources/nickel
- infrastructure/engineering_epc
- resources/water
- resources/balsa
- energy/fission_smr
rows_found_this_cycle:
  resources/niobium: 0
  energy/wind: 0
  infrastructure/building_materials: 0
  energy/solar: 0
  resources/copper: 0
  infrastructure/port_cranes: 0
  resources/lithium: 0
  energy/power_plants_grid: 3
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 1
  resources/graphite: 0
  energy/other_renewables: 1
  resources/nickel: 0
  infrastructure/engineering_epc: 0
  resources/water: 0
  resources/balsa: 0
  energy/fission_smr: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 3
  other: 0
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 405
  prc: 375
  allied: 405
  other: 91
  n: 1276
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
