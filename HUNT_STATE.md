updated: 2026-10-05
cycle: 251
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 252 shuffle_seed=20261252; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us411/prc380/allied412); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco; Equatorial ADMS company primary if openable; Ascenty Vinhedo/Osasco USD breakouts if company primary opens; GATE R$20bn acceleration if State Grid company confirms vs R$18bn; Alupar TECP/Lot 7 CapEx if 2T26 PDF opens; KIO QRO2 USD 170m / 2026 >USD 200m nested breakouts if additive clarity needed; KIO QRO3 USD 1.3bn eval if FID. No U.S. territories.
next_row_id: (follow cycle-252 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 251) ===
# Filled this cycle: Brazil×solar NEW (us Atlas Draco BNDES ~R$1bn); LatAm×engineering_epc
#   NEW×2 (us ODATA DeltaFlow USD 630m; other KIO cumulative >USD 900m);
#   Brazil×power_plants_grid NEW×4 (prc CPFL 1H26 R$2.8bn; other TAESA greenfield
#   R$4.3bn; other TAESA FY2025 R$1.783bn; other Alupar growth-cycle R$8.1bn).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Atlas Draco + ODATA DeltaFlow NEW).
# PRC equal-budget: CPFL 1H26 R$2.8bn NEW (State Grid–controlled).

# === Cycle 251 (seed 20261251) ===
# Shuffled order (BRIEF.md numbered + Random(20261251).shuffle): solar,
#   bridges_roads, graphite, building_materials, water, fission_smr, port_ownership,
#   lithium, copper, engineering_epc, nickel, niobium, rail, port_cranes, wind, balsa,
#   other_renewables, power_plants_grid.
# Logged 7 new (2 US / 1 PRC / 0 allied / 4 other; ≥1/3 US hunt budget via Atlas+ODATA;
#   PRC via CPFL 1H26):
#   us solar NEW: atlas_draco_bndes_1bn_brl_2025 (~USD 192.60m).
#   us engineering_epc NEW: odata_deltaflow_630m_2026 (USD 630m).
#   other engineering_epc NEW: kio_cumulative_900m_latam_2026 (USD 900m floor).
#   prc power_plants_grid NEW: cpfl_1h26_capex_2p8bn_brl (~USD 539.28m).
#   other power_plants_grid NEW: taesa_greenfield_4p3bn_brl_aneel (~USD 828.18m).
#   other power_plants_grid NEW: taesa_fy2025_capex_1p783bn_brl (~USD 343.37m).
#   other power_plants_grid NEW: alupar_growth_cycle_8p1bn_brl (~USD 1559.99m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: bridges_roads, graphite, building_materials, water, fission_smr,
#   port_ownership, lithium, copper, nickel, niobium, rail, port_cranes, wind, balsa,
#   other_renewables
#   (catalog dense; Meitner/Wabtec MRS/Equinix already logged; thin dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only. TAESA greenfield HOLD filled.
# Active after cycle 251: us411 / prc380 / allied412 / other99 (n=1302).
shuffle_seed: 20261251
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- infrastructure/bridges_roads
- resources/graphite
- infrastructure/building_materials
- resources/water
- energy/fission_smr
- infrastructure/port_ownership
- resources/lithium
- resources/copper
- infrastructure/engineering_epc
- resources/nickel
- resources/niobium
- infrastructure/rail
- infrastructure/port_cranes
- energy/wind
- resources/balsa
- energy/other_renewables
- energy/power_plants_grid
rows_found_this_cycle:
  energy/solar: 1
  infrastructure/bridges_roads: 0
  resources/graphite: 0
  infrastructure/building_materials: 0
  resources/water: 0
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  resources/lithium: 0
  resources/copper: 0
  infrastructure/engineering_epc: 2
  resources/nickel: 0
  resources/niobium: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  resources/balsa: 0
  energy/other_renewables: 0
  energy/power_plants_grid: 4
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 0
  other: 4
thin_top_up_after_shuffle:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
thin_top_up_rows: 0
active_counts_after_cycle:
  us: 411
  prc: 380
  allied: 412
  other: 99
  n: 1302
thin_subcats_after:
  balsa: 25
  nickel: 26
  fission_smr: 29
  niobium: 30
  graphite: 30
