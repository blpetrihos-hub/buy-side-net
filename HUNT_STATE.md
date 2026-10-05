updated: 2026-10-05
cycle: 250
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 251 shuffle_seed=20261251; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us409/prc379/allied412); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco; Equatorial ADMS company primary if openable; Ascenty Vinhedo/Osasco USD breakouts if company primary opens; Cerro Verde USD 2.1bn life-extension if Freeport/Senace primary opens; TAESA greenfield R$4.3bn if not covered; GATE R$20bn acceleration if State Grid company confirms vs R$18bn. No U.S. territories.
next_row_id: (follow cycle-251 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 250) ===
# Filled this cycle: LatAm×engineering_epc NEW (us Google Cloud LatAm USD 1.2bn);
#   Brazil×power_plants_grid NEW×3 (allied Enel Q1 R$1.5bn; allied ISA autorizado
#   R$12.3bn; other Light SESA ~R$10bn).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Google LatAm NEW).
# PRC equal-budget: honest residual (State Grid/CPFL/SPIC/CTG/PowerChina dense;
#   GATE R$20bn acceleration without company primary vs R$18bn).

# === Cycle 250 (seed 20261250) ===
# Shuffled order (BRIEF.md numbered + Random(20261250).shuffle): other_renewables,
#   port_ownership, wind, power_plants_grid, engineering_epc, nickel, water, graphite,
#   solar, niobium, fission_smr, bridges_roads, balsa, lithium, building_materials,
#   port_cranes, rail, copper.
# Logged 4 new (1 US / 0 PRC / 2 allied / 1 other; ≥1/3 US hunt budget via Google NEW;
#   PRC honest residual):
#   us engineering_epc NEW: google_latam_1p2bn_2022 (USD 1.2bn).
#   allied power_plants_grid NEW: enel_brasil_1p5bn_brl_1q26 (~USD 288.90m).
#   allied power_plants_grid NEW: isa_energia_autorizado_12p3bn_brl_2030 (~USD 2368.98m).
#   other power_plants_grid NEW: light_sesa_10bn_brl_2026_2030 (~USD 1926.00m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: other_renewables, port_ownership, wind, nickel, water, graphite,
#   solar, niobium, fission_smr, bridges_roads, balsa, lithium, building_materials,
#   port_cranes, rail, copper
#   (catalog dense; PRC CapEx exhausted on logged State Grid/CPFL set; thin dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 250: us409 / prc379 / allied412 / other95 (n=1295).
shuffle_seed: 20261250
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- infrastructure/port_ownership
- energy/wind
- energy/power_plants_grid
- infrastructure/engineering_epc
- resources/nickel
- resources/water
- resources/graphite
- energy/solar
- resources/niobium
- energy/fission_smr
- infrastructure/bridges_roads
- resources/balsa
- resources/lithium
- infrastructure/building_materials
- infrastructure/port_cranes
- infrastructure/rail
- resources/copper
rows_found_this_cycle:
  energy/other_renewables: 0
  infrastructure/port_ownership: 0
  energy/wind: 0
  energy/power_plants_grid: 3
  infrastructure/engineering_epc: 1
  resources/nickel: 0
  resources/water: 0
  resources/graphite: 0
  energy/solar: 0
  resources/niobium: 0
  energy/fission_smr: 0
  infrastructure/bridges_roads: 0
  resources/balsa: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  resources/copper: 0
rows_by_side_this_cycle:
  us: 1
  prc: 0
  allied: 2
  other: 1
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 409
  prc: 379
  allied: 412
  other: 95
  n: 1295
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
