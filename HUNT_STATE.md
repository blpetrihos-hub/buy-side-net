updated: 2026-10-05
cycle: 253
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 254 shuffle_seed=20261254; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us415/prc380/allied415); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco; Equatorial ADMS company primary if openable; Ascenty Vinhedo/Osasco USD breakouts if company primary opens; GATE R$20bn acceleration if State Grid company confirms vs R$18bn; Alupar TECP/Lot 7 CapEx if 2T26 PDF opens; Ada Franco da Rocha R$2.7bn if company CapEx figure opens; Scala FY2025 CapEx if sustainability R$4.7bn reconciles to DFS; KIO QRO2/2026 nested breakouts; Grenergy €3.7bn Chile ~45% if separable primary; Copel 1S26 R$1.5388bn if full earnings-release PDF opens beyond 2T26 presentation. No U.S. territories.
next_row_id: (follow cycle-254 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 253) ===
# Filled this cycle: LatAm×engineering_epc NEW×1 (us Cirion >USD 300m);
#   Brazil×building_materials NEW×2 (other Gerdau FY2025 R$6.1bn; other 2026 plan R$4.7bn);
#   Brazil×power_plants_grid NEW×2 (allied Neoenergia 1T26 R$1.8bn; other Copel 2T26 R$957.2m);
#   Brazil×water NEW×1 (other Aegea 6M26 R$832m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Cirion NEW).
# PRC equal-budget: honest residual (BYD/Goldwind/SPIC/CTG/CPFL CapEx already dense).

# === Cycle 253 (seed 20261253) ===
# Shuffled order (BRIEF.md numbered + Random(20261253).shuffle): port_ownership,
#   building_materials, niobium, copper, balsa, water, graphite, engineering_epc,
#   lithium, port_cranes, rail, solar, power_plants_grid, bridges_roads, wind,
#   other_renewables, nickel, fission_smr.
# Logged 6 new (1 US / 0 PRC / 1 allied / 4 other; ≥1/3 US hunt budget via Cirion;
#   PRC honest residual):
#   us engineering_epc NEW: cirion_latam_300m_2024 (USD 300m soft floor).
#   other building_materials NEW: gerdau_fy2025_capex_6p1bn_brl (~USD 1174.86m).
#   other building_materials NEW: gerdau_2026_capex_plan_4p7bn_brl (~USD 905.22m).
#   allied power_plants_grid NEW: neoenergia_1t26_capex_1p8bn_brl (~USD 346.68m).
#   other power_plants_grid NEW: copel_2t26_capex_957p2m_brl (~USD 184.36m).
#   other water NEW: aegea_6m26_capex_832m_brl (~USD 160.24m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: port_ownership, niobium, copper, balsa, graphite, lithium,
#   port_cranes, rail, solar, bridges_roads, wind, other_renewables, nickel,
#   fission_smr (catalog dense; PRC CapEx dense on logged set; thin dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 253: us415 / prc380 / allied415 / other104 (n=1314).

# === Cycle 252 (seed 20261252) summary ===
# Logged 6 new (3 US / 0 PRC / 2 allied / 1 other). Active after: us414/prc380/allied414/other100 (n=1308).

shuffle_seed: 20261253
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_ownership
- infrastructure/building_materials
- resources/niobium
- resources/copper
- resources/balsa
- resources/water
- resources/graphite
- infrastructure/engineering_epc
- resources/lithium
- infrastructure/port_cranes
- infrastructure/rail
- energy/solar
- energy/power_plants_grid
- infrastructure/bridges_roads
- energy/wind
- energy/other_renewables
- resources/nickel
- energy/fission_smr
rows_found_this_cycle:
  infrastructure/port_ownership: 0
  infrastructure/building_materials: 2
  resources/niobium: 0
  resources/copper: 0
  resources/balsa: 0
  resources/water: 1
  resources/graphite: 0
  infrastructure/engineering_epc: 1
  resources/lithium: 0
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  energy/solar: 0
  energy/power_plants_grid: 2
  infrastructure/bridges_roads: 0
  energy/wind: 0
  energy/other_renewables: 0
  resources/nickel: 0
  energy/fission_smr: 0
rows_by_side_this_cycle:
  us: 1
  prc: 0
  allied: 1
  other: 4
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 415
  prc: 380
  allied: 415
  other: 104
  n: 1314
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
