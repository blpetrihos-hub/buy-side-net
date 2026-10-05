updated: 2026-10-05
cycle: 249
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 250 shuffle_seed=20261250; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us408/prc379/allied410); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco; Equatorial ADMS company primary if openable; Ascenty Vinhedo/Osasco USD breakouts if company primary opens; Light SESA R$10bn if company Material Fact opens; Enel Brasil Q1 2026 R$1.5bn nested spend if not covered by plan rows; ISA Energia autorizado R$12.3bn if distinct from R&M carteira. No U.S. territories.
next_row_id: (follow cycle-250 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 249) ===
# Filled this cycle: Mexico×engineering_epc NEW (us AWS Mexico >USD 5bn);
#   Brazil×power_plants_grid NEW×3 (prc SGBH cumulative >R$30bn; other Cemig R$44bn;
#   other Energisa four-state ~R$18bn).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (AWS Mexico NEW).
# PRC equal-budget: SGBH cumulative CapEx NEW.

# === Cycle 249 (seed 20261249) ===
# Shuffled order (BRIEF.md numbered + Random(20261249).shuffle): nickel, lithium,
#   building_materials, rail, port_ownership, solar, fission_smr, port_cranes,
#   bridges_roads, power_plants_grid, engineering_epc, niobium, water, graphite, wind,
#   copper, balsa, other_renewables.
# Logged 4 new (1 US / 1 PRC / 0 allied / 2 other; ≥1/3 US hunt budget via AWS Mexico NEW):
#   us engineering_epc NEW: aws_mexico_5bn_2025 (USD 5bn floor).
#   prc power_plants_grid NEW: sgbh_cumulative_30bn_brl_2010_2025 (~USD 5776.85m).
#   other power_plants_grid NEW: cemig_capex_plan_44bn_brl_2026_2030 (~USD 8474.41m).
#   other power_plants_grid NEW: energisa_4states_18bn_brl_2026_2030 (~USD 3466.81m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: nickel, lithium, building_materials, rail, port_ownership, solar,
#   fission_smr, port_cranes, bridges_roads, niobium, water, graphite, wind, copper,
#   balsa, other_renewables
#   (catalog dense; CBMM/Progress Rail/holdovers already filled; thin dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 249: us408 / prc379 / allied410 / other94 (n=1291).
shuffle_seed: 20261249
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/nickel
- resources/lithium
- infrastructure/building_materials
- infrastructure/rail
- infrastructure/port_ownership
- energy/solar
- energy/fission_smr
- infrastructure/port_cranes
- infrastructure/bridges_roads
- energy/power_plants_grid
- infrastructure/engineering_epc
- resources/niobium
- resources/water
- resources/graphite
- energy/wind
- resources/copper
- resources/balsa
- energy/other_renewables
rows_found_this_cycle:
  resources/nickel: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  energy/fission_smr: 0
  infrastructure/port_cranes: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 3
  infrastructure/engineering_epc: 1
  resources/niobium: 0
  resources/water: 0
  resources/graphite: 0
  energy/wind: 0
  resources/copper: 0
  resources/balsa: 0
  energy/other_renewables: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 0
  other: 2
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 408
  prc: 379
  allied: 410
  other: 94
  n: 1291
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
