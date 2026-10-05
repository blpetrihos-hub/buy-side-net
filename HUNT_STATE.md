updated: 2026-10-05
cycle: 241
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 242 shuffle_seed=20261242; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us401/prc371/allied397); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-242 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 241) ===
# Filled this cycle: Chile×other_renewables NEW (us AES Solar Oriente USD 990m);
#   Antigua×water NEW (us Seven Seas WaaS USD 23m); Brazil×power_plants_grid NEW
#   (prc CTG Ilha+Jupiá mod R$1.5bn spent); Dominican Republic×other_renewables
#   CapEx-fill (allied Acciona La Gina USD 108m dual).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (AES Solar Oriente NEW + Seven Seas NEW + honest residual).
# PRC equal-budget: CTG modernization NEW.

# === Cycle 241 (seed 20261241) ===
# Shuffled order (BRIEF.md numbered + Random(20261241).shuffle): wind, balsa, water,
#   other_renewables, copper, lithium, solar, engineering_epc, power_plants_grid,
#   fission_smr, niobium, graphite, bridges_roads, nickel, port_ownership, port_cranes,
#   building_materials, rail.
# Logged 3 new + 1 CapEx-fill (2 US / 1 PRC / 1 allied / 0 other; ≥1/3 US hunt budget
#   via AES Solar Oriente NEW + Seven Seas NEW + honest residual):
#   us other_renewables NEW: aes_andes_solar_oriente_990m_2024 (USD 990m).
#   us water NEW: seven_seas_antigua_waas_23m_2024 (USD 23m SSWG).
#   prc power_plants_grid NEW: ctg_ilha_jupia_mod_1p5bn_spent_2026 (~USD 288.90m).
#   allied other_renewables CapEx-fill: acciona_la_gina_dr_2026 (USD 108m dual).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: wind, balsa, copper, lithium, solar, engineering_epc,
#   fission_smr, niobium, graphite, bridges_roads, nickel, port_ownership, port_cranes,
#   building_materials, rail
#   (catalog dense; Goldwind Sento Sé CapEx undisclosed; Vestas Dom Inocêncio /
#   Pampas+Cristales / Seven Seas plant COD already loaded; Aldesa EUR / RAP /
#   Huaxin–CSN / Xinhai MoU / COP/CLP/PEN skipped; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 241: us401 / prc371 / allied397 / other91 (n=1260).
shuffle_seed: 20261241
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/wind
- resources/balsa
- resources/water
- energy/other_renewables
- resources/copper
- resources/lithium
- energy/solar
- infrastructure/engineering_epc
- energy/power_plants_grid
- energy/fission_smr
- resources/niobium
- resources/graphite
- infrastructure/bridges_roads
- resources/nickel
- infrastructure/port_ownership
- infrastructure/port_cranes
- infrastructure/building_materials
- infrastructure/rail
rows_found_this_cycle:
  energy/wind: 0
  resources/balsa: 0
  resources/water: 1
  energy/other_renewables: 2
  resources/copper: 0
  resources/lithium: 0
  energy/solar: 0
  infrastructure/engineering_epc: 0
  energy/power_plants_grid: 1
  energy/fission_smr: 0
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  resources/nickel: 0
  infrastructure/port_ownership: 0
  infrastructure/port_cranes: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 1
  other: 0
thin_topup_after_pass:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0
active_after_cycle:
  us: 401
  prc: 371
  allied: 397
  other: 91
  n: 1260
NEXT_QUERY: Cycle 242 shuffle_seed=20261242; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us401/prc371/allied397); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
NEXT_ROW_ID: (follow cycle-242 shuffled_order)
NEXT_LAYER: energy
