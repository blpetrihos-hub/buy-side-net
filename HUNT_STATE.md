updated: 2026-10-05
cycle: 242
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 243 shuffle_seed=20261243; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us403/prc372/allied398); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Generadora Metropolitana Dune Plus USD 629m (Latham) if not nested under PowerChina EPC blank. No U.S. territories.
next_row_id: (follow cycle-243 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 242) ===
# Filled this cycle: Chile×other_renewables NEW×2 (us AES Altos del Sol USD 1.375bn;
#   us AES Llanos del Sol USD 635m); Brazil×other_renewables NEW (prc Sungrow–Roca
#   BESS R$500m); Brazil×power_plants_grid NEW (allied ISA R&M carteira R$7.2bn).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (AES Altos + Llanos NEW + honest residual).
# PRC equal-budget: Sungrow–Roca BESS NEW.

# === Cycle 242 (seed 20261242) ===
# Shuffled order (BRIEF.md numbered + Random(20261242).shuffle): building_materials,
#   niobium, solar, port_ownership, graphite, lithium, power_plants_grid,
#   engineering_epc, nickel, rail, other_renewables, water, balsa, port_cranes, wind,
#   copper, fission_smr, bridges_roads.
# Logged 4 new (2 US / 1 PRC / 1 allied / 0 other; ≥1/3 US hunt budget via AES Altos
#   + Llanos NEW + honest residual):
#   us other_renewables NEW: aes_andes_altos_del_sol_1375m_2024 (USD 1.375bn).
#   us other_renewables NEW: aes_andes_llanos_del_sol_635m_2024 (USD 635m).
#   prc other_renewables NEW: sungrow_roca_bess_400mwh_500m_brl_2025 (~USD 96.30m).
#   allied power_plants_grid NEW: isa_energia_rm_carteira_7p2bn_2026 (~USD 1386.72m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: building_materials, niobium, solar, port_ownership, graphite,
#   lithium, engineering_epc, nickel, rail, water, balsa, port_cranes, wind, copper,
#   fission_smr, bridges_roads
#   (catalog dense; Microsoft Chile USD 3.3bn IDC ecosystem not company CapEx;
#   BYD Camaçari auto archived/out of taxonomy; GATE retain company R$18bn vs press
#   R$23bn; Dune Plus USD 629m Latham hold; Goldwind Sento Sé CapEx undisclosed;
#   COP/CLP/PEN; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 242: us403 / prc372 / allied398 / other91 (n=1264).
shuffle_seed: 20261242
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- resources/niobium
- energy/solar
- infrastructure/port_ownership
- resources/graphite
- resources/lithium
- energy/power_plants_grid
- infrastructure/engineering_epc
- resources/nickel
- infrastructure/rail
- energy/other_renewables
- resources/water
- resources/balsa
- infrastructure/port_cranes
- energy/wind
- resources/copper
- energy/fission_smr
- infrastructure/bridges_roads
rows_found_this_cycle:
  infrastructure/building_materials: 0
  resources/niobium: 0
  energy/solar: 0
  infrastructure/port_ownership: 0
  resources/graphite: 0
  resources/lithium: 0
  energy/power_plants_grid: 1
  infrastructure/engineering_epc: 0
  resources/nickel: 0
  infrastructure/rail: 0
  energy/other_renewables: 3
  resources/water: 0
  resources/balsa: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 1
  other: 0
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 403
  prc: 372
  allied: 398
  other: 91
  n: 1264
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
